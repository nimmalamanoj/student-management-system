def normalize_name(name: str) -> str:
    """
    Converts name to proper format
    Example: 'sRIRAMULA sahith' -> 'Sriramula Sahith'
    """
    return " ".join(word.capitalize() for word in name.strip().split())


def is_valid_age(age: int) -> bool:
    """
    Valid age must be between 5 and 100
    """
    return 5 <= age <= 100
