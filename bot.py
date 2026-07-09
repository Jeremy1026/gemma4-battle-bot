import math
import random

def decide(state: dict, memory: dict) -> tuple[dict, dict]:
    me = state.get("self", {"x": 50, "y": 50, "angle": 0})
    enemies = state.get("enemies", [])
    new_memory = memory.copy()
    action = {"type": "move", "direction": "none"}

    if not enemies:
        # Search mode: move toward center
        dx = 50 - me["x"]
        dy = 50 - me["y"]
        action = {"type": "move", "direction": "towards_center"}
        return action, new_memory

    # Find nearest enemy
    nearest = min(enemies, key=lambda e: math.sqrt((e["x"]-me["x"])**2 + (e["y"]-me["y"])**2))

    # Logic for moving/attacking will go here...
    return action, new_memory

if __name__ == "__main__":
    # Simple local test structure
    test_state = {"entities": []}
    test_memory = {}
    print(f"Test run: {decide(test_state, test_memory)}")
