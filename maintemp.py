from Persistencia.Persistencia import DatabaseInterface, init_db
from Persistencia.datos_mock import datos

# Importar los modelos para asegurarse de que se registran con Base
from LogicaDeNegocio.Pais import Pais
from LogicaDeNegocio.Provincia import Provincia
from LogicaDeNegocio.RegionVitivinicola import RegionVitivinicola
from LogicaDeNegocio.Bodega import Bodega
from LogicaDeNegocio.Varietal import Varietal
from LogicaDeNegocio.Vino import Vino
from LogicaDeNegocio.Enofilo import Enofilo
from LogicaDeNegocio.Resenia import Resenia

paises, provincias, regiones, bodegas, varietales, vinos, resenias = datos()

init_db()

db_interface = DatabaseInterface()

# Insertar cada grupo de objetos en la base de datos
db_interface.add_objects(paises)       # Primero almacenamos los países
db_interface.add_objects(provincias)   # Luego las provincias, que dependen de los países
db_interface.add_objects(regiones)     # Después las regiones, que dependen de las provincias
db_interface.add_objects(bodegas)      # Luego las bodegas, que dependen de las regiones
db_interface.add_objects(varietales)   # Insertamos los varietales
db_interface.add_objects(vinos)        # Luego los vinos, que dependen de bodegas y varietales
db_interface.add_objects(resenias)     # Finalmente, las reseñas, que dependen de los vinos

print("Datos almacenados correctamente en la base de datos.")


