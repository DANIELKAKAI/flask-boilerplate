import json
import uuid

from flask import request
from flask_restful import Api, Resource

from models.dispenser import Dispenser, db
import config
from schemas.dispenser import DispenserSchema

api = Api(prefix=config.API_PREFIX)


class DispenserAPI(Resource):
    dispenser_schema = DispenserSchema()

    def post(self):
        data = json.loads(request.data)
        dispenser = Dispenser(id=str(uuid.uuid4()), **data)
        db.session.add(dispenser)
        db.session.commit()
        return self.dispenser_schema.dump(dispenser)


class DispenserStatusAPI(Resource):
    dispenser_schema = DispenserSchema()

    def put(self, id):
        data = json.loads(request.data)
        dispenser = Dispenser.query.get(str(id))
        dispenser.status = data["status"]
        db.session.commit()
        return self.dispenser_schema.dump(dispenser)


class DispenserSpendingAPI(Resource):
    dispenser_schema = DispenserSchema()

    def get(self, id):
        dispenser = Dispenser.query.get(str(id))
        return self.dispenser_schema.dump(dispenser)


api.add_resource(DispenserAPI, "/dispenser")

api.add_resource(DispenserStatusAPI, "/dispenser/<uuid:id>/status")

api.add_resource(DispenserSpendingAPI, "/dispenser/<uuid:id>/spending")
