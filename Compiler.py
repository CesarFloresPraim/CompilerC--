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
    """int main(void){ 
int i;
i = 0;
if (a[i] >= x[]){
x = a[i];
k = i;
}
return ;
}/* END of main() */""": True,
"""/* A program to perform selection sort on a
10 element array */
int x[10];
int miniloc(int a[], int low, int high){
int i; int x; int k;
k = low;
x = a[low];
i = low + 1;
while (i < high){
if (a[i] < x){
x = a[i];
k = i;
}
i = i + 1;
}
return k;
}/* END of miniloc() */
void sort(int a[], int low, int high){
int i; int k;
i = low;
while (i < high - 1){
int t;
k = minloc(a,I,high);
t = a[k];
a[k] = a[i];
a[i] = t;
i = i +1;
}
}/* END of sort() */
void main(void){
int i;
i = 0;
while (i < 10){
input x[i];
i = i + 1;
}
sort(x,0,10);
i = 0;
while (i < 10){
output x[i];
i = i + 1;
}
}/* END of main() *//* A program to perform selection sort on a
10 element array */
int x[10];
int miniloc(int a[], int low, int high){
int i; int x; int k;
k = low;
x = a[low];
i = low + 1;
while (i < high){
if (a[i] < x){
x = a[i];
k = i;
}
i = i + 1;
}
return k;
}/* END of miniloc() */
void sort(int a[], int low, int high){
int i; int k;
i = low;
while (i < high - 1){
int t;
k = minloc(a,I,high);
t = a[k];
a[k] = a[i];
a[i] = t;
i = i +1;
}
}/* END of sort() */
void main(void){
int i;
i = 0;
while (i < 10){
input x[i];
i = i + 1;
}
sort(x,0,10);
i = 0;
while (i < 10){
output x[i];
i = i + 1;
}
}/* END of main() */""": True
}
#Check errors on table size
for fila in tablaTransicion.values():
     if len(fila) != 21:
        print(len(fila))
        print('Tabla mal')

for fila in tablaTransicion:
    tablaTransicion.update({fila: dict(zip(tablaHeader, tablaTransicion[fila]))})

#print(tablaTransicion)

class Lexer:

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
            print("(LEXER): Error: unexpected token '{1}' after '{0}'".format(self.lecturaActual,simbolo))

        aceptacion = True if nuevoEstado in estadosAceptacion else False

        #mando a tablas
        if aceptacion:
            #Si estado es 6 que es id encontrado guarda el valor en su respectiva tabla
            if nuevoEstado == 10:
                if self.lecturaActual not in keywords:
                    tablaStrings.append({"Lexema": self.lecturaActual})
                    tablaTokens.append({"type": "id", "value": self.lecturaActual})
                else:
                    tablaTokens.append({"type": "keyword", "value": self.lecturaActual})
                self.setEstadoValor(0, False)
                self.lecturaActual = ""
            #Si estado es 7 que es number encontrado guarda el valor en su respectiva tabla
            elif nuevoEstado == 11:
                tablaNumeros.append({"Lexema": int(self.lecturaActual)})
                tablaTokens.append({"type": "number", "value": int(self.lecturaActual)})
                self.setEstadoValor(0, False)
                self.lecturaActual = ""
            #Token sencillo encontrado y no doble se guarda el valor en su respectiva tabla
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

        
        #Si estado actual es 1 de strings y hay una letra acutla guardar valor hasta que haya un delimitador
        if (nuevoEstado == 1) and letra:
            self.setLecturaActual(letra)
         #Si estado actual es 2 de numero y hay un numero actual guardar valor valor hasta que haya un delimitador
        elif nuevoEstado == 2 and numero:
            self.setLecturaActual(numero)
        #Otro caracter
        else:
            #Si el simbolo es espacio no ignorar y no append  ninguna tabla
            if simbolo != " " and simbolo != '\n':
                self.setLecturaActual(simbolo)
            #Si se encuentra en un estado de aceptacion, guardara el valor acutal a menos que sea un comentario
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

