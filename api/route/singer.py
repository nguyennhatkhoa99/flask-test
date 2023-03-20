from http import HTTPStatus
from flask import Blueprint, request, jsonify
from ..schema.movie import MovieInfo, movie_schema
from json import JSONEncoder
from flask_restful import Api, Resource, url_for
import jsonpickle
from pathlib import Path
import subprocess


singer_info = Blueprint('singer', __name__)
singer = Api(singer_info)
@singer_info.route("/")
class SingerAPI(Resource):
    def post(self):
        project_folder = Path.cwd().absolute()
        singer_data = request.get_json()
        create_catalog_command = [
                "tap-redshift",
                "-c"
                f"{project_folder}/config.json",
                "-d",
            ]
        redshift_tap_cmd = [
                "tap-redshift",
                "-c"
                "config.json",
                "--catalog",
                "catalog.json"
            ]
        postgres_target_cmd = [
            "target-postgres",
            "--config",
            f"{project_folder}/postgres_config.json",
        ]
        
        # with open('catalog.json', 'w') as catalog:
        #     create_catalog_process = subprocess.Popen(create_catalog_command, stdout=catalog)
            

        tap_redshift_process = subprocess.Popen(redshift_tap_cmd, stdout=subprocess.PIPE)
        target_postgres_process = subprocess.Popen(postgres_target_cmd, stdin=tap_redshift_process.stdout, stdout=subprocess.PIPE)
        for line in target_postgres_process.stdout:
            print(line.decode("utf-8").strip())
        response =  {
               'message': 'succeed'
        }
        return response, 200
    
singer.add_resource(SingerAPI, '/singer', endpoint= "budget")

        