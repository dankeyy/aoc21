
m ← ↑⍎¨¨⊃⎕NGET'/home/dankey/dev/aoc21/11test01.txt'1

reset ← {⍵>9:0 ⋄ ⍵}¨¨⊢
sumAdj ← {+/,⍵}⌺3 3
next ← {reset ⍵ + ⍵{1+ sumAdj 9<⍺+⍵}⍣≡0}
count0s ← {+/,⍵=0}
allNot0 ← {0= +/,⍵≠0}
sum0Upto ← {+/ {count0s (next⍣⍵) m}¨⍳⍵}

gg ← sum0Upto 100 ⍝ p1
wp ← acc←0 ⋄ acc⊣{next ⍵ ⊣ acc+←1}⍣allNot0 m +1 ⍝ p2
