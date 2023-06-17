# Problem 3: Tito quita y pon.

#### Rainel Fernández Abreu C412

#### Lázaro Alejandro Castro Arango C411

## El problema:

Tito cayó en arresto domiciliario tras ser vinculado a una serie de negocios turbios. Tras días de encierro llegó a un punto en el que estaba absolutamente aburrido. De pronto, encontró un pequeño juego de mesa que, según la cubierta, se llamaba "Quita y pon". El juego contaba con una colección de cajitas. Cada cajita tenía 3 agujeros de colores. Habían k colores distintos. Además tenía con una bolsa con de pelotas, cada una con el tamaño exacto para rellenar un agujero. La cantidad de pelotas era suficiente para rellenar todos los agujeros.

Al inicio del juego, algunos agujeros están llenos con su pelota correspondiente. Tito puede quitar o poner pelotas en los agujeros siempre que cumpla con que si interactúa con un agujero de color 
, debe interactuar con todos los agujeros de ese mismo color en todas las cajas existentes. Se entiende interactuar como quitar (agujero lleno) o poner una pelota (agujero vacío). El objetivo del juego es encontrar si existe un conjunto de interacciones que, luego de ejecutadas resulten en que todas las cajas tengan al menos un agujero lleno y al menos un agujero vacío.

**Resumen:**

Se tienen un conjunto de cajitas, las cuales tienen exactamente 3 agujeros de colores, con k colores. Se quiere determinar si existe un conjunto de interacciones tales que luego de realizadas resulte que cada caja tenga un agujero vacio y uno lleno con la pelota correspondiente, donde interactuar es colocar o quitar una pelota de algún hueco de la caja.

**Solución:**

Por la descripción del problema y luego de haber asistido a las clases de DAA, se puede pensar que el problema tiene características donde coincide con el problema `3-sat`.  **SAT** fue el primer problema identificado como perteneciente a la clase de complejidad NP-C. El SAT sigue siendo NP-completo incluso si todas las fórmulas están en forma normal conjuntiva FNC con 3 variables por cláusula (3SAT-FNC) creando el problema (3SAT), o aun en el caso de que solo se permita un único valor verdadero en cada cláusula (3SAT en 1).

Para probar que nuestro probema es NP-C, que es uno de los objetivos de este proyecto vamos a seguir una serie de pasos con la mayor formalidad posible.

1. Probar que L \in NP

2. Seleccionar un problema NPC conocido.

3. Describir un algortimo que compute una función f la cual debe mapear para cada instancia x \in \{ 0,1\}^* de L^{'} a una instancia f(x) de L.

4. Probar la correctitud de dicha función.

5. Probar que este algoritmo que computa f se resuelve en tiempo polinomial.
