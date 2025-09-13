import sys
import sqlite3
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkcalendar import Calendar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# ---------------------------
# 1. CREACIÓN DEL GRAFO
# ---------------------------
nodos = {
    "La Comarca": {"país": "Tierra Media", "aeropuerto": "Bilbo Bolsón", "tipo": "Ordinaria"},
    "Rivendel": {"país": "Tierra Media", "aeropuerto": "Altos Elfos", "tipo": "Importante"},
    "Rohan": {"país": "Tierra Media", "aeropuerto": "Caballo Verde", "tipo": "Ordinaria"},
    "Reino del Bosque": {"país": "Tierra Media", "aeropuerto": "Elfos Silvanos", "tipo": "Ordinaria"},
    "Erebor": {"país": "Tierra Media", "aeropuerto": "Durin", "tipo": "Ordinaria"},
    "Gondor": {"país": "Tierra Media", "aeropuerto": "Isildur", "tipo": "Capital"},
    "Moria": {"país": "Tierra Media", "aeropuerto": "Khazad Dum", "tipo": "Ordinaria"},
    "Isengard": {"país": "Tierra Media", "aeropuerto": "Mago Blanco", "tipo": "Ordinaria"},
    "Mordor": {"país": "Tierra Media", "aeropuerto": "Ojo de Sauron", "tipo": "Importante"},
    "Narnia": {"país": "Narnia", "aeropuerto": "León Real", "tipo": "Capital"},
    "Telmar": {"país": "Narnia", "aeropuerto": "Príncipe Caspian", "tipo": "Importante"},
    "Charn": {"país": "Narnia", "aeropuerto": "Bruja Blanca", "tipo": "Importante"},
    "Ciudad Esmeralda": {"país": "Oz", "aeropuerto": "Mago de Oz", "tipo": "Capital"},
    "Winkie": {"país": "Oz", "aeropuerto": "Bruja del Oeste", "tipo": "Importante"},
    "Munchkin": {"país": "Oz", "aeropuerto": "Dorita", "tipo": "Ordinaria"},
}

