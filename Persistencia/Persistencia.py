from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os

# Crea la base para los modelos
Base = declarative_base()

DATABASE_URL = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'vinos.db')}" 

# Crea el motor y la sesión
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = scoped_session(sessionmaker(bind=engine))

# Inicializar la base de datos
def init_db():
    Base.metadata.create_all(bind=engine)

class DatabaseInterface:
    def __init__(self):
        self.session = SessionLocal()

    def add_objects(self, objects):
        # Guarda una lista de objetos"
        try:
            self.session.add_all(objects)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()

    def get_all(self, model_class):
        # Recupera todos los datos de una clase especifica
        try:
            return self.session.query(model_class).all()
        finally:
            self.session.close()

    def get_by_id(self, model_class, obj_id):
        # Recupera un objeto especifico por id
        try:
            return self.session.query(model_class).get(obj_id)
        finally:
            self.session.close()

