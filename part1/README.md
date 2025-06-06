
# HBnB Project

## Introduction
The HBNB project is a mini-version of the Airbnb website.
The user can set some informations about the place, users, review and amenity.
This document constitutes the complete technical information for this project.
It brings together all the UML diagrams produced to illustrate the application architecture, the business logic and the communication flows between layers. 
The goal is to provide a clear, readable and structured explanation of our project.



## Package Diagram 
In this diagramm, the purpose is to show how the global architecture of the application work. It illustrates how to application is modularly divided into three keys logical layers. 
This diagram helps developers quickly understand the structure and responsibility of each major part of the application without diving into the implementation details.

```mermaid
graph TD
    subgraph UserInterface
    end

    subgraph BusinessLogic
    end

    subgraph DataBase
    end

    UserInterface --> BusinessLogic
    BusinessLogic --> DataBase
```

    
## Class Diagram 

This diagram describe the interaction with the différent Logic component.
First the place have some amenity, a amenity cannot exist without place. 
A place is located by a user, this user can make a review about the quality of service. 
AMENITY, USER, PLACE AND REVIEW are the entity use by the website via the BusinessLogicLayer
Relation between place and review. 
1 place can have many review
1 Review is written by one user and one place
1 user can create many review

```mermaid
classDiagram
direction TB
namespace BusinessLogicLayer {


    class AmenityEntity {
+int idAmenity
    +String name
    +String description
    +int idPlace
    +Date dateCreation
    +Date dateModification
    +createAmenity()
    +updateAmenity()
    +deleteAmenity()
    }

    class ReviewEntity {
    +Float rating
    +String comment
    +Date dateCreation
    +Date dateModification
    +int idPlace
    +int idUser
    +listReviewByPlace(idPlace) List Review
    +listReviewByUser(idUser) List Review
+createReview()
    +updateReview()
    +deleteReview()
    }

    class UserEntity {
    +int idUser
    +String firstName
    +String lastName
    +String email
    +String password
    +bool isAdmin
    +Date dateCreation
    +Date dateModification
    +isAdmin()
    +createUser()
    +updateUser()
    +deleteUser()
+listUser()
+listAdmin()
    }

    class PlaceEntity {
    +int idPlace
    +String title
    +String description
    +Float price
    +Float latitude
    +Float longitude
    +Date dateCreation
    +Date dateModification
    +createPlace()
    +updatePlace()
    +deletePlace()
+listPlace()
+listAmenity(idPlace) List:Amenity
    }
}
    PlaceEntity *-- AmenityEntity
    PlaceEntity "1" -- "*" ReviewEntity
    ReviewEntity "*" -- "1" UserEntity
```
