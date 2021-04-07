# -*- coding: utf-8 -*-
"""Main module template with example functions."""


def sum_numbers(number_list):
    """Example function. Sums a list of numbers using a for loop.

    Parameters
    ----------
    number_list : list
        List of ints or floats

    Returns
    -------
    int or float
        Sum of list

    Notes
    -----
    This is NOT good Python, just an example function for tests.

    Examples
    --------
    >>> number_list = [2,3,4]
    >>> sum_numbers(number_list)
    9
    """

    sum_val = 0
    for n in number_list:
        sum_val += n

    return sum_val


def max_number(number_list):
    """Example function. Finds max of list of numbers using a for loop.

    Parameters
    ----------
    number_list : list
        List of ints or floats

    Returns
    -------
    int or float
        Sum of list

    Notes
    -----
    Also not good Python.


    Examples
    --------
    >>> number_list = [2,3,4]
    >>> max_number(number_list)
    4
    """

    cur_max = number_list[0]
    for n in number_list[1:]:
        if n > cur_max:
            cur_max = n

    return cur_max

# std::vector<double> add_vectors(std::vector<double> &v1, std::vector<double> &v2)
# {
#     // Check inputs
#     if (v1.size() != v2.size())
#     {
#         throw std::invalid_argument("There's a mismatch in vector size" + std::to_string(v1.size()) + "!=" + std::to_string(v2.size()));
#     }

#     //
#     // Solution 1
#     //

#     // Add the vectors
#     std::vector<double> new_vector(v1.size());

#     for (size_t i = 0; i < v1.size(); i++)
#     {
#         new_vector[i] = v1[i] + v2[i];
#     }

#     //
#     // Solution 2
#     //

#     // std::vector<double> new_vector = v1;
#     // std::transform(new_vector.begin(), new_vector.end(), v2.begin(), new_vector.begin(), std::plus<double>());

#     return new_vector;
# }
