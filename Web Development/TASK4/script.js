document.addEventListener("DOMContentLoaded", function () {
    const sections = document.querySelectorAll(".slide-in");
    const options = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver(function (entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }
        });
    }, options);

    sections.forEach(section => {
        observer.observe(section);
    });

    // Background Animation
    const body = document.body;
    function createBackgroundAnimation() {
        const star = document.createElement("div");
        star.classList.add("star");
        star.style.left = `${Math.random() * 100}vw`;
        star.style.animationDuration = `${Math.random() * 3 + 2}s`;
        body.appendChild(star);
        setTimeout(() => star.remove(), 5000);
    }
    setInterval(createBackgroundAnimation, 200);

    // Smooth Scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute("href")).scrollIntoView({
                behavior: "smooth"
            });
        });
    });

    // Navbar Scroll Effect
    const navbar = document.querySelector("nav ul");
    window.addEventListener("scroll", function () {
        if (window.scrollY > 50) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }
    });

    // Dark Mode Toggle
    const toggleBtn = document.createElement("button");
    toggleBtn.innerText = "Toggle Dark Mode";
    toggleBtn.style.position = "fixed";
    toggleBtn.style.bottom = "20px";
    toggleBtn.style.right = "20px";
    toggleBtn.style.padding = "10px 20px";
    toggleBtn.style.cursor = "pointer";
    body.appendChild(toggleBtn);

    toggleBtn.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode");
    });
});
