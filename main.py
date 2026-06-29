# ============================================================
#  SISTEMA DE CONTROL DE ALMUERZOS
#  Proyecto Integrador — Python básico
#  Diccionarios, listas, condicionales, ciclos, funciones
# ============================================================

# ------------------------------------------------------------
# PRECIOS
# ------------------------------------------------------------
PRECIO_SOPA    = 1.00
PRECIO_SEGUNDO = 1.50
PRECIO_JUGO    = 0.50

# ------------------------------------------------------------
# CONTRASEÑA ADMINISTRADOR
# ------------------------------------------------------------
CLAVE_ADMIN = "admin123"

# ------------------------------------------------------------
# DATOS INICIALES — 10 personas ficticias
# ------------------------------------------------------------
personas = [
    {"cedula": "1111111111", "nombre": "Ana Torres",     "empresa": "Empresa A"},
    {"cedula": "2222222222", "nombre": "Carlos Mendoza", "empresa": "Empresa A"},
    {"cedula": "3333333333", "nombre": "Lucia Paredes",  "empresa": "Empresa B"},
    {"cedula": "4444444444", "nombre": "Jorge Ramirez",  "empresa": "Empresa B"},
    {"cedula": "5555555555", "nombre": "Maria Castillo", "empresa": "Empresa C"},
    {"cedula": "6666666666", "nombre": "Pedro Suarez",   "empresa": "Empresa C"},
    {"cedula": "7777777777", "nombre": "Sofia Flores",   "empresa": "Empresa A"},
    {"cedula": "8888888888", "nombre": "Diego Vasquez",  "empresa": "Empresa B"},
    {"cedula": "9999999999", "nombre": "Valeria Mora",   "empresa": "Empresa C"},
    {"cedula": "1234567890", "nombre": "Luis Gomez",     "empresa": "Empresa A"},
]

# ------------------------------------------------------------
# REGISTROS DEL DÍA Y DEL MES
# ------------------------------------------------------------
consumos_dia = []
consumos_mes = []


# ============================================================
# FUNCIONES AUXILIARES DE VISUALIZACIÓN
# ============================================================

def linea_doble():
    print("=" * 54)

def linea_simple():
    print("-" * 54)

def mensaje_ok(texto):
    """Mensaje de éxito — siempre con el mismo formato."""
    print("  [OK] " + texto)

def mensaje_error(texto):
    """Mensaje de error — siempre con el mismo formato."""
    print("  [ERROR] " + texto)

def mensaje_aviso(texto):
    """Mensaje informativo — siempre con el mismo formato."""
    print("  [!] " + texto)

def mostrar_dinero(valor):
    """Devuelve el valor formateado como $X.XX sin imports."""
    entero   = int(valor)
    centavos = int(valor * 100) - entero * 100
    if centavos < 10:
        return "$ " + str(entero) + ".0" + str(centavos)
    return "$ " + str(entero) + "." + str(centavos)

def titulo(texto):
    """Muestra un bloque de título con líneas dobles."""
    print()
    linea_doble()
    print("  " + texto)
    linea_doble()


# ============================================================
# FUNCIONES AUXILIARES DE LÓGICA
# ============================================================

def validar_cedula(cedula):
    """Retorna True si la cedula tiene exactamente 10 digitos numericos."""
    if len(cedula) != 10:
        return False
    for caracter in cedula:
        if caracter < "0" or caracter > "9":
            return False
    return True


def pedir_cedula(mensaje):
    """
    Muestra el formato esperado antes de pedir la cedula.
    Repite hasta recibir una cedula valida o 'salir'.
    Retorna la cedula o None si el usuario escribe 'salir'.
    """
    print("  (Ingrese 10 digitos numericos, o escriba 'salir' para cancelar)")
    while True:
        cedula = input("  " + mensaje).strip()
        if cedula.lower() == "salir":
            return None
        if not validar_cedula(cedula):
            mensaje_error("La cedula debe tener exactamente 10 digitos numericos.")
            print("  Ejemplo valido: 1234567890")
            continue
        return cedula


