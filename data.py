valid_tokens = ["id", "+", "-", "*", "/", "(", ")"]

table_column = ["id", "+", "-", "*", "/", "(", ")", "$", "E", "T", "F"]
table = [
#     id     +     -      *     /    (      )     $     E      T      F  
    ["S5",  None, None, None, None, "S4", None, None,  "1",   "2",   "3"  ],  # state 0
    [None,  "S6", "S7", None, None, None, None, "Acc", None, None, None ],  # state 1
    [None,  "R3", "R3", "S8", "S9", None, "R3", "R3",  None, None, None ],  # state 2
    [None,  "R6", "R6", "R6", "R6", None, "R6", "R6",  None, None, None ],  # state 3
    ["S5",  None, None, None, None, "S4", None, None, "10",  "2",   "3"  ],  # state 4
    [None,  "R8", "R8", "R8", "R8", None, "R8", "R8",  None, None, None ],  # state 5
    ["S5",  None, None, None, None, "S4", None, None, None,  "11",  "3"  ],  # state 6
    ["S5",  None, None, None, None, "S4", None, None, None,  "12",  "3"  ],  # state 7
    ["S5",  None, None, None, None, "S4", None, None, None,  None,  "13" ],  # state 8
    ["S5",  None, None, None, None, "S4", None, None, None,  None,  "14" ],  # state 9
    [None,  "S6", "S7", None, None, None, "S15", None, None, None, None ],  # state 10
    [None,  "R1", "R1", "S8", "S9", None, "R1", "R1",  None, None, None ],  # state 11
    [None,  "R2", "R2", "S8", "S9", None, "R2", "R2",  None, None, None ],  # state 12
    [None,  "R4", "R4", "R4", "R4", None, "R4", "R4",  None, None, None ],  # state 13
    [None,  "R5", "R5", "R5", "R5", None, "R5", "R5",  None, None, None ],  # state 14
    [None,  "R7", "R7", "R7", "R7", None, "R7", "R7",  None, None, None ]   # state 15
]

# Production rules from the provided grammar
productions = {
    1: ("E", ["E", "+", "T"]),
    2: ("E", ["E", "-", "T"]),
    3: ("E", ["T"]),
    4: ("T", ["T", "*", "F"]),
    5: ("T", ["T", "/", "F"]),
    6: ("T", ["F"]),
    7: ("F", ["(", "E", ")"]),
    8: ("F", ["id"])
}


