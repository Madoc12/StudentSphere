document.addEventListener("DOMContentLoaded", () => {
  const menuItems = document.querySelectorAll(".menu li");
  const content = document.querySelector("#content");

  // 🔹 Handle active state
  menuItems.forEach((item) => {
    item.addEventListener("click", async (e) => {
      e.preventDefault();

      // remove active class from all
      menuItems.forEach((i) => i.classList.remove("active"));
      item.classList.add("active");

      // 🔹 Find the <a> tag inside this menu item
      const link = item.querySelector("a");
      if (!link) return;

      const url = link.dataset.url;
      if (!url) return; // skip if no data-url

      try {
        // 🔹 Fetch the new page content (AJAX)
        const response = await fetch(url, {
          headers: { "X-Requested-With": "XMLHttpRequest" },
        });

        const html = await response.text();

        // 🔹 Replace only the main content area
        content.innerHTML = html;
      } catch (error) {
        console.error("Error loading page:", error);
      }
    });
  });
});
  // 🔹 Hover effects


  menuItems.forEach((item) => {
    item.addEventListener("mouseenter", (e) => {
      const highlight = document.createElement("div");
      highlight.classList.add("highlight");
      highlight.style.position = "absolute";
      highlight.style.top = "0";
      highlight.style.left = "0";
      highlight.style.width = "100%";
      highlight.style.height = "100%";
      highlight.style.borderRadius = "16px";
      highlight.style.background =
        "radial-gradient(circle at " +
        e.offsetX +
        "px " +
        e.offsetY +
        "px, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0) 70%)";
      highlight.style.pointerEvents = "none";

      item.appendChild(highlight);

      setTimeout(() => {
        highlight.style.opacity = "0";
        setTimeout(() => {
          item.removeChild(highlight);
        }, 300);
      }, 500);
    });
  });

  const cards = document.querySelectorAll(".card");
  cards.forEach((card) => {
    card.addEventListener("mousemove", (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const rotateY = (x / rect.width - 0.5) * 10;
      const rotateX = (y / rect.height - 0.5) * -10;

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.05)`;
    });

    card.addEventListener("mouseleave", () => {
      card.style.transform = "translateY(0) scale(1)";
      card.style.transition = "transform 0.5s ease";
    });
  });
