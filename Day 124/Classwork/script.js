let f = document.getElementById('f')
let e = document.getElementById('e')
let p = document.getElementById('p')

f.onsubmit = function (event) {
    event.preventDefault()
    console.log('Email: ' + e.value + ', Password: ' + p.value)
}

let imgs = [
    'img/Image1.png',
    'img/Image2.png',
    'img/Image3.png',
]


let i = 0
let imgTag = document.getElementById('img')
imgTag.src = imgs[i]

document.getElementById('prev').onclick = function () {
    i--
    if (i < 0) i = imgs.length - 1
    imgTag.src = imgs[i]
}

document.getElementById('next').onclick = function () {
    i++
    if (i >= imgs.length) i = 0
    imgTag.src = imgs[i]
}