def pedir_si_no(mensaje):
    """
    Pide S o N. Muestra el formato esperado si la respuesta no es valida.
    Retorna 'S' o 'N'. Escribe 'salir' para cancelar y retorna None.
    """
    while True:
        respuesta = input("  " + mensaje + " (S/N, o 'salir' para cancelar): ").strip().upper()
        if respuesta == "SALIR":
            return None
        if respuesta == "S" or respuesta == "N":
            return respuesta
        mensaje_error("Respuesta no valida. Ingrese S para si o N para no.")


def verificar_clave():
    """
    Pide la clave de administrador con maximo 3 intentos.
    Retorna True si es correcta, False si falla.
    """
    print("  (Tiene 3 intentos para ingresar la contrasena)")
    intentos = 0
    while intentos < 3:
        clave = input("  Contrasena de administrador: ").strip()
        if clave == CLAVE_ADMIN:
            return True
        intentos = intentos + 1
        restantes = 3 - intentos
        if restantes > 0:
            mensaje_error("Contrasena incorrecta. Puede intentarlo " + str(restantes) + " vez/veces mas.")
        else:
            mensaje_error("Contrasena incorrecta.")
    print()
    mensaje_error("Acceso bloqueado por demasiados intentos fallidos.")
    print("  Contacte al administrador del sistema si necesita ayuda.")
    return False


def buscar_persona(cedula):
    """Busca en personas por cedula. Retorna el diccionario o None."""
    for persona in personas:
        if persona["cedula"] == cedula:
            return persona
    return None


def ya_comio_hoy(cedula):
    """Retorna True si la cedula ya tiene un consumo registrado hoy."""
    for consumo in consumos_dia:
        if consumo["cedula"] == cedula:
            return True
    return False


def calcular_total(sopa, segundo, jugo):
    """Calcula el total segun los componentes elegidos."""
    total = 0.0
    if sopa:
        total = total + PRECIO_SOPA
    if segundo:
        total = total + PRECIO_SEGUNDO
    if jugo:
        total = total + PRECIO_JUGO
    return total


def contar_consumos_dia():
    """Retorna cuantos consumos hay registrados hoy."""
    return len(consumos_dia)


def contar_consumos_mes():
    """Retorna cuantos consumos hay acumulados en el mes."""
    return len(consumos_mes)


# ============================================================
# MÓDULO ADMINISTRADOR
# ============================================================

def registrar_persona():
    """Permite al administrador agregar una nueva persona al sistema."""
    titulo("REGISTRAR NUEVA PERSONA")
    print("  (Escriba 'salir' en cualquier campo para cancelar)")
    print()

    # Pedir cedula
    cedula = pedir_cedula("Cedula: ")
    if cedula is None:
        mensaje_aviso("Registro cancelado.")
        return

    if buscar_persona(cedula) is not None:
        mensaje_error("Ya existe una persona registrada con la cedula " + cedula + ".")
        print("  Si necesita modificar sus datos, consulte con el administrador del sistema.")
        return

    # Pedir nombre
    print("  (Solo letras y espacios)")
    while True:
        nombre = input("  Nombre completo: ").strip()
        if nombre.lower() == "salir":
            mensaje_aviso("Registro cancelado.")
            return
        if len(nombre) < 3:
            mensaje_error("El nombre es demasiado corto. Ingrese el nombre completo.")
            continue
        valido = True
        for c in nombre:
            if not (c.isalpha() or c == " "):
                valido = False
                break
        if not valido:
            mensaje_error("El nombre solo puede contener letras y espacios.")
            continue
        break

    # Pedir empresa
    while True:
        empresa = input("  Empresa a la que pertenece: ").strip()
        if empresa.lower() == "salir":
            mensaje_aviso("Registro cancelado.")
            return
        if len(empresa) < 2:
            mensaje_error("El nombre de la empresa es demasiado corto.")
            continue
        break

    # Confirmar antes de guardar
    print()
    linea_simple()
    print("  Confirme los datos antes de guardar:")
    print("  Cedula  : " + cedula)
    print("  Nombre  : " + nombre)
    print("  Empresa : " + empresa)
    linea_simple()

    confirmacion = pedir_si_no("Desea guardar esta persona")
    if confirmacion is None or confirmacion == "N":
        mensaje_aviso("Registro cancelado. No se guardaron cambios.")
        return

    personas.append({
        "cedula":  cedula,
        "nombre":  nombre,
        "empresa": empresa
    })

    print()
    mensaje_ok("Persona registrada exitosamente en el sistema.")


