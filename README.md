# reservation-system scratch.png

https://raw.githubusercontent.com/HomeroHerrero4r6/reservation-system/main/scratch.png

# Modelos a Tener En Cuenta

Cliente

Habitacion

Reserva

Metodo De Pago(Por lo general utilizo una api externa pero en este caso queria simular el record-me)

# Rutas A tener en Cuenta

POST: Un request del tipo post a cada uno de los Objetos del dominio (Modelos)

GET: De Igual MAnera ya que siempre es util listarlos ya sea para renderizarlos en alguna app o solo para ayuda propia

PATCH: A Reserva y a Room ya que modificamos parcialmente sus datos en caso de la reserva en el estado y la habitacion la disponibilidad 

POST: En Caso de que deseemos modificar posteriormente un registro

# Para Correr La App

En la carpeta root 

Para Crear y levantar el contenedor

### docker-compose build 

### docker-compose up -d

Aqui ya deberias poder ingresar a la url del host y visualizar la app 

# Crear migraciones

### docker exec api_drf_curriculum_web_1 bash -c "python manage.py makemigrations" 

### docker exec api_drf_curriculum_web_1 bash -c "python manage.py migrate" 
