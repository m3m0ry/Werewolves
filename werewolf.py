import random
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def play_werewolf(n_human, n_werewolf):
    while n_human > n_werewolf and n_human > 0 and n_werewolf > 0:
        # Night -> kill human
        n_human -= 1
        # Day -> random choise
        if random.choice([False]*n_human + [True]*n_werewolf):
            n_werewolf -= 1
        else:
            n_human -=1
    # Debug:
    #print(n_human, n_werewolf)
    if n_werewolf == 0:
        return True
    else:
        return False


# Sampling of werewolf games:
humans_max = 15
humans_min = 4
werewolves_max = 5
werewolves_min = 1
samples = 1000
out = np.zeros((humans_max - humans_min, werewolves_max - werewolves_min))
out2 = np.zeros((samples))

for h in range(humans_max - humans_min):
    for w in range(werewolves_max - werewolves_min):
        for i in range(samples):
            out2[i] = play_werewolf(h + humans_min, w + werewolves_min) / samples
        out[h,w] = np.sum(out2)
#print(out)


# Graphical output:
fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.array(range(humans_min, humans_max))
Y = np.array(range(werewolves_min, werewolves_max))
X,Y = np.meshgrid(X, Y)
X = np.transpose(X)
Y = np.transpose(Y)
#print(X)
#print(Y)

surf = ax.plot_surface(X, Y, out, cmap=cm.jet)
ax.set_xlabel("Number of humans")
ax.set_ylabel("Number of werewolves")
ax.set_zlabel("Probability of human victory")
#wire = ax.plot_wireframe(X,Y, out)

plt.show() 
