// Form
let f = document.getElementById('f')
let n = document.getElementById('n')
let a = document.getElementById('a')

f.addEventListener('submit', function(e){
    e.preventDefault()
    console.log('გამარჯობა ' + n.value + ', შენ ხარ ' + a.value + ' წლის')
})

// Password
let p = document.getElementById('p')
let s = document.getElementById('s')
let l = document.getElementById('l')

s.addEventListener('change', function(){
    if(s.checked) p.type = 'text'
    else p.type = 'password'
})

l.addEventListener('click', function(){
    console.log('პაროლი: ' + p.value)
})

// Counter
let c = 0
let cv = document.getElementById('c')
let plus = document.getElementById('plus')
let minus = document.getElementById('minus')
let r = document.getElementById('r')

plus.addEventListener('click', function(){
    c++
    cv.textContent = c
})

minus.addEventListener('click', function(){
    if(c>0) c--
    cv.textContent = c
})

r.addEventListener('click', function(){
    c=0
    cv.textContent = c
})

let box = document.getElementById('box')
let cols = document.querySelectorAll('.col')

for (let i = 0; i < cols.length; i++) {
    cols[i].onclick = function() {
        box.style.background = cols[i].getAttribute('data-color')
        console.log('ფერი: ' + cols[i].getAttribute('data-color'))
    }
}
