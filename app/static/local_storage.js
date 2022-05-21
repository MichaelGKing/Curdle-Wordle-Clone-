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
function userSucceeded() {
  localStorage.setItem("puzzleState", "win");
  localStorage.setItem("lastCompleted", getDate());
}

function userFailed() {
  localStorage.setItem("puzzleState", "fail")
  let date = getDate();
  localStorage.setItem("lastCompleted", date)
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
  var testObject = { 'one': 1, 'two': 2, 'three': 3 };

  // Put the object into storage
  localStorage.setItem('testObject', JSON.stringify(testObject));

  // Retrieve the object from storage
  var retrievedObject = localStorage.getItem('testObject');

  console.log('retrievedObject: ', JSON.parse(retrievedObject));
}