from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, value=None):
        if value is not None:
            self.root = Node(value)
        else:
            self.root = None

    def preorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if node is None:
            return

        print(node, end=" ")

        if node.left is not None:
            self.preorder_traversal(node.left)

        if node.right is not None:
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if node.left is not None:
            self.inorder_traversal(node.left)

        print(node, end=" ")

        if node.right is not None:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if node.left is not None:
            self.postorder_traversal(node.left)

        if node.right is not None:
            self.postorder_traversal(node.right)

        print(node, end=" ")

    def get_height(self, node=None):
        if node is None:
            node = self.root

        left_height = 0
        right_height = 0

        if node.left:
            left_height = self.get_height(node.left)
        if node.right:
            right_height = self.get_height(node.right)

        if left_height > right_height:
            return left_height + 1
        return right_height + 1

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if node.left is None:
            node.left = Node(value)
        else:
            node.right = self._insert(node.right, value)

        return node

    def insert_many(self, values):
        for value in values:
            self.insert(value)

    # --- NOVA IMPLEMENTAÇÃO DO MÉTODO ---
    def insert_at(self, value, target_index):
        """
        Insere um nó com 'value' no 'target_index' da árvore, se o espaço estiver vazio.
        A indexação é por nível (largura), começando com a raiz no índice 0.
        Retorna True se a inserção for bem-sucedida, False caso contrário.
        """
        new_node = Node(value)

        # Caso 1: Inserindo a raiz (índice 0)
        if target_index == 0:
            if self.root is None:
                self.root = new_node
                return True
            else:
                print(
                    f"Erro: O índice 0 (raiz) já está ocupado pelo valor {self.root.value}."
                )
                return False

        # Se a árvore está vazia, não podemos inserir em outro índice além do 0
        if self.root is None:
            print("Erro: Árvore vazia. Só é possível inserir no índice 0.")
            return False

        # Caso 2: Inserindo em outros índices
        # Precisamos encontrar o nó pai para inserir o novo nó.
        parent_index = (target_index - 1) // 2

        # Usamos BFS para encontrar o nó pai
        queue = deque([(self.root, 0)])
        parent_node = None

        while queue:
            current_node, current_index = queue.popleft()

            if current_index == parent_index:
                parent_node = current_node
                break

            if current_node.left:
                queue.append((current_node.left, 2 * current_index + 1))
            if current_node.right:
                queue.append((current_node.right, 2 * current_index + 2))

        # Se não encontrarmos o pai, a inserção é inválida (árvore não é contígua)
        if parent_node is None:
            print(
                f"Erro: O nó pai para o índice {target_index} não existe. A árvore deve ser preenchida sem 'buracos'."
            )
            return False

        # Determina se o alvo é um filho esquerdo ou direito
        # Filho esquerdo
        if target_index == 2 * parent_index + 1:
            if parent_node.left is None:
                parent_node.left = new_node
                return True
            else:
                print(
                    f"Erro: O índice {target_index} já está ocupado pelo valor {parent_node.left.value}."
                )
                return False
        # Filho direito
        else:  # target_index == 2 * parent_index + 2
            if parent_node.right is None:
                parent_node.right = new_node
                return True
            else:
                print(
                    f"Erro: O índice {target_index} já está ocupado pelo valor {parent_node.right.value}."
                )
                return False

    def __str__(self):
        if self.root is None:
            return "Empty tree"

        result = []

        def preorder_string(node):
            if node is None:
                return
            result.append(str(node))
            preorder_string(node.left)
            preorder_string(node.right)

        preorder_string(self.root)
        return " -> ".join(result)
