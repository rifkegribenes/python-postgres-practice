class linked_list:
    def __init__(self):
        self.root = None

    def add_to_list(self, new_node):
        if self.root:
            new_node.next = self.root
        else:
            self.root = node

    def find(self, name):
        marker = self.root
        while marker:
            if marker.name == name:
                return marker
            try:
                marker = marker.next
            except ValueError:
                print(f"Couldn't find {name}")

