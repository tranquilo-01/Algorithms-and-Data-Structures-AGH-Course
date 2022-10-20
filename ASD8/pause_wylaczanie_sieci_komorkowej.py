# Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w
# Polsce. Jednym z głównych elementów całej procedury jest wyłaczenie wszystkich stacji nadawczych (które
# tworza spójny graf połaczen). Ze wzgledów technologicznych urzadzenia nalezy wyłaczac pojedynczo a operatorowi
# dodatkowo zalezy na tym, by podczas całego procesu wszyscy abonenci znajdujacy sie w zasiegu
# działajacych stacji mogli sie ze soba łaczyc (czyli by graf pozostał spójny). Prosze zaproponowac algorytm
# podajacy kolejnosc wyłaczania stacji.

# 1. zrobic BFSem drzewo dzieci z danego wierzcholka, usuwac po kolei liscie

# 2. preoreder i postorder DFSem, sortujemy wierzchołki po postorder
