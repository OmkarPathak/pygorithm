"""
Base2 to Base16

Convert binary numbers to hexadecimal numbers

Author: Ian Doarn
"""


hex_values = {"0000": "0", "0001": "1", "0010": "2",
              "0011": "3", "0100": "4", "0101": "5",
              "0110": "6", "0111": "7", "1000": "8",
              "1001": "9", "1010": "A", "1011": "B",
              "1100": "C", "1101": "D", "1110": "E",
              "1111": "F"}


def convert_base2_to_base16(n, visualize=False):
    """
    Convert binary numbers to hexadecimal numbers

    :param n: binary number
    :param visualize: Visualise the process
    :return: hexadecimal number
    """
    grouped_list = __create_group_list(n)
    _list = []
    for value in grouped_list:
        if visualize:
            print("{} -> {}".format(value, hex_values[value]))
        # for each value in the grouped_list,
        # get its respective value from the hex
        # table by referencing the key with the
        # current value from the grouped_list
        _list.append(hex_values[value])

    return ''.join(_list)


def __create_group_list(n):
    """
    Helper method for conversion

    Takes binary number and converts to a list of
    grouped binary values

    Process:
        1. convert number to a list of chars
        2. reverse the list
        3. iterate through the list creating groups of 4
           removing each value as its iterated
        4. if the remaining values can not make a group,
           add 0's to the end to get to 4
        5. join each list together
        6. reverse each value in the final list to put
           them back in order

    Example:

        n = 11101100101001001100101001
        reverse = 10010100110010010100110111

        Start grouping values:

            [['1', '0', '0', '1'],
             ['0', '1', '0', '0'],
             ['1', '1', '0', '0'],
             ['1', '0', '0', '1'],
             ['0', '1', '0', '0'],
             ['1', '1', '0', '1']]

             remaining value = 11
             add missing 0's -> 1100
             
        join each list:
        
            ['1', '0', '0', '1'] = 1001
            ['0', '1', '0', '0'] = 0100
            ['1', '1', '0', '0'] = 1100
            ['1', '0', '0', '1'] = 1001
            ['0', '1', '0', '0'] = 0100
            ['1', '1', '0', '1'] = 1101

        ['1100', '1101', '0100', '1001', '1100', '0100', '1001']
        
        reverse final list
        result = ['0011', '1011', '0010', '1001', '0011', '0010', '1001']

    :param n: binary number
    :return: list
    """
    reversed_number_list = list(str(n)[::-1])
    grouped_list = []

    while len(reversed_number_list) != 0:
        # go until list is empty
        if len(reversed_number_list) < 4:
            # remaining values can not make a group
            # join remaining values
            value = ''.join(reversed_number_list)
            # find the missing amount needed then add that many
            # zeros to the end of the value
            f_value = value + ('0' * (4 - len(value)))
            # add to the group
            grouped_list.append(f_value)
            break
        else:
            temp_list = []
            while len(temp_list) != 4:
                # go until temp list does not have 4 values
                temp_list.append(reversed_number_list.pop(0))
        # join each value in temp list and add to group
        grouped_list.append(''.join(temp_list))

    # reverse the entire grouped_list
    # then reverse each value in the grouped_list
    # and return the results
    return [i[::-1] for i in grouped_list[::-1]]
