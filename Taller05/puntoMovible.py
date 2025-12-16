import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton

# Puntos fijos
p1 = [5.4, 3.2]
# Punto intermedio movible
p2 = [9.5, 0.7]
p3 = [12.3, -3.6]

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
ax.set_xlim(4, 14)
ax.set_ylim(-6, 5)

# Dibujar los puntos
points, = ax.plot([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], 'ro')
curve, = ax.plot([], [], 'b-', linewidth=2)

# Crear leyenda vacía (se actualizará)
legend_text = ax.legend([f"p2: ({p2[0]:.2f}, {p2[1]:.2f})"], loc="upper left")

selected = [False]  # Para saber si estamos arrastrando p2

def interpolate_parabola(p1, p2, p3):
    # Sistema lineal para resolver coeficientes de parábola
    A = np.array([
        [p1[0]**2, p1[0], 1],
        [p2[0]**2, p2[0], 1],
        [p3[0]**2, p3[0], 1]
    ])
    Y = np.array([p1[1], p2[1], p3[1]])
    a, b, c = np.linalg.solve(A, Y)
    return a, b, c, lambda x: a*x**2 + b*x + c

def update_plot():
    # Actualiza los puntos y la curva
    points.set_data([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]])
    a, b, c, parabola = interpolate_parabola(p1, p2, p3)
    x_vals = np.linspace(p1[0], p3[0], 300)
    y_vals = parabola(x_vals)
    curve.set_data(x_vals, y_vals)

    # Actualiza la leyenda con coordenadas y ecuación
    legend_text.remove()
    eq_str = f"y = {a:.2f}x² + {b:.2f}x + {c:.2f}"
    new_label = f"p2: ({p2[0]:.2f}, {p2[1]:.2f})\n{eq_str}"
    ax.legend([new_label], loc="upper left")

    fig.canvas.draw_idle()

def on_press(event):
    if event.button == MouseButton.LEFT:
        # Verifica si hizo clic cerca de p2
        if abs(event.xdata - p2[0]) < 0.3 and abs(event.ydata - p2[1]) < 0.3:
            selected[0] = True

def on_release(event):
    selected[0] = False

def on_motion(event):
    if selected[0] and event.xdata and event.ydata:
        p2[0], p2[1] = event.xdata, event.ydata
        update_plot()

fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_motion)

update_plot()
plt.title("Interpolación Parabólica con p2 Movible")
plt.grid(True)
plt.show()