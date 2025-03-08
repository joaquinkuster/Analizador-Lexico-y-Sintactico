# Importar yacc
from ply import yacc
from lexer import tokens

# -------------------
# ANALIZADOR SINTÁCTICO
# -------------------

# Precedencias para los operadores
precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'PRODUCTO', 'DIVISION', 'MODULO'),
)

# Reglas de producción

def p_programa(p):
    '''
    programa : lista_declarativas inicio
             | inicio
    '''
    if len(p) == 3:
        p[0] = f"programa → {p[1]}\n{p[2]}"
    else:
        p[0] = f"programa → {p[1]}"

# Declarativas
def p_lista_declarativas(p):
    '''
    lista_declarativas : declarativa lista_declarativas
                       | declarativa
    '''
    if len(p) == 3:
        p[0] = f"lista_declarativas → {p[1]} {p[2]}"
    else:
        p[0] = f"lista_declarativas → {p[1]}"

def p_declarativa(p):
    '''
    declarativa : inclusion
    '''
    p[0] = f"declarativa → {p[1]}"

# Inclusion de biblioteca
def p_inclusion(p):
    '''
    inclusion : INCLUIR BIBLIOTECA
    '''
    p[0] = f"inclusion → {p[1]} {p[2]}"

# Función principal
def p_inicio(p):
    '''
    inicio : ENTERO PRINCIPAL PARENTESIS_IZQ lista_parametros PARENTESIS_DER bloque
           | ENTERO PRINCIPAL PARENTESIS_IZQ PARENTESIS_DER bloque
    '''
    if len(p) == 7:
        p[0] = f"inicio → {p[1]} {p[2]} ( {p[4]} ) {p[6]}"
    else:
        p[0] = f"inicio → {p[1]} {p[2]} ( ) {p[5]}"

# Bloque de código
def p_bloque(p):
    '''
    bloque : LLAVE_IZQ lista_instrucciones retorno LLAVE_DER 
           | LLAVE_IZQ lista_instrucciones LLAVE_DER
           | LLAVE_IZQ retorno LLAVE_DER
           | LLAVE_IZQ LLAVE_DER
    '''
    if len(p) == 5:
        p[0] = f"bloque → {{ {p[2]} {p[3]} }}"
    elif len(p) == 4:
        p[0] = f"bloque → {{ {p[2]} }}"
    else:
        p[0] = "bloque → { }"

# Instrucciones
def p_lista_instrucciones(p):
    '''
    lista_instrucciones : instruccion lista_instrucciones
                        | instruccion
    '''
    if len(p) == 3:
        p[0] = f"lista_instrucciones → {p[1]}\n{p[2]}"
    else:
        p[0] = f"lista_instrucciones → {p[1]}"

def p_instruccion(p):
    '''
    instruccion : declaracion
                | sentencia
                | estructura_de_control
    '''
    p[0] = f"instruccion → {p[1]}"

# Declaraciones
def p_declaracion(p):
    '''
    declaracion : declaracion_variable PUNTO_Y_COMA
                | prototipo_funcion PUNTO_Y_COMA
                | definicion_funcion
    '''
    if len(p) == 3:
        p[0] = f"declaracion → {p[1]} ;"
    else:
        p[0] = f"declaracion → {p[1]}"

# Declaraciones de variables
def p_declaracion_variable(p):
    '''
    declaracion_variable : tipo lista_identificadores
    '''
    p[0] = f"declaracion_variable → {p[1]} {p[2]}"

def p_lista_identificadores(p):
    '''
    lista_identificadores : IDENTIFICADOR
                          | IDENTIFICADOR ASIGNACION expresion
                          | IDENTIFICADOR COMA lista_identificadores
                          | IDENTIFICADOR ASIGNACION expresion COMA lista_identificadores 
    '''
    if len(p) == 2:
        p[0] = f"lista_identificadores → {p[1]}"
    elif len(p) == 4:
        p[0] = f"lista_identificadores → {p[1]} {p[2]} {p[3]}"
    elif len(p) == 6:
        p[0] = f"lista_identificadores → {p[1]} = {p[3]} , {p[5]}"

# Prototipo de funciones generales
def p_prototipo_funcion(p):
    '''
    prototipo_funcion : tipo IDENTIFICADOR PARENTESIS_IZQ lista_parametros PARENTESIS_DER
    '''
    p[0] = f"prototipo_funcion → {p[1]} {p[2]} ( {p[4]} )"

# Declaración de funciones generales
def p_definicion_funcion(p):
    '''
    definicion_funcion : tipo IDENTIFICADOR PARENTESIS_IZQ lista_parametros PARENTESIS_DER bloque
                       | tipo IDENTIFICADOR PARENTESIS_IZQ PARENTESIS_DER bloque
    '''
    if len(p) == 7:
        p[0] = f"definicion_funcion → {p[1]} {p[2]} ( {p[4]} ) {p[6]}"
    elif len(p) == 6:
        p[0] = f"definicion_funcion → {p[1]} {p[2]} ( ) {p[5]}"

def p_lista_parametros(p):
    '''
    lista_parametros : lista_parametros COMA parametro
                     | parametro
                     | VACIO
    '''
    if len(p) == 4:
        p[0] = f"lista_parametros → {p[1]} , {p[3]}"
    else:
        p[0] = f"lista_parametros → {p[1]}"

