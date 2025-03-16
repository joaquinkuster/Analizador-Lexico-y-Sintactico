# Analizador Léxico y Sintáctico con PLY (Python LEX-YACC)

## Integrantes

- **Joaquín Kuster** (joaquinkuster3000@gmail.com)

---

## Descripción

Este proyecto consiste en la implementación de un **analizador léxico y sintáctico** para un subconjunto del lenguaje de programación **C**, utilizando la herramienta **PLY** (Python Lex-Yacc). El objetivo es analizar un código en C, identificar sus componentes léxicos (tokens) y validar su estructura sintáctica según una gramática definida.

---

## Código en C a analizar

```c
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
```

---

## Tokens

A continuación se listan los tokens que el analizador léxico debe reconocer, junto con una breve descripción de cada uno:

| **Token**            | **Descripción**                                      |
|--------------------|------------------------------------------------|
| **PRINCIPAL**         | Palabra reservada que indica la función principal del programa (`main`). |
| **INCLUIR**           | Directiva de preprocesador para incluir bibliotecas (`#include`). |
| **BIBLIOTECA**        | Nombre de la biblioteca incluida (ej. `<stdio.h>`). |
| **SI**                | Palabra reservada para la estructura condicional `if`. |
| **SI_NO**             | Palabra reservada para el bloque `else` en una estructura condicional. |
| **MIENTRAS**          | Palabra reservada para el bucle `while`. |
| **PARA**              | Palabra reservada para el bucle `for`. |
| **HACER**             | Palabra reservada para el bucle `do-while`. |
| **RETORNAR**          | Palabra reservada para devolver un valor en una función (`return`). |
| **ENTERO**            | Tipo de dato para números enteros (`int`). |
| **VACIO**             | Tipo de dato que indica la ausencia de valor (`void`). |
| **IDENTIFICADOR**     | Nombre de una variable, función o otro identificador. |
| **NUMERO**            | Valor numérico entero o decimal. |
| **CADENA**            | Cadena de texto entre comillas dobles (`"texto"`). |
| **SUMA**              | Operador aritmético de suma (`+`). |
| **RESTA**             | Operador aritmético de resta (`-`). |
| **PRODUCTO**          | Operador aritmético de multiplicación (`*`). |
| **DIVISION**          | Operador aritmético de división (`/`). |
| **MODULO**            | Operador aritmético de módulo (`%`). |
| **ASIGNACION**        | Operador de asignación (`=`). |
| **IGUAL_QUE**         | Operador de comparación de igualdad (`==`). |
| **DIFERENTE_QUE**     | Operador de comparación de desigualdad (`!=`). |
| **MENOR_QUE**         | Operador de comparación "menor que" (`<`). |
| **MENOR_IGUAL_QUE**   | Operador de comparación "menor o igual que" (`<=`). |
| **MAYOR_QUE**         | Operador de comparación "mayor que" (`>`). |
| **MAYOR_IGUAL_QUE**   | Operador de comparación "mayor o igual que" (`>=`). |
| **Y_LOGICO**          | Operador lógico "AND" (`&&`). |
| **O_LOGICO**          | Operador lógico "OR" (`||`). |
| **NEGACION**          | Operador lógico de negación (`!`). |
| **INCREMENTO**        | Operador de incremento (`++`). |
| **DECREMENTO**        | Operador de decremento (`--`). |
| **LLAVE_IZQ**         | Símbolo de apertura de bloque (`{`). |
| **LLAVE_DER**         | Símbolo de cierre de bloque (`}`). |
| **PARENTESIS_IZQ**    | Símbolo de apertura de paréntesis (`(`). |
| **PARENTESIS_DER**    | Símbolo de cierre de paréntesis (`)`). |
| **ESCRIBIR**          | Función para leer entrada del usuario (`scanf`). |
| **IMPRIMIR**          | Función para imprimir en consola (`printf`). |
| **REFERENCIA**        | Operador de referencia (`&`). |
| **PUNTO_Y_COMA**      | Símbolo que indica el fin de una instrucción (`;`). |
| **COMA**              | Símbolo para separar elementos en una lista (`,`). |

