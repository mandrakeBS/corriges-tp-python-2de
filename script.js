// === Basculer clair/sombre ===
function toggleMode() {
  const body = document.body;
  const dark = body.classList.toggle("dark-mode");
  localStorage.setItem("theme", dark ? "dark" : "light");

  const btn = document.getElementById("theme-toggle");
  if (btn) btn.textContent = dark ? "🌙" : "☀️";
}

// === Rétablir le thème choisi au chargement ===
window.addEventListener("DOMContentLoaded", () => {
  const stored = localStorage.getItem("theme");
  if (stored === "dark") document.body.classList.add("dark-mode");

  const btn = document.getElementById("theme-toggle");
  if (btn) btn.textContent = document.body.classList.contains("dark-mode") ? "🌙" : "☀️";

  // Activer les boutons "Afficher / masquer"
  document.querySelectorAll("button[data-target]").forEach(btn => {
    btn.addEventListener("click", () => {
      const id = btn.getAttribute("data-target");
      const corr = document.getElementById(id);
      if (corr) corr.classList.toggle("visible");
    });
  });
});
