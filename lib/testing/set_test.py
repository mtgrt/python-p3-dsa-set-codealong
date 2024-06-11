#!/usr/bin/env python3
from MySet import MySet



class TestSet:
    def test_init(self):
        '''Test __init__ set with list'''
        test_set = MySet([1, 2, 3, 4])
        assert len(test_set.elements) == 4
        for num in [1, 2, 3, 4]:
            assert num in test_set.elements

    def test_add(self):
        '''Test add() to set'''
        test_set = MySet([1, 2, 3, 4])
        test_set.add(5)
        assert 5 in test_set.elements

    def test_delete(self):
        '''Test delete()'''
        test_set = MySet([1, 2, 3, 4])
        test_set.delete(2)
        assert 2 not in test_set.elements

    def test_has(self):
        '''Test has()'''
        test_set = MySet([1, 2, 3, 4])
        assert test_set.has(3) is True
        assert test_set.has(5) is False

    def test_size(self):
        '''Test size()'''
        test_set = MySet([1, 2, 3, 4])
        assert test_set.size() == 4