class Parser:

    global tablaTokens

    def __init__(self):
        self.currentTokenValue = 0
        self.currentTokenType = 0
        self.currentTokenIndex = 0
        self.error = False

    def __str__(self):
        return str(self.current_token_value)

#    1.	declarationList -> int ID declaration declarationListPrime | void ID ( paramsList ) compundStmtVoid declarationListPrime
    def declarationList(self):
        #print("declarationList  -> ", self.currentTokenValue)
        if (self.currentTokenType == "keyword" and self.currentTokenValue == "int"):
            self.match("int")
            self.match("id")
            self.declaration()
            self.declarationListPrime()

        elif (self.currentTokenType == "keyword" and self.currentTokenValue == "void"):
            self.match("void")
            self.match("id")
            self.match("(")
            self.paramsList()
            self.match(")")
            self.compundStmtVoid()
            self.declarationListPrime()

        else:
            print("Error in declaration list")
            return
#    2.	declarationListPrime -> int ID declaration declarationListPrime | void ID ( paramsList ) compundStmtVoid declarationListPrime | epsilon
    def declarationListPrime(self):
        #print("declarationListPrime  -> ", self.currentTokenValue)
        if (self.currentTokenType == "keyword" and self.currentTokenValue == "int"):
            self.match("int")
            self.match("id")
            self.declaration()
            self.declarationListPrime()

        elif (self.currentTokenType == "keyword" and self.currentTokenValue == "void"):
            self.match("void")
            self.match("id")
            self.match("(")
            self.paramsList()
            self.match(")")
            self.compundStmtVoid()
            self.declarationListPrime()

        elif (self.currentTokenType == "EOF" and self.currentTokenValue == "$" and self.error != True):
            print("(PARSER): ExitIng with status : (accepted)")
            return

        else:
            print("(PARSER): ExitIng with status : (not-accepted)")
            print("")
            return
#    3.	declaration -> varOrArrayDeclaration ; | ( paramsList ) compountStmtNoVoidReturn

    def declaration(self):
        #print("declaration  -> ", self.currentTokenValue)
        if (self.currentTokenType == "symbol" and self.currentTokenValue == "("):
            self.match("(")
            self.paramsList()
            self.match(")")
            self.compountStmtNoVoidReturn()
        else:
            self.varOrArrayDeclaration()
            self.match(";")
#    4.	varOrArrayDeclaration -> [arithmeticExpression]  | epsilon
    def varOrArrayDeclaration(self):
        #print("varOrArrayDeclaration  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "["):
            self.match("[")
            self.arithmeticExpression()
            self.match("]")
        elif (self.currentTokenValue == ";"
                or self.currentTokenValue == "="
                or self.currentTokenValue == "{"
                or self.currentTokenType == "id"
                or self.currentTokenValue == "if"
                or self.currentTokenValue == "while"
                or self.currentTokenValue == "input"
                or self.currentTokenValue == "output"
                or self.currentTokenValue == "}"
                or self.currentTokenValue == "return"
                or self.currentTokenValue == "-"
                or self.currentTokenValue == "+"
                or self.currentTokenValue == "]"
                or self.currentTokenValue == "<="
                or self.currentTokenValue == "<"
                or self.currentTokenValue == ">"
                or self.currentTokenValue == ">="
                or self.currentTokenValue == "=="
                or self.currentTokenValue == "!="
                or self.currentTokenValue == ")"
                or self.currentTokenValue == "else"
                or self.currentTokenValue == ","
        ):
            return
        else:
            print("")
            return
#    5.	paramsList -> int ID paramVarOrArray paramsListPrime | void
    def paramsList(self):
        #print("paramsList  -> ", self.currentTokenValue)
        if (self.currentTokenType == "keyword" and self.currentTokenValue == "int"):
            self.match("int")
            self.match("id")
            self.paramVarOrArray()
            self.paramsListPrime()
        elif (self.currentTokenType == "keyword" and self.currentTokenValue == "void"):
            self.match("void")
        else:
            print("")
            return
