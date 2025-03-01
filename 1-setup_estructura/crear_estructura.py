import os
import json
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox

#   Archivo de configuración
config_file = "config.json"

#   Estructura predeterminada del JSON
default_config = {
    "lenguajes": {
        "Python": {
            "carpetas": [
                "01-Introduccion",
                "02-Fundamentos",
                "03-Manejo-de-Datos",
                "04-Estructuras-de-Control",
                "05-Manejo-de-Archivos",
                "06-Manejo-de-Errores-y-Modulos",
                "07-Expresiones-Regulares",
                "08-Proyectos-Pequeños",
                "09-Proyectos-Grandes"
            ],
            "archivos": {
                "01-Introduccion": ["README.md", "instalacion_python.md", "primer_hola_mundo.py"],
                "02-Fundamentos": ["01-variables.py", "02-operadores_aritmeticos.py", "03-operadores_comparacion.py",
                                   "04-operadores_logicos.py", "05-condicionales.py", "README.md"],
                "03-Manejo-de-Datos": ["01-metodos_cadenas.py", "02-metodos_listas.py", "03-metodos_diccionarios.py",
                                       "04-entrada_datos.py", "README.md"],
                "04-Estructuras-de-Control": ["01-bucles_for.py", "02-bucles_while.py", "03-funciones.py",
                                              "04-funciones_lambda.py", "README.md"],
                "05-Manejo-de-Archivos": ["01-archivos_txt.py", "02-archivos_csv.py", "README.md"],
                "06-Manejo-de-Errores-y-Modulos": ["01-modulos.py", "02-excepciones.py", "README.md"],
                "07-Expresiones-Regulares": ["01-expresiones_regulares.py", "README.md"],
                "08-Proyectos-Pequeños": ["01-calculadora.py", "02-gestor_tareas.py", "README.md"],
                "09-Proyectos-Grandes": ["README.md"]
            }
        },
        "JavaScript": {
            "carpetas": [
                "01-Introduccion",
                "02-Sintaxis-Basica",
                "03-DOM",
                "04-Eventos",
                "05-Funciones",
                "06-Objetos",
                "07-ES6+",
                "08-Proyectos-Pequeños",
                "09-Proyectos-Grandes"
            ],
            "archivos": {
                "01-Introduccion": ["README.md", "instalacion_javascript.md", "primer_hola_mundo.js"],
                "02-Sintaxis-Basica": ["01-variables.js", "02-operadores.js", "03-condicionales.js", "README.md"],
                "03-DOM": ["01-manipulacion_DOM.js", "README.md"],
                "04-Eventos": ["01-eventos.js", "README.md"],
                "05-Funciones": ["01-funciones.js", "README.md"],
                "06-Objetos": ["01-objetos.js", "README.md"],
                "07-ES6+": ["01-arrow_functions.js", "02-promesas.js", "README.md"],
                "08-Proyectos-Pequeños": ["01-calculadora.js", "02-to_do_list.js", "README.md"],
                "09-Proyectos-Grandes": ["README.md"]
            }
        },
        "C++": {
            "carpetas": [
                "01-Introduccion",
                "02-Sintaxis-Basica",
                "03-Estructuras-de-Control",
                "04-Funciones",
                "05-POO",
                "06-Manipulacion-de-Archivos",
                "07-Proyectos-Pequeños",
                "08-Proyectos-Grandes"
            ],
            "archivos": {
                "01-Introduccion": ["README.md", "instalacion_cpp.md", "primer_hola_mundo.cpp"],
                "02-Sintaxis-Basica": ["01-variables.cpp", "02-operadores.cpp", "03-condicionales.cpp", "README.md"],
                "03-Estructuras-de-Control": ["01-bucles.cpp", "README.md"],
                "04-Funciones": ["01-funciones.cpp", "README.md"],
                "05-POO": ["01-clases.cpp", "02-herencia.cpp", "README.md"],
                "06-Manipulacion-de-Archivos": ["01-archivos_txt.cpp", "README.md"],
                "07-Proyectos-Pequeños": ["01-calculadora.cpp", "02-gestor_tareas.cpp", "README.md"],
                "08-Proyectos-Grandes": ["README.md"]
            }
        }
    }
}

