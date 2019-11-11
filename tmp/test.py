myarr = [
    ["val1", "val11"],
    ["val1", "val12"],
    ["val2", "val21"],
    ["val2", "val22"],
    ["val3", "val31"],
    
]

out = {}
for i in myarr:
    if out.get(i[0]) is None:
        out[i[0]] = [i[1]]
    else:
        out[i[0]].append(i[1])


print(out)
