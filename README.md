# HSC Ancient History Jeopardy

Six revision games for Year 12 Ancient History (NSW), two per topic:

| Topic | Game 1 | Game 2 |
|---|---|---|
| Spartan Society to the Battle of Leuctra 371 BC | `games/sparta-1.html` — The State | `games/sparta-2.html` — Society and Culture |
| The Greek World 500–440 BC | `games/greek-world-1.html` — The Persian Wars | `games/greek-world-2.html` — Athens, Empire and Sparta |
| Personalities in their Times — Xerxes | `games/xerxes-1.html` — The Empire and the King | `games/xerxes-2.html` — In Stone, in War and in History |

Every game has 5 categories × 5 clues (100–500 points) plus a Final Jeopardy clue.
Categories are named after the syllabus dot points, and no question is repeated anywhere across the six games.

**Extra game:** `games/sparta-3.html` — Spartan Society: Survey & Government. It covers only the survey
dot point and government (ephorate, gerousia, ekklesia), with 6 categories × 5 clues, a hidden Daily Double
and Final Jeopardy. It is a focused review, so it revisits some core facts from Sparta I. It plays slightly
differently (Space shows the answer, then click the team that earns the points; Escape returns to the board),
and its clues use the fields `clue`, `answer`, `accept`, `dotPoint` and `ref` — the note at the top of the
file explains how to edit them. `tools/update_keys_and_index.py` reads both formats.

Open `index.html` to see all the games in one place.

## Playing a game

Everything runs in the browser from a single file — nothing to install, no internet needed once the page is open.

1. Open the game file (double-click it, or use the link on `index.html`) and put the browser in full screen on the projector.
2. Set the number of teams with the **−** / **+** buttons (2 to 6). Click a team's name to rename it.
3. A team picks a category and a point value. Click the tile: the clue fills the screen.
4. Press **Show answer** (or the **A** key). Use the **+** / **−** buttons next to each team to award or deduct the points, then **Close**. The tile greys out.
5. If you click a tile by mistake, close it and click it again — a greyed tile can be reopened.
6. When the board is finished press **Final Jeopardy**. Teams write their wager first; then press **Reveal the clue**, then **Show answer**. Type each team's wager into the *Points to award* box before pressing their + or −.
7. Scores and the board are remembered by the browser (even if the page is refreshed) until you press **Reset game**.

**Answer key.** Press **Answer key** in the game for a printable list of every question, answer and syllabus dot point, or open the matching file in `answer-keys/`.

## Changing a question

1. Open the game file (for example `games/sparta-1.html`) in a text editor such as TextEdit (choose *Format ▸ Make Plain Text* first) or VS Code.
2. Near the top, find the block that starts `<script id="game-data" type="application/json">`.
3. Each clue looks like this:

   ```
   {"q": "The question the class sees", "a": "The answer you reveal"}
   ```

   Change the words between the quotes. Keep the double quotes, and keep the comma between clues.
   If you need a double quote *inside* a question, write it as `\"`.
4. Save, then reopen the game in the browser. That is all the game needs.
5. To refresh the printed answer keys and the index page as well, open Terminal, `cd` into this folder and run:

   ```
   python3 tools/update_keys_and_index.py
   ```

   If you have broken the format (usually a missing comma), the script will tell you which game and what is wrong.

## Folder guide

```
index.html                 front page linking to every game and answer key
games/                     the six playable games (edit questions here)
answer-keys/               one printable answer key per game (rebuilt by the script)
tools/questions.py         the original questions used to create the games
tools/build_games.py       creates the game files from questions.py (only for a fresh start —
                           running it with --force would overwrite any edits made in games/)
tools/update_keys_and_index.py   rebuilds answer-keys/ and index.html from the current games
```

## Sources

Questions are grounded in the class textbooks and study guides for each topic
(the Spartan Society source study guide, the Greek World 500–440 BC textbook and HSC study guide,
and the Xerxes student booklet) and cross-checked against the class NotebookLM notebooks.
Point values rise with difficulty: 100 = core recall, 300 = a specific detail or source,
500 = a historian's view, a piece of evidence or a link between ideas.
