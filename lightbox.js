const lightbox = document.getElementById("lightbox");
const lightboxImage = document.getElementById("lightbox-image");

function closeLightbox() {
  lightbox.hidden = true;
  document.body.classList.remove("lightbox-open");
  lightboxImage.src = "";
}

document.querySelectorAll(".gallery-item").forEach((item) => {
  item.addEventListener("click", () => {
    lightboxImage.src = item.dataset.fullImage;
    lightboxImage.alt = item.querySelector("img").alt;
    lightbox.hidden = false;
    document.body.classList.add("lightbox-open");
  });
});

document.querySelector(".lightbox-close").addEventListener("click", closeLightbox);
lightbox.addEventListener("click", (event) => {
  if (event.target === lightbox) closeLightbox();
});
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !lightbox.hidden) closeLightbox();
});
