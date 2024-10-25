egg = 2
floor = 4

def solve(egg: int, floorLow: int, floorHigh: int, maxFloor: int, throws: int) -> int:
    print("Egg: {0}, Floor Low: {1}, Floor High: {2}, maxFloor: {3}, Throws: {4}"
          .format(egg, floorLow, floorHigh, maxFloor, throws))
    
    if egg == 0 or floorLow == floorHigh or floorHigh > maxFloor:
        return throws
    
    if egg == 1:
        for i in range(floorLow, floorHigh + 1):
            # I can throw egg from here
            return min(solve(egg-1, i, floorHigh, maxFloor, throws + 1), 
                       solve(egg, i+1, floorHigh, maxFloor, throws + 1))

    if egg > 1:
        for i in range(floorHigh, floorLow, -1):
            # I throw an egg here

            # What can happen?
            # The egg breaks, we move on to the floor below
            return min(solve(egg-1, floorLow, floorHigh - 1, maxFloor, throws+1), 
                       solve(egg, floorLow, floorHigh + 1, maxFloor, throws + 1))

result = solve(egg, 1, floor, floor, 0)

print("Optimal throws = " + str(result))