---

## Expresiones regulares para los tokens

Esta sección define las expresiones regulares utilizadas para reconocer cada uno de los tokens en el análisis léxico. Cada token tiene una expresión regular que permite identificarlo en el código fuente.

| **Token**         | **Expresión regular**         |
|-------------------|-------------------------------|
| **PRINCIPAL**     | `r'main'`                     |
| **INCLUIR**       | `r'\#include'`                |
| **BIBLIOTECA**    | `r'<[a-zA-Z_][a-zA-Z0-9_]*\.h>'` |
| **SI**            | `r'if'`                       |
| **SI_NO**         | `r'else'`                     |
| **MIENTRAS**      | `r'while'`                    |
| **PARA**          | `r'for'`                      |
| **HACER**         | `r'do'`                       |
| **RETORNAR**      | `r'return'`                   |
| **ENTERO**        | `r'int'`                      |
| **VACIO**         | `r'void'`                     |
| **IDENTIFICADOR** | `r'[a-zA-Z_][a-zA-Z_0-9]*'`   |
| **NUMERO**        | `r'\d+(\.\d+)?'`              |
| **CADENA**        | `r'\"(\\.|[^\\"])*\"'`        |
| **SUMA**          | `r'\+'`                       |
| **RESTA**         | `r'-'`                        |
| **PRODUCTO**      | `r'\*'`                       |
| **DIVISION**      | `r'/'`                        |
| **MODULO**        | `r'%'`                        |
| **ASIGNACION**    | `r'='`                        |
| **IGUAL_QUE**     | `r'=='`                       |
| **DIFERENTE_QUE** | `r'!='`                       |
| **MENOR_QUE**     | `r'<'`                        |
| **MENOR_IGUAL_QUE** | `r'<='`                     |
| **MAYOR_QUE**     | `r'>'`                        |
| **MAYOR_IGUAL_QUE** | `r'>='`                     |
| **Y_LOGICO**      | `r'&&'`                       |
| **O_LOGICO**      | `r'\|\|'`                     |
| **NEGACION**      | `r'!'`                        |
| **INCREMENTO**    | `r'\+\+'`                     |
| **DECREMENTO**    | `r'--'`                       |
| **LLAVE_IZQ**     | `r'\{'`                       |
| **LLAVE_DER**     | `r'\}'`                       |
| **PARENTESIS_IZQ** | `r'\('`                      |
| **PARENTESIS_DER** | `r'\)'`                      |
| **PUNTO_Y_COMA**  | `r';'`                        |
| **COMA**          | `r','`                        |
| **ESCRIBIR**      | `r'scanf'`                    |
| **IMPRIMIR**      | `r'printf'`                   |
| **REFERENCIA**    | `r'&'`                        |

---

## Gramática 

La gramática define la estructura sintáctica del lenguaje. A continuación se presenta una tabla con las reglas gramaticales utilizadas en el analizador sintáctico:

| Regla                     | Definición                                                                       |
|---------------------------|----------------------------------------------------------------------------------|
| **Programa**              | `programa → lista_declarativas inicio` \| `programa → inicio`                   |
| **Lista de Declarativas** | `lista_declarativas → declarativa lista_declarativas` \| `lista_declarativas → ε`|
| **Declarativa**           | `declarativa → inclusion` \| `declarativa → declaracion_variable`               |
| **Inclusión**             | `inclusion → INCLUIR BIBLIOTECA`                                               |
| **Inicio**                | `inicio → ENTERO PRINCIPAL PARENTESIS_IZQ lista_parametros PARENTESIS_DER bloque` \| `inicio → ENTERO PRINCIPAL PARENTESIS_IZQ PARENTESIS_DER bloque` |
| **Bloque**                | `bloque → LLAVE_IZQ lista_instrucciones LLAVE_DER` \| `bloque → LLAVE_IZQ LLAVE_DER` |
| **Lista de Instrucciones**| `lista_instrucciones → instruccion lista_instrucciones` \| `lista_instrucciones → ε` |
| **Instrucción**           | `instruccion → declaracion` \| `instruccion → sentencia` \| `instruccion → estructura_de_control` |
| **Declaración**           | `declaracion → declaracion_variable PUNTO_Y_COMA` \| `declaracion → prototipo_funcion PUNTO_Y_COMA` \| `declaracion → definicion_funcion` |
| **Declaración de Variable**| `declaracion_variable → tipo lista_identificadores`                            |
| **Lista de Identificadores**| `lista_identificadores → IDENTIFICADOR` \| `lista_identificadores → IDENTIFICADOR ASIGNACION expresion` \| `lista_identificadores → IDENTIFICADOR COMA lista_identificadores` |
| **Prototipo de Función**  | `prototipo_funcion → tipo IDENTIFICADOR PARENTESIS_IZQ lista_parametros PARENTESIS_DER` \| `prototipo_funcion → tipo IDENTIFICADOR PARENTESIS_IZQ PARENTESIS_DER` |
| **Definición de Función** | `definicion_funcion → tipo IDENTIFICADOR PARENTESIS_IZQ lista_parametros PARENTESIS_DER bloque` \| `definicion_funcion → tipo IDENTIFICADOR PARENTESIS_IZQ PARENTESIS_DER bloque` |
| **Lista de Parámetros**   | `lista_parametros → parametro COMA lista_parametros` \| `lista_parametros → parametro` \| `lista_parametros → ε` |
| **Parámetro**             | `parametro → tipo IDENTIFICADOR`                                               |
| **Sentencia**             | `sentencia → asignacion PUNTO_Y_COMA` \| `sentencia → llamado_a_funcion PUNTO_Y_COMA` \| `sentencia → retorno PUNTO_Y_COMA` |
| **Asignación**            | `asignacion → IDENTIFICADOR ASIGNACION expresion` \| `asignacion → IDENTIFICADOR INCREMENTO` \| `asignacion → IDENTIFICADOR DECREMENTO` |
| **Condición**             | `condicion → expresion Y_LOGICO expresion` \| `condicion → expresion O_LOGICO expresion` \| `condicion → NEGACION expresion` \| `condicion → expresion IGUAL_QUE expresion` |
| **Tipo**                  | `tipo → ENTERO` \| `tipo → VACIO`                                              |
| **Expresión**             | `expresion → expresion SUMA expresion` \| `expresion → expresion RESTA expresion` \| `expresion → expresion PRODUCTO expresion` \| `expresion → expresion DIVISION expresion` \| `expresion → expresion MODULO expresion` \| `expresion → PARENTESIS_IZQ expresion PARENTESIS_DER` \| `expresion → NUMERO` \| `expresion → IDENTIFICADOR` \| `expresion → llamado_a_funcion` |
| **Llamado a Función**     | `llamado_a_funcion → IDENTIFICADOR PARENTESIS_IZQ lista_argumentos PARENTESIS_DER` \| `llamado_a_funcion → ESCRIBIR PARENTESIS_IZQ lista_argumentos PARENTESIS_DER` \| `llamado_a_funcion → IMPRIMIR PARENTESIS_IZQ lista_argumentos PARENTESIS_DER` |
| **Lista de Argumentos**   | `lista_argumentos → argumento COMA lista_argumentos` \| `lista_argumentos → argumento` \| `lista_argumentos → ε` |
| **Argumento**             | `argumento → expresion` \| `argumento → CADENA` \| `argumento → referencia`    |
| **Referencia**            | `referencia → REFERENCIA IDENTIFICADOR`                                         |
| **Retorno**               | `retorno → RETORNAR expresion` \| `retorno → RETORNAR`                         |
| **Estructura de Control** | `estructura_de_control → seleccion` \| `estructura_de_control → iteracion`     |
| **Selección**             | `seleccion → SI PARENTESIS_IZQ condicion PARENTESIS_DER bloque` \| `seleccion → SI PARENTESIS_IZQ condicion PARENTESIS_DER bloque SI_NO bloque` \| `seleccion → SI PARENTESIS_IZQ condicion PARENTESIS_DER bloque SI_NO seleccion` |
| **Iteración**             | `iteracion → MIENTRAS PARENTESIS_IZQ condicion PARENTESIS_DER bloque` \| `iteracion → PARA PARENTESIS_IZQ declaracion_variable PUNTO_Y_COMA condicion PUNTO_Y_COMA asignacion PARENTESIS_DER bloque` \| `iteracion → HACER bloque MIENTRAS PARENTESIS_IZQ condicion PARENTESIS_DER PUNTO_Y_COMA` |

