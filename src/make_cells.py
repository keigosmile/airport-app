# 空港ごとの「なわばり」（同じ都道府県の中で一番近い空港の範囲）を作る
# python3 src/make_cells.py  → src/airport_geo.json
import csv, json, math, pathlib
root = pathlib.Path(__file__).resolve().parent
COS = math.cos(math.radians(36)); K = 46.0; LON0 = 128.4; LAT0 = 45.75
def proj(lon, lat): return ((lon - LON0) * COS * K, (LAT0 - lat) * K)
def proj_pref(pref, lon, lat):
    x, y = proj(lon, lat)
    if pref == "沖縄県":
        ox, oy = proj(122.85, 27.95)
        x, y = 376 + (x - ox) * 1.2, 638 + (y - oy) * 1.2
    return x, y

airports = json.load(open(root.parent / "data_airports_jp.json", encoding="utf-8"))["airports"]
src = pathlib.Path("/home/claude/ourairports-data/airports.csv")
rows = list(csv.DictReader(open(src, encoding="utf-8")))
by_iata = {r["iata_code"]: r for r in rows if r["iso_country"] == "JP" and r["iata_code"]}
by_ident = {r["ident"]: r for r in rows if r["iso_country"] == "JP"}
EXTRA = {"REBUN": "RJCR", "NIIJIMA": "RJAN", "KOZUSHIMA": "RJAZ", "OJIKA": "RJDO", "KAMIGOTO": "RJDK",
         "CHOFU": "RJTF", "KONAN": "RJBK", "KENOU": "JP-0007", "YAO": "RJOY", "CHITOSE": "RJCJ"}
ll = {}
for a in airports:
    r = by_iata.get(a["iata"]) if a["iata"] else by_ident.get(EXTRA[a["id"]])
    if r is None: r = by_ident[EXTRA[a["id"]]]
    ll[a["id"]] = (float(r["longitude_deg"]), float(r["latitude_deg"]))

# 都道府県の形の中に入っているか確認（座標の取り違え防止）
geo = json.load(open("/home/claude/dataofjapan/land/japan.geojson", encoding="utf-8"))
shapes = {f["properties"]["nam_ja"]: (f["geometry"]["coordinates"] if f["geometry"]["type"] == "MultiPolygon" else [f["geometry"]["coordinates"]]) for f in geo["features"]}
def inside(lon, lat, polys):
    for poly in polys:
        ring = poly[0]; c = False; j = len(ring) - 1
        for i in range(len(ring)):
            xi, yi = ring[i]; xj, yj = ring[j]
            if (yi > lat) != (yj > lat) and lon < (xj - xi) * (lat - yi) / (yj - yi + 1e-12) + xi: c = not c
            j = i
        if c: return True
    return False
def near(lon, lat, polys, km=3.0):
    for poly in polys:
        for x, y in poly[0]:
            if math.hypot((x - lon) * 91, (y - lat) * 111) < km: return True
    return False
for a in airports:
    lon, lat = ll[a["id"]]
    if not inside(lon, lat, shapes[a["pref"]]) and not near(lon, lat, shapes[a["pref"]]):
        raise SystemExit("県の外にある: %s %s %s" % (a["id"], a["name"], (lon, lat)))

def clip(poly, px, py, qx, qy):
    # p より q に近い側を捨てる（p側の半平面で切り取る）
    mx, my = (px + qx) / 2, (py + qy) / 2; nx, ny = qx - px, qy - py
    def side(pt): return (pt[0] - mx) * nx + (pt[1] - my) * ny
    out = []
    for i in range(len(poly)):
        a, b = poly[i - 1], poly[i]; sa, sb = side(a), side(b)
        if sb <= 0:
            if sa > 0:
                t = sa / (sa - sb); out.append((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t))
            out.append(b)
        elif sa <= 0:
            t = sa / (sa - sb); out.append((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t))
    return out
BOX = [(-50, -50), (820, -50), (820, 920), (-50, 920)]
def cells(only_active):
    res = {}
    prefs = {}
    for a in airports:
        if only_active and a["status"] != "active": continue
        prefs.setdefault(a["pref"], []).append(a)
    for p, lst in prefs.items():
        pts = {a["id"]: proj_pref(p, *ll[a["id"]]) for a in lst}
        for a in lst:
            poly = BOX[:]
            px, py = pts[a["id"]]
            for b in lst:
                if b["id"] == a["id"]: continue
                qx, qy = pts[b["id"]]
                if abs(qx - px) < 1e-6 and abs(qy - py) < 1e-6: continue
                poly = clip(poly, px, py, qx, qy)
            res[a["id"]] = "M" + " ".join("%.1f %.1f" % q for q in poly) + "Z"
    return res
out = {
    "pt": {a["id"]: [round(v, 1) for v in proj_pref(a["pref"], *ll[a["id"]])] for a in airports},
    "all": cells(False),
    "active": cells(True),
}
(root / "airport_geo.json").write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print("ok", len(out["pt"]), len(out["all"]), len(out["active"]))
