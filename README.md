# python-professional
My projects and notes of the course "Profesional de Python" at Platzi

- **Introducción**
    - ¿Qué se necesita para este curso?
        - [Curso básico de Python](https://platzi.com/clases/python/)
        - [Curso profesional de Git y Github](https://platzi.com/clases/git-github/)
        - [Curso intermedio de Python](https://platzi.com/clases/python-intermedio/)
        - [Curso de POO](https://platzi.com/clases/oop/)
    - ¿Cómo funciona Python?

        **Compliated vs interpreted** 🐍

        ![https://static.platzi.com/media/user_upload/compilate-2919a8ad-bb82-45d8-9300-6fe146afa200.jpg](https://static.platzi.com/media/user_upload/compilate-2919a8ad-bb82-45d8-9300-6fe146afa200.jpg)

        - Tanto **compiladores** como **interpretadores** son programas que convierten el código que escribes a lenguaje de máquina.
        - **Compilado:** Aquel lenguaje que tiene que ser traducido al código de máquina para producir un programa ejecutable.

            ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b3fa8312-8477-47af-b1c4-b9d86aec891b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b3fa8312-8477-47af-b1c4-b9d86aec891b/Untitled.png)

        - **Interpretado:** es un lenguaje de programación para el que la mayoría de sus implementaciones ejecuta las instrucciones directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina.

            ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/99047383-66ad-47e9-abd6-0b2df622f0b3/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/99047383-66ad-47e9-abd6-0b2df622f0b3/Untitled.png)

            ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0df8f128-1ee9-4e78-8e29-15885b743a97/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0df8f128-1ee9-4e78-8e29-15885b743a97/Untitled.png)

            **¿Los interpretados son más lentos?**

            Con el nivel de hardware que tenemos en la actualidad, no es relevante para propositos generales, para casos más avanzados ya es necesario centrarse en soluciones compiladas.

        - **Garbage collector:** Es una sección especial de python que se encarga de tomar los objetos y las variables que no están en uso y eliminarlas..

            ![https://upload.wikimedia.org/wikipedia/commons/3/3b/Garbage_collection.gif](https://upload.wikimedia.org/wikipedia/commons/3/3b/Garbage_collection.gif)

        - **¿Qué es la carpeta pycache?** Dentro de la carpeta tenemos el **bytecode** que es el código intermedio que crea python al ser un lenguaje interpretado para que pueda ser leido por la máquina virtual, la ventaja es que funiona como una especie de recuperacion del código que ya hemos trabajado, para que la proxima vez que ejecutes el programa se ejecutará más rápido porque no tiene que convertirse a bytecode de nuevo.

        **Tambien podemos verlo de esta forma:**

        1. Los lenguajes compilados convierten el código a binario que es el que lee la computadora.
        2. Los interpretados requieren de un programa que lee las instrucciones en tiempo real y las ejecuta, por lo que el programa interpreta el código escrito y lo traduce en lenguaje de máquina en tiempo real. Esto también explicaría porque en los notebook escritos en collab o jupyter podemos ejecutar nuestro código de python por partes.
    - ¿Cómo organizar las carpetas de tus proyectos?

        📁Un **módulo** es cualquier archivo de Python. Generalmente, contiene código que puedes reutilizar.

        🗄 Un **paquete** es un conjunto de módulos. Siempre posee el archivo **`__init__.py`**.

        **dunder init.py / double-underscore**

        Un ejemplo de organización de archivos: 

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/798c00d2-29cc-4063-ab94-5b99b6d369ae/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/798c00d2-29cc-4063-ab94-5b99b6d369ae/Untitled.png)

        ![https://static.platzi.com/media/user_upload/paquettes-5a4095f3-0811-4e56-8f06-296b42b2e497.jpg](https://static.platzi.com/media/user_upload/paquettes-5a4095f3-0811-4e56-8f06-296b42b2e497.jpg)

    - ¿Qué son los tipados?

        💻 Los tipados es una clasificación de los lenguajes de programación, tenemos cuatro tipos:

        **Estático**

        Detectan los errores en tiempo de compilación. No se ejecuta hasta corregir. Por ej, *Java*

        **Dinámico**

        Detectan el error en tiempo de ejecución. Nos dice el error cuando llega a la línea del código. Por ej, *Python*

        **Fuerte**

        Más severidad con los tipos de datos. Sumar un número + una letra arrojará error.

        **Débil**

        Menos severidad con los tipos de datos. Si quiero sumar número y letra, las concatenaría como strings. Castea tipos de datos automáticamente. Por ej, *PHP*

        El tipado del lenguaje depende de cómo trata a los tipos de datos.

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/48c8687e-76c5-4800-b22e-1c513912287f/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/48c8687e-76c5-4800-b22e-1c513912287f/Untitled.png)

        El tipado **estático** es el que levanta un error en el tiempo de compilación, ejemplo en **JAVA**:

        ```java
        String str = "Hello" // Variable tipo String
        str = 5 // ERROR: no se puede convertir un tipo de dato en otro de esta forma.
        ```

        El tipado **dinámico** levantan el error en tiempo de ejecución, ejemplo en **Python**:

        ```python
        str = "Hello" # Variable tipo String
        str = 5 # La variable ahora es de tipo Entero, no hay error

        ## TIPADO FUERTE
        x = 1
        y = "2"
        z = x + y #ERROR: no podemos hacer estas operaciones con tipos de datos distintos entre sí
        ```

        El tipado **débil** es el que hace un cambio en un tipo de dato para poder operar con el, como lo hace JavaScript y PHP.

        **Python Es un lenguaje de tipado 👾 Dinámico y 💪 Fuerte.**

- **Static Typing**
    - Tipado estático en Python

        Para hacer que Python sea de tipado estático es necesario agregar algo de sintaxis adicional a lo aprendido, además.

        ```python
        # De esta manera se declara una variable, se colocan los dos puntos (:), el tipo de dato y para finalizar se usa el signo igual para asignar el valor a la variable.

        <variable> : <tipo_de_dato> = <valor_asignado>

        a: int = 5
        print(a)

        b: str = "Hola"
        print(b)

        c: bool =Trueprint(c)
        ```

        Del mismo modo se puede usar esta metodología de tipado en Python a funciones adicionando el signo menos a continuación del signo mayor que para determinar el tipo de dato. Ejemplo:

        ```python
        def <nombre_func> ( <parametro1> : <tipo_de_dato>, <parametro2> : <tipo_de_dato> ) ->  <tipo_de_dato> :
        passdefsuma(a: int, b: int) -> int :
        return a + b

        print(suma(1,2))

        # 3
        ```

        Existe una librería de fabrica que viene preinstalada con Python que se llama **typing,** que es de gran utilidad para trabajar con tipado con estructuras de datos entre la versión **3.6** y **3.9**, entonces:.

        ```python
        from typingimportDict,List

        positives:List [int] = [1,2,3,4,5]

        users:Dict [str, int] = {
        	"argentina": 1.
        	"mexico": 34,
        	"colombia": 45,
        }

        countries:List[Dict[str, str]] = [
        	{
        		"name" : "Argentina",
        		"people" : "45000",
        	},
        	{
        		"name" : "México",
        		"people" : "9000000",
        	},
        	{
        		"name" : "Colombia",
        		"people" : "99999999999",
        	}
        ]

        ```

        ```python
        from typingimportTuple,Dict,List

        CoordinatesType =List[Dict[str,Tuple[int, int]]]

        coordinates: CoordinatesType = [
        	{
        		"coord1": (1,2),
        		"coord2": (3,5)
        	},
        	{
        		"coord1": (0,1),
        		"coord2": (2,5)
        	}
        ]
        ```

        ### Modulo `mypy`

        El modulo mypy se complementa con el modulo typing ya que permitirá mostrar los errores de tipado debil en Python.

        Esto funciona desde python 3.6

    - Practicando el tipado estático

        Creamos un repositorio y entorno

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/84d06649-b455-43f2-b422-b28489cf031e/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/84d06649-b455-43f2-b422-b28489cf031e/Untitled.png)

- **Conceptos avanzados de funciones**
    - Scope: Alcance de las variables

        Resumen

        El scope es el alcance que tienen las variables. Depende de donde declares o inicialices una variable para saber si tienes acceso. **Regla de oro:**

        una variable solo esta disponible dentro de la region donde fue creada

        ### Local Scope

        Es la región que corresponde el ámbito de una función, donde podremos tener una o mas variables, las variables van a ser accesibles únicamente en esta region y no serán visibles para otras regiones.

        ```python
        def my_func():
        	y = 5 # y solo vive localmente
        	print(y)
        ```

        ### Global Scope

        Al escribir una o mas variables en esta region, estas podrán ser accesibles desde cualquier parte del código.

        ```python
        y = 5 # y vive en todo el código
        def my_func():
        	print(y)

        def my_other_func():
        	print(y+1)
        ```

        ![https://static.platzi.com/media/user_upload/Untitled-5d8878b2-048d-4017-a0de-a582e3f494d5.jpg](https://static.platzi.com/media/user_upload/Untitled-5d8878b2-048d-4017-a0de-a582e3f494d5.jpg)

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2cc9033d-dedb-4672-aff4-798cf9785f04/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2cc9033d-dedb-4672-aff4-798cf9785f04/Untitled.png)

    - Closures

        **Nested functions:** funciones creadas dentro de otra función

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/31e0f246-2a5a-4d69-b2d9-0a96da7b2f5b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/31e0f246-2a5a-4d69-b2d9-0a96da7b2f5b/Untitled.png)

        **Closure:** variable de un scope superior es recordada en un scope inferior, aún cuando se elimine.

        ```python
        def main():
            a = 1
            
            def nested():
                print(a)
                
            return nested
        my_func = main()
        my_func()
        del(main)
        my_func()

        #1
        #1
        ```

        **Reglas para encontrar un closure**

        1. Debemos tener una **nested function**
        2. la nested function **debe referenciar un valor de un scope superior**
        3. la función que envuelve la nested **debe retornarla también.**

        cuando tenemos una clase que tiene solo un método cuando trabajamos con decoradores

        ```python
        def make_multiplier(x):
            def multiplier(n):
                return x*n
            return multiplier

        times10 = make_multiplier(10)
        times4 = make_multiplier(4)

        print(times10(3)) #30
        print(times4(5)) #20
        print(times10(times4(2))) #80
        ```

        **¿Dónde aparecen los closures?**

        1. Clase corta con un objeto sirve para hacerlas más elegantes.
        2. Cuando trabajemos con decoradores.
    - Practicando Closures

        práctica closures.py

        ```python
        #Hola 3 -> HolaHolaHola
        #Felipe 4 -> FelipeFelipeFelipe

        def make_repeater_of(n):
            def repeater(string):
                assert type(string) == str, "Solo puedes utilizar cadenas" #afirmamos que nos llega una string
                return string*n
            return repeater

        def run():
            repeat_5 = make_repeater_of(5)
            print(repeat_5("Hola"))
            repeat_10 = make_repeater_of(10)
            print(repeat_5("Felipe"))

        if __name__ == '__main__':
            run()
        ```

        Reto: elaborar un closure makedivisionby(n) returna una función que retorna una división de un número x por n

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a5758a17-6239-46b1-8a5f-2a1920fe36a4/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a5758a17-6239-46b1-8a5f-2a1920fe36a4/Untitled.png)

    - Decoradores

        > Es un closure especial, es una función que recibe parametros de otra función, le añade cosas y retorna una función diferente

        ```python
        def decorador(func):
            def envoltura():
                print('esto se añade a mi función original')
                func()
            return envoltura

        def saludo():
            print('¡Hola!')
            
        #llamado sencillo
        saludo()

        #llamado decorado
        saludo = decorador(saludo)
        saludo()

        #output
        ¡Hola!
        esto se añade a mi función original
        ¡Hola!
        ```

        Una forma más pythonica es con 'Azúcar Sintáctica'/Sugar Syntax enbellece el código para comprenderlo mejor

        ```python
        def decorador(func):
            def envoltura():
                print('esto se añade a mi función original')
                func()
            return envoltura

        @decorador
        def saludo():
            print('¡Hola!')
            
        saludo()

        #output
        esto se añade a mi función original
        ¡Hola!
        ```

        Ejemplo:

        ```python
        def mayusculas(func):
        def envoltura(texto):
        return func(texto).upper()
        return envoltura

        @mayusculas
        def mensaje(nombre):
        return f'{nombre}, recibiste un mensaje'

        print(mensaje('Felipe'))

        #output
        FELIPE, RECIBISTE UN MENSAJE
        ```

    - Programando decoradores

        ```python
        from datetime import datetime

        def execution_time(func):
            def wrapper(*args, **kwargs):
                initial_time = datetime.now()
                func(*args, **kwargs)
                final_time = datetime.now()
                time_elapsed = final_time - initial_time
                print('execution time:' + str(time_elapsed.total_seconds())+' seconds')
            return wrapper

        @execution_time
        def random_func():
            for _ in range(1,10000000):
                pass

        @execution_time
        def sum(a: int, b: int) -> int:
            return a + b

        @execution_time
        def saludo(nombre):
            print("Hola " + nombre)

        random_func()
        sum(5,5)
        saludo('Felipe')
        #The wrapper needs to know the arguments and keyword args
        #that´s why we use "*args, **kwargs" in wraper and func

        #output
        execution time:0.121 seconds
        execution time:0.0 seconds
        Hola Felipe
        execution time:0.001002 seconds
        ```

