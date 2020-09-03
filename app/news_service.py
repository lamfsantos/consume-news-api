import app.news_repository as repository
import requests
import datetime
import json

def  consume_api(country, key):
    url = ('http://newsapi.org/v2/top-headlines?'
           'country='+country+
           '&apiKey='+key)
    response = requests.get(url)
    return(response.json())

def  controller(country, key):
    #Checking if there is some information about that country on the DB
    response = repository.find_by_country(country)

    #if the lenght is greater than zero, means the DB returned something,
    #then we need to if 20 minutes have passed
    if len(response)>0:
        response = response[0]
        #the DB are saving everything as text, then we must convert the type
        #to datetime again
        str_date_insert = datetime.datetime.strptime(response[1], '%Y-%m-%d %H:%M:%S.%f')

        #here we check if 20 minutes have passed, by adding the minutes to the
        #datetime of the insertion and comparing with the current datetime.
        #If 40 minutes have passed, we gonne update the DB by requesting the
        #NewsAPI again.
        if str_date_insert + datetime.timedelta(minutes=40) < datetime.datetime.now():
            repository.delete_by_time(str_date_insert)
            response_api = consume_api(country, key)
            repository.insert(response_api, country)
            response = response_api
        #if not, we gonna just return the news we have on our DB
        else:
            response = response[0]
    #if not, we don't have anything on DB, we just need to do the request to
    #NewsAPI
    else:
        #consume API, insert in the DB
        response_api = consume_api(country, key)
        repository.insert(response_api, country)
        response = repository.find_by_country(country)
        response = response[0]
        response = response[0]

    return(json.loads(response))
