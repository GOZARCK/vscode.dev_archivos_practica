def collatz(numero):
    secuencia = [numero]
    while numero != 1:
        if numero % 2 == 0:
            numero = numero // 2
        else:
            numero = numero * 3 + 1
        secuencia.append(numero)
    return secuencia


# ==================== PROGRAMA PRINCIPAL ====================

print("=== CONJETURA DE COLLATZ (Solo números pares positivos) ===\n")

while True:
    entrada = input("Ingresa un número par positivo: ").strip()
    
    if not entrada:
        print("❌ Error: No ingresaste nada.\n")
        continue
    
    if not entrada.isdigit():
        print("❌ Error: Solo se permiten números enteros positivos (sin letras ni signos).\n")
        continue
    
    try:
        n = int(entrada)
    except ValueError:
        print("❌ Error: Número inválido.\n")
        continue
    
    if n <= 0:
        print("❌ Error: El número debe ser positivo.\n")
        continue
    
    if n % 2 != 0:
        print("❌ Error: Debes ingresar un número PAR.\n")
        continue
    
    # Número válido
    print(f"\n✅ Número válido: {n}\n")
    print("Calculando secuencia...\n")
    
    secuencia = collatz(n)
    
    # Mostrar secuencia principal
    for i, num in enumerate(secuencia):
        if i < len(secuencia) - 1:
            print(num, end=" → ")
        else:
            print(num, end=" → ")
    
    # ==================== CICLO REPETITIVO (Solo demostración) ====================
    print("1 → 4 → 2 → 1 → 4 → 2 → 1")
    print("\n🔄 Ciclo repetitivo de Collatz (1 → 4 → 2 → 1) se repite infinitamente.")
    
    # Mostrar el ciclo 3 veces más como muestra
    print("\nDemostración del ciclo (3 repeticiones):")
    ciclo = [1, 4, 2]
    for _ in range(3):
        for num in ciclo:
            print(num, end=" → ")
        print("1", end=" → " if _ < 2 else "")
    print("... (continúa infinitamente)")
    
    print(f"\nTotal de pasos hasta llegar a 1: {len(secuencia)-1}")
    break