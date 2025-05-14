sentence = input("PLease enter a sentence: ").strip()
words = sentence.split()
unique_combinations = set()
for i in range(len(words)):
    for j in range(i+1, len(words)):
        for k in range(j+1, len(words)):
            pair = tuple(sorted([words[i], words[j], words[k]]))
            unique_combinations.add(pair)
sorted_combinations = sorted(unique_combinations)
for w1, w2, w3 in sorted_combinations:
    print(w1, w2, w3)
