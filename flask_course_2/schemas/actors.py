from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_course_2.database.models import Actor


class ActorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Actor
        load_instance = True
