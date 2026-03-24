# src/task_config.py

def get_prompt(task_data):
    return f"""
    CONTEXT: {task_data['context']}
    INITIAL LOGIC: {task_data['initial_state']['logic_gate_map']}
    CURRENT INPUTS: {task_data['initial_state']['inputs']}
    
    CRITICAL CHANGE: {task_data['constraint_pivot']['faulty_component']}
    NEW RULE: {task_data['constraint_pivot']['new_rule']}
    
    TASK: {task_data['constraint_pivot']['goal']}
    Explain your reasoning and state the final input values.
    """