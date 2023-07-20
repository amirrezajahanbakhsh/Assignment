names = ["ali", "taha", "abbas", "amir", "gholam", "mohamamd", "kiya"]
scores = [20, 19.25, 18.5, 19.75, 18, 20, 18.75, 19.5]
names_scores = {}
c = 0
for j in names:
    names_scores[str(j)] = scores[c]
    c += 1

print(names_scores)