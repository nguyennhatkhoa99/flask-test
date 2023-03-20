from ast import Num
from attr import field
from flask_marshmallow import Schema
from marshmallow.fields import Nested
from marshmallow.fields import Str, Number, List

class MovieInfo(Schema):
    class Meta:
        fields = ("id","name", "casts", "gernes")
    id  = Number()
    name = Str()
    casts = Str()
    gernes = Str()

movie_schema = MovieInfo(many = True)