import math
import random

def decide(state: dict, memory: dict) -> tuple[dict, dict]:
    me = state.get("self", {"x": 50, "y": 50, "angle": 0})
    enemies = state.get("enemies", [])
    new_memory = memory.copy()

    if not enemies:
        return {"type": "move", "direction": "center"}, new_memory

    nearest = min(enemies, key=lambda e: math.sqrt((e["x"]-me["x"])**2 + (e["y"]-me["y"])**2))

    # Target angle
    target_angle = math.atan2(nearest["y"] - me["y"], nearest["x"] - me["x"])

    # Angular error calculation
    error = (target_angle - me["angle"] + math.pi) % (2 * math.pi) - math.pi

    if abs(error) <= math.radians(22.5):
        return {"type": "attack", "target": nearest["id"]}, new_memory
    else:
        # Rotate and move
        return {"type": "move", "angle": target_angle, "dist": 1}, new_memory

if __name__ == "__main__":
    # Simple local test structure
    test_state = {"entities": []}
    test_memory = {}
    print(f"Test run: {decide(test_state, test_memory)}")
