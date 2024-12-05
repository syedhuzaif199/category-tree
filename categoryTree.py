import random

class CategoryTreeIterator:
    def __init__(self, root):
        self.root = root
        self.stack = [{"node":root, "depth":0}]

    def __next__(self):
        if(len(self.stack) > 0):
            next = self.stack.pop()
            self.stack.extend([{"node": child, "depth":next["depth"] + 1} for child in next["node"]["children"][::-1]])
            return next
        else:
            raise StopIteration


class CategoryTree:
    def __init__(self, max_depth = 2, max_children = 2, faker = None, title="Tree"):
        self.title = title
        self.max_depth = max_depth
        self.max_children = max_children

        queue = []

        def word():
            if faker is not None:
                return "_" + faker.word()
            else:
                return ""
        self.root = {"name":"0" + word(), "remDepth":max_depth, "children":[]}
        queue.insert(0, self.root)
        total = 1
        while(len(queue) > 0):
            next = queue.pop()
            remDepth = next["remDepth"]
            if(remDepth <= 0):
                continue

            child_count = random.randint(1, max_children)
            for i in range(child_count):
                child = {"name": str(total) + word(), "remDepth":remDepth - random.randint(1, remDepth), "children":[]}
                total += 1
                queue.insert(0, child)
                next["children"].append(child)

    def __iter__(self):
        return CategoryTreeIterator(self.root)

    def __str__(self):
        out = "-" * (self.max_depth + 20)
        out += "\n" + self.title + "\n"
        out += "-" * (self.max_depth + 20) + "\n"
        for next in self:
            depth = next["depth"]
            next = next["node"]
            out += "| " * depth + next["name"] + "\n"

        return out
    

    
    def __repr__(self):
        return self.__str__()
    
    def render_tree_graphViz(self, dot, out_filepath):
        i = 0
        queue = [[0, self.root]]
        dot.node(str(i), self.root['name'])
        i += 1
        while(len(queue) > 0):
            next = queue.pop()
            nextStr = str(next[0])
            next = next[1]
            for child in next['children']:
                queue.insert(0, [i, child])
                dot.node(str(i), child['name'])
                dot.edge(nextStr, str(i))
                i += 1
        dot.render(out_filepath).replace('\\', '/')
        print("Tree rendered to", out_filepath)