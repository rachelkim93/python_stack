class Statue:
    def __init__(self, height, color):
        self.height = height
        self.color = color

    def paint(self):
        self.color = color

    def print_attributes(self):
        print(self.height)
        print(self.color)


the_david = Statue("100ft", "pink")
the_david.print_attributes()

# the_david.paint("marble")
# the_david.print_attributes()