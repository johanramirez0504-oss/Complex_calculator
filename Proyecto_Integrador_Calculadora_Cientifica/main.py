import Calculadora_Cientifica as calc

def mostrar_menu():
    print("\n" + "="*50)
    print("      CALCULADORA CIENTÍFICA - MENÚ PRINCIPAL")
    print("="*50)
    print("--- Operaciones Aritméticas ---")
    print("1. Sumar, Restar, Multiplicar, Dividir")
    print("2. División entera y Residuo (Módulo)")
    print("--- Funciones Científicas y Avanzadas ---")
    print("3. Potencia / Radicación")
    print("4. Valor absoluto")
    print("5. Trigonometría (Seno, Coseno, Tangente, Secante, Cosecante, Cotangente)")
    print("6. Conversión de ángulos (Grados ⇄ Radianes)")
    print("7. Teorema de Pitágoras (Hipotenusa o Cateto)")
    print("8. Factorial y Logaritmo")
    print("9. Generar número aleatorio")
    print("0. Salir")
    print("="*50)

def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        try:
                
            if opcion == "0":
                print("Saliendo de la calculadora. ¡Excelente trabajo!")
                break

            elif opcion == "1":
                a = float(input("Primer número: "))
                b = float(input("Segundo número: "))
                op = input("Elige operador (+, -, *, /): ").strip()
                if op == "+": print("Resultado:", calc.sumar(a, b))
                elif op == "-": print("Resultado:", calc.restar(a, b))
                elif op == "*": print("Resultado:", calc.multiplicar(a, b))
                elif op == "/": print("Resultado:", calc.dividir(a, b))
                else: print("Operador no válido.")

            elif opcion == "2":
                a = int(input("Primer número entero: "))
                b = int(input("Segundo número entero: "))
                op = input("Elige ((D)ivisión entera / (R)esiduo): ").upper().strip()
                if op == "D": print("División entera:", calc.dividir_entero(a, b))
                elif op == "R": print("Residuo:", calc.residuo(a, b))
                else: print("Opción no válida.")

            elif opcion == "3":
                sub = input("(P)otencia O (R)adicación: ").upper().strip()
                if sub == "P":
                    base = float(input("Base: "))
                    exp = float(input("Exponente: "))
                    print("Resultado:", calc.potencia(base, exp))
                elif sub == "R":
                    num = float(input("Radicando: "))
                    expo = float(input("Exponente del radicando: "))
                    indi= float(input("Índice: "))
                    print("Raíz:", calc.radicacion(num,indi,expo))

            elif opcion == "4":
                num = float(input("Número: "))
                print("Valor absoluto:", calc.valor_absoluto(num))

            elif opcion == "5":
                angulo = float(input("Ángulo en radianes: "))
                print(f"Seno: {calc.seno(angulo):.4f}")
                print(f"Coseno: {calc.coseno(angulo):.4f}")
                print(f"Tangente: {calc.tangente(angulo):.4f}")
                print(f"Secante: {calc.secante(angulo):.4f}")
                print(f"Cosecante: {calc.cosecante(angulo):.4f}")
                print(f"Cotangente: {calc.cotangente(angulo):.4f}")

            elif opcion == "6":
                sub = input("(G)rados a radianes o (R)adianes a grados: ").upper().strip()
                val = float(input("Valor numérico: "))
                if sub == "G": print("En radianes:", calc.radianes(val))
                elif sub == "R": print("En grados:", calc.grados(val))

            elif opcion == "7":
                sub = input("¿Qué deseas calcular? (H)ipotenusa o (C)ateto: ").upper().strip()
                if sub == "H":
                    c1 = float(input("Cateto 1: "))
                    c2 = float(input("Cateto 2: "))
                    print("Hipotenusa:", calc.teorema_pitagoras(c1, c2))
                elif sub == "C":
                    hip = float(input("Hipotenusa: "))
                    cat = float(input("Cateto conocido: "))
                    print("Cateto faltante:", calc.teorema_pitagoras_cateto(hip, cat))

            elif opcion == "8":
                sub = input("(F)actorial o (L)ogaritmo: ").upper().strip()
                if sub == "F":
                    n = int(input("Número entero positivo: "))
                    print("Factorial:", calc.factorial(n))
                elif sub == "L":
                    n = float(input("Número: "))
                    base_log = input("Base del logaritmo: ").strip()
                    if base_log == "":

                        print("Logaritmo natural:", calc.logaritmo(n))
                    else:
                        print("Logaritmo:", calc.logaritmo(n, float(base_log)))

            elif opcion == "9":
                
                min_v = int(input("Mínimo: "))
                max_v = int(input("Máximo: "))
                print("Número aleatorio:", calc.numero_aleatorio(min_v,max_v))
           
            else:
                print("Opción no válida.")

        except ValueError as e:
            print(f"Error de cálculo o formato: {e}")

if __name__ == "__main__":
    ejecutar()
    