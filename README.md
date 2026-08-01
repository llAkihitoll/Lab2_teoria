# Laboratorio 2 - Teoria de la computacion

Implementacion de los problemas 2 y 3 del laboratorio 2:

- **Problema 2**: validador de balanceo de expresiones infix usando una pila.
- **Problema 3**: algoritmo de Shunting Yard para convertir expresiones regulares de infix a postfix.

## Problema 3: algoritmo de Shunting Yard

El algoritmo de Shunting Yard (Dijkstra) convierte una expresion infix en
postfix (notacion polaca inversa) sin necesidad de parentesis, usando una
pila auxiliar para los operadores y una salida donde se van acumulando los
operandos y operadores ya resueltos.

Funcionamiento general:

1. Se recorre la expresion token por token.
2. Si el token es un operando (letra, digito, clase de caracteres, caracter
   escapado), se envia directamente a la salida.
3. Si el token es un operador, mientras el tope de la pila sea un operador
   con precedencia mayor o igual (y no sea un parentesis de apertura), se
   saca de la pila y se envia a la salida; luego se apila el operador
   actual.
4. Si el token es "(", se apila directamente.
5. Si el token es ")", se sacan operadores de la pila y se envian a la
   salida hasta encontrar el "(" correspondiente, que se descarta (no va a
   la salida).
6. Al terminar de recorrer todos los tokens, se sacan todos los operadores
   que queden en la pila y se envian a la salida.

Adaptacion para expresiones regulares:

- Operadores: `|` (union), concatenacion implicita, y `*` `+` `?` (postfijos
  unarios).
- Precedencia, de menor a mayor: `|` < concatenacion < `*` `+` `?`.
- Asociatividad izquierda para `|` y la concatenacion; los operadores
  postfijos unarios se aplican directo al operando anterior.
- En estas expresiones la concatenacion no tiene simbolo explicito (`ab`
  significa "a seguido de b"), asi que antes de correr el algoritmo se
  inserta un operador de concatenacion interno (no usamos `.` para esto
  porque `.` tambien aparece como caracter literal en las expresiones, por
  ejemplo en dominios de correo).
- Los operadores `+` y `?` se expanden antes de aplicar el algoritmo
  (`a+` -> `aa*`, `a?` -> `(a|epsilon)`), para trabajar solo con los
  operadores primitivos `|`, `*` y concatenacion, igual que en la
  conversion a AFN del problema 1.
- Las clases de caracteres `[xyz]` se tratan como un solo operando (no se
  abren caracter por caracter, a diferencia del validador de balanceo del
  problema 2).
- Los caracteres escapados con `\` se tratan como operandos literales,
  nunca como operadores.

## Video

Video de YouTube (no listado) con la ejecucion de los programas: https://youtu.be/-Dqk36rnSBs

## Como ejecutar

Requiere Python 3. No hay dependencias externas.

```
python problema2.py ejemplos/problema2.txt
python problema3.py ejemplos/problema3.txt
```

Cada programa recibe la ruta a un archivo de texto con una expresion por
linea, y para cada una imprime los pasos hechos sobre la pila y el
resultado final (balanceada/no balanceada, o la expresion en postfix).
