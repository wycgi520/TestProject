class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        import re
        
        def dictcount(fm):
            kw0 = dict()
            ret = self.bracketfind(fm)
            if ret:
                for temp in ret:
                    new_formula = re.search(r"\((.*)\)",temp).group(1)
                    temp_num = re.search(r"\d+$", temp).group()
                    kw1 = dictcount(new_formula)
                    kw1 = {i:v*int(temp_num) for i,v in kw1.items()}
                    self.kwupdate(kw0, kw1)
                    
                    fm = fm.replace(temp,"")
            
            words = re.findall(r"[A-Z][a-z]*\d+|[A-Z][a-z]*",fm)
            kw2 = dict()
            for word in words:
                string = re.search(r"\D+", word).group()
                num = re.search(r"\d+", word)
                if string in kw2:
                    kw2[string] = kw2[string]+int(num.group()) if num else kw2[string]+1
                else:
                    kw2[string] = int(num.group()) if num else 1
                    
            self.kwupdate(kw0, kw2)
            return kw0
                    
        kw = dictcount(formula)
        str_list = list()
        for i,v in kw.items():
            if v == 1:
                v = ""
            str_list.append(i+str(v))
        str_list.sort()
        return "".join(str_list)
        
    
    def kwupdate(self, kwmain, otherkw):
        for i,v in otherkw.items():
            if i in kwmain:
                kwmain[i] += v
            else:
                kwmain[i] = v
        return kwmain
            
    def bracketfind(self, fm):
        bl = list()
        ret = list()
        for i,v in enumerate(fm):
            if v == '(':
                bl.append(i)
            if v == ')':
                i0 = bl.pop()
                if not bl:
                    r_n = re.search(r"^\d+",fm[i+1:]).group()
                    ret.append(fm[i0:i+1]+r_n)
                    
        return ret
