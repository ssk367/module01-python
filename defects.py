from collections import Counter

def log_defect(defect: str, log: list[str] | None = None) -> list[str]:
    """Log a defect and return the updated log.

    Args:
        defect (str): The defect description.
        log (list[str] | None, optional): The current defect log. Defaults to None.

    Returns:
        list[str]: The updated defect log.
    """
    if log is None:
        log = []
    log.append(defect)
    return log

def count_defects(log: list[str]) -> dict[str, int]:
    """Count the number of defects per defect type.

    Args:
        log (list[str]): The current defect log.

    Returns:
        dict[str, int]: A dictionary with the defects name and count.
    """
    return dict(Counter(log))

def top_defects(log: list[str], n: int = 3) -> list[tuple[str, int]]:
    """Return the top n defects by count.

    Args:
        log (list[str]): The current defect log.
        n (int, optional): The number of top defects to return. Defaults to 3.

    Returns:
        list[tuple[str, int]]: A list of tuples with defect name and count.
    """
    return Counter(log).most_common(n)

if __name__ == "__main__":
    log = ["dent", "scratch", "chip", "chip", "scratch",
           "deform", "chip", "chip", "chip", "scratch",
           "dent", "scratch"]
    print(f"Defect counts: {count_defects(log)}\n")
    print(f"Top defects: {top_defects(log)}")
    
