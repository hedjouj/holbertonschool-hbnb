## Entity-Relationship Diagram

```mermaid
erDiagram
    USER ||--o{ PLACES : own
    PLACES }|..|{ AMENITY : has 
    USER ||--o{ REVIEW : write
    PLACES ||--o{ REVIEW : receive
```