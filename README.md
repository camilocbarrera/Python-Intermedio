# Curso de Python Intermedio

# 1. ****Algunas cosas que aprenderás sobre Python en este curso****

Para tomar este curso se necesita un conocimiento previo, es importante si no se tiene el conocimiento esencial. Qué se tome el curso básico de python y el curso de github para manejar control de versiones y ser ordenados con nuestras clases y el código que construimos.

# 2. ****El Zen de Python****

El zen de Python son los 20 principios de software más importantes que tienen Python para poder escribir nuestras líneas de código de manera correcta y precisa. Fueron creados por Tim Peaters en 1990.

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>>
```

# 3. ****¿Qué es la documentación?****

La documentación es ese espacio de información que explica detalladamente cómo creamos nuestro artefacto. Podemos compararla como con el manual de un producto que viene con un manual de instrucciones.

[https://docs.python.org/3.9/](https://docs.python.org/3.9/)

[https://www.python.org/dev/peps/pep-0008/#introduction](https://www.python.org/dev/peps/pep-0008/#introduction)

 

# 4. ****¿Qué es un entorno virtual?****

Es cómo tener un python para cada proyecto, en cada uno de los proyectos podemos definir de manera dedicada una versión y módulos o librerías. Entonces de forma virtual podemos aislar cada Python y cada librería para proyectos especificos.

# 5. ****El primer paso profesional: creación de un entorno virtual****

Así se crea un ambiente virtual o venv. Esto en el entorno de windows. 

 Desde nuestra consola debemos ejecutar este comando para crear un ambiente virtual de python.

## Creando un entorno virtual en Windows

`python -m venv venv`

El `venv` del final es básicamente el nombre del ambiente virtual, sin embargo puede tener un nombre personalizado.

La m significa que vamos a llamar un módulo

## Activando el ambiente virtual  (Windows)

`source venv/Scripts/activate`

Aquí nos aparece entonces entre paréntesis `(venv)`  que representa que ya estamos apuntando directamente a ese virtual envirnoment.

## Desactivar el ambiente virtual

Sólo basta con escribir en la consola el comando `deactivate`

## Crear un alias para el comando de activar 🙊

Desde la consola de git bash se puede utilizar este comando 

`alias avenv="source ./venv/Scripts/activate”`

en donde avenv ese el nuevo alias que representa la forma para activar el virtual environment.

# 6. ****Instalación de dependencias con pip****

Dentro de python existen diferentes módulos que ya vienen por defecto con python, pero hay algunos módulos o librerías que no están por defecto con python, entonces estas se deben instalar. Este proceso se realiza a través de un manejador de dependencias o manejador de paquetes.  El más popular dentro de python es `pip` **(Package Installer for Python)** que viene por defecto instalado con python en la mayoría de sus versiones. Dentro de los módulos más no vienen instalados con Python encontramos algunos que son muy populares cómo:

- Requests (Web Scraping)
- BeatifulSoup4
- Pandas (Data Science)
- Numpy
- Pytest (Testing)

## Instalando módulos mediante PIP

La idea es instalar estas depedencias dentro de nuestro ambiente virtual. 

Entonces lo primero que debo hacer es: 

- Activar mi ambiente virtual
- Con el comando `pip freeze` puedo comprobar que módulos tengo instalado en este momento. (En mac o linux es un poco diferente)
- Ejemplo, si queremos instalar pandas. Sólo basta con ejecutar `pip install pandas`. Cómo pandas es un módulo tan complejo, requiere de módulos de dependencia.

```python
$ pip freeze
numpy==1.22.2
pandas==1.4.0
python-dateutil==2.8.2
pytz==2021.3
six==1.16.0
```

- Es normal ver una advertencia de tipo WARNING para actualizar pip

## ¿Que pasa si quiero compartir este proyecto con otra persona en otro lugar del mundo?

En ocasiones requerimos compartir nuestros proyectos para trabajar en equipo, por esta razón nace la necesidad de crear una lista de requerimientos con las dependencias que utiliza mi proyecto.

Para ello podemos guardar la salida del comando `pip freeze` en un archivo de texto plano el cual se suele llamar `requirements.txt` . Esto se puede hacer con el siguiente comando:

`pip freeze > requirements.txt`

Este comando crear el archivo con los módulos listados. Podemos comprobarlo con el comando `cat requierements.txt`

