from re import sub

def string_analyzer(input: str):
    stack_like = []
    err_line = 0
    current_line = 0
    for line in input.split("\n"):
        current_line += 1
        for char in line:
            if char == '\'' or char == '\"':
                if len(stack_like) and stack_like[-1] == char:
                    stack_like = stack_like[:-1]
                else:
                    stack_like.append(char)
        if len(stack_like):
            err_line = current_line
            break
        stack_like.clear()
    
    if not err_line:
        new_input = []
        for line in input.split("\n"):
            new_input.append(sub('\".*\"', '"string"', line))
        return True, "\n".join(new_input)
    else:
        return False, err_line
