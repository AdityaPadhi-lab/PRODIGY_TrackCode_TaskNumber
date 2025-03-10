window.addEventListener("scroll", function() {
    var navbar = document.getElementById("navbar");
    if (window.scrollY > 50) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
});window.addEventListener("scroll", function() {
    var navbar = document.getElementById("navbar");
    if (window.scrollY > 50) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
});

document.querySelectorAll(".nav-links a").forEach(link => {
    link.addEventListener("mouseover", function() {
        this.style.color = "#FFD700";
        this.style.transform = "scale(1.1)";
    });
    link.addEventListener("mouseout", function() {
        this.style.color = "white";
        this.style.transform = "scale(1)";
    });
});
