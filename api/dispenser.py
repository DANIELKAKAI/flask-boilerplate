import json
from flask import jsonify, request
from flask_restful import Api, Resource

from models.dispenser import Dispenser, db
import config

api = Api(prefix=config.API_PREFIX)


class DispenserAPI(Resource):
    def post(self):
        data = json.loads(request.data)
        dispenser = Dispenser(**data)
        db.session.add(dispenser)
        db.session.commit()
        return jsonify(dispenser)


class DispenserStatusAPI(Resource):
    def put(self, id):
        data = json.loads(request.data)
        dispenser = Dispenser.query.get(str(id))
        dispenser.status = data["status"]
        db.session.commit()
        return jsonify(dispenser)


class DispenserSpendingAPI(Resource):
    def get(self):
        return "get"


api.add_resource(DispenserAPI, '/dispenser')

api.add_resource(DispenserStatusAPI, '/dispenser/<uuid:id>/status')

api.add_resource(DispenserSpendingAPI, '/dispenser/<uuid:id>/spending')
