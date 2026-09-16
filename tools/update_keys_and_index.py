#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_keys_and_index.py — reads the questions inside games/*.html and rebuilds
  answer-keys/<game>-answer-key.html   (one printable page per game)
  index.html                           (the front page linking to everything)

Run it after you edit any question in a game file:
    python3 tools/update_keys_and_index.py
"""
import glob
import html
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
POINTS = [100, 200, 300, 400, 500]
ORDER = ['sparta-1', 'sparta-2', 'greek-world-1', 'greek-world-2', 'xerxes-1', 'xerxes-2']


def read_games():
    games = {}
    for path in glob.glob(os.path.join(ROOT, 'games', '*.html')):
        text = open(path, encoding='utf-8').read()
        m = re.search(r'<script id="game-data" type="application/json">\s*(\{.*?\})\s*</script>', text, re.S)
        if not m:
            print('WARNING: no game-data block found in', path)
            continue
        try:
            g = json.loads(m.group(1))
        except json.JSONDecodeError as e:
            print('ERROR: the questions in', os.path.basename(path), 'are not valid JSON:', e)
            print('       (usually a missing comma or an unescaped double quote)')
            continue
        games[g['id']] = g
    ordered = [games[i] for i in ORDER if i in games] + [g for i, g in games.items() if i not in ORDER]
    return ordered


def e(s):
    return html.escape(str(s))


KEY_CSS = '''
  body { font-family: Calibri, "Helvetica Neue", Arial, sans-serif; font-size: 11pt; color: #1b1a17; margin: 24px; background: #fff; }
  h1 { font-size: 18pt; margin: 0 0 2px; color: #1f3a5f; }
  .topic { color: #5a5245; margin-bottom: 12px; }
  table { width: 100%; border-collapse: collapse; }
  th, td { border: 1px solid #b9ad9a; padding: 5px 7px; vertical-align: top; text-align: left; }
  th { background: #e9dfcb; }
  td.pts { text-align: right; white-space: nowrap; }
  td.cat { width: 17%; font-weight: 700; }
  .dp { font-weight: 400; color: #5a5245; font-size: 9pt; margin-top: 3px; }
  tr.final td { background: #fff6dc; }
  .note { margin-top: 10px; color: #5a5245; font-size: 9.5pt; }
  .nav { margin-bottom: 10px; font-size: 10pt; }
  @media print { .nav { display: none; } @page { size: A4 landscape; margin: 12mm; } }
'''


def render_key(g):
    rows = []
    for cat in g['categories']:
        for r, cl in enumerate(cat['clues']):
            catcell = e(cat['name']) + ('<div class="dp">' + e(cat['dotpoint']) + '</div>' if r == 0 else '')
            rows.append('<tr><td class="cat">%s</td><td class="pts">%d</td><td>%s</td><td>%s</td></tr>'
                        % (catcell, POINTS[r], e(cl['q']), e(cl['a'])))
    f = g['final']
    rows.append('<tr class="final"><td class="cat">Final Jeopardy — %s<div class="dp">%s</div></td><td class="pts">wager</td><td>%s</td><td>%s</td></tr>'
                % (e(f['category']), e(f['dotpoint']), e(f['q']), e(f['a'])))
    return '''<!DOCTYPE html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s — answer key</title><style>%s</style></head>
<body>
<div class="nav"><a href="../index.html">← All games</a> · <a href="../games/%s.html">Open this game</a> · <a href="#" onclick="window.print();return false;">Print</a></div>
<h1>%s — answer key</h1>
<div class="topic">%s · NSW Ancient History Stage 6 · each row shows the syllabus dot point the category is built on</div>
<table>
<tr><th>Category</th><th>Pts</th><th>Question</th><th>Answer</th></tr>
%s
</table>
<p class="note">Answers marked "any two" / "any one" accept any of the listed alternatives. Point values rise with difficulty: 100 = core recall, 300 = a specific detail or source, 500 = interpretation, evidence or a historian's view.</p>
</body></html>
''' % (e(g['title']), KEY_CSS, e(g['id']), e(g['title']), e(g['topic']), '\n'.join(rows))


INDEX_CSS = '''
  :root { --bg:#14110f; --panel:#221c19; --gold:#f2c14e; --ink:#f6efe4; --muted:#cbbba7; --accent:#e0b64a; }
  * { box-sizing: border-box; }
  body { margin:0; padding:0 16px 40px; background:var(--bg); color:var(--ink);
         font-family:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif; }
  header { text-align:center; padding:28px 0 16px; border-bottom:10px solid transparent;
    border-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='40' height='10' viewBox='0 0 40 10'><path d='M0 9h6V3h8v6h6V1H4v6h4V5H6M20 9h6V3h8v6h6V1H24v6h4V5h-2' fill='none' stroke='%23e0b64a' stroke-width='1.6'/></svg>") 0 0 10 0 repeat; }
  .brand { font-size:.95rem; letter-spacing:.18em; text-transform:uppercase; color:var(--muted); }
  h1 { margin:6px 0 4px; font-size:clamp(1.9rem,4vw,3rem); color:var(--gold); font-weight:600; }
  .sub { color:var(--muted); font-style:italic; }
  main { max-width:1100px; margin:0 auto; }
  h2 { color:var(--gold); margin:30px 0 10px; font-size:1.5rem; border-bottom:1px solid rgba(255,255,255,.15); padding-bottom:6px; }
  .grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:14px; }
  .card { background:var(--panel); border:2px solid var(--accent); border-radius:12px; padding:16px 18px; }
  .card h3 { margin:0 0 4px; font-size:1.3rem; }
  .card h3 a { color:var(--gold); text-decoration:none; }
  .card h3 a:hover { text-decoration:underline; }
  .card .cats { color:var(--muted); font-size:.95rem; margin:6px 0 10px; line-height:1.35; }
  .card .links a { display:inline-block; margin-right:12px; color:var(--ink); }
  .card .links a.play { background:var(--accent); color:#1b1408; font-weight:700; padding:7px 14px; border-radius:8px; text-decoration:none; }
  .how { background:var(--panel); border-radius:12px; padding:16px 20px; margin-top:26px; color:var(--muted); line-height:1.5; }
  .how b { color:var(--ink); }
  .sparta .card { border-color:#d9a441; } .greek .card { border-color:#e8c56b; } .xerxes .card { border-color:#43c8c0; }
'''


def render_index(games):
    topics = []
    for g in games:
        if g['topic'] not in [t[0] for t in topics]:
            topics.append((g['topic'], g['theme']))
    sections = []
    for topic, theme in topics:
        cards = []
        for g in [x for x in games if x['topic'] == topic]:
            cats = ' · '.join(c['name'] for c in g['categories']) + ' · Final: ' + g['final']['category']
            cards.append('''<div class="card"><h3><a href="games/%s.html">%s</a></h3>
<div class="cats">%s</div>
<div class="links"><a class="play" href="games/%s.html">Play</a><a href="answer-keys/%s-answer-key.html">Answer key</a></div></div>''' % (e(g['id']), e(g['title']), e(cats), e(g['id']), e(g['id'])))
        sections.append('<section class="%s"><h2>%s</h2><div class="grid">%s</div></section>' % (e(theme), e(topic), '\n'.join(cards)))
    return '''<!DOCTYPE html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>HSC Ancient History Jeopardy</title><style>%s</style></head>
<body>
<header>
  <div class="brand">Year 12 Ancient History · Revision</div>
  <h1>HSC Ancient History Jeopardy</h1>
  <div class="sub">Six revision games built on the NESA Ancient History Stage 6 syllabus dot points</div>
</header>
<main>
%s
<div class="how">
<b>How to play.</b> Open a game on the projector, set the number of teams (2–6) and rename them. Teams choose a category and a point value; click the tile to show the clue. Press <b>Show answer</b> (or the A key) to reveal it, use the + / − buttons to award or deduct the points, then <b>Close</b>. Answered tiles grey out. When the board is done, press <b>Final Jeopardy</b>: teams write a wager first, then reveal the clue, and type the wager into the points box before awarding. Scores are remembered by the browser until you press <b>Reset game</b>.<br><br>
<b>Difficulty.</b> 100 points = core recall every student should know; 300 = a specific detail or source; 500 = a historian's view, a piece of evidence, or a link between ideas. No question is repeated anywhere across the six games, so the two games for a topic can be played on different days.
</div>
</main>
</body></html>
''' % (INDEX_CSS, '\n'.join(sections))


def build_keys_and_index():
    games = read_games()
    keys_dir = os.path.join(ROOT, 'answer-keys')
    os.makedirs(keys_dir, exist_ok=True)
    for g in games:
        path = os.path.join(keys_dir, g['id'] + '-answer-key.html')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(render_key(g))
        print('wrote   ', os.path.relpath(path, ROOT))
    with open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(render_index(games))
    print('wrote    index.html')


if __name__ == '__main__':
    build_keys_and_index()
