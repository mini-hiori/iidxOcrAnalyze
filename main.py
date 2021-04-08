from split_movie import split_movie
from ocr import ocr
from trim_image import trim_image
from typing import List


def main():
    target_image_path = "movie_frames/0151.jpg"
    trimed_image_path = trim_image(target_image_path)
    image_texts: List[str] = ocr(trimed_image_path)
    print(image_texts)


if __name__ == "__main__":
    main()
