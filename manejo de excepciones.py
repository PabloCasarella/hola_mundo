'''Manejo de excepciones.

Es posible escribir programas que manejen excepciones seleccionadas. Mire el siguiente ejemplo, que le pide al usuario que ingrese hasta que se haya ingresado un numero entero valido, pero que le permite al usuario interrumpir el programa usando o lo que admita el sistema operativo); tengan en cuenta que una interrpcion generada por el usuario se señala al generar la excepcion.'''

while True:
    try:
        x = int(input("please, enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")

print("hola")

'''La try declaracion funciona de la siguiente manera:
* Primero, se ejecuta la clausula try (las declaraciones entre las palabras clave try y except.

* Si no se produce excepcion, se omite la clausula try y finaliza la declaracion.

* Si se produce una excepcion durante la ejecucion de la clasula try, se omite el resto de la clausula. Luego, si su tipo coincide con la excepcion nombrada despues de la palabra clave except, se ejecuta la clausula de la excepcion y luego la ejecucion continua despues del bloque try/except.

* Si ocurre una excepcion que no coindice con la excepcion nombrada en la clusula de excepcion, se pasa a las try declaraciones externas; si no se encuentra un controlador, es una excepcion no controlada y la ejecucion se detiene con un mensaje como se muestra arriba.

Una declaracion try puede tener mas una clausula excepto, para especificar controladores para diferentes excepciones. Como maximo se ejecutara un controlador. Los controladores solo manejan las excepciones que ocurren en la clausula try correspondiente, no en otros controladores de la misma try declaracion. Una clausula de excepcion puede nomnbrar multiples excepciones como una tupoa entre parentesis, por ejemplo:

except (RuntimeError, TypeError, NameError):
    pass

'''


