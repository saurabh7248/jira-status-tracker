from src.compare import compare

def interactive_compare():
    d1 = input("Enter first date (YYYY-MM-DD): ")
    d2 = input("Enter second date (YYYY-MM-DD): ")
    print(compare(d1, d2))

if __name__ == "__main__":
    interactive_compare()
