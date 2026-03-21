import keyboard
import pynput
import time

mouse = pynput.mouse.Controller()

class NumPadRangeController:
    def __init__(self):
        self.current_input = []
        self.enter_pressed = False
        self.running = True
        self.panic_key = 'f11'

    def on_key(self, event):
        if event.event_type == keyboard.KEY_DOWN:
            if event.name in [str(i) for i in range(10)]:
                self.current_input.append(event.name)
                print(f"Введено: {''.join(self.current_input)}")

            elif event.name == 'enter':
                self.enter_pressed = True

            elif event.name == 'backspace' and self.current_input:
                self.current_input.pop()
                print(f"Удалено, теперь: {''.join(self.current_input)}")

            elif event.name == 'f12':
                self.running = False
                print("Выход по F12.")

    def calculate_presses(self, distance):
        """100 м = 6 нажатий, +50 м = +2 нажатия"""
        if distance < 100:
            return 0
        steps = (distance - 100) // 50
        presses = round(3 + steps * 2.1)
        return presses

    def press_mouse_button(self, count):
        """Безопасное нажатие кнопки мыши X2 несколько раз"""
        print(f"Нажимаем кнопку мыши X2 {count} раз...\n")
        for i in range(count):
            if keyboard.is_pressed(self.panic_key):
                print("⚠ Аварийная остановка (F11)!")
                break
            mouse.press(pynput.mouse.Button.x2)
            time.sleep(0.05)
            mouse.release(pynput.mouse.Button.x2)
            time.sleep(0.1)

    def process_input(self):
        if self.enter_pressed and self.current_input:
            try:
                distance = int(''.join(self.current_input))
                count = self.calculate_presses(distance)
                print(f"\n=== Установка дальности {distance} м ===")
                print(f"→ Будет выполнено {count} безопасных нажатий X2\n")

                if count > 0:
                    self.press_mouse_button(count)
                else:
                    print("Меньше 100 м — ничего не делаем.")

            except Exception as e:
                print(f"Ошибка: {e}")
            finally:
                self.current_input = []
                self.enter_pressed = False

    def start(self):
        print("=== Контроллер дальности War Thunder ===")
        print("Вводи число (в метрах) и жми Enter.")
        print("F11 — аварийная остановка, F12 — выход.\n")

        keyboard.hook(self.on_key)

        try:
            while self.running:
                self.process_input()
                time.sleep(0.05)
        finally:
            keyboard.unhook_all()
            print("Программа завершена безопасно.")

if __name__ == "__main__":
    NumPadRangeController().start()
