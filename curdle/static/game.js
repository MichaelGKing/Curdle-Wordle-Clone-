let cheese = ["Cheddar", "Cow", "Type-5", "false"];
let guessNum = 1;

let correctName = false;
let correctAnimal = false;
let correctType = false;
let correctMold = false;

function resultArray() {
  let guess = document.getElementById("cheese-choice").value;
  guessedCheese = ["Cheddar", "Cow", "Type-5", "false"];
  return guessedCheese;
}

$(document).ready(function () {
  $("#button").click(function () {
    $("#result-"+guessNum).fadeOut("slow");
  });
});