// Sélectionner les éléments à modifier
var body = document.getElementById('main');
var toggleBtn = document.getElementById("btn_mode");

// Fonction pour activer le mode "clair"
function activateLightMode() {
  body.classList.remove('bg-dark');
  body.classList.remove('text-light');
  body.classList.add('bg-light');
  body.classList.add('text-dark');
  toggleBtn.innerText = "Dark Mode";
}

// Fonction pour activer le mode "sombre"
function activateDarkMode() {
  body.classList.remove('bg-light');
  body.classList.remove('text-dark');
  body.classList.add('bg-dark');
  body.classList.add('text-light');
  toggleBtn.innerText = "Light Mode";
}

// Ajouter un écouteur d'événement sur le bouton de basculement
toggleBtn.addEventListener("click", function() {
  // Vérifier si le mode sombre est activé
  if (body.classList.contains("dark-mode")) {
    // Désactiver le mode sombre
    body.classList.remove("dark-mode");
    activateLightMode();
  } else {
    // Activer le mode sombre
    body.classList.add("dark-mode");
    activateDarkMode();
  }
});

// Vérifier si le mode sombre est déjà activé
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
  body.classList.add("dark-mode");
  activateDarkMode();
}
