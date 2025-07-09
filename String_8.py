"""______Remove brackets from an algebraic epression______"""

def remv_brackets(expresn):
    return expresn.replace("(", "").replace(")", "").replace("[", "").replace("]", "")

input_exp = "3 * (x + 2) - [y / (z + 1)]"
print(f"Given expression '{input_exp}', after removing brackets it becomes: {remv_brackets(input_exp)}")