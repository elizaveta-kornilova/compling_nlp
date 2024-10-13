MAX_DIFFERENCE = 3
class RopeWalker:
    # Инициализация нового объекта-канатоходца
    def __init__(self):
        self.left_birds = 0
        self.right_birds = 0
        self.fallen = False

    # Канатоходец продолжает движение    
    def is_walking(self):
        return not self.fallen

    # Количество птиц на шесте слева и справа
    def birds_on_pole(self):
        return (self.left_birds, self.right_birds)

    # N птиц садятся на шест слева
    def add_left_birds(self, n):
        if not self.fallen:
            self.left_birds += n
            self._check_balance()

    # N птиц садятся на шест справа
    def add_right_birds(self, n):
        if not self.fallen:
            self.right_birds += n
            self._check_balance()

    # N птиц взлетают с шеста слева
    def remove_left_birds(self, n):
        if not self.fallen:
            self.left_birds = max(0, self.left_birds - n)
            self._check_balance()

    # N птиц взлетают с шеста справа
    def remove_right_birds(self, n):
        if not self.fallen:
            self.right_birds = max(0, self.right_birds - n)
            self._check_balance()
    # Проверка баланса
    def _check_balance(self):
        if (self.left_birds - self.right_birds) > MAX_DIFFERENCE:
            self.fallen = True
            self.left_birds = 0
            self.right_birds = 0

def test():
    print("Тест №1:")
    walker_1 = RopeWalker()
    print(f"Начальные данные: {walker_1.birds_on_pole()}")
    walker_1.add_left_birds(2)
    print(f"Прилетели 2 птицы слева: {walker_1.birds_on_pole()}")
    walker_1.remove_left_birds(2)
    print(f"Улетели 2 птицы слева: {walker_1.birds_on_pole()}")
    walker_1.add_left_birds(2)
    print(f"Прилетели 2 птицы слева: {walker_1.birds_on_pole()}")
    walker_1.add_right_birds(3)
    print(f"Прилетели 3 птицы справа: {walker_1.birds_on_pole()}")
    walker_1.add_left_birds(1)
    print(f"Прилетела 1 птица слева: {walker_1.birds_on_pole()}")

    print("\nТест №2:")
    walker_2 = RopeWalker()
    print(f"Начальные данные: {walker_2.birds_on_pole()}")
    walker_2.add_left_birds(1)
    print(f"Прилетела 1 птица слева: {walker_2.birds_on_pole()}")
    walker_2.add_right_birds(2)
    print(f"Прилетели 2 птицы справа: {walker_2.birds_on_pole()}")
    walker_2.add_left_birds(3)
    print(f"Прилетели 3 птицы слева: {walker_2.birds_on_pole()}")
    walker_2.remove_left_birds(1)
    print(f"Улетела 1 птица слева: {walker_2.birds_on_pole()}")
    walker_2.add_right_birds(1)
    print(f"Прилетела 1 птица справа: {walker_2.birds_on_pole()}")

    print("\nТест №3:")
    walker_3 = RopeWalker()
    print(f"Начальные данные: {walker_3.birds_on_pole()}")
    walker_3.add_left_birds(2)
    print(f"Прилетели 2 птицы слева: {walker_3.birds_on_pole()}")
    walker_3.remove_left_birds(1)
    print(f"Улетела 1 птица слева: {walker_3.birds_on_pole()}")
    walker_3.add_right_birds(2)
    print(f"Прилетели 2 птицы справа: {walker_3.birds_on_pole()}")
    walker_3.add_left_birds(5)
    print(f"Прилетели 5 птиц слева (должен упасть,должно быть по нулям): {walker_3.birds_on_pole()}")
    walker_3.remove_left_birds(2)
    print(f"Улетели 2 птицы слева (канатоходец уже упал, должно быть по нулям): {walker_3.birds_on_pole()}")
    walker_3.add_right_birds(1)
    print(f"Прилетела 1 птица справа (канатоходец уже упал, должно быть по нулям): {walker_3.birds_on_pole()}")

    assert walker_1.is_walking()
    assert walker_1.birds_on_pole() == (3, 3)
    assert walker_2.is_walking()
    assert walker_2.birds_on_pole() == (3, 3)
    assert not walker_3.is_walking()
    assert walker_3.birds_on_pole() == (0, 0)
    
if __name__ == "__main__":
  test()
