from PIL import Image
import cv2


def trim_image(target_filename: str) -> str:
    """
    曲名とクリアレートだけ残せるように選曲画面画像をトリミングする
    """
    result_file_path = 'clear_rate.jpg'
    cv2.resize(filename, (1280, 720))  # 座標指定は選曲画面の画像が1280*720であることが前提
    im = Image.open(target_filename)
    im_crop = im.crop((0, 150, 700, 500))
    im_crop.save(result_file_path, quality=100)

    # im = Image.open(target_filename)
    # im_crop = im.crop((0, 150, 700, 350))
    # im_crop.save('music_info.jpg', quality=100) # 曲名、ジャンル名、作曲者名だけ欲しい時用
    return result_file_path


if __name__ == "__main__":
    image_trimming("movie_frames/0176.jpg")
