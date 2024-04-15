from consts import *


def main(argc: int, argv: typing.List[str]):
    try:
        x = float(argv[1])
        y = float(argv[2])
        z = float(argv[3])
    except Exception:
        print("Некорректный ввод")
        sys.exit(-1)

    from main_window import MainWindow
    MainWindow(x, y, z)


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
