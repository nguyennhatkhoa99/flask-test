from http import HTTPStatus
from flask import Blueprint, request, jsonify
from flasgger import swag_from
from ..model.movie import MoviesModel
from ..schema.movie import MovieInfo, movie_schema
from ..model.movie import db
from json import JSONEncoder
from flask_restful import Api, Resource, url_for
import jsonpickle

class MovieEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__ 


movie_info = Blueprint('movies', __name__)

# @movie_info.route('/')
# @swag_from({
#     'responses':{
#         HTTPStatus.OK.value:{
#             'description': 'this is a movie info',
#             'schema': MovieInfo
#         }
#     }
# })
# def get_info():
#     """
#     Get movie information
#     A more detailed description of the endpoint
#     ---
#     """
#     # all_movies = [MovieEncoder().encode(movie) for movie in movies_list]
#     # result = MoviesModel(name="The Shawshank Redemption", casts = ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"], gernes=["Dramabalhablah"])
#     # data = jsonpickle.encode(movies_list)

#     # return jsonify(data),200
#     result = movie_schema.dump(MoviesModel.query.all())
#     return jsonify(result), 200

# @movie_info.route('/', methods = ['GET', 'POST'])
# @swag_from({
#     'responses':{
#         HTTPStatus.OK.value:{
#             'description': 'Add new movie to the list',
#             'schema': MovieInfo
#         }
#     }
# })
# def post_movie():
#     data = request.get_json()
#     movie = MoviesModel(name= data["name"], casts = data["casts"], gernes= data["gernes"])
#     # movie = MoviesModel(**data)
#     db.session.add(movie)
#     db.session.commit()
#     response =  {
#                'message': 'new user registered'
#                 }
#     return jsonify(response), 200

# @movie_info.route('/<index>', methods = ['PUT'])
# @swag_from({
#     'responses':{
#         HTTPStatus.OK.value:{
#             'description': 'Edit an existing movie to the list',
#             'schema': MovieInfo
#         }
#     }
# })
# def update_movie(index):
#     movie = request.get_json()
#     index = index.replace("_", " ")
#     querry = db.session.query(MoviesModel).filter(MoviesModel.name == index).first()
#     # movies_list[int(index)] = MoviesModel(name= movie["name"], casts= movie["casts"], gernes= movie["gernes"])
#     querry.gernes = movie["gernes"]
#     db.session.commit()
#     response = {
#                'message': 'new user registered'
#                    }
#     return jsonify(response), 200



class MovieLogic(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}