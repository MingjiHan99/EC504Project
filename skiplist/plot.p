f(x) = a * x * log (x) + b * x + c
set title "Time of Querying N elements on SkipList"

set xlabel "Input Size"
set ylabel "Time"

plot "data.txt" using 1:2 title "Time points"
fit f(x) "data.txt" using 1:2 via a, b, c
replot f(x) title "Fitting Curve: O(NlogN)"
set term postscript color
set output "plot.ps"
replot
