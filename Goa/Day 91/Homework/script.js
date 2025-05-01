function calculateBMI() {
    
    let weight = document.getElementById('weight').value
    let height = document.getElementById('height').value
    let result = document.getElementById('bmi') 
    
    weight = parseFloat(weight)
    height = parseFloat(height)
    
    height = height / 100
    let bmi = weight / (height * height)

    result.innerHTML = "თქვენი BMI არის: " + bmi.toFixed(2)
    
}