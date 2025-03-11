from ply import yacc
from analizador_lexico import tokens

# -----------------
# ÁRBOL GRAMATICAL|
# -----------------
# El árbol gramatical representa la estructura jerárquica y gramatical de un código fuente cuando la 
# sintaxis es correcta. Se construye a partir de las producciones de las reglas gramaticales durante 
# el análisis sintáctico y léxico, donde los símbolos no terminales se descomponen en terminales (tokens) 
# u otros no terminales. Cada nodo del árbol representa un símbolo, y las ramas conectan nodos hijos (hojas). 
# El árbol comienza con el símbolo no terminal raíz ("programa") y se descompone hasta llegar a los terminales, 
# que no pueden descomponerse más (elementos léxicos).

# Estructura de un nodo en el árbol gramatical
class Nodo:
    def __init__(self, simbolo, valor=None, hijo=None):
        self.simbolo = simbolo
        self.valor = valor
        self.hijo = hijo if hijo is not None else []

    def __str__(self):
        if self.valor is not None: # Es terminal (token) y no se puede descomponer más
            return f'{self.simbolo}: {self.valor}'
        else: # Es no terminal y se descompone en más simbolos
            return f'{self.simbolo}'
        
# Precedencias para los operadores aritméticos
precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'PRODUCTO', 'DIVISION', 'MODULO'),
)

# Reglas de producción

# Programa inicial
def p_programa(p):
    '''
    programa : lista_declarativas inicio
             | inicio
    '''
    if len(p) == 3:
        p[0] = Nodo('programa', hijo=[p[1], p[2]])
    else:
        p[0] = Nodo('programa', hijo=[p[1]])

# Declarativas
def p_lista_declarativas(p):
    '''
    lista_declarativas : declarativa lista_declarativas
                       | declarativa
    '''
    if len(p) == 3:
        p[0] = Nodo('lista_declarativas', hijo=[p[1], p[2]])
    else:
        p[0] = Nodo('lista_declarativas', hijo=[p[1]])

def p_declarativa(p):
    '''
    declarativa : inclusion
    '''
    p[0] = Nodo('declarativa', hijo=[p[1]])

# Inclusión de biblioteca
def p_inclusion(p):
    '''
    inclusion : INCLUIR BIBLIOTECA
    '''
    p[0] = Nodo('inclusion', hijo=[Nodo('INCLUIR', valor=p[1]), Nodo('BIBLIOTECA', p[2])])

# Función principal
def p_inicio(p):
    '''
    inicio : ENTERO PRINCIPAL PARENTESIS_IZQ lista_parametros PARENTESIS_DER bloque
           | ENTERO PRINCIPAL PARENTESIS_IZQ PARENTESIS_DER bloque
    '''
    if len(p) == 7:
        p[0] = Nodo('inicio', hijo=[Nodo('ENTERO', valor=p[1]), Nodo('PRINCIPAL', valor=p[2]), Nodo('PARENTESIS_IZQ', valor=p[3]), p[4], Nodo('PARENTESIS_DER', valor=p[5]), p[6]])
    else:
        p[0] = Nodo('inicio', hijo=[Nodo('ENTERO', valor=p[1]), Nodo('PRINCIPAL', valor=p[2]), Nodo('PARENTESIS_IZQ', valor=p[3]), Nodo('PARENTESIS_DER', valor=p[4]), p[5]])

# Bloques de código
def p_bloque(p):
    '''
    bloque : LLAVE_IZQ lista_instrucciones LLAVE_DER 
           | LLAVE_IZQ LLAVE_DER
    '''
    if len(p) == 4:
        p[0] = Nodo('bloque', hijo=[Nodo('LLAVE_IZQ', valor=p[1]), p[2], Nodo('LLAVE_DER', valor=p[3])])
    else:
        p[0] = Nodo('bloque', hijo=[Nodo('LLAVE_IZQ', valor=p[1]), Nodo('LLAVE_DER', valor=p[2])])

# Instrucciones
def p_lista_instrucciones(p):
    '''
    lista_instrucciones : instruccion lista_instrucciones
                        | instruccion
    '''
    if len(p) == 3:
        p[0] = Nodo('lista_instrucciones', hijo=[p[1], p[2]])
    else:
        p[0] = Nodo('lista_instrucciones', hijo=[p[1]])

def p_instruccion(p):
    '''
    instruccion : declaracion
                | sentencia
                | estructura_de_control
    '''
    p[0] = Nodo('instruccion', hijo=[p[1]])

# Declaraciones
def p_declaracion(p):
    '''
    declaracion : declaracion_variable PUNTO_Y_COMA
                | prototipo_funcion PUNTO_Y_COMA
                | definicion_funcion
    '''
    if len(p) == 3:
        p[0] = Nodo('declaracion', hijo=[p[1], Nodo('PUNTO_Y_COMA', valor=p[2])])
    else:
        p[0] = Nodo('declaracion', hijo=[p[1]])

