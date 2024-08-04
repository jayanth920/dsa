def solve(s):
    ll = 0
    word = ""
    for i in range(len(s)):
        if s[i] != " ":
            word += s[i]
        else:
            if word:
                ll = len(word)
                word = ""
    if word:
        ll = len(word)
    return ll
            