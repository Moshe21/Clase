import tkinter as tk
from tkinter import messagebox
import random
import pygame

# Inicializar pygame para sonidos
pygame.mixer.init()

# Cargar sonidos
sonido_correcto = pygame.mixer.Sound("correcto.mp3")  # Agrega un sonido de respuesta correcta
sonido_incorrecto = pygame.mixer.Sound("incorrecto.mp3")  # Agrega un sonido de error
sonido_subir_nivel = pygame.mixer.Sound("nivel_up.mp3")  # Sonido para subir de nivel

# Diccionario de preguntas organizadas por nivel
preguntas = {
    1: [
        {
            "pregunta": "¿Qué representa un diagrama de actividades en UML?",
            "opciones": ["La estructura de una base de datos",
                         "El flujo de trabajo de un proceso",
                         "La jerarquía de clases en un sistema",
                         "La interacción entre usuarios y el sistema"],
            "respuesta": "El flujo de trabajo de un proceso",
            "pista": "Se usa para modelar procesos y describir cómo fluyen las actividades."
        },
        {
            "pregunta": "¿Cuál de estos elementos representa una decisión en un diagrama de actividades?",
            "opciones": ["Un rectángulo", "Un diamante", "Un círculo", "Una flecha"],
            "respuesta": "Un diamante",
            "pista": "También se usa en diagramas de flujo para representar bifurcaciones."
        }
    ],
    2: [
        {
            "pregunta": "En UML, ¿qué representa un nodo inicial en un diagrama de actividades?",
            "opciones": ["El fin del proceso", "Una actividad en curso", "El punto de inicio del flujo", "Una bifurcación"],
            "respuesta": "El punto de inicio del flujo",
            "pista": "Este nodo indica dónde comienza el flujo de actividades."
        }
    ]
}

# Variables de juego
nivel = 1
puntaje = 0
respuestas_correctas = 0
total_para_subir = 5  # Cambia a 10 para dificultad real
pregunta_actual = None
intentos = 0

# Crear ventana de Tkinter
root = tk.Tk()
root.title("Juego de Diagramas de Actividades")
root.geometry("600x400")

# Widgets de la interfaz
lbl_nivel = tk.Label(root, text=f"Nivel: {nivel}", font=("Arial", 14))
lbl_nivel.pack(pady=10)

lbl_pregunta = tk.Label(root, text="", font=("Arial", 12), wraplength=500, justify="center", fg="black")
lbl_pregunta.pack(pady=20)

btn_opciones = []  # Lista para los botones de respuestas
for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 10), width=50, command=lambda i=i: verificar_respuesta(i))
    btn.pack(pady=5)
    btn_opciones.append(btn)

lbl_pista = tk.Label(root, text="", font=("Arial", 10), fg="blue")
lbl_pista.pack(pady=10)

lbl_progreso = tk.Label(root, text=f"Progreso: {respuestas_correctas}/{total_para_subir}", font=("Arial", 12))
lbl_progreso.pack(pady=10)

# Función para hacer animación en la pregunta (cambia el color temporalmente)
def animar_pregunta():
    lbl_pregunta.config(fg="red")
    root.after(300, lambda: lbl_pregunta.config(fg="black"))  # Vuelve a negro después de 300ms

# Función para cargar una nueva pregunta
def nueva_pregunta():
    global pregunta_actual, intentos
    intentos = 0
    if nivel not in preguntas:
        pygame.mixer.Sound.play(sonido_subir_nivel)
        messagebox.showinfo("¡Felicidades!", "Has completado todas las preguntas. 🏆")
        root.quit()
        return

    pregunta_actual = random.choice(preguntas[nivel])
    lbl_pregunta.config(text=pregunta_actual["pregunta"])
    lbl_pista.config(text="")  # Resetear pista

    opciones = pregunta_actual["opciones"]
    random.shuffle(opciones)  # Mezclar opciones
    for i in range(4):
        btn_opciones[i].config(text=opciones[i], state=tk.NORMAL)

# Función para verificar respuesta
def verificar_respuesta(indice):
    global respuestas_correctas, puntaje, nivel, intentos

    respuesta_seleccionada = btn_opciones[indice].cget("text")  # Obtener texto del botón
    if respuesta_seleccionada == pregunta_actual["respuesta"]:
        pygame.mixer.Sound.play(sonido_correcto)  # Reproducir sonido correcto
        messagebox.showinfo("✅ Correcto", "¡Bien hecho! 🎉")
        respuestas_correctas += 1
        puntaje += 1
        lbl_progreso.config(text=f"Progreso: {respuestas_correctas}/{total_para_subir}")

        if respuestas_correctas >= total_para_subir:
            nivel += 1
            respuestas_correctas = 0
            lbl_nivel.config(text=f"Nivel: {nivel}")
            pygame.mixer.Sound.play(sonido_subir_nivel)  # Sonido de subir de nivel
            messagebox.showinfo("🎉 Subiste de Nivel", f"¡Felicidades! Ahora estás en el Nivel {nivel} 🔥")
        
        nueva_pregunta()
    else:
        pygame.mixer.Sound.play(sonido_incorrecto)  # Reproducir sonido de error
        intentos += 1
        animar_pregunta()  # Animar la pregunta cambiando color

        if intentos == 1:
            lbl_pista.config(text=f"❌ Incorrecto. Pista: {pregunta_actual['pista']}")
        else:
            messagebox.showerror("❌ Incorrecto", f"La respuesta correcta era: {pregunta_actual['respuesta']}")
            nueva_pregunta()

# Iniciar la primera pregunta
nueva_pregunta()

# Ejecutar la ventana
root.mainloop()