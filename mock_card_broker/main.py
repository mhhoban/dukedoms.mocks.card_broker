import connexion
import logging

from card_broker.shared.db import init_db

logger = logging.getLogger('card_broker')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('card_broker.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

app = connexion.App(__name__, specification_dir='swagger/')
app.add_api('card_broker_api.yaml')
init_db()
application = app.app
