"""
SELECT QUERIES
"""
from flask_course_2 import db, app
from flask_course_2.database import models
from sqlalchemy import and_

with app.app_context():
    films = db.session.query(models.Film).order_by(models.Film.rating.desc()).all()

with app.app_context():
    chamber = db.session.query(models.Film).filter(models.Film.title == 'Harry Potter and Chamber of Secrets').first()

with app.app_context():
    azkaban = db.session.query(models.Film).filter_by(title='Harry Potter and the Prizoner of Azkaban').first()

with app.app_context():
    and_1 = db.session.query(models.Film).filter(
        models.Film.title != 'Harry Potter and Chamber of Secrets',
        models.Film.rating >= 7.5
    ).all()

with app.app_context():
    and_2 = db.session.query(models.Film).filter(
        and_(
            models.Film.title != 'Harry Potter and Chamber of Secrets',
            models.Film.rating >= 7.5
        )
    ).all()

with app.app_context():
    deadly_hallow = db.session.query(models.Film).filter(
        models.Film.title.ilike('%Deathly%')
    ).all()

with app.app_context():
    length = db.session.query(models.Film).filter(
        ~models.Film.length.in_((146, 161))
    )[:3]


"""
JOIN QUERIES
"""
with app.app_context():
    films_with_actors = db.session.query(models.Film).join(models.Film.actors).all()
print(films_with_actors)