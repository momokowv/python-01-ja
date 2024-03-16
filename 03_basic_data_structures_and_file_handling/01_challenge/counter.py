def counter():
    occurrences = {}
    fruits = [
        "apple",
        "banana",
        "orange",
        "grape",
        "apple",
        "kiwi",
        "banana",
        "melon",
        "orange",
        "strawberry",
    ]

    counts=[]
    for x in fruits:
        counts.append(fruits.count(str(x)))

    occurrences=dict(zip(fruits,counts))

    for k, v in occurrences.items():
        print(k, ":", v)

        

    return occurrences

print(counter())
