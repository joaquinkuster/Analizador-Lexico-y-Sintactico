# Analizador Léxico y Sintáctico con PLY (Python LEX-YACC)

## Integrantes

- *Joaquín Kuster* (joaquinkuster3000@gmail.com)

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

- PRINCIPAL
- INCLUIR
- BIBLIOTECA
- SI
- SI_NO
- MIENTRAS
- PARA
- HACER
- RETORNAR
- ENTERO
- VACIO
- IDENTIFICADOR
- NUMERO
- CADENA
- SUMA
- RESTA
- PRODUCTO
- DIVISION
- MODULO
- ASIGNACION
- IGUAL_QUE
- DIFERENTE_QUE
- MENOR_QUE
- MENOR_IGUAL_QUE
- MAYOR_QUE
- MAYOR_IGUAL_QUE
- Y_LOGICO
- O_LOGICO
- NEGACION
- INCREMENTO
- DECREMENTO
- LLAVE_IZQ
- LLAVE_DER
- PARENTESIS_IZQ
- PARENTESIS_DER
- ESCRIBIR
- IMPRIMIR
- REFERENCIA
- PUNTO_Y_COMA
- COMA

---

## Expresiones regulares para los tokens

<table>
  <thead>
    <tr>
      <th>Token</th>
      <th>Expresiones regulares</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PRINCIPAL</td>
      <td>r'main'</td>
    </tr>
    <tr>
      <td>INCLUIR</td>
      <td>r'\#include'</td>
    </tr>
    <tr>
      <td>BIBLIOTECA</td>
      <td>r'<[a-zA-Z_][a-zA-Z0-9_]*\.h>'</td>
    </tr>
    <tr>
      <td>SI</td>
      <td>r'if'</td>
    </tr>
    <tr>
      <td>SI_NO</td>
      <td>r'else'</td>
    </tr>
    <tr>
      <td>MIENTRAS</td>
      <td>r'while'</td>
    </tr>
    <tr>
      <td>PARA</td>
      <td>r'for'</td>
    </tr>
    <tr>
      <td>HACER</td>
      <td>r'do'</td>
    </tr>
    <tr>
      <td>RETORNAR</td>
      <td>r'return'</td>
    </tr>
    <tr>
      <td>ENTERO</td>
      <td>r'int'</td>
    </tr>
    <tr>
      <td>VACIO</td>
      <td>r'void'</td>
    </tr>
    <tr>
      <td>IDENTIFICADOR</td>
      <td>r'[a-zA-Z_][a-zA-Z_0-9]*'</td>
    </tr>
    <tr>
      <td>NUMERO</td>
      <td>r'\d+(\.\d+)?'</td>
    </tr>
    <tr>
      <td>CADENA</td>
      <td>r'\"(\\.|[^\\"])*\"'</td>
    </tr>
    <tr>
      <td>SUMA</td>
      <td>r'\+'</td>
    </tr>
    <tr>
      <td>RESTA</td>
      <td>r'-'</td>
    </tr>
    <tr>
      <td>PRODUCTO</td>
      <td>r'\*'</td>
    </tr>
    <tr>
      <td>DIVISION</td>
      <td>r'/'</td>
    </tr>
    <tr>
      <td>MODULO</td>
      <td>r'%'</td>
    </tr>
    <tr>
      <td>ASIGNACION</td>
      <td>r'='</td>
    </tr>
    <tr>
      <td>IGUAL_QUE</td>
      <td>r'=='</td>
    </tr>
    <tr>
      <td>DIFERENTE_QUE</td>
      <td>r'!='</td>
    </tr>
    <tr>
      <td>MENOR_QUE</td>
      <td>r'<'</td>
    </tr>
    <tr>
      <td>MENOR_IGUAL_QUE</td>
      <td>r'<='</td>
    </tr>
    <tr>
      <td>MAYOR_QUE</td>
      <td>r'>'</td>
    </tr>
    <tr>
      <td>MAYOR_IGUAL_QUE</td>
      <td>r'>='</td>
    </tr>
    <tr>
      <td>Y_LOGICO</td>
      <td>r'&&'</td>
    </tr>
    <tr>
      <td>O_LOGICO</td>
      <td>r'\|\|'</td>
    </tr>
    <tr>
      <td>NEGACION</td>
      <td>r'!'</td>
    </tr>
    <tr>
      <td>INCREMENTO</td>
      <td>r'\+\+'</td>
    </tr>
    <tr>
      <td>DECREMENTO</td>
      <td>r'--'</td>
    </tr>
    <tr>
      <td>LLAVE_IZQ</td>
      <td>r'\{'</td>
    </tr>
    <tr>
      <td>LLAVE_DER</td>
      <td>r'\}'</td>
    </tr>
    <tr>
      <td>PARENTESIS_IZQ</td>
      <td>r'\('</td>
    </tr>
    <tr>
      <td>PARENTESIS_DER</td>
      <td>r'\)'</td>
    </tr>
    <tr>
      <td>PUNTO_Y_COMA</td>
      <td>r';'</td>
    </tr>
    <tr>
      <td>COMA</td>
      <td>r','</td>
    </tr>
    <tr>
      <td>ESCRIBIR</td>
      <td>r'scanf'</td>
    </tr>
    <tr>
      <td>IMPRIMIR</td>
      <td>r'printf'</td>
    </tr>
    <tr>
      <td>REFERENCIA</td>
      <td>r'&'</td>
    </tr>
  </tbody>
