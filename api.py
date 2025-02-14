import services

from fastapi import FastAPI

App = FastAPI()


@App.get('/get-word/{word}')
async def find_word(word):
    return services.find_word(word)


@App.get('/all-words')
async def all_words():
    return services.all_words()
