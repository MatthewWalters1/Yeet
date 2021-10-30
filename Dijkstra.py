def array(roads):
    def __init__(self, roads):
        self.edges = []
        for i in roads:
            for path in i.connected:
                a = map.edge()
                a.frum = i
                a.to = path
                self.edges.append(a)
    def path(roada, roadb):
        print("hi")
        # here, run dijkstra's algorithm, the edges have random distance variables from 0-10, so it will find the "shortest" path,
        # but it will be pretty random