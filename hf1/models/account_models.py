from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from datetime import datetime
from hf1.database import db

class Account(db.Model):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    voornaam = Column(String(100), nullable=False)
    achternaam = Column(String(100), nullable=False)
    telefoon = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    aanmaak_datum = Column(DateTime)

    def __init__(self, voornaam, achternaam, email, telefoon):
        self.achternaam = achternaam
        self.voornaam = voornaam
        self.telefoon = telefoon
        self.email = email
        self.aanmaak_datum = datetime.utcnow()

    def __repr__(self):
        return '<Account %r>' % (self.email)