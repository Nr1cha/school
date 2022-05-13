/* Lesson 2 */

/* VARIABLES */

// Step 1: declare and instantiate a variable to hold your name
const myName = 'Nick Richards';


// Step 2: place the value of the name variable into the HTML file (hint: document.querySelector())
document.querySelector('#name').textContent = myName;


// Step 3: declare and instantiate a variable to hold the current year
const currentYear = 2022;

// Step 4: place the value of the current year variable into the HTML file
document.querySelector('#year').textContent = currentYear;

// Step 5: declare and instantiate a variable to hold the name of your picture
const picture = 'images/missionPic.jpg';

// Step 6: copy your image into the "images" folder

// Step 7: place the value of the picture variable into the HTML file (hint: document.querySelector().setAttribute())
document.querySelector('img').setAttribute('src', picture);



/* ARRAYS */

// Step 1: declare and instantiate an array variable to hold your favorite foods
const foodsILike = ['pizza', ' grilled cheese sandwiches', ' sushi', ' rootbeer drink'];

// Step 2: place the values of the favorite foods variable into the HTML file
document.querySelector('#food').textContent = foodsILike;

// Step 3: declare and instantiate a variable to hold another favorite food
const secondFavFood = ' Moms Spaghetti';

// Step 4: add the variable holding another favorite food to the favorite food array
foodsILike.push(secondFavFood); //this is adding it to my foodsILike list 

// Step 5: repeat Step 2
document.querySelector('#food').textContent = foodsILike; //this will now show the new value from step 4

// Step 6: remove the first element in the favorite foods array
foodsILike.shift(); //removes the 0 position item from the list

// Step 7: repeat Step 2
document.querySelector('#food').textContent = foodsILike;

// Step 8: remove the last element in the favorite foods array
foodsILike.pop(); //removes the last position item from the list


// Step 7: repeat Step 2
document.querySelector('#food').textContent = foodsILike; // shows what the original list had on it


