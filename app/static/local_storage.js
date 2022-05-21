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
  if (localStorage.getItem("visits") == 1) {
    toggleHelp();
  } else {
    if (localStorage.getItem("last_puzzle_attempted") == puzzleNum) {
      let guesses = localStorage.getItem("guesses_made");
      let guessesArray = guesses.split(',');
      console.log(guessesArray);
      for (let i = 0; i < guessesArray.length; i++) {
        entryTest(guessesArray[i]);
      }
      localStorage.setItem("guesses_made", guesses);
    }
    if (localStorage.getItem("last_puzzle_attempted") != puzzleNum) {
      localStorage.removeItem("guesses_made");
      localStorage.removeItem("puzzleState");
      localStorage.removeItem("userCompleted");
      localStorage.removeItem("guess_made");
    }
    // if (localStorage.getItem("guess_made") == 'true') {
    //   let guesses = localStorage.getItem("guesses_made").split(',');
    //   console.log(guesses);
    // }
  }


  // let puzzleComplete = localStorage.getItem("puzzleComplete");
  // if ((puzzleNum.toString()) != (localStorage.getItem("lastCompleted"))) {
  //   localStorage.setItem("userCompleted", false);
  //   localStorage.removeItem("guesses_made");
  //   localStorage.removeItem("puzzleState");
  // } else {
  //   if (localStorage.getItem("gueeses_made") != null) {
  //     let guesses = localStorage.getItem("gueeses_made").split(',');
  //     console.log(guesses);
  //   }
  // }
}

//Function loads when user gets correct guess
function userCompleted() {
  localStorage.setItem("userCompleted", true);
}

function userSucceeded() {
  localStorage.setItem("puzzleState", "win");
  localStorage.setItem("lastWin", puzzleNum);
  userCompleted();
}

function userFailed() {
  localStorage.setItem("puzzleState", "fail");
  userCompleted();
}

function userPlayed(guess) {
  localStorage.setItem("guess_made", true);
  localStorage.setItem("last_puzzle_attempted", puzzleNum);
  let guesses_made = localStorage.getItem("guesses_made");
  if (guesses_made == null) {
    localStorage.setItem("guesses_made", guess);
  } else {
    guesses_made = guesses_made + "," + guess;
    localStorage.setItem("guesses_made", guesses_made);
  }
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