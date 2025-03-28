from get_tokens import *
from  data import *

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
    # Reduce operation
    production_index = int(action[1:])
    lhs, rhs = productions[production_index]
    print(f"Reducing using rule {production_index}: {lhs} -> {' '.join(rhs)}")

    # Pop twice for each symbol in RHS (symbol + state)
    for _ in range(len(rhs) * 2):
      stack.pop()

    # Get the new current state
    new_state = stack[-1]

    # Find the goto state
    goto_state = table[new_state][table_column.index(lhs)]
    stack.append(lhs)
    stack.append(int(goto_state))
    print(f"Reduced Stack: {stack}")

  elif action == "Acc":
    print("Parsing succesful. Accepting input.")
    break

  else:
    print("Parsing error. Invalid syntax.")
    break

_name_ == "__main__":
main()