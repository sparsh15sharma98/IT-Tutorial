# Name - Sparsh Sharma, Student ID - U3315385, Date - 16.09.2025
# Boolean Circuit Simulation

def circuit_A(a, b):
    # Circuit A steps
    not_a = not a       # a)
    not_b = not b       # b)
    nand_c = not (not_a and not_b)  # c)
    not_b2 = not b      # d)
    and_e = not_b2 and nand_c and a # e)
    and_f = b and nand_c and a      # f)
    out_A = and_e or and_f          # g)
    return out_A

def circuit_B(a, b, c):
    # Circuit B steps
    not_b_h = not b           # h)
    or_i = not_b_h or c       # i)
    out_B = or_i and a        # j)
    return out_B

# -----------------------
# Get Inputs from User
# -----------------------
def get_boolean_input(prompt):
    while True:
        val = input(prompt + " (True/False): ").strip().lower()
        if val in ['true', 't', '1']:
            return True
        elif val in ['false', 'f', '0']:
            return False
        else:
            print("Invalid input. Enter True or False.")

# User input
A = get_boolean_input("Enter value for A")
B = get_boolean_input("Enter value for B")
C = get_boolean_input("Enter value for C")

# Compute outputs
X = circuit_A(A, B)  # Output of Circuit A
Y = circuit_B(A, B, C)  # Output of Circuit B

# Display results
print("\n--- Circuit Outputs ---")
print(f"Input: A={A}, B={B}, C={C}")
print(f"Output X (Circuit A): {X}")
print(f"Output Y (Circuit B): {Y}")
