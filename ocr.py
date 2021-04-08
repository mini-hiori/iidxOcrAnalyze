import os
import json
from google.cloud import vision
from typing import List


def ocr(target_file_path: str) -> List[str]:
    """
    画像認識して認識できた単語をlist[str]で返却する
    googleのOCRAPI使っているので、あまり使いすぎるとコストがかかることに注意
    """
    google_credential_path = 'credential.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = google_credential_path

    client = vision.ImageAnnotatorClient()

    with open(target_file_path, 'rb') as f:
        image_binary = f.read()

    image = vision.Image(content=image_binary)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    result_texts: list[str] = []
    for text in texts:
        result_texts.append(text.description)
    if result_texts:
        # OCR結果の先頭に全体から読み取れた文すべてが改行区切りで入っている。
        # これを分割してOCR結果の単語として追加する
        result_texts = result_texts[1:] + result_texts[0].split("\n")
        result_texts = list(set(result_texts))
    # なんかよくわからんけど弱とか強とかのノイズが混じるので除く
    noizes = (
        "BEGINNER",
        "NORMAL",
        "HYPER",
        "ANOTHER",
        "LEGGENDARIA",
        "PLAY",
        "RATE",
        "CLEAR",
        "FULL",
        "COMBO",
        "CHARGE",
        "PLAY STYLE",
        "CLEAR RATE",
        "FULL COMBO RATE",
        "弱",
        "強",
        ",強",
        "|強",
        "強,",
        "*",
        "弱,",
        "&",
        "|",
        ",",
        "%",
        ""
    )
    return [i for i in result_texts if i not in noizes]


if __name__ == "__main__":
    analyze_image()
