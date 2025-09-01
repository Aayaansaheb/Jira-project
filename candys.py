def find_candy_pieces(limit=200):
    for n in range(limit):
        if n % 5 == 2 and n % 6 == 3 and n % 7 == 2:
            return n
    return None

if __name__ == "__main__":
    result = find_candy_pieces()
    if result:
        print(f"The number of candies in the jar is: {result}")
    else:
        print("No valid solution found under the given limit.")