#   Cargar configuración o crear `config.json` con valores predeterminados
def cargar_config():
    if not os.path.exists(config_file):  #  Si el archivo no existe, se crea con valores por defecto
        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=4)
        return default_config
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:  #  Si está corrupto, lo reinicia
        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=4)
        return default_config

config = cargar_config()

#   Guardar configuración en `config.json`
def guardar_config():
    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

#   Actualizar lista de carpetas cuando cambia el lenguaje
def actualizar_carpetas(event):
    lenguaje = combo_lenguajes.get()
    if lenguaje in config["lenguajes"]:
        carpetas = config["lenguajes"][lenguaje]["carpetas"]
        combo_carpetas["values"] = carpetas
        combo_carpetas.set("Seleccione una carpeta")

#   Habilitar o deshabilitar el combo de carpetas según el tipo
def actualizar_tipo(event):
    tipo = combo_tipo.get()
    if tipo == "Archivo":
        combo_carpetas["state"] = "readonly"
        actualizar_carpetas(None)  # Actualiza las carpetas si el usuario selecciona "Archivo"
    else:
        combo_carpetas["state"] = "disabled"
        combo_carpetas.set("No requerido")

#   Mostrar estructura en Treeview
def mostrar_estructura():
    tree.delete(*tree.get_children())  # Limpiar árbol
    for lenguaje, datos in config["lenguajes"].items():
        lang_node = tree.insert("", "end", text=lenguaje, open=True)
        for carpeta in datos["carpetas"]:
            carpeta_node = tree.insert(lang_node, "end", text=carpeta, open=True)
            for archivo in datos["archivos"].get(carpeta, []):
                tree.insert(carpeta_node, "end", text=archivo)

#   Agregar nuevo lenguaje
def agregar_lenguaje():
    nombre = entry_nuevo_lenguaje.get().strip().capitalize()
    if not nombre or nombre in config["lenguajes"]:
        messagebox.showwarning("Error", "Ingrese un nombre válido o que no exista.")
        return

    config["lenguajes"][nombre] = {"carpetas": ["01-Introduccion"], "archivos": {"01-Introduccion": ["README.md"]}}
    guardar_config()
    entry_nuevo_lenguaje.delete(0, "end")
    combo_lenguajes["values"] = list(config["lenguajes"].keys())  # Actualizar menú de lenguajes
    mostrar_estructura()
    messagebox.showinfo("Éxito", f"Lenguaje '{nombre}' agregado.")

#   Agregar carpeta o archivo
def agregar_elemento():
    lenguaje = combo_lenguajes.get()
    if lenguaje not in config["lenguajes"]:
        messagebox.showwarning("Error", "Seleccione un lenguaje válido.")
        return

    tipo = combo_tipo.get()
    nombre = entry_elemento.get().strip().capitalize()
    if not nombre:
        messagebox.showwarning("Error", "Ingrese un nombre válido.")
        return

    if tipo == "Carpeta":
        if nombre in config["lenguajes"][lenguaje]["carpetas"]:
            messagebox.showwarning("Error", "La carpeta ya existe.")
            return
        config["lenguajes"][lenguaje]["carpetas"].append(nombre)
        config["lenguajes"][lenguaje]["archivos"][nombre] = []
    else:  # Si es un Archivo
        carpeta = combo_carpetas.get()
        if carpeta not in config["lenguajes"][lenguaje]["carpetas"]:
            messagebox.showwarning("Error", "Seleccione una carpeta válida.")
            return
        if nombre in config["lenguajes"][lenguaje]["archivos"][carpeta]:
            messagebox.showwarning("Error", "El archivo ya existe.")
            return
        config["lenguajes"][lenguaje]["archivos"][carpeta].append(nombre)

    guardar_config()
    entry_elemento.delete(0, "end")
    mostrar_estructura()
    messagebox.showinfo("Éxito", f"{tipo} '{nombre}' agregado.")

