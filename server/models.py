from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    animal = db.relationship('Animal', backref='zookeeper', lazy=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'birthday': self.birthday,
            'animal_id': self.animal_id
        }


class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(50), nullable=False)  
    open_to_visitors = db.Column(db.Boolean, nullable=False)    
    animals = db.relationship('Animal', backref='enclosure', lazy=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'environment': self.environment,
            'open_to_visitors': self.open_to_visitors,
            'animal_id': self.animal_id
        }

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False) 
    species = db.Column(db.String(50), nullable=False)
    zookeeper = db.relationship('Zookeeper', backref='animal', lazy=True)
    enclosure = db.relationship('Enclosure', backref='animal', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'species': self.species,
        }


