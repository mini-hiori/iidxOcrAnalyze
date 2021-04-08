from PIL import Image
import cv2


def trim_image(target_filename: str) -> str:
    """
    曲名とクリアレート、フルコンレートだけ残せるように選曲画面画像をトリミングする
    """
    target_image = cv2.imread(target_filename)
    # トリミングの座標指定は選曲画面の画像が1280*720であることが前提
    cv2.resize(target_image, (1280, 720))

    result_file_path = 'clear_rate.jpg'
    im = Image.open(target_filename)
    im_crop = im.crop((0, 150, 700, 500))
    im_crop.save(result_file_path, quality=100)

    # im = Image.open(target_filename)
    # im_crop = im.crop((0, 150, 700, 350))
    # im_crop.save('music_info.jpg', quality=100) # 曲名、ジャンル名、作曲者名だけ欲しい時用
    return result_file_path


if __name__ == "__main__":
    image_trimming("movie_frames/0176.jpg")
