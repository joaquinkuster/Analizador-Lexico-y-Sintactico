from ply import lex

# ------------------
# ANALIZADOR LÉXICO|
# ------------------
# El analizador léxico recibe el código fuente y lo descompone en tokens definidos (términos 
# significativos como palabras clave, reservadas, identificadores, operadores, etc.). 

# Definición de tokens
tokens = (
    # Palabras reservadas
    'PRINCIPAL', 'INCLUIR', 'BIBLIOTECA',
    
    # Estructuras de control y funciones
    'SI', 'SI_NO', 'MIENTRAS', 'PARA', 'HACER', 'RETORNAR',
    
    # Tipos de datos
    'ENTERO', 'VACIO',
    
    # Identificadores y valores
    'IDENTIFICADOR', 'NUMERO', 'CADENA',
    
    # Operadores aritméticos
    'SUMA', 'RESTA', 'PRODUCTO', 'DIVISION', 'MODULO',
    
    # Operadores de asignación y condicionales
    'ASIGNACION', 'IGUAL_QUE', 'DIFERENTE_QUE', 'MENOR_QUE', 'MENOR_IGUAL_QUE', 
    'MAYOR_QUE', 'MAYOR_IGUAL_QUE', 'Y_LOGICO', 'O_LOGICO', 'NEGACION',
    
    # Incremento y decremento
    'INCREMENTO', 'DECREMENTO',
    
    # Aperturas y cierres de estructuras de control y funciones
    'LLAVE_IZQ', 'LLAVE_DER', 'PARENTESIS_IZQ', 'PARENTESIS_DER',
    
    # Operadores de entrada/salida
    'ESCRIBIR', 'IMPRIMIR', 'REFERENCIA',
    
    # Puntuación
    'PUNTO_Y_COMA', 'COMA'
)

# Expresiones regulares para tokens simples
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

# Expresiones regulares para tokens más complejos
def t_NUMERO(t):
    r'\d+(\.\d+)?'
    return t

def t_CADENA(t):
    r'\"(\\.|[^\\"])*\"'
    return t

def t_BIBLIOTECA(t):
    r'<[a-zA-Z_][a-zA-Z0-9_]*\.h>'
    return t

def t_INCLUIR(t):
    r'\#include'
    return t

# Palabras reservadas
reservadas = {
    'main': 'PRINCIPAL',
    'if': 'SI', 'else': 'SI_NO', 'while': 'MIENTRAS', 'for': 'PARA', 'do': 'HACER',
    'return': 'RETORNAR', 
    'void': 'VACIO', 'int': 'ENTERO',
    'scanf': 'ESCRIBIR', 'printf': 'IMPRIMIR'
}

# Identificadores y palabras reservadas
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'IDENTIFICADOR')
    return t

# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal: '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

# Función para probar el analizador léxico
def test_analizador_lexico(codigo):
    try:
        lexer.input(codigo)
        print(f"\nEl resultado del análisis léxico es:\n")
        for token in lexer:
            print(f'Token: {token.type}, Valor: {token.value}, Línea: {token.lineno}')
    except Exception as e:
        print(f"Error durante el análisis léxico: {e}")
        
# Código de prueba en C
codigo_a_analizar = '''
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
test_analizador_lexico(codigo_a_analizar)