def ver_personas():
    """Muestra la lista completa de personas registradas."""
    titulo("PERSONAS REGISTRADAS EN EL SISTEMA")
    print("  Total: " + str(len(personas)) + " persona(s)")
    print()
    print("  N    Cedula         Nombre                    Empresa")
    linea_simple()
    numero = 1
    for persona in personas:
        print("  " + str(numero).ljust(4) +
              " " + persona["cedula"] +
              "     " + persona["nombre"].ljust(25) +
              " " + persona["empresa"])
        numero = numero + 1


def menu_administrador():
    """Modulo de administracion: requiere contrasena."""
    titulo("MODULO ADMINISTRADOR")

    if not verificar_clave():
        return

    mensaje_ok("Acceso concedido. Bienvenido, administrador.")

    while True:
        print()
        linea_simple()
        print("  MENU ADMINISTRADOR")
        linea_simple()
        print("  1. Registrar nueva persona")
        print("  2. Ver personas registradas")
        print("  3. Volver al menu principal")
        linea_simple()

        opcion = input("  Que desea hacer? Ingrese el numero: ").strip()

        if opcion == "1":
            registrar_persona()
        elif opcion == "2":
            ver_personas()
        elif opcion == "3":
            mensaje_aviso("Saliendo del modulo administrador...")
            break
        else:
            mensaje_error("Opcion no valida. Ingrese 1, 2 o 3.")


# ============================================================
# MÓDULO USUARIO
# ============================================================

