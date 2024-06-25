import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

#funciones para manejar archivos JSON
def abrir_archivo(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def crear_archivo(ruta):
    if os.path.exists(ruta):
        return
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump([], archivo)

def escribir_archivo(ruta, datos):
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4)

#funciones para clientes
def listar_clientes():
    clientes = abrir_archivo(clientes_json)
    if not clientes:
        messagebox.showinfo("Información", "No hay clientes en la base de datos.")
    else:
        mostrar_lista(clientes, "Clientes")

def agregar_cliente():
    clientes = abrir_archivo(clientes_json)
    nombre = simpledialog.askstring("Nombre", "Ingrese Nombre:")
    apellido = simpledialog.askstring("Apellido", "Ingrese Apellido:")
    documento = simpledialog.askstring("Documento", "Ingrese Documento:")
    direccion = simpledialog.askstring("Dirección", "Ingrese Dirección:")
    telefono = simpledialog.askstring("Teléfono", "Ingrese Teléfono:")
    correo_electronico = simpledialog.askstring("Correo Electrónico", "Ingrese Correo Electrónico:")
    
    cliente = {
        'id_cliente': len(clientes) + 1,
        'nombre': nombre,
        'apellido': apellido,
        'documento': documento,
        'direccion': direccion,
        'telefono': telefono,
        'correo_electronico': correo_electronico
    }
    
    clientes.append(cliente)
    escribir_archivo(clientes_json, clientes)

def eliminar_cliente():
    clientes = abrir_archivo(clientes_json)
    documento = simpledialog.askstring("Documento", "Ingrese el documento del cliente a eliminar:")
    clientes = [cliente for cliente in clientes if cliente['documento'] != documento]
    escribir_archivo(clientes_json, clientes)

def buscar_cliente():
    clientes = abrir_archivo(clientes_json)
    documento = simpledialog.askstring("Documento", "Ingrese el documento del cliente a buscar:")
    cliente = next((cliente for cliente in clientes if cliente['documento'] == documento), None)
    if cliente:
        mostrar_detalle(cliente)
    else:
        messagebox.showinfo("Información", "Cliente no encontrado")

#funciones para vehículos
def listar_vehiculos():
    vehiculos = abrir_archivo(vehiculos_json)
    if not vehiculos:
        messagebox.showinfo("Información", "No hay vehículos en la base de datos.")
    else:
        mostrar_lista(vehiculos, "Vehículos")

def agregar_vehiculo():
    vehiculos = abrir_archivo(vehiculos_json)
    patente = simpledialog.askstring("Patente", "Ingrese Patente:")
    marca = simpledialog.askstring("Marca", "Ingrese Marca:")
    modelo = simpledialog.askstring("Modelo", "Ingrese Modelo:")
    tipo = simpledialog.askstring("Tipo", "Ingrese Tipo:")
    año = simpledialog.askstring("Año", "Ingrese Año:")
    kilometraje = simpledialog.askstring("Kilometraje", "Ingrese Kilometraje:")
    precio_compra = simpledialog.askstring("Precio de Compra", "Ingrese Precio de Compra:")
    precio_venta = simpledialog.askstring("Precio de Venta", "Ingrese Precio de Venta:")
    
    #validaciones
    if not año.isdigit() or int(año) < 1930 or int(año) > 2024:
        messagebox.showerror("Error", "Año inválido. Debe ser un número entre 1930 y 2024.")
        return
    if not kilometraje.isdigit() or int(kilometraje) < 0:
        messagebox.showerror("Error", "Kilometraje inválido. Debe ser un número positivo.")
        return
    if not precio_compra.isdigit() or int(precio_compra) < 0:
        messagebox.showerror("Error", "Precio de compra inválido. Debe ser un número positivo.")
        return
    if not precio_venta.isdigit() or int(precio_venta) < 0:
        messagebox.showerror("Error", "Precio de venta inválido. Debe ser un número positivo.")
        return
    
    vehiculo = {
        'id_vehiculo': len(vehiculos) + 1,
        'patente': patente,
        'marca': marca,
        'modelo': modelo,
        'tipo': tipo,
        'año': año,
        'kilometraje': kilometraje,
        'precio_compra': precio_compra,
        'precio_venta': precio_venta,
        'estado': 'Disponible'
    }
    
    vehiculos.append(vehiculo)
    escribir_archivo(vehiculos_json, vehiculos)

def eliminar_vehiculo():
    vehiculos = abrir_archivo(vehiculos_json)
    patente = simpledialog.askstring("Patente", "Ingrese la patente del vehículo a eliminar:")
    vehiculos = [vehiculo for vehiculo in vehiculos if vehiculo['patente'] != patente]
    escribir_archivo(vehiculos_json, vehiculos)

def buscar_vehiculo():
    vehiculos = abrir_archivo(vehiculos_json)
    patente = simpledialog.askstring("Patente", "Ingrese la patente del vehículo a buscar:")
    vehiculo = next((vehiculo for vehiculo in vehiculos if vehiculo['patente'] == patente), None)
    if vehiculo:
        mostrar_detalle(vehiculo)
    else:
        messagebox.showinfo("Información", "Vehículo no encontrado")

#funciones para transacciones
def listar_transacciones():
    transacciones = abrir_archivo(transacciones_json)
    if not transacciones:
        messagebox.showinfo("Información", "No hay transacciones en la base de datos.")
    else:
        mostrar_lista(transacciones, "Transacciones")

