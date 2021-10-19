def babylonian_algorithm(S):
    e = 0.00001
    mean = (S + 1) / 2  # This is the first pass of the algorithm
    print(f"x\t\t{S}/x\t\tMean")
    while abs(mean ** 2 - S) > e:
        estimate = S / mean
        mean = (mean + estimate) / 2
        print(f"{mean:f}\t{estimate:f}\t{mean:f}")
    return mean


S = 5  # Number to find the square root of
print(f"\nThe square root of {S} is close to {babylonian_algorithm(S):f}\n")
S = 64  # Number to find the square root of
print(f"\nThe square root of {S} is close to {babylonian_algorithm(S):f}")