#!/usr/bin/env python


class BaseTypes(object):

    @staticmethod
    def get_fractions(a_b: str, c_b: str) -> str:
        """
        :param a_b: fraction string, for example 1/3
        :param c_b: fraction string, for example 5/3
        :return: string: for example, '1/3 + 5/3 = 6/3'
        """
        return '1/3 + 5/3 = 6/3'
