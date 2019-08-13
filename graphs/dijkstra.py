"""
以下图为例：
                     A
                  /  ^  \
               6 /   |   \ 1
                /    |    \
            start    3    end   
                \    |    /
               2 \   |   / 5
                  \  |  /
                     B
    说明：start(起点) 指向 A 和 B，A 和 B 指向 end(终点)，B 指向 A
"""

# 构建图
graph = {}

# 记录各个节点的邻居 (由于要记录邻居是谁，即到达该邻居的开销，所以记录邻居时以字典的形式记录。例：{'start':{'A': 6, 'B': 2}})
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['end'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5

graph['end'] = {}

# 记录开销的散列表
infinity = float('inf')  # 表示无穷大
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['end'] = infinity  # 由于初始时，start 到达不了 end，所以先用无穷大表示

# 记录父节点的散列表
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None

# 记录处理过的节点
processed = []


# 相关的数据准备完成，看一下算法执行过程
"""
1. 只要还有要处理的节点
2. 获取离起点最近的节点
3. 更新其邻居的开销
4. 如果有邻居的开销被更新，同时更新其父节点
5. 将第2步的节点标记为已处理
6. 重复以上过程
"""

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def find_lowest_cost_path():
    node = find_lowest_cost_node(costs)
    while node:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

find_lowest_cost_path()
print(costs, parents)
