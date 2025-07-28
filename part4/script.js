/* 
  HBnB Application - JavaScript complet
  Implémentation de toutes les fonctionnalités requises
*/

// Fonctions utilitaires pour les cookies
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

// Variables globales
window.allPlaces = [];
let currentUser = null;

// Fonction pour vérifier l'authentification
function checkAuthentication() {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');

  if (loginLink) {
    if (!token) {
      loginLink.style.display = 'block';
    } else {
      loginLink.style.display = 'none';
    }
  }

  // Pour la page des détails de place
  const addReviewSection = document.getElementById('add-review');
  if (addReviewSection) {
    if (!token) {
      addReviewSection.style.display = 'none';
    } else {
      addReviewSection.style.display = 'block';
    }
  }

  return token;
}

// Fonction pour obtenir l'ID de place depuis l'URL
function getPlaceIdFromURL() {
  const params = new URLSearchParams(window.location.search);
  return params.get('place_id');
}

// === FONCTIONS POUR LA PAGE INDEX ===

// Récupérer la liste des places
async function fetchPlaces(token) {
  const headers = {
    'Content-Type': 'application/json'
  };
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  try {
    const response = await fetch('http://localhost:5000/api/v1/places', { 
      method: 'GET',
      headers 
    });
    
    if (!response.ok) {
      throw new Error('Erreur lors de la récupération des places');
    }
    
    const data = await response.json();
    let places = [];
    
    if (data && Array.isArray(data.places)) {
      places = data.places;
    } else if (Array.isArray(data)) {
      places = data;
    }
    
    window.allPlaces = places;
    displayPlaces(places);
  } catch (error) {
    console.error('Erreur lors de la récupération des places:', error);
    showMessage('Erreur lors de la récupération des places', 'error');
  }
}

// Afficher la liste des places
function displayPlaces(places) {
  const placesList = document.getElementById('places-list');
  if (!placesList) return;

  placesList.innerHTML = '';

  if (!places || places.length === 0) {
    placesList.innerHTML = '<p>Aucune place disponible.</p>';
    return;
  }

  places.forEach(place => {
    const card = document.createElement('div');
    card.className = 'place-card';
    card.setAttribute('data-price', place.price);
    
    card.innerHTML = `
      <h3>${place.title || place.name || 'Sans titre'}</h3>
      <p><strong>Prix par nuit:</strong> $${place.price !== undefined ? place.price : 'N/A'}</p>
      <p><strong>Description:</strong> ${place.description || 'Aucune description'}</p>
      <button class="details-button" onclick="viewPlaceDetails('${place.id}')">Voir les détails</button>
    `;
    
    placesList.appendChild(card);
  });
}

// Fonction pour rediriger vers les détails d'une place
function viewPlaceDetails(placeId) {
  window.location.href = `place.html?place_id=${placeId}`;
}

// === FONCTIONS POUR LA PAGE PLACE DETAILS ===

// Récupérer les détails d'une place
async function fetchPlaceDetails(token, placeId) {
  const headers = {
    'Content-Type': 'application/json'
  };
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  try {
    const response = await fetch(`http://localhost:5000/api/v1/places/${placeId}`, {
      method: 'GET',
      headers
    });

    if (!response.ok) {
      throw new Error('Place non trouvée');
    }

    const place = await response.json();
    displayPlaceDetails(place);
  } catch (error) {
    console.error('Erreur lors de la récupération des détails:', error);
    showMessage('Erreur lors de la récupération des détails de la place', 'error');
  }
}

