class Animal:
    alive = []

    def __init__(self, name: str, hidden: bool = False,
                 health: int = 100) -> None:
        self.name = name
        self.hidden = hidden
        self.health = health
        Animal.alive.append(self)

    def cheak_alive(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore (Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore (Animal):
    def bite(self, prey: Animal) -> None:
        if isinstance(prey, Carnivore):
            return
        if prey.hidden:
            return
        prey.health -= 50
        prey.cheak_alive()
