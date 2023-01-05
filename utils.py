'''The module contains functions for additions to other classes. From time
to  time these functions are brought together in some functionality class'''
import inflect

inflect_engine = inflect.engine()


def number_to_words(number):
    """__number_to_words Convert number to words .

    Args:
        number ([type]): [description]

    Returns:
        [type]: [description]
    """
    return inflect_engine.number_to_words(number)
