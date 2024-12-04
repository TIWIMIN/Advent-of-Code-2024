sum = 0
i = 0
do = True

input_string = ""

while i < len(input_string): 
    if i > 3 and input_string[i - 4: i] == "do()": 
        do = True
    if i > 6 and input_string[i - 7: i] == "don't()": 
        do = False
    if i > 3 and input_string[i - 4: i] == "mul(" and do:
        temp_counter = 0 
        factor_a = "" 
        factor_b = ""
        while i < len(input_string) and input_string[i].isdigit() and temp_counter < 3: 
            temp_counter += 1
            factor_a += input_string[i]
            i += 1
        if i < len(input_string) and input_string[i] == ',': 
            i += 1
            temp_counter = 0
            while i < len(input_string) and input_string[i].isdigit() and temp_counter < 3: 
                temp_counter += 1
                factor_b += input_string[i]
                i += 1
        if i < len(input_string) and input_string[i] == ")" and factor_a and factor_b:
            sum += int(factor_a) * int(factor_b)
    i += 1

print(sum)