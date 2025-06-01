function button(){
    let main = document.getElementById("main")
    let p = document.createElement('p')
    let element = document.createElement("button")
    let text = document.createTextNode("Hello My Name Is Sanan")
    let text2 = document.createTextNode("I am 14 years old")
    
    main.appendChild(p)
    main.appendChild(element)
    p.appendChild(text)
    element.appendChild(text2)

    
}