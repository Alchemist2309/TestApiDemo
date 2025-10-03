def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def ordenar_cadenas(cadena: str) -> str:
    palabras = cadena.lower().split()
    palabras.sort()
    return " ".join(palabras)


def es_palindromo(cadena: str) -> bool:
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]


def fibonacci(n: int) -> list:
    if n <= 0:
        return []
    secuencia = [0, 1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia[:n]


def suma_dos_numeros(nums: list, objetivo: int):
    vistos = set()
    for num in nums:
        complemento = objetivo - num
        if complemento in vistos:
            return (complemento, num)
        vistos.add(num)
    return None


def menu():
    while True:
        print("\n===== MENÚ DE RETOS =====")
        print("1. Verificar si un número es primo")
        print("2. Ordenar palabras en una cadena")
        print("3. Verificar si una cadena es palíndromo")
        print("4. Generar secuencia de Fibonacci")
        print("5. Encontrar dos números que sumen un objetivo")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            n = int(input("Ingresa un número entero positivo: "))
            print("Resultado:", "Verdadero" if es_primo(n) else "Falso")

        elif opcion == "2":
            cadena = input("Ingresa una cadena de palabras separadas por espacios: ")
            print("Resultado:", ordenar_cadenas(cadena))

        elif opcion == "3":
            cadena = input("Ingresa una palabra o frase: ")
            print("Resultado:", "Verdadero" if es_palindromo(cadena) else "Falso")

        elif opcion == "4":
            n = int(input("¿Cuántos números de la secuencia Fibonacci deseas generar?: "))
            print("Resultado:", fibonacci(n))

        elif opcion == "5":
            lista = input("Ingresa una lista de números separados por espacios: ")
            lista = list(map(int, lista.split()))
            objetivo = int(input("Ingresa el número objetivo: "))
            print("Resultado:", suma_dos_numeros(lista, objetivo))

        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
