import collections
import matplotlib.pyplot as plt

from Combat import Combat
from Ships.Corvette import Corvette
from Ships.AncientMiningDrone import AncientMiningDrone

list_ship_a = [Corvette("Missiles", level=2, armor=2) for _ in range(4)]
list_ship_b = [AncientMiningDrone() for _ in range(2)]

list_of_results = []

for i in range(10000):

    ship_a = Corvette("Missiles", level=1, armor=2)
    ship_b = AncientMiningDrone()
    ship_b.take_damage(attacking_ship=ship_a)
    ship_b.take_damage(attacking_ship=ship_a)
    list_of_results.append(ship_b.take_damage(attacking_ship=ship_a))

occurrences = collections.Counter(list_of_results)

x = occurrences.keys()
y = occurrences.values()
plt.xlabel("Status")
plt.ylabel("Iterations")
plt.bar(x, y)
plt.show()