aristas = [
    {"origen": "La Comarca", "destino": "Rivendel", "tipo": "N", "distancia": 500.00, "tiempo": 1.5, "costo": 1550.00},
    {"origen": "Rivendel", "destino": "La Comarca", "tipo": "N", "distancia": 500.00, "tiempo": 1.5, "costo": 1850.00},
    {"origen": "Rivendel", "destino": "Reino del Bosque", "tipo": "N", "distancia": 950.00, "tiempo": 2.4, "costo": 2400.00},
    {"origen": "Rivendel", "destino": "Rohan", "tipo": "N", "distancia": 550.00, "tiempo": 1.6, "costo": 1975.00},
    {"origen": "Rivendel", "destino": "Telmar", "tipo": "I", "distancia": 1100.00, "tiempo": 5.2, "costo": 3750.00},
    {"origen": "Rohan", "destino": "Rivendel", "tipo": "N", "distancia": 550.00, "tiempo": 1.6, "costo": 1675.00},
    {"origen": "Rohan", "destino": "Isengard", "tipo": "N", "distancia": 400.00, "tiempo": 1.3, "costo": 1300.00},
    {"origen": "Rohan", "destino": "Gondor", "tipo": "N", "distancia": 600.00, "tiempo": 1.7, "costo": 1550.00},
    {"origen": "Gondor", "destino": "Rohan", "tipo": "N", "distancia": 600.00, "tiempo": 1.7, "costo": 2350.00},
    {"origen": "Gondor", "destino": "Erebor", "tipo": "N", "distancia": 1250.00, "tiempo": 3.0, "costo": 4225.00},
    {"origen": "Gondor", "destino": "Mordor", "tipo": "N", "distancia": 450.00, "tiempo": 3.4, "costo": 3125.00},
    {"origen": "Gondor", "destino": "Narnia", "tipo": "I", "distancia": 550.00, "tiempo": 4.1, "costo": 1975.00},
    {"origen": "Gondor", "destino": "Ciudad Esmeralda", "tipo": "I", "distancia": 1100.00, "tiempo": 5.2, "costo": 4250.00},
    {"origen": "Mordor", "destino": "Isengard", "tipo": "N", "distancia": 550.00, "tiempo": 1.6, "costo": 1375.00},
    {"origen": "Mordor", "destino": "Winkie", "tipo": "I", "distancia": 600.00, "tiempo": 3.2, "costo": 1500.00},
    {"origen": "Isengard", "destino": "Rohan", "tipo": "N", "distancia": 400.00, "tiempo": 1.3, "costo": 1300.00},
    {"origen": "Isengard", "destino": "Moria", "tipo": "N", "distancia": 400.00, "tiempo": 1.3, "costo": 1100.00},
    {"origen": "Moria", "destino": "Isengard", "tipo": "N", "distancia": 400.00, "tiempo": 1.3, "costo": 1300.00},
    {"origen": "Moria", "destino": "Erebor", "tipo": "N", "distancia": 900.00, "tiempo": 2.3, "costo": 2225.00},
    {"origen": "Erebor", "destino": "Moria", "tipo": "N", "distancia": 900.00, "tiempo": 2.3, "costo": 2000.00},
    {"origen": "Erebor", "destino": "Gondor", "tipo": "N", "distancia": 1250.00, "tiempo": 3.0, "costo": 3525.00},
    {"origen": "Reino del Bosque", "destino": "Erebor", "tipo": "N", "distancia": 500.00, "tiempo": 4.5, "costo": 2450.00},
    {"origen": "Reino del Bosque", "destino": "Rivendel", "tipo": "N", "distancia": 950.00, "tiempo": 2.4, "costo": 2100.00},
    {"origen": "Narnia", "destino": "Telmar", "tipo": "N", "distancia": 400.00, "tiempo": 1.3, "costo": 1800.00},
    {"origen": "Narnia", "destino": "Charn", "tipo": "N", "distancia": 450.00, "tiempo": 3.4, "costo": 3125.00},
    {"origen": "Narnia", "destino": "Gondor", "tipo": "I", "distancia": 550.00, "tiempo": 4.1, "costo": 2875.00},
    {"origen": "Narnia", "destino": "Ciudad Esmeralda", "tipo": "I", "distancia": 1300.00, "tiempo": 5.6, "costo": 4750.00},
    {"origen": "Telmar", "destino": "Narnia", "tipo": "N", "distancia": 400.00, "tiempo": 1.3, "costo": 1500.00},
    {"origen": "Telmar", "destino": "Rivendel", "tipo": "I", "distancia": 1100.00, "tiempo": 5.2, "costo": 3750.00},
    {"origen": "Charn", "destino": "Narnia", "tipo": "N", "distancia": 450.00, "tiempo": 3.4, "costo": 1225.00},
    {"origen": "Charn", "destino": "Winkie", "tipo": "I", "distancia": 700.00, "tiempo": 3.4, "costo": 875.00},
    {"origen": "Ciudad Esmeralda", "destino": "Munchkin", "tipo": "N", "distancia": 200.00, "tiempo": 3.4, "costo": 875.00},
    {"origen": "Ciudad Esmeralda", "destino": "Winkie", "tipo": "N", "distancia": 300.00, "tiempo": 3.1, "costo": 2250.00},
    {"origen": "Ciudad Esmeralda", "destino": "Gondor", "tipo": "I", "distancia": 1100.00, "tiempo": 5.2, "costo": 4250.00},
    {"origen": "Ciudad Esmeralda", "destino": "Narnia", "tipo": "I", "distancia": 1300.00, "tiempo": 5.6, "costo": 4750.00},
    {"origen": "Winkie", "destino": "Mordor", "tipo": "I", "distancia": 600.00, "tiempo": 3.2, "costo": 750.00},
    {"origen": "Winkie", "destino": "Charn", "tipo": "I", "distancia": 700.00, "tiempo": 3.4, "costo": 875.00},
]

grafo = nx.DiGraph()
for ciudad, atributos in nodos.items():
    grafo.add_node(ciudad, **atributos)
for ruta in aristas:
    origen, destino = ruta["origen"], ruta["destino"]
    grafo.add_edge(origen, destino, **ruta)

