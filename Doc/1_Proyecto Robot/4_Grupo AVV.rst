=======================
👨🏻‍🎓 Grupo AVV
=======================
Equipo formado por Agustín Escalera Zamudio, Víctor Gavira Florido y Vid Baćić.

Concepto
=======================

*Especificaciones de diseño*
-----------------------------------------
En este apartado se recogen las restricciones de diseño así como la lista de los materiales disponibles para construir el robot.

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
*Cinemática del robot*
---------------------------------
Tal y como se comentó en el concepto inicial, el robot cuenta con una tracción de tipo **"differential drive"**. Para poder manejar con comodidad un robot con esta tracción, es necesario realizar un estudio cinemático del mismo. Este estudio se apoya principalmente en la aplicación del concepto de Centro Instantáneo de Rotación, y permite calcular las velocidades perimetrales en cada rueda con el objetivo de mover el robot a una determinada velocidad, cumpliendo un radio de curvatura deseado. Las expresiones para determinar las velocidades en cada rueda son:
.. math::

   \begin{align}
   V_L = \frac{v}{\rho}(\rho - \frac{t}{2}) \\
   V_R = \frac{v}{\rho}(\rho + \frac{t}{2})
   \end{align}

La siguiente figura permite entender estos conceptos de manera visual:

.. image:: ../_static/GrupoAVV/CIRexplain.svg

Sin embargo, como vemos es necesario definir un radio de curvatura :math:`\rho`. Este vendrá dado por los inputs de nuestro control, que se realiza en la aplicación **Dabble**. Esta app permite mandar consignas al microprocesador, a través de una interfaz muy amigable que cuenta con distintos controles: joysticks, botones, etc. En nuestro caso, se relaciona el radio del joystick con una velocidad, mientras que la orientación del mismo está asociada al radio de curvatura. Los radios de curvatura menores se asocian a ángulos más cercanos a la horizontal, mientras que los mayores se asocian a la vertical. La siguiente función relaciona en nuestro caso el radio de curvatura con la orientación del joystick, en grados:
.. image:: ../_static/GrupoAVV/RhoMapPlot.svg

Esta función viene dada por la siguiente expresión:
.. math::

   \begin{align}
   \rho = \frac{56}{Joystick_{deg}-90}
   \end{align}

Aplicando los conceptos anteriores, se puede simular el comportamiento del robot ante una entrada determinada. Las siguientes animaciones son un ejemplo de ello. Esta simulación se ha desarrollado en MATLAB.

Pruebas
=======================