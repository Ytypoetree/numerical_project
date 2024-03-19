import numpy as np
import matplotlib.pyplot as plt

rate = 1
T = 10
dt = 0.01
num_paths = 10

paths = []

for i in range(num_paths):
    path = [0] 
    t = 0 
    while t < T: 
        increment = np.random.poisson(rate * dt) 
        t += dt
        path.append(path[-1] + increment)
    paths.append(path[:-1])

# Generate time axis
time_axis = np.linspace(0, T - dt, len(paths[0]))

plt.figure(figsize=(10, 6)) 
for path in paths: 
    plt.step(time_axis, path, where='post')  
plt.xlabel('Time') 
plt.ylabel('Number of events')  
plt.title('10 Paths of Poisson Process with Rate 1') 
plt.grid(True)  
plt.show() 