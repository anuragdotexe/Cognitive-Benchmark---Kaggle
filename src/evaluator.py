import json
import re

def evaluate_response(model_output, ground_truth):
    """
    Scoring logic: Did the model pivot to the backup path?
    """
    # 1. Check if the model mentions the backup inputs (C or D)
    mentions_c = "C=1" in model_output.replace(" ", "") or "C to 1" in model_output
    mentions_d = "D=1" in model_output.replace(" ", "") or "D to 1" in model_output
    
    # 2. Check if it acknowledges the broken AND gate
    acknowledges_fault = "AND gate" in model_output and ("faulty" in model_output or "broken" in model_output)

    if (mentions_c or mentions_d) and acknowledges_fault:
        return 1.0  # Full marks for pivoting
    elif (mentions_c or mentions_d):
        return 0.5  # Half marks for right answer, weak reasoning
    else:
        return 0.0  # Fail: Likely tried to reuse the broken path

if __name__ == "__main__":
    # Load sample for local testing
    with open("data/circuits_v1.json", "r") as f:
        data = json.load(f)
    
    # Mock test
    sample_output = "Since the AND gate is faulty, I will set C=1 to keep the output HIGH."
    score = evaluate_response(sample_output, data[0]["ground_truth"])
    print(f"Test Score: {score}")