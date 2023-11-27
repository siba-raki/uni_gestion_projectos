
# Ejemplo del archivo .env
### Tiene que estar en la raiz del proyecto
```poweshell
vim /opt/uni_gestion_projectos/.env
```

> Pegamos las siguientes variables y guardamos el archivo
```poweshell
KEY=secret_key
POSTGRES_DB=bibliografias
POSTGRES_USER=postgres
POSTGRES_PASSWORD=root
HOST=IpdeTuMaquina
```

### En frontend /src/api/api.js

#### Colocar tambien la direccion de la ip
```poweshell
vim /src/api/api.js
```

```poweshell
const API_URL = "http://<TU_IP>:8000/api";
```

### Para correr el projecto:

#### Primero ejecutamos el archivo "init_install.sh" para instalar docker y docker compose, esto tambien instalara "node" y "npm" segun sistema operativo que tengamos, sea rocky linux, ubuntu o centOs.

> Nos dirigimos alsiguiente directorio

```poweshell
cd /opt/uni_gestion_projectos
```
#### Damos permisos de ejecucuin al archivo

```poweshell
chmod 755 init_install.sh
```
#### Empezamos a levantar los contenedores
>Esto podria demorar unos minutos

> Ejecutamos los siguientes comandos
```poweshell
sudo docker-compose build
```
```poweshell
sudo docker-compose up
```

### Mientras esté corriendo los contenedores:
> Ejecutar:
```poweshell
sudo docker exec -it uni_gestion_projectos_web_1 bash
```
```poweshell
python3 manage.py makemigrations api
```
```poweshell
python3 manage.py migrate api
```
#### Nos dirigimos a nuestro navegador de preferencia y pegamos la siguiente URL
```poweshell
http://<TU_IP>:5173/
```