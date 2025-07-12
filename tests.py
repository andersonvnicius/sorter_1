import pytest
from main import sort, MASS_HEAVY, VOLUME_BULKY, LENGTH_BULKY


def test_standard_case():
    assert sort(width=1, height=1, length=1, mass=1) == "standard"

def test_special_due_to_volume():
    # volume exceeds bulky threshold: e.g., width * height * length > VOLUME_BULKY
    length = LENGTH_BULKY - 1 # Ensure test will fail because of volume, not lenght
    width = height = int((VOLUME_BULKY // length) + 1)  # just over volume threshold
    assert sort(width=width, height=height, length=length, mass=1) == "special"

def test_special_due_to_length():
    # length equals bulky threshold
    assert sort(width=1, height=1, length=LENGTH_BULKY, mass=1) == "special"

def test_special_due_to_mass():
    # mass just over heavy threshold
    assert sort(width=1, height=1, length=1, mass=MASS_HEAVY + 1) == "special"

def test_rejected_case():
    assert sort(width=1, height=1, length=LENGTH_BULKY + 1, mass=MASS_HEAVY + 1) == "rejected"

def test_invalid_length_raises():
    with pytest.raises(ValueError, match="Invalid dimensions"):
        sort(width=1, height=1, length=-1, mass=1)

def test_invalid_mass_raises():
    with pytest.raises(ValueError, match="Invalid dimensions"):
        sort(width=1, height=1, length=1, mass=0)
