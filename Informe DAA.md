# Problem 1: Josués y Karles balanceados.

#### Rainel Fernández Abreu C412

#### Lázaro Alejandro Castro Arango C411

## El problema:

Alejandra está comenzando a quedarse dormida en mitad de un turno de `**censura**`. La verdad es que ya conoce todo el contenido de la conferencia, pero no quiere cerrar los ojos y herir los sentimientos del profesor. Así que, para dejar que su mente se entretenga en algo, comienza a imaginar clones de Josué y Karel, colocados uno al lado del otro formando una lista. La imaginación de Alejandra es tan poderosa que empieza a realizar el siguiente proceso: Primero imagina dos listas cualesquiera de Josués y Karels. Luego trata de imaginar una tercera lista tal que las dos primeras son sublistas no necesariamente continuas de esta y que además esté balanceada.

Alejandra define una lista de Josués y Karels balanceada como una lista que cumple lo siguiente:

- Una lista formada por sólo un josué y un karel, en ese orden, está balanceada.

- Si a una lista balanceada, se le agrega un Josué al principio y un Karel al final, el resultado sigue estando balanceado.

- La concatenación de dos listas de Josués y Karel balanceadas es también una lista de Josués y Karel balanceada.

Ayude a Alejandra (a perder el tiempo) con su proceso. Dadas dos listas de Josués y Karel cualesquiera, encuentre la menor lista tal que las dos primeras son sublistas no necesariamente continuas de esta y además está balanceada.

**Resumen**

Dadas dos cadenas $str1,str2$ paréntesis, se quiere formar otra tal que cumpla:

- Debe estar balanceada.

- Debe ser de tamaño mínimo.

- Debe contener a $str1, str2$ como subsecuencias.

### Solución fuerza bruta :

Una primera idea para atacar el problema pasa por generar todas las cadenas $S$ de paréntesis balanceados de tamaño mayor igual que la mayor de las cadenas de entradas dadas y comprobar que se cumplan los requisitos de salida. Esto es extremadamente costoso puesto que para cada índice $i$ de la cadena generada existen dos posibilidades colocar $($ o $)$; lo que derivaría en un algoritmo exponencial de complejidad temporal $O(2^n)$ solo para generar las cadenas. 

Como la cadena a formar debe ser balanceada, una mejora al algoritmo anterior consta de formar solo aquellas cadenas balanceadas e ir comprobando si alguna contiene a las dadas como subsecuencia no necesariamente continua. Para una cadena de tamaño $2*n$ deben existir $n$ paréntesis abiertos y la misma cantidad de cerrados, pues es condición necesaria para que una cadena este balanceada. Luego basado en la idea anterior agregamos la siguiente poda:

Coloco $($ cada vez que pueda hacerlo, esto sucede cuando el número de abiertos es menor que $n$ y coloco $)$  solamente cuando el número de cerrados colocados es menor que el número de abiertos colocados. 

Con esas dos ideas fundamentales se contruyó el algoritmo tipo backtraking para saber dado un $n$ (número de paréntesis abiertos y cerrados) cuantas cadenas de tamaño $2*n$ balanceadas existan. Es conocido que este número es coincidente con el número de Catalán en $n$  (a partir de ahora $C(n)$). Por tanto existen $C(n)$  cadenas válidas por lo que la complejidad de este  código sería $O(C(n))$ y $O((2n)!/{((n+1)!*n!)})$  si se desarrolla $C(n)$.   

Usando el generador anterior se va comprobando si cada cadena encontrada posee como subsecuencia a las dos dadas. Esto se realiza mediante un recorrido por la cadena resultante y si el caracter actual coincide con el primero en la cadena dada, éste se elimina y se continua el chequeo. Si al final las cadenas de entradas están vacías es porque estan contenidas y se ha encontrado una solución. Sumando este paso la complejidad pasa a ser  $O(2*n*C(n))$, representando $2*n$ el tamaño de la cadena resultante. De no encontrarse solución para un tamaño $n$ se continua con $n+1$ hasta encontar una cadena válida. La complejidad total de esta solución fuerza bruta es entonces $O(m*n*C(n))$ siendo $m$ la cantidad de veces que se aumenta el tamaño de la cadena.

El código correspondiente a esta solución aparece en basic_sol.py.

### Segunda solución:

En esta idea se buscarán todas las cadenas que contengan a las cadenas de entrada como subsecuencias sin contener ningún caracter extra, sean estas $A , B$  respectivamente como subsecuencias y su tamaño sea menor igual que $A+B$ a lo sumo.

Se selecciona ese tamaño porque el máximo que puede tomar una cadena al ser balanceada solo poniendo los caracteres necesarios es su doble. Por ejemplo esto ocurre si en una cadena todos los caracteres son del mismo tipo. Por tanto toda cadena balanceada que contenga a $A$ y a $B$  como subsecuencias que sea de tamaño mayor a $2|A+B|$  tendrá como mínimo una cadena de  tamaño $2|A+B|$ menor que ella que contiene a $A$ y a $B$.  

Para construir la posible solución, sea $C$ una posible solución, se llevará un índice que indicará hasta que parte de la cadena tengo ya agregado a $C$; sea $i$ y $j$ este índice respectivamente para $A$ y $B$.

Se procede de la siguiente forma:

* Si $A[i] = B[j]$ se añade ese caracter a $C$ y se aumentan en uno ambos índices. Anadir el caracter contrario se descarta pues aumentaría $C$ sin consumir caracteres de $A$ o $B$.

* Si $A[i] \neq B[j]$ se analizan todas las cadenas donde o avanzo en $A$ y aumento $i$ en uno o avanzo por $B$ y aumento $j$ .

El caso base sucede cuando ya he consumido toda una cadena, $|A| = i$ o $|B|=j$, es decir que esta cadena estará contenida en $C$. Para garantizar que $C$ contenga a ambas cadenas concateno al final la no consumida aún, de esta forma $C$ contiene a $A$ y $B$ como subsecuencias. 

Para llevar el recuento de lo mejor hasta ahora se debe balancear $C$ y compararla con la mejor respuesta actual, en nuestro caso tomamos como la mejor de inicio a $A+B$. La comparación debe hacerse una vez balanceada porque $|X|<|Y|$ no implica $|Bal(X)|< |Bal(Y)|$, donde $X$ y $Y$ son cadenas cualesquiera y $Bal(x)$ devuleve la cadena balanceada de tamaño mínimo que contiene a $x$. Para demostrar lo anterior tenemos el siguiente contra-ejemplo : 

