from sqlalchemy import func
from flask_course_2 import db
from flask_restful import Resource
from flask_course_2.database.models import Film


class AggregationAPI(Resource):
    def get(self):
        film_count = db.session.query(func.count(Film.id)).scalar()
        max_rating = db.session.query(func.max(Film.rating)).scalar()
        min_rating = db.session.query(func.min(Film.rating)).scalar()
        avg_rating = db.session.query(func.avg(Film.rating)).scalar()
        sum_rating = db.session.query(func.sum(Film.rating)).scalar()
        return {
            'count': film_count,
            'max_rating': max_rating,
            'min_rating': min_rating,
            'avg_rating': avg_rating,
            'sum_rating': sum_rating
        }