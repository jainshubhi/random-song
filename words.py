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
    word = words_api.getRandomWord()
    # If a more condensed form of word exists, return that instead
    if word.canonicalForm:
        print 'Printed Canonical Form of Word'
        return word.canonicalForm
    elif word.originalWord:
        print 'Printed Original Form of Word'
        return originalWord
    return word.word
