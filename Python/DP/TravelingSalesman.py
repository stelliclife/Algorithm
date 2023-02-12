def get_traveling_salesman(data):
    temp = []
    result = []

    def find_path(nodes):
        if len(nodes) == 0:
            result.append(temp[:])
            length = len(temp[:])
            cost = 0
            for i in range(length-1):
                cost += temp[i][i+1]
            cost += temp[-1][0]
            result.append(cost)

        for node in nodes:
            target = nodes[:]
            target.remove(node)
            temp.append(node)
            find_path(target[:])
            temp.pop()

    find_path(data)

    length = len(result)
    minimum = result[1]
    n = 0
    for i in range(1, length+1, 2):
        if minimum > result[i]:
            n = i
    route = [data.index(node) for node in result[n-1]]
    return result[n], route