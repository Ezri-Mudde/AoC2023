from typing import Dict, Optional


class Node:
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def __init__(self, name: str) -> None:
        self.name = name


def traverse_input(file_name: str) -> None:
    nodes: Dict[str, Node] = {}

    def get_node(node_name: str) -> Node:
        if node_name not in nodes:
            node = Node(node_name)
            nodes[node_name] = node
        else:
            node = nodes[node_name]
        return node

    with open(file_name, "r") as f:
        lines = f.readlines()
        instructions = lines[0].strip()

        for line in lines[2:]:
            node_name, left_right = line.split(" = ")
            left_right = left_right[1:-2]
            left, right = left_right.split(", ")

            node = get_node(node_name)
            node.left = get_node(left)
            node.right = get_node(right)

        done = False
        node = get_node("AAA")
        count = 0
        while not done:
            for instruction in instructions:
                count += 1
                print(f"At node {node.name}", end="")
                if instruction == "L":
                    node = node.left
                elif instruction == "R":
                    node = node.right
                print(f" instruction {instruction} goes to {node.name}")
                if node.name == "ZZZ":
                    done = True
                    break
        print(f"file {file_name} took {count}")


if __name__ == "__main__":
    traverse_input("day8/test_input")
    traverse_input("day8/input")