Sea $X = (((($, $Y = ((()$  entonces $|X|<|Y|$ y $Bal(X) = (((())))$,  $Bal(Y) = ((()))$ de donde $|Bal(X)| > |Bal(Y)|$.

El algoritmo anterior para, porque en cada paso aumento algún índice $i$ o $j$, lo que me hace arribar al caso base y garantiza la solución del problema, porque genera todas las posibles cadenas que contiene a $A$ y $B$, y como subsecuencia las balancea y se queda con la menor de ellas.

El peor de los casos ocurre cuando ambas cadenas son disjuntas, es decir no existe $A[i] = B[j]$ para cualesquiera $i,j$. En este caso para cada paso debo ver ambos caminos, o avanzo en $A$ o en $B$, quedando la fórmula recursiva como :

$T(n,m) = T(n-1,m) + T (n,m-1) + c$

El árbol binario generado por $T$ en cada nivel genera dos subárboles donde $m$ o $n$ se reduce en 1. Por lo que para el último nivel habrán $2^{n+m}$. Por tanto $T(n,m) = O(2^{n+m})$ 

El código correspondiente a esta solución aparece en recursive_par.py.

### Solución dinámica :

A continuación se recogen una serie de definiciones que serán útiles para la comprensión de la solución.

**Definiciones:**

- *Factor de balace:* El factor de balance de una cadena es el número de paréntesis abiertos menos el de paréntesis cerrados.

- *Cadena válida:* Una cadena se dice válida si cumple que, al recorrerla de incio a fin su factor de balance nunca se vuelve negativo.

- *Contiene:* Se dice que una cadena b está contenida dentro de una cadena a si b es sublista de a.

Se construye una lista de tres dimensiones llamada dp, donde la posición $dp[i][j][k]$ guarda el tamaño de la menor cadena válida que contiene los $i$ primeros caracteres del $str1$ , $j$ primeros caracteres del $str2$ y tiene factor de balance $k$.

El tamaño de $dp$ es $[len(str1)+1] \times [len(str2)+1] \times 301$. Para el caso del índice $i$, este va desde 0 hasta $len(str1) + $1 porque son todos los prefijos del $str1$ incluyendo el prefijo vacío. Análogamente sucede para $str2$ y $j$. El índice $k$ va desde 0 hasta 300 porque a lo sumo la cantidad de paréntesis abiertos en ambas cadenas es 300, nunca se hace negativo pues en el dp solo se analizan cadenas válidas.

Como el $dp$ no contiene como está formada la cadena sino el tamaño de la menor cadena válida, se necesita de alguna manera construir la cadena, pues es la salida la que se pide en el problema. Para ello se tiene una lista $prv$ de 3 dimensiones, donde en cada posición de esta se almacena una tupla de tamaño 3. Luego $prv[i][j][k]$ nos dice la casilla desde la que se llegó a esta. Dicha matriz se actualiza junto con el $dp$, que se explica más adelante. Para construir la solución se recorre $prv$ con un `bfs` partiendo de la casilla $prv[len(str1)][len(str2)][c]$ . Cuando estamos en esta casilla comprobamos, cómo es el valor $k$ de la casilla que venimos respecto a la posición actual; si $prvK < k$ ,con $prvK$ el valor de $k$ de la anterior casilla entonces se agrega a nuestra solución un paréntesis $"("$, sino pues se agrega un paréntesis $")"$ . Al llegar a la casilla $(0,0,0)$ hemos contruido la solución, solo que está en orden inverso, basta hallar el reverso de esta y agregar los paréntesis cerrados para balancearla, se asegura que solo se necesitan cerrados para balancear pues siempre se forman cadenas válidas en el $dp$. Hacer el recorrido hacia atrás con un `bfs` es efectivo pues en cada paso de iteración la solución crece en 1.

El caso base será $dp[0][0][0] = 0$ que representa la mejor solución de este subproblema del temaño de la menor cadena válida que contiene el prefijo vacío de $str1$ y $str2$ ; y tiene factor de balance 0, dicha solución es la cadena vacía. Los demás valores de la matriz se inicializan con valor 1000.

Para llenar la matriz del $dp$ se recorre la misma por los índices $i,j,k$ en ese orden. Suponga que en algún momento del ciclo para llenar la matriz dp se está en una casilla $dp[i][j][k] = l$ , esto quiere decir que la cadena óptima de este subproblema para llegar a esta casilla tiene tamaño $l$, esta cadena es un posible prefijo de alguna solución general entonces es necesario hacerla crecer hasta alcanzar una óptima del problema. La única forma de crecerla es agregando un paréntesis al final, para no romper la consistencia del $dp$. Por lo anterior dicho se asume que no se lleva la cadena de forma explícita, si de forma implícita dado que se tiene el tamaño de la cadena. Para analizar el $dp[i][j][k]$ se consideran dos casos:

- Colocar un paréntesis abierto

- Colocar un paréntesis cerrado

Para el primer caso, si alguna cadena $str1$ o $str2$ para los índices $i,j$ respectivamente tiene un paréntesis abierto entonces su índice mueve a la posición siguiente, de esta manera se actualiza el prefijo que está contenido de cada cadena en esta solución óptima. Como se agregó un paréntesis abierto el factor de balance aumentó en 1, entonces el valor de $k$ crece en 1 también.

Para el caso de añadir un paréntesis cerrado, es análogo al primero solo que disminuyendo el factor de balance en 1. El factor de balance nunca se hace negativo porque el ciclo que recorre los k va desde 1 hasta 301.

Existe un caso que no se debe pasar por alto: suponga que se ha reconocido un prefijo de tamaño $i$ de la cadena $str1$ y otro de tamaño $j$ de la cadena $str2$, y que $str1[i]=str2[j]=´(´$ y el $dp$ va a colocar un paréntesis cerrado en este momento, en este caso se va a actualizar $dp[i][j][k-1]$ que es una casilla que ya se vió, al actualizarla para no romper la consistencia del algoritmo, $dp[i][j][k-1]$ debe actualizar otras posiciones pero se demuestra continuacón que esto no sucede. Véase que el paréntesis cerrado que se quiere colocar no se empareja con ninguno de los caracteres del prefijo que comienza en 0 y termina en $i$ de la cadena $str1$ ni con el prefijo de 0 hasta $j$ de la cadena $str2$, entonces colocar en la solución este paréntesis no mejora para este momento del problema, puede ser que dicho paréntesis se empareje con algún otro que está luego del $i-ésimo$ caracter de $str1$ o después del $j-ésimo$ de $str2$, pero para descubrir esto se debe antes colocar un paréntesis abierto. Entonces poner este paréntesis cerrado hace que la casilla que se actualizó tenga un mayor tamaño que cuando pasé por ella. Luego, los que esta casilla vaya a actualizar solo va a empeorar. La idea es como decidir ahorrarse colocar el paréntesis en este momento, para que si hace falta, siempre exista la posibilidad de ponerlo al final.

Para demostrar que el problema tiene una **subestructura óptima** se verán varios casos. El primero de ellos, sea :

$str1 =(a_1,a_2,...,a_n)$

$str2 =(b_1,b_2,...,b_m)$

$C= (c_1,c_2,...,c_d)$ con factor de balance $k$.

las cadenas de entrada y $C$ una cadena tal que la suma de $d + k$ es mínima y se cumple que $c_d =a_n=b_m =´(´$ . Se quiere probar que la cadena $C´= (c_1,c_2,...,c_d-1)$ cumple que $d-1 + k-1$ es mínimo para el subproblema donde se quitaron de $str1$ y de $str2$ sus últimos caracteres que eran paréntesis abiertos y además tiene factor de balance $k-1$. Para demostrar que su factor de balance es $k-1$ asumamos que $C´$ tiene factor de balance $t$, si a $C´$ en la posición siguiente a $d-1$ le añadimos un paréntesis abierto obtenemos la cadena $C$ que tiene factor de balance $k$, luego $t+1=k \rightarrow t=k-1$. Para demostrar que resuelve el subproblema para las cadenas $str1´ =str1[0:len(str1)-2]$ y $str2´= str2[len(str2)-2]$ supongamos que $C´$ no es la mejor, entonces existe otra cadena $W$ que tiene longitud $l$, con $l$ menor que $d-1$ y cumple que $l+t\lt d-1 + k-1$, si agregamos un paréntesis abierto a $W$ y $C´$ obtenemos que $C´$ se convierte en $C$, entonces $l+t+2\lt d+k$, luego la cadena $C$ no era óptima, Contradicción!.

Resta demostrar el caso simétrico a este (con el paréntesis $´)´$) y cuando el último de la solución empareja con 1 solo de $str1$ o $str2$. Estas demostraciones no logramos completarlas pero creemos que por ahÍ es la demostración de que existe una subestructura óptima.

Demostremos que la solución del problema no es única, para ello veamos un contraejemplo sencillo. Sean las cadenas de entrada $str1=´((´$ y $str2=´))´$. Para estas entradas del problema la solución puede ser o bien $(())$ o $()()$, es fácil comprobar que ambas cadenas tienen factor de balance 0 y contienen a $str1$ y $str2$ como sublistas de esta.

**Complejidad Temporal**

En el algoritmo se hacen 3 ciclos `for` anidados, la complejidad de estos ciclos es $O(|str1|*|str2|*300)$ . También se recorre el $dp[str1][str2]$, o sea el ciclo se mueve por los valores de $k$ de dicha posición del $dp$, esto tiene un costo constante pues el factor de balance es a lo sumo 300. Luego se realiza un ciclo `while` para moverse en la matriz $prv$ con un `bfs`, la complejidad del `bfs` es $O(|str1|*|str2|)$. Luego por regla de la suma podemos concluir que la complejidad temporal del algoritmo es $O(|str1|*|str2|*300)$.

### Generador de casos de prueba

Usando la solución fuerza bruta se generaron 10000 casos donde cada secuencia posee a lo sumo tamaño 10. Estos se guardan en cases.json donde para cada caso se guardan las cadenas de entrada $A, B$ y la solución. Como se menciona anteriormente esta solución no es única, por lo que al comparar con las soluciones del algoritmo recursivo y el dp, se ve si para cada entrada la salida las contiene como subsecuencia y coincide en tamaño con la solucion guardada.

Análogamente se generan casos de prueba usando el segundo algoritmo y se comparan con el dp. Esta vez fue posible generar casos de prueba de tamaño 20 para las cadenas de entrada.   

Los casos de prueba se generan en test_gen.py y pueden ejecutarse en test_execute.py.
