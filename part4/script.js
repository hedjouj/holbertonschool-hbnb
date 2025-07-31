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

function deleteTokenCookie() {
  document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";
}

function checkAuthentication() {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');

  if (!loginLink) return;

  if (!token) {
    loginLink.style.display = 'block';
    loginLink.textContent = 'Login';
    loginLink.href = 'login.html';
    // Fetch places without authentication - but show login message
    const placesList = document.getElementById('places-list');
    if (placesList) {
      placesList.innerHTML = `<a href="login.html"><p class='noLogged'>Login to display places.</p></a>`;
    }
  } else {
    loginLink.style.display = 'block';
    loginLink.textContent = 'Logout';
    loginLink.href = '#';
    loginLink.onclick = function(event) {
      event.preventDefault();
      deleteTokenCookie();
      window.location.href = 'login.html';
    };
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
      
      const email = document.getElementById('email').value.trim();
      const password = document.getElementById('password').value.trim();

      // Validation côté client
      if (!email || !password) {
        displayErrorMessage("Please fill in both email and password fields.");
        return;
      }

      // Validation basique de l'email
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        displayErrorMessage("Please enter a valid email address.");
        return;
      }

      try {
        await loginUser(email, password);
      } catch (error) {
        console.error("Login error:", error);
        displayErrorMessage("An unexpected error occurred. Please try again.");
      }
    });
    return; // Don't run the rest of the code on login.html
  }

  // Place details page
  if (document.getElementById('place-details')) {
    const placeId = getPlaceIdFromURL();
    if (placeId) {
      fetchPlaceDetails(placeId);
      fetchPlaceReviews(placeId);
    }
  }

  // Index page - places list
  if (document.getElementById('places-list')) {
    checkAuthentication();
  }

  // Populate the price filter dropdown
  const priceFilter = document.getElementById('price-filter');
  if (priceFilter) {
    const options = [
      { value: 'all', text: 'All' },
      { value: '10', text: '10' },
      { value: '50', text: '50' },
      { value: '100', text: '100' }
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
        filtered = window.allPlaces.filter(place => {
          const placePrice = parseFloat(place.price);
          return placePrice <= maxPrice;
        });
      }
      displayPlaces(filtered);
    });
  }

  // Review form handling
  const reviewForm = document.getElementById('review-form');
  if (reviewForm) {
    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const token = getCookie('token');
      const placeId = getPlaceIdFromURL();
      const rating = document.getElementById('rating').value;
      const textElement = document.getElementById('text') || document.getElementById('review-text');

      if (!token) {
        alert("You must be logged in to add a review.");
        window.location.href = "login.html";
        return;
      }

      if (!placeId) {
        alert("Place ID is missing.");
        return;
      }

      try {
        await submitReview(token, placeId, rating, textElement.value);
      } catch (error) {
        console.error("Error submitting review:", error);
        alert("Failed to submit review. Please try again.");
      }
    });
  }
});

/** Login User avec gestion d'erreurs */
async function loginUser(email, password) {
  console.log(email, password);
  
  // Cacher le message d'erreur précédent s'il existe
  hideErrorMessage();
  
  try {
    const response = await fetch("http://127.0.0.1:5000/api/v1/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    if (response.ok) {
      const data = await response.json();
      const token = data.access_token || data.token;
      if (token) {
        setCookie('token', token, 7);
        window.location.href = 'index.html';
      } else {
        displayErrorMessage('Login failed: No token received');
      }
    } else {
      // Gérer différents types d'erreurs
      let errorMessage = "Login failed. Please try again.";
      
      if (response.status === 401) {
        errorMessage = "Invalid email or password. Please check your credentials.";
      } else if (response.status === 400) {
        errorMessage = "Please fill in all required fields.";
      } else if (response.status >= 500) {
        errorMessage = "Server error. Please try again later.";
      }
      
      // Essayer de récupérer le message d'erreur du serveur
      try {
        const errorData = await response.json();
        if (errorData.message) {
          errorMessage = errorData.message;
        }
      } catch (e) {
        // Utiliser le message par défaut si impossible de parser la réponse
      }
      
      displayErrorMessage(errorMessage);
    }
  } catch (error) {
    console.error("Network error:", error);
    displayErrorMessage("Network error. Please check your connection and try again.");
  }
}

/** Afficher le message d'erreur */
function displayErrorMessage(message) {
  // Chercher s'il existe déjà un container d'erreur
  let errorContainer = document.getElementById("error-message");
  
  if (!errorContainer) {
    // Créer le container d'erreur s'il n'existe pas
    errorContainer = document.createElement("div");
    errorContainer.id = "error-message";
    errorContainer.className = "error-message";
    
    // L'insérer avant le formulaire de login
    const loginForm = document.getElementById("login-form");
    if (loginForm) {
      loginForm.parentNode.insertBefore(errorContainer, loginForm);
    }
  }
  
  errorContainer.textContent = message;
  errorContainer.style.display = "block";
  
  // Faire disparaître le message après 5 secondes
  setTimeout(() => {
    hideErrorMessage();
  }, 5000);
}