#    6.	paramsListPrime -> , int  ID param_array paramsListPrime | epsilon
    def paramsListPrime(self):
        #print("paramsListPrime  -> ", self.currentTokenValue)
        if (self.currentTokenType == "symbol" and self.currentTokenValue == ','):
            self.match(",")
            self.match("int")
            self.match("id")
            self.paramVarOrArray()
            self.paramsListPrime()
        elif (self.currentTokenValue == ")"):
            return
        else:
            print("")
            return
#   7.	paramVarOrArray -> [ ] | epsilon
    def paramVarOrArray(self):
        #print("paramVarOrArray  -> ", self.currentTokenValue)
        if (self.currentTokenType == "symbol" and self.currentTokenValue == "["):
            self.match("[")
            self.match("]")
        elif (self.currentTokenValue == "," or self.currentTokenValue == ")"):
            return
        else:
            print("")
            return
#   8.	compundStmtVoid -> { localDeclarations stmtListVoid }
    def compundStmtVoid(self):
        #print("compundStmtVoid  -> ", self.currentTokenValue)
        if (self.currentTokenType == "symbol" and self.currentTokenValue == "{"):
            self.match("{")
            self.localDeclarations()
            self.stmtListVoid()
            self.match("}")
        else:
            print("")
            return
#   9.	compountStmtNoVoidReturn -> { localDeclarations stmtListNoVoid returnStmtNoVoid }
    def compountStmtNoVoidReturn(self):
        #print("compountStmtNoVoidReturn  -> ", self.currentTokenValue)
        if (self.currentTokenType == "symbol" and self.currentTokenValue == "{"):
            self.match("{")
            self.localDeclarations()
            self.stmtListNoVoid()
            self.returnStmtNoVoid()
            self.match("}")
        else:
            print("")
            return
#   10.	compundStmtNoVoidNoReturn -> { localDeclarations stmtListNoVoid }
    def compundStmtNoVoidNoReturn(self):
        #print("compundStmtNoVoidNoReturn  -> ", self.currentTokenValue)
        if (self.currentTokenType == "symbol" and self.currentTokenValue == "{"):
            self.match("{")
            self.localDeclarations()
            self.stmtListNoVoid()
            self.match("}")
        else:
            print("")
            return
#   11.	localDeclarations ->  int ID varOrArrayDeclaration; localDeclarations | epsilon
    def localDeclarations(self):
        #print("localDeclarations  -> ", self.currentTokenValue)
        if (self.currentTokenType == "keyword" and self.currentTokenValue == "int"):
            self.match("int")
            self.match("id")
            self.varOrArrayDeclaration()
            self.match(";")
            self.localDeclarations()
        elif (self.currentTokenValue == "{"
              or self.currentTokenValue == "}"
              or self.currentTokenType == "id"
              or self.currentTokenValue == "if"
              or self.currentTokenValue == "while"
              or self.currentTokenValue == "input"
              or self.currentTokenValue == "output"
              or self.currentTokenValue == "return"):
            return
        else:
            print("")
            return
#   13.	stmtListVoid ->  stmtVoid stmtListVoid | epsilon
    def stmtListVoid(self):
        #print("stmtListVoid  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "{"
            or self.currentTokenType == "id"
            or self.currentTokenValue == "if"
            or self.currentTokenValue == "while"
            or self.currentTokenValue == "input"
            or self.currentTokenValue == "output"):
            self.stmtVoid()
            self.stmtListVoid()
        elif (self.currentTokenValue == "}"):
            return
        else:
            print("")
            return
#   14.	stmtListNoVoid ->  stmtNoVoid stmtListNoVoid | epsilon
    def stmtListNoVoid(self):
        #print("stmtListNoVoid  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "{"
            or self.currentTokenType == "id"
            or self.currentTokenValue == "if"
            or self.currentTokenValue == "while"
            or self.currentTokenValue == "input"
            or self.currentTokenValue == "output"):
            self.stmtNoVoid()
            self.stmtListNoVoid()
        elif (self.currentTokenValue == "return" or self.currentTokenValue == "}"):
            return
        else:
            print("")
            return
