from typing import List

class Node:
    def __init__(self, name: str, k: float, link: str):
        self.name = name
        self.k = k
        self.link = link

class Solution:
    def get_nodes(self, a: str, b:str) -> List[Node]:
        result_a = []
        result_b = []
        for node in self.nodes:
            if node.name == a:
                result_a.append(node)
            if node.name == b:
                result_b.append(node)
        return result_a, result_b

    def recursive_calculate(self, a: str, b: str, k:int = 1, except_nodes=None) -> float:
        result = -1.0
        if except_nodes is None:
            except_nodes = []

        for node in self.nodes:
            if node in except_nodes:
                continue
            if node.name == a:
                if node.link == b:
                    result = k * node.k
                    break
                else:
                    except_nodes.append(node)
                    result = self.recursive_calculate(node.link, b, k * node.k, except_nodes)
                    if result != -1.0:
                        break

        return result

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []
        self.nodes = []
        names = []
        for i, n in enumerate(equations):
            cur_value = values[i]
            self.nodes.append(Node(n[0], cur_value, n[1]))
            self.nodes.append(Node(n[1], 1/cur_value, n[0]))
            names.append(n[0])
            names.append(n[1])

        for q in queries:
            if q[0] not in names or q[1] not in names:
                result.append(-1.0)
            else:
                result.append(self.recursive_calculate(q[0], q[1]))

        return result

equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

print(Solution().calcEquation(equations, values, queries))