document.addEventListener("DOMContentLoaded", function () {
    // Background Animation
    function createBackgroundAnimation() {
        const particle = document.createElement("div");
        particle.classList.add("particle");
        particle.style.left = `${Math.random() * 100}vw`;
        particle.style.animationDuration = `${Math.random() * 3 + 2}s`;
        document.getElementById("background-animation").appendChild(particle);
        setTimeout(() => particle.remove(), 5000);
    }
    setInterval(createBackgroundAnimation, 200);

    // Fetch Weather by City
    async function fetchWeather(city) {
        const apiKey = "YOUR_API_KEY_HERE"; 
        const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

        try {
            const response = await fetch(url);
            const data = await response.json();
            displayWeather(data);
        } catch (error) {
            document.getElementById("weatherResult").innerHTML = "Error fetching weather data.";
        }
    }

    document.getElementById("getWeather").addEventListener("click", function () {
        const city = document.getElementById("cityInput").value;
        fetchWeather(city);
    });

    // Fetch Weather by Location
    document.getElementById("getLocationWeather").addEventListener("click", function () {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(async function (position) {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                const apiKey = "YOUR_API_KEY_HERE";
                const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric`;

                try {
                    const response = await fetch(url);
                    const data = await response.json();
                    displayWeather(data);
                } catch (error) {
                    document.getElementById("weatherResult").innerHTML = "Error fetching location weather data.";
                }
            });
        } else {
            document.getElementById("weatherResult").innerHTML = "Geolocation not supported.";
        }
    });

    // Display Weather Data
    function displayWeather(data) {
        document.getElementById("weatherResult").innerHTML = `
            <h2>${data.name}</h2>
            <p>Temperature: ${data.main.temp}°C</p>
            <p>Condition: ${data.weather[0].description}</p>
        `;
    }
});
