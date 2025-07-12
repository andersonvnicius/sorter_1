MASS_HEAVY = 20
VOLUME_BULKY = 1e6
LENGTH_BULKY = 150

decision_map = {
    (True, True): "rejected",
    (True, False): "special",
    (False, True): "special",
    (False, False): "standard",
}


def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Classifies a package based on its dimensions and mass.

    Parameters:
        width (float): The width of the package in cm.
        height (float): The height of the package in cm.
        length (float): The length of the package in cm.
        mass (float): The mass of the package in kg.

    Returns:
        str: The classification result ("standard", "special", "rejected", or error message).
    """
    if any(x <= 0 for x in (width, height, length, mass)):
        raise ValueError("Invalid dimensions: all values must be positive")

    volume = width * height * length
    is_heavy = mass > MASS_HEAVY
    is_bulky = volume > VOLUME_BULKY or any(
        x >= LENGTH_BULKY for x in (width, height, length)
    )

    return decision_map[(is_bulky, is_heavy)]
