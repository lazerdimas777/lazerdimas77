class Pet:
    def __init__(self, name, age, breed, health=100):
        self.name = name
        self.age = age
        self.breed = breed
        self.health = health

    def eat(self):
        print(f"{self.name} їсть смачненьке!")
        self.health += 5

    def sleep(self):
        print(f"{self.name} солодко спить...")
        self.health += 10

    def play(self):
        print(f"{self.name} грається з іграшкою!")
        self.health -= 2

    def get_sick(self):
        print(f"{self.name} захворів!")
        self.health -= 10

    def is_healthy(self):
        if self.health > 70:
            return "Здоров'я відмінне!"
        elif self.health > 50:
            return "Почувається непогано."
        else:
            return "Потрібно звернутися до ветеринара!"

    def __str__(self):
        return f"Ім'я: {self.name}\nВік: {self.age}\nПорода: {self.breed}\nЗдоров'я: {self.health}"