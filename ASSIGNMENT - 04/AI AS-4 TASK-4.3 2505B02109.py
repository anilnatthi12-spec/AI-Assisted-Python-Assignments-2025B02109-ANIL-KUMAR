def format_name(full_name):
    """Format a full name as 'Last, First'."""
    parts = full_name.strip().split()
    if len(parts) >= 2:
        first = parts[0]
        last = parts[-1]
        return f"{last}, {first}"
    else:
        return full_name  # return as-is if only one name is given

# ---- runner so the script accepts input and shows output ----
if __name__ == "__main__":
    name = input("Enter full name: ").strip()
    formatted = format_name(name)
    print("Formatted:", formatted)
