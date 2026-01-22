# ProyectoCompis - Agenda

Proyecto base (Fase 1): estructura del proyecto + menú de consola mínimo.

## Ejecutar
Desde la raíz:

```bash
python -m src.main

Agenda de Contactos en Python


Este proyecto es una agenda de contactos en consola desarrollada en Python.
Permite al usuario guardar, ver y buscar contactos de manera sencilla usando un menú interactivo.
Cada contacto contiene:

* Nombre
* Correo electrónico
* Número de teléfono

El programa valida que los datos ingresados sean correctos antes de guardarlos.

## Funcionalidades

El programa ofrece las siguientes opciones:

1. **Agregar contacto**
2. **Listar contactos**
3. **Buscar contacto**
4. **Salir**

### Inicio del programa

El archivo `main.py` es el punto de inicio.
Este archivo crea la agenda y muestra el menú principal, el cual se repite hasta que el usuario decide salir.

### Agregar contacto

El usuario debe ingresar:

* **Nombre** (no puede estar vacío)
* **Correo electrónico** (debe tener un formato válido, por ejemplo: [usuario@dominio.com](mailto:usuario@dominio.com))
* **Teléfono** (debe tener exactamente 8 números)

Si el correo o el teléfono no cumplen con el formato correcto, el programa vuelve a pedir el dato.

Una vez que los datos son válidos, el contacto se guarda en la agenda.

### Listar contactos

Muestra todos los contactos guardados en la agenda con el siguiente formato:

`Nombre | Correo | Teléfono`

Si no hay contactos registrados, el programa lo indica.


### Buscar contacto

Permite buscar contactos escribiendo:

* parte del **nombre**
* parte del **correo**
* o el **teléfono**

La búsqueda es **parcial**, lo que significa que no es necesario escribir el dato completo.
Por ejemplo, al buscar “ana” se pueden encontrar contactos como “Ana”, “Anabella” o “Mariana”.

Si hay varios contactos que coinciden con la búsqueda, se muestran todos.


### Validaciones

El programa valida los datos ingresados:

* El correo debe tener un formato válido.
* El teléfono debe tener exactamente 8 dígitos numéricos.
* No se permiten entradas vacías.





