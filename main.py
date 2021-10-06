#!/usr/bin/env python


def get_fractions(a_b: str, c_b: str) -> str:
    """
    Create a function what takes two parameters of string type which are fractions and
    returns a sum expression of these fractions and the sum result.
    """
    return (
        a_b
        + " + "
        + c_b
        + " = {}/{}".format(
            int(a_b.split("/")[0]) + int(c_b.split("/")[0]), a_b.split("/")[-1]
        )
    )
