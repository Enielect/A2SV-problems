def mutate_string(string, position, character):
    str_to_list = list(string)
    str_to_list[position] = character
    return str(''.join(str_to_list))
    

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
