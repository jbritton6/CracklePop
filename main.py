def crackle_pop(number):
    """FizzBuzz like program for numbers from 1 to number.
    
    Args:
        number: Integer value greater than 1.

    Returns:
        List of numbers from 1 to numbers according to the followung:
          Crackle if it is divisble by 3,
          Pop if it is divisble by 5,
          CracklePop if it is divisble by 3 and 5.

    Raises:
        ValueError: If input is less than 1.
    """
    if number < 1:
        raise ValueError('Input must be greater than 1.')
    for i in range(1, number + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print('CracklePop')
        elif i % 3 == 0:
            print('Crackle')
        elif i % 5 == 0:
            print('Pop')
        else:
            print(i)

if __name__ == '__main__':
    crackle_pop(100)