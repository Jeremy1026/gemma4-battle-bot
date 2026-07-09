import math
import random

def decide(state: dict, memory: dict) -> tuple[dict, dict]:
    # Placeholder for logic
    action = {"type": "move", "direction": "none"}
    new_memory = memory.copy()
    return action, new_memory

if __name__ == "__main__":
    # Simple local test structure
    test_state = {"entities": []}
    test_memory = {}
    print(f"Test run: {decide(test_state, test_memory)}")
