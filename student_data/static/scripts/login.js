// Toggle between log in and sign up views
document.querySelectorAll('.info-item .btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
        var container = document.querySelector('.container');
        container.classList.toggle('log-in');
    });
});

// Handle form submissions (log in or sign up buttons)
document.querySelectorAll('.container-form .btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
        var container = document.querySelector('.container');
        container.classList.add('active');
    });
});
