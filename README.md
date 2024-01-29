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

## MIT License
```Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.```
### Chinese Hint
以下来源于百度百科：

```·被授权人权利

被授权人有权利使用、复制、修改、合并、出版发行、散布、再授权及贩售软件及软件的副本。

被授权人可根据程序的需要修改授权条款为适当的内容。

·被授权人义务

在软件和软件的所有副本中都必须包含版权声明和许可声明。

·其他重要特性

此授权条款并非属copyleft的自由软件授权条款，允许在自由/开放源码软件或非自由软件（proprietary software）所使用。

MIT的内容可依照程序著作权者的需求更改内容。此亦为MIT与BSD（The BSD license, 3-clause BSD license）本质上不同处。

MIT条款可与其他授权条款并存。另外，MIT条款也是自由软件基金会（FSF）所认可的自由软件授权条款，与GPL兼容。```

