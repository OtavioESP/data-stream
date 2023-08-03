import requests


def simple_decoder(encoded_var: bytes) -> int:
    return encoded_var.decode('utf-8')


def find_word():
    response = requests.get(
        'http://localhost:8001/get-word/worried', stream=True)

    for r in response.iter_lines():
        decoded_data = simple_decoder(r)
        print(decoded_data)


def all_file():
    response = requests.get('http://localhost:8001/all-words', stream=True)

    for r in response.iter_lines():
        decoded_data = simple_decoder(r)
        print(decoded_data)


all_file()
print('\n\n\n\n\n\n\n\n\n\n\n\n')
find_word()
