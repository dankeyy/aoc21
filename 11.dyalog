m ← ↑⍎¨¨⊃⎕NGET'/home/dankey/dev/aoc21/11test01.txt'1

reset ← {⍵>9:0 ⋄ ⍵}¨¨⊢
sumAdj ← {+/,⍵}⌺3 3
next ← {reset ⍵ + ⍵{1+ sumAdj 9<⍺+⍵}⍣≡0}

gg ← +/ {+/,0=(next⍣⍵)m}¨⍳100 ⍝ p1
wp ← 0{0=+/,⍵≠0 : ⍺ ⋄ ⍺ + 1 ∇ next ⍵}m ⍝ p2
