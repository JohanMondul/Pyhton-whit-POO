from Principal import Preguntas
import json


users=[
    {
      "User": "johan",
      "Password": "10"
    },
    {
      "User": "root",
      "Password": "root"
    },
    {
      "User": "Johan",
      "Password": "2220"
    }
  ]


#Mostrar Resultado



def login():
    print ("\n----------INICIO DE SESION---------- ")    
    usuario=input("\n Ingrese usuario: ")
    password=input ("\n Ingrese Contraseña: ")
    val1 = False
    while val1 != True:
        for user in users:
                    ##  Valida usuario y contraseña 
            if usuario == user["User"] and password== user["Password"]:
                        ##Variable para colocar nombre del usuario
                global persona
                persona=usuario
                print ("Usted Ingreso Correctamente \n"+"Bienvenido: "+ persona+" \n")
                val1 = True
                menu1()
            else:
                print("Contraseña o Usuario erroneo")
                login()
                    

#Menu de opciones
def menu1():
    while True:

        print("------------Menu----------.\n\
        1.- Iniciar el programas\n\
        2.- Consultar historial \n\
        3.- Salir")

        n1 = (input("Ingrese la opcion deseada:  "))

        if n1 != '' and n1.isnumeric() == True:
            num = int(n1)
            #Opcion numero 1 sistemas de reglas
            if num < 4:
                if num == 1:
                    Preguntas()
                elif num == 2:
                    Consultar()
                #Opcion numero 3 salir 
                elif num == 3:
                    print("Gracias por su tiempo!!")
                    quit()
            else:

                print("Opcion incorrecta!! ")
            continue


def Consultar():
        seguir= True
        while(seguir):
            numcorrect=False
            while(not numcorrect):  
                print ("1- Consultar por usuario")                     
                print ("2- Consultar por id")
                print ("3- Salir")
                n2=input("Seleccione una Opción: ")
                if n2 != '' and n2.isnumeric() == True:
                    num2 = int(n2)
                if num2== 1:
                    Usuarioconsu()
                elif num2== 2:
                    Idconsu()
                else:
                    seguir=False
                    print ("Gracias!\n")
                    break   

def Usuarioconsu():
    with open("resultado.json")as archivo:
        datos= json.load(archivo)
        contador=0
        usuario=input("\n Ingrese usuario: ")
        #Recorre los diferentes datos en el json resultados                 
        for dato in datos["Datos"]:
            if usuario == dato["Usuario"] :
                contador+=1
                print(dato)
        if contador==0:
            print( "No se encontro historico de usuario o usuario no existe") 
                    

def Idconsu():
    with open("resultado.json")as archivo:
        datos= json.load(archivo)
        contador=0
        id=int(input("\n Ingrese id: "))
        #Recorre los diferentes datos en el json resultados                 
        for dato in datos["Datos"]:
            if id == dato["id"] :
                contador+=1
                print(dato)
                           
        if contador== 0:
            print( "No se encontro historico de usuario o usuario no existe") 





login()