from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_course_2.database.models import Actor
from marshmallow_sqlalchemy.fields import Nested


class ActorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Actor
        load_instance = True
        include_fk = True
    films = Nested('FilmSchema', many=True, exclude=('actors',))
