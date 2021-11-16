name = ["антон, алиса, анна", ' ', '?', '213231', 'qqqq', "антон , алиса,  анна"]
for i in name:
    spl = i.split(', ')
    fstr = [_[0].upper() + _[1:] for _ in spl]
    print(fstr)
    result = (' ').join(fstr)
    print(result)

