# www/index.html を作る：python3 src/build.py
import pathlib
root = pathlib.Path(__file__).resolve().parent
t = (root / "index.template.html").read_text(encoding="utf-8")
t = t.replace("__AIRPORTS__", (root / "airports_compact.json").read_text(encoding="utf-8").strip())
t = t.replace("__MAP__", (root / "map_paths.json").read_text(encoding="utf-8").strip())
t = t.replace("__GEO__", (root / "airport_geo.json").read_text(encoding="utf-8").strip())
# アプリ用：完全なHTML文書
doc = '<!doctype html>\n<html lang="ja">\n<head>\n<meta charset="utf-8">\n' + t.replace("<script>", "</head>\n<body>\n<script>", 0)
head_end = t.index("</style>") + len("</style>")
doc = '<!doctype html>\n<html lang="ja">\n<head>\n<meta charset="utf-8">\n' + t[:head_end] + "\n</head>\n<body>\n" + t[head_end:] + "\n</body>\n</html>\n"
(root.parent / "www" / "index.html").write_text(doc, encoding="utf-8")
# プレビュー用（Claudeのアーティファクト）：本文だけ
(root / "preview.html").write_text(t, encoding="utf-8")
print("www/index.html と src/preview.html を作成しました")
