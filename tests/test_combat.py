import pytest
from bot import decide

def test_attack_alignment():
    # Bot is at 50,50 facing 0 deg. Enemy is at 60,50 (angle 0).
    # This should trigger an attack because 0 deg is within +/- 22.5 deg.
    state = {
        "self": {"x": 50, "y": 50, "angle": 0},
        "enemies": [{"id": "e1", "x": 60, "y": 50}]
    }
    memory = {}
    action, _ = decide(state, memory)
    assert action["type"] == "attack"
