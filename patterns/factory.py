class Button:
    html = ""

    def get_html(self):
        return self.html


class Image(Button):
    html = "<img></img>"


class Input(Button):
    html = "<input></input>"


class Flash(Button):
    html = "<obj></obj>"


class ButtonFactory:
    button_types = ["image", "input", "flash"]

    def create_button(self, button_type):
        return getattr(self, button_type)()

    def image(self):
        return Image()

    def input(self):
        return Input()

    def flash(self):
        return Flash()


button_obj = ButtonFactory()

for button_type in ButtonFactory.button_types:
    button = button_obj.create_button(button_type)
    print(button.get_html())

# Output:
# <img></img>
# <input></input>
# <obj></obj>
