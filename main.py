from get_tokens import *
import table

def main():
    input = get_tokens("./test_cases/1.in")
    input.append("$")
    print(input)

    stack = [0]
    index = 0

    print(f"Beginning Stack: {stack}")
    
    while True:
        current_state = stack[-1]
        current_token = input[index]
        print(f"Current token: {current_token}")

        action = table.table[current_state][table.table_column.index(current_token)]
        print(f"Action: {action}")

        if action.startswith('S'):
            state_to_shift = int(action[1:])
            stack.append(current_token)
            stack.append(state_to_shift)
            index += 1
            print(f"Shifted Stack: {stack}")

            
        break
        
    
        

if __name__ == "__main__":
    main()