def p_parametro(p):
    '''
    parametro : tipo IDENTIFICADOR
    '''
    p[0] = f"parametro → {p[1]} {p[2]}"

# Sentencias
def p_sentencia(p):
    '''
    sentencia : asignacion PUNTO_Y_COMA
              | llamado_a_funcion PUNTO_Y_COMA
              | retorno PUNTO_Y_COMA
    '''
    p[0] = f"sentencia → {p[1]} ;"

# Asignaciones
def p_asignacion(p):
    '''
    asignacion : IDENTIFICADOR ASIGNACION expresion
               | IDENTIFICADOR INCREMENTO
               | IDENTIFICADOR DECREMENTO
    '''
    if len(p) == 4:
        p[0] = f"asignacion → {p[1]} = {p[3]}"
    else:
        p[0] = f"asignacion → {p[1]} {p[2]}"

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
        p[0] = f"condicion → {p[1]} {p[2]} {p[3]}"
    else:
        p[0] = f"condicion → {p[1]} {p[2]}"

# Tipos de datos
def p_tipo(p):
    '''
    tipo : ENTERO
         | VACIO
    '''
    p[0] = f"tipo → {p[1]}"

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
            p[0] = f"expresion → ( {p[2]} )"
        else:
            p[0] = f"expresion → {p[1]} {p[2]} {p[3]}"
    else:
        p[0] = f"expresion → {p[1]}"

# Llamados a funciones
def p_llamado_a_funcion(p):
    '''
    llamado_a_funcion : IDENTIFICADOR PARENTESIS_IZQ lista_argumentos PARENTESIS_DER
                      | ESCRIBIR PARENTESIS_IZQ lista_argumentos PARENTESIS_DER 
                      | IMPRIMIR PARENTESIS_IZQ lista_argumentos PARENTESIS_DER
    '''
    p[0] = f"llamado_a_funcion → {p[1]} ( {p[3]} )"

def p_lista_argumentos(p):
    '''
    lista_argumentos : lista_argumentos COMA argumento
                     | argumento
                     | VACIO
    '''
    if len(p) == 4:
        p[0] = f"lista_argumentos → {p[1]} , {p[3]}"
    else:
        p[0] = f"lista_argumentos → {p[1]}"

def p_argumento(p):
    '''
    argumento : expresion
              | CADENA
              | referencia
    '''
    p[0] = f"argumento → {p[1]}"

def p_referencia(p):
    '''
    referencia : REFERENCIA IDENTIFICADOR    
    '''
    p[0] = f"referencia → & {p[2]}"
    
# Retornos
def p_retorno(p):
    '''
    retorno : RETORNAR expresion
            | RETORNAR
    '''
    if len(p) == 3:
        p[0] = f"retorno → {p[1]} {p[2]}"
    else:
        p[0] = f"retorno → {p[1]}"

# Estructuras de control
def p_estructura_de_control(p):
    '''
    estructura_de_control : seleccion
                          | iteracion
    '''
    p[0] = f"estructura_de_control → {p[1]}"

# Estructuras de control de selección
def p_seleccion(p):
    '''
    seleccion : SI PARENTESIS_IZQ condicion PARENTESIS_DER bloque
              | SI PARENTESIS_IZQ condicion PARENTESIS_DER bloque SI_NO bloque
              | SI PARENTESIS_IZQ condicion PARENTESIS_DER bloque SI_NO seleccion
    '''
    if len(p) == 6:
        p[0] = f"seleccion → if ( {p[3]} ) {p[5]}"
    else:
        p[0] = f"seleccion → if ( {p[3]} ) {p[5]} else {p[7]}"

# Estructuras de control de iteración
def p_iteracion(p):
    '''
    iteracion : MIENTRAS PARENTESIS_IZQ condicion PARENTESIS_DER bloque
              | PARA PARENTESIS_IZQ declaracion_variable PUNTO_Y_COMA condicion PUNTO_Y_COMA asignacion PARENTESIS_DER bloque
              | HACER bloque MIENTRAS PARENTESIS_IZQ condicion PARENTESIS_DER PUNTO_Y_COMA
    '''
    if len(p) == 6:
        p[0] = f"iteracion → while ( {p[3]} ) {p[5]}"
    elif len(p) == 10:
        p[0] = f"iteracion → for ( {p[3]} ; {p[5]} ; {p[7]} ) {p[9]}"
    else:
        p[0] = f"iteracion → do {p[2]} while ( {p[5]} ) ;"

# Manejo de errores en la sintaxis
def p_error(p):
    if p:
        print(f"Error de sintaxis en la entrada. Token inesperado: {p.value} en la línea {p.lineno}")
        print(f"Contexto: {p.lexer.lexdata[p.lexpos-20:p.lexpos+20]}")  # Muestra el contexto del error
    else:
        print("Error de sintaxis en la entrada. Final inesperado.")

# Construcción del parser
parser = yacc.yacc(debug=True)

# Código de prueba en C
codigo_prueba = '''
#include <stdio.h>

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

# Analizar la cadena de entrada
result = parser.parse(codigo_prueba)

# Imprimir el resultado del análisis sintactico
if result:
    print("\n\n") 
    print("El resultado del análisis es: \n\n" + result)
else:
    print("El análisis no tuvo éxito.")