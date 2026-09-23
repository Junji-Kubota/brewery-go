"""data/places.js の形式チェック。使い方: python tools/validate.py"""
import json, re, sys, pathlib

DAYS = "日月火水木金土"
HOURS_PART = re.compile(r"^([日月火水木金土](?:-[日月火水木金土])?)+(\d{1,2}:\d{2}-\d{1,2}:\d{2})(,\d{1,2}:\d{2}-\d{1,2}:\d{2})*$")

def load():
    src = pathlib.Path(__file__).resolve().parent.parent / "data" / "places.js"
    text = src.read_text(encoding="utf-8")
    body = text[text.index("["): text.rindex("]") + 1]
    body = re.sub(r"^\s*//.*$", "", body, flags=re.M)              # コメント行
    body = re.sub(r"([{,]\s*)([A-Za-z_]\w*)\s*:", r'\1"\2":', body)  # キーを引用符で囲む
    body = re.sub(r",\s*([\]}])", r"\1", body)                       # 末尾カンマ
    return json.loads(body)

def main():
    errors, ids = [], set()
    places = load()
    for i, p in enumerate(places):
        tag = f"#{i} {p.get('id')}"
        for k in ("id", "type", "name", "addr", "lat", "lng", "src"):
            if p.get(k) in (None, ""):
                errors.append(f"{tag}: {k} がない")
        if p.get("id") in ids:
            errors.append(f"{tag}: id が重複")
        ids.add(p.get("id"))
        if p.get("type") not in ("brewery", "shop"):
            errors.append(f"{tag}: type は brewery か shop")
        lat, lng = p.get("lat"), p.get("lng")
        if not (isinstance(lat, (int, float)) and 24 <= lat <= 46 and isinstance(lng, (int, float)) and 122 <= lng <= 154):
            errors.append(f"{tag}: 緯度経度が日本の範囲外")
        h = p.get("h")
        if h:
            for part in h.split(";"):
                if not HOURS_PART.match(part):
                    errors.append(f"{tag}: 営業時間の書式が不正 → {part}")
        if p.get("service") not in (None, "shipping"):
            errors.append(f"{tag}: service は shipping のみ")
        if p.get("service") == "shipping" and p.get("h"):
            errors.append(f"{tag}: 出荷専用なのに営業時間がある")
        for a in p.get("awards", []) or []:
            if a.get("c") not in ("JGBA", "IBC", "WBC"):
                errors.append(f"{tag}: 未知の審査会 {a.get('c')}")
    b = sum(1 for p in places if p.get("type") == "brewery")
    nh = sum(1 for p in places if not p.get("h") and p.get("service") != "shipping" and not p.get("closed"))
    ns = sum(1 for p in places if p.get("service") == "shipping")
    nbulk = sum(1 for p in places if p.get("bulk"))
    print(f"{len(places)}件（醸造所{b}・酒屋{len(places)-b}）／出荷専用 {ns}件／一括登録（未確認） {nbulk}件／営業時間 要確認 {nh}件")
    for e in errors:
        print("NG", e)
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
