import os

os.system("cls")

saldo = 0
cantidad_retiro = 0
opcion = 0

while opcion != 4:

    print("=== CAJERO AUTOMÁTICO ===")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    try:
        opcion = int(input("Ingrese opción: "))

        if opcion == 1:
            print("1. Consultar saldo")
            print(f"Saldo actual: ${saldo}")

        elif opcion == 2:
            print("2. Depositar dinero")

            deposito = 0

            while deposito <= 0:
                deposito = int(input("Ingrese valor a depositar: "))

                if deposito <= 0:
                    print("El monto debe ser positivo.")

            saldo = saldo + deposito
            print(f"Depósito realizado correctamente.")
            print(f"Saldo actual: ${saldo}")

        elif opcion == 3:
            print("3. Retirar dinero")

            if saldo <= 0:
                print("No tienes suficiente saldo para retirar.\n")

            elif cantidad_retiro >= 3:
                print("Has alcanzado el máximo de 3 retiros.")

            else:
                retiro = int(input("Ingrese monto a retirar: "))

                if retiro <= 0:
                    print("El monto debe ser positivo.")

                elif retiro > saldo:
                    print("No tienes saldo suficiente para realizar este retiro.")

                elif retiro % 10000 != 0:
                    print("El retiro debe ser un múltiplo de $10.000.")

                else:
                    saldo = saldo - retiro
                    cantidad_retiro = cantidad_retiro + 1

                    print("Retiro realizado correctamente.")
                    print(f"Retiraste: ${retiro}")
                    print(f"Saldo actual: ${saldo}")
                    print(f"Retiros realizados: {cantidad_retiro}/3")

        elif opcion == 4:
            print("Gracias por utilizar el cajero automático.")

        else:
            print("Opción inválida. Debe ingresar un número del 1 al 4.")

    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")