#   15.	stmtVoid -> assignmentCallStmt | compundStmtVoid | selectionStmtVoid | loopStmtVoid | ioStmt 
    def stmtVoid(self):
        #print("stmtVoid  -> ", self.currentTokenValue)
        if (self.currentTokenType == "id"):
            self.assignmentCallStmt()
        elif (self.currentTokenValue == "{"):
            self.compundStmtVoid()
        elif (self.currentTokenValue == "if"):
            self.selectionStmtVoid()
        elif (self.currentTokenValue == "while"):
            self.loopStmtVoid()
        elif (self.currentTokenValue == "input" or self.currentTokenValue == "output"):
            self.ioStmt()
        else:
            print("")
            return
#   16.	stmtNoVoid -> assignmentCallStmt | compundStmtNoVoidNoReturn | selectionStmtNoVoid | loopStmtNoVoid | returnStmtNoVoid | ioStmt
    def stmtNoVoid(self):
        #print("stmtNoVoid  -> ", self.currentTokenValue)
        if (self.currentTokenType == "id"):
            self.assignmentCallStmt()
        elif (self.currentTokenValue == "{"):
            self.compundStmtNoVoidNoReturn()
        elif (self.currentTokenValue == "if"):
            self.selectionStmtNoVoid()
        elif (self.currentTokenValue == "while"):
            self.loopStmtNoVoid()
        elif (self.currentTokenValue == "return"):
            self.returnStmtNoVoid()
        elif (self.currentTokenValue == "input" or self.currentTokenValue == "output"):
            self.ioStmt()
        else:
            print("")
            return
#   17.	ioStmt -> inputStmt | outputStmt
    def ioStmt(self):
        #print("ioStmt  -> ", self.currentTokenValue)
        if(self.currentTokenValue == "input"):
            self.inputStmt()
        elif(self.currentTokenValue == "output"):
            self.outputStmt()
        else:
            print("")
            return
#   18.	assignmentCallStmt -> ID assignmentCallStmtPrime ;
    def assignmentCallStmt(self):
        #print("assignmentCallStmt  -> ", self.currentTokenValue)
        if (self.currentTokenType == "id"):
            self.match("id")
            self.assignmentCallStmtPrime()
            self.match(";")
        else:
            print("")
            return
#   19.	assignmentCallStmtPrime -> varOrArrayDeclaration = expression  | ( args )
    def assignmentCallStmtPrime(self):
        #print("assignmentCallStmtPrime  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "("):
            self.match("(")
            self.args()
            self.match(")")
        elif (self.currentTokenValue == "[" or self.currentTokenValue == "="):
            self.varOrArrayDeclaration()
            self.match("=")
            self.expression()
        else:
            print("")
            return
#   20.	selectionStmtVoid -> if  ( expression )  stmtVoid  selectionStmtNoVoidElsePart
    def selectionStmtVoid(self):
        #print("selectionStmtVoid  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "if"):
            self.match("if")
            self.match("(")
            self.expression()
            self.match(")")
            self.stmtVoid()
            self.selectionStmtNoVoidElsePart()
        else:
            print("")
            return
#   21.	selectionStmtNoVoidElsePart ->  else  stmtVoid  | epsilon
    def selectionStmtNoVoidElsePart(self):
        #print("selectionStmtNoVoidElsePart  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "else"):
            self.match("else")
            self.stmtVoid()
        elif (self.currentTokenValue == "{"
              or self.currentTokenValue == "}"
              or self.currentTokenType == "id"
              or self.currentTokenValue == "if"
              or self.currentTokenValue == "while"
              or self.currentTokenValue == "input"
              or self.currentTokenValue == "output"):
            return
        else:
            print("")
            return
