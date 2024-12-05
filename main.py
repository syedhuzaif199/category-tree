import graphviz

from faker import Faker

from categoryTree import CategoryTree 


def main():
    tree = CategoryTree(10, 2, Faker())
   
    print(tree)

    dot = graphviz.Digraph(comment='Category Tree')

    tree.render_tree_graphViz(dot, 'doctest-output/category-tree.gv')
    


if __name__ == "__main__":
    main()
