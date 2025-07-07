def beer_countdown(bottles):
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} bottle{'s' if bottles - 1 != 1 else ''} of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        bottles -= 1

def main():
    try:
        num = int(input("How many bottles of beer are on the wall? "))
        if num < 1:
            print("Please enter a number greater than 0.")
        else:
            beer_countdown(num)
            print("Time to buy more beer!")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