#   22.	selectionStmtNoVoid -> if  ( expression )  stmtNoVoid  selectionStmtNoVoidElsePart
    def selectionStmtNoVoid(self):
        #print("selectionStmtNoVoid  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "if"):
            self.match("if")
            self.match("(")
            self.expression()
            self.match(")")
            self.stmtNoVoid()
            self.selectionStmtNoVoidElsePart()
        else:
            print("")
            return
#   23.	selectionStmtNoVoidElsePart ->  else  stmtNoVoid  | epsilon
    def selectionStmtNoVoidElsePart(self):
        #print("selectionStmtNoVoidElsePart  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "else"):
            self.match("else")
            self.stmtNoVoid()
        elif (self.currentTokenValue == "{"
              or self.currentTokenValue == "}"
              or self.currentTokenType == "id"
              or self.currentTokenValue == "if"
              or self.currentTokenValue == "while"
              or self.currentTokenValue == "return"
              or self.currentTokenValue == "input"
              or self.currentTokenValue == "output"):
            return
        else:
            print("")
            return
#   24.	loopStmtVoid -> while ( expression )  stmtVoid
    def loopStmtVoid(self):
        #print("loopStmtVoid  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "while"):
            self.match("while")
            self.match("(")
            self.expression()
            self.match(")")
            self.stmtVoid()
        else:
            print("")
            return
#   25.	loopStmtNoVoid -> while ( expression )  stmtNoVoid
    def loopStmtNoVoid(self):
        #print("loopStmtNoVoid  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "while"):
            self.match("while")
            self.match("(")
            self.expression()
            self.match(")")
            self.stmtNoVoid()
        else:
            print("")
            return
#   26.	returnStmtNoVoid -> return returnStmtNoVoidPrime;
    def returnStmtNoVoid(self):
        #print("returnStmtNoVoid  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "return"):
            self.match("return")
            self.returnStmtNoVoidPrime()
            self.match(";")
        else:
            print("")
            return
#   27.	returnStmtNoVoidPrime -> expression | epsilon
    def returnStmtNoVoidPrime(self):
        #print("returnStmtNoVoidPrime  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "("
                or self.currentTokenType == "number"
                or self.currentTokenType == "id"):
            self.expression()

        elif (self.currentTokenValue == ";"):
            return
        else:
            print("")
            return
#   28.	inputStmt -> input ID varOrArrayDeclaration ;
    def inputStmt(self):
        #print("inputStmt  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "input"):
            self.match("input")
            self.match("id")
            self.varOrArrayDeclaration()
            self.match(";")
        else:
            print("")
            return
#   29.	outputStmt -> output expression ;
    def outputStmt(self):
        #print("outputStmt  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "output"):
            self.match("output")
            self.expression()
            self.match(";")
        else:
            print("")
            return
#   30.	expression -> arithmeticExpression expressionPrime
    def expression(self):
        #print("expression  -> ", self.currentTokenValue)
        if(self.currentTokenValue == '('
            or self.currentTokenType == 'id'
            or self.currentTokenType == 'number'):

            self.arithmeticExpression()
            self.expressionPrime()
        else:
            print("")
            return
#   31.	expressionPrime -> relop arithmeticExpression | epsilon
    def expressionPrime(self):
        #print("expressionPrime  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "<="
                or self.currentTokenValue == "<"
                or self.currentTokenValue == ">="
                or self.currentTokenValue == ">"
                or self.currentTokenValue == "=="
                or self.currentTokenValue == "!="):
            self.relop()
            self.arithmeticExpression()
        elif (self.currentTokenValue == ";" 
                or self.currentTokenValue == ")"
                or self.currentTokenValue == "}"
                or self.currentTokenValue == "{"
                or self.currentTokenType == "id"
                or self.currentTokenValue == "if"
                or self.currentTokenValue == ")"
                or self.currentTokenValue == "while"
                or self.currentTokenValue == "return"
                or self.currentTokenValue == "input"
                or self.currentTokenValue == "output"
                or self.currentTokenValue == "else"):
            return
        else:
            print("")
            return
