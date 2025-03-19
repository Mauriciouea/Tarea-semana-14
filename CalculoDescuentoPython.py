def calcular_descuento (monto_total, porcentaje_descuento=10):
    #calcular el descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    #devolver el monto de descuento
    return descuento

monto = 89
descuento_calculado = calcular_descuento(monto)
print (f"El monto del descuento es: {descuento_calculado}: el monto a cancelar es {monto}")