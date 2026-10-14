# 空港制覇（アプリ版）

国内97空港の「行ったことある」を記録する制覇アプリです。おかきバトルと同じ構成（Web＋Capacitor＋Codemagic）です。

## 中身
- `www/index.html` … アプリ本体（`python3 src/build.py` で src/ から作る）
- `src/` … 画面の元ファイル・空港と地図のデータ・作成スクリプト
- `data_airports_jp.json` … 空港データの元（97空港。公開前に国交省の一覧と照合すること）
- `resources/` … アイコンと起動画面（仮）
- `capacitor.config.json` … アプリ名・ID
- `codemagic.yaml` … Codemagicでのビルド手順（くくノートの設定を流用）

## アプリID
`com.keigosmile.kuukouseiha`（App Store Connectでアプリを登録するときに同じIDを使う）

## ビルドのしかた
1. Codemagicでこのリポジトリを追加する
2. `build` ブランチに main の内容を送ると、iOS版がビルドされてTestFlightに届く
