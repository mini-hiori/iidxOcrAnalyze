from split_movie import split_movie
from ocr import ocr
from trim_image import trim_image
from typing import List
import Levenshtein
import re


def main():
    for i in range(50):
        image_number: str = str(i + 150).zfill(2)
        target_image_path = f"movie_frames/0{image_number}.jpg"
        trimed_image_path = trim_image(target_image_path)
        image_texts: List[str] = ocr(trimed_image_path)
        music_name = search_music_name(image_texts)
        clear_rate = search_clear_rate(image_texts)
        fullcombo_rate = search_fullcombo_rate(image_texts)
        # print(image_texts)
        print(image_number)
        print(f"music_name:{music_name}")
        print(f"clear_rate:{clear_rate}")
        print(f"full_combo_rate:{fullcombo_rate}")
        print()


def search_music_name(detected_texts: List[str]) -> str:
    """
    detected_texts(画像認識で見つかった単語のlist)の中で最も曲名っぽい文字列を返却する
    """
    # IIDXに存在する曲名をmusic_list.txtにあらかじめ保存しておく
    with open("music_list.txt", "r", encoding="utf-8") as f:
        music_list = f.read().split("\n")
    max_score: float = -1
    candidate: str = ""

    for music_name in music_list:
        for text in detected_texts:
            if not text or not music_name:
                continue
            distance = Levenshtein.distance(music_name, text)
            # もっとも曲名っぽい→マッチ文字列ができるだけ長くて差分が少ない
            score = (len(music_name) + len(text)) / 2 - distance
            if score > max_score:
                max_score = score
                candidate = music_name
    return candidate


def search_clear_rate(detected_texts: List[str]) -> str:
    """
    detected_texts(画像認識で見つかった単語のlist)の中で最もクリアレートっぽい文字列を返却する
    """
    candidates: List[float] = []
    for i in detected_texts:
        # 数字の読み取りで0→O、1→Iに化けることがままあるので、それを考慮
        if re.match(r"^[0-9OI¥. ]+%$", i):
            percentage = float(
                i.replace(
                    "%",
                    "").replace(
                    "O",
                    "0").replace(
                    "I",
                    "1"))
            candidates.append(percentage)
    if candidates:
        clear_rate = str(max(candidates)) + "%"
    else:
        clear_rate = ""
    return clear_rate


def search_fullcombo_rate(detected_texts: List[str]) -> str:
    """
    detected_texts(画像認識で見つかった単語のlist)の中で最もクリアレートっぽい文字列を返却する
    """
    candidates: List[float] = []
    for i in detected_texts:
        if re.match(r"^[0-9OI¥. ]+%$", i):
            percentage = float(
                i.replace(
                    "%",
                    "").replace(
                    "O",
                    "0").replace(
                    "I",
                    "1"))
            candidates.append(percentage)
    if candidates:
        fullcombo_rate = str(min(candidates)) + "%"
    else:
        fullcombo_rate = ""
    return fullcombo_rate


if __name__ == "__main__":
    main()
