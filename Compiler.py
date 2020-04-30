from pprint import pprint

tablaHeader = ["letter", "digit", "+", "-", "/", "*", "<", ">", "=", "!", ";", ",", "(", ")", "[", "]", "{", "}", " ", "\n"]

tablaTransicion = {
    0:	[1,	2,	14,	15,	5,	16,	6,	7,	8,	9,	18,	19,	20,	21,	22,	23,	24,	25,	0,	0,	0],
    1:	[1, 25,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	6,	6],
    2:	[25, 2,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	7,	7],
    3:	[3, 3,	3,	3,	3,	4,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3],
    4:	[3, 3,	3,	3,	13,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3],
    5:	[12, 12, 12, 12, 12, 3,	12,	12,	12,	12,	12,	12,	12,	12,	12,	12,	12,	12,	12,	12,	12],
    6:	[26, 26, 26, 26, 26, 26,26,	26,	17,	26,	26,	26,	26,	26,	26,	26,	26,	26,	26,	26,	26],
    7:	[27, 27, 27, 27, 27, 27,27,	27,	17,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27],
    8:	[28, 28, 28, 28, 28, 28,28,	28,	17,	28,	28,	28,	28,	28,	28,	28,	28,	28,	28,	28,	28],
    9:	[29, 29, 29, 29, 29, 29,29,	29,	17,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29]
}

estadosAceptacion = []
estadosError = []

tablaIdentificadores = []
tablesNumeros = []

estadosAceptacion = [i for i in range(10,30)]
estadosError = [30]

keywords = ["if", "else", "input", "output", "int", "return", "while", "void"]

tablaTokens = []
tablaStrings = []
tablaNumeros = []

mensajesError = []
testCases = {
    "/*AB/C */ if (4  <5){var =46  /": False,
    "/*AB/C */ if (4  <5){var =46  /;": True,
    "/* x= 34 <=": False,
    "if (4$  <5){var =46": False,
}
#Check errors on table size
for fila in tablaTransicion.values():
     if len(fila) != 21:
         print(len(fila))
         print('Tabla mal')

for fila in tablaTransicion:
    tablaTransicion.update({fila: dict(zip(tablaHeader, tablaTransicion[fila]))})

#print(tablaTransicion)

class Estado:

    def __init__(self):
        self.estado = 0
        self.valor = False
        self.lecturaActual = ""
        print('Estado es: ', str(self))

    def __str__(self):
        return str(self.estado)

    def getEstadoAcutal(self):
        return self.estado

    def getEstadoValorAcutal(self):
        return self.valor
    
    def setEstadoValor(self, estado, valor):
        self.estado = estado
        self.valor = valor
    
    def setLecturaActual(self, simbolo):
        self.lecturaActual += simbolo

    def transicion(self, simbolo):
        if simbolo in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            letra = simbolo
            simbolo = 'letter'
        elif simbolo in ['1','2','3','4','5','6','7','8','9','0']:
            numero = simbolo
            simbolo = 'digit'


        #Si el estado no esta en la tabla de transicion
        if self.getEstadoAcutal() not in tablaTransicion:
            error = True if self.getEstadoAcutal() in estadosError else False
            #Si esta en estado de error
            if error:
                return self.setEstadoValor(self.getEstadoAcutal(), 'Error')
            aceptacion = True if self.getEstadoAcutal() in estadosAceptacion else False
            return self.setEstadoValor(self.getEstadoAcutal(), aceptacion)

        #Transiscion posible
        try:
             nuevoEstado = tablaTransicion[self.getEstadoAcutal()][simbolo]
        except KeyError:
            nuevoEstado = 30
            print("Error: unexpected token '{1}' after '{0}'".format(self.lecturaActual,simbolo))

        aceptacion = True if nuevoEstado in estadosAceptacion else False

        #mando a tablas
        if aceptacion:
            #Si estado es 6 que es identifier encontrado
            if nuevoEstado == 10:
                if self.lecturaActual not in keywords:
                    tablaStrings.append({"Lexema": self.lecturaActual})
                else:
                    tablaTokens.append({"type": "keyword", "value": self.lecturaActual})
                self.setEstadoValor(0, False)
                self.lecturaActual = ""
            #Si estado es 7 que es number encontrado
            elif nuevoEstado == 11:
                tablaNumeros.append({"Lexema": int(self.lecturaActual)})
                #tablaTokens.append({"type": "symbol", "value": int(self.lecturaActual)})
                self.setEstadoValor(0, False)
                self.lecturaActual = ""
            #Single token, not double
            elif nuevoEstado in [26,27,28,29,12]:
                tablaTokens.append({"type": "symbol", "value": self.lecturaActual})
                self.setEstadoValor(0, False)
                self.lecturaActual = ""
            
            #Transiscion posible
            nuevoEstado = tablaTransicion[self.getEstadoAcutal()][simbolo]
            aceptacion = True if nuevoEstado in estadosAceptacion else False

        error = True if nuevoEstado in estadosError else False
        #Si esta en estado de error
        if error:
            return self.setEstadoValor(nuevoEstado, 'Error')

        
        #Si estado actual es 1 de strings y hay una letra acutla guardar valor
        if (nuevoEstado == 1) and letra:
            self.setLecturaActual(letra)
         #Si estado actual es 2 de numero y hay un numero actual guardar valor
        elif nuevoEstado == 2 and numero:
            self.setLecturaActual(numero)
        #Otro caracter
        else:
            #Si el simbolo es espacio no append
            if simbolo != " ":
                self.setLecturaActual(simbolo)
            if nuevoEstado in estadosAceptacion:
                #Difernete de comment
                if nuevoEstado != 13:
                    tablaTokens.append({"type": "symbol", "value": self.lecturaActual})
                    self.lecturaActual = ""
                #comment found
                else:
                    self.lecturaActual = ""
                return self.setEstadoValor(0, False)
        return self.setEstadoValor(nuevoEstado, aceptacion)


def main():
    global tablaTokens
    global tablaStrings
    global tablaNumeros
    
    estado = Estado()
    print("\n")
    for testCase, value in testCases.iteritems():
        print(testCase)
        for simbolo in testCase:
            estado.transicion(simbolo)
        if estado.getEstadoAcutal() in [3,4]:
            print('Error: Reached EOF and comment closing token missing ')
        #Unexpected end of file
        if estado.getEstadoAcutal() in [1,2,5,6,7,8,9]:
            print("Error: Unexpected EOF found '{0}' not in acceptance state, missing delimiter after".format(estado.lecturaActual))
        
        estado.setEstadoValor(0,False)

        print("___Tabla de tokens___")
        pprint(tablaTokens)
        print("\n")
        print("___Tabla de strings___")
        pprint(tablaStrings)
        print("\n")
        print("___Tabla de numeros___")
        pprint(tablaNumeros)
        print("\n")

        tablaTokens = []
        tablaStrings = []
        tablaNumeros = []
if __name__ == "__main__":
    main()