# Declaraciones de variables
def p_declaracion_variable(p):
    '''
    declaracion_variable : tipo lista_identificadores
    '''
    p[0] = Nodo('declaracion_variable', hijo=[p[1], p[2]])

def p_lista_identificadores(p):
    '''
    lista_identificadores : IDENTIFICADOR
                          | IDENTIFICADOR ASIGNACION expresion
                          | IDENTIFICADOR COMA lista_identificadores
                          | IDENTIFICADOR ASIGNACION expresion COMA lista_identificadores 
    '''
    if len(p) == 2:
        p[0] = Nodo('lista_identificadores', hijo=[Nodo('IDENTIFICADOR', valor=p[1])])
    elif len(p) == 4:
        p[0] = Nodo('lista_identificadores', hijo=[Nodo('IDENTIFICADOR', valor=p[1]), Nodo(p.slice[2].type, valor=p[2]), p[3]])
    elif len(p) == 6:
        p[0] = Nodo('lista_identificadores', hijo=[Nodo('IDENTIFICADOR', valor=p[1]), Nodo('ASIGNACION', valor=p[2]), p[3], Nodo('COMA', valor=p[4]), p[5]])

# Prototipo de funciones generales
def p_prototipo_funcion(p):
    '''
    prototipo_funcion : tipo IDENTIFICADOR PARENTESIS_IZQ lista_parametros PARENTESIS_DER
                      | tipo IDENTIFICADOR PARENTESIS_IZQ PARENTESIS_DER
    '''
    if len(p) == 6:
        p[0] = Nodo('prototipo_funcion', hijo=[p[1], Nodo('IDENTIFICADOR', valor=p[2]), Nodo('PARENTESIS_IZQ', valor=p[3]), p[4], Nodo('PARENTESIS_DER', valor=p[5])])
    else:
        p[0] = Nodo('prototipo_funcion', hijo=[p[1], Nodo('IDENTIFICADOR', valor=p[2]), Nodo('PARENTESIS_IZQ', valor=p[3]), Nodo('PARENTESIS_DER', valor=p[4])])

# Declaración de funciones generales
def p_definicion_funcion(p):
    '''
    definicion_funcion : tipo IDENTIFICADOR PARENTESIS_IZQ lista_parametros PARENTESIS_DER bloque
                       | tipo IDENTIFICADOR PARENTESIS_IZQ PARENTESIS_DER bloque
    '''
    if len(p) == 7:
        p[0] = Nodo('definicion_funcion', hijo=[p[1], Nodo('IDENTIFICADOR', valor=p[2]), Nodo('PARENTESIS_IZQ', valor=p[3]), p[4], Nodo('PARENTESIS_DER', valor=p[5]), p[6]])
    elif len(p) == 6:
        p[0] = Nodo('definicion_funcion', hijo=[p[1], Nodo('IDENTIFICADOR', valor=p[2]), Nodo('PARENTESIS_IZQ', valor=p[3]), Nodo('PARENTESIS_DER', valor=p[4]), p[5]])

def p_lista_parametros(p):
    '''
    lista_parametros : parametro COMA lista_parametros
                     | parametro
                     | VACIO
    '''
    if len(p) == 4:
        p[0] = Nodo('lista_parametros', hijo=[p[1], Nodo('COMA', valor=p[2]), p[3]])
    else:
        if str(p[1]).__contains__('parametro'):
            p[0] = Nodo('lista_parametros', hijo=[p[1]])
        else:
            p[0] = Nodo('lista_parametros', hijo=[Nodo('VACIO', valor=p[1])])

def p_parametro(p):
    '''
    parametro : tipo IDENTIFICADOR
    '''
    p[0] = Nodo('parametro', hijo=[p[1], Nodo('IDENTIFICADOR', valor=p[2])])

# Sentencias
def p_sentencia(p):
    '''
    sentencia : asignacion PUNTO_Y_COMA
              | llamado_a_funcion PUNTO_Y_COMA
              | retorno PUNTO_Y_COMA
    '''
    p[0] = Nodo('sentencia', hijo=[p[1], Nodo('PUNTO_Y_COMA', valor=p[2])])

# Asignaciones
def p_asignacion(p):
    '''
    asignacion : IDENTIFICADOR ASIGNACION expresion
               | IDENTIFICADOR INCREMENTO
               | IDENTIFICADOR DECREMENTO
    '''
    if len(p) == 4:
        p[0] = Nodo('asignacion', hijo=[Nodo('IDENTIFICADOR', valor=p[1]), Nodo('ASIGNACION', valor=p[2]), p[3]])
    else:
        p[0] = Nodo('asignacion', hijo=[Nodo('IDENTIFICADOR', valor=p[1]), Nodo(p.slice[2].type, valor=p[2])])

