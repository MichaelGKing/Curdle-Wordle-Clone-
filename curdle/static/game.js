//Stores information on the correct cheese.
let correctAttributes = ["Cheddar", "Europe", "Cow", "Type-5", "false"];

//Stores a list of all the valid cheeses.
let cheeseList = ["Cheddar", "Camembert", "Parmesan", "Red Leicester", "Blue Cheese"];

//Entries are name, continent, mold, animal, cheese type.
let correctChoice = [false, false, false, false, false];
let resultNum = 1;
let cheeseIndex = 0;

/**
 * Generates boolean array indicating if attribute of guessed cheese is same
 * as attribute of the correct cheese.
 */
function attributeChecker() {
  let guess = document.getElementById("cheese-choice").value.toLowerCase();

  // Array brought back from server after pinged with guess value.
  let guessAttributes = ["Cheddar", "Europe", "Cow", "Type-5", "false"];

  // Mutates correctChoice array if guess attribute aligns with correct attribute.
  for (let i = 0; i < guessAttributes.length; i++) {
    if (guessAttributes[i] == correctAttributes[i]) {
      correctChoice[i] = true;
    }
  }
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
  if (correctChoice[0] == true) {
    $("#word-" + resultNum).css("border", "3px solid green");
  }
  $("#word-" + resultNum).css("display", "flex").hide().fadeIn("slow");

  //Generates section indicating if continent is correct.
  document.getElementById("world-" + resultNum).classList.toggle("active");
  $("#world-" + resultNum).append("<i class='fa fa-globe'></i>");
  if (correctChoice[1] == true) {
    $("#world-" + resultNum + " i").css("color", "green");
  }
  $("#world-" + resultNum).css("display", "flex").hide().fadeIn("slow");

  //Generates section indicating if mold content is correct.
  document.getElementById("mold-" + resultNum).classList.toggle("active");
  $("#mold-" + resultNum).append("<i class='fa-solid fa-bacteria'></i>");
  if (correctChoice[2] == true) {
    $("#mold-" + resultNum + " i").css("color", "green");
  }
  $("#mold-" + resultNum).css("display", "flex").hide().fadeIn("slow");

  //Generates section indicating if animal of origin is correct.
  document.getElementById("animal-" + resultNum).classList.toggle("active");
  $("#animal-" + resultNum).append("<i class='fa-solid fa-paw'></i>");
  if (correctChoice[3] == true) {
    $("#animal-" + resultNum + " i").css("color", "green");
  }
  $("#animal-" + resultNum).css("display", "flex").hide().fadeIn("slow");

  //Generates section indicating if type of cheese is correct.
  document.getElementById("type-" + resultNum).classList.toggle("active");
  $("#type-" + resultNum).append("<i class='fas fa-cheese'></i>");
  if (correctChoice[4] == true) {
    $("#type-" + resultNum + " i").css("color", "green");
  }
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
    attributeChecker();
    if (correctChoice[0] == true) {
      $("#guess-textbox").fadeOut("slow");
      $("#guess-button").fadeOut("slow");
    }
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

/**
 * Generates popupbox for help and stats button.
 */
function toggleHelp() {
  document.getElementById("popup-2").classList.toggle("active");
}

function toggleStats() {
  document.getElementById("popup-3").classList.toggle("active");
}