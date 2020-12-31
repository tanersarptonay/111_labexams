"""
Initial Memory is [0,0,0,0,0,0,0,0,0,0]
"""
def decode_and_execute(Memory, Instruction):
    instruction_name = Instruction.split(" ")[0]

    if instruction_name == "CLRMEM":
        Memory[0]=0
        Memory[1]=0
        Memory[2]=0
        Memory[3]=0
        Memory[4]=0
        Memory[5]=0
        Memory[6]=0
        Memory[7]=0
        Memory[8]=0
        Memory[9]=0
        return "NO ERROR"

    elif instruction_name == "SUB":
        instruction_input_1 = Instruction.split(" ")[1][0:-1]
        instruction_input_2 = Instruction.split(" ")[2]
        try:
            instruction_input_2 = int(instruction_input_2)
            instruction_input_1 = int(instruction_input_1)
        except ValueError:
            return "INVALID ADDRESS"
        if not 0<=int(instruction_input_1)<=9 or not 0<=int(instruction_input_2)<=9:
            return "INVALID ADDRESS"
        Memory[instruction_input_1] -= Memory[instruction_input_2]
        return "NO ERROR"

    elif instruction_name == "LOAD":
        instruction_input_1 = Instruction.split(" ")[1][0:-1]
        instruction_input_2 = Instruction.split(" ")[2]
        try:
            instruction_input_1 = int(instruction_input_1)
        except ValueError:
            return "INVALID ADDRESS"
        if not 0<=int(instruction_input_1)<=9:
            return "INVALID ADDRESS"
        try:
            instruction_input_2 = int(instruction_input_2)
        except ValueError:
            return "NOT A NUMBER"
        Memory[instruction_input_1] = instruction_input_2
        return "NO ERROR"

    elif instruction_name == "SUBI":
        instruction_input_1 = Instruction.split(" ")[1][0:-1]
        instruction_input_2 = Instruction.split(" ")[2]
        try:
            instruction_input_1 = int(instruction_input_1)
        except ValueError:
            return "INVALID ADDRESS"
        if not 0<=int(instruction_input_1)<=9:
            return "INVALID ADDRESS"
        try:
            instruction_input_2 = int(instruction_input_2)
        except ValueError:
            return "NOT A NUMBER"
        Memory[instruction_input_1] -= instruction_input_2
        return "NO ERROR"

    elif instruction_name == "DIVI":
        instruction_input_1 = Instruction.split(" ")[1][0:-1]
        instruction_input_2 = Instruction.split(" ")[2]
        try:
            instruction_input_1 = int(instruction_input_1)
        except ValueError:
            return "INVALID ADDRESS"
        if not 0<=int(instruction_input_1)<=9:
            return "INVALID ADDRESS"
        try:
            instruction_input_2 = int(instruction_input_2)
        except ValueError:
            return "NOT A NUMBER"
        if instruction_input_2 == 0:
            return "DIVISION BY ZERO"
        Memory[instruction_input_1] /= instruction_input_2
        return "NO ERROR"

    else:
        return "UNKNOWN INSTRUCTION"





