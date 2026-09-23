# Brewery GO

東京近郊のクラフトビール醸造所・酒屋を地図で探す個人用アプリ。GitHub Pagesで公開（main ブランチのルート）。

- `index.html` … アプリ本体（Leaflet + MapLibre/OpenFreeMap、CDN読み込み）
- `data/places.js` … 店データ。項目の意味は README.md 参照
- 醸造所のみ金・銀・銅ランク（受賞歴・創業年・手動補正で計算）。酒屋はランクなし
- ビアバー（仕入れて出すだけの店）は対象外。ブルーパブは醸造所に含める
- 「飲んだ」「行きたい」はブラウザの localStorage（キー: beersanpo-v1）に保存。キー名は変えない
- 今後：データの一括収集と定期更新（500件以上を想定）

## データ更新
- 店データの調査・追加・修正は `.claude/skills/brewery-update/SKILL.md`の手順に従う
- 編集後は必ず `python tools/validate.py` を実行して NG がないことを確認する
- `data/guide203.csv` はビアEXPO2025 出展203社の一覧（ランクの「掲載+3点」の根拠）
