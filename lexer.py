from ply import lex

# -------------------
# ANALIZADOR LÉXICO
# -------------------

# Definición de tokens

tokens = (
    # Palabras reservadas
    'PRINCIPAL', 'INCLUIR', 'BIBLIOTECA',
    
    # Estructuras de control y funciones
    'SI', # if
    'SI_NO', # else
    'MIENTRAS', # while
    'PARA', # for
    'HACER', # do
    'RETORNAR', # return
    
    # Tipos de datos
    'ENTERO', # int
    'VACIO', # void
    
    # Nombres de las variables
    'IDENTIFICADOR', 
    
    # Valores
    'NUMERO', 'CADENA',
    
    # Operadores aritméticos
    'SUMA', # +
    'RESTA', # -
    'PRODUCTO', # *
    'DIVISION', # /
    'MODULO', # %
    
    # Operadores de asignación y condicionales
    'ASIGNACION', # =
    'IGUAL_QUE', # ==
    'DIFERENTE_QUE', # !=
    'MENOR_QUE', # <
    'MENOR_IGUAL_QUE', # <=
    'MAYOR_QUE', # >
    'MAYOR_IGUAL_QUE', # >=
    'Y_LOGICO', # &&
    'O_LOGICO', # ||
    'NEGACION', # !
    
    # Incremento y decremento
    'INCREMENTO', # ++
    'DECREMENTO', # --
    
    # Aperturas y cierres de estructuras de control y funciones
    'LLAVE_IZQ', # {
    'LLAVE_DER', # }
    'PARENTESIS_IZQ', # ( 
    'PARENTESIS_DER', # ) 
    
    # Operadores de entrada/salida
    'ESCRIBIR', # funcion printf del stdio.h
    'IMPRIMIR', # funcion scanf del stdio.h 
    'REFERENCIA', # simbolo & para obtener la direccion de memoria de una variable 
    
    # Puntuación
    'PUNTO_Y_COMA', # ;
    'COMA' # ,
)


# Expresiones regulares para los tokens
t_NUMERO = r'\d+(\.\d+)?'
t_CADENA = r'\"(\\.|[^\\"])*\"'

t_BIBLIOTECA = r'(<stdio.h>)'
t_INCLUIR = r'(\#include)'

t_SUMA = r'\+'
t_RESTA = r'-'
t_PRODUCTO = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'

t_ASIGNACION = r'='
t_IGUAL_QUE = r'=='
t_DIFERENTE_QUE = r'!='
t_MENOR_QUE = r'<'
t_MENOR_IGUAL_QUE = r'<='
t_MAYOR_QUE = r'>'
t_MAYOR_IGUAL_QUE = r'>='
t_Y_LOGICO = r'&&'
t_O_LOGICO = r'\|\|'
t_NEGACION = r'!'

t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'

t_PUNTO_Y_COMA = r';'
t_COMA = r','

t_INCREMENTO = r'\+\+'
t_DECREMENTO = r'--'

t_REFERENCIA = r'&'


# Palabras reservadas y su asignación a tokens
reservadas = {    
    # Palabras reservadas
    'main': 'PRINCIPAL',
              
    # Estructuras de control
    'if': 'SI', 'else': 'SI_NO', 'while': 'MIENTRAS', 'for': 'PARA', 'do': 'HACER',
    
    # Funciones de retorno
    'return': 'RETORNAR', 
    
    # Tipos de datos
    'void': 'VACIO', 'int': 'ENTERO',
    
    # Funciones de entrada y salida
    'scanf': 'ESCRIBIR', 'printf': 'IMPRIMIR'
}

# Funcion de manejo para cualquier palabra reservada que no cumpla ningun regex
# Podria ser el nombre de una variable o palabra reservada
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'IDENTIFICADOR')  # Si es una palabra reservada, se le asigna a una palabra en especial del Tokens
    return t

def t_ENTERO(t):
    r'int'
    return t

# Maneja los saltos de línea y actualiza el número de línea del lexer
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar las tabulaciones
t_ignore = ' \t'

# Manejo de errores de tokens
def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

def test_analizador_lexico(codigo):
    lexer.input(codigo)
    # Iterar sobre los tokens encontrados para imprimir el analisis lexico
    for token in lexer:
        print(f'Token: {token.type}, Valor: {token.value}, Línea: {token.lineno}')

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

# Ejecutar el lexer con el código de prueba
test_analizador_lexico(codigo_prueba)