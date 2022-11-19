from flask_restful import Api
import config

api = Api(prefix=config.API_PREFIX)
