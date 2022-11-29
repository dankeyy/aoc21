type RangePoints = number[][];

function parse(s: string): RangePoints {
    return s.substring(13)
            .split(', ')
            .map(sub => sub.substring(2)
                           .split('..')
                           .map(Number));
}


function step(x: number, y: number, xv: number, yv: number) {
    x += xv;
    y += yv;
    xv = xv < 0 ? xv+1 : xv > 0 ? xv-1 : xv; // adjustment due to drag
    yv--;
    return [[x, y], [xv, yv]];
}


function iterateFrom(r: RangePoints, xv: number, yv: number): number | undefined {
    let x = 0, y = 0, maxHeight = 0;
    let [[x0, x1],[y0, y1]] = r;

    while (true) {
        if (x >= x0 && x <= x1 && y >= y0 && y <= y1) {
            return maxHeight;
        }

        else if (x > x1 || y < y0) {
            return undefined;
        }

        else {
            [[x,y], [xv, yv]] = step(x, y, xv, yv);
            maxHeight = y > maxHeight ? y : maxHeight;
        }
    }

}


function solve(s: string) {
    let r: RangePoints = parse(s);
    let height = 0, maxHeight = 0, c = 0;

    // let me bruteforce like a monkey once in a while
    // though after solving it and reading online, i see maxHeight can also be found
    // with the simple formula (-y0) * (-y0-1) / 2
    // that is bc in the end, we reach y=0, which means
    // yv = -y0 -1
    // summing for y with regular sum formula we get the above formula
    // but i think that approach may break for some inputs
    // didnt really think about it a whole lot though so not sure

    for (let i = -500; i < 500; i++) {
        for (let j = -500; j < 500; j++) {
            height = iterateFrom(r, i, j);
            if (height !== undefined) {
                c++;
                maxHeight = height > maxHeight ? height : maxHeight;
            }
        }
    }
    return [maxHeight, c];
}

let test = "target area: x=14..50, y=-267..-225"
// let test = "target area: x=20..30, y=-10..-5"
console.log(solve(test))
