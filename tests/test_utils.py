from utils import generate_with_uuid, unique
from validator import validate
import re

def test_generate_with_uuid_uniqueness():
    used = set()
    name1 = generate_with_uuid(2, "-", used)
    name2 = generate_with_uuid(2, "-", used)
    assert name1 != name2
    assert name1 in used
    assert name2 in used
    assert len(name1.split("-")) == 3


def test_unique_returns_unique_names():
    used = set()
    name1 = unique(used, 2, "-")
    name2 = unique(used, 2, "-")
    assert name1 != name2
    assert name1 in used
    assert name2 in used
    assert validate(name1)
    assert validate(name2)

        
def test_generate_with_uuid_suffix_length():
    used = set()
    name = generate_with_uuid(2, "-", used)
    suffix = name.split("-")[-1]
    assert re.fullmatch(r"[a-f0-9]{4}", suffix)
