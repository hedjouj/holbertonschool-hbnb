/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
fetchPlaces();  
});

function fetchPlaces() {
    fetch('http://localhost:5000/api/v1')
        .then(response => response.json())
        .then(data => {
            displayPlaces(data);
        })
        .catch(error => {
            console.error('Error fetching places:', error);
        });
}
  function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    placesList.innerHTML = '';

    places.forEach(place => {
        const card = document.createElement('div');
        card.className = 'place-card';

        card.innerHTML = `
            <h3>${place.name}</h3>
            <p>Price per night: $${place.price}</p>
            <button class="details-button" data-id="${place.id}">View Details</button>
        `;

        placesList.appendChild(card);
    });
}