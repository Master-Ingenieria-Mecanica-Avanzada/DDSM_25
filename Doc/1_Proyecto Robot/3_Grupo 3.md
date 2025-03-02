<div style="text-align: justify;">

# 👨🏻‍🎓Grupo CYBERTRUCK:

</div>

El equipo esta formado por Antonio Rojas López, Lucía Gallego Carrasco e Ivan Sanchez Shevtsova.
Aquí se registrará la documentación para el diseño y fabricación de un robot de batalla con las siguientes limitaciones de diseño, como son el peso, dimensiones o materiales a utilizar.

## Concepto

### Especificaciones técnicas y reglas de diseño
El robot de batalla debe tener un peso máximo de 1000 gramos y unas dimensiones máximas de 200x250x100 milimetros. Se tiene que controlar de forma remota y se tienen que utilizar los siguientes materiales.

* Batería Lipo 3500mAh 2s 25C, 7.4V
* Controlador de motores TB6612FNG
* Servo estándar S3003 360 grados
* Motor micro metal 50:1 HP con eje extendido
* Motor N20 1:150 133rpm con driver integrado
* ESP32 Wroom WIFI + Bluetooth

El robot tendrá tracción a las dos ruedas controlados por dos motores PWM situados en las ruedas de un mismo eje. El funcionamiento será independiente del sentido vertical de la base, pudiendo funcionar en ambos planos gracias a las ruedas de TPU con mayores dimensiones que el alto de la base.

En cuanto a las armas se desarrolla una giratoria utilizando un motor situado en el frontal del robot.

Todos los componentes electronicos son controlados por la ESP32 que tiene 4 salidas de puertos digitales para alimetar las 2 señales de los motores PWM, 1 para el servo y 1 para la placa dedicada al control del motor del arma, que esta a su vez tiene una salida analogica que alimenta el motor.

### Poster Concepto

![Cartel Concepto Robot](Doc/1_Proyecto Robot/Poster/cartel_CYBERTRUCK.png)

## Diseño detalle

.........

## Pruebas

...........
