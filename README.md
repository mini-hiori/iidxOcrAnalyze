# iidxOcrAnalyze
beatmaniaの選曲画面をOCRして情報を取り出す

### 資料
- Vision APIのpythonラッパーの公式ドキュメント
    - https://github.com/googleapis/python-vision
    - https://cloud.google.com/vision/docs/libraries?hl=ja#client-libraries-install-python

- Vision APIはじめかた
    - 全体通し
        - https://valmore.work/cloud-vision-api-ocr/#GCP
        - https://www.asobou.co.jp/blog/web/vision-api
    - GCPの請求を有効にする部分
        - https://cloud.google.com/billing/docs/how-to/modify-project?hl=ja

- python-opencvが動くDockerfile
    - https://qiita.com/narista/items/a3d7d26ae50d54c2553a

- 動画をフレーム単位で画像に分割する
    - https://note.nkmk.me/python-opencv-video-to-still-image/