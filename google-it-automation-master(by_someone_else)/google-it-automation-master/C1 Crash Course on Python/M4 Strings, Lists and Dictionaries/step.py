def palindro(inp):
    ns = ''
    rs = ''
    for i in inp.lower() :
        ns = ns + i
        rs = i + rs
    print(ns)
    print(rs)

palindro('BEY')