- **Estructuras de datos avanzadas**
    - Iteradores

        ### Antes de entender qué son los iteradores, primero debemos entender a los iterables.

        Son todos aquellos objetos que podemos recorrer en un ciclo. Son aquellas estructuras de datos divisibles en elementos únicos que yo puedo recorrer en un ciclo.

        Pero en Python las cosas no son así. Los iterables se convierten en iteradores.

        Ejemplo:

        ```python
        # Creando un iterador

        my_list = [1,2,3,4,5]
        my_iter = iter(my_list)

        # Iterando un iterador

        print(next(my_iter))

        # Cuando no quedan datos, la excepción StopIteration es elevada
        ```

        ---

        ```python
        # Creando un iterador

        my_list = [1,2,3,4,5]
        my_iter = iter(my_list)

        # Iterando un iterador

        while True: #ciclo infinito
            try:
                element = next(my_iter)
                print(element)
            except StopIteration:
                break
        ```

        **Momento impactante:** El ciclo “for” dentro de Python, no existe. Es un while con StopIteration. 🤯🤯🤯

        For es Sugar Syntax in python

        ```python
        my_list = [1,2,3,4,5]

        for elementin my_list:
          print(element)
        ```

        **Construyamos nuestro iterador:**

        ---

        `evenNumbers.py`:

        ```python
        class EvenNumbers:
          """Clase que implementa un iterador de todos los números pares,
          o los números pares hasta un máximo
          """
          #Constructor de la clase
            def __init__(self, max =None): #self hace referencia al objeto futuro que voy a crear con esta clase
                self.max = max

         #Método para tener elementos o atributos que voy a necesitar para que el iterador funcione
            def __iter__(self):
                self.num = 0 #Primer número par
        				#Convertir un iterable en un iterador
                return self
         
        #Método para tener la función "next" de Python
            def __next__(self):
                if not self.max or self.num <= self.max:
                    result = self.num
                    self.num += 2
                    return result
                else:
                    raise StopIteration
        ```

        **Ventajas de usar iteradores:**

        1. Nos ahorra recursos.
        2. Ocupan poca memoria.
    - Practicando iteradores: Sucesión de Fibonacci

        vamos a crear un iterador de esta sucesión en python, almacenando cada elemento en la memoria.

        ```python
        import time

        class FiboIter():
            #in this case we dont init initializate so we don´t use __init__

            def __iter__(self):
                self.n1 = 0
                self.n2 = 1
                self.counter = 0
                return self

            def __next__(self):
                if self.counter == 0:
                    self.counter += 1
                    return self.n1
                elif self.counter == 1:
                    self.counter += 1
                    return self.n2
                else:
                    self.aux = self.n1 + self.n2
                    #self.n1 = self.n2
                    #self.n2 = self.aux
                    #We better use a swapping 👇🏽
                    self.n1, self.n2 = self.n2, self.aux
                    self.counter += 1
                    return self.aux

        if __name__ == '__main__':
            fibonacci = FiboIter()
            for element in fibonacci:
                print(element)
                time.sleep(0.05) #each print wait 0.05 secs for a better understanding of the iteration
        ```

        Reto:

        En lugar de almacenarla hasta el infinito, vamos a definirle un límite que una vez llegue a el eleve el error StopIteration

        ```python
        import time

        class FiboIter():
            def __init__(self, max_numb:int):
                self.max_numb = max_numb

            def __iter__(self):
                self.n1 = 0
                self.n2 = 1
                self.counter = 0
                return self

            def __next__(self):        
                if self.counter == 0:
                    self.counter += 1
                    return self.n1
                elif self.counter == 1:
                    self.counter += 1
                    return self.n2
                else:
                    self.aux = self.n1 + self.n2
                    if self.aux >= self.max_numb:
                        print(f"this program is limited to iterate until number {self.max_numb}")
                        raise StopIteration                 
                    self.n1, self.n2 = self.n2, self.aux
                    self.counter += 1
                    return self.aux
            
        if __name__ == '__main__':
            fibonacci = FiboIter(47)
            for element in fibonacci:
                print(element)
                time.sleep(0.05) #each print wait 0.05 secs for a better understanding of the iteration
        ```

    - Generadores

        Sugar Syntax para los Iteradores. Son funcionas que guardan un estado

        ```python
        def my_gen():

          """un ejemplo de generadores"""

          print('Hello world!')
          n = 0
          yield n # es exactamente lo mismo que return pero detiene la función, cuando se vuelva a llamar a la función, seguirá desde donde se quedó

          print('Hello heaven!')
          n = 1
          yield n

          print('Hello hell!')
          n = 2
          yield n

        a = my_gen()
        print(next(a)) # Hello world!
        print(next(a)) # Hello heaven!
        print(next(a)) # Hello hell!
        print(next(a)) #StopIteration
        ```

        yield nos pausa la función hasta donde estaba ese yield, cuando se vuelve a llamar la función inicia a partir del punto del yield anterior

        Ahora veremos un **generator expression** (es como list comprehension pero mucho mejor, porque podemos manejar mucha cantidadde información sin tener problemas de rendimiento):

        ```python
        #Generator expression

        my_list = [0,1,4,7,9,10]

        my_second_list = [x*2for x in my_list] #List comprehension
        my_second_gen = (x*2for x in my_list]) #Generator expression
        ```

        en el segundo caso se itera cada valor hasta obtener el resultado sin la necesidad de guardar en memoria cada valor.

    - Mejorando nuestra sucesión de fibonacci

        ```python
        import time

        def fibo_gen(max_num: int):
            n1, n2 = 0 , 1
            while n1 <= max_num:
                yield n1
                n1, n2 = n2, n1 + n2
            else:
                print(f"this program is limited to iterate until number {max_num}")    

        if __name__ == '__main__':
            fibonacci = fibo_gen(47)
            for element in fibonacci:
                print(element)
                time.sleep(0.05)

        #Output
        0
        1
        1
        2
        3
        5
        8
        13
        21
        34
        this program is limited to iterate until number 47
        ```

    - Sets

        **Un pequeño resumen**:

        Los sets son una estructura de datos muy similares a las listas en cuanto a su forma, pero presentan ciertas características particulares:

        - Los sets son **mutables, sus elementos son inmutables.**
        - Cada elemento del set es único, esto es que no se admiten duplicados, aun si durante la definición del set se agregan elementos repetidos pyhton solo guarda un elemento
        - los sets guardan los elementos en desorden.

        **A la derecha tenemos un set**

        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6246e75b-e908-42c1-b777-1617bf9a1512/Untitled.png)

        Para declararlos se utilizan los {} parecido a los diccionarios solo que carece de la composición de conjunto {a:b, c:d}

        ```python
        # set de enteros
        my_set = {1, 3, 5}
        print(my_set)

        # set de diferentes tipos de datos
        my_set = {1.0, "Hi", (1, 4, 7)}
        print(my_set)
        ```

        Los sets no pueden ser leídos como las listas o recorridos a través de slices, esto debido a que no tienen un criterio de orden. Sin embargo si podemos agregar o eliminar items de los sets utilizando métodos:

        - **add():** nos permite agregar elementos al set, si se intenta agregar un elemento existente simplemente python los ignorara
        - **update():** nos permite agregar múltiples elementos al set
        - **remove():** permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python elevará un error
        - **discard():** permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python dejará el set intacto, sin elevar ningún error.
        - **pop():** permite eliminar un elemento del set, pero lo hará de forma aleatoria.
        - **clear():** Limpia completamente el set, dejándolo vació.

        ```python
        #ejemplo de operaciones sobre sets
        my_set = {1, 2, 3}
        print(my_set) #Output {1, 2, 3}

        #añadiendo un elemento al set
        my_set.add(4)
        print(my_set) #Output {1, 2, 3, 4}

        #añadiendo varios elementos al set, python ignorará elementos repetidos
        my_set.update([1, 5, 6])
        print(my_set) #Output {1, 2, 3, 4, 5, 6}

        # eliminado elementos del set
        my_set.discard(1)
        print(my_set) #Output {2, 3, 4, 5, 6}

        # borrando un elemento aleatorio
        my_set.pop()
        print(my_set) #Output el set menos un elemento aleatorio

        #limpiar el set
        my_set.clear()
        print(my_set) # Output set()
        ```

        **Casting sets**

        Podemos utilizar estructuras de datos existentes para transformarlas a sets utilizando el método **set**:

        ```python
        #usando listas para crear sets
        my_list = [1, 2, 3, 3, 4, 5]
        my_set = set(my_list)
        print(my_set)  #output {1, 2, 3, 4, 5}

        #usando tuplas para crear sets
        my_tuple = ('hola', 'hola', 1, 2)
        my_set2 = set(my_tuple)
        print(my_set2) #Output {'hola', 1}
        ```

        **Añadir elementos al set**

        ```python
        my_set = {1,2,3}
        print(my_set)

        #add an element
        my_set.add(4)
        print(my_set)

        #add multiple elements
        my_set.update([1,2,5])
        print(my_set)

        #another way to add multiple elements
        my_set.update((1,7,2), {6,8})
        print(my_set)
        ```

        **Erasing elenments of a set**

        ```python
        my_set = {1, 2, 3, 4, 5, 6, 7, 8}
        print(my_set)

        my_set.discard(1)
        print(my_set)

        my_set.remove(2)
        print(my_set)

        my_set.discard(10)
        print(my_set)

        my_set.remove(12)
        print(my_set)

        #discard recive the order of existing and non-existing elements to erase and return the resulto
        #remove raise error if the element doesn't exist
        ```

        **Errasing random elements of a set or everything**

        ```python
        my_set = {1, 2, 3, 4, 5, 6, 7}
        print(my_set)

        my_set.pop()
        print(my_set)

        my_set.clear()
        print(my_set)
        ```

    - Operaciones con sets

        **Union (elementos of both sets |**

        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d15b1201-8219-42db-b8a5-31ec07d061bf/Untitled.png)

        **Interception (only common elements) &**

        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5a508896-4eaf-4056-9ca4-90f1631d5f77/Untitled.png)

        **Difference (taking out the uniques values of one set) -**

        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/14daecc5-4dda-491f-8d53-abdce8d9ce3a/Untitled.png)

        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7d0d924f-dbfc-48e3-8210-9ee8257f7336/Untitled.png)

        **Symmetric difference (inverse of the interception) ^**

        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a331c0f3-f211-48f3-b3f7-fe3f5514e174/Untitled.png)

        En caso de que quieran hacer operaciones con sets y hacerlo de forma más explícita pueden usar los métodos:

        ```python
        set1.union(set2)
        set1.symmetric_difference(set2)
        set1.difference(set2)
        set1.intersection(set2)
        ```

        Y pueden encontrar más métodos que pueden serles útiles [aquí](https://python-reference.readthedocs.io/en/latest/docs/sets/) 😄

    - Eliminando los repetidos de una lista

        Practicando el uso de los conjuntos

        Reto: crea un programa que elimine los elementos repetidos de una lista pero en lugar de utilizar un ciclo for utiliza sets.

        ```python
        #we need to create a solution that remove duplicates of a list and return the result
        #for example
        # [1,1,2,2,4] -> [1,2,4]

        def remove_duplicates(some_list):
            without_duplicates = []
            for element in some_list:
                if element not in without_duplicates:
                    without_duplicates.append(element)
            return without_duplicates

        #The challenges is to do the same but with sets

        def remove_duplicates_with_sets(some_list):
            return list(set(some_list))

        def run():
            random_list = [1,1,2,2,4]
            print("Removing duplicates with for loop: ", remove_duplicates(random_list))
            print("Removing duplicates with sets: ", remove_duplicates_with_sets(random_list))
            
        if __name__ == '__main__':
            run()
        ```

- **Bonus**
    - Manejo de fechas

        Utilizando de la mejor manera datetime

        ```python
        import datetime

        my_time = datetime.datetime.now()

        print(my_time)

        #Output
        #2021-08-13 07:27:52.130964
        ```

        Es importante evitar usar datetime.now() porque toma la hora local. Mejor usar datetime.utcnow() para usar la hora universal. Nosotros trabajamos con equipos de todo el mundo, no podemos usar hora local

        ```python
        import datetime

        my_time = datetime.datetime.utcnow()

        print(my_time)

        #Output
        #2021-08-13 12:28:59.812380
        ```

        Podemos acceder a distintos componentes de la fecha

        ```python
        import datetime

        my_day = datetime.date.today()

        print(f'Year: {my_day.year}')
        print(f'Month: {my_day.month}')
        print(f'Day: {my_day.day}')

        #Output
        #Year: 2021
        #Month: 8
        #Day: 13
        ```

        **Date formatting**

        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/04583357-939f-41fc-90b1-3e1ad17c2f61/Untitled.png)

        ```python
        from datetime import datetime

        my_datetime = datetime.now()
        print(my_datetime)

        my_str = my_datetime.strftime('%d/%m/%Y')
        print(f'Formato LATAM: {my_str}')

        my_str = my_datetime.strftime('%m/%d/%Y')
        print(f'Formato USA: {my_str}')

        my_str = my_datetime.strftime('Estamos en el año %Y')
        print(f'Formato Random: {my_str}')

        #Output
        from datetime import datetime

        my_datetime = datetime.now()
        print(my_datetime)

        my_str = my_datetime.strftime('%d/%m/%Y')
        print(f'Formato LATAM: {my_str}')

        my_str = my_datetime.strftime('%m/%d/%Y')
        print(f'Formato USA: {my_str}')

        my_str = my_datetime.strftime('Estamos en el año %Y')
        print(f'Formato Random: {my_str}')
        ```

    - Time zones

        Vamos a operar con los casos en que nuestras fechas deben interactuar con las zonas horarias de distintas partes del mundo

        instalación del módulo **pytz** en nuestro venv

        ```python
        from datetime import datetime
        import pytz

        bogota_timezone = pytz.timezone('America/Bogota')
        bogota_date = datetime.now(bogota_timezone)
        print("Bogota:", bogota_date.strftime('%d/%m/%Y, %H:%M:%S'))

        mexico_timezone = pytz.timezone('America/Mexico_City')
        mexico_date = datetime.now(mexico_timezone)
        print("Ciudad de México:", mexico_date.strftime('%d/%m/%Y, %H:%M:%S'))

        caracas_timezone = pytz.timezone('America/Caracas')
        caracas_date = datetime.now(caracas_timezone)
        print("Caracas:", caracas_date.strftime('%d/%m/%Y, %H:%M:%S'))
        ```

- **Conclusión**
    -