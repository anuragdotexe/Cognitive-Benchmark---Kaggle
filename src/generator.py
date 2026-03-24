import json
import random

def generate_circuit_puzzle(num_gates=5):
    """
    Generates a logic circuit puzzle with a mandatory 'pivot' constraint.
    """
    gates = ["AND", "OR", "XOR", "NAND"]
    
    # Define a simple 3-input, 2-layer circuit
    puzzle = {
        "inputs": ["A", "B", "C"],
        "initial_logic": "(A AND B) OR C",
        "target_output": 1,
        "input_values": {"A": 1, "B": 1, "C": 0},
        "constraint_change": "The 'AND' gate is now FAULTY. You must achieve the target without it.",
        "alternative_path_possible": True
    }
    
    return puzzle

# Save for testing
if __name__ == "__main__":
    sample_data = [generate_circuit_puzzle() for _ in range(10)]
    with open("data/circuits_v1.json", "w") as f:
        json.dump(sample_data, f, indent=4)
    print("Dataset generated in data/circuits_v1.json")