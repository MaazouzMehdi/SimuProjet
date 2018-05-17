reset
set title "nombre de digits différents par paquet de 5 décimales"
set xrange [0:6]
set xtics 1
set yrange [0:105000]
set ytics 5000
set xlabel "digits"
set ylabel "Nombre de résultats"
set style fill solid border -1
 
# Dessin de la courbe
plot 'pokerValues.dat' with boxes title 'Histogramme'  lc rgb"red"

