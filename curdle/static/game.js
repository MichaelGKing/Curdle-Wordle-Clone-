let cheese = ["Cheddar", "Cow", "Type-5", "false"];
let cheeseList = ["Cheddar", "Camembert", "Parmesan", "Red Leicester", "Blue Cheese"];
let resultNum = 1;

let correctName = false;
let correctAnimal = false;
let correctType = false;
let correctMold = false;

function resultArray() {
  let guess = document.getElementById("cheese-choice").value;
  guessedCheese = ["Cheddar", "Cow", "Type-5", "false"];
  return guessedCheese;
}

/**
 * Function generates results box.
 */
function resultGen() {

}


/**
 * Function removes text from the text input box.
 */
function removeText() {
  document.getElementById("cheese-choice").value = "";
}

/**
 * Functions tests if entry is valid entry and performs followup functions.
 */
function entryTest() {
  //Removes the textbox and button when user has had 6 valid guesses.
  if (resultNum == 6) {
    $("#guess-textbox").fadeOut("slow");
    $("#guess-button").fadeOut("slow");
  }
  let entry = document.getElementById("cheese-choice").value;
  let validEntry = false;
  for (let i = 0; i < cheeseList.length; i++) {
    if (entry.toLowerCase() == cheeseList[i].toLowerCase()) {
      validEntry = true;
    }
  }

  if (validEntry == false) {
    togglePopup();
  }

  if (validEntry == true) {
    removeText();
    $("#result-"+resultNum).fadeOut("slow");
    resultNum++;
  }
}


/**
 * Generates a popup box when the user does not enter a valid cheese.
 */
function togglePopup() {
  document.getElementById("popup-1").classList.toggle("active");
}