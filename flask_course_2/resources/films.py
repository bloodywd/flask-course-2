from datetime import datetime
from flask_restful import Resource
from marshmallow import ValidationError
from flask_course_2 import db
from flask_course_2.database.models import Film
from flask_course_2.schemas.films import FilmSchema
from flask import request


class FilmListApi(Resource):
    film_schema = FilmSchema()

    def get(self, uuid=None):
        if not uuid:
            films = db.session.query(Film).all()
            return self.film_schema.dump(films, many=True), 200
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if film:
            return self.film_schema.dump(film), 200
        return film, 404

    def post(self):
        try:
            film = self.film_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 200

    def put(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return "", 404
        try:
            film = self.film_schema.load(request.json, instance=film, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 200

    def patch(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        print(film)
        if not film:
            return film, 404
        film_json = request.json
        title = film_json.get('title')
        release_date = (datetime.strptime(film_json.get('release_date'), '%B %d, %Y')
                        if film_json.get('release_date') else None)
        distributed_by = film_json.get('distributed_by')
        description = film_json.get('description')
        length = film_json.get('length')
        rating = film_json.get('rating')
        if title:
            film.title = title
        elif release_date:
            film.release_date = release_date
        elif distributed_by:
            film.distributed_by = distributed_by
        elif description:
            film.description = description
        elif length:
            film.length = length
        elif rating:
            film.rating = rating
        db.session.add(film)
        db.session.commit()

    @staticmethod
    def delete(uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return film, 404
        db.session.delete(film)
        db.session.commit()
        return '', 204
