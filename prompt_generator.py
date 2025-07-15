def get_cascade_inputs():
    """Gets user input for each part of the CASCADE framework."""
    cascade = {
        "C": "Camera (shot type, angle, style): ",
        "A": "Ambiance (lighting, time of day): ",
        "S": "Subject (main focus): ",
        "X": "Context (setting, background): ", # Changed to X to avoid duplicate key with S
        "N": "Action (what the subject is doing): ", # Changed to N to avoid duplicate key with A
        "D": "Dialogue (any speech included): ",
        "E": "Emotion (feeling or expression): "
    }
    
    user_inputs = {}
    for key, prompt in cascade.items():
        user_inputs[key] = input(prompt)
        
    return user_inputs

def generate_prompt(inputs):
    """Generates a prompt from the user's inputs."""
    prompt = ""
    # Order of keys matters for the prompt, so we'll use a predefined order
    ordered_keys = ["C", "A", "S", "X", "N", "D", "E"] 
    for key in ordered_keys:
        if key in inputs and inputs[key]:
            prompt += f"{inputs[key]}, "
            
    # Remove trailing comma and space
    return prompt.strip(", ")

if __name__ == "__main__":
    inputs = get_cascade_inputs()
    prompt = generate_prompt(inputs)
    print("\nGenerated Prompt:")
    print(prompt)
