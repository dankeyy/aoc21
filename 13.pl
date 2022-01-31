use feature 'say';
use Data::Dumper;

open(FILE, "13test01.txt") or die "lol";
my (@points, @folds);

while (<FILE>) {
    chomp($_);

    if ($_ =~ /\d+,\d+/) {
        push @points, [split /,/, $_];
    }

    elsif ($_ =~ /fold along \w=/) {
        $_ =~ s/fold along //g;
        push @folds, $_;
    }
}

my ($dir, $n);

foreach (@folds) {
    ($dir, $n) = split /=/, $_;
    if ($dir =~ /y/) {
        splice(@points, 0, $#points,
               map {
                   $points[$_][1] > $n
                       ? [$points[$_][0], ($n * 2) % $points[$_][1]]
                       : $points[$_]
               } (0 .. $#points-1));
    }

    elsif ($dir =~ /x/) {
        splice(@points, 0, $#points,
               map {
                   $points[$_][0] > $n
                       ? [($n * 2) % $points[$_][0], $points[$_][1]]
                       : $points[$_]
               } (0 .. $#points -1));
    }
    last;
}

sub uniq {
    my %seen;
    grep ! $seen{ Dumper $_ }++, @_
}

say scalar uniq(@points);
