/* Lesson 3 */

/* FUNCTIONS */

// Step 1: Using function declaration, define a function named add that takes two arguments, number1 and number2
// Step 2: In the function, return the sum of the parameters number1 and number2
function add(number1, number2) {
    return number1 + number2;
}

// Step 3: Step 3: Using function declaration, define another function named addNumbers that gets the values of two HTML form controls with IDs of addend1 and addend2. Pass them to the add function

// Step 4: Assign the return value to an HTML form element with an ID of sum
function addNumbers() {
    let num1 = parseInt(document.getElementById('addend1').value);
    let num2 = parseInt(document.getElementById('addend2').value);
    document.getElementById("sum").value = add(num1,num2);
}

// Step 5: Add a "click" event listener to the HTML button with an ID of addNumbers that calls the addNumbers function
document.getElementById('addNumbers').addEventListener('click',addNumbers);

// Step 6: Using function expressions, repeat Steps 1-5 with new functions named subtract and subtractNumbers and HTML form controls with IDs of minuend, subtrahend, difference and subtractNumbers
const subtract = function(subtract1, subtract2) {
    return subtract1 - subtract2
};

const subtractNumbers = function () {
    let sub1 = parseInt(document.getElementById('minuend').value);
    let sub2 = parseInt(document.getElementById('subtrahend').value);
    document.getElementById('difference').value = subtract(sub1,sub2);
}

document.getElementById('subtractNumbers').addEventListener('click',subtractNumbers);


// Step 7: Using arrow functions, repeat Steps 1-5 with new functions named multiply and mulitplyNumbers and HTML form controls with IDs of factor1, factor2, product and multiplyNumbers
//arrow timestamp 32:30
const multiply = (number1, number2) => number1 * number2;

const mulitplyNumbers = () => {
    let num1 = parseInt(document.getElementById('factor1').value);
    let num2 = parseInt(document.getElementById('factor2').value);
    document.getElementById('product').value = multiply(num1,num2);
}

document.getElementById('multiplyNumbers').addEventListener('click',mulitplyNumbers);


// Step 8: Using any of the three function declaration types, repeat Steps 1-5 with new functions named divide and divideNumbers and HTML form controls with IDs of dividend, divisor, quotient and divideNumbers
const divide = (number1,number2) => number1 / number2;

const divideNumbers = () => {
    let num1 = parseInt(document.getElementById('dividend').value);
    let num2 = parseInt(document.getElementById('divisor').value);
    document.getElementById('quotient').value = divide(num1,num2);
}

document.getElementById('divideNumbers').addEventListener('click',divideNumbers);


// Step 9: Test all of the mathematical functionality of the task3.html page.


/* BUILT-IN METHODS */

// Step 1: Declare and instantiate a variable of type Date to hold the current date
const date = new Date();

// Step 2: Declare a variable to hold the current year
// Step 3: Using the variable declared in Step 1, call the built-in getFullYear() method/function and assign it to the variable declared in Step 2
const year = date.getFullYear();


// Step 4: Assign the current year variable to an HTML form element with an ID of year
document.getElementById('year').innerText = year;

// /* ARRAY METHODS */ timestamp = 25:20

// Step 1: Declare and instantiate an array variable to hold the numbers 1 through 25
let numbers = [];
for (let i=1; i<=25; i++) {
    numbers.push(i);
}
console.log(numbers);
console.log(date);
console.log(year);

// Step 2: Assign the value of the array variable to the HTML element with an ID of "array"
document.getElementById('array').innerHTML = numbers;

// Step 3: Use the filter array method to find all of the odd numbers of the array variable and assign the reult to the HTML element with an ID of "odds" ( hint: % (modulus operartor) )
const oddNumbers = numbers.filter(number => number % 2 != 0);
document.getElementById('odds').innerHTML = oddNumbers;

// Step 4: Use the filter array method to find all of the even numbers of the array variable and assign the result to the HTML element with an ID of "evens"
const evenNumbers = numbers.filter(number => number % 2 == 0);
document.getElementById('evens').innerHTML = evenNumbers;

// Step 5: Use the reduce array method to sum the array variable elements and assign the result to the HTML element with an ID of "sumOfArray"
const sumArray = numbers.reduce((sum,currentValue)=>{ 
    return sum + currentValue
},0);
document.getElementById('sumOfArray').innerHTML = sumArray;


// Step 6: Use the map array method to multiple each element in the array variable by 2 and assign the result to the HTML element with an ID of "multiplied"
//map timestamp 37:25
const multiplyi = numbers.map(currentValue => currentValue * 2);
document.getElementById('multiplied').innerHTML = multiplyi;


// Step 7: Use the map and reduce array methods to sum the array elements after multiplying each element by two.  Assign the result to the HTML element with an ID of "sumOfMultiplied"
const multiplyNum = numbers
    .map(currentValue => currentValue * 2)
    .reduce((oldValue,currentValue) => {
        return oldValue + currentValue
    },0);
    document.getElementById('sumOfMultiplied').innerHTML = multiplyNum;


