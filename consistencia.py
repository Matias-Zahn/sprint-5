def consistir_transaccion_BLACK(cliente, transaccion): 
        if transaccion.tipo == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
            # Limita el saldo negativo hasta -10,000 y verifica el límite diario de retiro de 100,000
            if (transaccion.saldoCuenta - transaccion.monto < -10000):
                transaccion.estado = "RECHAZADA"
                transaccion.rechazo = "Saldo insuficiente, límite de descubierto alcanzado"
            elif transaccion.monto > 100000:
                transaccion.estado = "RECHAZADA"
                transaccion.rechazo = "Excede el límite diario de retiro"

        elif transaccion.tipo == 'ALTA_TARJETA_CREDITO':
            # Máximo 5 tarjetas de crédito
            if transaccion.totalTarjetas >= 5:
                transaccion.estado = "RECHAZADA"
                transaccion.rechazo = "Límite de tarjetas de crédito alcanzado"

        elif transaccion.tipo == 'ALTA_CHEQUERA':
            # Máximo 2 chequeras para clientes Black
            if transaccion.totalCheq >= 2:
                transaccion.estado = "RECHAZADA"
                transaccion.rechazo = "Límite de chequeras alcanzado"

        elif transaccion.tipo == 'COMPRAR_DOLAR':
            # Clientes Black deben tener cuenta en dólares para realizar la compra
            if not cliente.tiene_cuenta_dolares:
                transaccion.estado = "RECHAZADA"
                transaccion.rechazo = "Cliente sin cuenta en dólares"

        elif transaccion.tipo == 'TRANSFERENCIA_ENVIADA':
            # No aplica comisión y no requiere autorización adicional
            if transaccion.monto > transaccion.saldo_en_cuenta and (transaccion.saldo_en_cuenta - transaccion.monto < -10000):
                transaccion.estado = "RECHAZADA"
                transaccion.rechazo = "Saldo insuficiente para cubrir transferencia"

        elif transaccion.tipo == 'TRANSFERENCIA_RECIBIDA':
            # Clientes Black pueden recibir transferencias sin límite y sin autorización previa
            transaccion.estado = "ACEPTADA"  # Aceptada sin validaciones adicionales

def consistir_transaccion_GOLD(cliente, transaccion):
            if transaccion.tipo == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                # Limita el saldo negativo hasta -10,000 y verifica el límite diario de retiro de 100,000
                if (transaccion.saldoCuenta - transaccion.monto < -10000):
                    transaccion.estado = "RECHAZADA"
                    transaccion.rechazo = "Saldo insuficiente, límite de descubierto alcanzado"
                elif transaccion.monto > 20000:
                    transaccion.estado = "RECHAZADA"
                    transaccion.rechazo = "Excede el límite diario de retiro"

            elif transaccion.tipo == 'ALTA_TARJETA_CREDITO':
                # Máximo 5 tarjetas de crédito
                if transaccion.totalTarjetas > 1:
                    transaccion.estado = "RECHAZADA"
                    transaccion.rechazo = "Límite de tarjetas de crédito alcanzado"

            elif transaccion.tipo == 'ALTA_CHEQUERA':
                # Máximo 2 chequeras para clientes Black
                if transaccion.totalCheq > 1:
                    transaccion.estado = "RECHAZADA"
                    transaccion.rechazo = "Límite de chequeras alcanzado"

            elif transaccion.tipo == 'COMPRAR_DOLAR':
                # Clientes Black deben tener cuenta en dólares para realizar la compra
                if not cliente.tiene_cuenta_dolares:
                    transaccion.estado = "RECHAZADA"
                    transaccion.rechazo = "Cliente sin cuenta en dólares"

            elif transaccion.tipo == 'TRANSFERENCIA_ENVIADA':
                transf_comision = (transaccion.monto * 0.005) 

                if transf_comision > transaccion.saldo_en_cuenta and (transaccion.saldo_en_cuenta - transaccion.monto < -10000):
                    transaccion.estado = "RECHAZADA"
                    transaccion.rechazo = "Saldo insuficiente para cubrir transferencia"

            elif transaccion.tipo == 'TRANSFERENCIA_RECIBIDA':
                if transaccion.monto > '50000':
                    transaccion.estado = "RECHAZADA"
                    transaccion.rechazo = "El monto supera el pactado como cliente, comuniquese con un representante para solucionar el problema"


def consistir_transaccion_CLASSIC(cliente, transaccion):
            if transaccion.tipo == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                if transaccion.monto > 1000:
                    transaccion.estado = "RECHAZADA"
                    transaccion.rechazo = "Excede el límite diario de retiro"
            elif transaccion.tipo == 'ALTA_TARJETA_CREDITO':
                if transaccion.totalTarjetas >= 1:
                    transaccion.estado = "RECHAZADA"
                    transaccion.rechazo = "No puede acceder a las tarjetas de credito"

            elif transaccion.tipo == 'ALTA_CHEQUERA':
                if transaccion.totalCheq >= 1:
                    transaccion.estado = "RECHAZADA"
                    transaccion.rechazo = "No puede acceder a chequeras"

            elif transaccion.tipo == 'COMPRAR_DOLAR':
                if not cliente.tiene_cuenta_dolares:
                    transaccion.estado = "RECHAZADA"
                    transaccion.rechazo = "Cliente sin cuenta en dólares"

            elif transaccion.tipo == 'TRANSFERENCIA_ENVIADA':

                transf_comision = (transaccion.monto * 0.01) 

                if transf_comision > transaccion.saldo_en_cuenta:
                    transaccion.estado = "RECHAZADA"
                    transaccion.rechazo = "Saldo insuficiente para cubrir transferencia"

            elif transaccion.tipo == 'TRANSFERENCIA_RECIBIDA':
                if transaccion.monto > '150000':
                    transaccion.estado = "RECHAZADA"
                    transaccion.rechazo = "El monto supera el pactado como cliente, comuniquese con un representante para solucionar el problema"