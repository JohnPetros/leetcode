class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f"Node[value: {self.value} next: {self.next}]"