# Marcar aristas bidireccionales internamente
for origen, destino in list(grafo.edges()):
    if grafo.has_edge(destino, origen):
        grafo[origen][destino]["flecha"] = "doble"
        grafo[destino][origen]["flecha"] = "doble"

colores_nodos = {'Capital': 'gold', 'Importante': 'skyblue', 'Ordinaria': 'lightgreen'}
tamaños_nodos = {'Capital': 1000, 'Importante': 700, 'Ordinaria': 500}
pos = nx.spring_layout(grafo, seed=42)

fig, ax = plt.subplots(figsize=(6, 6))
for tipo, color in colores_nodos.items():
    nodos_tipo = [nodo for nodo, datos in grafo.nodes(data=True) if datos['tipo'] == tipo]
    nx.draw_networkx_nodes(grafo, pos, nodelist=nodos_tipo,
                           node_color=color,
                           node_size=[tamaños_nodos[tipo]] * len(nodos_tipo),
                           alpha=0.8, ax=ax)
nx.draw_networkx_labels(grafo, pos, font_size=10, font_color='black', ax=ax)

dibujadas = set()
for origen, destino, datos in grafo.edges(data=True):
    if (origen, destino) in dibujadas or (destino, origen) in dibujadas:
        continue
    if "flecha" in datos and datos["flecha"] == "doble":
        nx.draw_networkx_edges(grafo, pos, edgelist=[(origen, destino)],
                               arrowstyle='-|>', arrowsize=20,
                               connectionstyle='arc3,rad=0.1', edge_color='gray', alpha=0.6, ax=ax)
        nx.draw_networkx_edges(grafo, pos, edgelist=[(destino, origen)],
                               arrowstyle='-|>', arrowsize=20,
                               connectionstyle='arc3,rad=0.1', edge_color='gray', alpha=0.6, ax=ax)
    else:
        nx.draw_networkx_edges(grafo, pos, edgelist=[(origen, destino)],
                               arrowstyle='-|>', arrowsize=20,
                               connectionstyle='arc3,rad=0.1', edge_color='gray', alpha=0.6, ax=ax)
    dibujadas.add((origen, destino))

ax.set_title("Mapa de Rutas entre Ciudades de Mundos Fantásticos", fontsize=14)
ax.axis('off')

# ---------------------------
# 2. INTERFAZ TKINTER
# ---------------------------
root = tk.Tk()
root.title("Sistema de Registro de Vuelos")
root.state("zoomed")

def on_closing():
    root.destroy()
    sys.exit()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Crear dos frames: uno para el grafo y otro para los formularios
frame_izquierda = tk.Frame(root, width=800)
frame_izquierda.grid(row=0, column=0, sticky="nsew")
frame_derecha = tk.Frame(root)
frame_derecha.grid(row=0, column=1, sticky="nsew")
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=3)
root.rowconfigure(0, weight=1)

canvas_grafo = FigureCanvasTkAgg(fig, master=frame_izquierda)
canvas_grafo.get_tk_widget().pack(fill=tk.BOTH, expand=True)
canvas_grafo.draw()

toolbar = NavigationToolbar2Tk(canvas_grafo, frame_izquierda)
toolbar.update()
canvas_grafo.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# ---------------------------
# 3. BASE DE DATOS: NUEVA ESTRUCTURA
# ---------------------------
# Se crearán 3 tablas:
#   - Usuarios: se agrega el campo 'pasaporte' (único)
#   - Vuelos: cada vuelo es único (por origen, destino, fecha y ruta) y contiene capacidad y ocupación
#   - Usuarios_Vuelos: tabla intermedia para asociar usuarios a vuelos

