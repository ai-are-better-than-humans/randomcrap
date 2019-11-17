# modified version of code by http://effbot.org/zone/python-code-generator.htm
import os


class CodeGeneratorBackend(object):

    def __init__(self, tab="\t", path=None, name=None):
        self.status_dict = {
            "code": [],
            "tab": tab,
            "level": 0,
            "path": path,
            "name": name
        }
        assert isinstance(self.status_dict["tab"], str), "the variable tab is not of type string"
        assert ((self.status_dict["path"] is not None and self.status_dict["name"] is not None) or (
                self.status_dict["name"] is None and self.status_dict[
            "path"] is None)), "both path specific variables were in different states"
        assert ((isinstance(self.status_dict["name"], str) and isinstance(self.status_dict["path"],
                                                                          str))) or (
                       isinstance(self.status_dict["name"], type(None)) and isinstance(self.status_dict["path"],
                                                                                       type(
                                                                                           None))), "one or more of " \
                                                                                                    "the path " \
                                                                                                    "specific " \
                                                                                                    "variables is not " \
                                                                                                    "of type string "

    def end(self):
        if os._exists(r"{path}\{name}.txt".format(path=self.status_dict["path"], name=self.status_dict["name"])):
            return None
        if self.status_dict["path"] is not None:
            try:
                foo = open(r"{path}\{name}.txt".format(path=self.status_dict["path"], name=self.status_dict["name"]),
                           "w+")
            except Exception as e:
                path = self.status_dict["path"]
                name = self.status_dict["name"]
                raise SyntaxError(f"the following error occurred during opening of {path}\{name}: \'{e}\'.")
            foo.write("".join(self.status_dict["code"]))
            foo.close()
            os.rename(r"{path}\{name}.txt".format(path=self.status_dict["path"], name=self.status_dict["name"]),
                      r"{path}\{name}.py".format(path=self.status_dict["path"], name=self.status_dict["name"]))
        else:
            return self.status_dict["code"]

    def __repr__(self):
        return repr(self.status_dict["code"])

    def __str__(self):
        return str(self.status_dict["code"])

    def __call__(self):
        return self.status_dict["code"]

    def append(self, string):
        if os._exists(r"{path}\{name}.txt".format(path=self.status_dict["path"], name=self.status_dict["name"])):
            return None
        assert isinstance(string, str), "the variable string is not of type string"
        self.status_dict["code"].append(self.status_dict["tab"] * self.status_dict["level"] + string + "\n")

    def remove(self, line, chr_num=None):
        if os._exists(r"{path}\{name}.txt".format(path=self.status_dict["path"], name=self.status_dict["name"])):
            return None
        assert isinstance(line, int), "the variable line\' is not of type integer"
        assert isinstance(chr_num, tuple) or isinstance(chr_num,
                                                        type(
                                                            None)), "the variable chr_num is set to a type besides " \
                                                                    "that of None and tuple "
        assert line <= (len(self.status_dict["count"])) and chr_num[1] <= len(self.status_dict["count"][
                                                                                  line]) and chr_num[0] <= len(
            self.status_dict["count"][
                line]), "one or more of the code indexing variables is longer than the space it occupies"
        assert len(chr_num) == 2, "the amount of values in the variable chr_num are not equal to 2"
        assert chr_num[0] is int and chr_num[
            1] is int, "one or more of the vaules inside the variable chr_num is not of type int"
        if chr_num is None:
            self.status_dict["count"].pop(abs(line))
        else:
            self.status_dict["count"][abs(line)][abs(chr_num[0]):abs(chr_num[1])] = ""

    def replace(self, line, chrs, chr_num=None, ):
        if os._exists(r"{path}\{name}.txt".format(path=self.status_dict["path"], name=self.status_dict["name"])):
            return None
        assert isinstance(line, int), "the variable line is not of type integer"
        assert isinstance(chrs, str), "the variable chrs is not of type string"
        assert isinstance(chr_num, tuple) or isinstance(chr_num,
                                                        type(
                                                            None)), "the variable chr_num is set to a type besides " \
                                                                    "that of None and tuple "
        assert line <= (len(self.status_dict["count"])) and chr_num[1] <= len(self.status_dict["count"][
                                                                                  line]) and chr_num[0] <= len(
            self.status_dict["count"][
                line]), "one or more of the code indexing variables is longer than the space it occupies"
        assert len(chr_num) == 2, "the amount of values in the variable chr_num are not equal to 2"
        assert chr_num[0] is int and chr_num[
            1] is int, "one or more of the values inside the variable chr_num is not of type int"
        if chr_num is None:
            self.status_dict["count"][abs(line)] = chrs
        else:
            self.status_dict["count"][abs(line)][abs(chr_num[0]):abs(chr_num[1])] = chrs

    def indent(self, amount=1):
        if os._exists(r"{path}\{name}.txt".format(path=self.status_dict["path"], name=self.status_dict["name"])):
            return None
        assert isinstance(amount, int), "the variable amount is not of type integer"
        self.status_dict["level"] += abs(amount)

    def set_indent(self, amount):
        if os._exists(r"{path}\{name}.txt".format(path=self.status_dict["path"], name=self.status_dict["name"])):
            return None
        assert isinstance(amount, int), "the variable amount is not of type integer"
        self.status_dict["level"] = abs(amount)

    def unindent(self, amount=1):
        if os._exists(r"{path}\{name}.txt".format(path=self.status_dict["path"], name=self.status_dict["name"])):
            return None
        assert isinstance(amount, int), "the variable amount is not of type integer"
        if self.status_dict["level"] != 0:
            self.status_dict["level"] -= abs(amount)

    def multi(self, string=None, readpath=None):
        if os._exists(r"{path}\{name}.txt".format(path=self.status_dict["path"], name=self.status_dict["name"])):
            return None
        assert not (
                string is None and readpath is None), "you need to set one of the two variables to hold either a path " \
                                                      "to a readable file or a string in python "
        assert (isinstance(string, str) and readpath is None) or (isinstance(readpath,
                                                                             str) and string is None), "one of the " \
                                                                                                       "variables, " \
                                                                                                       "path and " \
                                                                                                       "string, " \
                                                                                                       "is not of " \
                                                                                                       "type string, " \
                                                                                                       "or more than " \
                                                                                                       "one of the " \
                                                                                                       "variables was " \
                                                                                                       "set "
        try:
            assert (len(
                string) >= 10) or string is None, "the string provided is not long enough to where it would make " \
                                                  "sense to do multi, please use the append() function. "
        except ValueError:
            pass
        if readpath is None:
            dump = ""
            cur = 0
            while cur < len(string) - 1:
                if cur + 2 < len(string) - 1:
                    while string[cur:cur + 2] != "\\(":
                        if cur + 2 > len(string) - 1:
                            break
                        dump += string[cur]
                        cur += 1
                if cur + 2 > len(string) - 1:
                    dump += string[cur]
                    dump += string[cur + 1]
                    break
                try:
                    self.status_dict["code"].append(
                        (" " * self.status_dict["level"] + dump + "\n"))
                    count = cur + 2
                    ext = 0
                    while string[count + ext + 1] in "0123456789":
                        ext += 1
                    self.status_dict["level"] = int(string[cur + 2:count + ext + 1])
                    dump = ""
                    cur += ext + 1 + 3
                except TypeError:
                    raise SyntaxError(
                        "during handling of the string, a character of non-int type appeared during in the tuple "
                        "formatting")
            self.status_dict["code"].append(
                (" " * self.status_dict["level"] + dump + "\n"))
        elif string is None:
            try:
                foo = open(readpath, "r+")
            except Exception as e:
                raise SyntaxError(f"the following error occurred during opening of {readpath}: \'{e}\'.")
            foo = [f.replace("\n", "").replace("\t", " " * 8) for f in foo.readlines()]
            tabs = 0
            tab_list = []
            for i in foo:
                for f in i:
                    if f == " ":
                        tabs += 1
                        continue
                    break
                tab_list.append(tabs)
                tabs = 0
            for t, k in enumerate(foo):
                dump = ""
                first = True
                for i in range(len(k)):
                    if first:
                        self.status_dict["level"] = tab_list[t]
                        first = False
                    if i < tab_list[t]:
                        continue
                    dump += k[i]
                self.status_dict["code"].append(
                    (" " * self.status_dict["level"] + dump + "\n"))
