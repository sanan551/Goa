const pageTitle = document.getElementById('pageTitle');
const registerForm = document.getElementById('registerForm');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const confirmBtn = document.getElementById('confirmBtn');

registerForm.addEventListener('submit', function (event) {
    event.preventDefault(); 
    const username = usernameInput.value.trim();

    if (!username) {
        usernameInput.focus();
        return;
    }
    
    registerForm.remove();
    pageTitle.textContent = `Welcome ${username}`;

    const sub = document.createElement('p');
    sub.textContent = 'რეგისტრაცია წარმატებით დასრულდა.';
    sub.style.marginTop = '12px';
    sub.style.color = '#444';

    document.querySelector('.card').appendChild(sub);
    
    const pw = passwordInput.value; 
    console.log('Registered user:', username, 'password length:', pw.length);
});
