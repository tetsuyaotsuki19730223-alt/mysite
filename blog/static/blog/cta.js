document.addEventListener("DOMContentLoaded", function () {
    const cta = document.getElementById("scroll-cta");
    if (!cta) return;

    let shown = false;

    window.addEventListener("scroll", function () {
        if (shown) return;

        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollRate = scrollTop / docHeight;

        if (scrollRate > 0.8) {
            cta.classList.remove("hidden");
            shown = true;
        }
    });
});

document.querySelectorAll(".subscribe-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.getElementById("modal-post-title").innerText =
      `「${btn.dataset.postTitle}」を読むには購読が必要です`;

    document.getElementById("subscribe-modal").classList.remove("hidden");
  });
});

document.getElementById("close-modal").addEventListener("click", () => {
  document.getElementById("subscribe-modal").classList.add("hidden");
});
