import json
import kaggle_benchmarks as kbench
from src.evaluator import evaluate_response
from src.task_config import get_prompt

class ExecutiveFunctionTask(kbench.BenchmarkTask):
    """
    Kaggle-compliant task for testing Executive Function (Pivot Logic).
    """
    def __init__(self, data_path="data/circuits_v1.json"):
        # Metadata is required by the SDK for the dashboard
        self.metadata = {
            "name": "Circuit Pivot Challenge",
            "track": "Executive Functions",
            "description": "Tests if a model can re-plan logic when a gate is faulted.",
            "version": "1.0.0"
        }
        with open(data_path, "r") as f:
            self.dataset = json.load(f)

    def run(self, model_id: str):
        """
        Executes the benchmark against a specific model ID.
        """
        model = kbench.llms.get(model_id)
        results = []
        
        for task in self.dataset:
            prompt = get_prompt(task)
            
            # The SDK uses .generate or .query depending on the version
            response = model.generate(prompt) 
            
            score = evaluate_response(response, task['ground_truth'])
            
            results.append({
                "task_id": task['id'],
                "score": score,
                "model_response": response
            })
            
        return results

# Local Test Execution
if __name__ == "__main__":
    # Test with a lightweight model first to save quota
    tester = ExecutiveFunctionTask()
    summary = tester.run('google/gemini-3.1-flash-lite-preview')
    print(f"Test Run Completed. Tasks Scored: {len(summary)}")





    # need some data in creating this 