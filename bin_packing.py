import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# dikdörtgenler için sınıf
class Rectangle:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

# nesil boyutu,nesil sayısı,mutasyon oranı
pop_size = 100
num_generations = 1000
mutation_rate = 0.01

# dikdörtgenlerin boyutları ve pozisyonlarını tanımlar
rectangles = [Rectangle(2, 12, 0, 0),
              Rectangle(7, 12, 0, 0),
              Rectangle(8, 6, 0, 0),
              Rectangle(3, 6, 0, 0),
              Rectangle(3, 5, 0, 0),
              Rectangle(5, 5, 0, 0),
              Rectangle(3, 12, 0, 0),
              Rectangle(3, 7, 0, 0),
              Rectangle(5, 7, 0, 0),
              Rectangle(2, 6, 0, 0),
              Rectangle(3, 2, 0, 0),
              Rectangle(4, 2, 0, 0),
              Rectangle(3, 4, 0, 0),
              Rectangle(4, 4, 0, 0),
              Rectangle(9, 2, 0, 0),
              Rectangle(11, 2, 0, 0)
             ]

# dikdörtgenlerin üst üste gelip gelmediğini kontrol eder
def check_overlap(rect1, rect2):
    if rect1.x < rect2.x + rect2.width and rect1.x + rect1.width > rect2.x and rect1.y < rect2.y + rect2.height and rect1.y + rect1.height > rect2.y:
        return True
    return False

# verilen çözümün uygunluğunu değerlendirir
def evaluate_fitness(rectangles):
    fitness = 0
    for i in range(len(rectangles)):
        for j in range(i+1, len(rectangles)):
            if not check_overlap(rectangles[i], rectangles[j]):
                fitness += 1
    return fitness

# eski nesilden yeni nesil oluşturur
def create_new_population(old_population):
    new_population = []
    for i in range(pop_size):
        parent1 = random.choice(old_population)
        parent2 = random.choice(old_population)
        child = []
        for j in range(16):
            if random.random() < 0.5:
                child.append(Rectangle(rectangles[j].width, rectangles[j].height, parent1[j].x, parent1[j].y))
            else:
                child.append(Rectangle(rectangles[j].width, rectangles[j].height, parent2[j].x, parent2[j].y))
            if random.random() < mutation_rate:
                child[j].x = random.randint(0, 20 - child[j].width)
                child[j].y = random.randint(0, 20 - child[j].height)
        new_population.append(child)
    return new_population

# Başlangıç nesli oluşturur
population = [[Rectangle(rectangles[i].width, rectangles[i].height, random.randint(0, 20 - rectangles[i].width), random.randint(0, 20 - rectangles[i].height)) for i in range(16)] for j in range(pop_size)]

#genetik algoritmayı çalıştırır
for i in range(num_generations):
    population.sort(key=evaluate_fitness, reverse=True)
    population = population[:int(pop_size/2)]
    population = create_new_population(population)

# genetik algoritmadan en iyi çözümü alır
best_solution = population[0]

# bir şekil ve eksen oluşturur
fig, ax = plt.subplots()


# eksenin sınırlarını ayarlar
ax.set_xlim([0, 20])
ax.set_ylim([0, 20])

# 16 renkten oluşan bir renk haritası oluşturur
colormap = cm.rainbow(np.linspace(0, 1, len(best_solution)))

# En iyi çözümde dikdörtgenleri yeniler
for i, rectangle in enumerate(best_solution):
    rect = ax.add_patch(plt.Rectangle((rectangle.x, rectangle.y), rectangle.width, rectangle.height, color=colormap[i]))
    ax.annotate("{}x{}".format(rectangle.width, rectangle.height), (rectangle.x, rectangle.y), fontsize=8, color='black')

#şekli gösterir
plt.show()

