<div style="text-align: justify;">

# 👨🏻‍🎓Grupo DR. EMEL:

</div>

El grupo se conforma por:

- Álvaro Extremera
- Mario Domínguez

## Concepto
### Born as a roomba, grew as Dr. Emel
El robot parte de la idea de un robot de limpieza al que se le añade un arma a partir de la fuerza centrífuga que genera la rotación del anillo exterior.

### Componentes utilizados
Tras el estudio de concepto se establecen los componentes que van a ser utilizados:

- ESP32 Wroom WIFI + Bluetooth => ECU
- Motor N20 1:150 con driver integrado => Tracción de las ruedas
- Motor micro metal 50:1 HP + Controlador de motor => Engranaje motor
- ~~Servo estándar S3003, 360 grados~~ => No usado, falta de espacio para el concepto que se quiere desarrollar.
- Batería Lipo 3500mAh 2S 25C 7.4V

### Sistema de dirección y avance
Únicamente se disponen dos ruedas que se encargan tanto de la tracción como de la dirección del robot. Para que no exista desequilibrio, se disponen unos patines sobre los que apoyará la estructura.

El **Control** se basa en ambas ruedas siendo independientes, controladas por dos joysticks diferenciados. El movimiento se resume en la siguiente tabla:

| Rueda izquierda | Rueda derecha | Desplazamiento |
| ------------- | ------------- | ------------- |
| ⬆️ | ⬆️ | ⬆️ |
| ⬇️ | ⬇️ | ⬇️ |
| ⬆️ | ⏺️ | ➡️ |
| ⏺️ | ⬆️ | ⬅️ |
| ⬆️ | ⬇️ | 🔃 |
| ⬇️ | ⬆️ | 🔄 |

### Cartel de concepto
:filefolder: 
- [DR. EMEL](Cartel robot.pdf)



## Diseño detalle

.........

## Pruebas

...........
