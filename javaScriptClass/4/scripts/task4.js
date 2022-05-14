/* Lesson 4 */

/* DATA */

// Step 1: Declare a new variable to hold information about yourself
let nickRichards = {};

// Step 2: Inside of the object, add a property named name with a value of your name as a string
nickRichards.name = "Nick Richards";

// Step 3: Add another property named photo with a value of the image path and name (used in Task 2) as a string

nickRichards.photo = "images/nick.jpg";

// Step 4: Add another property named favoriteFoods with a value of an array of your favorite foods as strings ( hint: [] )

nickRichards.favoriteFoods = ["pizza","sushi","chips","soda","my wifs cooking"];

// Step 5: Add another property named hobbies with a value of an array of your hobbies as strings

nickRichards.hobbies = ["gaming", "hiking", "carpentry"];

// Step 6: Add another property named placesLived with a value of an empty array

nickRichards.placesLived = [];

/* Step 7: Inside of the empty array above, add a new 
object with two properties: 
place and 
length and 
values of an empty string
*/
nickRichards.placesLived.push({ place: "", tlength: "" });

// Step 8: For each property, add appropriate values as strings
nickRichards.placesLived.push({ place: "utah", tlength: "16 years" });
nickRichards.placesLived.push({ place: "washington", tlength:"15 years" });
nickRichards.placesLived.push({ place: "virginia", tlength:"2 years" });

// Step 9: Add additional objects with the same properties for each place you've lived


/* OUTPUT */

// Step 1: Assign the value of the name property (of the object declared above) to the HTML <span> element with an ID of name
document.getElementById('name').innerHTML = nickRichards.name;
//Step 2: Assign the value of the photo property as the src attribute of the HTML <img> element with an ID of photo

document.getElementById('photo').src = nickRichards.photo;

// Step 3: Assign the value of the name property as the alt attribute of the HTML <img> element with an ID of photo
document.getElementById('photo').alt = nickRichards.name;

// Step 4: For each favorite food in the favoriteFoods property, create an HTML <li> element and place its value in the <li> element

let foodElement = document.getElementById('favorite-foods');
for (food of nickRichards.favoriteFoods) {
    foodElement.innerHTML += "<li>" + food + "</li>";
}

// Step 5: Append the <li> elements created above as children of the HTML <ul> element with an ID of favorite-foods
//*DONE
// Step 6: Repeat Step 4 for each hobby in the hobbies property
let hobbieList = document.getElementById('hobbies');
for (hobbie of nickRichards.hobbies) {
    hobbieList.innerHTML += "<li>" + hobbie + "</li>";
}

// Step 7: Repeat Step 5 using the HTML <ul> element with an ID of hobbies
//*DONE
// Step 8: For each object in the placesLived property:
// - Create an HTML <dt> element and put its place property in the <dt> element
// - Create an HTML <dd> element and put its length property in the <dd> element

let livedPlaces = document.getElementById('places-lived');
for (placesDwelled of nickRichards.placesLived) {
    livedPlaces.innerHTML += "<dt>" + placesDwelled.place + "</dt>"
    livedPlaces.innerHTML += "<dd>" + placesDwelled.tlength + "</dd>"
}
// Step 9: Append the HTML <dt> and <dd> elements created above to the HTML <dl> element with an ID of places-lived




