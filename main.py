from pioneer_sdk import Pioneer, Camera
from edubot_sdk import EdubotGCS

import cv2
import sys


def main():
    args = sys.argv[1:]
    if len(args) < 3:
        print(
            "Не переданы необходимые аргументы: порт Пионера, порт камеры Пионера, порт Геобота. Пример: python main.py 8000 18000 8001"
        )
        exit(1)

    pioneer = Pioneer(ip="127.0.0.1", mavlink_port=int(args[0]))
    pioneer_camera = Camera(ip="127.0.0.1", port=int(args[1]))
    geobot = EdubotGCS(ip="127.0.0.1", mavlink_port=int(args[2]))


if __name__ == "__main__":
    main()
