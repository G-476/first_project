# Функциональный стиль программирования
# map() ---- замена For
lst = ['1', '2', '3']
int_lst = []
for number in lst:
    int_lst.append(int(number))
print(lst)
print(int_lst)

# -----------------
gen_lst = [int(number) for number in lst]
print(gen_lst)
# -----------------
map_lst = map(int, lst)
print(int_lst.__sizeof__())
print(map_lst.__sizeof__())
print(list(map_lst))

names = ['dior', 'muhammad', 'sanjar']
map_names = map(str.capitalize, names)
print(names)
print(list(map_names))


def double_num(number: int):
    return number ** 2
lst = [23, 42, 55, 52, 63]
map_lst = map(double_num, lst)
print(lst)
print(list(map_lst))


words = ['purple', 'yellow', 'orange', 'apple', 'nokia', 'windows', 'transformer', 'not', 'ton', 'bin', 'cod']
less_5 = []
more_5 = []
for letter in words:
    if len(letter) <= 5:
        less_5.append(letter)
    else:
        more_5.append(letter)
print(more_5)
print(less_5)


words = ['purple', 'yellow', 'orange', 'apple', 'nokia', 'windows', 'transformer', 'not', 'ton', 'bin', 'cod', 'olx']
def get_words_less_5(word: str):
    return len(word) <= 5

filter_lst = filter(get_words_less_5, words)
print(list(filter_lst))
# ----------------------------------
words = ['apple', 'alive', 'after', 'assembler', 'application', 'byd', 'bwm', 'banana', 'brabus', 'bentley', 'Brasil']
def get_words_with_a(word: str):
    return word.startswith("a")
filtered = filter(get_words_with_a, words)
print(list(filtered))

# --------------------------------









