import time

def obtener_primos_hasta(limite):
    if limite < 2:
        return []

    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False

    for i in range(2, int(limite**0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, limite + 1, i):
                es_primo[j] = False

    return [i for i, primo in enumerate(es_primo) if primo]


print("=== CONTADOR DE NÚMEROS PRIMOS ===\n")

limite = int(input("¿Hasta qué número quieres contar los primos?: "))

inicio = time.time()

primos = obtener_primos_hasta(limite)

tiempo = time.time() - inicio

print("\n=== LISTA DE PRIMOS ===\n")

for secuencia, primo in enumerate(primos, start=1):
    print(f"{secuencia:>8} -> {primo}")

print(f"\nCantidad total de primos: {len(primos):,}")
print(f"Tiempo: {tiempo:.3f} segundos")