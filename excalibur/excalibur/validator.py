def validate_prompt(prompt):
    if not prompt:
        raise ValueError("Prompt cannot be empty")
    return True
