# -*- coding:utf8 -*-
"""
计算器加法、除法
"""

class Calculator:
    
    def add(self,a,b):
        return a+b

    def div(self,a,b):
        if b==0:
            return "division by zero"
        elif not isinstance(a,int) and not isinstance(a,float):
            return "TypeError"
        elif not isinstance(b,int) and not isinstance(b,float):
            return "TypeError"

        return a/b