def menu_usuario():
    """Modulo de usuario: valida cedula y registra consumo del dia."""
    titulo("SERVICIO DE ALMUERZO")

    # Pedir cedula con instrucciones claras
    cedula = pedir_cedula("Ingrese su numero de cedula: ")
    if cedula is None:
        mensaje_aviso("Operacion cancelada.")
        return

    persona = buscar_persona(cedula)
    if persona is None:
        print()
        mensaje_error("Su cedula no esta registrada en el sistema.")
        print("  Cedula ingresada: " + cedula)
        print("  Si cree que es un error, consulte con el administrador")
        print("  para que lo registren antes de volver a intentarlo.")
        return

    print()
    mensaje_ok("Identidad verificada.")
    print("  Bienvenido/a, " + persona["nombre"])
    print("  Empresa      : " + persona["empresa"])

    if ya_comio_hoy(cedula):
        print()
        mensaje_aviso("Usted ya registro su almuerzo el dia de hoy.")
        print("  Solo se permite un almuerzo por persona por dia.")
        print("  Si tiene algun problema, consulte con el administrador.")
        return

    # Mostrar precios antes de pedir seleccion
    print()
    linea_simple()
    print("  COMPONENTES DISPONIBLES HOY")
    linea_simple()
    print("  Sopa    ->  " + mostrar_dinero(PRECIO_SOPA))
    print("  Segundo ->  " + mostrar_dinero(PRECIO_SEGUNDO))
    print("  Jugo    ->  " + mostrar_dinero(PRECIO_JUGO))
    linea_simple()
    print("  Seleccione los componentes que desea.")
    print("  Puede elegir uno, varios o todos.")
    print()

    # Seleccion con confirmacion inmediata por componente
    respuesta_sopa = pedir_si_no("Desea sopa")
    if respuesta_sopa is None:
        mensaje_aviso("Pedido cancelado. No se registro ningun consumo.")
        return
    if respuesta_sopa == "S":
        mensaje_ok("Sopa agregada a su pedido  ->  " + mostrar_dinero(PRECIO_SOPA))
    else:
        mensaje_aviso("Sopa no seleccionada.")

    respuesta_segundo = pedir_si_no("Desea segundo")
    if respuesta_segundo is None:
        mensaje_aviso("Pedido cancelado. No se registro ningun consumo.")
        return
    if respuesta_segundo == "S":
        mensaje_ok("Segundo agregado a su pedido  ->  " + mostrar_dinero(PRECIO_SEGUNDO))
    else:
        mensaje_aviso("Segundo no seleccionado.")

    respuesta_jugo = pedir_si_no("Desea jugo")
    if respuesta_jugo is None:
        mensaje_aviso("Pedido cancelado. No se registro ningun consumo.")
        return
    if respuesta_jugo == "S":
        mensaje_ok("Jugo agregado a su pedido  ->  " + mostrar_dinero(PRECIO_JUGO))
    else:
        mensaje_aviso("Jugo no seleccionado.")

    sopa    = respuesta_sopa    == "S"
    segundo = respuesta_segundo == "S"
    jugo    = respuesta_jugo    == "S"

    if not sopa and not segundo and not jugo:
        print()
        mensaje_aviso("No selecciono ningun componente.")
        print("  No se registro ningun consumo.")
        print("  Puede volver al menu principal y empezar de nuevo.")
        return

    total = calcular_total(sopa, segundo, jugo)

    # Confirmacion del pedido antes de registrar
    print()
    linea_simple()
    print("  RESUMEN DE SU PEDIDO")
    linea_simple()
    if sopa:
        print("  Sopa     " + mostrar_dinero(PRECIO_SOPA))
    if segundo:
        print("  Segundo  " + mostrar_dinero(PRECIO_SEGUNDO))
    if jugo:
        print("  Jugo     " + mostrar_dinero(PRECIO_JUGO))
    linea_simple()
    print("  TOTAL    " + mostrar_dinero(total))
    linea_simple()

    confirmacion = pedir_si_no("Confirma este pedido")
    if confirmacion is None or confirmacion == "N":
        mensaje_aviso("Pedido cancelado. No se registro ningun consumo.")
        print("  Puede volver al menu principal y empezar de nuevo.")
        return

    # Guardar consumo
    consumo = {
        "cedula":  cedula,
        "nombre":  persona["nombre"],
        "empresa": persona["empresa"],
        "sopa":    sopa,
        "segundo": segundo,
        "jugo":    jugo,
        "total":   total
    }
    consumos_dia.append(consumo)
    consumos_mes.append(consumo)

    print()
    mensaje_ok("Pedido registrado exitosamente.")
    print("  Total a pagar: " + mostrar_dinero(total))
    print("  Buen provecho, " + persona["nombre"] + "!")


# ============================================================
# MÓDULO REPORTES
# ============================================================

def reporte_dia():
    """Muestra el resumen de consumos del dia actual."""
    titulo("RESUMEN DEL DIA")

    if len(consumos_dia) == 0:
        mensaje_aviso("No hay consumos registrados hoy todavia.")
        return

    total_dia      = 0.0
    total_sopas    = 0
    total_segundos = 0
    total_jugos    = 0

    print("  Cedula         Nombre                   Sopa  2do  Jugo  Total")
    linea_simple()

    for consumo in consumos_dia:
        s = "Si" if consumo["sopa"]    else "No"
        g = "Si" if consumo["segundo"] else "No"
        j = "Si" if consumo["jugo"]    else "No"

        print("  " +
              consumo["cedula"] + "     " +
              consumo["nombre"].ljust(22) + " " +
              s.ljust(5) + " " +
              g.ljust(4) + " " +
              j.ljust(5) + " " +
              mostrar_dinero(consumo["total"]))

        total_dia      = total_dia + consumo["total"]
        total_sopas    = total_sopas    + (1 if consumo["sopa"]    else 0)
        total_segundos = total_segundos + (1 if consumo["segundo"] else 0)
        total_jugos    = total_jugos    + (1 if consumo["jugo"]    else 0)

    linea_simple()
    print()
    print("  Personas atendidas : " + str(len(consumos_dia)))
    print("  Sopas servidas     : " + str(total_sopas))
    print("  Segundos servidos  : " + str(total_segundos))
    print("  Jugos servidos     : " + str(total_jugos))
    print()
    print("  TOTAL DEL DIA      : " + mostrar_dinero(total_dia))


