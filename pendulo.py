from vpython import*
import math
T = 10000
dt = 0.01
m = 1.0
v = 0.1
l = 12.0
g = 9.81
teta = 90.0
t = 0
w = 0.0
teta = teta*math.pi/180.0
y = -l*math.cos(teta)
x = l*math.sin(teta)

base1 = box(pos=vector(0, -2, -2), axis=vector(0, -15, 0), size=vector(15, 5, 0.25), material=materials.wood)
base2 = box(pos=vector(0, -9.5, -2), axis=vector(0, -15, 0), size=vector(0.25, 5, 10), material=materials.wood)

esfera = sphere(pos=vector(x, y + 5, 0), radius = 0.5)

haste2 = cilinder(pos=vector(0, 5, 0.5), axis=vector(0, 0, -2.5), radius= 0.2)
haste1 = cilinder(pos=vector(0, 5, 0), axis=vector(x, y, 0), radius= 0.03)

while(t <= T):
    rate(200)
    haste.pos = vector(0, 5, 0)
    esfera.pos = vector(x, y + 5, 0)
    haste.axis = vector(x, y, 0)
    teta = teta + w*dt
    w = w + (-g/l*sin(teta) - b/m*w)*dt
    y = -l*math.cos(teta)
    x = l*math.sin(teta)
    t = t + dt