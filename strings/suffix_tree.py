class Edge:
    __slots__ = ['index', 'size']
    
    def __init__(self, index, size):
        self.index = index
        self.size = size
    
    def __hash__(self):
        return hash(text[self.index])
    
    def __eq__(self, other):
        return text[self.index] == text[other.index]


def find_right_edge(tree, edge):
    keys = tree.keys()
    for key in keys:
        if key == edge:
            return key


def get_overlap(suffix, old_edge):
    i = 0
    while i < old_edge.size and suffix.index + i < text_len and \
        old_edge.index + i < text_len and \
        text[suffix.index + i] == text[old_edge.index + i]:
        i += 1
    return i


def build_suffix_tree():
    tree = {}
    current_length = 0
    for begin_of_suffix in range(text_len):
        current_node = 0
        suff_len = text_len - begin_of_suffix
        suffix = Edge(begin_of_suffix, suff_len)
        while current_node in tree and suffix in tree[current_node]:
            prev_node = current_node
            current_node = tree[current_node][suffix]
            prev_edge = find_right_edge(tree[prev_node], suffix)
            overlap = get_overlap(suffix, prev_edge)
            suffix.index += overlap
            suffix.size -= overlap
            if suffix.index >= text_len:
                break
            if prev_edge.size == overlap:
                continue
            else:
                current_length += 1
                new_node = current_length
                current_node = new_node
                
                edge_from_new_node = Edge(prev_edge.index + overlap, prev_edge.size - overlap)
                edge_to_new_node = Edge(prev_edge.index, overlap)
                
                tree[new_node] = {}
                tree[new_node][edge_from_new_node] = tree[prev_node].pop(prev_edge)
                tree[prev_node][edge_to_new_node] = new_node
                break

        current_length += 1
        if suffix.index < text_len:
            if current_node not in tree:
                tree[current_node] = {}
            tree[current_node][suffix] = current_length
    return tree


def print_all_edges(tree, text):
    for node in tree:
        for s in tree[node]:
            print(text[s.index:s.index + s.size])


text = input()
text_len = len(text)
tree = build_suffix_tree()
print_all_edges(tree, text)
