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


