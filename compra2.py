import datetime
import random

nombre_tienda = input("Ingresa el nombre de la tienda: ")
nombre = input("Ingresa tu nombre: ")
producto = input("Ingresa el nombre del producto: ")
total_compra = float(input("Ingresa el total de tu compra: "))

folio = random.randint(1000, 9999)


fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


descuento = total_compra * 0.10
total_final = total_compra - descuento


print("\n=====================================")
print("         TICKET DE COMPRA           ")
print("=====================================")
print(f"Tienda:{nombre_tienda}")
print(f"Folio: {folio}")
print(f"Fecha y hora: {fecha_hora}")
print("\nCliente:", nombre)
print("Producto:", producto)
print(f"Total de la compra: ${total_compra:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${total_final:.2f}")
print("\n=====================================")
print("¡Gracias por tu compra! ¡Vuelve pronto!")
print("=====================================")