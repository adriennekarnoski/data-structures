"""Create a Graph class data structure."""
from stack import Stack


class Graph(object):
    """Graph object."""

    def __init__(self):
        """Graph things on initialization."""
        self._nodes = {}

    def nodes(self):
        """List all nodes in the Graph."""
        return [key for key in self._nodes]

    def edges(self):
        """List all edges in the Graph."""
        edge_list = []
        for node, value in self._nodes.items():
            for edge, weight, in value.items():
                edge_list.append([node, edge])
        return [y for x in edge_list for y in x]

    def add_node(self, *args):
        """Add a new node to the Graph."""
        for arg in args:
            self._nodes.setdefault(arg, {})

    def add_edge(self, val1, val2, weight):
        """Add a new edge to the Graph and connects the values.

        If either value doesn't exist they will be created.
        """
        self.add_node(val1, val2)
        if val2 in self._nodes[val1]:
            pass
        else:
            self._nodes[val1].update({val2: weight})

    def del_node(self, val):
        """Delete the node containing the given value."""
        if self.has_node(val):
            del self._nodes[val]
        else:
            raise KeyError("No such Node exists")
        for key in self._nodes:
            if val in list(self._nodes[key]):
                self._nodes[key].pop(val)

    def del_edge(self, val1, val2):
        """Delete the edge connecting the two values."""
        try:
            for node in self._nodes[val1]:
                if val2 == node:
                    self._nodes[val1].pop(node)
                    return
            raise IndexError("No connection between those two Nodes.")
        except KeyError:
            raise KeyError("No Node with given first value.")

    def has_node(self, val):
        """Return True is node containing value exists in Graph."""
        return True if val in self._nodes else False

    def neighbors(self, val):
        """Return list of all nodes connected to node containing the value."""
        if self.has_node(val):
            return list(self._nodes[val].keys())
        else:
            raise KeyError("No such Node exists")

    def adjacent(self, val1, val2):
        """Return True if there is an edge connecting the two values."""
        if self.has_node(val1) and self.has_node(val2):
            try:
                if self._nodes[val1][val2]:
                    return True
            except KeyError:
                return False
        else:
            raise KeyError('Both nodes are not present in graph')

   