// Afficher les détails d'une place
function displayPlaceDetails(place) {
  const detailsSection = document.getElementById('place-details');
  if (!detailsSection) return;

  let hostInfo = '';
  if (place.owner) {
    hostInfo = `
      <div class="place-info">
        <strong>Propriétaire:</strong> ${place.owner.first_name} ${place.owner.last_name}
        <br><strong>Email:</strong> ${place.owner.email}
      </div>
    `;
  }

  let amenitiesInfo = '';
  if (place.amenities && Array.isArray(place.amenities) && place.amenities.length > 0) {
    amenitiesInfo = `
      <div class="place-info">
        <strong>Équipements:</strong>
        <ul>
          ${place.amenities.map(amenity => `<li>${amenity.name}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  let reviewsInfo = '';
  if (place.reviews && Array.isArray(place.reviews) && place.reviews.length > 0) {
    reviewsInfo = `
      <div class="place-info">
        <strong>Avis (${place.reviews.length}):</strong>
        <div id="place-reviews">
          ${place.reviews.map(review => `
            <div class="review-card">
              <p><strong>Note:</strong> ${review.rating}/5</p>
              <p>${review.text}</p>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  detailsSection.innerHTML = `
    <h1>${place.title || place.name}</h1>
    <div class="place-info">
      <strong>Prix par nuit:</strong> $${place.price}
    </div>
    <div class="place-info">
      <strong>Description:</strong> ${place.description || 'Aucune description'}
    </div>
    <div class="place-info">
      <strong>Localisation:</strong> Latitude ${place.latitude}, Longitude ${place.longitude}
    </div>
    ${hostInfo}
    ${amenitiesInfo}
    ${reviewsInfo}
  `;
}

// === FONCTIONS POUR LES AVIS ===

// Récupérer les avis d'une place
async function fetchPlaceReviews(placeId) {
  try {
    const response = await fetch(`http://localhost:5000/api/v1/reviews/places/${placeId}/reviews`);
    
    if (!response.ok) {
      console.log('Aucun avis trouvé pour cette place');
      return;
    }

    const reviews = await response.json();
    displayPlaceReviews(reviews);
  } catch (error) {
    console.error('Erreur lors de la récupération des avis:', error);
  }
}

// Afficher les avis d'une place
function displayPlaceReviews(reviews) {
  const reviewsSection = document.getElementById('reviews');
  if (!reviewsSection) return;

  reviewsSection.innerHTML = '<h2>Avis des clients</h2>';

  if (!reviews || reviews.length === 0) {
    reviewsSection.innerHTML += '<p>Aucun avis pour le moment.</p>';
    return;
  }

  reviews.forEach(async (review) => {
    try {
      const userResponse = await fetch(`http://localhost:5000/api/v1/users/${review.user_id}`);
      let userName = 'Utilisateur inconnu';
      
      if (userResponse.ok) {
        const user = await userResponse.json();
        userName = `${user.first_name} ${user.last_name}`;
      }

      const reviewCard = document.createElement('div');
      reviewCard.className = 'review-card';
      reviewCard.innerHTML = `
        <p><strong>${userName}</strong> - Note: ${review.rating}/5</p>
        <p>${review.text}</p>
      `;
      
      reviewsSection.appendChild(reviewCard);
    } catch (error) {
      console.error('Erreur lors de la récupération des informations utilisateur:', error);
    }
  });
}

// Soumettre un nouvel avis
async function submitReview(token, placeId, reviewText) {
  if (!reviewText.trim()) {
    showMessage('Veuillez saisir un avis', 'error');
    return false;
  }

  try {
    const response = await fetch('http://localhost:5000/api/v1/reviews/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        text: reviewText,
        rating: 5, // Note par défaut, vous pouvez ajouter un champ de sélection
        place_id: placeId
      })
    });

    if (response.ok) {
      showMessage('Avis soumis avec succès !', 'success');
      document.getElementById('review-text').value = '';
      // Recharger les avis
      fetchPlaceReviews(placeId);
      return true;
    } else {
      const errorData = await response.json();
      showMessage('Erreur lors de la soumission: ' + (errorData.error || 'Erreur inconnue'), 'error');
      return false;
    }
  } catch (error) {
    console.error('Erreur lors de la soumission de l\'avis:', error);
    showMessage('Erreur lors de la soumission de l\'avis', 'error');
    return false;
  }
}

// === FONCTIONS UTILITAIRES ===

// Afficher un message à l'utilisateur
function showMessage(message, type) {
  // Supprimer les anciens messages
  const existingMessages = document.querySelectorAll('.message');
  existingMessages.forEach(msg => msg.remove());

  const messageDiv = document.createElement('div');
  messageDiv.className = `message ${type}`;
  messageDiv.textContent = message;
  
  document.body.insertBefore(messageDiv, document.body.firstChild);
  
  // Supprimer le message après 3 secondes
  setTimeout(() => {
    messageDiv.remove();
  }, 3000);
}

