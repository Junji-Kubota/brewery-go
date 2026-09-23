# Brewery GO

東京近郊のクラフトビール醸造所・酒屋を地図で探す個人用アプリ。GitHub Pagesで公開（main ブランチのルート）。

- `index.html` … アプリ本体（Leaflet + MapLibre/OpenFreeMap、CDN読み込み）
- `data/places.js` … 店データ。項目の意味は README.md 参照
- 醸造所のみ金・銀・銅ランク（受賞歴・創業年・手動補正で計算）。酒屋はランクなし
- ビアバー（仕入れて出すだけの店）は対象外。ブルーパブは醸造所に含める
- 「飲んだ」「行きたい」はブラウザの localStorage（キー: beersanpo-v1）に保存。キー名は変えない
- 今後：データの一括収集と定期更新（500件以上を想定）