</table>

---

## Gramática

| Regla | Definición |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| programa | `programa → lista_declarativas inicio` \| `programa → inicio` |
| lista_declarativas | `lista_declarativas → declarativa lista_declarativas` \| `lista_declarativas → declarativa` |
| declarativa | `declarativa → inclusion` |
| inclusion | `inclusion → INCLUIR BIBLIOTECA` |
| inicio | `inicio → ENTERO PRINCIPAL PARENTESIS_IZQ lista_parametros PARENTESIS_DER bloque` \| `inicio → ENTERO PRINCIPAL PARENTESIS_IZQ PARENTESIS_DER bloque` |
| bloque | `bloque → LLAVE_IZQ lista_instrucciones LLAVE_DER` \| `bloque → LLAVE_IZQ LLAVE_DER` |
| lista_instrucciones | `lista_instrucciones → instruccion lista_instrucciones` \| `lista_instrucciones → instruccion` |
| instruccion | `instruccion → declaracion` \| `instruccion → sentencia` \| `instruccion → estructura_de_control` |
| declaracion | `declaracion → declaracion_variable PUNTO_Y_COMA` \| `declaracion → prototipo_funcion PUNTO_Y_COMA` \| `declaracion → definicion_funcion` |
| declaracion_variable | `declaracion_variable → tipo lista_identificadores` |
| lista_identificadores | `lista_identificadores → IDENTIFICADOR` \| `lista_identificadores → IDENTIFICADOR ASIGNACION expresion` \| `lista_identificadores → IDENTIFICADOR COMA lista_identificadores` \| `lista_identificadores → IDENTIFICADOR ASIGNACION expresion COMA lista_identificadores` |
| prototipo_funcion | `prototipo_funcion → tipo IDENTIFICADOR PARENTESIS_IZQ lista_parametros PARENTESIS_DER` \| `prototipo_funcion → tipo IDENTIFICADOR PARENTESIS_IZQ PARENTESIS_DER` |
| definicion_funcion | `definicion_funcion → tipo IDENTIFICADOR PARENTESIS_IZQ lista_parametros PARENTESIS_DER bloque` \| `definicion_funcion → tipo IDENTIFICADOR PARENTESIS_IZQ PARENTESIS_DER bloque` |
| lista_parametros | `lista_parametros → parametro COMA lista_parametros` \| `lista_parametros → parametro` \| `lista_parametros → VACIO` |
| parametro | `parametro → tipo IDENTIFICADOR` |
| sentencia | `sentencia → asignacion PUNTO_Y_COMA` \| `sentencia → llamado_a_funcion PUNTO_Y_COMA` \| `sentencia → retorno PUNTO_Y_COMA` |
| asignacion | `asignacion → IDENTIFICADOR ASIGNACION expresion` \| `asignacion → IDENTIFICADOR INCREMENTO` \| `asignacion → IDENTIFICADOR DECREMENTO` |
| condicion | `condicion → expresion Y_LOGICO expresion` \| `condicion → expresion O_LOGICO expresion` \| `condicion → NEGACION expresion` \| `condicion → expresion IGUAL_QUE expresion` \| ... |
| tipo | `tipo → ENTERO` \| `tipo → VACIO` |
| expresion | `expresion → expresion SUMA expresion` \| `expresion → expresion RESTA expresion` \| `expresion → expresion PRODUCTO expresion` \| `expresion → expresion DIVISION expresion` \| `expresion → expresion MODULO expresion` \| `expresion → PARENTESIS_IZQ expresion PARENTESIS_DER` \| `expresion → NUMERO` \| `expresion → IDENTIFICADOR` \| `expresion → llamado_a_funcion` |
| llamado_a_funcion | `llamado_a_funcion → IDENTIFICADOR PARENTESIS_IZQ lista_argumentos PARENTESIS_DER` \| `llamado_a_funcion → ESCRIBIR PARENTESIS_IZQ lista_argumentos PARENTESIS_DER` \| `llamado_a_funcion → IMPRIMIR PARENTESIS_IZQ lista_argumentos PARENTESIS_DER` |
| lista_argumentos | `lista_argumentos → argumento COMA lista_argumentos` \| `lista_argumentos → argumento` \| `lista_argumentos → VACIO` |
| argumento | `argumento → expresion` \| `argumento → CADENA` \| `argumento → referencia` |
| referencia | `referencia → REFERENCIA IDENTIFICADOR` |
| retorno | `retorno → RETORNAR expresion` \| `retorno → RETORNAR` |
| estructura_de_control | `estructura_de_control → seleccion` \| `estructura_de_control → iteracion` |
| seleccion | `seleccion → SI PARENTESIS_IZQ condicion PARENTESIS_DER bloque` \| `seleccion → SI PARENTESIS_IZQ condicion PARENTESIS_DER bloque SI_NO bloque` \| `seleccion → SI PARENTESIS_IZQ condicion PARENTESIS_DER bloque SI_NO seleccion` |
| iteracion | `iteracion → MIENTRAS PARENTESIS_IZQ condicion PARENTESIS_DER bloque` \| `iteracion → PARA PARENTESIS_IZQ declaracion_variable PUNTO_Y_COMA condicion PUNTO_Y_COMA asignacion PARENTESIS_DER bloque` \| `iteracion → HACER bloque MIENTRAS PARENTESIS_IZQ condicion PARENTESIS_DER PUNTO_Y_COMA` |

