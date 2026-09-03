from pathlib import Path

from PIL import Image, ImageOps
from pillow_heif import register_heif_opener


MAX_SIZE = 1024
JPEG_QUALITY = 88


def convert_images(image_directory: Path) -> int:
    register_heif_opener()
    converted_count = 0

    for source_path in sorted(image_directory.iterdir()):
        if source_path.suffix.lower() not in {".heic", ".heif"}:
            continue

        target_path = source_path.with_suffix(".jpg")
        with Image.open(source_path) as image:
            image = ImageOps.exif_transpose(image)
            image.thumbnail((MAX_SIZE, MAX_SIZE), Image.Resampling.LANCZOS)

            if image.mode not in {"RGB", "L"}:
                image = image.convert("RGB")

            image.save(
                target_path,
                format="JPEG",
                quality=JPEG_QUALITY,
                optimize=True,
            )

        converted_count += 1
        print(f"Converted: {source_path.name} -> {target_path.name}")

    return converted_count


if __name__ == "__main__":
    images_directory = Path(__file__).parent / "images"
    converted_count = convert_images(images_directory)
    print(f"Converted {converted_count} image(s).")
