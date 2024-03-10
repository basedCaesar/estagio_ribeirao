def inverter_string(s):
    invert = ''
    for i in range(len(s) - 1, -1, -1):
        invert += s[i]
    return invert

def produce_result(s):
    return print(f"String Original: {s}\nString Invertida: {inverter_string(s)}")

produce_result(input("Digite a string que deseja inverter: "))