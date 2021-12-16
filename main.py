from models import Canvas, shapes


def main():
    canvas = Canvas(20, 30, (255, 255, 255))
    s = shapes.Square(1, 3, 3, (0, 100, 222))
    s.draw(canvas)
    canvas.make('a.png')


if __name__ == '__main__':
    main()
