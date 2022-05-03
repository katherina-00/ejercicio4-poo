class Ventana:
    __titulo: ""
    __valorY_Izq:0
    __valorX_Izq:0
    __valorY_Der:500
    __valorX_Der:500

    def __init__(self,titulo,valorY_Izq,valorX_Izq,valorY_Der,valorX_Der):
        if (((valorX_Izq & valorY_Izq)>0) & ((valorY_Der & valorX_Der)<500)):
            self.__titulo=titulo
            self.__valorY_Izq=valorY_Izq
            self.__valorX_Izq=valorX_Izq
            self.__valorY_Der=valorY_Der
            self.__valorX_Der=valorX_Der

    def getTitulo(self):
        return self.__titulo
    def getValorY_Izq(self):
        return  self.__valorY_Izq
    def getValorX_Izq(self):
        return  self.__valorX_Izq
    def getValorY_Der(self):
        return self.__valorY_Der
    def getValorX_Der(self):
        return self.__valorX_Der

    def mostrar(self):
        print(f"Titulo: {self.__titulo}, Valor Y izquierdo: {self.__valorY_Izq}, Valor x izquierdo: {self.__valorX_Izq}, "
              f"Valor Y derecho: {self.__valorY_Der}, Valor X derecho: {self.__valorX_Der}")

        #dibuja un rectangulo con *
        '''
        anchura = (self.__valorX_Der + self.__valorX_Izq)
        altura = (self.__valorY_Izq + self.__valorY_Der)
        for i in range(altura):
            for j in range(anchura):
                print("* ", end="")
            print() '''

    def alto(self):
        return self.__valorY_Der+self.__valorY_Izq

    def ancho(self):
        return self.__valorX_Der+self.__valorX_Izq

    def moverDerecha(self,cant):
        self.__valorX_Izq-=cant
        self.__valorX_Der+=cant

    def moverIzquierda(self,cant):
        self.__valorX_Izq+=cant
        self.__valorX_Der-=cant

    def bajar(self,cant):
        self.__valorY_Izq-=cant
        self.__valorY_Der+=cant

    def subir(self,cant):
        self.__valorY_Izq+=cant
        self.__valorY_Der-=cant
