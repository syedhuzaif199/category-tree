import graphviz

from faker import Faker

from categoryTree import CategoryTree 


def main():
    named_tree = CategoryTree(10, 2, Faker(), 'Named Tree')
   
    print(named_tree)

    dot = graphviz.Digraph(comment='Named Tree')

    named_tree.render_tree_graphViz(dot, 'output/named-tree.svg')
    
    # tree without faker

    dot = graphviz.Digraph(comment='Nameless Tree')

    nameless_tree = CategoryTree(10, 2, None, 'Nameless Tree')

    print(nameless_tree)

    nameless_tree.render_tree_graphViz(dot, "output/nameless-tree.svg")
    

if __name__ == "__main__":
    main()
