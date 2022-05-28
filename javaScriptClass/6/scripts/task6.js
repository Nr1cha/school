
let dateNow = new Date();
let currentDay = dateNow.getDay();

let message = "hang in there"

if (currentDay == 1, 2, 3, 4, 5) {
    message = "Hang in there!";
}else {
    message = "Woohoo! it is the weekend!";
}

/* SWITCH, CASE, BREAK 
day*/
let anotherMessage1 = "";

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

document.getElementById("message1").innerHTML = message;
document.getElementById("message2").innerHTML = anotherMessage1;


/* FETCH */
let filmList = [];


function output(listOfNames) {
    for (film of listOfNames) {
        // let nL = document.createElement("br");
        let templeId = document.getElementById("movies");
        let articleElement = document.createElement("article");

        let h3Tag = document.createElement("h3")
        h3Tag.innerText = film.title;

        let movieDate = document.createElement("h3")
        movieDate = "Date Released: " + film.release_date;

        let h4Tag = document.createElement("h4");
        h4Tag.innerText = "Producer: " + film.producer

        let h4_2Tag = document.createElement("h4");
        h4_2Tag = "Director: " + film.director

        articleElement.append(h3Tag, movieDate, h4Tag, h4_2Tag);
        templeId.append(articleElement);

    }
}

async function getMovies() {
    let remoteData = await fetch("https://swapi.dev/api/films");
    let result = await remoteData.json();
    filmList = result.results;
    output(filmList);
}
getMovies();

function reset() {
    let results = document.getElementById("movies");
    results.innerHTML = "";
}

// sort function
function sortBy(){
    reset();
    let sort = document.getElementById("sortBy").value;
    if (sort ==  "filmsAscending") {
        filmList.sort(sortAscending);
    }
    if (sort == "filmsDescending"){
        filmList.sort(sortDescending);
        // console.log(filmList)
    }
    output(filmList);
}

// sort descending
function sortDescending (a,b){
    if (a.title < b.title){
        return 1;
    }
    if (a.title > b.title){
        return -1;
    }
    return 0;
}

// sort ascending
function sortAscending (a,b){
    if (a.title < b.title){
        return -1;
    }
    if (a.title > b.title){
        return 1;
    }
    return 0;
}

//  event listener that calls the sortBy function
document.getElementById("sortBy").addEventListener("change",sortBy);

