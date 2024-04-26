def my_numbers():
    with open("numbers.txt", "r") as f:
        lines = f.read()
        lines = lines.replace(", ", "\n")
        print(lines)
        
if __name__ == "__main__":
    my_numbers()
