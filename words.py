import os
import random

from wordnik import *


############################### WORDNIK SETUP ##################################
api_url = 'http://api.wordnik.com/v4'
api_key = os.environ['WORDNIK_API_KEY']

client = swagger.ApiClient(api_key, api_url)

############################### WORDNIK FUNCS ##################################
def get_random_word():
    '''
    Return random word based on Wordnik API
    '''
    words_api = WordsApi.WordsApi(client)
    return words_api.getRandomWord().word
