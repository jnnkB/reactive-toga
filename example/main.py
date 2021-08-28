from reactive_toga import App, State, VerticalStack, Button, Label


class MyApp(App):
    number = State(0)

    def render(self):
        return VerticalStack(
            Button("Add", on_press=self.click_handler), Label(self.number)
        )

    def click_handler(self, widget):
        self.number += 1


if __name__ == "__main__":
    MyApp().main_loop()
