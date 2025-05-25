let photo = document.getElementById('photo');
let title = document.getElementById('title');

function changeWidth() {
  photo.style.width = '400px';
}

function changeHeight() {
  photo.style.height = '400px';
}

function changeRadius() {
  photo.style.borderRadius = '30px';
}

function toggleShadow() {
  photo.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.5)';
}

function changeColor() {
  title.style.color = 'blue';
}

function changeFontSize() {
  title.style.fontSize = '48px';
}
