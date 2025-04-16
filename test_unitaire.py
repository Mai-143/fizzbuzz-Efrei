import pytest
from main import fizzbuzz

def test_fizzbuzz():
    output = fizzbuzz()
    
    assert len(output) == 100  
    assert output[2] == "Fiz"  
    assert output[4] == "Buzz"  
    assert output[14] == "FizzBuzz"  
    assert output[98] == "Fizz"  
    assert output[99] == "Buzz"  
    assert output[0] == 1  
    assert output[1] == 2 
