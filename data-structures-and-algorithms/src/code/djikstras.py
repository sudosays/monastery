
"""
We could have used a tuple instead but this is for illustrative purposes
"""
class Flight:
    def __init__(self, destination, ugh):
        self.destination = destination
        self.ugh = ugh

    def __str__(self):
        return "-> %s (%d)" % (self.destination.name, self.ugh)

class Airport:

    def __init__(self, name, flights=None):
        self.name = name
        self.flights = flights

    def __str__(self):
        output = self.name
        if self.flights is not None:
            output += ":"
            for f in self.flights:
                output += "\n" + str(f) 

        return output

def setup():

    YVR = Airport("YVR")
    LHR = Airport("LHR", flights=[Flight(YVR, 9)])
    JFK = Airport("JFK", flights=[Flight(YVR, 8)])
    DXB = Airport("DXB", flights=[Flight(JFK, 14), Flight(LHR, 8)])
    JHB = Airport("JHB", flights=[Flight(LHR, 17), Flight(DXB, 10)])
    CPT = Airport("CPT", flights=[Flight(JFK, 22), Flight(DXB, 9)])
    GRJ = Airport("GRJ", flights=[Flight(CPT, 1), Flight(JHB, 2)])

    return [GRJ, CPT, JHB, DXB, JFK, LHR, YVR]


def djikstras(airports, start, dest):
    ughs = {}
    prev = {}

    for a in airports:
        ughs[a] = float("inf")
        prev[a] = None

    ughs[start] = 0

    visited = []
    unvisited = ughs

    while len(unvisited) > 0:
        
        current = min({airport:ugh for (airport, ugh) in 
            filter(lambda t: t[0] not in visited, ughs.items())},
            key=ughs.get)

        visited.append(current)

        if current == dest:
            break

        for f in current.flights:
           
            temp = ughs[current] + f.ugh
            
            if temp < ughs[f.destination]:
           
                ughs[f.destination] = temp
                prev[f.destination] = current

    return ughs, prev

if __name__ == "__main__":
    
    airports = setup()
    
    ughs, prev = djikstras(airports, airports[0], airports[-1]) 

    flight_path = airports[-1].name
    current = airports[-1]

    while prev[current] is not None:
        flight_path = prev[current].name + "->" + flight_path
        current = prev[current]

    print(flight_path)
