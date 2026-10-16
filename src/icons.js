// 称号のアイコン（オリジナル。48×48の線画）。SVGでもcanvasでも同じ形で描ける
// 形の種類：s=線(ふつうの色) a=線(アクセント色) A=塗り(アクセント色) f=塗り(ふつうの色)
var ICON_SPECS = (function () {
  function C(x, y, r) { return "M" + (x - r) + " " + y + "a" + r + " " + r + " 0 1 0 " + 2 * r + " 0a" + r + " " + r + " 0 1 0 " + -2 * r + " 0z"; }
  function E(x, y, rx, ry) { return "M" + (x - rx) + " " + y + "a" + rx + " " + ry + " 0 1 0 " + 2 * rx + " 0a" + rx + " " + ry + " 0 1 0 " + -2 * rx + " 0z"; }
  function R(x, y, w, h, r) { return "M" + (x + r) + " " + y + "h" + (w - 2 * r) + "a" + r + " " + r + " 0 0 1 " + r + " " + r + "v" + (h - 2 * r) + "a" + r + " " + r + " 0 0 1 " + -r + " " + r + "h" + -(w - 2 * r) + "a" + r + " " + r + " 0 0 1 " + -r + " " + -r + "v" + -(h - 2 * r) + "a" + r + " " + r + " 0 0 1 " + r + " " + -r + "z"; }
  return {
    bag: [["s", R(10, 17, 28, 22, 5)], ["s", "M18 17v-3a3 3 0 0 1 3-3h6a3 3 0 0 1 3 3v3"], ["a", "M18 24v9M30 24v9"], ["A", C(24, 28.5, 2.4)]],
    card: [["s", R(7, 13, 34, 23, 4)], ["A", "M7 19h34v6H7z"], ["s", "M12 31h9M31 31h5"]],
    selfie: [["s", C(20, 29, 12)], ["f", C(16.4, 27, 1.2)], ["f", C(23.6, 27, 1.2)], ["s", "M15.5 32.5q4.5 4 9 0"], ["s", R(30, 5, 12, 20, 3)], ["A", C(36, 10, 1.8)], ["a", "M27 12l-3-3M26 18l-4-1M28 7l-1-4"]],
    compass: [["s", C(24, 24, 16)], ["A", "M34 14L27 27L21 21z"], ["f", "M14 34L21 21L27 27z"], ["s", "M24 6v3M24 39v3M6 24h3M39 24h3"]],
    train: [["s", "M4 32V24a4 4 0 0 1 4-4h16c8 0 14 5 20 12z"], ["s", "M9 25h3M15 25h3M21 25h3"], ["A", "M4 29h38.4l1.6 3H4z"], ["s", C(14, 36.5, 2.6)], ["s", C(33, 36.5, 2.6)], ["s", "M3 42h42"]],
    hand: [["s", C(21, 17, 5.5)], ["s", "M10 42v-7a8 8 0 0 1 8-8h6a8 8 0 0 1 8 8v7"], ["s", "M30 30l6-14"], ["f", C(36.8, 13.6, 2.6)], ["a", "M41 8l2-2M43 14h3M33 7l-1-3"]],
    yawn: [["s", C(23, 27, 14)], ["s", "M16 24q2-2 4 0M26 24q2-2 4 0"], ["A", E(23, 33, 3.6, 4.6)], ["a", "M34 6h7l-7 8h7"]],
    chart: [["s", "M8 8v32h32"], ["a", "M13 14l9 9 6-5 9 12"], ["a", "M30 31h7v-7"]],
    hide: [["s", C(24, 24, 16)], ["A", R(10, 16, 12, 8, 4)], ["A", R(26, 16, 12, 8, 4)], ["s", "M19 33q5 3 10 0"]],
    tee: [["s", "M17 8l-10 7 4 8 6-3v20h14V20l6 3 4-8-10-7q-7 5-14 0z"], ["A", C(24, 28, 3.4)]],
    cookie: [["s", C(24, 24, 16)], ["A", C(18.5, 18.5, 2.4)], ["A", C(29.5, 20.5, 2.4)], ["A", C(21.5, 30, 2.4)], ["A", C(31, 30.5, 1.9)], ["s", "M33 11l3-3"]],
    wine: [["s", "M15 7h18v13a9 9 0 0 1-18 0z"], ["A", "M15 17h18v3a9 9 0 0 1-18 0z"], ["s", "M24 29v11M16 41h16"]],
    dove: [["s", E(22, 26, 13, 9)], ["s", C(34, 15, 5.5)], ["A", "M39.5 14l5 2.2-5 2z"], ["f", C(35.2, 13.8, 1.1)], ["s", "M9 23l-5-3M9 28l-6 1"], ["a", "M14 25q8-8 17-1"], ["s", "M19 35v6M16 41h5M27 35v6M24 41h5"]],
    eagle: [["s", C(21, 27, 15)], ["A", "M32 21c8 0 13 5 13 12-5-4-9-5-14-4z"], ["f", C(25.5, 22, 2.4)], ["a", "M15 15l14 5"], ["a", "M14 8l3 5M21 5l1 6M28 8l-1 4"]],
    angel: [["a", E(24, 9, 8.5, 3.2)], ["s", C(24, 28, 14)], ["s", "M17 27q2-2.4 4 0M27 27q2-2.4 4 0"], ["s", "M19 34q5 4 10 0"]],
    crown: [["s", "M7 34L9 14l10 9 5-12 5 12 10-9 2 20z"], ["A", "M8 38h32v4H8z"], ["A", C(24, 28, 2.4)]],
    lock: [["s", R(12, 21, 24, 19, 4)], ["s", "M17 21v-5a7 7 0 0 1 14 0v5"], ["A", C(24, 30.5, 2.4)]]
  };
})();
// ふつうの画面（SVG）：色はCSS側で決める（.ic-s .ic-a .ic-A .ic-f）
function iconSvg(key) {
  var sp = ICON_SPECS[key] || [];
  return '<svg class="icon" viewBox="0 0 48 48" aria-hidden="true" focusable="false">' + sp.map(function (p) { return '<path class="ic-' + p[0] + '" d="' + p[1] + '"/>'; }).join("") + "</svg>";
}
// シェア画像（canvas）
function drawIcon(g, key, x, y, size, ink, acc) {
  g.save(); g.translate(x, y); g.scale(size / 48, size / 48);
  g.lineWidth = 2.6; g.lineCap = "round"; g.lineJoin = "round";
  (ICON_SPECS[key] || []).forEach(function (p) {
    var path = new Path2D(p[1]);
    if (p[0] === "s") { g.strokeStyle = ink; g.stroke(path); }
    else if (p[0] === "a") { g.strokeStyle = acc; g.stroke(path); }
    else if (p[0] === "A") { g.fillStyle = acc; g.fill(path); }
    else { g.fillStyle = ink; g.fill(path); }
  });
  g.restore();
}
