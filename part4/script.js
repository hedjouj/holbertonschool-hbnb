function getCookie(name) {
    const cookieValue = document.cookie
      .split("; ")
      .find((row) => row.startsWith(name))
      ?.split("=")[1];
    return cookieValue;
  }
  
  /* 
    This is a SAMPLE FILE to get you started.
    Please, follow the project instructions to complete the tasks.
  */
  
  function checkAuthentication() {
    const token = getCookie("token");
    const loginLink = document.getElementById("login-link");
    // const logoutLink = document.getElementById("logout-link");
    const placesList = document.getElementById("places-list");
    const addReviewBtn = document.getElementById("add-review-btn");
    const footer = document.querySelector('footer');
  
    if (!token) {
      loginLink.style.display = "block";
      loginLink.textContent = "Login";
      loginLink.href = "login.html";
      /**logoutLink.style.display = "none";**/

      // Hide add review button if not logged in
      if (addReviewBtn) {
        addReviewBtn.style.display = "none";
      }

      if (placesList) {
        placesList.innerHTML =
          `<a href="login.html">
            <p class='noLogged'>Login to display places.</p>
          </a>`;
          footer.style.position = 'fixed';
      }
    } else {
      loginLink.style.display = "block";
      loginLink.textContent = "Logout";
      loginLink.href = "#";
      loginLink.onclick = function(event) {
        event.preventDefault();
        deleteTokenCookie();
        window.location.href = "login.html";
      };
      
      // Show add review button if logged in and on place details page
      if (addReviewBtn) {
        addReviewBtn.style.display = "block";
      }
      
      //logoutLink.style.display = "block";
      if (placesList) {
        fetchPlaces(token);
      }
    }
  }
  
  
  /** Login/Logout Form  */
  document.addEventListener("DOMContentLoaded", () => {
    // Authentification check for user based on the token cookie
    checkAuthentication();
  
    // Logout functionnality, deleting the cookie token
    const logoutLink = document.getElementById("logout-link");
    if (logoutLink) {
      logoutLink.addEventListener("click", function (event) {
        event.preventDefault();
        deleteTokenCookie();
        window.location.href = "login.html";
      });
    }
  
    // Submit event for login ( receiveing email and password from form)
    const loginForm = document.getElementById("login-form");
    if (loginForm) {
      loginForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;
  
        try {
          await loginUser(email, password);
        } catch (error) {
          console.log("error:" + error);
        }
      });
    }

    // Add Review Form Submission
    const reviewForm = document.getElementById("review-form");
    if (reviewForm) {
      reviewForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const token = getCookie("token");
        const urlParams = new URLSearchParams(window.location.search);
        const placeId = urlParams.get("id");
        const rating = document.getElementById("rating").value;
        const text = document.getElementById("text").value;

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
          await submitReview(token, placeId, rating, text);
        } catch (error) {
          console.error("Error submitting review:", error);
          alert("Failed to submit review. Please try again.");
        }
      });
    }

    // Add Review Button Click Handler
    const addReviewBtn = document.getElementById("add-review-btn");
    if (addReviewBtn) {
      addReviewBtn.addEventListener("click", function() {
        const urlParams = new URLSearchParams(window.location.search);
        const placeId = urlParams.get("id");
        if (placeId) {
          window.location.href = `add_review.html?id=${placeId}`;
        }
      });
    }
  
  });
  
  // Fch detailed place if token and place id identified
  const token = getCookie("token");
  const urlParams = new URLSearchParams(window.location.search);
  const placeId = urlParams.get("id");
  try {
    if (token && placeId) {
      fetchDetailedPlace(token, placeId);
    }
  } catch (error) {
    console.error(error);
  }
  
  
  /** Login User */
  /** Login User avec gestion d'erreurs améliorée */
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
      document.cookie = `token=${data.access_token}; path=/`;
      window.location.href = "index.html";
      console.log(`${data.access_token}`);
    } else {
      // Gérer différents types d'erreurs
      let errorMessage = "Login failed. Please try again.";
      
      if (response.status === 401) {
        errorMessage = "Invalid email or password.";
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
  
  /** Places fetch and display */
  async function fetchPlaces(token) {
    try {
      const response = await fetch("http://127.0.0.1:5000/api/v1/places/", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      const places = await response.json();
      displayPlaces(places);
    } catch (error) {
      console.error("Error fetching places:", error);
    }
  }
  
  
  function displayPlaces(places) {
    const placesList = document.getElementById("places-list");
    if (!placesList)
      return;
    placesList.innerHTML = "";
    
    places.forEach((place) => {
      const placeCard = document.createElement("div");
      placeCard.className = "place-card";
      placeCard.innerHTML = `
        <a href="place.html?id=${place.id}" class="place-card-image">
          ${place.title}
        </a>
        <div class="place-card-content">
          <h2>${place.title}</h2>
          <p class="description">${place.description}</p>
          <p class="price-card"><strong>${place.price} €</strong> per night</p>
        </div>
      `;
      placesList.appendChild(placeCard);
    });
    /*applyPriceFilter();*/
  }
  
  /** Place Details Fetch and Display */
  async function fetchDetailedPlace(token, placeId) {
    try {
      const response = await fetch(
        `http://127.0.0.1:5000/api/v1/places/${placeId}`,
        {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      if (response.ok) {
        const detailedPlace = await response.json();
        displayDetailedPlaces(detailedPlace);
      } else {
        console.error("Failed to fetch detailed place.");
      }
    } catch (error) {
      console.error("Error fetching place detail:", error);
    }
  }
  
  function displayDetailedPlaces(place) {
    const placeDetailsSection = document.getElementById("place-details");
    if (!placeDetailsSection) return;

    // Create place info section with required classes
    placeDetailsSection.innerHTML = `
      <div class="place-info">
        <h1 class="detailedTitle">${place.title}</h1>
        
        <div class="host-info">
          <h3>Hosted by <span class="host-name">${place.owner ? place.owner.first_name + ' ' + place.owner.last_name : 'Unknown Host'}</span></h3>
          <p>Host since: <span class="host-since">${place.owner ? new Date(place.owner.created_at).getFullYear() : 'Unknown'}</span></p>
        </div>

        <div class="place-description">
          <h3>About this place</h3>
          <p class="detailedDescription">${place.description}</p>
        </div>

        <div class="price-info">
          <h3>Price: <span class="place-price">${place.price} €</span> per night</h3>
        </div>

        <div class="amenities">
          <h3>Amenities</h3>
          <p class="amenities-text">What this place offers:</p>
          <ul class="amenities-list">
            ${place.amenities && place.amenities.length > 0 
              ? place.amenities.map(amenity => `<li>${amenity.name}</li>`).join('') 
              : '<li>No amenities listed</li>'}
          </ul>
        </div>
      </div>
    `;

    // Display reviews
    displayReviews(place.reviews || []);
  }

  function displayReviews(reviews) {
    const reviewsSection = document.getElementById("reviews");
    if (!reviewsSection) return;

    reviewsSection.innerHTML = `
      <div class="reviews-section">
        <h3>Reviews</h3>
        <div id="reviews-container">
          ${reviews.length > 0 
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
  
  function deleteTokenCookie() {
    document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";
  }