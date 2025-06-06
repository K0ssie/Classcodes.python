def TowerOfHanoi(n, source, destination_rod, auxiliary_rod  ):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination_rod)
        return
    TowerOfHanoi(n - 1, source, destination_rod, auxiliary_rod)
    print("Move disk ",n ,"from source",  source, "to destination", destination_rod)
    TowerOfHanoi(n - 1,source, auxiliary_rod, destination_rod)
TowerOfHanoi(3, "A", "B", "C")