### Instalando dependencias desde un requirements.txt

Para instalar las dependencias debemos ejeutar el siguiente comando:

`pip install -r requirements.txt`

**pyenv** y **pipenv**

# 7. ****Listas y diccionarios anidados****

Primero elegimos nuestro directorio, creamos un repositorio para seguir las buenas practicas. Ahora podemos comenzar. 

Una buena practica, es ignorar el directorio del venv/ que contiene nuestro ambiente de trabajo. Eso lo debemos hacer en el archivo .gitignore . Si no existe lo creamos y comenzamos a agregar los directorios y archivos que quiero que sean ignorados.

```python
my_list = [1, 2,'hellow', True, 4.5]
    my_dict = {'firstname': 'Cristian Camilo','lastname': 'Correa Barrera'}
    super_list = [
        {'firstname': 'Cristian Camilo','lastname': 'Correa Barrera'},
        {'firstname': 'Pepe','lastname': 'Torres'},
        {'firstname': 'Susana','lastname': 'Martinez'},
        {'firstname': 'José','lastname': 'García'},
        {'firstname': 'Amanda','lastname': 'Silva'}
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums':[-1, -2, 0, 1, 2],
        'floating_nums':[1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key,' : ',value)

    for dicti in super_list:
        print(dicti['firstname'],' : ',dicti['lastname'])
```

De ahora en adelanta debemos comenzar a programar en inglés.

# 8. ****List comprehensions****

[ element `for`  element `in`  itreable `if`  condition ]

- Element Representa a cada uno de los elementos a poner en la nueva lista
- For Ciclo a partir del cual se extraerán elementos de otra lista o cualquier estructura iterable.
- If condición opcional para filtrar los elementos del ciclo

Para cada elemento en el iterable, sólo voy a guardar ese elemento si se cumple esa condición.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d303d265-9ec5-4df8-8236-3c0a49818374/Untitled.png)

Para cada i de los números de 1..101 voy a guardar esa i al cuadrado sólo si la i mod 3 es diferente de cero.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/376e3e25-ad69-408e-9c25-82bb58db4e31/Untitled.png)

```python
# vamos a resolver el mismo problema con list comprenhension
    squares = [i**2 for i in range(1,101) if i % 3 != 0 ]
    # print(squares)

    squares_b = [i for i in range(1,100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 ]
    print(squares_b)
```

# 9. D****ictionary comprehensions****

[ element `for`  element `in`  itreable `if`  condition ]

- Element Representa a cada uno de los elementos a poner en la nueva lista
- For Ciclo a partir del cual se extraerán elementos de otra lista o cualquier estructura iterable.
- If condición opcional para filtrar los elementos del ciclo

Para cada elemento en el iterable, sólo voy a guardar ese elemento si se cumple esa condición.

```python
my_dic = {i: i**3 for i in range(1,101,1) if i % 3 != 0}

{key:value for value in itreable if condition}
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3959effd-e960-47b2-aceb-a19301445257/Untitled.png)

Para cada elemento en un iterable, voy a colocar una llave y un valor sólo si cumple la condición en donde el módulo sea diferente de 0.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a529301f-07e9-4d01-af3b-447947cf97c3/Untitled.png)

```python
	  my_dic = {i: i**3 for i in range(1,101,1) if i % 3 != 0}

    dictionary_challenge = {i: round(i**(1/2),2) for i in range(1,1001,1) if True }

    print(dictionary_challenge)

    # for i in range(1,101,1):
        # if i % 3 != 0:
            # my_dic[i] = i**3
            
    print(my_dic)
    # for k,v in my_dic.items():
        # print(k,' : ', v)
