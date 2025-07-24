/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
  // Only run on place.html
  if (document.getElementById('place-details')) {
    const placeId = getPlaceIdFromURL();
    if (placeId) {
      fetchPlaceDetails(placeId);
      fetchPlaceReviews(placeId);
    }
  }
  if (document.getElementById('places-list')) {
    fetchPlaces();
  }
});

function getPlaceIdFromURL() {
  const params = new URLSearchParams(window.location.search);
  return params.get('place_id');
}

function fetchPlaceDetails(placeId) {
  fetch(`http://localhost:5000/api/v1/places/${placeId}`)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(place => {
      displayPlaceDetails(place);
    })
    .catch(error => {
      console.error('Error fetching place details:', error);
    });
}

function displayPlaceDetails(place) {
  const detailsSection = document.getElementById('place-details');
  if (!detailsSection) return;

  // Host info (if available)
  let hostInfo = '';
  if (place.owner) {
    hostInfo = `
      <div class="place-info">
        <strong>Host:</strong> ${place.owner.first_name} ${place.owner.last_name} (${place.owner.email})
      </div>
    `;
  }

  // Amenities
  let amenities = '';
  if (Array.isArray(place.amenities) && place.amenities.length > 0) {
    amenities = `
      <div class="place-info">
        <strong>Amenities:</strong>
        <ul>
          ${place.amenities.map(a => `<li>${a.name}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  detailsSection.innerHTML = `
    <div class="place-info"><strong>Title:</strong> ${place.title || place.name}</div>
    ${hostInfo}
    <div class="place-info"><strong>Price:</strong> $${place.price}</div>
    <div class="place-info"><strong>Description:</strong> ${place.description}</div>
    ${amenities}
  `;
}

function fetchPlaces() {
  fetch('http://localhost:5000/api/v1/places')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      let places = [];
      // If backend returns { places: [...] }
      if (data && Array.isArray(data.places)) {
        places = data.places;
      } else if (Array.isArray(data)) {
        // If backend returns an array directly
        places = data;
      } else {
        // Log the unexpected data for debugging
        console.error('Unexpected response format:', data);
        return; // Don't call displayPlaces with bad data
      }
      displayPlaces(places);
    })
    .catch(error => {
      console.error('Error fetching places:', error);
    });
}

function displayPlaces(places) {
  const placesList = document.getElementById('places-list');
  if (!placesList) {
    console.error('No element with id \"places-list\" found in the DOM.');
    return;
  }
  placesList.innerHTML = '';
  places.forEach(place => {
    const card = document.createElement('div');
    card.className = 'place-card';
    card.innerHTML = `
      <h3>${place.name || place.title || 'No Name'}</h3>
      <p>Price per night: $${place.price !== undefined ? place.price : 'N/A'}</p>
      <button class="details-button" data-id="${place.id}">View Details</button>
    `;
    placesList.appendChild(card);
  });
}


function fetchPlaceReviews(placeId) {
  fetch(`http://localhost:5000/api/v1/reviews/places/${placeId}/reviews`)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(reviews => {
      displayPlaceReviews(reviews);
    })
    .catch(error => {
      console.error('Error fetching reviews:', error);
    });
}

function displayPlaceReviews(reviews) {
  const reviewsSection = document.getElementById('reviews');
  if (!reviewsSection) return;
  reviewsSection.innerHTML = '<h2>Reviews</h2>';
  if (!Array.isArray(reviews) || reviews.length === 0) {
    reviewsSection.innerHTML += '<p>No reviews yet.</p>';
    return;
  }

  // For each review, fetch the user name and display the review card
  reviews.forEach(review => {
    fetch(`http://localhost:5000/api/v1/users/${review.user_id}`)
      .then(response => response.ok ? response.json() : { first_name: 'Unknown', last_name: '' })
      .then(user => {
        const card = document.createElement('div');
        card.className = 'review-card';
        card.innerHTML = `
          <p><strong>${user.first_name || 'Unknown'} ${user.last_name || ''}</strong> rated: ${review.rating}/5</p>
          <p>${review.text}</p>
        `;
        reviewsSection.appendChild(card);
      })
      .catch(() => {
        const card = document.createElement('div');
        card.className = 'review-card';
        card.innerHTML = `
          <p><strong>Unknown User</strong> rated: ${review.rating}/5</p>
          <p>${review.text}</p>
        `;
        reviewsSection.appendChild(card);
      });
  });
}
