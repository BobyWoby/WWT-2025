

document.body.style.display = "flex";
document.body.style.justifyContent = "center";
document.body.style.alignItems = "center";
document.body.style.height = "100vh";
document.body.style.margin = "0";

const square = document.createElement("div");
square.style.width = "200px";
square.style.height = "200px";
square.style.backgroundColor = "white";
square.style.display = "flex";
square.style.justifyContent = "center";
square.style.alignItems = "center";
square.style.border = "1px solid black";

const text = document.createElement("p");
text.innerText = "This is a test";
text.style.fontSize = "12pt";
text.style.fontFamily = "Arial";

square.appendChild(text);
document.body.appendChild(square);


console.log("This is a test for a spoof website");