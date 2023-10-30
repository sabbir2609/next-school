window.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("data-bs-theme");
    const body = document.querySelector("body");
    const icon = document.getElementById("dark-mode-icon");

    if (savedTheme === "dark") {
        body.setAttribute("data-bs-theme", "dark");
        icon.classList.remove("fa-moon");
        icon.classList.add("fa-sun");
    } else {
        body.setAttribute("data-bs-theme", "light");
        icon.classList.remove("fa-sun");
        icon.classList.add("fa-moon");
    }
});

function toggleDarkMode() {
    const body = document.querySelector("body");
    const currentTheme = body.getAttribute("data-bs-theme");
    const icon = document.getElementById("dark-mode-icon");

    if (currentTheme === "light") {
        // Switch to dark mode
        body.setAttribute("data-bs-theme", "dark");
        icon.classList.remove("fa-moon");
        icon.classList.add("fa-sun");
        localStorage.setItem("data-bs-theme", "dark");
    } else {
        // Switch to light mode
        body.setAttribute("data-bs-theme", "light");
        icon.classList.remove("fa-sun");
        icon.classList.add("fa-moon");
        localStorage.setItem("data-bs-theme", "light");
    }
}


// Scroll to top button
function scrollToTop() {
    window.scrollTo(0, 0);

}


// FAB options
function toggleFabOptions() {
    var fabToggle = document.querySelector(".fab-toggle");
    var fabOptions = document.querySelector(".fab-options");

    fabToggle.classList.toggle("active");
    fabOptions.classList.toggle("active");
}

// Add an event listener to close FAB options when clicking outside
document.body.addEventListener("click", function (event) {
    var fabOptions = document.querySelector(".fab-options");
    var fabToggle = document.querySelector(".fab-toggle");
    if (fabOptions.classList.contains("active") && !event.target.closest(".fab-container")) {
        fabOptions.classList.remove("active");
        fabToggle.classList.remove("active");
    }
});

// Add scroll event listener to the gallery container
// const imageGalleryContainer = document.getElementById("imageGalleryContainer");
// imageGalleryContainer.addEventListener("wheel", (event) => {
//     if (event.deltaY !== 0) {
//         imageGalleryContainer.scrollBy({
//             left: event.deltaY,
//         });
//     }
// }, { passive: false });


var multipleCardCarousel = document.querySelector("#customCarousel");

if (window.matchMedia("(min-width: 576px)").matches) {
    var carousel = new bootstrap.Carousel(multipleCardCarousel, {
        interval: false
    });
    var carouselInner = multipleCardCarousel.querySelector(".carousel-inner");
    var carouselWidth = carouselInner.scrollWidth;
    var cardWidth = multipleCardCarousel.querySelector(".carousel-item").offsetWidth;
    var scrollPosition = 0;
    var animationFrameId;
    var animationDuration = 600; // Animation duration in milliseconds
    var reachedEnd = false;

    multipleCardCarousel.querySelector(".carousel-control-next").addEventListener("click", function () {
        if (reachedEnd) {
            scrollPosition = -250; // If at the end, scroll back to the start
            reachedEnd = false;
        } else {
            var remainingWidth = carouselWidth - scrollPosition;
            var targetScrollPosition = scrollPosition + Math.min(300, remainingWidth);
            if (targetScrollPosition >= carouselWidth - cardWidth * 2) {
                reachedEnd = true;
            }
            animateScroll(targetScrollPosition);
        }
    });

    multipleCardCarousel.querySelector(".carousel-control-prev").addEventListener("click", function () {
        var targetScrollPosition = Math.max(0, scrollPosition - 300);
        animateScroll(targetScrollPosition);
    });

    function animateScroll(targetPosition) {
        var startTime;

        function step(currentTime) {
            if (!startTime) startTime = currentTime;
            var progress = (currentTime - startTime) / animationDuration;
            if (progress < 1) {
                scrollPosition = scrollPosition + (targetPosition - scrollPosition) * progress;
                carouselInner.scrollLeft = scrollPosition;
                animationFrameId = requestAnimationFrame(step);
            } else {
                scrollPosition = targetPosition;
                carouselInner.scrollLeft = scrollPosition;
            }
        }

        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }

        requestAnimationFrame(step);
    }
} else {
    multipleCardCarousel.classList.add("slide");
}