---

## Ejemplo de Árbol Gramatical

El símbolo inicial `S'` representa la regla **programa**, compuesta por **directivas** y la regla **inicio**, que contiene una lista de instrucciones como **declaraciones**, **secuencias** y **estructuras de control**. Al final de `main`, debe haber una instrucción de retorno.

Diferencias entre tipos de instrucciones:

- **Directivas**: Instrucciones del preprocesador ejecutadas antes de la compilación. Ejemplo: `#include <stdio.h>`
- **Declaraciones**: Reservan memoria y definen identificadores, sin ejecutar acciones directas. Ejemplo: `int numero;`
- **Secuencias**: Ejecutan acciones directas usando valores almacenados. Ejemplo: `numero = 10; printf("%d", numero);`
- **Estructuras de Control**: Modifican el flujo del código mediante decisiones e iteraciones. Ejemplo: los condicionales if o los bucles.

```plaintext
programa
    lista_declarativas
        declarativa
            inclusion
                #include <stdio.h>
        lista_declarativas
            declarativa
                inclusion
                    #include <math.h>
    inicio
        ENTERO: int
        PRINCIPAL: main
        PARENTESIS_IZQ: (
        PARENTESIS_DER: )
        bloque
            LLAVE_IZQ: {
            lista_instrucciones
                instruccion
                    declaracion
                        declaracion_variable
                            tipo: ENTERO
                            lista_identificadores
                                IDENTIFICADOR: n
                                COMA: ,
                                lista_identificadores
                                    IDENTIFICADOR: a
                                    ASIGNACION: =
                                    expresion: 0
                                    COMA: ,
                                    lista_identificadores
                                        IDENTIFICADOR: b
                                        ASIGNACION: =
                                        expresion: 1
                                        COMA: ,
                                        lista_identificadores
                                            IDENTIFICADOR: siguiente
                        PUNTO_Y_COMA: ;
                lista_instrucciones
                    instruccion
                        estructura_de_control
                            iteracion
                                HACER: do
                                bloque
                                    LLAVE_IZQ: {
                                    lista_instrucciones
                                        instruccion
                                            sentencia
                                                llamado_a_funcion
                                                    IMPRIMIR: printf
                                                    PARENTESIS_IZQ: (
                                                    lista_argumentos
                                                        argumento: "Digite la cantidad de términos de la secuencia de Fibonacci: "
                                                    PARENTESIS_DER: )
                                                PUNTO_Y_COMA: ;
                                        lista_instrucciones
                                            instruccion
                                                sentencia
                                                    llamado_a_funcion
                                                        ESCRIBIR: scanf
                                                        PARENTESIS_IZQ: (
                                                        lista_argumentos
                                                            argumento: "%d"
                                                            COMA: ,
                                                            lista_argumentos
                                                                argumento
                                                                    referencia: &n
                                                        PARENTESIS_DER: )
                                                    PUNTO_Y_COMA: ;
                                    LLAVE_DER: }
                                MIENTRAS: while
                                PARENTESIS_IZQ: (
                                condicion
                                    expresion: n
                                    MENOR_IGUAL_QUE: <=
                                    expresion: 0
                                PARENTESIS_DER: )
                                PUNTO_Y_COMA: ;
            LLAVE_DER: }
```

---

## Ejecución del Analizador

Para ejecutar el analizador léxico y sintáctico, sigue estos pasos:

### Instalar PLY en tu entorno de Python:

```bash
pip install ply
```

### Ejecutar el script de Python que contiene el analizador:

```bash
python analizador_lexico.py 
python analizador_sintactico.py 
```

El programa analizará el código en C proporcionado y mostrará los tokens identificados, así como la estructura sintáctica validada.

### Para generar el árbol gramatical:

```bash
python arbol_gramatical.py
