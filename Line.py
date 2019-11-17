from numpy import array, zeros, uint8
from math import floor


# Cv2 Line Class
class Line(object):
    def __init__(self, pos1, pos2, img, rgb=None):
        self.pos1, self.pos2, self.img = pos1, pos2, img
        if rgb is None: rgb = [0, 0, 0]
        self.rgb = rgb
        if type(self.pos1) != tuple or type(self.pos2) != tuple or type(self.rgb) != list or len(self.rgb) != 3 or len(
                self.pos1) != 2 or len(self.pos2) != 2: raise TypeError
        for i in range(2):
            if type(self.pos1[i]) != int or type(self.pos2[i]) != int or type(self.rgb[i]) != int: raise ValueError
        assert rgb[2] is not int, "one or more of your rgb's color values was not an integer"
        self.bgr, self.y1, self.x1, self.y2, self.x2, x1, y1, x2, y2 = [self.rgb[2], self.rgb[1], self.rgb[0]], \
                                                                       self.pos1[1], self.pos1[0], self.pos2[1], \
                                                                       self.pos2[0], self.pos1[0], self.pos1[1], \
                                                                       self.pos2[0], self.pos2[1]
        if y1 >= array(self.img).shape[1] - 1: y1 = array(self.img).shape[1] - 1
        if y2 >= array(self.img).shape[1] - 1: y2 = array(self.img).shape[1] - 1
        if x1 >= array(self.img).shape[0] - 1: x1 = array(self.img).shape[0] - 1
        if x2 >= array(self.img).shape[0] - 1: x2 = array(self.img).shape[0] - 1
        if y1 < 0: y1 = 0
        if y2 < 0: y2 = 0
        if x1 < 0: x1 = 0
        if x2 < 0: x2 = 0
        try:
            cy = int((y2 - y1) / (abs(y2 - y1)))
        except ZeroDivisionError:
            cy = 0
        try:
            cx = int((x2 - x1) / (abs(x2 - x1)))
        except ZeroDivisionError:
            cx = 0
        self.length, self.width = abs(x2 - x1), abs(y2 - y1)
        if abs(y2 - y1) == 0 and abs(x2 - x1) == 0:
            raise ValueError
        elif abs(y2 - y1) == 0 and abs(x2 - x1) != 0:
            ux, ret = x1, [((x1, y1), self.bgr)]
            while ux != x2: ux += cx; ret.append(((ux, y1), self.bgr))
            new_img = self.img.copy()
            for i in ret: new_img[i[0]] = i[1]
            self.ret, self.line_img = ret, new_img.copy()
        elif abs(y2 - y1) != 0 and abs(x2 - x1) == 0:
            uy, ret = y1, [((x1, y1), self.bgr)]
            while uy != y2: uy += cy; ret.append(((x1, uy), self.bgr))
            new_img, self.ret = self.img.copy(), ret
            for i in ret: new_img[i[0]] = i[1]
            self.line_img = new_img.copy()
        elif abs(x2 - x1) > abs(y2 - y1):
            ux, uy, ret, shift = x1, y1, [((x1, y1), self.bgr)], 0
            try:
                ca = floor(((abs(y2 - y1) / int(((abs(x2 - x1)) / (abs(y2 - y1)) * abs(y2 - y1)))) - (
                    ((int(floor(abs(x2 - x1) / abs(y2 - y1)))) * abs(y2 - y1)))))
            except ZeroDivisionError:
                ca = 0
            while ux != x2 and uy != y2:
                for i in range(int(floor(abs(x2 - x1) / abs(y2 - y1)))): ux += cx; ret.append(((ux, uy), self.bgr))
                if uy != floor(abs(y2 - y1) / 2) and shift == abs(ca):
                    ux += cx
                    ret.append(((ux, uy), self.bgr))
                    shift = 0
                elif shift == abs(ca):
                    self.mid = (ux, uy)
                    for i in range(abs(y2 - y1) - ca): ux += cx; ret.append(((ux, uy), self.bgr)); shift = 0
                else:
                    shift += 1
                uy += cy
                ret.pop()
                ret.append(((ux, uy), self.bgr))
            ret.pop()
            ret.append(((x2, y2), self.bgr))
            new_img, self.ret = self.img.copy(), ret
            for i in ret: new_img[i[0]] = i[1]
            self.line_img = new_img.copy()
        elif abs(y2 - y1) > abs(x2 - x1):
            ux, uy, ret, shift = x1, y1, [((x1, y1), self.bgr)], 0
            try:
                ca = floor((abs(x2 - x1) / int(((abs(y2 - y1)) / abs(x2 - x1))) * abs(x2 - x1)) - (
                    ((int(floor(abs(y2 - y1) / abs(x2 - x1)))) * abs(x2 - x1))))
            except ZeroDivisionError:
                ca = 0
            while ux != x2 and uy != y2:
                for i in range(int(floor(abs(y2 - y1) / abs(x2 - x1)))): uy += cy; ret.append(((ux, uy), self.bgr))
                if ux != floor(abs(x2 - x1) / 2) and shift == abs(ca):
                    uy += cy
                    ret.append(((ux, uy), self.bgr))
                    shift = 0
                elif shift == abs(ca):
                    self.mid = (ux, uy)
                    for i in range(abs(x2 - x1) - ca): uy += cy; ret.append(((ux, uy), self.bgr)); shift = 0
                else:
                    shift += 1
                ux += cx
                ret.pop()
                ret.append(((ux, uy), self.bgr))
            ret.pop()
            ret.append(((x2, y2), self.bgr))
            new_img, self.ret = self.img.copy(), ret
            for i in ret: new_img[i[0]] = i[1]
            self.line_img = new_img
        elif abs(y2 - y1) == abs(x2 - x1):
            ux, uy, ret = x1, y1, [((x1, y1), self.bgr)]
            while ux != x2 and uy != y2: uy += cy; ux += cx; ret.append(((ux, uy), self.bgr))
            ret.append(((x2, y2), self.bgr))
            new_img, self.ret = self.img.copy(), ret
            for i in ret: new_img[i[0]] = i[1]
            self.line_img = new_img
        if self.y2 == self.y1:
            self.type, self.start_cords, self.end_cords, self.mid = "horizontal", (min(x1, x2), y1), (
                max(x1, x2), y1), (floor((x1 + x2) / 2), y1)
        elif self.x2 == self.x1:
            self.type, self.start_cords, self.end_cords, self.mid = "vertical", (x1, min(y2, y1)), (x1, max(y2, y1)), (
                x1, floor((y1 + y2) / 2))
        elif (self.x1 > self.x2 and self.y2 > self.y1) or (self.x1 < self.x2 and self.y2 < self.y1):
            self.type, self.start_cords, self.end_cords = "diagonal_r", (
                [x for x in [(x1, y1), (x2, y2)] if x[1] == min(y2, y1)][0], min(y2, y1)), (
                                                              [x for x in [(x1, y1), (x2, y2)] if x[1] == max(y2, y1)][
                                                                  0],
                                                              max(y2, y1))
        else:
            self.type, self.start_cords, self.end_cords = "diagonal_l", (
                [x for x in [(x1, y1), (x2, y2)] if x[1] == min(y2, y1)][0], min(y2, y1)), (
                                                              [x for x in [(x1, y1), (x2, y2)] if x[1] == max(y2, y1)][
                                                                  0],
                                                              max(y2, y1))

    @staticmethod
    def blank_image(one_rgb):
        assert isinstance(one_rgb, int), "your single rgb type was not of type integer"
        assert 0 < one_rgb < 256, "your single rgb was less/more than the range of values for an rgb"
        img = zeros((512, 512, 3), uint8)
        img.fill(255)
        return img.copy()

    @staticmethod
    def update(img, line_list):
        out_img = img.copy()
        assert isinstance(line_list, list), "the line list was not of type list"
        for i in line_list:
            assert isinstance(i, Line), "the values within your line list were not of type line"
            for p in i.ret: out_img[p[0]] = p[1]
        return out_img

    @staticmethod
    def delete(img, line_list, orig_rgb, ignore_rgb=None):
        out_img = img.copy()
        if len(orig_rgb) != 3 or type(line_list) != list or type(orig_rgb) != list or (
                ignore_rgb is not None and type(ignore_rgb) != list) or (
                ignore_rgb is not None and len(ignore_rgb) != 3): raise ValueError
        if ignore_rgb is not None: assert all([isinstance(i, int) for i in ignore_rgb]) or all(
            [0 < i < 256 for i in ignore_rgb]), "your rgb value to ignore was not of correct format"
        assert ([isinstance(i, int) for i in orig_rgb]) or all(
            [0 < i < 256 for i in orig_rgb]), "your original rgb color was not of correct format"
        for i in line_list:
            assert isinstance(i, Line), "the values within your line list were not of type line"
            for p in i.ret:
                if ignore_rgb is not None and all([ignore_rgb[i] == p[0][i] for i in range(3)]): continue
                out_img[p[0]] = orig_rgb
        return out_img