# Function to print first 10 multiples of a number using a for loop
def print_multiples_for(num):
    print(f"First 10 multiples of {num} using for loop:")
    for i in range(1, 11):
        print(num * i)
        
# Example
print_multiples_for(5)