def agregar_transaccion():
    transacciones = abrir_archivo(transacciones_json)
    id_vehiculo = simpledialog.askstring("ID Vehículo", "Ingrese ID del Vehículo:")
    id_cliente = simpledialog.askstring("ID Cliente", "Ingrese ID del Cliente:")
    tipo_transaccion = simpledialog.askstring("Tipo de Transacción", "Ingrese Tipo de Transacción (Compra/Venta):")
    fecha = simpledialog.askstring("Fecha", "Ingrese Fecha (YYYY-MM-DD):")
    monto = simpledialog.askstring("Monto", "Ingrese Monto:")
    
    transaccion = {
        'id_transaccion': len(transacciones) + 1,
        'id_vehiculo': id_vehiculo,
        'id_cliente': id_cliente,
        'tipo_transaccion': tipo_transaccion,
        'fecha': fecha,
        'monto': monto,
        'observaciones': simpledialog.askstring("Observaciones", "Ingrese Observaciones:")
    }
    
    transacciones.append(transaccion)
    escribir_archivo(transacciones_json, transacciones)

    #actualizar el estado del vehículo si es una venta
    if tipo_transaccion.lower() == 'venta':
        vehiculos = abrir_archivo(vehiculos_json)
        for vehiculo in vehiculos:
            if vehiculo['id_vehiculo'] == int(id_vehiculo):
                vehiculo['estado'] = 'Vendido'
                break
        escribir_archivo(vehiculos_json, vehiculos)

def eliminar_transaccion():
    transacciones = abrir_archivo(transacciones_json)
    id_transaccion = simpledialog.askstring("ID Transacción", "Ingrese el ID de la transacción a eliminar:")
    transacciones = [transaccion for transaccion in transacciones if transaccion['id_transaccion'] != int(id_transaccion)]
    escribir_archivo(transacciones_json, transacciones)

def buscar_transaccion():
    transacciones = abrir_archivo(transacciones_json)
    id_transaccion = simpledialog.askstring("ID Transacción", "Ingrese el ID de la transacción a buscar:")
    transaccion = next((transaccion for transaccion in transacciones if transaccion['id_transaccion'] == int(id_transaccion)), None)
    if transaccion:
        mostrar_detalle(transaccion)
    else:
        messagebox.showinfo("Información", "Transacción no encontrada")

#funciones adicionales
def imprimir_listado_ventas():
    id_cliente = simpledialog.askstring("ID Cliente", "Ingrese ID de Cliente (opcional):")
    id_vehiculo = simpledialog.askstring("ID Vehículo", "Ingrese ID de Vehículo (opcional):")
    fecha_inicio = simpledialog.askstring("Fecha Inicio", "Ingrese Fecha de Inicio (YYYY-MM-DD, opcional):")
    fecha_fin = simpledialog.askstring("Fecha Fin", "Ingrese Fecha de Fin (YYYY-MM-DD, opcional):")
    
    transacciones = abrir_archivo(transacciones_json)
    ventas = [t for t in transacciones if t['tipo_transaccion'].lower() == 'venta']
    
    if id_cliente:
        ventas = [t for t in ventas if t['id_cliente'] == int(id_cliente)]
    if id_vehiculo:
        ventas = [t for t in ventas if t['id_vehiculo'] == int(id_vehiculo)]
    if fecha_inicio and fecha_fin:
        ventas = [t for t in ventas if fecha_inicio <= t['fecha'] <= fecha_fin]
    
    total_monto = sum(int(t['monto']) for t in ventas)
    
    mostrar_lista(ventas, "Ventas")
    messagebox.showinfo("Total de Ventas", f"Total de ventas: {total_monto}")

def mostrar_lista(lista, titulo):
    ventana_lista = tk.Toplevel()
    ventana_lista.title(titulo)
    
    texto = tk.Text(ventana_lista)
    texto.pack(expand=True, fill='both')
    
    for item in lista:
        texto.insert('end', f"{item}\n")

def mostrar_detalle(item):
    ventana_detalle = tk.Toplevel()
    ventana_detalle.title("Detalle")
    
    texto = tk.Text(ventana_detalle)
    texto.pack(expand=True, fill='both')
    
    texto.insert('end', f"{item}\n")

#inicialización de archivos JSON
clientes_json = 'clientes.json'
vehiculos_json = 'vehiculos.json'
transacciones_json = 'transacciones.json'

for ruta in [clientes_json, vehiculos_json, transacciones_json]:
    crear_archivo(ruta)

#interfaz gráfica tkinter
def menu():
    root = tk.Tk()
    root.title("Sistema de Gestión de Concesionaria de Vehículos Usados")
    
    ttk.Button(root, text="Listar Clientes", command=listar_clientes).pack(fill='x')
    ttk.Button(root, text="Agregar Cliente", command=agregar_cliente).pack(fill='x')
    ttk.Button(root, text="Eliminar Cliente", command=eliminar_cliente).pack(fill='x')
    ttk.Button(root, text="Buscar Cliente", command=buscar_cliente).pack(fill='x')
    ttk.Button(root, text="Listar Vehículos", command=listar_vehiculos).pack(fill='x')
    ttk.Button(root, text="Agregar Vehículo", command=agregar_vehiculo).pack(fill='x')
    ttk.Button(root, text="Eliminar Vehículo", command=eliminar_vehiculo).pack(fill='x')
    ttk.Button(root, text="Buscar Vehículo", command=buscar_vehiculo).pack(fill='x')
    ttk.Button(root, text="Listar Transacciones", command=listar_transacciones).pack(fill='x')
    ttk.Button(root, text="Agregar Transacción", command=agregar_transaccion).pack(fill='x')
    ttk.Button(root, text="Eliminar Transacción", command=eliminar_transaccion).pack(fill='x')
    ttk.Button(root, text="Buscar Transacción", command=buscar_transaccion).pack(fill='x')
    ttk.Button(root, text="Imprimir Listado de Ventas", command=imprimir_listado_ventas).pack(fill='x')
    
    root.mainloop()

#ejecutar el menú
menu()


