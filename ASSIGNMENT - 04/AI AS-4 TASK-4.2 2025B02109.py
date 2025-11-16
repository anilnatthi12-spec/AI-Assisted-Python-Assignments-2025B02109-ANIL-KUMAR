def cm_to_inches(cm):
    """Convert centimeters to inches."""
    inches = cm * 0.3937
    return inches

# --- Call the function ---
cm = float(input("Enter value in centimeters: "))
inches = cm_to_inches(cm)
print(f"{cm} cm = {inches} inches")
