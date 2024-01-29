


class NameNum:
    def __init__(self, csv_path='palworld_name2num.csv'):
        # load csv
        self.name2num={}
        self.num2name={}
        with open(csv_path, 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            line = line.strip('\ufeff')
            name, num = line.split(',')
            self.name2num[name] = num
            self.num2name[num] = name

    def get_name(self, num: str):
        return self.num2name[num]

    def get_num(self, name: str):
        return self.name2num[name]

    def get_names(self, num_list):
        return [self.num2name[str(num)] for num in num_list]

class BreedEquals:
    def __init__(self, csv_path='palworld_breed.csv'):
        # load csv
        self.offsprings = {}
        self.parents = {}
        with open(csv_path, 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            line = line.strip('\ufeff')
            p1, p2, off = line.split(',')
            if p1 in self.offsprings:
                self.offsprings[p1][p2] = off
            else:
                self.offsprings[p1] = {p2: off}
            if p2 in self.offsprings:
                self.offsprings[p2][p1] = off
            else:
                self.offsprings[p2] = {p1: off}
            self.parents[off] = (p1, p2)

    def get_all_offspring(self, p1: str):
        if p1 in self.offsprings:
            return self.offsprings[p1]
        else:
            return None

    def get_offspring(self, p1: str, p2: str):
        if p1 in self.offsprings:
            if p2 in self.offsprings[p1]:
                return self.offsprings[p1][p2]
        return None

    def get_parents(self, off:str):
        if off in self.parents:
            return self.parents[off]
        return None, None


class Closure:
    def __init__(self):
        self.closure = {}
        self.add_times = 0
        self.size = 0
        self.be = BreedEquals()
        self.nn = NameNum()

    def add_pals(self, num_list):
        for num in num_list:
            num = str(num)
            self.closure[num] = {'dist': self.add_times}
            self.size += 1
        self.add_times += 1
        if self.size > 1:
            tmp_size = 0
            while tmp_size < self.size:
                tmp_size = self.size
                for p1 in list(self.closure.keys()):
                    for p2 in list(self.closure.keys()):
                        off = self.be.get_offspring(p1, p2)
                        if off and off not in self.closure:
                            self.closure[off] = {'dist': self.add_times, 'path': (p1, p2)}
                            self.size += 1
                self.add_times += 1

    def get_closure_all_num(self):
        return list(self.closure.keys())

    def get_closure_all_name(self):
        return [self.nn.get_name(num) for num in list(self.closure.keys())]

    def get_closure_key_as_name(self):
        r = {}
        for k, v in list(self.closure.items()):
            v['num'] = k
            r[self.nn.get_name(k)] = v
        return r

    def check_num(self, num):
        num = str(num)
        if num in self.closure:
            return True
        else:
            return False

    def num_path(self, num):
        num = str(num)
        r = []
        check_list = [num]
        checked_list = []
        while check_list:
            off = check_list.pop()
            if 'path' in self.closure[off] and off not in checked_list:
                p1, p2 = self.closure[off]['path']
                check_list.append(p1)
                check_list.append(p2)
                r.append((off,p1,p2))
            checked_list.append(off)
        return r

    def path2string(self, path):
        if not path:
            return 'This is original Pal.'
        s = ''
        for off, p1, p2 in path:
            num2name = lambda x: self.nn.get_name(x)
            s += f'{num2name(off)} <- {num2name(p1)} + {num2name(p2)}\n'
        return s

class Parents:
    def __init__(self, start_num):
        self.start_num = str(start_num)
        self.be = BreedEquals()
        self.nn = NameNum()
        self.parents = {}
        check_list = [self.start_num]
        checked_list = [None]
        while check_list:
            off = check_list.pop()
            p1, p2 = self.be.get_parents(off)
            if p1 not in checked_list:
                check_list.append(p1)
            if p2 not in checked_list:
                check_list.append(p2)
            if p1:
                self.parents[p1] = off
            if p2:
                self.parents[p2] = off
            checked_list.append(off)

    def check_parents(self, p_num):
        p = str(p_num)
        if p in list(self.parents.keys()):
            return True
        else:
            return False

    def check_parents_not_included(self, closure: Closure):
        nums = closure.get_closure_all_num()
        not_included = []
        for p in list(self.parents.keys()):
            if p not in nums:
                not_included.append(p)
        return not_included

if __name__ == '__main__':
    print("Init Name Num table...")
    nn = NameNum()
    print(nn.name2num, nn.num2name)
    print()
    print("Init Name Num table OK")
    print()
    
    print("Init BreedEquals...")
    be = BreedEquals()
    print(be.offsprings, be.parents)
    print("Init BreedEquals OK")
    print()
    
    print("Build Closure with nums of 1,2,3,4,5,11,12,13,14,15")
    c = Closure()
    c.add_pals([1,2,3,4,5,11,12,13,14,15])
    print(c.get_closure_key_as_name())
    print("Check num 86:", c.check_num(86))
    print("Check num 56:", c.check_num(56))
    print("Print Shortest Path to num 64:")
    print(c.path2string(c.num_path(64)))
    print("Closure OK")
    print()

    print("Build Parents...")
    p = Parents(64)
    print("Show all parent {p: off}:", p.parents)
    print("Check num 10:", p.check_parents(10))
    print("Check Closure not included:", nn.get_names(p.check_parents_not_included(c)))
