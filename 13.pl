use warnings;
use strict;
use feature 'say';
use Data::Dumper;


open(FILE, "13.txt") or die "lol";
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


my ($axis, $n, $x, $y);

foreach (@folds) {
    ($axis, $n) = split /=/, $_;

    splice(@points, 0, scalar @points,
            map {
                if ($axis =~ /y/) {
                    $y = $n;
                    $points[$_][1] > $n
                        ? [$points[$_][0], ($n * 2) % $points[$_][1]]
                        : $points[$_]
                }
                elsif ($axis =~ /x/) {
                    $x = $n;
                    $points[$_][0] > $n
                        ? [($n * 2) % $points[$_][0], $points[$_][1]]
                        : $points[$_]
                }
            } (0..$#points)
    );

    # last; # break if p1
}


sub uniq {
    my %seen;
    grep ! $seen{ Dumper $_ }++, @_;
}
my @uniq_points = uniq(@points);


# p1
say scalar @uniq_points;


# p2, for which we actually have to draw the grid
my (@grid, $i, $j);
foreach (@uniq_points) {
    ($i, $j) = @$_;
    $grid[$i][$j] = '#';
}

for(my $row = 0; $row < $x; $row++) {
    for(my $col = 0; $col < $y; $col++) {
        print defined($grid[$row][$col]) ? '#' : ' ';
    }
    print "\n";
}
