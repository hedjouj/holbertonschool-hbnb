import uuid
from datetime import datetime


class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Mets à jour la modif date(upadate_at) quand l'obj est changé"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Mets à jours les attributs de l'obj à l'aide d'un dico"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Mets à jour la date de modif