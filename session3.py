from fractions import Fraction 
def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''

    if not(isinstance(base,int)) or base<2 or base>36:#Check base is integer number and base is between 2 to 36 (including)
        raise ValueError('Number base should be an value between 2 and 36')    
    elif len(digit_map)!=base:#Check digit_map has sufficient number of characters
        raise ValueError(f'digit_map should has {len(digit_map)} characters, it should have {base} characters')

    loc=1 #to fetch from next charator in digit_map
    for x in digit_map:#Check digit_map doesnot have repeated character
        for i in range(loc,len(digit_map)-1):
            if x == digit_map[i]:
                raise ValueError('No repeating characters allowed in digit map')                        
        loc = loc + 1

    if number<0: #check if number is negative
        number = abs(number)
        num_sign = '-' #Store sign
    else:
        num_sign=''

    if number==0:
        return [0]
    new_number = [ ]
    while number>0: # change base
        remainder=number%base
        number=number//base
        new_number.insert(0,digit_map[remainder])

    return (num_sign+''.join(new_number))

def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05
    tol=max(rel_tol*max(abs(a),abs(b)),abs_tol)
    if abs(a-b)<tol:
        return True
    else:
        return False

def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can not use inbuilt constructors like int, float, etc
    '''
    if not(isinstance(f_num,int) or isinstance(f_num,float)): # check if number is a Rational number
        raise ValueError('Please provide Integer or Float numbers only!')

    fraction_num = Fraction(str(f_num)) # Get fraction of float number
    if f_num >=0: #Use div operator to get truncated number
        trunc_num = fraction_num.numerator//fraction_num.denominator
    else: #if negative Truncate towards zero
        trunc_num = fraction_num.numerator//fraction_num.denominator + 1

    return trunc_num

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    if f_num>=0:
        sign_bit = 1
    else:
        sign_bit = -1
        f_num = abs(f_num)
# To get the number after decimal points first get truncated number and then take difference of float number and truncated number
    trunc_num = manual_truncation_function(f_num)
    trunc_num1 = manual_truncation_function((f_num-trunc_num)*10)# get the first digit after decimal point

    if trunc_num1 > 5:
        return ((trunc_num+1)*sign_bit)
    else:
        return trunc_num*sign_bit

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    if f_num>=0:
        sign_bit = 1
    else:
        sign_bit = -1
        f_num = abs(f_num)
    round_up = f_num + 0.5
    trunc_num = manual_truncation_function(round_up)         
    return trunc_num*sign_bit