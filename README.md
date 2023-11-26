
ejemplo del archivo .env
tiene que estar en la raiz del proyecto

KEY=secret_key
POSTGRES_DB=bibliografias
POSTGRES_USER=postgres
POSTGRES_PASSWORD=root
HOST=IpdeTuMaquina

en /frontend/src/api/api.js
colocar tambien la direccion de la ip

para correr el projecto:
- estar en la raiz
- sudo docker-compose build
- sudo docker-compose up
Mientras esté corriendo los contenedores:
Ejecutar:
- sudo docker exec -it uni_gestion_projectos_web_1 bash
- python3 manage.py makemigrations
- python3 manage.py migrate
