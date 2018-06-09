import connexion
import logging

app = connexion.App(__name__, specification_dir='swagger/')
app.add_api('card_broker_api.yaml')
application = app.app
