
// document.getElementById('show-password-checkbox').addEventListener('change', function () {
//     var passwordInput = document.getElementById('password');
//     var confirmPasswordInput = document.getElementById('confirm-password');
//     if (this.checked) {
//         passwordInput.type = 'text';
//         confirmPasswordInput.type = 'text';
//     } else {
//         passwordInput.type = 'password';
//         confirmPasswordInput.type = 'confirm-password';
//     }
// });

// document.getElementById('show-password-checkbox').addEventListener('change', function () {
//     var passwordInput = document.getElementById('password');
//     var confirmPasswordInput = document.getElementById('confirm-password');

//     passwordInput.type = confirmPasswordInput.type = this.checked ? 'text' : 'password';
// });

document.getElementById('show-password-checkbox').addEventListener('change', function () {
    var passwordInput = document.getElementById('password');
    var confirmPasswordInput = document.getElementById('confirm-password'); // Check if exists

    passwordInput.type = this.checked ? 'text' : 'password';

    if (confirmPasswordInput) {
        confirmPasswordInput.type = this.checked ? 'text' : 'password';
    }
});