# Condiciones
def p_condicion(p):
    '''
    condicion : expresion Y_LOGICO expresion
              | expresion O_LOGICO expresion
              | NEGACION expresion
              | expresion IGUAL_QUE expresion
              | expresion DIFERENTE_QUE expresion
              | expresion MENOR_QUE expresion
              | expresion MENOR_IGUAL_QUE expresion
              | expresion MAYOR_QUE expresion
              | expresion MAYOR_IGUAL_QUE expresion
    '''
    if len(p) == 4:
        p[0] = Nodo('condicion', hijo=[p[1], Nodo(p.slice[2].type, valor=p[2]), p[3]])
    else:
        p[0] = Nodo('condicion', hijo=[Nodo('NEGACION', valor=p[1]), p[2]])

# Tipos de datos
def p_tipo(p):
    '''
    tipo : ENTERO
         | VACIO
    '''
    p[0] = Nodo('tipo', hijo=[Nodo(p.slice[1].type, valor=p[1])])

# Expresiones y operaciones aritméticas
def p_expresion(p):
    '''
    expresion : expresion SUMA expresion
              | expresion RESTA expresion
              | expresion PRODUCTO expresion
              | expresion DIVISION expresion
              | expresion MODULO expresion
              | PARENTESIS_IZQ expresion PARENTESIS_DER
              | NUMERO
              | IDENTIFICADOR
              | llamado_a_funcion
    '''
    if len(p) == 4:
        if p[1] == '(':
            p[0] = Nodo('expresion', hijo=[Nodo('PARENTESIS_IZQ', valor=p[1]), p[2], Nodo('PARENTESIS_DER', valor=p[3])])
        else:
            p[0] = Nodo('expresion', hijo=[p[1], Nodo(p.slice[2].type, valor=p[2]), p[3]])
    else:
        if str(p[1]).__contains__('llamado_a_funcion'):
            p[0] = Nodo('expresion', hijo=[p[1]])
        else:
            p[0] = Nodo('expresion', hijo=[Nodo(p.slice[1].type, valor=p[1])])

# Llamados a funciones
def p_llamado_a_funcion(p):
    '''
    llamado_a_funcion : IDENTIFICADOR PARENTESIS_IZQ lista_argumentos PARENTESIS_DER
                      | ESCRIBIR PARENTESIS_IZQ lista_argumentos PARENTESIS_DER 
                      | IMPRIMIR PARENTESIS_IZQ lista_argumentos PARENTESIS_DER
    '''
    p[0] = Nodo('llamado_a_funcion', hijo=[Nodo(p.slice[1].type, valor=p[1]), Nodo('PARENTESIS_IZQ', valor=p[2]), p[3], Nodo('PARENTESIS_DER', valor=p[4])])

def p_lista_argumentos(p):
    '''
    lista_argumentos : argumento COMA lista_argumentos
                     | argumento
                     | VACIO
    '''
    if len(p) == 4:
        p[0] = Nodo('lista_argumentos', hijo=[p[1], Nodo('COMA', valor=p[2]), p[3]])
    else:
        if str(p[1]).__contains__('argumento'):
            p[0] = Nodo('lista_argumentos', hijo=[p[1]])
        else:
            p[0] = Nodo('lista_argumentos', hijo=[Nodo('VACIO', valor=p[1])])

def p_argumento(p):
    '''
    argumento : expresion
              | CADENA
              | referencia
    '''
    if str(p[1]).startswith('"'):
        p[0] = Nodo('argumento', hijo=[Nodo('CADENA', valor=p[1])])
    else:
        p[0] = Nodo('argumento', hijo=[p[1]])

def p_referencia(p):
    '''
    referencia : REFERENCIA IDENTIFICADOR    
    '''
    p[0] = Nodo('referencia', hijo=[Nodo('REFERENCIA', valor=p[1]), Nodo('IDENTIFICADOR', valor=p[2])])
    
# Retornos
def p_retorno(p):
    '''
    retorno : RETORNAR expresion
            | RETORNAR
    '''
    if len(p) == 3:
        p[0] = Nodo('retorno', hijo=[Nodo('RETORNAR', valor=p[1]), p[2]])
    else:
        p[0] = Nodo('retorno', hijo=[Nodo('RETORNAR', valor=p[1])])

# Estructuras de control
def p_estructura_de_control(p):
    '''
    estructura_de_control : seleccion
                          | iteracion
    '''
    p[0] = Nodo('estructura_de_control', hijo=[p[1]])

