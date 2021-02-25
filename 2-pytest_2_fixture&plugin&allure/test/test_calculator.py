#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
Calculator测试类
"""

import pytest



class TestCalc:

    def test_add_int(self, get_instance, get_add_int_datas_from_fixture):
        param = get_add_int_datas_from_fixture
        assert get_instance.add(param[0],param[1]) == param[2]

    def test_add_float(self, get_instance, get_add_float_datas_from_fixture):
        param = get_add_float_datas_from_fixture
        assert round(get_instance.add(param[0], param[1]), 3) == param[2]

    def test_add_other(self, get_instance, get_add_other_datas_from_fixture):
        param = get_add_other_datas_from_fixture
        assert get_instance.add(param[0],param[1]) == param[2]

    def test_add_typeerror(self, get_instance, get_add_typeerror_datas_from_fixture):
        param = get_add_typeerror_datas_from_fixture
        with pytest.raises(TypeError) :
            get_instance.add(param[0],param[1]) == param[2]

    def test_div_int(self, get_instance,get_div_int_datas_from_fixture):
        param = get_div_int_datas_from_fixture
        assert get_instance.div(param[0],param[1]) == param[2]

    def test_div_float(self, get_instance,get_div_float_datas_from_fixture):
        param = get_div_float_datas_from_fixture
        assert get_instance.div(param[0],param[1]) == param[2]

    def test_div_zero(self, get_instance,get_div_zero_div_datas_from_fixture):
        param = get_div_zero_div_datas_from_fixture
        assert get_instance.div(param[0],param[1]) == param[2]

    def test_div_typeerror(self, get_instance,get_div_typeerror_datas_from_fixture):
        param = get_div_typeerror_datas_from_fixture
        assert get_instance.div(param[0],param[1]) == param[2]



if __name__ == "__main__":
    pytest.main(["test_calculator.py::TestCalc","-v"])