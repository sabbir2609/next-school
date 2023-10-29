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
    }, 10000)

})


// Sidebar toggle


const sidebarToggle = document.getElementById('sidebar-toggle');
sidebarToggle.addEventListener("click", function () {
    document.getElementById("sidebar").classList.toggle("collapsed");
});


// theme toggle

document.querySelector(".theme-toggle").addEventListener("click", () => {
    toggleLocalStorage();
    toggleRootClass();
});

function toggleRootClass() {
    const current = document.documentElement.getAttribute("data-bs-theme");
    const inverted = current == "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-bs-theme", inverted);
}

function toggleLocalStorage() {
    if (isLight()) {
        localStorage.removeItem("light");
    } else {
        localStorage.setItem("light", "set");
    }
}

function isLight() {
    return localStorage.getItem("light");
}

if (isLight()) {
    toggleRootClass();
}

