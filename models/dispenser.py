import datetime
import enum
import uuid
from dataclasses import dataclass

from sqlalchemy import Enum

from models import db


class DispenserStatus(enum.Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"


@dataclass
class Dispenser(db.Model):
    __tablename__ = "dispenser"

    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    amount = db.Column(db.Float, nullable=False, default=0)
    flow_volume = db.Column(db.Float, nullable=False, default=0)
    status = db.Column(Enum(DispenserStatus), default="CLOSED")
    date_updated = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )


@dataclass
class DispenserUsage(db.Model):
    __tablename__ = "dispenser_usage"

    id = db.Column(db.String(), primary_key=True, default=str(uuid.uuid4()))
    flow_volume = db.Column(db.Float, nullable=False, default=0)
    total_spent = db.Column(db.Float, nullable=False, default=0)
    opened_at = db.Column(db.DateTime, nullable=False)
    closed_at = db.Column(db.DateTime, nullable=False)
    dispenser_id = db.Column(
        db.String, db.ForeignKey("dispenser.id"), nullable=False
    )
    dispenser = db.relationship(
        "Dispenser", backref=db.backref("dispenser_usages", lazy=True)
    )
