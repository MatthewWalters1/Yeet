import map
class array():
    def __init__(self, roads):
        self.edges = []
        x = 0
        for i in roads:
            for path in i.connected:
                x += 1
                print(str(x))
                a = map.edge()
                a.frum = i
                a.to = path
                self.edges.append(a)
    def path(roada, roadb):
        print("hi")
        # here, run dijkstra's algorithm, the edges have random distance variables from 0-10, so it will find the "shortest" path,
        # but it will be pretty random