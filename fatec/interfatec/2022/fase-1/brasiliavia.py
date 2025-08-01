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

    def mark_group_as_unsafe(self, element):
        """Marca o grupo do elemento como inseguro."""
        root = self.find(element)
        self.is_unsafe[root] = True

    # 2. CORREÇÃO: Lógica correta para encontrar todas as raízes.
    def get_roots(self):
        """Retorna uma lista de todos os nós que são raízes."""
        return [i for i in range(1, self.count + 1) if self.parents[i] == i]


# --- Lógica Principal ---

people_count = 20
union_find = UnionFind(people_count)

inputs = [
    "c 1 2",
    "c 1 3",
    "c 2 4",
    "n",
    "c 14 7",
    "ns",
    "ni",
    "ii",
    "p 14",
    "ni",
    "ii",
    "c 7 2",
    "ii",
    "ni",
]

for instruction in inputs:
    parts = instruction.split()
    command = parts[0]

    match command:
        case "c":
            union_find.union(int(parts[1]), int(parts[2]))
        case "p":
            union_find.mark_group_as_unsafe(int(parts[1]))
        case "n":
            print(len(union_find.get_roots()))
        case "ns":
            safe_roots = [
                root
                for root in union_find.get_roots()
                if not union_find.is_unsafe[root]
            ]
            print(len(safe_roots))
        case "ni":
            unsafe_roots = [
                root for root in union_find.get_roots() if union_find.is_unsafe[root]
            ]
            print(len(unsafe_roots))
        case "ii":
            insecure_people = []
            for person in range(1, people_count + 1):
                root = union_find.find(person)
                if union_find.is_unsafe[root]:
                    insecure_people.append(str(person))

            if not insecure_people:
                print("vazio")
            else:
                print(" ".join(insecure_people))
