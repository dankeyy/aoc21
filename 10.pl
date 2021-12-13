%scoresA = qw- ) 3 ] 57 } 1197 > 25137 -;
%scoresB = qw- ( 1 [ 2 { 3 < 4 -;
$pairs = qr"(\(\))|(\{\})|(\[\])|(\<\>)";
$closing = qr"[\)\}\]\>]";


sub first_closing_score {
    my @brackets = split '', shift @_;
    foreach (@brackets) {
        if (exists($scoresA{$_})) {
            return "$scoresA{$_} ";
        }
    }
}

sub score_by_closers {
    my @brackets = split '', reverse(shift @_);
    my $c = 0;
    foreach(@brackets){
        if (exists($scoresB{$_})) {
            $c = $c * 5 + $scoresB{$_};
        }
    }
    return $c;
}

open(FILE, "10.txt") or die "lol";
my $p1 = 0;
my @p2 = 0;

while (<FILE>) {
    1 while ($_ =~ s/${pairs}//g);
    if (m/$closing/) {
        $p1 += first_closing_score($_);
        next;
    }
    push @p2, score_by_closers($_);
}
@p2 = sort { $a <=> $b } @p2;

print "$p1 $p2[@p2/2]";
