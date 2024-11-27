class Personaje():
    def __init__(self,personaje,raza,nivel):
        self.personaje=personaje
        self.raza=raza
        self.nivel=nivel
        self.habilidades=[]
        self.transformaciones=[("super",1.5),("kaioken",2.5)]




    def transformaciones_(self):
        
        nivel=self.nivel
        if not self.transformaciones:
            return nivel
    

        print("1. habilidad")
        print("2. transformarse")
        print("3. cancelar")         #interfaz de seleccion general

        opcion=input()

        if opcion=="2":

            for i in range(len(self.transformaciones)):
                transformacions,multi=self.transformaciones[i]
                print("{}.{}".format(i+1,transformacions))

            transformacion=int(input("eliga una transformacion: "))

            transf,multip=self.transformaciones[transformacion-1]
            self.nivel=self.nivel*multip       #se multiplica el poder por la transformacion elegida
            
            del self.transformaciones[transformacion-1]

            return self.transformaciones_()
        
        else:
            return f"nivel de poder final= {nivel}"




poder=Personaje("goku","sayayin",200)
final=poder.transformaciones_()
print(final)







