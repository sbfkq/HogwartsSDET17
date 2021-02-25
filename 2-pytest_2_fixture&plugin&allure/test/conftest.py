#!/usr/bin/env python
# -*- coding:utf8 -*-
# conftest.py 文件名是固定的，不能改
import sys
sys.path.append('../../2-pytest_2_fixture&plugin&allure')

import pytest
import yaml
from calc_python.calculator import Calculator

@pytest.fixture(scope='session')        # 每个包只运行一次（session,module,class,function)
def get_instance():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("结束计算")


def get_datas(name,type):
    with open('datas/calc.yml') as f:
        datas = yaml.safe_load(f)
    testdata = datas[name][type]['datas']
    ids = datas[name][type]['ids']
    return (testdata, ids)


@pytest.fixture(params=get_datas('add','int')[0],ids=get_datas('add','int')[1])
def get_add_int_datas_from_fixture(request):
    return request.param

@pytest.fixture(params=get_datas('add','float')[0],ids=get_datas('add','float')[1])
def get_add_float_datas_from_fixture(request):
    return request.param

@pytest.fixture(params=get_datas('add','other')[0],ids=get_datas('add','other')[1])
def get_add_other_datas_from_fixture(request):
    return request.param

@pytest.fixture(params=get_datas('add','type_error')[0],ids=get_datas('add','type_error')[1])
def get_add_typeerror_datas_from_fixture(request):
    return request.param

@pytest.fixture(params=get_datas('div','int_normal')[0],ids=get_datas('div','int_normal')[1])
def get_div_int_datas_from_fixture(request):
    return request.param

@pytest.fixture(params=get_datas('div','float_normal')[0],ids=get_datas('div','float_normal')[1])
def get_div_float_datas_from_fixture(request):
    return request.param

@pytest.fixture(params=get_datas('div','zero_div')[0],ids=get_datas('div','zero_div')[1])
def get_div_zero_div_datas_from_fixture(request):
    return request.param

@pytest.fixture(params=get_datas('div','type_error')[0],ids=get_datas('div','type_error')[1])
def get_div_typeerror_datas_from_fixture(request):
    return request.param