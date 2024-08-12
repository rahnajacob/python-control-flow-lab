def disemvowel(string):
  acc = []
  for c in string:
     if c not in "aeiou":
        acc.append(c)
  return "".join(acc)

def disemvowel1(string):
  return "".join([c for c in string if c not in "aeiou"])
print(disemvowel1("microphone"))
