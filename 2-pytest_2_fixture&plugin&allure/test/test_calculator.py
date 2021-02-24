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
    # calc = Calculator()
    add_normal_data = get_datas('add','normal')
    div_int_normal = get_datas('div','int_normal')
    div_zero_div = get_datas('div', 'zero_div')
    div_type_error = get_datas('div', 'type_error')

    def setup_class(self):
        self.calc = Calculator()


    def setup(self):
        print("开始计算")


    def teardown(self):
        print("计算结束")


    @pytest.mark.parametrize(['a', 'b', 'result'],add_normal_data[0],ids=add_normal_data[1])
    def test_add_normal(self,a,b,result):
        assert self.calc.add(a,b) == result


    @pytest.mark.parametrize(['a', 'b', 'result'], div_int_normal[0], ids=div_int_normal[1])
    def test_div_int_normal(self,a,b,result):
        assert self.calc.div(a,b) == result


    @pytest.mark.parametrize(['a', 'b', 'result'], div_zero_div[0], ids=div_zero_div[1])
    def test_div_zero_div(self, a, b, result):
        # with pytest.raises(ZeroDivisionError) as excinfo:
        #     assert self.calc.div(a,b)
        # assert result in str(excinfo.value)
        assert self.calc.div(a,b) == result


    @pytest.mark.parametrize(['a', 'b', 'result'], div_type_error[0], ids=div_type_error[1])
    def test_div_type_error(self, a, b, result):
        assert self.calc.div(a, b) == result




if __name__ == "__main__":
    pytest.main(["test_calculator.py::TestCalc","-v"])