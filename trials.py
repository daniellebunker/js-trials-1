"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    evenNums = []

    for num in nums:
        if num % 2 == 0:
            evenNums.append(nums)
    
    return nums

def get_odd_indices(items):

    result = []

    for i in range(len(items)):
        if i % 2 == 0:
            result.append(items[i])
    
    return result

def print_as_numbered_list(items):
    i = 1

    for i in items:
        print(f'{i}. {item}')
    
    i = items[i] + 1

def get_range(start, stop):
    nums = []

    for num in range(start, stop):
        nums.append(num)
    
    return nums

def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letters)

    return chars

def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
