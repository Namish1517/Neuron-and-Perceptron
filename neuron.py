import random


def get_user_params(num_inputs):
    weights = []
    print(f"Enter weights for {num_inputs} inputs:")
    for i in range(num_inputs):
        while True:
            try:
                w = float(input(f"Weight {i+1}: "))
                weights.append(w)
                break
            except ValueError:
                print("Please enter a valid number.")
    
    while True:
        try:
            bias = float(input("Enter bias value: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    return weights, bias

#weights and bias random
def reset_params(num_inputs):
    weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
    bias = random.uniform(-1, 1)
    print(f"Reseted weights: {weights}")
    print(f"Reseted bias: {bias}")
    return weights, bias

inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

num_inputs = len(inputs[0]) 
weights, bias = get_user_params(num_inputs)

while True:
    print("\nCurrent weights:", weights)
    print("Current bias:", bias)
    
    choice = input("\nChoose: [1] Adjust weights/bias [2] Reset randomly [3] Continue\nEnter choice: ")
    
    if choice == "1":
        weights, bias = get_user_params(num_inputs)
    elif choice == "2":
        weights, bias = reset_params(num_inputs)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")



def compute_weighted_sum(input_vector, weights, bias):
    total = 0
    for x, w in zip(input_vector, weights):
        total += x * w
    total += bias
    return total


print("\nWeighted sums for each input:")
weighted_sums = []
for inp in inputs:
    ws = compute_weighted_sum(inp, weights, bias)
    weighted_sums.append(ws)
    print(f"Input: {inp}, Weighted Sum: {ws}")


def step_activation(weighted_sum):
    if weighted_sum > 0:
        return 1
    else:
        return 0

# activation function
print("\nNeuron outputs (after activation):")
for inp, ws in zip(inputs, weighted_sums):
    output = step_activation(ws)
    print(f"Input: {inp}, Output: {output}")
