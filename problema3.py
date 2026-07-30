import sys

from file_utils import leer_lineas
from shunting_yard import convertir_a_postfix


def main():
    if len(sys.argv) < 2:
        print("Uso: python problema3.py <archivo>")
        return

    ruta = sys.argv[1]
    expresiones = leer_lineas(ruta)

    for numero, expresion in enumerate(expresiones, start=1):
        print(f"\nExpresion {numero}: {expresion}")
        postfix, pasos = convertir_a_postfix(expresion)

        for paso in pasos:
            print(f"  {paso}")

        print(f"  Postfix: {' '.join(postfix)}")


if __name__ == "__main__":
    main()
