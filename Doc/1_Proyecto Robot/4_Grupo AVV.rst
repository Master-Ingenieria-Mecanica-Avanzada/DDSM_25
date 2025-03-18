=======================
👨🏻‍🎓 Grupo AVV
=======================
Equipo formado por Agustín Escalera Zamudio, Víctor Gavira Florido y Vid Baćić.

Concepto
=======================

Las batallas de robots son un tipo de competición en la cual robots dirigidos por control remoto luchan usando distintas estrategias para incapacitarse. Suele destacar la gran variedad de diseños y armas, siendo la premisa principal la de construir un robot con el menor número de debilidades posible. Nuestro robot, denominado AVV, cuenta con un sistema de tracción diferencial y un arma que emula la pala de una excavadora. Siguiendo la estrategia de levantar a los enemigos, forzándolos a perder tracción y expulsarlos del octágono. 

*Especificaciones de diseño*
-----------------------------------------
 
Para maximizar la creatividad y minimizar costes, el inventario otorgado a cada equipo es particularmente pequeño. Cabe destacar que, cuanto menor sea el inventario, más fácil es perjudicar el rendimiento del robot si se toman malas decisiones en términos de diseño. Esto fuerza a los equipos a perfeccionar cada aspecto del robot para tener un rendimiento eficiente.

Además, con tal de facilitar aun más la igualdad, los robots se rigen en base a un extenso reglamento, que limita las dimensiones máximas a 200x250x100mm y el peso a 1kg. Fruto de esto, hemos optado por un diseño compacto, con tal de tener un bajo centro de gravedad y estabilidad decente.


*Sistema de tracción*
---------------------------------------

.. image:: ../_static/GrupoAVV/frames2200.gif 
   :width: 30%
   :align: right  

Se ha optado por un **sistema de tracción diferencial**, disponiendo de dos ruedas de tracción y una tercera rueda loca para aportar estabilidad. Las ruedas tractoras se accionarán con los dos **motores de reducción 150:1**, uno para cada rueda, con la posibilidad de añadir reducciones intermedias para aumentar el par motor. 
Cuando ambos motores giren a la misma velocidad y en el mismo sentido el robot podrá avanzar en línea recta, mientras que al reducir la velocidad de giro de uno de los motores permitirá que el robot trace una curva alrededor de un punto exterior. En caso de que ambos motores giren a la misma velocidad pero en sentidos opùestos, el robot girará alrededor de si mismo. Los motores se alimentarán con la batería LiPo, y su velocidad y sentido de giro se controlarán mediante **señales PWM enviadas desde el ESP32**.


*Concepto del arma*
---------------------------------
El arma del robot busca elevar a los oponentes durante el combate, tratando de desestabilizarlos o hacer que pierdan la tracción. Para ello, se pueden recurrir a diversos mecanismos, normalmente, basados en inversiones cinemáticas de mecanismos básicas como el mecanismo de 4 barras o el biela manivela. En este caso, debido a las limitaciones de materiales por normativa, y por la experiencia del grupo en la fabricación con PLA, se opta por eliminar todas las deslizaderas existentes. 

La apuesta del grupo AVV es el mecanismo de 4 barras conocido como **Chebyshev Lambda**. Este mecanismo aproxima un **movimiento rectilineo** mediante el movimiento rotativo de uno de los eslabones. Este último, se consigue mediante la conexión de uno de los eslabones con el **servomotor S3003**. Gracias al uso de este motor, contamos con un par elevado, suficiente para elevar a oponentes de hasta 1 kg. 


Este mecanismo cuenta con unas proporciones establecidas entre sus eslabones, las cuales se usarán como punto de partida. Sin embargo, el propósito del grupo es implementar algoritmos genéticos para optimizar características del mecanismo tales como:

.. image:: ../_static/GrupoAVV/MecanismoRecortado.gif 
   :width: 45%
   :align: left  

* Cumplir con restricciones de espacio (evitar colisiones con elementos circundantes, reducir altura total, etc.)
* Minimizar la pérdida de carga en las ruedas tractoras.
* Minimizar el par ejercido por el servomotor.

*Póster resumen*
---------------------------------
El siguiente poster recoge de manera resumida los principales aspectos del robot de combate.

.. image:: ../_static/GrupoAVV/AVVCombatRobotPoster.svg

Diseño detalle
=======================
...

Pruebas
=======================