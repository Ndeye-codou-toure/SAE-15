set terminal png size 800,600
set output 'image.png'
set key inside bottom right
set autoscale
set xlabel 'temps'
set xdata time
set timefmt "%H:%M:%S"
set format x "%H:%M"
set ylabel 'Le taux d occupation'
set title "Evolution du taux d occupation"
plot "Data.txt" using 1:2 title 'Voiture' with linespoints, "Data.txt" using 1:3 title 'Velo' with linespoints