| **Declaración**                                                    | **Tipo**       | **Gramática**                                                                 |
|-----------------------------------------------------------------|--------------|-----------------------------------------------------------------------------|
| `#include <stdio.h>`                                           | inclusión    | `RESERVADO RESERVADO`                                                      |
| `int main() { }`                                               | inicio      | `ENTERO PRINCIPAL PARENTESIS_IZQ PARENTESIS_DER bloque`             |
| `int n, a = 0, b = 1, siguiente;`                              | declaración  | `RESERVADO IDENTIFICADOR COMA IDENTIFICADOR IGUAL valor COMA ... PUNTOCOMA` |
| `do { ... } while (n <= 0);`                                   | iteración    | `RESERVADO bloque RESERVADO PARENTESIS_IZQ condicion PARENTESIS_DER PUNTOCOMA` |
| `printf("Digite la cantidad de términos de la secuencia...");` | función      | `RESERVADO PARENTESIS_IZQ argumento PARENTESIS_DER PUNTOCOMA`             |
| `scanf("%d", &n);`                                             | función      | `RESERVADO PARENTESIS_IZQ argumentos PARENTESIS_DER PUNTOCOMA`            |
| `if (n <= 0) { ... }`                                          | selección    | `RESERVADO PARENTESIS_IZQ condicion PARENTESIS_DER bloque`               |
| `printf("Por favor, ingresa un número mayor que 0.\n");`       | función      | `RESERVADO PARENTESIS_IZQ argumento PARENTESIS_DER PUNTOCOMA`             |
| `for (int i = 1; i <= n; i++) { ... }`                         | iteración    | `RESERVADO PARENTESIS_IZQ declaracion PUNTOCOMA condicion PUNTOCOMA incremento PARENTESIS_DER bloque` |
| `printf("%d ", a);`                                             | función      | `RESERVADO PARENTESIS_IZQ argumento PARENTESIS_DER PUNTOCOMA`             |
| `siguiente = a + b;`                                           | asignación   | `IDENTIFICADOR IGUAL operacion PUNTOCOMA`                                |
| `a = b;`                                                       | asignación   | `IDENTIFICADOR IGUAL IDENTIFICADOR PUNTOCOMA`                            |
| `b = siguiente;`                                               | asignación   | `IDENTIFICADOR IGUAL IDENTIFICADOR PUNTOCOMA`                            |
| `return 0;`                                                    | retorno      | `RESERVADO valor PUNTOCOMA`                                              |
| `&n`                                                           | referencia   | `AMPERSON IDENTIFICADOR`                                                 |
| `i = 1; i <= n; i++`                                           | argumentos   | `argumento PUNTOCOMA argumentos`                                         |
| `"Digite la cantidad de términos de la secuencia..."`         | argumento    | `STRING`                                                                |
| `"%d", &n`                                                     | argumentos   | `argumento COMA argumentos`                                             |
| `"%d"`                                                         | argumento    | `STRING`                                                                |
| `i = 1`                                                        | asignación   | `IDENTIFICADOR IGUAL valor`                                             |
| `i <= n`                                                       | condición    | `IDENTIFICADOR MENOR_IGUAL valor`                                       |
| `i++`                                                          | incremento   | `IDENTIFICADOR MASMAS`                                                  |
| `a + b`                                                        | operación    | `valor MAS valor`                                                       |
| `"%d ", a`                                                     | argumentos   | `argumento COMA argumentos`                                             |




