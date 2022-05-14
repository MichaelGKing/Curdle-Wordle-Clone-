let cheese = ["Cheddar", "Cow", "Type-5", "false"];
let cheeseList = ["Cheddar", "Camembert", "Parmesan", "Red Leicester", "Blue Cheese"];
let resultNum = 1;
let cheeseIndex = 0;

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
  //resultnum starts at 1
  document.getElementById("word-" + resultNum).classList.toggle("active");
  let newEle = document.createElement("p");
  let para = document.createTextNode(cheeseList[cheeseIndex]);
  newEle.appendChild(para);
  document.getElementById("word-" + resultNum).appendChild(newEle);
  $("#word-" + resultNum).css("display", "flex").hide().fadeIn("slow");

  document.getElementById("world-" + resultNum).classList.toggle("active");
  $("#world-" + resultNum).css("display", "flex").hide().fadeIn("slow");

  document.getElementById("mold-" + resultNum).classList.toggle("active");
  $("#mold-" + resultNum).css("display", "flex").hide().fadeIn("slow");

  document.getElementById("animal-" + resultNum).classList.toggle("active");
  $("#animal-" + resultNum).css("display", "flex").hide().fadeIn("slow");

  document.getElementById("type-" + resultNum).classList.toggle("active");
  $("#type-" + resultNum).css("display", "flex").hide().fadeIn("slow");

  resultNum++;
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
      cheeseIndex = i;
    }
  }

  if (validEntry == false) {
    togglePopup();
  }

  if (validEntry == true) {
    removeText();
    $("#result-"+resultNum).fadeOut(500);
    setTimeout(resultGen, 500);
    
  }
}


/**
 * Generates a popup box when the user does not enter a valid cheese.
 */
function togglePopup() {
  document.getElementById("popup-1").classList.toggle("active");
}