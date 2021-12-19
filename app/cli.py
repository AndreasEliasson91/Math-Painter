from models import canvas as c
from models import shapes as s

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class CLI:
    @staticmethod
    def run():
        canvas = input('First enter the height and the width of your canvas (in pixels x and y), '
                       'separated with a white space. E.g. 20 30 equals 20 height and 30 width\n>> ')
        canvas = tuple([int(i) for i in canvas.split()])

        canvas_color = input('Now enter if the canvas should be white (W) or black (B): W/B\n>> ')
        canvas = c.Canvas(canvas, WHITE if canvas_color.upper() == 'W' else BLACK)

        print('Now let\'s create some colorful shapes!')

        while True:
            while True:
                shape = input(
                    'Do you want to paint a square (S) or a rectangle (R), only S or R are valid inputs:\n>> ')
                if shape.upper() == 'S' or shape.upper() == 'R':
                    break

            rgb = input('Enter the RGB values for the color of your shape: E.g. 255 0 0 makes a bright red color\n>> ')
            color = tuple([int(i) for i in rgb.split()])

            if shape.upper() == 'S':
                width = int(input('Enter the width of your square:\n>> '))
            else:
                width, height = input('Enter the width and the height of your rectangle:\n>> ').split()
                width, height = int(width), int(height)

            x, y = input('And lastly!\nWhere do you want to place your shape at the canvas? '
                         'Enter the x and y value separated with a whitespace:\n>> ').split()
            x, y = int(x), int(y)

            if shape.upper() == 'S':
                shape_to_paint = s.Square(x, y, width, color)
            else:
                shape_to_paint = s.Rectangle(x, y, width, height, color)
            shape_to_paint.draw(canvas)

            another = input('Do you want to paint another shape? Y/N\n>> ')
            if another.upper() == 'N':
                break

        name = input('What dou you want to call this painting?\n>> ')
        name = '../paintings/' + name.lower() + '.png'
        canvas.make(name)