def conectar_bd():
    conn = sqlite3.connect("vuelos.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pasaporte TEXT UNIQUE,
        nombre TEXT NOT NULL,
        ap_paterno TEXT NOT NULL,
        ap_materno TEXT NOT NULL,
        fecha_nacimiento DATE NOT NULL,
        nacionalidad TEXT NOT NULL,
        raza TEXT NOT NULL,
        telefono TEXT NOT NULL,
        correo TEXT NOT NULL
    )''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vuelos (
        vuelo_id INTEGER PRIMARY KEY AUTOINCREMENT,
        origen TEXT NOT NULL,
        destino TEXT NOT NULL,
        fecha DATE NOT NULL,
        ruta TEXT NOT NULL,
        distancia_total REAL NOT NULL,
        tiempo_total REAL NOT NULL,
        costo_total REAL NOT NULL,
        capacidad INTEGER NOT NULL,
        ocupacion INTEGER NOT NULL DEFAULT 0,
        UNIQUE(origen, destino, fecha, ruta)
    )''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios_Vuelos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        vuelo_id INTEGER NOT NULL,
        UNIQUE(usuario_id, vuelo_id),
        FOREIGN KEY (usuario_id) REFERENCES Usuarios(id),
        FOREIGN KEY (vuelo_id) REFERENCES Vuelos(vuelo_id)
    )''')
    conn.commit()
    return conn, cursor

# Función para insertar o recuperar un usuario (según el pasaporte)
def insertar_usuario(cursor, conn, pasaporte, nombre, ap_paterno, ap_materno, fecha_nacimiento, nacionalidad, raza, telefono, correo):
    cursor.execute("SELECT id FROM Usuarios WHERE pasaporte=?", (pasaporte,))
    result = cursor.fetchone()
    if result:
        return result[0]  # El usuario ya existe, devolver su ID
    else:
        cursor.execute('''
        INSERT INTO Usuarios (pasaporte, nombre, ap_paterno, ap_materno, fecha_nacimiento, nacionalidad, raza, telefono, correo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (pasaporte, nombre, ap_paterno, ap_materno, fecha_nacimiento, nacionalidad, raza, telefono, correo))
        conn.commit()
        return cursor.lastrowid

# Funciones para trabajar con vuelos
def obtener_vuelo_existente(cursor, origen, destino, fecha, ruta_str):
    cursor.execute("SELECT vuelo_id, ocupacion, capacidad FROM Vuelos WHERE origen=? AND destino=? AND fecha=? AND ruta=?", 
                   (origen, destino, fecha, ruta_str))
    return cursor.fetchone()  # Devuelve (vuelo_id, ocupacion, capacidad) o None

def insertar_vuelo_grupal(cursor, conn, origen, destino, fecha, ruta_seleccionada, distancia_total, tiempo_total, costo_total, capacidad):
    ruta_str = ",".join(ruta_seleccionada)
    cursor.execute('''
    INSERT INTO Vuelos (origen, destino, fecha, ruta, distancia_total, tiempo_total, costo_total, capacidad, ocupacion)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0)''', (origen, destino, fecha, ruta_str, distancia_total, tiempo_total, costo_total, capacidad))
    conn.commit()
    return cursor.lastrowid

def actualizar_ocupacion(cursor, conn, vuelo_id, incremento):
    cursor.execute("UPDATE Vuelos SET ocupacion = ocupacion + ? WHERE vuelo_id=?", (incremento, vuelo_id))
    conn.commit()

def asociar_usuario_vuelo(cursor, conn, usuario_id, vuelo_id):
    try:
        cursor.execute("INSERT INTO Usuarios_Vuelos (usuario_id, vuelo_id) VALUES (?, ?)", (usuario_id, vuelo_id))
        conn.commit()
    except sqlite3.IntegrityError:
        # Ya está asociado; no hacemos nada
        pass

# Función para calcular la capacidad según la ruta
def obtener_capacidad_por_ruta(ruta):
    """
    Asigna capacidad:
      - Si al menos un tramo es 'Importante': 30 asientos.
      - Si la ruta tiene más de 3 tramos (y ninguno 'Importante'): 25 asientos.
      - En otro caso: 20 asientos.
    """
    if any(grafo[u][v]['tipo'] == 'I' for u, v in zip(ruta[:-1], ruta[1:])):
        return 30
    elif len(ruta) > 3:
        return 25
    else:
        return 20

# Función para obtener la cantidad de usuarios ya asociados a un vuelo (ocupación)
def obtener_asientos_ocupados(cursor, vuelo_id):
    cursor.execute("SELECT ocupacion FROM Vuelos WHERE vuelo_id=?", (vuelo_id,))
    result = cursor.fetchone()
    if result:
        return result[0]
    return 0

