import logging

import app.controllers.webserver as server


formatter = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
logging.basicConfig(
    level=logging.INFO,
    format=formatter
)


if __name__ == "__main__":
    server.start()
