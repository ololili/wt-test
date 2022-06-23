
def summer(length = 5):
    nums = []
    for i in range(length):
        nums.append(int(input("Geef mij een getal: ")))

    print(sum(nums))

one_liner = lambda length = 5 : print(sum([int(input("Geef mij een getal: ")) for i in range(length)]))
