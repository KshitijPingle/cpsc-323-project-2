import data

# Gets input string and converts it into an array of tokens.
def get_tokens(filename):
    try:
        with open(filename, "r") as file:
            input = file.read()
            input = input.replace(" ", "").replace("\t", "").replace("\n", "")
            
            tokens = []
            current_token = ""

            for char in input:
                current_token += char
                if current_token in data.valid_tokens:
                    tokens.append(current_token)
                    current_token = ""

            return tokens
    except Exception as e:
        print(f"Error type: {e}")
        print("\nPlease check if the spelling is correct.")
        print('\nEXAMPLE: input = get_tokens("./test_cases/10.in)')