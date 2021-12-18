m ← ↑⍎¨¨⊃⎕NGET'/home/dankey/dev/aoc21/11test01.txt'1

reset ← {⍵>9:0 ⋄ ⍵}¨¨⊢
sumAdj ← {+/,⍵}⌺3 3
next ← {reset ⍵ + ⍵{1+ sumAdj 9<⍺+⍵}⍣≡0}
count0s ← {+/,⍵=0}
all0 ← {0= +/,⍵≠0}
sum0sUpto ← {+/ {count0s (next⍣⍵) m}¨⍳⍵}

gg ← sum0sUpto 100 ⍝ p1
wp ← acc←0 ⋄ acc⊣{next ⍵ ⊣ acc+←1}⍣all0 m +1 ⍝ p2


⍝ alternatively
gg ← +/ {+/,0=({{⍵>9:0 ⋄ ⍵}¨¨⊢⍵ + ⍵{1+ {+/,⍵}⌺3 3 9<⍺+⍵}⍣≡0}⍣⍵) m}¨⍳100
wp ← 0{0=+/,⍵≠0 : ⍺ ⋄ ⍺ + 1 ∇ next ⍵}m
