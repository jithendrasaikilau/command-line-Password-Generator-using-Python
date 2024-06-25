import random
import string
import argparse

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not (use_letters or use_numbers or use_symbols):
        raise ValueError("At least one of letters, numbers, or symbols must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a random password")
    parser.add_argument('-l', '--length', type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument('--letters', action='store_true', help="Include letters in the password")
    parser.add_argument('--numbers', action='store_true', help="Include numbers in the password")
    parser.add_argument('--symbols', action='store_true', help="Include symbols in the password")
    
    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.letters, args.numbers, args.symbols)
        print("Generated password:", password)
    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()
