test_settings = {
    "tema": "Oscuro",
    "notificaciones": "Desactivado",
    "volumen": "Bajo",
}

def add_setting(cfg,par):
    clave, valor = par
    clave = clave.lower()
    valor = valor.lower()

    if clave in cfg:
        return f"Setting '{clave}' already exists! Cannot add a new setting with this name."
    cfg[clave] = valor
    return f"Setting '{clave}' added with value '{valor}' successfully!"

def update_setting(cfg,par):
    clave, valor = par
    clave = clave.lower()
    valor = valor.lower()

    if clave in cfg:
     cfg[clave] = valor
     return f"Setting '{clave}' updated to '{valor}' successfully!"

    else:
      return f"Setting '{clave}' does not exist! Cannot update a non-existing setting."

def delete_setting(cfg, clave):
    clave = clave.lower()

    if clave in cfg:
        del cfg[clave]
        return f"Setting '{clave}' deleted successfully!"
    else:
        return ("Setting not found!")

def view_settings(cfg):
    if len(cfg) == 0:
        return ("No settings available.")

    resultado = "Current User Settings:\n"

    for clave, valor in cfg.items():
         resultado += f"{clave.capitalize()}: {valor}\n"
    return resultado