 function convertToFahren() {
      let celsius = document.getElementById("celsius").value;
      let fahren = (celsius * 9/5) + 32;
      document.getElementById("result").innerText = celsius + "°C არის " + fahren + "°F";
}