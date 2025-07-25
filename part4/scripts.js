/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
  return null;
}

function setCookie(name, value, days) {
  let expires = '';
  if (days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

function checkAuthentication() {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');

  if (!loginLink) return;

  if (!token) {
    loginLink.style.display = 'block';
    fetchPlaces();
  } else {
    loginLink.style.display = 'none';
    // Fetch places data if the user is authenticated
    fetchPlaces(token);
  }
}

// Store all places globally for filtering
window.allPlaces = [];

document.addEventListener('DOMContentLoaded', () => {
  // Login form handling
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      try {
        const response = await fetch('http://localhost:5000/api/v1/auth/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email, password })
        });
        if (!response.ok) {
          throw new Error('Invalid credentials');
        }
        const data = await response.json();
        if (data && data.token) {
          setCookie('token', data.token, 7); // Store token for 7 days
          window.location.href = 'index.html';
        } else {
          alert('Login failed: No token received');
        }
      } catch (error) {
        alert('Login failed: ' + error.message);
      }
    });
    return; // Don't run the rest of the code on login.html
  }

  if (document.getElementById('place-details')) {
    const placeId = getPlaceIdFromURL();
    if (placeId) {
      fetchPlaceDetails(placeId);
      fetchPlaceReviews(placeId);
    }
  }
  if (document.getElementById('places-list')) {
    checkAuthentication();
  }

  // Populate the price filter dropdown
  const priceFilter = document.getElementById('price-filter');
  if (priceFilter) {
    const options = [
      { value: '10', text: '$10' },
      { value: '50', text: '$50' },
      { value: '100', text: '$100' },
      { value: 'all', text: 'All' }
    ];
    options.forEach(opt => {
      const option = document.createElement('option');
      option.value = opt.value;
      option.textContent = opt.text;
      priceFilter.appendChild(option);
    });
    // Add event listener for filtering
    priceFilter.addEventListener('change', (event) => {
      const selected = event.target.value;
      let filtered = window.allPlaces;
      if (selected !== 'all') {
        const maxPrice = parseFloat(selected);
        filtered = window.allPlaces.filter(place => Number(place.price) <= maxPrice);
      }
      displayPlaces(filtered);
    });
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

  let hostInfo = '';
  if (place.owner) {
    hostInfo = `
      <div class="place-info">
        <strong>Host:</strong> ${place.owner.first_name} ${place.owner.last_name} (${place.owner.email})
      </div>
    `;
  }

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

// Fetch places data using Fetch API and handle the response
async function fetchPlaces(token) {
  const headers = {};
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }
  try {
    const response = await fetch('http://localhost:5000/api/v1/places', { headers });
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    let places = [];
    if (data && Array.isArray(data.places)) {
      places = data.places;
    } else if (Array.isArray(data)) {
      places = data;
    } else {
      console.error('Unexpected response format:', data);
      return;
    }
    window.allPlaces = places;
    displayPlaces(places);
  } catch (error) {
    console.error('Error fetching places:', error);
  }
}

// Populate places list by creating HTML elements for each place
function displayPlaces(places) {
  const placesList = document.getElementById('places-list');
  if (!placesList) {
    console.error('No element with id "places-list" found in the DOM.');
    return;
  }
  // Clear the current content of the places list
  placesList.innerHTML = '';
  // Iterate over the places data
  places.forEach(place => {
    // For each place, create a div element and set its content
    const card = document.createElement('div');
    card.className = 'place-card';
    card.innerHTML = `
      <h3>${place.name || place.title || 'No Name'}</h3>
      <p>Price per night: $${place.price !== undefined ? place.price : 'N/A'}</p>
      <button class="details-button" data-id="${place.id}">View Details</button>
    `;
    // Append the created element to the places list
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
