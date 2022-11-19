from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.dispenser import Dispenser, DispenserStatus
from marshmallow_enum import EnumField


class DispenserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Dispenser
        include_relationships = True
        load_instance = True

    status = EnumField(DispenserStatus, by_value=True)
