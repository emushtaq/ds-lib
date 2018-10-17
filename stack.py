# -*- coding: utf-8 -*-
""" Stack.py

This module demonstrates an implementation of the abstract data type - Stack implemented using lists in python.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
from exception import DS_LIB_ERROR


class Stack:
    def __init__(self):
        self.values = []

    def push(self, data):
        return self.values.append(data)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values[len(self.values) - 1]

    def isEmpty(self):
        return self.values == []

    def size(self):
        return len(self.values)
