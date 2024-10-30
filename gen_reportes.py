import json

from consistencia  import consistir_transaccion_BLACK, consistir_transaccion_CLASSIC, consistir_transaccion_GOLD


class Cliente:
    def __init__(self, apellido, nombre, numero, dni, tipo) -> None:
        self.transacciones = []
        self.apellido = apellido
        self.nombre = nombre
        self.numero = numero
        self.dni = dni
        self.tipo = tipo

    def nueva_transaccion(self, transaccion):
        self.transacciones.append(transaccion)

class Transaccion:
    def __init__(self, estado, tipo, cuentaNumero, cupoDiarioRes, monto, fecha, numero, saldoCuenta, totalTarjetas, totalCheq) -> None:
        self.estado = estado
        self.tipo = tipo
        self.cuenta_numero = cuentaNumero
        self.cupoDiarioRes = cupoDiarioRes
        self.monto = monto
        self.fecha = fecha
        self.numero = numero
        self.saldoCuenta = saldoCuenta
        self.totalTarjetas = totalTarjetas
        self.totalCheq = totalCheq
        self.rechazo = ""

    def es_rechazada(self):
        return self.estado == "RECHAZADA"
    
class SISTEMA_TPS:
    def leer_data(self) -> Cliente :
        with open("data.json", "r") as archivo:
            data = json.load(archivo)
        
        cliente = Cliente(
            data["apellido"],
            data["nombre"],
            data["numero"],
            data["DNI"],
            data["tipo"],
        )

        for data_transacciones in data["transacciones"]:
            transaccion = Transaccion(
                data_transacciones["estado"],
                data_transacciones["tipo"],
                data_transacciones["cuentaNumero"],
                data_transacciones["cupoDiarioRestante"],
                data_transacciones["monto"],
                data_transacciones["fecha"],
                data_transacciones["numero"],
                data_transacciones["saldoEnCuenta"],
                data_transacciones["totalTarjetasDeCreditoActualmente"],
                data_transacciones["totalChequerasActualmente"],
            )

            ##VALIDAR DICHAS TRANSACCIONES POR TIPO DE CLIENTE

            if cliente.tipo == 'BLACK':
                consistir_transaccion_BLACK(cliente, transaccion)
            elif cliente.tipo == "GOLD":
                consistir_transaccion_GOLD(cliente, transaccion)
            else:
                consistir_transaccion_CLASSIC(cliente, transaccion)

            cliente.nueva_transaccion(transaccion)
        return cliente

class ReporteHTML:
    def generar(self, cliente):
        # Estructura HTML básica usando formato de cadenas de Python
        html = f"""
        <html>
        <head><title>Reporte de Transacciones</title></head>
        <body>
            <h1>Reporte de {cliente.nombre} {cliente.apellido}</h1>
            <p>DNI: {cliente.dni}</p>
            <p>Tipo de Cliente: {cliente.tipo}</p>
            <table border="1">
                <tr>
                    <th>Fecha</th><th>Tipo</th><th>Estado</th><th>Monto</th><th>Razón Rechazo</th>
                </tr>
        """
        
        # Agregar cada transacción del cliente al HTML
        for trans in cliente.transacciones:
            razon_rechazo = trans.rechazo if trans.es_rechazada() else ""
            html += f"""
                <tr>
                    <td>{trans.fecha}</td>
                    <td>{trans.tipo}</td>
                    <td>{trans.estado}</td>
                    <td>{trans.monto}</td>
                    <td>{razon_rechazo}</td>
                </tr>
            """
        
        # Cerrar las etiquetas HTML
        html += """
            </table>
        </body>
        </html>
        """
        
        return html

# Crear instancias y generar reporte
procesador = SISTEMA_TPS()
cliente = procesador.leer_data()

reporte = ReporteHTML()
html_historial = reporte.generar(cliente)

# Guardar el HTML en un archivo
with open('reporte.html', 'w') as file:
    file.write(html_historial)
