def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    '''
    gas = [1,2,3,4,5], cost = [3,4,5,1,2]

    station/index 0:
    gas = 1, next stop = 3
    1 < 3, cant
    
    station/index 1:
    gas = 2, next stop = 4
    2 < 4, cant
    
    station/index 2:
    gas = 3, next stop = 5
    3 < 5, cant
    
    station/index 3:
    gas = 4, next stop = 1
    4 !< 1, can
    
    tank = 0 + 4 = 4
    to station 4: tank = 4 - 1 + 5 = 8
    
    to station 0: tank = 8 - 2 + 1 = 7
    
    to station 1: tank = 7 - 3 + 2 = 6
    
    to station 2: tank = 6 - 4 + 3 = 5
    
    to station 3: tank = 5 - 5 + 4 = 4
    
    
    gas = [2,3,4], cost = [3,4,3]
    
    station/index 0:
    gas = 2, cost = 3
    0 + 2 < 3, cant
    
    station/index 1:
    gas = 3, cost = 4
    0 + 3 < 4, cant
    
    station/index 2:
    gas = 4, cost = 3
    0 + 4 !< 3, can
    
    tank = 0 + 4 = 4
    
    to station 0: tank = 4 - 3 + 2 = 3
    
    to station 1: tank = 3 - 3 + 3 = 3
    
    to station 2: tank = 3 - 4, not possible

    '''
    tank = 0
    for i in range(len(gas)):
        tank = 0
        index = i
        # fuel at starting point
        tank += gas[index]
        while tank >= cost[index]:
            # travel to next station
            tank -= cost[index]

            # looping
            if index == len(gas) - 1:
                index = 0
            else:
                index += 1

            # check
            if tank >= 0 and index == i:
                return i
            elif tank >= 0:
                print("Travel to station "+ str(index) + ". Your tank = " + str(tank + cost[index]) + " - " + str(cost[index]) + " + " + str(gas[index]) + " = " + str(tank + gas[index]))
                tank += gas[index]
            else:
                return -1
    return -1

if __name__ == '__main__':
    # gas = [6, 3, 4]
    # cost = [3, 4, 3]
    print(canCompleteCircuit(gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]))
