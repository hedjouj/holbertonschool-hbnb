from app.models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, user, place, content):
        super().__init__()
        self.user = user      # instance de User
        self.place = place    # instance de Place
        self.content = content