def reporte_mes():
    """Muestra el resumen acumulado del mes con totales por persona."""
    titulo("RESUMEN DEL MES")

    if len(consumos_mes) == 0:
        mensaje_aviso("No hay consumos registrados en el mes todavia.")
        return

    resumen = []

    for consumo in consumos_mes:
        cedula = consumo["cedula"]
        encontrado = False
        for fila in resumen:
            if fila["cedula"] == cedula:
                fila["cantidad"] = fila["cantidad"] + 1
                fila["total"]    = fila["total"] + consumo["total"]
                encontrado = True
                break
        if not encontrado:
            resumen.append({
                "cedula":   cedula,
                "nombre":   consumo["nombre"],
                "empresa":  consumo["empresa"],
                "cantidad": 1,
                "total":    consumo["total"]
            })

    print("  Cedula         Nombre                   Empresa     Almuerzos  Total")
    linea_simple()

    total_mes = 0.0
    for fila in resumen:
        print("  " +
              fila["cedula"] + "     " +
              fila["nombre"].ljust(22)  + " " +
              fila["empresa"].ljust(11) + " " +
              str(fila["cantidad"]).ljust(10) + " " +
              mostrar_dinero(fila["total"]))
        total_mes = total_mes + fila["total"]

    linea_simple()
    print()
    print("  Registros en el mes  : " + str(len(consumos_mes)))
    print("  Personas distintas   : " + str(len(resumen)))
    print()
    print("  TOTAL DEL MES        : " + mostrar_dinero(total_mes))


def cerrar_dia():
    """Limpia los consumos del dia. Los del mes se conservan."""
    titulo("CERRAR DIA")

    if len(consumos_dia) == 0:
        mensaje_aviso("No hay consumos del dia para cerrar.")
        return

    print("  Esta accion borrara los registros del dia.")
    print("  Los consumos del mes NO se veran afectados.")
    print("  Registros actuales del dia: " + str(len(consumos_dia)))
    print()

    confirmacion = pedir_si_no("Esta seguro que desea cerrar el dia")
    if confirmacion is None or confirmacion == "N":
        mensaje_aviso("Operacion cancelada. No se hicieron cambios.")
        return

    while len(consumos_dia) > 0:
        consumos_dia.pop()

    print()
    mensaje_ok("Dia cerrado correctamente.")
    print("  Los consumos quedaron guardados en el reporte mensual.")


