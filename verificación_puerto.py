try:
    puerto_str = input("Ingrese el número de puerto TCP/UDP: ")
    puerto = int(puerto_str)

    if 0 <= puerto <= 1023:
        print(f"El puerto {puerto} pertenece al rango de Puertos Bien Conocidos (0-1023).")
    elif 1024 <= puerto <= 49151:
        print(f"El puerto {puerto} pertenece al rango de Puertos Registrados (1024-49151).")
    elif 49152 <= puerto <= 65535:
        print(f"El puerto {puerto} pertenece al rango de Puertos Dinámicos o Privados (49152-65535).")
    else:
        print(f"El número {puerto} está fuera del rango válido de puertos TCP/UDP (0-65535).")

except ValueError:
    print(f"Error: '{puerto_str}' no es un número entero válido.")
    print("Por favor, ingrese solo números.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")