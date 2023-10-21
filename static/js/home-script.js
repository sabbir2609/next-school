// JavaScript for the scroll-to-top button
// const scrollToTopBtn = document.getElementById("scrollToTopBtn");

// Show or hide the button based on scroll position
// window.addEventListener("scroll", () => {
//     if (window.scrollY > 100) {
//         scrollToTopBtn.style.display = "block";
//     } else {
//         scrollToTopBtn.style.display = "none";
//     }
// });

// Scroll to the top when the button is clicked
// scrollToTopBtn.addEventListener("click", () => {
//     window.scrollTo({
//         top: 0,
//         behavior: "smooth", // Smooth scrolling animation
//     });
// });


// Function to show the floating button when scrolling down
// window.addEventListener('scroll', function () {
//     const floatingButton = document.querySelector('.floating-language-button');
//     if (window.scrollY > 100) {
//         floatingButton.style.display = 'block';
//     } else {
//         floatingButton.style.display = 'none';
//     }
// });

// <!-- Custom JavaScript to change language -->

// function changeLanguage(language) {
//     const translatedText = {
//         'Bangla': 'স্কুলের জন্য একটি স্মার্ট সমাধানে বিশ্বাস করুন !',
//         'English': 'Believe in a smart solution for school'
//     };

//     document.getElementById('translatedText').innerText = translatedText[language];
//     document.querySelector('.language-picker button').innerHTML = `${language}`;

//     event.preventDefault();
// }


// Add scroll event listener to the gallery container
const imageGalleryContainer = document.getElementById("imageGalleryContainer");
imageGalleryContainer.addEventListener("wheel", (event) => {
    if (event.deltaY !== 0) {
        event.preventDefault();
        imageGalleryContainer.scrollBy({
            left: event.deltaY,
        });
    }
});


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
