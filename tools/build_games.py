#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_games.py — creates the six game files in games/ from tools/questions.py,
then builds the answer keys and index.html.

  python3 tools/build_games.py            # creates any game file that does not exist yet
  python3 tools/build_games.py --force    # OVERWRITES all six game files (loses any edits made in games/*.html)

After the first build, edit questions directly inside games/<name>.html (see README.md),
then run  python3 tools/update_keys_and_index.py  to refresh the answer keys and index.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from questions import GAMES            # noqa: E402
from update_keys_and_index import build_keys_and_index   # noqa: E402

TEMPLATE = r'''<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<!--
  ============================================================
  HSC ANCIENT HISTORY JEOPARDY — __TITLE__
  ============================================================
  TO EDIT THE QUESTIONS: scroll down to the block that starts
      <script id="game-data" type="application/json">
  Every question is written like this:
      {"q": "The question the class sees", "a": "The answer you reveal"}
  Keep the double quotes, and keep the comma between items.
  If you need a double quote INSIDE a question, write it as \"
  Each category has five clues in order: 100, 200, 300, 400, 500 points.
  Save the file and reopen it in the browser — that is all.
  Then run  python3 tools/update_keys_and_index.py  to refresh the printed answer key.
  ============================================================
-->
<style>
  :root {
    --bg: #14110f; --panel: #221c19; --tile: #7a1f1f; --tile-hover: #952727;
    --tile-used: #2c2422; --gold: #f2c14e; --ink: #f6efe4; --muted: #cbbba7;
    --accent: #e0b64a; --answer: #ffd98a; --danger: #b23a3a;
  }
  body[data-theme="sparta"] {
    --bg: #160e0d; --panel: #261614; --tile: #7d1d1d; --tile-hover: #9a2626;
    --tile-used: #2e2220; --gold: #f2c14e; --accent: #d9a441; --answer: #ffd98a;
  }
  body[data-theme="greek"] {
    --bg: #0a1a2e; --panel: #12263f; --tile: #1e4a76; --tile-hover: #285d92;
    --tile-used: #1b2a3c; --gold: #f4efe6; --accent: #e8c56b; --answer: #ffe39a;
  }
  body[data-theme="xerxes"] {
    --bg: #100f2c; --panel: #1a1946; --tile: #26307d; --tile-hover: #303d9c;
    --tile-used: #23224a; --gold: #f0c24f; --accent: #43c8c0; --answer: #ffe39a;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }
  body {
    background: var(--bg); color: var(--ink);
    font-family: "Iowan Old Style", "Palatino Linotype", Palatino, "Book Antiqua", Georgia, "Times New Roman", serif;
    min-height: 100vh; padding: 0 16px 32px;
  }
  header {
    text-align: center; padding: 18px 0 10px;
    border-bottom: 10px solid transparent;
    border-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='40' height='10' viewBox='0 0 40 10'><path d='M0 9h6V3h8v6h6V1H4v6h4V5H6M20 9h6V3h8v6h6V1H24v6h4V5h-2' fill='none' stroke='%23e0b64a' stroke-width='1.6'/></svg>") 0 0 10 0 repeat;
  }
  .brand { font-size: .95rem; letter-spacing: .18em; text-transform: uppercase; color: var(--muted); }
  h1 { margin: 6px 0 2px; font-size: clamp(1.8rem, 4vw, 3rem); color: var(--gold); font-weight: 600; letter-spacing: .01em; }
  .sub { color: var(--muted); font-size: clamp(.95rem, 1.6vw, 1.2rem); font-style: italic; }
  .toolbar { margin-top: 12px; display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }
  button {
    font: inherit; cursor: pointer; border: 2px solid var(--accent); background: transparent;
    color: var(--ink); border-radius: 8px; padding: 8px 16px; font-size: 1rem;
  }
  button:hover { background: rgba(255,255,255,.08); }
  button.primary { background: var(--accent); color: #1b1408; border-color: var(--accent); font-weight: 700; }
  button.primary:hover { filter: brightness(1.08); }
  button.danger { border-color: var(--danger); color: #ffb3b3; }
  main { max-width: 1500px; margin: 0 auto; }

  /* ---------- board ---------- */
  .board { display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin: 18px 0 14px; }
  .cat {
    background: var(--panel); border: 2px solid var(--accent); border-radius: 10px;
    padding: 12px 8px; text-align: center; font-weight: 700; color: var(--gold);
    font-size: clamp(.9rem, 1.35vw, 1.3rem); line-height: 1.2; display: flex; align-items: center; justify-content: center;
    min-height: 82px; text-wrap: balance;
  }
  .tile {
    background: var(--tile); color: var(--gold); border: 0; border-radius: 10px;
    font-size: clamp(1.6rem, 3.2vw, 2.9rem); font-weight: 700; padding: 0;
    min-height: clamp(64px, 10.5vh, 110px); box-shadow: inset 0 -6px 0 rgba(0,0,0,.25);
    transition: transform .08s ease, background .15s ease;
  }
  .tile:hover { background: var(--tile-hover); transform: translateY(-2px); }
  .tile.used { background: var(--tile-used); color: rgba(255,255,255,.22); box-shadow: none; font-size: 1.4rem; }
  .tile.used:hover { transform: none; }

  /* ---------- scores ---------- */
  .scores { background: var(--panel); border-radius: 12px; padding: 12px 14px; }
  .scores-head { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; color: var(--muted); }
  .scores-head b { color: var(--ink); }
  .teams { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 10px; margin-top: 10px; }
  .team { background: rgba(0,0,0,.28); border-radius: 10px; padding: 10px 12px; text-align: center; border: 2px solid transparent; }
  .team.leader { border-color: var(--accent); }
  .team .name { font-size: 1.15rem; font-weight: 700; color: var(--gold); outline: none; padding: 2px 6px; border-radius: 6px; }
  .team .name:focus { background: rgba(255,255,255,.1); }
  .team .score { font-size: clamp(1.9rem, 3.4vw, 2.8rem); font-weight: 700; margin: 2px 0 6px; font-variant-numeric: tabular-nums; }
  .team .score.neg { color: #ff9a9a; }
  .team .btns { display: flex; gap: 6px; justify-content: center; }
  .team .btns button { padding: 6px 12px; font-size: 1rem; }
  .hint { color: var(--muted); font-size: .9rem; margin-top: 8px; text-align: center; }

  /* ---------- clue overlay ---------- */
  .overlay {
    position: fixed; inset: 0; background: var(--bg); z-index: 50; display: none;
    flex-direction: column; padding: 16px 24px; overflow: auto;
  }
  .overlay.open { display: flex; }
  .ov-top { display: flex; justify-content: space-between; align-items: center; gap: 12px; color: var(--muted); flex-wrap: wrap; }
  .ov-cat { font-size: clamp(1.1rem, 2vw, 1.6rem); color: var(--gold); font-weight: 700; }
  .ov-pts { font-size: clamp(1.1rem, 2vw, 1.6rem); }
  .ov-body { flex: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 12px 0; }
  .ov-q { font-size: clamp(1.7rem, 3.6vw, 3.4rem); line-height: 1.3; max-width: 1300px; text-wrap: balance; }
  .ov-a {
    margin-top: 28px; font-size: clamp(1.4rem, 2.7vw, 2.5rem); line-height: 1.35; color: var(--answer);
    max-width: 1300px; border-top: 2px solid var(--accent); padding-top: 22px; display: none; text-wrap: balance;
  }
  .ov-a.shown { display: block; }
  .ov-a .lbl { display: block; font-size: 1rem; letter-spacing: .2em; text-transform: uppercase; color: var(--muted); margin-bottom: 8px; }
  .ov-actions { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin-top: 18px; }
  .ov-actions button { font-size: 1.15rem; padding: 12px 22px; }
  .award { margin-top: 16px; background: var(--panel); border-radius: 12px; padding: 12px; }
  .award-head { display: flex; align-items: center; gap: 10px; justify-content: center; flex-wrap: wrap; color: var(--muted); }
  .award-head input { font: inherit; font-size: 1.2rem; width: 120px; text-align: center; border-radius: 8px; border: 2px solid var(--accent); background: rgba(0,0,0,.3); color: var(--ink); padding: 6px; }
  .award-teams { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin-top: 10px; }
  .award-team { display: flex; align-items: center; gap: 6px; background: rgba(0,0,0,.28); border-radius: 10px; padding: 6px 10px; }
  .award-team span { color: var(--gold); font-weight: 700; }
  .award-team button { padding: 6px 12px; }

  /* ---------- answer key view ---------- */
  .key { display: none; background: #fbf7ef; color: #1b1a17; padding: 20px; border-radius: 12px; margin-top: 16px; font-size: .95rem; }
  .key.open { display: block; }
  .key h2 { margin: 0 0 4px; }
  .key table { width: 100%; border-collapse: collapse; margin-top: 12px; }
  .key th, .key td { border: 1px solid #b9ad9a; padding: 6px 8px; vertical-align: top; text-align: left; }
  .key th { background: #e9dfcb; }
  .key td.pts { text-align: right; white-space: nowrap; }
  .key .dp { color: #5a5245; font-size: .85em; }
  .key .kbtns { display: flex; gap: 10px; }
  .key .kbtns button { border-color: #5a5245; color: #1b1a17; }
  body.show-key main, body.show-key header .toolbar { display: none; }

  @media print {
    body { background: #fff; color: #000; padding: 0; }
    header, main, .overlay { display: none !important; }
    .key { display: block !important; border-radius: 0; padding: 0; background: #fff; }
    .key .kbtns { display: none; }
    @page { size: A4 landscape; margin: 12mm; }
  }
  @media (max-width: 700px) {
    .board { gap: 6px; }
    .cat { min-height: 60px; padding: 6px 4px; }
    .tile { min-height: 48px; }
  }
</style>
</head>
<body data-theme="__THEME__">

<!-- ============================================================
     GAME DATA — edit the questions and answers here.
     ============================================================ -->
<script id="game-data" type="application/json">
__DATA__
</script>

<header>
  <div class="brand">HSC Ancient History · Revision Jeopardy</div>
  <h1 id="title"></h1>
  <div class="sub" id="subtitle"></div>
  <div class="toolbar">
    <button class="primary" id="btnFinal">Final Jeopardy</button>
    <button id="btnKey">Answer key</button>
    <button class="danger" id="btnReset">Reset game</button>
  </div>
</header>

<main>
  <section class="board" id="board" aria-label="Game board"></section>
  <section class="scores" id="scores" aria-label="Scoreboard">
    <div class="scores-head">
      <div>Teams: <button id="teamMinus" title="Remove a team">−</button> <b id="teamCount">3</b> <button id="teamPlus" title="Add a team">+</button></div>
      <div>Click a team's name to rename it. Scores are saved in this browser until you press Reset.</div>
    </div>
    <div class="teams" id="teams"></div>
  </section>
  <p class="hint">Click a point tile to open the clue. Show the answer, award the points, then Close. A greyed-out tile can be reopened by clicking it again.</p>
</main>

<div class="overlay" id="overlay" role="dialog" aria-modal="true">
  <div class="ov-top">
    <div class="ov-cat" id="ovCat"></div>
    <div class="ov-pts" id="ovPts"></div>
  </div>
  <div class="ov-body">
    <div class="ov-q" id="ovQ"></div>
    <div class="ov-a" id="ovA"><span class="lbl">Answer</span><span id="ovAText"></span></div>
    <div class="ov-actions">
      <button class="primary" id="btnReveal">Show answer</button>
      <button id="btnClose">Close</button>
    </div>
  </div>
  <div class="award">
    <div class="award-head">Points to award: <input type="number" id="awardPts" step="50"> <span>(change this for a Final Jeopardy wager)</span></div>
    <div class="award-teams" id="awardTeams"></div>
  </div>
</div>

<section class="key" id="key">
  <div class="kbtns"><button id="btnKeyPrint">Print</button><button id="btnKeyBack">Back to game</button></div>
  <h2 id="keyTitle"></h2>
  <div id="keyTopic" class="dp"></div>
  <table id="keyTable"></table>
</section>

<script>
(function () {
  'use strict';
  var GAME = JSON.parse(document.getElementById('game-data').textContent);
  var POINTS = [100, 200, 300, 400, 500];
  var STORE = 'jeopardy:' + GAME.id;

  // ---------- state (saved in this browser) ----------
  var state = load() || freshState();
  function freshState() {
    return { used: {}, finalUsed: false, teams: [{name:'Team 1',score:0},{name:'Team 2',score:0},{name:'Team 3',score:0}] };
  }
  function load() { try { var s = localStorage.getItem(STORE); return s ? JSON.parse(s) : null; } catch (e) { return null; } }
  function save() { try { localStorage.setItem(STORE, JSON.stringify(state)); } catch (e) {} }

  // ---------- header ----------
  document.getElementById('title').textContent = GAME.title;
  document.getElementById('subtitle').textContent = GAME.subtitle;
  document.title = GAME.title;

  // ---------- board ----------
  var board = document.getElementById('board');
  function renderBoard() {
    board.innerHTML = '';
    GAME.categories.forEach(function (cat) {
      var h = document.createElement('div'); h.className = 'cat'; h.textContent = cat.name; board.appendChild(h);
    });
    POINTS.forEach(function (_, r) {
      GAME.categories.forEach(function (cat, c) {
        var key = c + '-' + r;
        var b = document.createElement('button');
        b.className = 'tile' + (state.used[key] ? ' used' : '');
        b.textContent = state.used[key] ? '✓' : POINTS[r];
        b.setAttribute('aria-label', cat.name + ' for ' + POINTS[r]);
        b.onclick = function () { openClue(c, r); };
        board.appendChild(b);
      });
    });
  }

  // ---------- scores ----------
  var teamsEl = document.getElementById('teams');
  function renderTeams() {
    teamsEl.innerHTML = '';
    var top = Math.max.apply(null, state.teams.map(function (t) { return t.score; }));
    state.teams.forEach(function (t, i) {
      var card = document.createElement('div');
      card.className = 'team' + (t.score === top && state.teams.filter(function (x) { return x.score === top; }).length === 1 ? ' leader' : '');
      var name = document.createElement('div'); name.className = 'name'; name.contentEditable = 'true'; name.spellcheck = false; name.textContent = t.name;
      name.onblur = function () { t.name = name.textContent.trim() || ('Team ' + (i + 1)); name.textContent = t.name; save(); renderAward(); };
      name.onkeydown = function (e) { if (e.key === 'Enter') { e.preventDefault(); name.blur(); } };
      var score = document.createElement('div'); score.className = 'score' + (t.score < 0 ? ' neg' : ''); score.textContent = t.score;
      var btns = document.createElement('div'); btns.className = 'btns';
      var minus = document.createElement('button'); minus.textContent = '−100'; minus.onclick = function () { adjust(i, -100); };
      var plus = document.createElement('button'); plus.textContent = '+100'; plus.onclick = function () { adjust(i, 100); };
      btns.appendChild(minus); btns.appendChild(plus);
      card.appendChild(name); card.appendChild(score); card.appendChild(btns);
      teamsEl.appendChild(card);
    });
    document.getElementById('teamCount').textContent = state.teams.length;
  }
  function adjust(i, delta) { state.teams[i].score += delta; save(); renderTeams(); }
  document.getElementById('teamPlus').onclick = function () {
    if (state.teams.length >= 6) return;
    state.teams.push({ name: 'Team ' + (state.teams.length + 1), score: 0 }); save(); renderTeams();
  };
  document.getElementById('teamMinus').onclick = function () {
    if (state.teams.length <= 2) return;
    state.teams.pop(); save(); renderTeams();
  };

  // ---------- clue overlay ----------
  var overlay = document.getElementById('overlay');
  var current = null;   // {c, r} or {final:true}
  function openClue(c, r) {
    var clue = GAME.categories[c].clues[r];
    current = { c: c, r: r };
    showOverlay(GAME.categories[c].name, POINTS[r] + ' points', clue.q, clue.a, POINTS[r]);
  }
  function openFinal() {
    current = { final: true };
    showOverlay('Final Jeopardy — ' + GAME.final.category, 'Teams write down their wagers, then reveal the clue', '', GAME.final.a, 0);
    // The clue is hidden until the teacher reveals it, so wagers can be made first
    var q = document.getElementById('ovQ'); q.textContent = '';
    var rev = document.createElement('button'); rev.className = 'primary'; rev.textContent = 'Reveal the clue';
    rev.onclick = function () { q.textContent = GAME.final.q; };
    q.appendChild(rev);
  }
  function showOverlay(cat, pts, q, a, award) {
    document.getElementById('ovCat').textContent = cat;
    document.getElementById('ovPts').textContent = pts;
    document.getElementById('ovQ').textContent = q;
    document.getElementById('ovAText').textContent = a;
    document.getElementById('ovA').classList.remove('shown');
    document.getElementById('awardPts').value = award;
    renderAward();
    overlay.classList.add('open');
    window.scrollTo(0, 0);
  }
  function renderAward() {
    var wrap = document.getElementById('awardTeams'); wrap.innerHTML = '';
    state.teams.forEach(function (t, i) {
      var box = document.createElement('div'); box.className = 'award-team';
      var nm = document.createElement('span'); nm.textContent = t.name;
      var plus = document.createElement('button'); plus.textContent = '+'; plus.title = 'Correct';
      var minus = document.createElement('button'); minus.textContent = '−'; minus.title = 'Incorrect';
      plus.onclick = function () { adjust(i, pts()); nm.textContent = t.name + ' ✓'; };
      minus.onclick = function () { adjust(i, -pts()); nm.textContent = t.name + ' ✗'; };
      box.appendChild(nm); box.appendChild(plus); box.appendChild(minus); wrap.appendChild(box);
    });
  }
  function pts() { var v = parseInt(document.getElementById('awardPts').value, 10); return isNaN(v) ? 0 : Math.abs(v); }
  document.getElementById('btnReveal').onclick = function () { document.getElementById('ovA').classList.add('shown'); };
  document.getElementById('btnClose').onclick = closeOverlay;
  function closeOverlay() {
    if (current && !current.final) { state.used[current.c + '-' + current.r] = true; }
    if (current && current.final) { state.finalUsed = true; }
    current = null; save(); overlay.classList.remove('open'); renderBoard();
  }
  document.addEventListener('keydown', function (e) {
    if (!overlay.classList.contains('open')) return;
    if (e.key === 'Escape') closeOverlay();
    if (e.key === 'a' || e.key === 'A') document.getElementById('ovA').classList.add('shown');
  });
  document.getElementById('btnFinal').onclick = openFinal;

  // ---------- reset ----------
  document.getElementById('btnReset').onclick = function () {
    if (!confirm('Reset the board and all scores for this game?')) return;
    state = freshState(); save(); renderBoard(); renderTeams();
  };

  // ---------- answer key view ----------
  var key = document.getElementById('key');
  function renderKey() {
    document.getElementById('keyTitle').textContent = GAME.title + ' — answer key';
    document.getElementById('keyTopic').textContent = GAME.topic;
    var t = document.getElementById('keyTable');
    var html = '<tr><th>Category</th><th>Pts</th><th>Question</th><th>Answer</th></tr>';
    GAME.categories.forEach(function (cat) {
      cat.clues.forEach(function (cl, r) {
        html += '<tr><td>' + esc(cat.name) + (r === 0 ? '<div class="dp">' + esc(cat.dotpoint) + '</div>' : '') + '</td><td class="pts">' + POINTS[r] + '</td><td>' + esc(cl.q) + '</td><td>' + esc(cl.a) + '</td></tr>';
      });
    });
    html += '<tr><td>Final Jeopardy — ' + esc(GAME.final.category) + '<div class="dp">' + esc(GAME.final.dotpoint) + '</div></td><td class="pts">wager</td><td>' + esc(GAME.final.q) + '</td><td>' + esc(GAME.final.a) + '</td></tr>';
    t.innerHTML = html;
  }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  document.getElementById('btnKey').onclick = function () { renderKey(); key.classList.add('open'); document.body.classList.add('show-key'); window.scrollTo(0, 0); };
  document.getElementById('btnKeyBack').onclick = function () { key.classList.remove('open'); document.body.classList.remove('show-key'); };
  document.getElementById('btnKeyPrint').onclick = function () { window.print(); };

  renderBoard(); renderTeams();
})();
</script>
</body>
</html>
'''


def render_game(game):
    data = json.dumps(game, ensure_ascii=False, indent=1)
    return (TEMPLATE
            .replace('__TITLE__', game['title'])
            .replace('__THEME__', game['theme'])
            .replace('__DATA__', data))


def main():
    force = '--force' in sys.argv
    games_dir = os.path.join(ROOT, 'games')
    os.makedirs(games_dir, exist_ok=True)
    for g in GAMES:
        path = os.path.join(games_dir, g['id'] + '.html')
        if os.path.exists(path) and not force:
            print('kept    ', os.path.relpath(path, ROOT), '(already exists — use --force to overwrite)')
            continue
        with open(path, 'w', encoding='utf-8') as f:
            f.write(render_game(g))
        print('wrote   ', os.path.relpath(path, ROOT))
    build_keys_and_index()


if __name__ == '__main__':
    main()
