/**
 * Retrieves the list of possible cheeses from the server.
 * @returns list of possible cheeses.
 */
function getCheeseList() {
  let response
  $.ajax({
    type: "POST",
    async: false,
    url: '/get-cheeses',
    dataType: "json",
    success: function (data, status, xhr) { response=data;}
  });
  let cheeseList = Object.values(response);
  return cheeseList;
}

/**
 * Function returns an array of boolean data for checking if the guesses attributes
 * align with the answers attributes.
 * @param entry the cheese value entered into guess box.
 * @returns array of guess results from the server.
 */
function sendCheese(entry) {
  let response
  $.ajax({
    type: "POST",
    async: false,
    url: '/check-guess',
    contentType: "application/json",
    dataType: "json",
    data: JSON.stringify({
      cheese_name: entry,
    }),
    success: function (data, status, xhr) { response=data;}
  });
  
  // Pushes the JSON array into a usable correctly ordered array for use in
  // JS functions.
  let result_arranged = [];
  result_arranged.push(response.name)
  result_arranged.push(response.country)
  result_arranged.push(response.mould)
  result_arranged.push(response.animal)
  result_arranged.push(response.type)
  result_arranged.push(response.continent)

  return result_arranged;
}

/**
 * Function retrieves the day's puzzle id. Used in tracking stats.
 */
function getPuzzleID() {
  let response;
  $.ajax({
    type: "POST",
    async: false,
    url: '/puzzle-id',
    dataType: "json",
    success: function (data, status, xhr) { response=data;}
  });
  let puzzleData = Object.values(response);
  puzzleNum = puzzleData[1];
}

/**
 * Function retrieves the answer to the puzzle and links to resources used. 
 * Revealed to users if they fail to guess.
 */
function getAnswer() {
  let response;
  $.ajax({
    type: "POST",
    async: false,
    url: '/get-answer',
    dataType: "json",
    success: function (data, status, xhr) { response=data;}
  });
  let answer = Object.values(response);
  
  $("#correct-cheese p").html(answer);
  console.log(answer);
}