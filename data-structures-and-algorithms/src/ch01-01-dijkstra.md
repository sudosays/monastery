# Djikstra's Algorithm

Finds the shortest distances from a source node in a graphs to all other nodes
in the graph. The algorithm may be stopped early when seeking the shortest
distance between two nodes only.

For the purpose of illustration we will be using the problem of determining the
most effective flights from my hometown airport in George, South Africa (blue)
and Vancouver, Canada (red).

![A map](./images/flightmap.svg)
Credit for the base map to [Petr
Dlouhý](https://commons.wikimedia.org/wiki/User:Petr_Dlouh%C3%BD)

The possible flights we can choose from are listed below as well as a made up
"ugh" score (a combination of the flight time and cost).

| From | To  | Ugh |
|------|-----|-----|
| GRJ  | CPT | 1   |
| GRJ  | JHB | 2   |
| CPT  | DXB | 9   | 
| CPT  | JFK | 22  | 
| JHB  | DXB | 10  | 
| JHB  | LHR | 17  | 
| DXB  | LHR | 8   |
| DXB  | JFK | 14  |
| LHR  | YVR | 9   |
| JFK  | YVR | 8   |


