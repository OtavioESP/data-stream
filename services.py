from fastapi.responses import StreamingResponse
from consts import FILE, DEBUG


def read_and_find_csv(word: str):
    with open(FILE, 'r') as csv_file:
        data = 'start'
        while data:
            data = csv_file.readline()
            yield data

            if DEBUG:
                print(data)

            if word in data:
                break


def read_all_csv():
    with open(FILE, 'r') as csv_file:
        data = 'start'
        while data:
            data = csv_file.readline()
            yield data
            if DEBUG:
                print(data)


def find_word(word: str):
    data_iter = read_and_find_csv(word)
    return StreamingResponse(data_iter)


def all_words():
    data_iter = read_all_csv()
    return StreamingResponse(data_iter)
