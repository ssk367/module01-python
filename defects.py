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