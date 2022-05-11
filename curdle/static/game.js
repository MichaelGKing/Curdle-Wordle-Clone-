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

//Removes
$(document).ready(function () {
  $("#button").click(function () {
    $("#result-"+guessNum).fadeOut("slow");
  });
});

let cheeseList = ["Cheddar", "Camembert", "Parmesan", "Red Leicester", "Blue Cheese"];

function removeText() {
  document.getElementById("cheese-choice").value = "";
}

/**
 * Functions tests if entry is valid entry and performs followup functions.
 */
function entryTest() {
  let entry = document.getElementById("cheese-choice").value;
  let validEntry = false;
  for (let i = 0; i < cheeseList.length; i++) {
    if (entry == cheeseList[i]) {
      validEntry = true;
    }
  }

  if (validEntry == false) {

  }

  if (validEntry == true) {
    removeText();
  }
}