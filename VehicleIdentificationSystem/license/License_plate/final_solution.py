# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:55:41 2020

@author: lenovo
"""
import os
from . import img_pretreatment as ip
from . import string_cut as sc
from . import predict_province as pp
from . import predict_digits as pd
from . import predict_letters as pl


def get_result(image_path):
    PROVINCES = (
    "京", "闽", "粤", "苏", "沪", "浙", "津", "渝", "冀", "豫", "云", "辽", "黑", "湘", "皖", "鲁", "新", "赣", "鄂", "桂", "甘", "晋", "蒙",
    "陕", "吉", "贵", "青", "藏", "川", "宁", "琼")

    LETTERS = (
    "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "I", "O")

    DIGITS = (
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P",
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

    pretreatment = ip.run(image_path)  # 改一下这里的路径就行
    sc.cut(pretreatment)
    cache_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'License_plate/cache/')
    if len(os.listdir(cache_path)) != 7:
        return None
    else:
        pro_max1_index, pro_max1, pro_max2_index, pro_max2, pro_max3_index, pro_max3 = pp.predict()
        let_max1_index, let_max1, let_max2_index, let_max2, let_max3_index, let_max3 = pl.predict()
        dig_max1_index, dig_max1, dig_max2_index, dig_max2, dig_max3_index, dig_max3 = pd.predict()
        province_result = {'first': {'result': PROVINCES[pro_max1_index], 'probability': pro_max1},
                           'second': {'result': PROVINCES[pro_max2_index], 'probability': pro_max2},
                           'third': {'result': PROVINCES[pro_max3_index], 'probability': pro_max3}}
        letter_result = {'first': {'result': LETTERS[let_max1_index], 'probability': let_max1},
                         'second': {'result': LETTERS[let_max2_index], 'probability': let_max2},
                         'third': {'result': LETTERS[let_max3_index], 'probability': let_max3}}
        digit_result = {'first': {'result': DIGITS[dig_max1_index], 'probability': dig_max1},
                        'second': {'result': DIGITS[dig_max2_index], 'probability': dig_max2},
                        'third': {'result': DIGITS[dig_max3_index], 'probability': dig_max3}}
        result = {'pro': province_result, 'let': letter_result, 'dig': digit_result}
        return result