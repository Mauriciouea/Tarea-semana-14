def calcular_descuento (monto_total, porcentaje_descuento=10):
    #calcular el descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    #devolver el monto de descuento
    return descuento

# Programa principal
if __name__ == "__main__":
    # Primera llamada a la función con solo el monto total
    monto1 = 357  # Monto total de la compra
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    print(f"Compra 1: Monto total: {monto1}, Descuento: {descuento1}, Monto final a pagar: {monto_final1}")

    # Segunda llamada a la función con monto total y porcentaje de descuento
    monto2 = 798  # Monto total de la compra
    porcentaje_descuento2 = 15  # Porcentaje de descuento
    descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
    monto_final2 = monto2 - descuento2
    print(f"Compra 2: Monto total: {monto2}, Descuento: {descuento2}, Monto final a pagar: {monto_final2}")