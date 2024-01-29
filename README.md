# PalworldBreedPython
[![Python application](https://github.com/liuxunchenglxc/PalworldBreedPython/actions/workflows/python-app.yml/badge.svg)](https://github.com/liuxunchenglxc/PalworldBreedPython/actions/workflows/python-app.yml)
Basic Python Function About Palworld Breeding Calculation

## Data Source
https://tieba.baidu.com/p/8876271764 -> [幻兽帕鲁] 中文版百科 版本12(我好喜欢然然啊).xlsx

## Class Doc

### NameNum
Translate between the name of pal and the num in data.
#### __init__(self, csv_path='palworld_name2num.csv')
Init func of name/num tables. If you want other language name, please obtain by yourself. Here only Chinese version provided.
#### get_name(self, num: str), get_names(self, num_list), and get_num(self, name: str)
The convert func of name/num.

### BreedEquals
The breed data loaded table in python.
#### __init__(self, csv_path='palworld_breed.csv')
Init func of BreedEquals, this is not related to language, only about the number of Pal.
#### get_all_offspring(self, p1: str)
Get all offspring at one level, do not search for offspring's offspring.
#### get_offspring(self, p1: str, p2: str)
Get the specific offspring.
#### get_parents(self, off:str)
Get the list of parents tuple as `[(p1, p2), (p3, p4), ...]` format.

### Closure
The closure of the existing pals that can be breeded. The pal out of closure is not able to be produced.
#### __init__(self)
Init func of Closure.
#### add_pals(self, num_list)
Add the first level of Pals, and calc all offspring in all generation, i.e., the closure of offspring.
#### get_closure_all_num(self), get_closure_all_name(self), and get_closure_key_as_name(self)
The func of getting the calc result of the closure.
#### check_num(self, num)
Check the num is or not in the closure.
#### num_path(self, num)
Get one shortest path to breed the Pal of spicific num in the closure.
#### path2string(self, path)
Get the string info that express the shortest path of breeding the Pal for printing to terminal.

### Parents
The func of getting parents of all generation.
#### __init__(self, start_num)
Init all parents of the spicific Pal.
#### check_parents(self, p_num)
Check num is or not its parents.
#### check_parents_not_included(self, closure: Closure)
Check the parents are not included in the closure, and return the num list of parents.
#### display_parents_with_generation_and_name(self, not_included)
The func for display the parents and its generations. This is writted for func `check_parents_not_included`.
