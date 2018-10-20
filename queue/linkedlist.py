class LinkedList:
    """
    You should implement the methods of this class which are currently
    raising a NotImplementedError!
    Don't change the name of the class or any of the methods.
    """
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_start_to_list(self, node):
        """
        You can reuse the method written for the previous assignment here.

        :param node: the node to add at the start
        :return: None
        """
        if self.__root:
            node.set_next(self.__root)
        self.__root = node

    def remove_end_from_list(self):
        """
        Implement this method! It should:
        - Iterate over each node
        - Find both the second-to-last node and the last node
        - Set the second-to-last node's next to be None
        - Return the last node
        :return: the removed Node.
        """
        marker = self.__root

        if not marker.get_next():
            self.__root = None
            return marker

        while marker:
            following_node = marker.get_next()
            if following_node:
                if not following_node.get_next():
                    marker.set_next(None)
                    return following_node
            marker = marker.get_next()

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, name):
        """
        You can reuse the method written for the previous assignment here.

        :param name: the name of the Node to find.
        :return: the found Node, or raises a LookupError if not found.
        """
        marker = self.__root
        while marker:
            if marker.name == name:
                return marker
            marker = marker.get_next()
        raise LookupError(f"Name {name} not found")

    def size(self):
        """
        You should implement this method!
        It should return the amount of Nodes in the list.
        :return: the amount of nodes in this list.
        """
        marker = self.__root
        count = 0
        while marker:
            count += 1
            marker = marker.get_next()
        return count
