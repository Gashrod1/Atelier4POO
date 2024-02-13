import math


class Forme:
    def __init__(self, x, y):
        self._x = x
        self._y = y


class Carre(Forme):
    def __init__(self, x, y, cote):
        super().__init__(x, y)
        self.cote = cote

    def dessiner(self, ecran):
        for i in range(self.cote):
            for j in range(self.cote):
                ecran[self._y + i][self._x + j] = "*"


class Triangle(Forme):
    def __init__(self, x, y, base):
        super().__init__(x, y)
        self.base = base

    def dessiner(self, ecran):
        for i in range(self.base):
            for j in range(self.base * 2):
                if j >= self.base - i - 1 and j <= self.base + i - 1:
                    ecran[self._y + i][self._x + j] = "*"


class Cercle(Forme):
    def __init__(self, x, y, rayon):
        super().__init__(x, y)
        self.rayon = rayon

    def dessiner(self, ecran):
        centre_x = self._x + self.rayon
        centre_y = self._y + self.rayon
        for i in range(2 * self.rayon + 1):
            for j in range(2 * self.rayon + 1):
                distance_centre = math.sqrt(
                    (i - self.rayon) ** 2 + (j - self.rayon) ** 2
                )
                if distance_centre <= self.rayon + 0.5:
                    ecran[self._y + i][self._x + j] = "*"


LARGEUR = 50
HAUTEUR = 20

ecran = [["." for _ in range(LARGEUR)] for _ in range(HAUTEUR)]

formes = [
    Carre(x=1, y=2, cote=3),
    Carre(x=5, y=3, cote=4),
    Triangle(x=10, y=5, base=5),
    Cercle(x=20, y=10, rayon=4),
]
for f in formes:
    f.dessiner(ecran)

for ligne in ecran:
    print(" ".join(ligne))
