# Importar yacc
from ply import yacc

# -------------------
# ANALIZADOR SINTÁCTICO
# -------------------

# Reglas de producción

# Declarativas
def p_declarativa(p):
    '''
    declarativa : inclusion
    '''
    pass

# Inclusion de biblioteca
def p_inclusion(p):
    '''
    inclusion : INCLUIR BIBLIOTECA
    '''
    pass

# Instrucciones 
def p_lista_instrucciones(p):
    '''
    lista_instrucciones : instruccion lista_instrucciones
                        | instruccion
    '''
    pass

def p_instruccion(p):
    '''
    instruccion : declaracion
                | sentencia
    '''
    pass

# Declaraciones
def p_declaracion(p):
    '''
    declaracion : declaracion_variable PUNTO_Y_COMA
                | definicion_funcion
    '''
    pass

# Declaraciones de variables
def p_declaracion_variable(p):
    '''
    declaracion_variable : tipo lista_identificadores
    '''
    pass

def p_lista_identificadores(p):
    '''
    lista_identificadores : IDENTIFICADOR
                          | IDENTIFICADOR ASIGNACION expresion
                          | lista_identificadores COMA IDENTIFICADOR
                          | lista_identificadores COMA IDENTIFICADOR ASIGNACION expresion
    '''
    pass

# Declaracion y prototipos de funciones generales
def p_definicion_funcion(p):
    '''
    definicion_funcion : tipo IDENTIFICADOR PARENTESIS_IZQ lista_parametros PARENTESIS_DER bloque
                       | tipo IDENTIFICADOR PARENTESIS_IZQ PARENTESIS_DER bloque
                       | tipo IDENTIFICADOR PARENTESIS_IZQ lista_parametros PARENTESIS_DER PUNTO_Y_COMA
    '''
    pass

# Declaración de la función principal
def p_definicion_funcion_main(p):
    '''
    definicion_funcion : ENTERO PRINCIPAL PARENTESIS_IZQ lista_parametros PARENTESIS_DER bloque
                       | ENTERO PRINCIPAL PARENTESIS_IZQ PARENTESIS_DER bloque
    '''
    pass

def p_lista_parametros(p):
    '''
    lista_parametros : lista_parametros COMA parametro
                     | parametro
                     | VACIO
    '''
    pass

def p_parametro(p):
    '''
    parametro : tipo IDENTIFICADOR
    '''
    pass

# Bloque de código (puede ser un procedimiento, por lo que puede retornar o no)
def p_bloque(p):
    '''
    bloque : LLAVE_IZQ lista_instrucciones retorno LLAVE_DER 
           | LLAVE_IZQ lista_instrucciones LLAVE_DER
           | LLAVE_IZQ retorno LLAVE_DER
           | LLAVE_IZQ LLAVE_DER
    '''
    pass

# Sentencias
def p_sentencia(p):
    '''
    sentencia : asignacion PUNTO_Y_COMA
              | seleccion 
              | iteracion
              | funcion PUNTO_Y_COMA
              | retorno PUNTO_Y_COMA
    '''
    pass

# Asignaciones
def p_asignacion(p):
    '''
    asignacion : IDENTIFICADOR ASIGNACION expresion
               | IDENTIFICADOR INCREMENTO
               | IDENTIFICADOR DECREMENTO
    '''
    pass

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
    pass

# Tipos de datos
def p_tipo(p):
    '''
    tipo : ENTERO
         | VACIO
    '''
    pass

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
              | funcion
    '''
    pass
    
# Funciones
def p_funcion(p):
    '''
    funcion : IDENTIFICADOR PARENTESIS_IZQ lista_argumentos PARENTESIS_DER
            | ESCRIBIR PARENTESIS_IZQ lista_argumentos PARENTESIS_DER 
            | IMPRIMIR PARENTESIS_IZQ lista_argumentos PARENTESIS_DER
    '''
    pass

def p_lista_argumentos(p):
    '''
    lista_argumentos : lista_argumentos COMA argumento
                     | argumento
                     | VACIO
    '''
    pass

def p_argumento(p):
    '''
    argumento : expresion
              | CADENA
              | referencia
    '''
    pass

def p_referencia(p):
    '''
    referencia : REFERENCIA IDENTIFICADOR    
    '''
    pass

# Estructuras de control
def p_seleccion(p):
    '''
    seleccion : SI PARENTESIS_IZQ condicion PARENTESIS_DER bloque
              | SI PARENTESIS_IZQ condicion PARENTESIS_DER bloque SI_NO bloque
              | SI PARENTESIS_IZQ condicion PARENTESIS_DER bloque SI_NO seleccion
    '''
    pass

# Bucles
def p_iteracion(p):
    '''
    iteracion : MIENTRAS PARENTESIS_IZQ condicion PARENTESIS_DER bloque
              | PARA PARENTESIS_IZQ asignacion PUNTO_Y_COMA condicion PUNTO_Y_COMA asignacion PARENTESIS_DER bloque
              | HACER bloque MIENTRAS PARENTESIS_IZQ condicion PARENTESIS_DER PUNTO_Y_COMA
    '''
    pass

# Retornos
def p_retorno(p):
    '''
    retorno : RETORNAR expresion
            | RETORNAR
    '''
    pass

# Manejo de errores en la sintaxis
def p_error(p):
    print(f"Error de sintaxis en '{p.value}'" if p else "Error de sintaxis")

# Construcción del parser
parser = yacc.yacc()
