/* Lesson 5 */

/* IF/ELSE IF */

// Step 1: Declare and initialize a new variable to hold the current date
let dateNow = new Date();


// Step 2: Declare another variable to hold the day of the week
let currentDay = dateNow.getDay();
// let weekDay = currentDate.getDay("1-5");

// Step 3: Using the variable declared in Step 1, assign the value of the variable declared in Step 2 to the day of the week ( hint: getDay() )
console.log(currentDay);

// Step 4: Declare a variable to hold a message that will be displayed
let message = "hang in there"

// Step 5: Using an if statement, if the day of the week is a weekday (i.e. Monday - Friday), set the message variable to the string 'Hang in there!'
if (currentDay == 1, 2, 3, 4, 5) {
    message = "Hang in there!";
}

// Step 6: Using an else statement, set the message variable to 'Woohoo!  It is the weekend!'
else {
    message = "Woohoo! it is the weekend!";
}

/* SWITCH, CASE, BREAK */

// Step 1: Declare a new variable to hold another message
let anotherMessage1 = "";
// Step 2: Use switch, case and break to set the message variable to the day of the week as a string (e.g. Sunday, Monday, etc.) using the day of week variable declared in Step 2 above
switch (currentDay) {
    case 0:
        anotherMessage1 = "Sunday";
        break;
    case 1:
        anotherMessage1 = "Monday";
        break;
    case 2:
        anotherMessage1 = "Tuesday";
        break;
    case 3:
        anotherMessage1 = "Wednesday";
        break;
    case 4:
        anotherMessage1 = "Thursday";
        break;
    case 5:
        anotherMessage1 = "Friday";
        break;
    case 6:
        anotherMessage1 = "Saturday";
        break;
}

/* OUTPUT */

// Step 1: Assign the value of the first message variable to the HTML element with an ID of message1
document.getElementById("message1").innerHTML = message;

// Step 2: Assign the value of the second message variable to the HTML element with an ID of message2
document.getElementById("message2").innerHTML = anotherMessage1;


/* FETCH */
// Step 1: Declare a global empty array variable to store a list of temples
let templeList = [];

// Step 2: Declare a function named output that accepts a list of temples as an array argument and does the following for each temple:
function output1(listOfTemples) {
    for (temple of listOfTemples) {

        let templeId = document.getElementById("temples");
        let articleElement = document.createElement("article");
        let h3Tag = document.createElement("h3")
        h3Tag.innerText = temple.templeName;
        let h4Tag = document.createElement("h4");
        h4Tag.innerText = temple.location
        let h4_2Tag = document.createElement("h4");
        h4_2Tag.innerText = temple.dedicated
        let imgTag = document.createElement("img");
        imgTag.alt = temple.imageUrl
        imgTag.src = temple.imageUrl

        articleElement.append(h3Tag, h4Tag, h4_2Tag, imgTag);
        templeId.append(articleElement);

    }
}
// - Creates an HTML <article> element
// - Creates an HTML <h3> element and add the temple's templeName property to it
// - Creates an HTML <h4> element and add the temple's location property to it
// - Creates an HTML <h4> element and add the temple's dedicated property to it
// - Creates an HTML <img> element and add the temple's imageUrl property to the src attribute and the temple's templeName property to the alt attribute
// - Appends the <h3> element, the two <h4> elements, and the <img> element to the <article> element as children
// - Appends the <article> element to the HTML element with an ID of temples

templeList.push({ templeName: "testTemple", location: "testLocation", dedicated: "testDedication", imageUrl: "https://ksltv.com/wp-content/uploads/2022/03/SMITHFIELD-EPHRAIM-RENDERS.jpg" })
output1(templeList);

// Step 3: Create another function called getTemples. Make it an async function.
function getTemples(){

}
// Step 4: In the function, using the built-in fetch method, call this absolute URL: 'https://byui-cse.github.io/cse121b-course/week05/temples.json'. Create a variable to hold the response from your fetch. You should have the program wait on this line until it finishes.
// Step 5: Convert your fetch response into a Javascript object ( hint: .json() ). Store this in the templeList variable you declared earlier (Step 1). Make sure the the execution of the code waits here as well until it finishes.
// Step 6: Finally, call the output function and pass it the list of temples. Execute your getTemples function to make sure it works correctly.

async function getTempleData() {
    let remoteData = await fetch("https://byui-cse.github.io/cse121b-course/week05/temples.json");
    remoteData = await remoteData.json();
    // output(remoteData);
    console.log(remoteData)
}
getTempleData();


// Step 7: Declare a function named reset that clears all of the <article> elements from the HTML element with an ID of temples

// Step 8: Declare a function named sortBy that does the following:
// - Calls the reset function
// - Sorts the global temple list by the currently selected value of the HTML element with an ID of sortBy
// - Calls the output function passing in the sorted list of temples

// Step 9: Add a change event listener to the HTML element with an ID of sortBy that calls the sortBy function

/* STRETCH */

// Consider adding a "Filter by" feature that allows users to filter the list of temples
// This will require changes to both the HTML and the JavaScript files