# Estructuras de control de selección
def p_seleccion(p):
    '''
    seleccion : SI PARENTESIS_IZQ condicion PARENTESIS_DER bloque
              | SI PARENTESIS_IZQ condicion PARENTESIS_DER bloque SI_NO bloque
              | SI PARENTESIS_IZQ condicion PARENTESIS_DER bloque SI_NO seleccion
    '''
    if len(p) == 6:
        p[0] = Nodo('seleccion', hijo=[Nodo('SI', valor=p[1]), Nodo('PARENTESIS_IZQ', valor=p[2]), p[3], Nodo('PARENTESIS_DER', valor=p[4]), p[5]])
    else:
        p[0] = Nodo('seleccion', hijo=[Nodo('SI', valor=p[1]), Nodo('PARENTESIS_IZQ', valor=p[2]), p[3], Nodo('PARENTESIS_DER', valor=p[4]), p[5], Nodo('SI_NO', valor=p[6]), p[7]])

# Estructuras de control de iteración
def p_iteracion(p):
    '''
    iteracion : MIENTRAS PARENTESIS_IZQ condicion PARENTESIS_DER bloque
              | PARA PARENTESIS_IZQ declaracion_variable PUNTO_Y_COMA condicion PUNTO_Y_COMA asignacion PARENTESIS_DER bloque
              | HACER bloque MIENTRAS PARENTESIS_IZQ condicion PARENTESIS_DER PUNTO_Y_COMA
    '''
    if len(p) == 6:
        p[0] = Nodo('iteracion', hijo=[Nodo('MIENTRAS', valor=p[1]), Nodo('PARENTESIS_IZQ', valor=p[2]), p[3], Nodo('PARENTESIS_DER', valor=p[4]), p[5]])
    elif len(p) == 10:
        p[0] = Nodo('iteracion', hijo=[Nodo('PARA', valor=p[1]), Nodo('PARENTESIS_IZQ', valor=p[2]), p[3], Nodo('PUNTO_Y_COMA', valor=p[4]), p[5], Nodo('PUNTO_Y_COMA', valor=p[6]), p[7], Nodo('PARENTESIS_DER', valor=p[8]), p[9]])
    else:
        p[0] = Nodo('iteracion', hijo=[Nodo('HACER', valor=p[1]), p[2], Nodo('MIENTRAS', valor=p[3]), Nodo('PARENTESIS_IZQ', valor=p[4]), p[5], Nodo('PARENTESIS_DER', valor=p[6]), Nodo('PUNTO_Y_COMA', valor=p[7])])

# Manejo de errores en la sintaxis
def p_error(p):
    if p:
        print(f"Error de sintaxis en la entrada. Token inesperado: {p.value} en la línea {p.lineno}")
        print(f"Contexto alrededor del error: {p.lexer.lexdata[p.lexpos-20:p.lexpos+20]}")  # Muestra el contexto del error
    else:
        print("Error de sintaxis en la entrada. Final inesperado.")

# Construcción del parser
parser = yacc.yacc(debug=True)

# Función para generar el árbol gramatical
def generar_arbol_gramatical(codigo):
    try:
        # Ejecutar el analizador léxico y sintáctico
        nodo_raiz = parser.parse(codigo) # Símbolo inicial de la grámatica
        # Guardar el árbol de descomposición gramatical en el archivo
        with open('arbol_gramatical.txt', 'w', encoding='utf-8') as archivo:
            if nodo_raiz:
                print("El árbol de descomposición gramatical es:\n", file=archivo)
                imprimir_nodo_arbol(nodo_raiz, archivo=archivo) 
                print("\nEl árbol de descomposición gramatical se generó correctamente.\n")
            else:
                print("La sintaxis no es correcta. El análisis sintáctico no tuvo éxito.")
    except Exception as e:
        print(f"Error durante el análisis sintáctico: {e}")
    
# Función para imprimir un nodo en el árbol gramatical
def imprimir_nodo_arbol(nodo, nivel=0, archivo=None):
    indentacion = '    ' * nivel
    if archivo is not None:
        print(indentacion + str(nodo), file=archivo)
    if hasattr(nodo, 'hijo'):
        for hijo in nodo.hijo:
            imprimir_nodo_arbol(hijo, nivel + 1, archivo)

# Código de prueba en C
codigo_a_analizar = '''
#include <stdio.h>
#include <math.h>

int main() {
    int n, a = 0, b = 1, siguiente;

    do {
        printf("Digite la cantidad de términos de la secuencia de Fibonacci: ");
        scanf("%d", &n);
        if (n <= 0) {
            printf("Por favor, ingresa un número mayor que 0.\n");
        }
    } while (n <= 0);  

    printf("Secuencia de Fibonacci: ");
    for (int i = 1; i <= n; i++) {
        printf("%d ", a);
        siguiente = a + b;
        a = b;
        b = siguiente;
    }
    
    return 0;
}
'''

# Generar el árbol gramatical a partir del código de prueba
generar_arbol_gramatical(codigo_a_analizar)


