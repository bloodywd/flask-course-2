from flask_course_2 import api
from flask_course_2.resources.actors import ActorListApi
from flask_course_2.resources.films import FilmListApi
from flask_course_2.resources.smoke import Smoke


api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)
api.add_resource(ActorListApi, '/actors', '/actors/<id>', strict_slashes=False)
