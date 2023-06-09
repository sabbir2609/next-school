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


// select2 widget for student dropdown in assign_student.html

$(document).ready(function () {
    $('#id_student').select2();
    $('#id_section').select2();
});