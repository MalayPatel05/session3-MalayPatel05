# Session 3 - Numeric Types Assignment

This assignment project is written in Python, and tested with pytest. It includes following files.
-session3.py      : This is the assignment code which needs to be fixed
-test_session3.py : This is pytest unit test. It tests completeness of assignment

>This assignment checks understanding of following concepts:
- Base conversion from base 10 numbers
- Floats equality using relative and absolute tolerance
- Truncation without using buit in functions
- Rounding towards zero
- Rounding towards infinity
- Use of Fraction for truncation
- Use of div operator

> Description of Functions/Class along with bug fixes

### encoded_from_base10
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    This function validates input as follow before changing base:
    - 2 <= base <= 36 else raise error ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the math module such as bin() or hex()

### float_equality_testing
    This function emulates the isclose method from the math module	
    We are going to assume:
      - Relative tolerance = 1e-12
      - Absolute tolerance = 1e-05
	This function uses maximum of relative and absolute tolerance for equality test.
	Relative tolerance = rel_tol * max (|x|,|y|)
	tol = max(rel_tol,abs_tol)
	If absolute difference of two numbers are less than tol then they are considered equal.
### manual_truncation_function
    This function emulates python's math.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. 
	This function does not use inbuilt constructors like int, float, etc
	This function gets fraction of float number and than uses div operator to get truncated value
	truncated value = numerator//denomenator
### manual_rounding_function
	This function emulates python's inbuild ROUND function.
    This function rounds float number to nearest integer number.
	
	-To get the number after decimal points it first gets truncated number and then take difference of foat number and truncated number.
	
	digit_after_decimal = f_num - trunc(f_num)
	
	-To get first digit after decimal point it first multiplies digit_after_decimal with 10 and then gets truncated number of it
	
	first_digit_after_decimal = trunc(digit_after_decimal*10)
	
	-Then if first_digit_after_decimal>5 the number is rounded up away from zero otherwise rounded towards zero .
### rounding_away_from_zero
	This function implements rounding away from zero as covered in the class.
	In case of tie when first digit after decimal point is 5, this function rounds away from zero.
. 	It first adds 0.5 in given number and then rounds it to nearest integer number using truncation function.
    If float number is 10.6 after adding 0.5, resultant number 11.1 will be truncated to 11. Similar way negative number are rounded away from zero.

### Unit Test Results

Unit test results screenshot uploaded in Unit_Test_Results.JPG