def reporte_por_empresa():
    """Muestra el resumen del mes agrupado por empresa: almuerzos y total a cobrar."""
    titulo("RESUMEN POR EMPRESA")

    if len(consumos_mes) == 0:
        mensaje_aviso("No hay consumos registrados en el mes todavia.")
        return

    # Construir resumen agrupado por empresa
    resumen = []

    for consumo in consumos_mes:
        empresa = consumo["empresa"]
        encontrado = False
        for fila in resumen:
            if fila["empresa"] == empresa:
                fila["almuerzos"] = fila["almuerzos"] + 1
                fila["sopas"]     = fila["sopas"]     + (1 if consumo["sopa"]    else 0)
                fila["segundos"]  = fila["segundos"]  + (1 if consumo["segundo"] else 0)
                fila["jugos"]     = fila["jugos"]     + (1 if consumo["jugo"]    else 0)
                fila["total"]     = fila["total"]     + consumo["total"]
                encontrado = True
                break
        if not encontrado:
            resumen.append({
                "empresa":   empresa,
                "almuerzos": 1,
                "sopas":     1 if consumo["sopa"]    else 0,
                "segundos":  1 if consumo["segundo"] else 0,
                "jugos":     1 if consumo["jugo"]    else 0,
                "total":     consumo["total"]
            })

    print("  Empresa          Almuerzos  Sopas  Segundos  Jugos  Total a cobrar")
    linea_simple()

    total_general    = 0.0
    total_almuerzos  = 0
    total_sopas      = 0
    total_segundos   = 0
    total_jugos      = 0

    for fila in resumen:
        print("  " +
              fila["empresa"].ljust(16) + " " +
              str(fila["almuerzos"]).ljust(10) + " " +
              str(fila["sopas"]).ljust(6) + " " +
              str(fila["segundos"]).ljust(9) + " " +
              str(fila["jugos"]).ljust(6) + " " +
              mostrar_dinero(fila["total"]))

        total_general   = total_general   + fila["total"]
        total_almuerzos = total_almuerzos + fila["almuerzos"]
        total_sopas     = total_sopas     + fila["sopas"]
        total_segundos  = total_segundos  + fila["segundos"]
        total_jugos     = total_jugos     + fila["jugos"]

    linea_simple()
    print("  " +
          "TOTALES".ljust(16) + " " +
          str(total_almuerzos).ljust(10) + " " +
          str(total_sopas).ljust(6) + " " +
          str(total_segundos).ljust(9) + " " +
          str(total_jugos).ljust(6) + " " +
          mostrar_dinero(total_general))
    print()
    print("  Empresas registradas : " + str(len(resumen)))
    print("  TOTAL GENERAL A COBRAR: " + mostrar_dinero(total_general))


def menu_reportes():
    """Modulo de reportes: requiere contrasena."""
    titulo("MODULO DE REPORTES")

    if not verificar_clave():
        return

    mensaje_ok("Acceso concedido.")

    while True:
        # Mostrar cuantos registros hay antes de entrar a cada reporte
        registros_dia = contar_consumos_dia()
        registros_mes = contar_consumos_mes()

        print()
        linea_simple()
        print("  MENU DE REPORTES")
        linea_simple()
        print("  1. Resumen del dia            (" + str(registros_dia) + " consumo(s) registrado(s))")
        print("  2. Resumen del mes por persona (" + str(registros_mes) + " consumo(s) acumulado(s))")
        print("  3. Resumen del mes por empresa")
        print("  4. Cerrar el dia")
        print("  5. Volver al menu principal")
        linea_simple()

        opcion = input("  Que desea hacer? Ingrese el numero: ").strip()

        if opcion == "1":
            reporte_dia()
        elif opcion == "2":
            reporte_mes()
        elif opcion == "3":
            reporte_por_empresa()
        elif opcion == "4":
            cerrar_dia()
        elif opcion == "5":
            mensaje_aviso("Saliendo del modulo de reportes...")
            break
        else:
            mensaje_error("Opcion no valida. Ingrese un numero del 1 al 5.")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

while True:
    print()
    linea_doble()
    print("    SISTEMA DE CONTROL DE ALMUERZOS")
    linea_doble()
    print("  Que desea hacer?")
    print()
    print("  1. Quiero pedir mi almuerzo")
    print("  2. Administrar personas del sistema")
    print("  3. Ver reportes del dia y del mes")
    print("  4. Salir del sistema")
    linea_doble()

    opcion = input("  Ingrese el numero de su opcion: ").strip()

    if opcion == "1":
        menu_usuario()
    elif opcion == "2":
        menu_administrador()
    elif opcion == "3":
        menu_reportes()
    elif opcion == "4":
        print()
        linea_doble()
        mensaje_ok("Sistema cerrado. Hasta luego.")
        linea_doble()
        break
    else:
        mensaje_error("Opcion no valida. Ingrese un numero del 1 al 4.")
