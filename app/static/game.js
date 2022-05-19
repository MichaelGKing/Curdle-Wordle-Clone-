//Stores information on the correct cheese. DATABASE
let correctAttributes = ["Cheddar", "Europe", "Cow", "Type-5", "false"];

//Stores a list of all the valid cheeses. DATABASE
let cheeseList = ["Cheddar", "Camembert", "Parmesan", "Red Leicester", "Blue Cheese"];

//Entries are name, continent, mold, animal, cheese type.
let correctChoice = [false, false, false, false, false];

//Tracks how many valid guesses have been made.
let resultNum = 1;

//Tracks the index of the cheeselist used in making the guess for generating
//word in the results box from the cheeselist not the user input, as user input
//may have incorrect capitalization.
let cheeseIndex = 0;

//For sharing your puzzle results. DATABASE
let puzzleNum = 1;

//Matrix array storing results.
// Create one dimensional array
var resultArray = new Array(5);
// Loop to create 2D array using 1D array
for (var i = 0; i < resultArray.length; i++) {
  resultArray[i] = [-1, -1, -1, -1, -1, -1];
}


/**
 * Generates boolean array indicating if attribute of guessed cheese is same
 * as attribute of the correct cheese. Also inputs results to 2-D array resultArray
 * for use in sharing results with others.
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

  for (let i = 0; i < correctChoice.length; i++) {
    if (correctChoice[i] == true) {
      resultArray[resultNum - 1][i] = 1;
    }
    if (correctChoice[i] == false) {
      resultArray[resultNum - 1][i] = 0;
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
    $("#share-button").css("display", "flex").hide().fadeIn("slow");
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
    let x = sendCheese();
    console.log(x);
    removeText();
    attributeChecker();
    if (correctChoice[0] == true) {
      $("#guess-textbox").fadeOut("slow");
      $("#guess-button").fadeOut("slow");
      toggleCongrats();
      $("#share-button").css("display", "flex").hide().fadeIn("slow");
    }
    $("#result-" + resultNum).fadeOut(500);
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

/**
 * Generates popup box for when the user completes the puzzle.
 */
function toggleCongrats() {
  document.getElementById("popup-4").classList.toggle("active");
}

/**
 * Copies result to clipboard when share button is pressed.
 */
function clipboard() {
  let text = "";
  for (let i = 0; i < resultArray.length; i++) {
    for (let j = 0; j < resultArray[i].length; j++) {
      if (resultArray[i][j] == -1) {
        continue;
      }
      if (resultArray[i][j] == 0) {
        let x = "🟥";
        text = text.concat(x);
        continue;
      }
      if (resultArray[i][j] == 1) {
        let x = "🟩";
        text = text.concat(x);
        continue;
      }
    }
    text = text.concat("\n");
  }

  text = `Curdle #${puzzleNum} ${resultNum - 1}/6\n${text}`;
  navigator.clipboard.writeText(text);
  alert("Copied the text: " + text);
}


// AJAX form.

function sendCheese() {
  let response = ""
  $.ajax({
    type: "POST",
    async: false,
    url: '/check-guess',
    contentType: "application/json",
    dataType: "json",
    data: JSON.stringify({
      cheese_name: $("#cheese-choice").val(),
    }),
    success: function (data, status, xhr) { response=JSON.stringify(data); }
  });
  return response;
}

console.log("Hello World");