// === INITIALISATION AU CHARGEMENT DE LA PAGE ===

document.addEventListener('DOMContentLoaded', () => {
  const token = checkAuthentication();

  // === PAGE LOGIN ===
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
          throw new Error('Identifiants incorrects');
        }

        const data = await response.json();
        const accessToken = data.access_token;

        if (accessToken) {
          setCookie('token', accessToken, 7);
          showMessage('Connexion réussie ! Redirection...', 'success');
          setTimeout(() => {
            window.location.href = 'index.html';
          }, 1500);
        } else {
          throw new Error('Token non reçu');
        }
      } catch (error) {
        console.error('Erreur de connexion:', error);
        showMessage('Échec de la connexion: ' + error.message, 'error');
      }
    });
    return;
  }

  // === PAGE INDEX ===
  const placesList = document.getElementById('places-list');
  if (placesList) {
    // Récupérer les places
    fetchPlaces(token);

    // Configurer le filtre de prix
    const priceFilter = document.getElementById('price-filter');
    if (priceFilter) {
      // Ajouter les options de filtre
      const options = [
        { value: 'all', text: 'Tous les prix' },
        { value: '10', text: 'Moins de $10' },
        { value: '50', text: 'Moins de $50' },
        { value: '100', text: 'Moins de $100' }
      ];

      options.forEach(opt => {
        const option = document.createElement('option');
        option.value = opt.value;
        option.textContent = opt.text;
        priceFilter.appendChild(option);
      });

      // Ajouter l'événement de filtrage
      priceFilter.addEventListener('change', (event) => {
        const selectedValue = event.target.value;
        let filteredPlaces = window.allPlaces;

        if (selectedValue !== 'all') {
          const maxPrice = parseFloat(selectedValue);
          filteredPlaces = window.allPlaces.filter(place => {
            return parseFloat(place.price) <= maxPrice;
          });
        }

        displayPlaces(filteredPlaces);
      });
    }
    return;
  }

  // === PAGE PLACE DETAILS ===
  const placeDetails = document.getElementById('place-details');
  if (placeDetails) {
    const placeId = getPlaceIdFromURL();
    
    if (placeId) {
      fetchPlaceDetails(token, placeId);
      fetchPlaceReviews(placeId);

      // Configurer le formulaire d'avis
      const reviewForm = document.getElementById('review-form');
      if (reviewForm && token) {
        reviewForm.addEventListener('submit', async (event) => {
          event.preventDefault();
          const reviewText = document.getElementById('review-text').value;
          await submitReview(token, placeId, reviewText);
        });
      }
    } else {
      showMessage('ID de place manquant dans l\'URL', 'error');
    }
    return;
  }

  // === PAGE ADD REVIEW ===
  const reviewForm = document.getElementById('review-form');
  if (reviewForm && !placeDetails) {
    // Vérifier l'authentification
    if (!token) {
      window.location.href = 'index.html';
      return;
    }

    const placeId = getPlaceIdFromURL();
    if (!placeId) {
      showMessage('ID de place manquant', 'error');
      return;
    }

    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const reviewText = document.getElementById('review').value;
      const rating = document.getElementById('rating').value;
      
      try {
        const response = await fetch('http://localhost:5000/api/v1/reviews/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          },
          body: JSON.stringify({
            text: reviewText,
            rating: parseInt(rating),
            place_id: placeId
          })
        });

        if (response.ok) {
          showMessage('Avis soumis avec succès !', 'success');
          reviewForm.reset();
        } else {
          const errorData = await response.json();
          throw new Error(errorData.error || 'Erreur lors de la soumission');
        }
      } catch (error) {
        console.error('Erreur:', error);
        showMessage('Erreur lors de la soumission: ' + error.message, 'error');
      }
    });

    // Ajouter les options de notation
    const ratingSelect = document.getElementById('rating');
    if (ratingSelect) {
      for (let i = 1; i <= 5; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.textContent = `${i} étoile${i > 1 ? 's' : ''}`;
        ratingSelect.appendChild(option);
      }
    }
  }
});