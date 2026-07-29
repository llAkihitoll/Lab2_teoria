import sys

from file_utils import leer_lineas
from balance_checker import validar_balanceo


def main():
    if len(sys.argv) < 2:
        print("Uso: python problema2.py <archivo>")
        return

    ruta = sys.argv[1]
    expresiones = leer_lineas(ruta)

    for numero, expresion in enumerate(expresiones, start=1):
        print(f"\nExpresion {numero}: {expresion}")
        esta_balanceada, pasos = validar_balanceo(expresion)

        for paso in pasos:
            print(f"  {paso}")

        resultado = "BALANCEADA" if esta_balanceada else "NO BALANCEADA"
        print(f"  Resultado: {resultado}")


if __name__ == "__main__":
    main()