#   32.	relop -> <= | < | > | >= | == | !=
    def relop(self):
        #print("relop  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "<="):
            self.match("<=")
        elif (self.currentTokenValue == "<"):
            self.match("<")
        elif (self.currentTokenValue == ">="):
            self.match(">=")
        elif (self.currentTokenValue == ">"):
            self.match(">")
        elif (self.currentTokenValue == "=="):
            self.match("==")
        elif (self.currentTokenValue == "!="):
            self.match("!=")
        else:
            print("")
            return
#   33.	arithmeticExpression -> term expPrime
    def arithmeticExpression(self):
        #print("arithmeticExpression  -> ", self.currentTokenValue)
        if(self.currentTokenValue == "(" or self.currentTokenType == "id" or self.currentTokenType == "number"):
            self.term()
            self.expPrime()
        else:
            print("")
            self.error = True
            return
#   34.	expPrime ->  + term exp' | - term exp' | epsilon
    def expPrime(self):
        #print("expPrime  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "+"):
            self.match("+")
            self.term()
            self.expPrime()
        elif(self.currentTokenValue == "-"):
            self.match("-")
            self.term()
            self.expPrime()
        elif (self.currentTokenValue == "]"
              or self.currentTokenValue == "<="
              or self.currentTokenValue == "<"
              or self.currentTokenValue == ">="
              or self.currentTokenValue == ">"
              or self.currentTokenValue == "=="
              or self.currentTokenValue == "!="
              or self.currentTokenValue == ";"
              or self.currentTokenValue == ")"
              or self.currentTokenValue == "}"
              or self.currentTokenValue == "{"
              or self.currentTokenType == "id"
              or self.currentTokenValue == "if"
              or self.currentTokenValue == "while"
              or self.currentTokenValue == "return"
              or self.currentTokenValue == "input"
              or self.currentTokenValue == "output"
              or self.currentTokenValue == ","
              or self.currentTokenValue == "else"):
            return
        else:
            print("")
            return
#   35.	term -> factor termPrime
    def term(self):
        #print("term  -> ", self.currentTokenValue)
        if(self.currentTokenValue == "(" or self.currentTokenType == "id" or self.currentTokenType == "number"):
            self.factor()
            self.termPrime()
        else:
            print("")
            return
#   36.	termPrime -> * factor termPrime | / factor termPrime | epsilon
    def termPrime(self):
        #print("termPrime  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "*"):
            self.match("*")
            self.factor()
            self.termPrime()
        elif(self.currentTokenValue == "/"):
            self.match("/")
            self.factor()
            self.termPrime()
        elif (self.currentTokenValue == "+"
              or self.currentTokenValue == "-"
              or self.currentTokenValue == "]"
              or self.currentTokenValue == "<="
              or self.currentTokenValue == "<"
              or self.currentTokenValue == ">="
              or self.currentTokenValue == ">"
              or self.currentTokenValue == "=="
              or self.currentTokenValue == "!="
              or self.currentTokenValue == ";"
              or self.currentTokenValue == ")"
              or self.currentTokenValue == "}"
              or self.currentTokenValue == "{"
              or self.currentTokenType == "id"
              or self.currentTokenValue == "if"
              or self.currentTokenValue == "while"
              or self.currentTokenValue == "return"
              or self.currentTokenValue == "input"
              or self.currentTokenValue == "output"
              or self.currentTokenValue == ","
              or self.currentTokenValue == "else"):
            return
        else:
            print("")
            return
#   37.	factor -> ( arithmeticExpression ) | ID varOrCall | NUM
    def factor(self):
        #print("factor  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "("):
            self.match("(")
            self.arithmeticExpression()
            self.match(")")
        elif (self.currentTokenType == "number"):
            self.match("number")
        elif (self.currentTokenType == "id"):
            self.match("id")
            self.varOrCall()
        else:
            print("")
            return
