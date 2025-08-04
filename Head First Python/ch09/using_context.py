# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 11:25:36 2025

@author: ArtemT

Эксперимент с контекстом with.
"""

class UseSet:
    
    
    def __init__(self, data: set) -> None:
       self.data = data
    
    
    def __enter__(self) -> set:
        print('Входные данные: ', self.data)
        return self.data
    
    
    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        print('Данные в контексте: ', self.data)