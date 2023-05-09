### 

# Problem 2: Problema en la pizarra.

#### Rainel Fernández Abreu C412

#### Lázaro Alejandro Castro Arango C411

## El problema:

Un día iba David por su facultad cuando ve un cuadrado formado por  cuadraditos de color blanco. A su lado, un mensaje ponía lo siguiente: "Las siguientes tuplas de la forma x1 , y1 , x2 , y2 son coordenadas para pintar de negro algunos rectángulos. (coordenadas de las esquina inferior derecha y superior izquierda)" Luego se veían k tuplas de cuatro enteros. Finalmente decía: "Luego de tener el cuadrado coloreado de negro en las secciones pertinentes, su tarea es invertir el cuadrado a su estado original. En una operación puede seleccionar un rectángulo y pintar todas sus casillas de blanco. El costo de pintar de blanco un rectángulo de  es el mínimo entre h y w. Encuentre el costo mínimo para pintar de blanco todo el cuadrado."

En unos 10 minutos David fue capaz de resolver el problema. Desgraciadamente esto no es una película y el problema de David no era un problema del milenio que lo volviera millonario. Pero ¿Sería usted capaz de resolverlo también?

#### Resumen:

Dada una matriz de n x n cuadraditos. Se tienen k tuplas de números de la forma:

(x_1,y_1 ; x_2,y_2) que representan las coordenadas de dos puntos, esquina inferior drecha y esquina superior izquierda, que resperesentan rectángulos que se pintaron de negro. El objetivo es volver la matriz de colo blanco totalmente de modo que cueste lo menor posible, y el costo de pintar de blanco un rectángulo es el min(h,w).
