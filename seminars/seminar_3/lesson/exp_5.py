source = 'a a a b c a a d c d d'.split()
count_dict = {}


def transfer(source_list: list):
    # for idx, el in enumerate(source_list, start=1):
    for el in source_list:
        if el not in count_dict:
            count_dict[el] = 0
            yield el
            continue
        count_dict[el] += 1
        yield f'{el}_{count_dict[el]}'


print([_  for _ in transfer(source)])

