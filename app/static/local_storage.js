//Function loads users information from local storage
function getDate() {
  var today = new Date();
  var dd = String(today.getDate()).padStart(2, '0');
  var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
  var yyyy = today.getFullYear();

  today = mm + '/' + dd + '/' + yyyy;
  return today;
}
function loadUser() {
  let puzzleComplete = localStorage.getItem("puzzleComplete");

}

//Function loads when user gets correct guess
function userCompleted() {
  localStorage.setItem("lastCompleted", puzzleNum);
}

function userSucceeded() {
  localStorage.setItem("puzzleState", "win");
  userCompleted();
}

function userFailed() {
  localStorage.setItem("puzzleState", "fail");
  userCompleted();
}

function userPlayed() {
  localStorage.setItem("played", 1)
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