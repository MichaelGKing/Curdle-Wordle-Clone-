// Initializes cheeseList variable which is set to the list of cheeses retrieved from the server on page load.
let cheeseList = [];
function storeCheeseList() {
  cheeseList = getCheeseList();
}

// Array indicating if guesses attributes are the same as the answers attributes.
// Initialized to all false, will be updated from server upon user input.
let correctChoice = [false, false, false, false, false, false];

//Tracks how many valid guesses have been made. For use in various mutator functions.
let resultNum = 1;

//Initializes puzzleNum variable which is set to the day's puzzle ID from the server.
let puzzleNum = -1;

// Initializes a 2-D array for storing the results of the users input. Used for creating
// a string that can be copied by the user to share their results.
var resultArray = new Array(5);
for (var i = 0; i < 6; i++) {
  resultArray[i] = [-1, -1, -1, -1, -1, -1];
}


/**
 * Function stores the results of the user in a 2-D array for use in creating
 * a string that can be copied by the user to share their results.
 */
function attributeChecker() {
  for (let i = 0; i < correctChoice.length -1; i++) {
    if (correctChoice[i] == true) {
      resultArray[resultNum - 1][i] = 1;
    }
    if (correctChoice[i] == false) {
      resultArray[resultNum - 1][i] = 0;
    }
  }
  if (correctChoice[5] == true && correctChoice[1] == false) {
    resultArray[resultNum - 1][1] = 2;
  }
}

/**
 * Function generates results box. Used both in user interaction and in creating the
 * page for the returning user.
 */
function resultGen(entry) {
  //resultnum starts at 1
  document.getElementById("word-" + resultNum).classList.toggle("active");
  let newEle = document.createElement("p");
  let para = document.createTextNode(entry);
  newEle.appendChild(para);
  document.getElementById("word-" + resultNum).appendChild(newEle);
  if (correctChoice[0] == true) {
    $("#word-" + resultNum).css("border", "2px solid green");
  }
  $("#word-" + resultNum).css("display", "flex").hide().fadeIn("slow");

  //Generates section indicating if country is correct.
  document.getElementById("world-" + resultNum).classList.toggle("active");
  $("#world-" + resultNum).append("<i class='fa fa-globe'></i>");
  if (correctChoice[1] == true) {
    $("#world-" + resultNum + " i").css("color", "green");
  }
  if ((correctChoice[1] == false) && (correctChoice[5] == true)) {
    $("#world-" + resultNum + " i").css("color", "orange");
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

  //Increments the result num
  resultNum++;
}

/**
 * Functions performs data validation by checking entry again database provided list of cheeses.
 */
function entryTest(entry) {
  // Data validation portion.
  let validEntry = false;
  for (let i = 0; i < cheeseList.length; i++) {
    if (entry.toLowerCase() == cheeseList[i].toLowerCase()) {
      validEntry = true;
      entry = cheeseList[i];
    }
  }
  // Displays pop up if invalid data.
  if (validEntry == false) {
    toggleInvalid();
  }
  
  if (validEntry == true) {
    // Stores guess in local storage.
    userPlayed(entry);
    // Makes an array that contains boolean for if the attributes of your guesses attributes match the answer.
    correctChoice = sendCheese(entry);
    // Removes text from the input box.
    removeText();
    // Stores results for use in clipboard share button.
    attributeChecker();
    // Tests if user correctly guessed cheese and removes inputs.
    if (correctChoice[0] == true) {
      $("#guess-textbox").fadeOut("slow");
      $("#guess-button").fadeOut("slow");
      toggleCongrats();
      $("#correct-cheese-container").css("display", "flex").hide().fadeIn("slow");
      $("#share-button").css("display", "flex").hide().fadeIn("slow");
      userSucceeded();
      // Retrieves answer and references materials used in a pop up box.
      getAnswer();
    }
    // Removes the results placeholder.
    $("#result-" + resultNum).fadeOut(500);
    // Adds results.
    setTimeout(resultGen(entry), 500);
  }

  // Triggers loss event and removes user input if user runs out of guesses and hasn't won.
  if ((resultNum == 7) && localStorage.getItem("puzzleState") != 'win') {
    // Retrieves answer and references materials used in a pop up box.
    getAnswer();
    toggleFail();
    $("#guess-textbox").fadeOut("slow");
    $("#guess-button").fadeOut("slow");
    $("#share-button").css("display", "flex").hide().fadeIn("slow");
    $("#correct-cheese-container").css("display", "flex").hide().fadeIn("slow");
    userFailed();
  }
}

/**
 * Function sets the stats in the stats page from data retrieved in the local
 * storage. Typically called when stats are changed.
 */
function setStats() {
  $("#played_text").html(localStorage.getItem("played"));
  $("#winrate_text").html(Math.round(parseInt(localStorage.getItem("winrate"))) + "%");
  $("#streak_text").html(localStorage.getItem("streak"));
  $("#best_text").html(localStorage.getItem("best-streak"));

  let guessDist = localStorage.getItem("guess-distribution").split(',');
  let guessDistInt = [];
  for (let i = 0; i < guessDist.length; i ++) {
    guessDistInt.push(parseInt(guessDist[i]));
  }
  let maxDist = Math.max.apply(Math, guessDistInt);
  let width;
  for (let i = 0; i < guessDistInt.length; i ++) {
    if (maxDist == 0) {
      width = 0
    } else {
      width = (guessDistInt[i] / maxDist) * 100;
    }
    $("#bar" + (i + 1)).css("width", width + "%")
    $("#bar" + (i + 1) + " p").html(guessDistInt[i])
  }
}