#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
Calculator测试类
"""

import sys

import pytest
import yaml

sys.path.append('..')
from calc_python.calculator import Calculator



def get_datas(name, type):

    with open('datas/calc.yml','rt') as f:
        all_datas = yaml.safe_load(f)
    test_data = all_datas[name][type]['datas']
    test_ids = all_datas[name][type]['ids']

    return (test_data,test_ids)


class TestCalc:

    add_int_data = get_datas('add', 'int')
    add_float_data = get_datas('add', 'float')
    add_other_data = get_datas('add', 'other')
    add_typeerror_data = get_datas('add', 'type_error')

    div_int_normal = get_datas('div','int_normal')
    div_float_normal = get_datas('div', 'float_normal')
    div_zero_div = get_datas('div', 'zero_div')
    div_type_error = get_datas('div', 'type_error')

    def setup_class(self):
        self.calc = Calculator()


    def setup(self):
        print("开始计算")


    def teardown(self):
        print("计算结束")


    @pytest.mark.parametrize(['a', 'b', 'result'], add_int_data[0], ids=add_int_data[1])
    def test_add_int(self,a,b,result):
        assert round(self.calc.add(a, b), 3) == result

    @pytest.mark.parametrize(['a', 'b', 'result'], add_float_data[0], ids=add_float_data[1])
    def test_add_float(self, a, b, result):
        assert round(self.calc.add(a, b), 3) == result


    @pytest.mark.parametrize(['a', 'b', 'result'], add_other_data[0], ids=add_other_data[1])
    def test_add_other(self, a, b, result):
        assert self.calc.add(a, b) == result

    @pytest.mark.parametrize(['a', 'b', 'result'], add_typeerror_data[0], ids=add_typeerror_data[1])
    def test_add_type_error(self, a, b, result):
        with pytest.raises(TypeError):
            self.calc.add(a, b) == result

    @pytest.mark.parametrize(['a', 'b', 'result'], div_int_normal[0], ids=div_int_normal[1])
    def test_div_int(self,a,b,result):
        assert self.calc.div(a,b) == result

    @pytest.mark.parametrize(['a', 'b', 'result'], div_float_normal[0], ids=div_float_normal[1])
    def test_div_float(self,a,b,result):
        assert self.calc.div(a,b) == result

    @pytest.mark.parametrize(['a', 'b', 'result'], div_zero_div[0], ids=div_zero_div[1])
    def test_div_zero_div(self, a, b, result):
        # with pytest.raises(ZeroDivisionError) as excinfo:
        #     self.calc.div(a,b)
        assert self.calc.div(a,b) == result


    @pytest.mark.parametrize(['a', 'b', 'result'], div_type_error[0], ids=div_type_error[1])
    def test_div_type_error(self, a, b, result):
        assert self.calc.div(a, b) == result




if __name__ == "__main__":
    pytest.main(["test_calculator.py::TestCalc","-v"])