#   38.	varOrCall -> varOrArrayDeclaration | ( args ) 
    def varOrCall(self):
        #print("varOrCall  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "("):
            self.match("(")
            self.args()
            self.match(")")
        elif (self.currentTokenValue == '[' 
        or self.currentTokenValue == '-'  
        or self.currentTokenValue == '+' 
        or self.currentTokenValue == ']' 
        or self.currentTokenValue == '<='    
        or self.currentTokenValue == '<'     
        or self.currentTokenValue == '>'   
        or self.currentTokenValue == '>='  
        or self.currentTokenValue == '=='   
        or self.currentTokenValue == '!='  
        or self.currentTokenValue == ';'  
        or self.currentTokenValue == ')'  
        or self.currentTokenValue == '}'    
        or self.currentTokenValue == '{' 
        or self.currentTokenType == 'id' 
        or self.currentTokenValue == 'if' 
        or self.currentTokenValue == 'while' 
        or self.currentTokenValue == 'return'
        or self.currentTokenValue == 'input' 
        or self.currentTokenValue == 'output' 
        or self.currentTokenValue == ',' 
        or self.currentTokenValue == 'else'):
            self.varOrArrayDeclaration()
        else:
            print("")
            return
#   39.	args -> arithmeticExpression argsList | epsilon
    def args(self):
        #print("args  -> ", self.currentTokenValue)
        if (self.currentTokenValue == "("
                or self.currentTokenType == "number"
                or self.currentTokenType == "id"):
            self.arithmeticExpression()
            self.argsList()
        elif (self.currentTokenValue == ")"):
            return
        else:
            print("")
            return
#   40.	argsList -> , arithmeticExpression argsList | epsilon
    def argsList(self):
        #print("argsList  -> ", self.currentTokenValue)
        if (self.currentTokenValue == ","):
            self.match(",")
            self.arithmeticExpression()
            self.argsList()
        elif (self.currentTokenValue == ")"):
            return

    def match(self, tokenValue):
        if (self.currentTokenType == tokenValue):
            #print("Matched Id:", tokenValue,", against -> ", self.currentTokenType)
            self.nextToken()
        elif (self.currentTokenValue == tokenValue):
            #print("Matched -> ", tokenValue,", against -> ", self.currentTokenValue)
            self.nextToken()
        else:
            print("Not matched -> ", tokenValue,", against -> ", self.currentTokenValue)

    def nextToken(self):
        self.currentTokenIndex = self.currentTokenIndex + 1
        self.currentTokenType = tablaTokens[self.currentTokenIndex]['type']
        self.currentTokenValue = tablaTokens[self.currentTokenIndex]['value']




def main():
    global tablaTokens
    global tablaStrings
    global tablaNumeros
    
    lexer = Lexer()
    parser = Parser()
    print("\n")
    for testCase, value in testCases.iteritems():
        #print(testCase)
        for simbolo in testCase:
            lexer.transicion(simbolo)
        if lexer.getEstadoAcutal() in [3,4]:
            print('(LEXER) Error: Reached EOF and comment closing token missing ')
        #Unexpected end of file
        if lexer.getEstadoAcutal() in [1,2,5,6,7,8,9]:
            print("(LEXER): Error: Unexpected EOF found '{0}' not in acceptance state, missing delimiter after".format(lexer.lecturaActual))
        lexer.setEstadoValor(0,False)

        tablaTokens.append({"type": "EOF", "value": "$"})
        # print("___Tabla de tokens___")
        # pprint(tablaTokens)
        # print("\n")
        # print("___Tabla de strings___")
        # pprint(tablaStrings)
        # print("\n")
        # print("___Tabla de numeros___")
        # pprint(tablaNumeros)
        # print("\n")
        parser.currentTokenIndex = 0
        parser.currentTokenValue = tablaTokens[0]['value']
        parser.currentTokenType = tablaTokens[0]['type']
        parser.error = False
        parser.declarationList()

        tablaTokens=[]
        tablaStrings=[]
        tablaNumeros=[]

if __name__ == "__main__":
    main()