def is_safe(query: str):
    banned_keywords = ["DROP", "DELETE", "UPDATE", "ALTER", "INSERT"]

    query_upper = query.upper().strip()

    if not query_upper.startswith("SELECT"):
        return False

    for keyword in banned_keywords:
        if keyword in query_upper:
            return False

    return True