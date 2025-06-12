const container1 = document.getElementById('container1')
const parentdiv = document.createElement('div')
const childspan = document.createElement('span')
childspan.textContent = 'child'
parentdiv.appendChild(childspan)
container1.appendChild(parentdiv)

const container2 = document.getElementById('container2')
const paragraph = document.getElementById('paragraph')
container2.removeChild(paragraph)

function onmouseenter() {
  console.log(5)
}

function onmouseleave() {
  console.log(10)
}

const container3 = document.getElementById('container3')
const newparagraph = document.createElement('p')
newparagraph.textContent = 'new'
const oldbutton = document.getElementById('oldbutton')
container3.replaceChild(newparagraph, oldbutton)
