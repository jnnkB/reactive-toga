import toga
from toga.style.pack import COLUMN


class View:
    _toga: toga.Box

    def render(self):
        return self._toga

    def _update(self):
        print("Update")


class App:
    def __init__(self):
        def startup(app):
            self.app = app
            temp = self.render()._toga
            temp.style.flex = 1
            return toga.Box("main", children=[temp])

        self.app = toga.App("Demo", "org.demo", startup=startup)

    def _update(self):
        main_box = self.app.main_window.content
        main_box.remove(main_box.children[0])
        main_box.refresh()
        temp = self.render()._toga
        temp.style.flex = 1
        main_box.add(temp)

    def main_loop(self):
        self.app.main_loop()


class VerticalStack(View):
    def __init__(self, *view: View):
        self._toga = toga.Box("VerticaclStack")
        self._toga.style.update(direction=COLUMN)
        self._toga.add(*map(lambda x: x._toga, view))


class Button(View):
    def __init__(self, label: str, on_press=lambda x: x):
        self.label = label
        self._toga = toga.Button(label, on_press=on_press)

    def __repr__(self):
        return f"<Button {self.label}>"


class Label(View):
    def __init__(self, label: str):
        self.label = label
        self._toga = toga.Label(label)

    def __repr__(self):
        return f"<Label {self.label}>"
