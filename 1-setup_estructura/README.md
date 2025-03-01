# Project Setup Scripts

Este repositorio contiene scripts diseñados para **crear estructuras de proyectos** de manera automática en varios lenguajes de programación, como Python, JavaScript y C++. 

## Características

- Te permite **seleccionar el lenguaje** que estás aprendiendo.
- Crea **carpetas organizadas** por temas (fundamentos, intermedio, avanzado, proyectos).
- Genera **archivos predeterminados** con código base para empezar a trabajar.
- Guarda la estructura en la **ubicación que elijas**.
- Usa un **archivo de configuración (`config.json`)** para personalizar la estructura sin modificar el código.

## Requisitos Previos

Antes de ejecutar el script, necesitas instalar Python y configurar tu entorno de desarrollo.

1. **Verifica que Python está en el PATH:**

   Asegúrate de tener Python y `pip` correctamente instalados en tu sistema con los siguientes comandos:
 
   python --version
   pip --version

2. **Si Tkinter no funciona, instálalo:**

   Si no tienes Tkinter instalado, puedes instalarlo con:
 
    pip install tk

3. **(Opcional) Instala ttkbootstrap para un mejor diseño:**

   Si deseas un diseño más atractivo en la interfaz gráfica, puedes instalar ttkbootstrap con: 
 
   pip install ttkbootstrap


4. **Prueba Tkinter en Python:**

   Para confirmar que Tkinter está correctamente instalado, ejecuta lo siguiente en Python:
   
    import tkinter
    print("Tkinter está instalado correctamente")

--------------------------------------------------------------------------------
### Personalización
Si quieres personalizar la estructura de los proyectos para otros lenguajes o agregar más carpetas y archivos, puedes editar el archivo config.json. El formato es fácil de entender y modificar.

--------------------------------------------------------------------------------
Si piensas mejorar el script o agregar más funcionalidades, siéntete libre de hacer un fork del repositorio y enviar un pull request.



