import models.integrantes
from database import session


integrante1 = models.integrantes.Integrantes(id=1, name="Rodrigo Parra")
integrante2 = models.integrantes.Integrantes(id=2, name="Andres Rodriguez")
integrante3 = models.integrantes.Integrantes(id=3, name="Tomas Rios")


session.add(integrante1)
session.add(integrante2)
session.add(integrante3)

# Confirmar los cambios en la base de datos
try:
    session.commit()
    print("Estudiantes agregados exitosamente.")
except Exception as e:
    print("Error al agregar estudiantes:", str(e))
    session.rollback()
finally:
    session.close()
