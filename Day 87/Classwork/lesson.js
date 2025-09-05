let password = 'group 39'
let attempt = ''

while (attempt !== password) {
    attempt = prompt('Enter the password')
    if (attempt === password) {
        alert('Welcome!')
    } else {
        alert('Incorrect password, try again.')
    }
}
