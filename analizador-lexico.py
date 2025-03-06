from ply import lex, yacc

# -------------------
# ANALIZADOR LÉXICO
# -------------------

# Definición de tokens
tokens = (
    'IDENTIFICADOR', 'NUMERO',
    'SUMA', 'RESTA', 'PRODUCTO', 'DIVISION', 'MODULO',
    'ASIGNACION', 'IGUALDAD', 'DIFERENTE', 'MENOR', 'MENOR_IGUAL',
    'MAYOR', 'MAYOR_IGUAL', 'Y_LOGICO', 'O_LOGICO', 'NEGACION',
    'PARENTESIS_IZQ', 'PARENTESIS_DER', 'LLAVE_IZQ', 'LLAVE_DER', 'CORCHETE_IZQ', 'CORCHETE_DER',
    'PUNTO_Y_COMA', 'COMA', 'PUNTO', 'DOS_PUNTOS',
    'INCREMENTO', 'DECREMENTO',
    'SUMA_ASIGNACION', 'RESTA_ASIGNACION', 'PRODUCTO_ASIGNACION', 'DIVISION_ASIGNACION',
    'SI', 'SI_NO', 'MIENTRAS', 'PARA', 'HACER', 'RETORNAR', 'SELECCIONAR', 'CASO',
    'INTERRUMPIR', 'CONTINUAR', 'POR_DEFECTO', 'IR_A', 'TIPO_DEF',
    'ESTRUCTURA', 'ENUMERACION', 'CONSTANTE', 'TAMANIO', 'ESTATICO',
    'CADENA', 'CARACTER', 'VACIO', 'ENTERO', 'FLOTANTE', 'DOBLE'
)

# Expresiones regulares para los tokens
t_NUMERO = r'\d+(\.\d+)?'
t_CADENA = r'\"(\\.|[^\\"])*\"'
t_CARACTER = r"\'([^\\]|\\.)\'"

t_SUMA = r'\+'
t_RESTA = r'-'
t_PRODUCTO = r'\*'

t_DIVISION = r'/'
t_MODULO = r'%'

t_ASIGNACION = r'='
t_IGUALDAD = r'=='
t_DIFERENTE = r'!='
t_MENOR = r'<'
t_MENOR_IGUAL = r'<='
t_MAYOR = r'>'
t_MAYOR_IGUAL = r'>='

t_Y_LOGICO = r'&&'
t_O_LOGICO = r'\|\|'
t_NEGACION = r'!'

t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'

t_PUNTO_Y_COMA = r';'
t_COMA = r','
t_PUNTO = r'\.'
t_DOS_PUNTOS = r':'

t_INCREMENTO = r'\+\+'
t_DECREMENTO = r'--'

t_SUMA_ASIGNACION = r'\+='
t_RESTA_ASIGNACION = r'-='
t_PRODUCTO_ASIGNACION = r'\*='
t_DIVISION_ASIGNACION = r'/='

# Palabras reservadas y su asignación a tokens
reservadas = {
    'if': 'SI', 'else': 'SI_NO', 'while': 'MIENTRAS', 'for': 'PARA', 'do': 'HACER',
    'return': 'RETORNAR', 'switch': 'SELECCIONAR', 'case': 'CASO', 'break': 'INTERRUMPIR',
    'continue': 'CONTINUAR', 'default': 'POR_DEFECTO', 'goto': 'IR_A', 'typedef': 'TIPO_DEF',
    'struct': 'ESTRUCTURA','enum': 'ENUMERACION', 'const': 'CONSTANTE',
    'sizeof': 'TAMANIO', 'static': 'ESTATICO', 'void': 'VACIO', 'int': 'ENTERO',
    'float': 'FLOTANTE', 'double': 'DOBLE',
}

# Funciones de manejo de tokens
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'IDENTIFICADOR')  # Si es una palabra reservada, se le asigna a una palabra en especial del Tokens
    return t

# Maneja los saltos de línea y actualiza el número de línea del lexer
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar caracteres de espacio en blanco
t_ignore = ' \t'

# Manejo de errores de tokens
def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

def test_lexer(code):
    lexer.input(code)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"Token({tok.type}, '{tok.value}', {tok.lineno}, {tok.lexpos})")

# Código de prueba en C
test_code = '''
int main() {
    int a = 10;
    float b = 5.5;
    char c = 'x';
    if (a > b) {
        a += 1;    }
    return 0;
}
'''

# Ejecutar el lexer con el código de prueba
test_lexer(test_code)