import cv2
import os


def split_movie(target_file: str) -> None:
    """
    target_fileの動画をフレーム単位で分割し、分割結果の画像をmovie_frames以下に保存する
    """
    # ref:https://note.nkmk.me/python-opencv-video-to-still-image/
    cap = cv2.VideoCapture(target_file)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            filename = f"movie_frames/{str(n).zfill(digit)}.jpg"
            cv2.imwrite(filename, frame)
            n += 1
        else:
            return


if __name__ == "__main__":
    save_all_frames("random.mp4")
