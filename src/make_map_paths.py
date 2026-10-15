import json, math
src=json.load(open('/home/claude/dataofjapan/land/japan.geojson'))
COS=math.cos(math.radians(36)); K=46.0
LON0=128.4; LAT0=45.75
OKI_DLON=5.9; OKI_DLAT=17.45
def proj(lon,lat): return ((lon-LON0)*COS*K, (LAT0-lat)*K)
def rdp(pts,eps):
    if len(pts)<3: return pts
    # iterative RDP
    keep=[False]*len(pts); keep[0]=keep[-1]=True
    stack=[(0,len(pts)-1)]
    while stack:
        a,b=stack.pop(); ax,ay=pts[a]; bx,by=pts[b]; dx,dy=bx-ax,by-ay; L=math.hypot(dx,dy) or 1e-9
        md=-1; mi=-1
        for i in range(a+1,b):
            px,py=pts[i]
            d=abs(dy*px-dx*py+bx*ay-by*ax)/L if L>1e-9 else math.hypot(px-ax,py-ay)
            if d>md: md=d; mi=i
        if md>eps: keep[mi]=True; stack+=[(a,mi),(mi,b)]
    return [p for p,k in zip(pts,keep) if k]
def area(pts): return abs(sum(pts[i][0]*pts[i-1][1]-pts[i-1][0]*pts[i][1] for i in range(len(pts))))/2
out={}; stats=0
for f in src['features']:
    name=f['properties']['nam_ja']; g=f['geometry']
    polys=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
    parts=[]
    for poly in polys:
        ring=poly[0]
        clat=sum(p[1] for p in ring)/len(ring); clon=sum(p[0] for p in ring)/len(ring)
        if name=='東京都' and clat<32: continue          # 小笠原・沖ノ鳥島など（空港なし）を除外
        pts=[proj(lon,lat) for lon,lat in ring]
        if name=='沖縄県':
            ox0,oy0=proj(122.85,27.95)
            pts=[(376+(x-ox0)*1.2, 638+(y-oy0)*1.2) for x,y in pts]   # 右下の枠(x370 y628)に配置
        a=area(pts)
        if a<(0.4 if name=='沖縄県' else 0.6): continue
        s=rdp(pts,0.35)
        if len(s)<3: s=pts[:: max(1,len(pts)//4)]
        if len(s)<3: continue
        parts.append((a,s))
    parts.sort(key=lambda x:-x[0])
    ds=[]
    for a,s in parts:
        d='M'+' '.join('%.1f %.1f'%p for p in s)+'Z'
        ds.append(d.replace('.0 ',' ').replace('.0Z','Z'))
    out[name]=ds
xs=[];ys=[]
for ds in out.values():
    for d in ds:
        nums=d[1:-1].split(' ')
        xs+= [float(v) for v in nums[0::2]]; ys+=[float(v) for v in nums[1::2]]
print('bbox',min(xs),min(ys),max(xs),max(ys))
print('prefs',len(out),'parts',sum(len(v) for v in out.values()))
s=json.dumps(out,ensure_ascii=False,separators=(',',':'))
print('bytes',len(s.encode()))
import pathlib
json.dump(out,open(pathlib.Path(__file__).resolve().parent/'map_paths.json','w'),ensure_ascii=False,separators=(',',':'))
