from get_tokens import *
from data import *
from tree import *

# Change this from True/False to enable/disable debug log
DEBUG = False


def debug_print(message):
    if DEBUG:
        print(message)


def main():
    input = get_tokens("./test_cases/1.in")

    if not input:
        return

    input.append("$")
    debug_print(input)

    stack = [0]
    cst_stack = []
    input_index = 0

    debug_print(f"Beginning Stack: {stack}")

    while True:
        current_state = stack[-1]
        current_token = input[input_index]
        debug_print(f"Current token: {current_token}")

        action = table[current_state][table_column.index(current_token)]
        debug_print(f"Action: {action}")

        if action is None:
            print("----------ERROR----------")
            print(
                f"Unexpected token '{current_token}' at index {input_index} of {input}\n")
            print(f"Current Stack: {stack}\n")
            print(f"Remaining Input: {input[input_index:]}")
            print("-------------------------")
            return

        if action.startswith('S'):
            state_to_shift = int(action[1:])
            stack.append(current_token)
            stack.append(state_to_shift)

            # Add CST leaf node
            cst_stack.append(tree_node(current_token))

            input_index += 1
            debug_print(f"Shifted Stack: {stack}")

        elif action.startswith('R'):
            production_index = int(action[1:])
            lhs, rhs = productions[production_index]
            debug_print(
                f"Reducing using rule {production_index}: {lhs} -> {' '.join(rhs)}")

            # Pop twice for each symbol in RHS (symbol + state)
            for _ in range(len(rhs) * 2):
                stack.pop()

            # Get new current state
            new_state = stack[-1]
            goto_state = table[new_state][table_column.index(lhs)]
            stack.append(lhs)
            stack.append(int(goto_state))
            debug_print(f"Reduced Stack: {stack}")

            # Create CST node
            num_children = len(rhs)
            children = cst_stack[-num_children:]
            del cst_stack[-num_children:]

            new_node = tree_node(lhs)
            for child in children:
                new_node.add_child(child)

            cst_stack.append(new_node)

        elif action == "Acc":
            debug_print("Parsing successful. Accepting input.\n")
            debug_print("Concrete Syntax Tree:")
            if cst_stack:
                cst_stack[0].print_tree()
            else:
                print("CST is empty.")
            break


if __name__ == "__main__":
    main()
