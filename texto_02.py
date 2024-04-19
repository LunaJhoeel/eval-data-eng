def extraer_informacion(correo):
    """
    Funcion que recibe un correo electrónico y devuelve
    el nombre del usuario y el nombre del dominio

    :param email: str,correo electrónico
    :return: tuple, (nombre_usuario, nombre_dominio)
    """
    # convierte el input a string si es posible
    try:
        correo_str = str(correo)
    except Exception as e:
        raise ValueError(f"No se puede convertir el input a string: {e}")

    # verifica que el correo tiene exactamente un '@'
    if correo_str.count('@') != 1:
        raise ValueError("El correo proporcionado no es válido.")

    # divide el correo
    partes = correo_str.split('@')

    # extrae nombre de usuario y dominio
    nombre_usuario, nombre_dominio = partes
    return nombre_usuario, nombre_dominio

# uso
email = "nombre.apellido@gmail.com"
usuario, dominio = extraer_informacion(email)

print("Nombre de usuario:", usuario)
print("Nombre de dominio:", dominio)
