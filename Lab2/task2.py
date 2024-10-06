def task2(text):
    tokens = text.split(" ")
    distinctTokens = set(tokens)
    print("Number of distinct tokens:", len(distinctTokens))

    token_count = {}
    for token in tokens:
        if token in token_count:
            token_count[token] += 1
        else:
            token_count[token] = 1

    for key, val in token_count.items():
        print(f"{key} : {val}")

    sortedDict = {k: v for k, v in sorted(token_count.items())}
    print("Sorted dictionary:")
    for key , val in sortedDict.items() :
        print (f"{key} : {val}")
    mostToken = max(sortedDict, key=sortedDict.get)
    print("Most frequent token:", mostToken)

text = "Nong Lam University Ho Chi Minh Viet Nam Nong Lam University"
task2(text)