/** Cacher le message d'erreur */
function hideErrorMessage() {
  const errorContainer = document.getElementById("error-message");
  if (errorContainer) {
    errorContainer.style.display = "none";
  }
}

function getPlaceIdFromURL() {
  const params = new URLSearchParams(window.location.search);
  return params.get('id') || params.get('place_id');
}

function fetchPlaceDetails(placeId) {
  const token = getCookie('token');
  const headers = {};
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, { headers })
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
      <div class="host-info">
        <h3>Hosted by <span class="host-name">${place.owner.first_name} ${place.owner.last_name}</span></h3>
        <p>Host since: <span class="host-since">${new Date(place.owner.created_at).getFullYear()}</span></p>
      </div>
    `;
  }

  let amenities = '';
  if (Array.isArray(place.amenities) && place.amenities.length > 0) {
    amenities = `
      <div class="amenities">
        <h3>Amenities</h3>
        <p class="amenities-text">What this place offers:</p>
        <ul class="amenities-list">
          ${place.amenities.map(a => `<li>${a.name}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  detailsSection.innerHTML = `
    <div class="place-info">
      <h1 class="detailedTitle">${place.title || place.name}</h1>
      ${hostInfo}
      <div class="place-description">
        <h3>About this place</h3>
        <p class="detailedDescription">${place.description}</p>
      </div>
      <div class="price-info">
        <h3>Price: <span class="place-price">${place.price} €</span> per night</h3>
      </div>
      ${amenities}
    </div>
  `;
}

// Fetch places data using Fetch API and handle the response
async function fetchPlaces(token) {
  const headers = {};
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }
  
  try {
    const response = await fetch('http://127.0.0.1:5000/api/v1/places/', { headers });
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
    const placesList = document.getElementById('places-list');
    if (placesList && !token) {
      placesList.innerHTML = `<a href="login.html"><p class='noLogged'>Login to display places.</p></a>`;
    }
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
  
  if (!places || places.length === 0) {
    placesList.innerHTML = '<p>No places available.</p>';
    return;
  }
  
  // Iterate over the places data
  places.forEach(place => {
    // For each place, create a div element and set its content
    const card = document.createElement('div');
    card.className = 'place-card';
    card.innerHTML = `
      <h3>${place.name || place.title || 'No Name'}</h3>
      <p class="description">${place.description || ''}</p>
      <p class="price-card"><strong>${place.price !== undefined ? place.price : 'N/A'} €</strong> per night</p>
      <button class="details-button" onclick="window.location.href='place.html?id=${place.id}'">View Details</button>
    `;
    // Append the created element to the places list
    placesList.appendChild(card);
  });
}

function fetchPlaceReviews(placeId) {
  const token = getCookie('token');
  const headers = {};
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}/reviews`, { headers })
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
      displayPlaceReviews([]);
    });
}

function displayPlaceReviews(reviews) {
  const reviewsSection = document.getElementById('reviews');
  if (!reviewsSection) return;
  
  reviewsSection.innerHTML = `
    <div class="reviews-section">
      <h3>Reviews</h3>
      <div id="reviews-container">
        ${reviews && reviews.length > 0 
          ? reviews.map(review => `
              <div class="review-card">
                <div class="review-header">
                  <h4>${review.user ? review.user.first_name + ' ' + review.user.last_name : 'Anonymous'}</h4>
                  <div class="rating">${createStarRating(review.rating)}</div>
                </div>
                <p class="review-comment">${review.text}</p>
                <small class="review-date">${new Date(review.created_at).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}</small>
              </div>
            `).join('')
          : '<p class="no-reviews">No reviews available for this place.</p>'
        }
      </div>
    </div>
  `;
}

function createStarRating(rating) {
  const fullStars = '★'.repeat(Math.floor(rating));
  const emptyStars = '☆'.repeat(5 - Math.floor(rating));
  return fullStars + emptyStars;
}

/** Submit Review */
async function submitReview(token, placeId, rating, text) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}/reviews`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      },
      body: JSON.stringify({
        rating: parseInt(rating),
        text: text
      })
    });

    if (response.ok) {
      const result = await response.json();
      alert("Review submitted successfully!");
      window.location.href = `place.html?id=${placeId}`;
    } else {
      const errorData = await response.json();
      throw new Error(errorData.message || "Failed to submit review");
    }
  } catch (error) {
    console.error("Error submitting review:", error);
    throw error;
  }
}