from flask import Blueprint, request
import app.news_service as service

index_blueprint = Blueprint("index", __name__)

#The JS will request this route passing the country as argument
@index_blueprint.route('/')
def index():
    country = request.args.get('country')
    apiKey = request.args.get('apiKey')

    return service.controller(country, apiKey)
