def read_file(filename):
    """ Safely reads the contents of a file using context management and error handling.
   Parameters:
    filename (str): Path to the file.

    Returns:
    str: File contents if successful, else None.
    """
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError as e:
        print(f"I/O error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

# Sample usage with user input
if __name__ == "__main__":
    filename = input("Enter the filename to read: ").strip()
    content = read_file(filename)
    if content:
        print("\nFile contents:\n")
        print(content)
    else:
        print("\nNo content to display.")