```

# 10. ****Funciones anónimas: lambda****

Existe una manera distinta de escribir funciones, en python se llaman lambda functions  o funciones anónimas. 

Estas son las llamadas funciones anonimas, funciones sin identificador. (Sin nombre)

### **lambda argumentos: expresión**

```python
# Esto es una lambda function
palindrome = lambda string: string == string[::-1]
print(palindrome('ana))

# así se haría con una función no lambda
def palindrome(string):
	return string == string[::-1]

print(palindrome('ana'))

#ambas cosas son lo mismo :3
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/74c0e857-b279-4bd0-816c-c4312ee88f74/Untitled.png)

El nombre que va a tener esta función será la variable que va a guardar el objeto de tipo función. Que esta expresión retorna. (No requiere la palabra return

# 11. ****High order functions: filter, map y reduce (Funciones de orden superior)****

Una función de orden superior es una función que recibe como parámetro a otra función.

Ejemplo: En la función saludo se recibe un parametro de tipo función.

```python
def saludo(func):
	func()

def hola():
	print("Hola!!!")

def adios():
	print("Adioss!!")

saludo(hola)
saludo(adios)
```

Hay tres funciones de orden superior que son sumamente importantes y son clasicos.

## Filter

Supongamos que tenemos una lista con los siguientes números

```sql
[1, 4, 5, 6, 9, 13, 19, 21]
# Solución con List comprenhension
# Un número es impar sólo si al dividirlo entre dos es diferente de cero.
    resp = [i for i in numbers if i%2 !=0]
    # print(resp)

#Ahora vamos a resolverlo con filter
# vamos a leer esto
# ¿Que hace la función labda?
# Recibe cómo parametro una x
#  y retorna el resultado x%2 !=0 
# Filter es una función de orden superior
# Recibe una función (lambda funtion) y un iterable, (cualquier elemento de Python que pueda iterarse)
# Esto retorna  un iterador
# El List de afuera es para pasar el iterador en una lista

    odd = list(filter(lambda x: x%2 !=0, numbers))

    print(odd)
```

## Map

De la misma manera que filter map funciona así 

```sql
# Map
# Primeoro con list comprenhension
    numbers = [1,2,3,4,5]
    resp = [i**2 for i in numbers]
    # print(resp)

#Esto mismo se puede resover con map
    squares = list(map(lambda x: x**2, numbers))
    print(squares)
```

## Reduce

Para usar reduce es necesario importar un módulo desde fun tools

```sql
from functools import reduce

all_mult = reduce(lambda a,b : a * b, numb)
    print(all_mult)
```

# 12. Filtrando datos

A partir de un diccionario voy a crear diferentes filtros.

```sql
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
```

```python
# all_python_devs = [ worker["name"] for worker in DATA if worker["language"] == "python"  ]
all_python_devs = list(filter(lambda worker: worker["language"].lower()=="python", DATA ))

# all_platzi_workers = [ worker["name"] for worker in DATA if worker["organization"].lower()=="platzi" ]

all_platzi_workers = list(filter(lambda worker: worker["organization"].lower() =="platzi", DATA ))
all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers ))

# adults = list( filter( lambda worker: worker["age"] > 18, DATA ) )

adults = [ w["name"] for w in DATA if w["age"]>18 ]

old_people = list(map(lambda worker: worker | {"old":worker["age"] > 70 },DATA))

old_people = [ worker | {"old":worker["age"] > 70 } for worker in DATA if worker["age"] > 70 ]

for x in old_people:
    print(x["name"]," tiene ", x["age"], " Es viejo ¿? ", x["old"])
    
```

# 13. Los errores en el código

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6f7105ef-6db3-4889-84da-6c3bf36c687d/Untitled.png)

- Para resolver los errores hay que revisarlo paso a paso linea por linea para entender en donde está el error.
- El otro tipo de error son las excepciones. Los syntax error detienen el programa. Pueden ser typos o errores de escritura.
- **KeyboardInterrupt:**  Excepción cuando pulsamos ctrl + c . Aquí todo se corta y se eleva una excepción. Python Crea un objeto de tipo excepción y lo va moviendo desde adentro hacia afuera.
- **KeyError:** Cuando intentamos acceder a una llave que no existe.
- **IndexError**:  ****Sucede cuando trabajamos con listas e intentamos acceder a un elemento que no existe.
- **FileNotFoundError:** Cuando intentamos importar un archivo y no es encontrado
- **ZeroDivisionError:** Error de división en cero
- **ImportError:** Cuando no se encuentra una librería o modulo en Python

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/85341ac8-4270-4453-8054-a38d16bdf383/Untitled.png)

¿Cómo se lee un traceback?

La mayoría de las personas, comienza a leer de inicio hacia el final. Pero lo mejor es leer desde la ultima linea hacia arriba.

# 14. Debugging

Debugging o depuración, es una herramienta que traen las ides por lo general se hace así
