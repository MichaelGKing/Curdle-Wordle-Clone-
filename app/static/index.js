/**
 * Function allows cheese guess to be made when enter key is hit.
 */
function search() {
  if (event.key === 'Enter') {
    entryTest(document.getElementById('cheese-choice').value);
  }
}

/**
 * Function removes text from the text input box.
 */
function removeText() {
  document.getElementById("cheese-choice").value = "";
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
      if (resultArray[i][j] == 2) {
        let x = "🟧";
        text = text.concat(x);
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
  let totalGuesses = resultNum - 1;
  // If user failed the puzzle changes the result to X to indicate user was not successful.
  if (localStorage.getItem("puzzleState") == 'fail') {
    totalGuesses = 'X';
  }
  text = `Curdle #${puzzleNum} ${totalGuesses}/6\n${text}`;
  navigator.clipboard.writeText(text);
  alert("Copied the text: " + text);
}