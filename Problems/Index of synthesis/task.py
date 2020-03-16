if __name__ == '__main__':
    morphemes = float(input())
    if 4 >= morphemes > 3:
        print("Polysynthetic")
    elif 3 >= morphemes >= 2:
        print("Synthetic")
    elif 2 > morphemes > 1:
        print("Analytic")