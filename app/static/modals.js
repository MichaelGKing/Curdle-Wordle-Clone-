/**
 * Function toggles the help page to appear.
 */
function toggleHelp() {
  document.getElementById("help-page").classList.toggle("active");
  $("#grid-container-e1").css("display", "grid").hide().fadeIn("slow");
  $("#grid-container-e2").css("display", "grid").hide().fadeIn("slow");
  $("#grid-container-e3").css("display", "grid").hide().fadeIn("slow");
}

/**
 * Generates a popup box when the user does not enter a valid cheese.
 */
function toggleInvalid() {
  document.getElementById("invalid-pop").classList.toggle("active");
}

/**
 * Opens the stats page.
 */
function toggleStats() {
  document.getElementById("stats-page").classList.toggle("active");
}

/**
 * Generates pop containing information on the correct cheese.
 */
function toggleCheese() {
  document.getElementById("cheese-pop").classList.toggle("active");
}

/**
 * Generates a bad luck pop up if user fails to guess in six attempts.
 */
function toggleFail() {
  document.getElementById("fail-pop").classList.toggle("active");
}

/**
 * Generates popup box for when the user successfully completes the puzzle.
 */
function toggleCongrats() {
  document.getElementById("congrats-pop").classList.toggle("active");
}