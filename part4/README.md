# HBnB Application - Frontend avec Thème Twix

## 🍫 Aperçu

Application web HBnB avec une interface utilisateur inspirée du thème Twix, offrant une expérience visuelle chaleureuse avec des couleurs dorées et chocolat.

## 📁 Structure du Projet

```
part4/
├── index.html          # Page principale - liste des places
├── login.html          # Page de connexion
├── place.html          # Détails d'une place
├── add_review.html     # Formulaire d'ajout d'avis
├── styles.css          # Styles CSS avec thème Twix
├── scripts.js          # JavaScript pour toutes les fonctionnalités
└── logo.png           # Logo de l'application (à ajouter)
```

## 🚀 Installation et Démarrage

### 1. Démarrer le serveur backend

```bash
cd part3
python run.py
```

Le serveur Flask démarrera sur `http://localhost:5000`

### 2. Servir les fichiers frontend

**Option A : Serveur Python simple**
```bash
cd part4
python -m http.server 8000
```

**Option B : Live Server (VS Code)**
- Installer l'extension "Live Server"
- Clic droit sur `index.html` → "Open with Live Server"

**Option C : Serveur Node.js**
```bash
cd part4
npx http-server -p 8000
```

### 3. Accéder à l'application

Ouvrir `http://localhost:8000` dans votre navigateur

## 🎨 Thème Twix

### Palette de couleurs
- **Or doré** : `#ffd700` - Accents et liens
- **Chocolat foncé** : `#8b4513` - Textes principaux
- **Caramel** : `#cd853f` - Bordures et boutons
- **Crème** : `#fff8dc` - Arrière-plans

### Éléments visuels
- Dégradés chocolat dans le header
- Boutons avec effet doré
- Cards avec ombres caramel
- Animations de survol fluides

## ⚡ Fonctionnalités Implémentées

### 🏠 Page Index (index.html)
- ✅ Affichage de la liste des places
- ✅ Filtre par prix (10$, 50$, 100$, Tous)
- ✅ Gestion de l'authentification
- ✅ Navigation vers les détails

### 🔐 Page Login (login.html)
- ✅ Formulaire de connexion
- ✅ Gestion des tokens JWT
- ✅ Messages d'erreur/succès
- ✅ Redirection automatique

### 📍 Page Place Details (place.html)
- ✅ Affichage des détails complets
- ✅ Informations propriétaire
- ✅ Liste des équipements
- ✅ Avis des utilisateurs
- ✅ Formulaire d'ajout d'avis (si connecté)

### ⭐ Page Add Review (add_review.html)
- ✅ Protection par authentification
- ✅ Validation des données
- ✅ Soumission d'avis avec note
- ✅ Gestion des erreurs

## 🔧 Configuration API

### Endpoints utilisés
```javascript
const API_BASE = 'http://localhost:5000/api/v1';

// Authentification
POST /auth/login

// Places
GET /places
GET /places/{id}

// Avis
GET /reviews/places/{place_id}/reviews
POST /reviews/

// Utilisateurs
GET /users/{id}
```

### Headers requis
```javascript
{
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + token  // Pour les requêtes authentifiées
}
```

## 🧪 Tests

Suivre le [Guide de Test](testing_guide.md) pour valider toutes les fonctionnalités.

### Comptes de test
Créer des utilisateurs via l'API ou utiliser les données de test de votre base.

### Données de test requises
- Au moins 3 places avec différents prix
- Quelques avis existants
- Un utilisateur avec privilèges admin (optionnel)

## 🐛 Dépannage

### Erreurs CORS
```javascript
// Dans run.py, vérifiez que CORS est configuré :
from flask_cors import CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})
```

### Token non reconnu
1. Vérifier que le serveur Flask fonctionne
2. Vérifier les cookies dans les DevTools
3. Tester l'endpoint login avec Postman

### Places ne se chargent pas
1. Vérifier l'URL de l'API dans scripts.js
2. Vérifier la base de données
3. Regarder la console développeur

### Styles non appliqués
1. Vérifier que styles.css est dans le même dossier
2. Vérifier les chemins relatifs
3. Vider le cache du navigateur

## 📱 Responsive Design

L'application est optimisée pour :
- 📱 Mobile (320px+)
- 📱 Tablette (768px+)
- 💻 Desktop (1024px+)

## 🔐 Sécurité

- Tokens JWT stockés en cookies sécurisés
- Validation côté client et serveur
- Protection des routes authentifiées
- Échappement HTML pour prévenir XSS

## 🎯 Améliorations futures

- [ ] Système de favoris
- [ ] Pagination des places
- [ ] Upload d'images
- [ ] Notifications en temps réel
- [ ] Mode sombre/clair
- [ ] Géolocalisation

## 👥 Contribution

1. Fork le projet
2. Créer une branche feature
3. Commiter les changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

---

**Développé avec 🍫 et beaucoup de ☕**