def calcular_ruta(ruta):
    distancia_total = sum(grafo[u][v]['distancia'] for u, v in zip(ruta[:-1], ruta[1:]))
    tiempo_total = sum(grafo[u][v]['tiempo'] for u, v in zip(ruta[:-1], ruta[1:]))
    costo_total = sum(grafo[u][v]['costo'] for u, v in zip(ruta[:-1], ruta[1:]))
    return distancia_total, tiempo_total, costo_total

# ---------------------------
# REGISTRO DE USUARIOS
# ---------------------------
# Lista global para almacenar los IDs de los usuarios registrados en la sesión
registered_users = []
registered_passports = []  # Para evitar duplicados en la sesión

def registrar_usuarios_multiples(total, current=1):
    def guardar_usuario():
        pasaporte = entry_pasaporte.get().strip()
        nombre = entry_nombre.get().strip()
        ap_paterno = entry_ap_paterno.get().strip()
        ap_materno = entry_ap_materno.get().strip()
        fecha_nacimiento = cal_fecha_nacimiento.get_date()
        nacionalidad = combo_nacionalidad.get().strip()
        raza = combo_raza.get().strip()
        telefono = entry_telefono.get().strip()
        correo = entry_correo.get().strip()
        if not pasaporte or not nombre or not ap_paterno or not telefono or not correo:
            messagebox.showwarning("Advertencia", "El pasaporte, nombre, apellido, teléfono y correo son obligatorios.")
            return
        # Evitamos registrar dos veces en la misma sesión
        if pasaporte in registered_passports:
            messagebox.showinfo("Info", f"El usuario con pasaporte {pasaporte} ya está registrado en esta sesión.")
        else:
            user_id = insertar_usuario(cursor, conn, pasaporte, nombre, ap_paterno, ap_materno, fecha_nacimiento, nacionalidad, raza, telefono, correo)
            registered_users.append(user_id)
            registered_passports.append(pasaporte)
            messagebox.showinfo("Éxito", f"Usuario {current} registrado correctamente")
        if current < total:
            registrar_usuarios_multiples(total, current + 1)
        else:
            # Una vez registrados todos los usuarios, se pasa al registro de vuelo grupal
            registrar_vuelo_grupal()
    
    for widget in frame_derecha.winfo_children():
        widget.destroy()
    
    ttk.Label(frame_derecha, text=f"Registro Persona {current} de {total}", font=("Arial", 14)).pack(pady=10)
    
    ttk.Label(frame_derecha, text="Pasaporte:").pack(pady=2)
    entry_pasaporte = ttk.Entry(frame_derecha, width=30)
    entry_pasaporte.pack(pady=5)
    
    ttk.Label(frame_derecha, text="Nombre:").pack(pady=2)
    entry_nombre = ttk.Entry(frame_derecha, width=30)
    entry_nombre.pack(pady=5)
    
    ttk.Label(frame_derecha, text="Apellido Paterno:").pack(pady=2)
    entry_ap_paterno = ttk.Entry(frame_derecha, width=30)
    entry_ap_paterno.pack(pady=5)
    
    ttk.Label(frame_derecha, text="Apellido Materno:").pack(pady=2)
    entry_ap_materno = ttk.Entry(frame_derecha, width=30)
    entry_ap_materno.pack(pady=5)
    
    ttk.Label(frame_derecha, text="Fecha de Nacimiento:").pack(pady=2)
    cal_fecha_nacimiento = Calendar(frame_derecha, selectmode='day')
    cal_fecha_nacimiento.pack(pady=5)
    
    ttk.Label(frame_derecha, text="Nacionalidad:").pack(pady=2)
    combo_nacionalidad = ttk.Combobox(frame_derecha, values=["Mediaterrano", "Narniano", "Ozniano"], state="readonly", width=27)
    combo_nacionalidad.pack(pady=5)
    
    ttk.Label(frame_derecha, text="Raza:").pack(pady=2)
    combo_raza = ttk.Combobox(frame_derecha, values=["Humano", "Elfo", "Enano", "Orco", "Duende", "Mago/Bruja", "Centauro", "Fauno", "Mono Alado", "Otro"], state="readonly", width=27)
    combo_raza.pack(pady=5)
    
    ttk.Label(frame_derecha, text="Teléfono:").pack(pady=2)
    entry_telefono = ttk.Entry(frame_derecha, width=30)
    entry_telefono.pack(pady=5)
    
    ttk.Label(frame_derecha, text="Correo Electrónico:").pack(pady=2)
    entry_correo = ttk.Entry(frame_derecha, width=30)
    entry_correo.pack(pady=5)
    
    ttk.Button(frame_derecha, text="Guardar Usuario", command=guardar_usuario).pack(pady=10)

