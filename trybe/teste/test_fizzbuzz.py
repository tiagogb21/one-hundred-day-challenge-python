from exercicio.fizzbuzz import fizzbuzz

def test_fizzbuzz_should_return_list_of_numbers():
    assert fizzbuzz(2) == [1, 2]

def test_fizzbuzz_should_return_list_of_numbers():
    assert fizzbuzz(3)[-1] == "Fizz"

def test_fizzbuzz_should_return_list_of_numbers():
    assert fizzbuzz(5)[-1] == "Buzz"

def test_fizzbuzz_should_return_list_of_numbers():
    assert fizzbuzz(15)[-1] == "FizzBuzz"