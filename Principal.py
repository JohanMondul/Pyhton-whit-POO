from random import choice
from sistemadereglas import *
import json


resultado={ }
resultado['Datos']=[]

def Preguntas():
    
    ## creacion del objeto
    engine = Sistemadereglas()
    ### reset Preparar el motor para la ejecución.
    engine.reset()
    ## se pregunta por la Marca deseada
    Imagen1 = input("Bienvenido a su tienda Online de disgnostico de TV \n\
        Su televisor muestra imagen? \n\
        si o no: ")
    if Imagen1 != '' and Imagen1.isalpha() == True:
        Imagen = Imagen1
        engine.declare(reglas(Imagen=choice([Imagen])))
    else:
        vali1 = False
        while(vali1 == False):
            print("Valor es numerico  por favor digite la opcion entre si y no\n")
            Imagen1 = input("Bienvenido a su tienda Online de disgnostico de TV \n\
            Su televisor muestra imagen? \n\
             1) menos de 2 \n\
             2) mas de 2  :  ")
            if Imagen1 != '' and Imagen.isalpha() == True:
                Imagen = Imagen1
                engine.declare(reglas(Imagen=choice([Imagen])))
                vali1 = True
                print("Repuesta correcta \n")
    
        

    ## se pregunta por las pulgadas
    Ledin1 = input("Su televisor prende el led indicador de energia? \n\
        si o no: ")
    if Ledin1 != '' and Ledin1.isalpha() == True:
        Ledin = Ledin1
        engine.declare(reglas(Ledin=choice([Ledin])))
    else:
        vali2 = False
        while(vali2 == False):
            print("Valor es numerico  por favor digite la opcion entre si y no\n")
            Ledin1 = input("Su televisor prende el led indicador de energia? \n\
            si o no: ")
            if Ledin1 != '' and Ledin.isalpha() == True:
                Ledin = Ledin1
                engine.declare(reglas(Ledin=choice([Ledin])))
                vali2 = True
                print("Repuesta correcta \n")

    ## se pregunta por el precio maximo a pagar
    Lineasr1 = input("Cuantas lineas de quebrado tiene su televisor: ")
    if Lineasr1 != '' and Lineasr1.isnumeric() == True:
        Lineasr=Lineasr1
        engine.declare(reglas(Lineasr=choice([int(Lineasr)])))
    else:
        vali3 = False
        while(vali3 == False):
            print("Valor no es numerico \n")
            Lineasr1 = input("Cuantas lineas de quebrado tiene su televisor: ")
            if Lineasr1 != '' and Lineasr1.isnumeric() == True:
                Lineasr = Lineasr1
                engine.declare(reglas(Lineasr=choice([int(Lineasr)])))
                vali3 = True
                print("Repuesta correcta \n")
            

    ## se pregunta por el metodo de pago
    Reini1= input("En 1 minuto cuantas veces se reinicia?:")
    ## declare agrega un hecho
    ##La función choice(secuencia) elige un valor al azar en un conjunto de elementos.
    if Reini1 != '' and Reini1.isnumeric() == True:
        Reini=Reini1
        engine.declare(reglas(Reini=choice([int(Reini)])))
    else:
        vali4 = False
        while(vali4 == False):
            print("Valor no es numerico \n")
            Reini1 = input("En 1 minuto cuantas veces se reinicia?:")
            if Reini1 != '' and Reini1.isnumeric() == True:
                Reini = Reini1
                engine.declare(reglas(Reinir=choice([int(Reini)])))
                vali4 = True
                print("Repuesta correcta \n")
    
    ## se pregunta si desea pagar el coste del envio a domicilio
    Sonido1= input("Su Televisor reproduce sonido? \n\
        si o no:  ")
    ## declare agrega un hecho
    ##La función choice(secuencia) elige un valor al azar en un conjunto de elementos.
    if Sonido1 != '' and Sonido1.isalpha() == True:
        Sonido = Sonido1
        engine.declare(reglas(Sonido=choice([Sonido])))
    else:
        vali5 = False
        while(vali5 == False):
            print("Valor es numerico  por favor digite la opcion entre si y no")
            Sonido1 = input("Su Televisor reproduce sonido?")
            if Sonido1 != '' and Sonido.isalpha() == True:
                Sonido = Sonido1
                engine.declare(reglas(Sonido=choice([Sonido])))
                vali5 = True
                print("Repuesta correcta \n")


    #definimos unas variables global para poder en el otro metodo usarlas  
    global Imagen2
    Imagen2 = Imagen
    
    global Ledin2
    Ledin2 = Ledin

    global Lineasr2
    Lineasr2 = Lineasr

    global Reini2
    Reini2 = Reini

    global Sonido2
    Sonido2 = Sonido

    engine.run()


    if len(Sonido2) > 0:
        guadar_datos()
        print("Guardo")
    


def guadar_datos():
    conid = 0
    conid+=1

    resultado["Datos"].append({
                'id':conid,
                    'Usuario': "Johan Mondul",
                    'Preguntas':[ 
                                    "1- Su televisor muestra imagen ?",
                                    "2- Su televisor prende el led indicador de energia ?",
                                    "3- Cuantas lines de roto tiene su televisor ?",
                                    "4- En 1 minuto cuantas veces se reinicia ?",
                                    "5- Tiene sonido ?"
                                                                         ],               
                'Respuestas Usuario':[
                        "Imagen: "+Imagen2,
                        "Led indicador: "+Ledin2,
                        "lines de rotura: "+Lineasr2,
                        "Reinicia: "+Reini2,
                        "Sonido: "+Sonido2
                                                    ]

    })
    with open ('resultado.json', 'w') as file:
                json.dump (resultado,file,indent=4)
                print ("\n ¡Datos Ingresados Correctamente! \n")
    
    
    


    ## Buenas profesor, quisiera que por favor cuando vea esto si es que lo ve, me pueda explicar como hago para que cuando termine y guarde vuelva al menu
    ## cuando lo importo para llamarlo me marca error

                