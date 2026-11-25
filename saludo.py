def saludar(nombre):
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")

    return f"Hola, {nombre}!"


print(saludar("GitHub"))
