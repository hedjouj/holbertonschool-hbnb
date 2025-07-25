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
    if (loginLink) loginLink.style.display = token ? 'none' : 'block';
    return token;
}
window.allPlaces = [];

document.addEventListener('DOMContentLoaded', () => {
    // Login form
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            try {
                const response = await fetch('http://localhost:5000/api/v1/auth/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });
                if (!response.ok) throw new Error('Invalid credentials');
                const data = await response.json();
                const token = data.token || data.access_token;
                if (token) {
                    setCookie('token', token, 7);
                    window.location.href = 'index.html';
                } else {
                    alert('Login failed: No token received');
                }
            } catch (error) {
                alert('Login failed: ' + error.message);
            }
        });
        return;
    }

    // Add review form
    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const rating = document.getElementById('rating').value;
            const text = document.getElementById('text').value;
            const params = new URLSearchParams(window.location.search);
            const placeId = params.get('place_id');
            const token = getCookie('token');
            if (!token) {
                alert('You must be logged in to add a review.');
                return;
            }
            try {
                const response = await fetch(`http://localhost:5000/api/v1/reviews/places/${placeId}/reviews`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`
                    },
                    body: JSON.stringify({ rating, text })
                });
                if (!response.ok) throw new Error('Failed to add review');
                window.location.href = `place.html?place_id=${placeId}`;
            } catch (error) {
                alert('Failed to add review: ' + error.message);
            }
        });
        return;
    }

    // Place details page
    if (document.getElementById('place-details')) {
        const params = new URLSearchParams(window.location.search);
        const placeId = params.get('place_id');
        if (placeId) {
            fetchPlaceDetails(placeId);
            fetchPlaceReviews(placeId);
            // Show add review button if logged in
            const token = checkAuthentication();
            const addReviewBtn = document.getElementById('add-review-btn');
            if (addReviewBtn) {
                addReviewBtn.style.display = token ? 'block' : 'none';
                addReviewBtn.onclick = () => {
                    window.location.href = `add_review.html?place_id=${placeId}`;
                };
            }
        }
        return;
    }

    // List of places page
    if (document.getElementById('places-list')) {
        checkAuthentication();
        fetchPlaces();
        // Populate price filter
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
            priceFilter.addEventListener('change', () => {
                let filtered = window.allPlaces;
                const selected = priceFilter.value;
                if (selected !== 'all') {
                    const maxPrice = parseFloat(selected);
                    filtered = window.allPlaces.filter(place => Number(place.price) <= maxPrice);
                }
                displayPlaces(filtered);
            });
        }
    }
});

async function fetchPlaces() {
    try {
        const response = await fetch('http://localhost:5000/api/v1/places');
        if (!response.ok) throw new Error('Network response was not ok');
        const data = await response.json();
        let places = [];
        if (data && Array.isArray(data.places)) places = data.places;
        else if (Array.isArray(data)) places = data;
        else return;
        window.allPlaces = places;
        displayPlaces(places);
    } catch (error) {
        console.error('Error fetching places:', error);
    }
}

function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    if (!placesList) return;
    placesList.innerHTML = '';
    places.forEach(place => {
        const card = document.createElement('div');
        card.className = 'place-card';
        card.innerHTML = `
            <h3>${place.name || place.title || 'No Name'}</h3>
            <p>Price per night: $${place.price !== undefined ? place.price : 'N/A'}</p>
            <button class="details-button" onclick="window.location.href='place.html?place_id=${place.id}'">View Details</button>
        `;
        placesList.appendChild(card);
    });
}

async function fetchPlaceDetails(placeId) {
    try {
        const response = await fetch(`http://localhost:5000/api/v1/places/${placeId}`);
        if (!response.ok) throw new Error('Network response was not ok');
        const place = await response.json();
        const detailsSection = document.getElementById('place-details');
        if (!detailsSection) return;
        let hostInfo = '';
        if (place.owner) {
            hostInfo = `<div class="place-info"><strong>Host:</strong> ${place.owner.first_name} ${place.owner.last_name} (${place.owner.email})</div>`;
        }
        let amenities = '';
        if (Array.isArray(place.amenities) && place.amenities.length > 0) {
            amenities = `<div class="place-info"><strong>Amenities:</strong><ul>${place.amenities.map(a => `<li>${a.name}</li>`).join('')}</ul></div>`;
        }
        detailsSection.innerHTML = `
            <div class="place-info"><strong>Title:</strong> ${place.title || place.name}</div>
            ${hostInfo}
            <div class="place-info"><strong>Price:</strong> $${place.price}</div>
            <div class="place-info"><strong>Description:</strong> ${place.description}</div>
            ${amenities}
        `;
    } catch (error) {
        console.error('Error fetching place details:', error);
    }
}

async function fetchPlaceReviews(placeId) {
    try {
        const response = await fetch(`http://localhost:5000/api/v1/reviews/places/${placeId}/reviews`);
        if (!response.ok) throw new Error('Network response was not ok');
        const reviews = await response.json();
        displayPlaceReviews(reviews);
    } catch (error) {
        console.error('Error fetching reviews:', error);
    }
}

function displayPlaceReviews(reviews) {
    const reviewsSection = document.getElementById('reviews');
    if (!reviewsSection) return;
    reviewsSection.innerHTML = '<h2>Reviews</h2>';
    if (!Array.isArray(reviews) || reviews.length === 0) {
        reviewsSection.innerHTML += '<p>No reviews yet.</p>';
        return;
    }
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