# ---------------------------
# REGISTRO DE VUELO GRUPAL
# ---------------------------
def registrar_vuelo_grupal():
    def buscar_ruta_grupal():
        origen = combo_origen.get().strip()
        destino = combo_destino.get().strip()
        criterio = combo_prioridad.get().strip()
        if not origen or not destino or not criterio:
            messagebox.showwarning("Advertencia", "Debe seleccionar origen, destino y prioridad.")
            return
        peso = {"Distancia": "distancia", "Tiempo": "tiempo", "Costo": "costo"}[criterio]
        rutas_optimas = list(nx.all_shortest_paths(grafo, source=origen, target=destino, weight=peso))
        rutas_mostrar = rutas_optimas[:3] if len(rutas_optimas) > 3 else rutas_optimas
        for widget in frame_rutas.winfo_children():
            widget.destroy()
        ttk.Label(frame_rutas, text=f"Se encontraron {len(rutas_mostrar)} rutas entre {origen} y {destino} (ordenadas por {criterio.lower()}):").pack(pady=10)
        for i, ruta in enumerate(rutas_mostrar, 1):
            distancia, tiempo, costo = calcular_ruta(ruta)
            ruta_texto = f"Ruta {i}: {ruta}\nDistancia: {distancia}, Tiempo: {tiempo}, Costo: {costo}"
            rb = ttk.Radiobutton(frame_rutas, text=ruta_texto, variable=var_ruta, value=",".join(ruta), command=actualizar_asientos_disponibles)
            rb.pack(anchor="w")
        frame_rutas.pack(pady=10)
        if rutas_mostrar and not var_ruta.get():
            var_ruta.set(",".join(rutas_mostrar[0]))
            actualizar_asientos_disponibles()

    def actualizar_asientos_disponibles():
        if var_ruta.get():
            ruta_seleccionada = var_ruta.get().split(",")
            capacidad = obtener_capacidad_por_ruta(ruta_seleccionada)
            fecha = cal_fecha.get_date()
            # Si el vuelo ya existe, consultamos su ocupación
            vuelo_existente = obtener_vuelo_existente(cursor, combo_origen.get(), combo_destino.get(), fecha, ",".join(ruta_seleccionada))
            if vuelo_existente:
                ocupacion = vuelo_existente[1]
            else:
                ocupacion = 0
            asientos_disponibles = capacidad - ocupacion
            label_asientos.config(text=f"Asientos disponibles: {asientos_disponibles} (Capacidad: {capacidad}, Ocupados: {ocupacion})")

    def guardar_vuelo_reg():
        ruta_str = var_ruta.get()
        fecha = cal_fecha.get_date()
        if not ruta_str:
            messagebox.showwarning("Advertencia", "Debe seleccionar una ruta antes de guardar.")
            return
        ruta_seleccionada = ruta_str.split(",")
        capacidad = obtener_capacidad_por_ruta(ruta_seleccionada)
        distancia_total, tiempo_total, costo_total = calcular_ruta(ruta_seleccionada)
        ruta_str = ",".join(ruta_seleccionada)
        
        # Verificar si ya existe el vuelo
        vuelo = obtener_vuelo_existente(cursor, combo_origen.get(), combo_destino.get(), fecha, ruta_str)
        if vuelo:
            vuelo_id, ocupacion, cap_existente = vuelo
            asientos_disponibles = cap_existente - ocupacion
            if len(registered_users) > asientos_disponibles:
                messagebox.showwarning("Advertencia", f"No hay asientos suficientes. Solo quedan {asientos_disponibles} asientos disponibles para esta ruta en la fecha {fecha}.")
                return
            # Asociar cada usuario al vuelo sin duplicados
            for user_id in registered_users:
                asociar_usuario_vuelo(cursor, conn, user_id, vuelo_id)
            actualizar_ocupacion(cursor, conn, vuelo_id, len(registered_users))
        else:
            # Insertar un nuevo vuelo
            vuelo_id = insertar_vuelo_grupal(cursor, conn, combo_origen.get(), combo_destino.get(), fecha, ruta_seleccionada, distancia_total, tiempo_total, costo_total, capacidad)
            if len(registered_users) > capacidad:
                messagebox.showwarning("Advertencia", f"No hay asientos suficientes. La capacidad es {capacidad} y se requieren {len(registered_users)} asientos.")
                return
            for user_id in registered_users:
                asociar_usuario_vuelo(cursor, conn, user_id, vuelo_id)
            actualizar_ocupacion(cursor, conn, vuelo_id, len(registered_users))
        
        # Calcular el total a pagar (multiplicando el costo unitario por el número de usuarios)
        total_cost = costo_total * len(registered_users)
        
        # Limpiar el frame y mostrar los resultados
        for widget in frame_derecha.winfo_children():
            widget.destroy()
        
        ttk.Label(frame_derecha, text="Resultados del Vuelo", font=("Arial", 16)).pack(pady=10)
        ttk.Label(frame_derecha, text=f"Total a Pagar: ${total_cost:.2f}").pack(pady=5)
        ttk.Label(frame_derecha, text=f"Tiempo de viaje: {tiempo_total} horas").pack(pady=5)
        ttk.Label(frame_derecha, text=f"Distancia total: {distancia_total} km").pack(pady=5)


    for widget in frame_derecha.winfo_children():
        widget.destroy()
    
    ttk.Label(frame_derecha, text="Registro de Vuelo para Todos los Usuarios", font=("Arial", 14)).pack(pady=10)
    
    ttk.Label(frame_derecha, text="Origen:").pack(pady=2)
    combo_origen = ttk.Combobox(frame_derecha, values=ciudades, state="readonly", width=30)
    combo_origen.pack(pady=5)
    
    ttk.Label(frame_derecha, text="Destino:").pack(pady=2)
    combo_destino = ttk.Combobox(frame_derecha, values=ciudades, state="readonly", width=30)
    combo_destino.pack(pady=5)
    
    ttk.Label(frame_derecha, text="Fecha:").pack(pady=2)
    cal_fecha = Calendar(frame_derecha, selectmode='day')
    cal_fecha.pack(pady=5)
    
    ttk.Label(frame_derecha, text="Prioridad:").pack(pady=2)
    combo_prioridad = ttk.Combobox(frame_derecha, values=prioridad, state="readonly", width=30)
    combo_prioridad.pack(pady=5)
    
    ttk.Button(frame_derecha, text="Buscar Ruta", command=buscar_ruta_grupal).pack(pady=10)
    
    frame_rutas = tk.Frame(frame_derecha)
    frame_rutas.pack(pady=10)
    var_ruta = tk.StringVar()
    
    label_asientos = ttk.Label(frame_derecha, text="Asientos disponibles: ")
    label_asientos.pack(pady=5)
    
    ttk.Button(frame_derecha, text="Guardar Vuelo", command=guardar_vuelo_reg).pack(pady=10)

# Valores para las listas de selección
ciudades = [
    "La Comarca", "Rivendel", "Rohan", "Reino del Bosque", "Erebor", "Gondor",
    "Moria", "Isengard", "Mordor", "Narnia", "Telmar", "Charn",
    "Ciudad Esmeralda", "Winkie", "Munchkin"
]
prioridad = ["Distancia", "Tiempo", "Costo"]

# ---------------------------
# INICIO DEL PROGRAMA
# ---------------------------
conn, cursor = conectar_bd()

# Preguntar si viaja con más personas
if messagebox.askyesno("Acompañantes", "¿Viaja con más personas?"):
    num_acompanantes = simpledialog.askinteger("Número de Acompañantes", "¿Cuántas personas viajan con usted?", minvalue=1)
else:
    num_acompanantes = 0

# Se asume que el usuario principal también se registra
total_registrations = 1 + num_acompanantes
registrar_usuarios_multiples(total_registrations, 1)
root.mainloop()
