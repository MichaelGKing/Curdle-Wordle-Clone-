//Function loads users information from local storage
function getDate() {
  var today = new Date();
  var dd = String(today.getDate()).padStart(2, '0');
  var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
  var yyyy = today.getFullYear();

  today = mm + '/' + dd + '/' + yyyy;
  return today;
}

//Resets the localstorage if the user returns on a different puzzle. Otherwise
//sets up page for returning user.
function loadUser() {
  $("#pageload").fadeOut("slow");
  if (localStorage.getItem("visits") == 1) {
    toggleHelp();
    localStorage.setItem("guess_made", false);
    localStorage.setItem("wins", 0);
    localStorage.setItem("played", 0);
    localStorage.setItem("winrate", 0);
    localStorage.setItem("streak", 0);
    localStorage.setItem("best-streak", 0);
    localStorage.setItem("guess-distribution", "0,0,0,0,0,0")
  } else {
    
    if (localStorage.getItem("last_puzzle_attempted") == puzzleNum) {
      let guesses = localStorage.getItem("guesses_made");
      let guessesArray = guesses.split(',');
      for (let i = 0; i < guessesArray.length; i++) {
        entryTest(guessesArray[i]);
      }
      localStorage.setItem("guesses_made", guesses);
    }
    if (localStorage.getItem("last_puzzle_attempted") != puzzleNum) {
      localStorage.removeItem("guesses_made");
      localStorage.removeItem("puzzleState");
      localStorage.removeItem("userCompleted");
      localStorage.setItem("guess_made", false);
    }
  }

  if (parseInt(localStorage.getItem("lastWin")) < (puzzleNum - 1)) {
    localStorage.setItem("streak", 0);
  }
  setStats();
}

//Function loads when user gets correct guess
function userCompleted() {
  localStorage.setItem("userCompleted", true);
}

function userSucceeded() {
  if (localStorage.getItem("puzzleState") == null) {
    localStorage.setItem("wins", parseInt(localStorage.getItem("wins")) + 1);
    localStorage.setItem("streak", parseInt(localStorage.getItem("streak")) + 1);
    if (parseInt(localStorage.getItem("streak")) > parseInt(localStorage.getItem("best-streak"))) {
      localStorage.setItem("best-streak", localStorage.getItem("streak"));
    }
    distCalc();
  }
  localStorage.setItem("puzzleState", "win");
  localStorage.setItem("lastWin", puzzleNum);
  userCompleted();
  let winrate = parseInt(localStorage.getItem("wins")) / parseInt(localStorage.getItem("played")) * 100;
  localStorage.setItem("winrate", winrate);
  
  setStats();
}

function userFailed() {
  localStorage.setItem("puzzleState", "fail");
  userCompleted();
}

//Function called when user makes a valid guess.
function userPlayed(guess) {
  if (localStorage.getItem("guess_made") == 'false') {
    localStorage.setItem("played", parseInt(localStorage.getItem("played")) + 1);
    let winrate = parseInt(localStorage.getItem("wins")) / parseInt(localStorage.getItem("played")) * 100;
    localStorage.setItem("winrate", winrate);
    
  }
  localStorage.setItem("guess_made", true);
  localStorage.setItem("last_puzzle_attempted", puzzleNum);
  let guesses_made = localStorage.getItem("guesses_made");
  if (guesses_made == null) {
    localStorage.setItem("guesses_made", guess);
  } else {
    guesses_made = guesses_made + "," + guess;
    localStorage.setItem("guesses_made", guesses_made);
  }
  setStats();
}

//Function stores how many user visits there have been.
function userVisited() {
  let visits = localStorage.getItem("visits");
  if (visits == null) {
    visits = 0;
  } 
  visits = parseInt(visits) + 1;
  if (visits == 1) {
    console.log("First visit")
  }
  else {console.log(visits + ' times visited')}

  localStorage.setItem('visits', visits);
}

function distCalc() {
  let dist = resultNum - 1;
  let guessDist = localStorage.getItem("guess-distribution");
  let guessDistArray = guessDist.split(',');
  let guessDistArrayInt = [];
  for (let i = 0; i < guessDistArray.length; i ++) {
    guessDistArrayInt.push(parseInt(guessDistArray[i]));
  }
  guessDistArrayInt[dist] = guessDistArrayInt[dist] + 1;
  localStorage.setItem("guess-distribution", guessDistArrayInt.join(","));
}