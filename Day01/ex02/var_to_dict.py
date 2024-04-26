def var_to_dic():
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]
    dic = dict(d)
    dic_swap = get_swap_dict(dic)
    for k, v in dic_swap.items():
        print(f'{k}: {v}')
    return dic_swap

def get_swap_dict(d):
    return {v: k for k, v in d.items()}


if __name__ == "__main__":
    var_to_dic()