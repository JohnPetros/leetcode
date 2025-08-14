class UnionFind:
    def __init__(self, elements_count):
        self.count = elements_count
        self.parents = list(range(self.count + 1))
        self.ranks = [0] * (self.count + 1)
        self.is_unsafe = [False] * (self.count + 1)

    def find(self, element):
        if self.parents[element] != element:
            self.parents[element] = self.find(self.parents[element])
        return self.parents[element]

    def union(self, element_x, element_y):
        root_x = self.find(element_x)
        root_y = self.find(element_y)

        if root_x == root_y:
            return

        if self.ranks[root_x] < self.ranks[root_y]:
            self.parents[root_x] = root_y
            self.is_unsafe[root_y] = self.is_unsafe[root_x] or self.is_unsafe[root_y]
        elif self.ranks[root_x] > self.ranks[root_y]:
            self.parents[root_y] = root_x
            self.is_unsafe[root_x] = self.is_unsafe[root_x] or self.is_unsafe[root_y]
        else:
            self.parents[root_y] = root_x
            self.ranks[root_x] += 1
            self.is_unsafe[root_x] = self.is_unsafe[root_x] or self.is_unsafe[root_y]

    def get_roots(self):
        """Retorna uma lista de todos os nós que são raízes."""
        return [i for i in range(1, self.count + 1) if self.parents[i] == i]


union_find = UnionFind(20)
union_find.union(1, 2)
root = union_find.find(2)
print(root)  # 1
