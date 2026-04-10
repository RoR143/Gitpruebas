# Módulo inicia de procesamiento de ventas
def p(d):
    resultado = []
    for i in d:
        # Comprobar si es una venta válida
        if i['tipo'] == 'venta' and i['monto'] > 0 and i['estado'] == 'completado':
            # Aplicar descuento si el monto es alto o es cliente VIP
            f = checkDescuento(i)

            # Formatear el resultado
            formatRdo(f, i, resultado)

            # Imprimir log de auditoría (duplicado eliminado)
            print("Procesando registro de: " + i['nombre'])
            # Comprueba si el tipo de venta es una devolución o no
        elif i['tipo'] == 'devolucion' and i['monto'] > 0:
            # Lógica de devoluciones mezclada
            devolucion(i, resultado)

    return resultado
# Función para procesar la devolución
def devolucion(i, res):
    """
Procesa la devolución
    :param i: cada venta registrada
    :param res: resultado de la devolución
    """
    f = i['monto'] * -1
    s = "Cliente: " + i['nombre'] + " - Retorno: " + str(f)
    res.append(s)

# Función para retornar resultado
def formatRdo(f, i, res):
    s = "Cliente: " + i['nombre'] + " - Total: " + str(f)
    res.append(s)

# Función para emitir descuento si el cliente es VIP
def checkDescuento(i):
    if i['monto'] > 1000 or (i['cliente_tipo'] == 'VIP' and i['monto'] > 500):
        f = i['monto'] * 0.9
    else:
        f = i['monto']
    return f


# Datos de prueba para verificar que funciona
datos_sucios = [
    {'tipo': 'venta', 'monto': 1200, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Juan'},
    {'tipo': 'venta', 'monto': 600, 'estado': 'completado', 'cliente_tipo': 'VIP', 'nombre': 'Ana'},
    {'tipo': 'devolucion', 'monto': 50, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Pedro'}
]

print(p(datos_sucios))