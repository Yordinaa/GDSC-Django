
import math

def basic_operations(a, b):
    add_result = a + b
    subtract_result = a - b 
    multiply_result = a * b
    try:
        divide_result = a / b
    except ZeroDivisionError:
        divide_result = "Division by zero error!"

    return {"Addition": add_result, 
            "Subtraction": subtract_result,
            "Multiplication": multiply_result,
            "Division": divide_result}

def power_operation(base, exponent, **kwargs):
    power_result = math.pow(base, exponent)
    if "modulo" in kwargs:
        modulo = kwargs["modulo"] 
        try: 
            power_result %= modulo
        except ZeroDivisionError:
            power_result = "Modulo by zero error!"

    return power_result

def apply_operations(operation_list):
    return list(map(lambda x: x[0](*x[1]), operation_list))
