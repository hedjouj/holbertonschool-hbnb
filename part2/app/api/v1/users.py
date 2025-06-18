from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace("users", description="User operations")
facade = HBnBFacade()

user_model = api.model("User", {
    "id": fields.String(readonly=True),
    "first_name": fields.String(required=True, max_length=50),
    "last_name": fields.String(required=True, max_length=50),
    "email": fields.String(required=True),
    "is_admin": fields.Boolean,
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime,
})
