# 🏨 HBnB - REST API - Part 2

Ce projet fait partie de l'ensemble HBnB de Holberton School. Il s'agit ici de la **deuxième partie** qui introduit une **architecture RESTful** pour gérer les entités principales de l'application (users, places, amenities, reviews...).

## 📚 Objectif

Créer une API web en utilisant **Flask + Flask-RESTx**, organisée selon une architecture en **trois couches** :

- **Presentation Layer (API)** : Gère les routes HTTP.
- **Business Logic Layer (Facade)** : Contient la logique métier (vérifications, validations...).
- **Persistence Layer (InMemoryRepository)** : Simule une base de données via des objets Python.

---

## 🧱 Entités gérées

- `User` : utilisateur.
- `Place` : lieu mis en location.
- `Amenity` : équipement.
- `Review` : avis laissé sur un lieu.

---

## 🚀 Endpoints disponibles

Tous les endpoints sont accessibles via `/api/v1/`.

Exemples :

- `POST /reviews/` : créer un avis.
- `GET /reviews/<id>` : récupérer un avis.
- `PUT /reviews/<id>` : mettre à jour un avis.
- `DELETE /reviews/<id>` : supprimer un avis.
- `GET /places/<place_id>/reviews` : lister les avis d’un lieu.

---

## 🧪 Tests & Validation

### ✅ Résultat des tests `unittest`

```bash
$ python3 -m unittest discover app/tests
.....
----------------------------------------------------------------------
Ran 5 tests in 0.032s

OK