#   Crear estructura de archivos
def crear_estructura():
    lenguaje = combo_lenguajes.get()
    if lenguaje not in config["lenguajes"]:
        messagebox.showwarning("Error", "Seleccione un lenguaje válido.")
        return

    ruta_base = filedialog.askdirectory(title="Seleccione la ubicación") or os.getcwd()
    ruta_principal = os.path.join(ruta_base, lenguaje)
    os.makedirs(ruta_principal, exist_ok=True)

    estructura = config["lenguajes"][lenguaje]
    for carpeta in estructura["carpetas"]:
        ruta_carpeta = os.path.join(ruta_principal, carpeta)
        os.makedirs(ruta_carpeta, exist_ok=True)

        for archivo in estructura["archivos"].get(carpeta, []):
            ruta_archivo = os.path.join(ruta_carpeta, archivo)
            with open(ruta_archivo, "w", encoding="utf-8") as f:
                f.write(f"# {archivo}\n# Descripción: Añade aquí una breve descripción.\n\n")

    messagebox.showinfo("Éxito", f"Estructura de {lenguaje} creada en {ruta_principal}.")

#   Interfaz gráfica moderna
root = ttk.Window(themename="cyborg")  # Tema oscuro y moderno
root.title("Gestor de Estructuras")
root.geometry("900x500")

#   Sección de agregar lenguaje
frame_lenguaje = ttk.LabelFrame(root, text="Agregar Lenguaje", bootstyle="primary")
frame_lenguaje.pack(pady=10, padx=10, fill="x")

entry_nuevo_lenguaje = ttk.Entry(frame_lenguaje, width=30)
entry_nuevo_lenguaje.pack(side="left", padx=5, pady=5)
btn_agregar_lenguaje = ttk.Button(frame_lenguaje, text="Agregar", bootstyle="success", command=agregar_lenguaje)
btn_agregar_lenguaje.pack(side="left", padx=5, pady=5)

#   Sección de agregar carpetas/archivos
frame_estructura = ttk.LabelFrame(root, text="Modificar Estructura", bootstyle="secondary")
frame_estructura.pack(pady=10, padx=10, fill="x")

combo_lenguajes = ttk.Combobox(frame_estructura, values=list(config["lenguajes"].keys()), state="readonly")
combo_lenguajes.set("Seleccione un lenguaje")
combo_lenguajes.pack(side="left", padx=5, pady=5)
combo_lenguajes.bind("<<ComboboxSelected>>", actualizar_carpetas)

combo_tipo = ttk.Combobox(frame_estructura, values=["Carpeta", "Archivo"], state="readonly")
combo_tipo.set("Seleccione tipo")
combo_tipo.pack(side="left", padx=5, pady=5)
combo_tipo.bind("<<ComboboxSelected>>", actualizar_tipo)  # 🟢 Se actualiza cuando el usuario selecciona "Archivo"

combo_carpetas = ttk.Combobox(frame_estructura, state="disabled")
combo_carpetas.set("No requerido")
combo_carpetas.pack(side="left", padx=5, pady=5)

entry_elemento = ttk.Entry(frame_estructura, width=20)
entry_elemento.pack(side="left", padx=5, pady=5)

btn_agregar_elemento = ttk.Button(frame_estructura, text="Agregar", bootstyle="success", command=agregar_elemento)
btn_agregar_elemento.pack(side="left", padx=5, pady=5)

#   Árbol de estructura
tree = ttk.Treeview(root)
tree.pack(pady=10, padx=10, fill="both", expand=True)

#   Botón para crear estructura
btn_crear = ttk.Button(root, text="Crear Estructura", bootstyle="success", command=crear_estructura)
btn_crear.pack(pady=10)

#   Cargar la estructura inicial
mostrar_estructura()

root.mainloop()
