def change(itera, change, spacing=1, start=0, stop=None):
    if stop is None: stop = len(itera)
    if type(itera) != list or any([type(elem) != int for elem in itera]) or type(change) != int or type(
            spacing) != int or type(start) != int or type(stop) != int or start > stop: raise TypeError
    test, changed, first, indexnum = 0, [], True, 0
    for i in range(0, len(itera[start:stop])):
        indexnum += 1
        if first:
            test = itera[indexnum - 1 + start]
            first = False
            indexnum += spacing - 1
        elif test + change <= itera[indexnum - 1 + start] or test - change >= itera[indexnum - 1 + start]:
            first = True
            changed.append(indexnum - 1 + start)
    return changed


if __name__ == "__main__":
    import numpy as np

    ran_list = np.random.randint(10, size=25)
    ran_list = [int(i) for i in ran_list]
    # ran_list.append("stop me")
    print(ran_list)
    print(change(itera=ran_list, change=4))
    print([ran_list[i] for i in change(itera=ran_list, change=4)])
