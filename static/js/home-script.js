// JavaScript for the scroll-to-top button
const scrollToTopBtn = document.getElementById("scrollToTopBtn");

// Show or hide the button based on scroll position
window.addEventListener("scroll", () => {
    if (window.scrollY > 100) {
        scrollToTopBtn.style.display = "block";
    } else {
        scrollToTopBtn.style.display = "none";
    }
});

// Scroll to the top when the button is clicked
scrollToTopBtn.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth", // Smooth scrolling animation
    });
});


// Function to show the floating button when scrolling down
window.addEventListener('scroll', function() {
    const floatingButton = document.querySelector('.floating-language-button');
    if (window.scrollY > 100) {
        floatingButton.style.display = 'block';
    } else {
        floatingButton.style.display = 'none';
    }
});

// <!-- Custom JavaScript to change language -->

function changeLanguage(language) {
    const translatedText = {
        'Bangla': 'বিশ্বাস করুন, স্কুলের জন্য একটি স্মার্ট সমাধান',
        'English': 'Believe in a smart solution for school'
    };

    document.getElementById('translatedText').innerText = translatedText[language];
    document.querySelector('.language-picker button').innerHTML = `${language}`;

    event.preventDefault();
}