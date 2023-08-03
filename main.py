import uvicorn

from api import App
from consts import HOST, PORT

if __name__ == '__main__':
    uvicorn.run(App, host=HOST, port=PORT)
