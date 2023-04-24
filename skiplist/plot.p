f(x) = a * x * log (x) + b * x + c
set title "Skip List"

set xlabel "Input Size"
set ylabel "Time"

plot "data.txt" using 1:2 title "Time of Querying N elements: O(NlogN)"
fit f(x) "data.txt" using 1:2 via a, b, c
replot f(x) title "Fitting Curve"
set term postscript color
set output "plot.ps"
replot
