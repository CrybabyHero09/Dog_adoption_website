document.addEventListener("DOMContentLoaded", function () {
      const hamburger = document.getElementById("hamburger");
      const dropdown = document.getElementById("dropdown");

      hamburger.addEventListener("click", function () {
        dropdown.classList.toggle("show");
      });
    });

function goToLogin() {
  window.location.href = "/login";
}

function goToSignup() {
  window.location.href = "/signup";
}
