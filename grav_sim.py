import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x, y = [0], [0]
ln, = plt.plot([], [], 'bo')

a = 10  # вертикальная полуось эллипса
v0 = 5  # горизонтальная полуось эллипса
vx = math.cos(a)*v0
vy = math.sin(a)*v0
t=1

# задание пределов координатных осей
def init():
    ax.set_xlim(0, 150)
    ax.set_ylim(0, 150)
    return ln,


# Рассчет координат точки в момент t
def X(x, vx):
    return x+vx


def Y(v, ):
    return 3

def update(frame):
    global t
    global vx
    global vy
    t += 5

    if X(x[-1], vx) > 150 or X(x[-1], vx) < 0:
        vx *= -0.8
    x.append(X(x[-1], vx))

    y.append(Y(v0, a, t))
    x.pop(-2)
    y.pop(-2)
    ln.set_data(x, y)
    print(x, y)
    return ln,


# FuncAnimation берет объект графики, настройку осей, функ, по которой
# происходит анимация,
ani = FuncAnimation(fig, update, frames=np.linspace(0, 70, 256),
                    init_func=init, blit=True, interval=60)
plt.show()