    ⍝ d ← 199 200 208 210 200 207 240 269 260 263
    
    ⍝ https://xpqz.github.io/learnapl/io.html - great article on file parsing and stuff
    
    d ← ⍎¨⊃⎕NGET'/home/dankey/dev/aoc21/01.txt' 1

    p1 ← +/ (1↓d) > (¯1↓d)

    p2 ← +/ (3↓d) > (¯3↓d)
