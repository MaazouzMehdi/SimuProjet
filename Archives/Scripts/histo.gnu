reset
set title "Occurrences des digits des decimales de pi"
set xrange [0:9]
set xtics 1
set yrange [0:13000]
set xlabel "digits"
set ylabel "Nombre de résultats"
set style fill solid border -1
 
# Dessin de la courbe
plot 'valeursHisto.dat' with boxes title 'Histogramme'  lc rgb"red"

