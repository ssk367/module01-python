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

# Test Functionality
if __name__ == "__main__":
    log = log_defect("scratch")
    log = log_defect("dent", log)
    log = log_defect("scratch", log)
    log = log_defect("scratch", log)
    print(count_defects(log))
