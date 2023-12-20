from flask_restful import Resource
from marshmallow import ValidationError
from flask_course_2 import db
from flask_course_2.database.models import Actor
from flask import request
from flask_course_2.schemas.actors import ActorSchema


class ActorListApi(Resource):
    actor_schema = ActorSchema()

    def get(self, id=None):
        if not id:
            actors = db.session.query(Actor).all()
            return self.actor_schema.dump(actors, many=True), 200
        film = db.session.query(Actor).filter_by(id=id).first()
        if film:
            return self.actor_schema.dump(film), 200
        return film, 404

    def post(self):
        try:
            actor = self.actor_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 200

    def put(self, id):
        actor = db.session.query(Actor).filter_by(id=id).first()
        if not actor:
            return "", 404
        try:
            actor = self.actor_schema.load(request.json, instance=actor, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 200

    @staticmethod
    def patch(id):
        pass

    @staticmethod
    def delete(id):
        pass
