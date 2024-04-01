def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def imprimir_impares_entre(numero):
    for i in range(-numero, numero + 1):
        if i % 2 != 0:
            print(i, end=' ')

def imprimir_primos(numero):
    limite_superior = numero * 100
    primos_encontrados = 0
    candidato = 2
    while primos_encontrados < numero:
        if es_primo(candidato):
            print(candidato, end=' ')
            primos_encontrados += 1
        candidato += 1

def main():
    while True:
        try:
            numero = int(input("Por favor, ingresa un número positivo mayor que 0: "))
            if numero <= 0:
                print("El número debe ser mayor que 0. Inténtalo de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    print("Números impares entre -{} y {}:".format(numero, numero))
    imprimir_impares_entre(numero)
    print("\nNúmeros primos entre 0 y {}:".format(numero * 100))
    imprimir_primos(numero)

if __name__ == "__main__":
    main()
