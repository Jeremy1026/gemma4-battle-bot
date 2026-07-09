import pytest
from bot import decide

def test_identify_nearest_enemy():
    state = {
        "self": {"x": 50, "y": 50, "angle": 0},
        "enemies": [
            {"id": "enemy1", "x": 60, "y": 60}, # Dist ~14.1
            {"id": "enemy2", "x": 40, "y": 40}  # Dist ~14.1 (tie)
        ]
    }
    memory = {}
    action, _ = decide(state, memory)
    # The bot should pick one of the enemies and attempt to move toward it
    assert action["type"] in ["move", "attack"]

def test_no_enemies_mode():
    state = {
        "self": {"x": 50, "y": 50, "angle": 0},
        "enemies": []
    }
    memory = {}
    action, _ = decide(state, memory)
    # Should default to searching (moving toward center or wandering)
    assert action["type"] == "move"
