let dateNow = new Date();
let currentDay = dateNow.getDay();

/* SWITCH, CASE, BREAK */
let day;
switch (currentDay) {
    case 0:
        day = "Sunday";
        break;
    case 1:
        day = "Monday";
        break;
    case 2:
        day = "Tuesday";
        break;
    case 3:
        day = "Wednesday";
        break;
    case 4:
        day = "Thursday";
        break;
    case 5:
        day = "Friday";
        break;
    case 6:
        day = "Saturday";
        break;
}

if ([1, 2, 3, 4, 5].includes(currentDay)) {
    message = "You're almost there!";
}
else {
    message = "Finally! it is the weekend!";
}
document.getElementById("day").innerHTML = day;
document.getElementById("message").innerHTML = message;

// global list
let filmList = [];


function output(listOfNames) {
    for (film of listOfNames) {
        let templeId = document.getElementById("movies");
        let articleElement = document.createElement("article");

        let h3Tag = document.createElement("h3");
        h3Tag.innerText = film.title;

        let movieDate = document.createElement("h3");
        movieDate = "Date Released: " + film.release_date;

        let h4Tag = document.createElement("h4");
        h4Tag.innerText = "Producer: " + film.producer;

        let h4_2Tag = document.createElement("h4");
        h4_2Tag = "Director: " + film.director;

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
function sortBy() {
    reset();
    let sort = document.getElementById("sortBy").value;
    if (sort == "filmsAscending") {
        filmList.sort(sortAscending);
    }
    if (sort == "filmsDescending") {
        filmList.sort(sortDescending);
    }
    output(filmList);
}

// sort descending
function sortDescending(a, b) {
    if (a.title < b.title) {
        return 1;
    }
    if (a.title > b.title) {
        return -1;
    }
    return 0;
}

// sort ascending
function sortAscending(a, b) {
    if (a.title < b.title) {
        return -1;
    }
    if (a.title > b.title) {
        return 1;
    }
    return 0;
}

//  event listener that calls the sortBy function
document.getElementById("sortBy").addEventListener("change", sortBy);

