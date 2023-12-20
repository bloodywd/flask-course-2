from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_course_2.database.models import Film


class FilmSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Film
        exclude = ['id']
        load_instance = True
