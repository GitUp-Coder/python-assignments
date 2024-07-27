
s = "   Python is fun!   "

# Remove leading and trailing whitespace character
trimmed_string = s.strip()


left_justified = trimmed_string.ljust(20, '*')

right_justified = trimmed_string.rjust(20, '*')

# Print
print(f"Trimmed string: '{trimmed_string}'")
print(f"Left justified: '{left_justified}'")
print(f"Right justified: '{right_justified}'")
