def division_con_errores(a, b):
    """
    Intenta dividir 'a' por 'b'.
    Provoca ZeroDivisionError si b es 0.
    Provoca TypeError si 'a' o 'b' no son números.
    """
    resultado = a / b
    return resultado

# 💥 Error 1: División por Cero (ZeroDivisionError)
print("Intentando 10 / 0...")
try:
    print(division_con_errores(10, 0))
except ZeroDivisionError as e:
    print(f"Error detectado: {e}")

print("-" * 20)

# 💥 Error 2: Tipos de Datos Incorrectos (TypeError)
print("Intentando 'hola' / 2...")
try:
    print(division_con_errores("hola", 2))
except TypeError as e:
    print(f"Error detectado: {e}")

print("-" * 20)

# ✅ Resultado Correcto (para demostrar el funcionamiento normal)
print("Intentando 10 / 2 (Correcto)...")
print(division_con_errores(10, 2))