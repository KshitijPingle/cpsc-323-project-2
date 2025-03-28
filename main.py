from get_tokens import *
from data import *

def main():
    input = get_tokens("./test_cases/1.in")

    if not input:
        return

    input.append("$")
    print(input)

    stack = [0]
    input_index = 0

    print(f"Beginning Stack: {stack}")

    while True:
        current_state = stack[-1]
        current_token = input[input_index]
        print(f"Current token: {current_token}")

        action = table[current_state][table_column.index(current_token)]
        print(f"Action: {action}")

        if action.startswith('S'):
            state_to_shift = int(action[1:])
            stack.append(current_token)
            stack.append(state_to_shift)
            input_index += 1
            print(f"Shifted Stack: {stack}")
        
        elif action.startswith('R'):
            # Reduce. 
            # Figure out which produciton rule to use
            produciton_index = int(action[1:])
            
            lhs, rhs = productions[produciton_index]
            break

        elif action == "Acc":
            # Accept. We output CST.
            break

        else:
            # Parsing failed.
            break
            
        break # Remove this if necessary. We traverse the element in the input by incrementing the input_index.
        
    
        
# comment
if __name__ == "__main__":
    main()