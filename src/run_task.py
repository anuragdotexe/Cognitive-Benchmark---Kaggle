# Updated snippet for src/run_task.py
MODELS_TO_TEST = [
    'google/gemini-3.1-pro-preview', # The reasoning leader
    'google/gemini-3-flash-preview',  # The fast collaborator
    'deepseek-ai/deepseek-r1-0528',   # The specialized thinker
    'google/gemma-3-4b'               # The small baseline
]

def run_benchmark():
    task = ExecutiveFunctionTask()
    summary_report = {}

    for model_id in MODELS_TO_TEST:
        print(f"Testing Model: {model_id}...")
        # Use the Kaggle SDK to initialize the specific model
        model = kbench.llms.get(model_id) 
        results = task.run(model)
        
        # Calculate average score for this model
        avg_score = sum(r['score'] for r in results) / len(results)
        summary_report[model_id] = avg_score
        print(f"Result for {model_id}: {avg_score * 100}%")

    return summary_report