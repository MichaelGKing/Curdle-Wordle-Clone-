/**
 * Function sets up the page for the user depending if they are new, returning to an attempted (or unattempted) puzzle,
 * or returning to a new puzzle.
 */
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

/**
 * Function generates localstorage to indicate if user has completed the puzzle.
 * Either won or run out of gueeses.
 */
function userCompleted() {
  localStorage.setItem("userCompleted", true);
}

/**
 * Function generates localstorage for if the user successfully completes the puzzle.
 */
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

/**
 * Function generates localstorage for if the user runs out of guesses.
 */
function userFailed() {
  localStorage.setItem("puzzleState", "fail");
  userCompleted();
}

/**
 * Function generates localstorage for the guesses made by the user on the day's puzzle,
 * and generates localstorage for if the puzzle has been attempted for that day.
 * For use in generating the site to a returning user.
 * @param guess 
 */
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

/**
 * Function generates localstorage for counting the number of visits a user has made.
 */
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

/**
 * Function calculates the distribution of guesses made by the user for the stats page.
 */
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