// Get all the toast elements
var toastElList = [].slice.call(document.querySelectorAll('.toast'))

// Create a new Toast object for each toast element
var toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl)
})

// Add an event listener to the close button of each toast element
toastElList.forEach(function (toastEl, index) {
    var closeButton = toastEl.querySelector('.btn-close')
    closeButton.addEventListener('click', function () {
        toastList[index].hide()
    })

    // auto hide toast after 5 seconds
    setTimeout(function () {
        toastList[index].hide()
    }, 5000)

})


// Sidebar toggle


const sidebar = document.getElementById('sidebar');

// Function to handle clicks outside the sidebar
document.addEventListener('click', function (event) {
    const isClickInside = sidebar.contains(event.target);
    const isClickOnSidebarToggle = event.target.closest('#sidebar-toggle');

    if (!isClickInside && !isClickOnSidebarToggle && window.innerWidth <= 682) {
        sidebar.classList.remove('toggle');
    }
});

// Sidebar toggle button functionality
const sidebarToggle = document.getElementById('sidebar-toggle');
sidebarToggle.addEventListener('click', function () {
    sidebar.classList.toggle('toggle');
});



// theme toggle
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

