import os, sys
from math import pi,    sqrt,sin


def Funcion_Muy_Mala(nombreee ,  edad ,ciudad="Desconocida",profesion = 'Programador' ):
    # Mezcla de comillas simples y dobles, espacios extraños
    mensaje = "Hola "+nombreee+' de '+  ciudad  + "!"
    
    # Una lista gigante en una sola línea (para probar el line-wrap)
    mi_lista_gigante = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, "manzana", "pera", "platano", "uvas", "sandia"]

    # Sangría inconsistente y operadores pegados
    calculo_raro=( (edad*50) + (100/3) ) / pi
    if calculo_raro>10:
      print(  mensaje  )
    else:
            print("Resultado bajo")

    # Un diccionario muy mal indentado
    dicc = {'llave1': 'valor1', 'llave2':
'valor2',      'llave3':'valor3'
        }
    
    return { "calculo":calculo_raro,"datos" : [  nombreee,edad,ciudad  ] }

# Más código sucio al final
resultado_final=Funcion_Muy_Mala("Juan",30,  ciudad="Madrid"  )
print(   resultado_final   )