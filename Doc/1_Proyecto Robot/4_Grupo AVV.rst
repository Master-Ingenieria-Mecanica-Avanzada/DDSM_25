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
Cuando ambos motores giren a la misma velocidad y en el mismo sentido el robot podrá avanzar en línea recta, mientras que al reducir la velocidad de giro de uno de los motores permitirá que el robot trace una curva alrededor de un punto exterior. En caso de que ambos motores giren a la misma velocidad pero en sentidos opuestos, el robot girará alrededor de si mismo. Los motores se alimentarán con la batería LiPo, y su velocidad y sentido de giro se controlarán mediante **señales PWM enviadas desde el ESP32**.


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

   V_L = \frac{v}{\rho}(\rho - \frac{t}{2}) \\
   V_R = \frac{v}{\rho}(\rho + \frac{t}{2})


La siguiente figura permite entender estos conceptos de manera visual:

.. image:: ../_static/GrupoAVV/CIRexplain.svg

Sin embargo, como vemos es necesario definir un radio de curvatura :math:`\rho`. Este vendrá dado por los inputs de nuestro control, que se realiza en la aplicación **Dabble**. Esta app permite mandar consignas al microprocesador, a través de una interfaz muy amigable que cuenta con distintos controles: joysticks, botones, etc. En nuestro caso, se relaciona el radio del joystick con una velocidad, mientras que la orientación del mismo está asociada al radio de curvatura. Los radios de curvatura menores se asocian a ángulos más cercanos a la horizontal, mientras que los mayores se asocian a la vertical. La siguiente función relaciona en nuestro caso el radio de curvatura con la orientación del joystick, en grados:

.. image:: ../_static/GrupoAVV/RhoMapPlot.svg

Esta función viene dada por la siguiente expresión:

.. math::

   \rho = \frac{56}{Joystick_{deg}-90}


Aplicando los conceptos anteriores, se puede simular el comportamiento del robot ante una entrada determinada. Las siguientes animaciones son un ejemplo de ello. Esta simulación se ha desarrollado en MATLAB.

.. raw:: html

   <div style="display: flex; justify-content: center; gap: 20px;">
       <img src="../_static/GrupoAVV/arrowsGif.gif" width="45%">
       <img src="../_static/GrupoAVV/Joystick.gif" width="45%">
   </div>

*Optimización del mecanismo*
---------------------------------
La principal limitación del **mecanismo Lambda de Chebyshev** es que para mantener la rectitud de la trayectoria **los eslabones deben mantener una relación específica** entre ellos. Por ello, la trayectoria del mecanismo solo puede desplazarse fuera del chasis del robot si se incrementa el tamaño de los eslabones o si se desplaza todo el mecanismo hacia adelante. En el primer caso, se violarían las restricciones de tamaño de la competición, y en el segundo caso se incrementa el riesgo de que el robot vuelque al intentar levantar el adversario. Debido a lo anterior, se ha optado por modificar el mecanismo teniendo en cuenta cuatro objetivos principales:

* Cumplir con las restricciones de tamaño impuestas.
* Hacer que el mecanismo siga la trayectoria deseada.
* Minimizar el par ejercido por el servomotor.
* Evitar el vuelco del robot.

Para alcanzar dichos objetivos, se puede jugar con las **longitudes de los eslabones**, la **posición de los puntos fijos O2 y O4** y las **distancias AB y BC**. 

Debido a la interacción entre los objetivos y entre las variables, se ha decidido utilizar un **algoritmo genético de evolución diferencial**. Para ello, es necesario definir una población de individuos, todos con un grupo definido de variables a optimizar consideradas "genes". En este caso, las variables a optimizar serán las descritas previamente, además del ángulo inicial y final del recorrido del mecanismo.

.. image:: ../_static/GrupoAVV/ParametrosOpti.svg

Con ello, cada individuo de la población será un mecanismo con una configuración única, que se resolverá tanto para posición como para fuerzas en el recorrido angular definido del eslabón motor. A partir de dichas soluciones, será posible evaluar lo bien que cumple el mecanismo los objetivos buscados. Para ello, es necesario definir una función de coste que, al evaluar un individuo, devuelva un error, que en definitiva indica que tan bien cumple dicho inidviduo los objetivos.

La **función de coste** construida se compone de dos términos, uno que evalúa el error de las restricciones cinemáticas :math:`e_c` y otro que evalúe el error de las restricciones dinámicas :math:`e_d`, ambos asociados con sus respectivos coeficientes de coste :math:`k_c` y :math:`k_d`, respectivamente.

.. math::
   error = \sqrt(k_c\cdot e_c^2 + k_d\cdot e_d^2)	

Las **restricciones cinemáticas** se evalúan de dos formas, la primera es comprobando si los puntos fijos :math:`O_2` y :math:`O_4` están dentro del espacio de diseño. Para ello, se recurre a una de las aplicaciones del `teorema de curva de Jordan <https://en.wikipedia.org/wiki/Jordan_curve_theorem#:~:text=.-,Application,-%5Bedit%5D>`_.
Para mejorar la evaluación del error, no solo se comprueba si el punto está dentro o fuera, sino si alguna de las coordenadas está dentro del espacio de diseño. Con ello, el error asociado a esta restricción aumenta a más coordenadas estén fuera del espacio de diseño.

La segunda restricción cinemática está asociada a la trayectoria del punto :math:`C` del mecanismo. En primera instancia, se comprueba la variación horizontal de la trayectoria del punto, restando la coordenada :math:`x` inicial del punto a la coordenada :math:`x` del punto en las sucesivas posiciones. Sin embargo, la trayectoria, aunque vertical, puede aparecer dentro del chasis del robot. Para ello, se añade un término adicional que comprueba si la trayectoria comienza en el punto deseado. Otro problema que puede aparecer es el hecho de que la trayectoria presenta un reducido movimiento vertical, además de que puede comenzar por debajo de la cota del suelo. Para ello, se añaden dos términos adicionales que comprueben si la variación de la coordenada :math:`y` se acerca a la altura deseada, y si la coordenada :math:`y` inicial se acerca a la coordenada :math:`y_lim`.

.. math::
   e_c = \sqrt((k_1\cdot(n_x^2+n_y^2))^2 + (k_2\cdot\sum_{i=2}^{n}{(x_{ci}-x_{c1})} + k_3\cdot\left(x_i-x_{c1}\right) + {k}_4\cdot\left(h\ -\left|y_{cend}-y_{ci}\right|\right) + {k}_5\cdot\left(y_{lim}\ -y_{cmin}\right) )^2 )

En cuanto a las **restricciones dinámicas**, primero se evalúa el par requerido, incrementado el error a mayor sea el par máximo necesario. En segundo lugar, se comprueba la carga vertical ejercida sobre el eje trasero del robot. Dicha fuerza se calcula realizando un equilibrio de momentos en el centro de gravedad del robot, considerando que sobre el punto C se aplica una fuerza vertical de 1kg en el instante en el que dicho punto está lo más alejado del centro de gravedad.

.. math::
   e_d = \sqrt( (k_{1d} \cdot T^2 )^2 + (k_{3d} \cdot F_{zt})^2)

A partir de la ecuación de restricción, es posible evaluar a cada individuo de la población, y seleccionar al mejor (el que tiene el menor error). Posteriormente, es posible crear una nueva población mezclando los genes del mejor individuo con el resto de miembros de la población. El proceso se repite varias veces, obteniendose al final el mejor de los miembros, con los parámetros optimizados.


Pruebas
=======================