## API para cursos online 
- diseñe esta api para el proyecto web Lolinail, la cual maneja el CRUD de la aplicacion y la logica de autenticacion para el panel administrativo.

> [!IMPORTANT]
> Actualmenete me encuentro refactorizando todo el proyecto, agregando como base de datos PostgreSQL y mejorando la legibilidad del codigo

## ¿Que implemente?
- Todos los endpoints para la creacion, actualizacion o eliminacion de cada curso.
- Login, register + autenticación mediante JWT y las clases de seguridad que ofrece FastAPI

## Proximos objetivos
- Implementar la logica de gestion de turnos online 🛠️
- Implementar la pasarela de pagos 🛠️
- Implementar autenticacion JWT para el panel administrativo ✅
- Testear correctamente cada endpoint y pulir cada defecto que haya pasado por alto 🛠️

Puedo decir que aprendi bastantes cosas nuevas mientras desarrollaba este proyecto, pude aplicar mis conocimientos y mejorarlos acorde a mis equivocaciones.
Es una trayectoria que me esta ayudando a progresar muy rapido, el poder abordar problemas fuera de mis conocimientos es algo que me esta formando y dando potencia a la hora de desarrollar!

## Podes probarlo!
- Posicionate en la carpeta src para evitar conflictos con las importaciones ```cd src```
- Para podes correr el servidor uvicorn ```uvicorn main:mainApp --reload```
- Proba los endpoints desde la docs ```http://127.0.0.1:8000/docs```
