
# Math mark, Physics marks
inputs = [
    [25, 20], 
    [29, 30], # imp
    [30, 29],  #imp
    [30, 30],  # imp
    [40, 45],  
    [49, 30],  
    [29, 29],
    [10, 15], 
    [72, 85],  
    [90, 67], 
    [5, 27]    
]
#labels 
labels = [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0]

# Each neuron has its own pair of weights (for Math and Physics) and a bias
weights = [
    [1, 1],  
    [0.5, 0.5],  
    [0.2, 0.26],   
    [0.2, 0.3]    
]

biases = [-60, -30, -18, -12]

def step_activation(x):
    return 1 if x >= 0 else 0
"""
print("\nLayer Outputs (each neuron output for each input):")
for idx, inp in enumerate(inputs):
    neuron_outputs = []
    for wn, bn in zip(weights, biases):
        weighted_sum = sum(x * w for x, w in zip(inp, wn)) + bn
        output = step_activation(weighted_sum)
        neuron_outputs.append(output)
    print(f"Input: {inp} => Neuron outputs: {neuron_outputs} (Label: {labels[idx]})")
"""

def predict_student_pass_fail():
    print("\nEnter student's marks to predict Pass or Fail:")
    while True:
        try:
            math_mark = float(input("Math mark: "))
            physics_mark = float(input("Physics mark: "))
            if not (0 <= math_mark <= 100) or not (0 <= physics_mark <= 100):
                print("Please enter marks between 0 and 100.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numeric marks.")

    user_input = [math_mark, physics_mark]
    neuron_outputs = []
    for wn, bn in zip(weights, biases):
        weighted_sum = sum(x * w for x, w in zip(user_input, wn)) + bn
        output = step_activation(weighted_sum)
        neuron_outputs.append(output)

    
    final_output = 1 if sum(neuron_outputs) > len(neuron_outputs)/2 else 0
    result = "pass" if final_output == 1 else "fail"
    print(f"Prediction based on entered marks: Student is predicted to {result}.")


predict_student_pass_fail()
