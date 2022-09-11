from Reglas import *




class Sistemadereglas(KnowledgeEngine):
    
    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c1(self):
        
        print("SU TELEVISOR ESTA, OK!")

    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="no" or "NO" or "No" or "nO")))
    
    def c2(self):
        
        print("SU TELEVISOR TIENE LOS PARLANTES DAÑADOS")

    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="no" or "NO" or "No" or "nO")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c3(self):
        
        print("EL LED SE ENCUENTRA QUEMADO")

    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c4(self):
        
        print("DAÑO EN LA FUENTE DE PODER")

    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="no" or "NO" or "No" or "nO")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c5(self):
        
        print("DAÑO EN LA FUENTE DE PODER CON LED QUEMADO")

    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="no" or "NO" or "No" or "nO")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="no" or "NO" or "No" or "nO")))
    
    def c6(self):
        
        print("COMPONENTES DE FUENTE Y AUDIO QUEMADOS")

    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="no" or "NO" or "No" or "nO")))
    
    def c7(self):
        
        print("DAÑO DE VIDRIO DEL DISPLAY CON PARLANTES ROTOS")

    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c8(self):
        
        print("DAÑO DE VIDRIO DEL DISPLAY")

    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="no" or "NO" or "No" or "nO")))
    
    def c9(self):
        
        print("DAÑO EN LA FUENTE DE PODER Y EN LOS PARLANTES")

    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="no" or "NO" or "No" or "nO")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="no" or "NO" or "No" or "nO")))
    
    def c10(self):
        
        print("DAÑO EN VIDRIO DE PANTALLA CON LED QUEMADO CON PARLANTES")

    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="no" or "NO" or "No" or "nO")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c11(self):
        
        print("DAÑO EN VIDRIO DE PANTALLA CON LED QUEMADO ")

    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c12(self):
        
        print("DAÑO INTERNO EN LA MOTHERBOARD")

    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="no" or "NO" or "No" or "nO")))
    
    def c13(self):
        
        print("DAÑO EN EL CRISTAL DEL DISPLAY CON PROBLEMAS DE AUDIO Y MOTHER BOARD")

    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="no" or "NO" or "No" or "nO")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="no" or "NO" or "No" or "nO")))
    
    def c14(self):
        
        print("TELEVISOR CON MULTPLES DAÑOS")

    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="no" or "NO" or "No" or "nO")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c15(self):
        
        print("MOTHERBOARD DAÑADA MAS LED QUEMADO")

    @Rule(AND(reglas(Imagen="si" or "SI" or "Si" or "sI")),(reglas(Ledin="no" or "NO" or "No" or "nO")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="no" or "NO" or "No" or "nO")))
    
    def c16(self):
        
        print("PARLANTES Y LED QUEMADOS")

    ##################################

    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c17(self):
        
        print("DISPLAY ROTO")
    
    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="no" or "NO" or "No" or "nO")))
    
    def c18(self):
        
        print("DISPLAY ROTO Y PARLANTES QUEMADAS")

    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="no" or "NO" or "No" or "nO")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c19(self):
        
        print("DISPLAY ROTO Y LED QUEMADO")

    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c20(self):
        
        print("DISPLAY ROTO Y DAÑO EN LA FUENTE")

    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="no" or "NO" or "No" or "nO")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c21(self):
        
        print("DAÑO EN FUENTE Y POSIBLE DAÑO EN LA MOTHER BOARD")

    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="no" or "NO" or "No" or "nO")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="no" or "NO" or "No" or "nO")))

    def c22(self):
        
        print("DAÑOS MULTIPLES POR QUEMADO INTERNO")

    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="no" or "NO" or "No" or "nO")))
    
    def c23(self):
        
        print("DISPLAY ROTO Y PARLANTES QUEMADAS")

    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c24(self):
        
        print("PANTALLA COMPLETA DAÑADA")

    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="no" or "NO" or "No" or "nO")))
    
    def c25(self):
        
        print("PANTALLA COMPLETA DAÑADA MAS PARLANTES QUEMADAS")

    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="no" or "NO" or "No" or "nO")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="no" or "NO" or "No" or "nO")))
    
    def c26(self):
        
        print("DISPLAY,LED Y PARLANTES QUEMADAS")

    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c27(self):
        
        print("PANTALLA COMPLETA DAÑADA MAS LED QUEMADO")

    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c28(self):
        
        print("PANTALLA COMPLETA DAÑADA MAS DAÑO EN LA FUENTE")

    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="si" or "SI" or "Si" or "sI")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="no" or "NO" or "No" or "nO")))
    
    def c29(self):
        
        print("TELEVISOR CON MULTPLES DAÑOS")

    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="no" or "NO" or "No" or "nO")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="no" or "NO" or "No" or "nO")))
    
    def c30(self):
        
        print("IRREPARABLE!!")
    
    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="no" or "NO" or "No" or "nO")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr ==2) & P(lambda Lineasr:Lineasr > 2))),
    (reglas(Reini=P(lambda Reini:Reini ==2) & P(lambda Reini:Reini > 2))),(reglas(Sonido="si" or "SI" or "Si" or "sI")))
    
    def c31(self):
        
        print("IRREPARABLE!!")

    @Rule(AND(reglas(Imagen="no" or "NO" or "No" or "nO")),(reglas(Ledin="no" or "NO" or "No" or "nO")),
    (reglas(Lineasr=P(lambda Lineasr:Lineasr >=0) & P(lambda Lineasr:Lineasr <= 1))),
    (reglas(Reini=P(lambda Reini:Reini >=0) & P(lambda Reini:Reini <= 1))),(reglas(Sonido="no" or "NO" or "No" or "nO")))
    
    def c32(self):
        
        print("PANTALLA DAÑADA MAS PARLANTE Y LED INDICADOR QUEMADAS")

    