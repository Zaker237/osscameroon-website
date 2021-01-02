from flask_restplus import Resource, fields
from flask import request, json
import datetime

# from app.main.utils.decorator import *
from app.main.utils.dto import ApiDto
from app.main.utils.database.twitter.top_tweets import get_top_tweets


api = ApiDto.api

c = Cache()

# Ex : /top-tweets
@api.route("/top-tweets", methods=["GET"])
class ApidtoTopTweets(Resource):
    @api.doc(
        "Get_top_tweets"
    )
    def get(self):
        """This method will return all top tweets"""

        result = get_top_tweets(c)

        return result, result["code"]


