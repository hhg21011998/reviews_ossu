# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

list_permutations = list()

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    n = len(sequence)
    calculate(sequence, 0, n-1)
    return list_permutations
    
def calculate(sequence, left, right):
    """
    Parameters
    ----------
    sequence : str
        this is the word we take.
    left : int
        the first letter in word.
    right : int
        the last letter in word.

    Returns: None
    -------
    """
    
    # Check left and right, if eft == right this means we reach at the end of sequence,
    # and we have nothing to do so we add this sequence to global list.
    if left == right :
          list_permutations.append(sequence)
          
    # Otherwise, we go through the first letter to last letter,
    # each recursion cycle, we move one char to the right    
    else :
        i = left
        while i <= right:
            swapped = swapChar(sequence, left, i)
            calculate(swapped, left + 1, right)
            i += 1
        
def swapChar(sequence, i, j):
    """
    Swap letters i and j place in sequence.

    Parameters: 
    ----------
    sequence: str
    i: int
    j: int

    Returns: string after swapping 2 char in it.
    -------
    """
    temp = ""
    listOfSequence = list()
    for letter in sequence:
        listOfSequence.append(letter)
    temp = listOfSequence[i]
    listOfSequence[i] = listOfSequence[j]
    listOfSequence[j] = temp
    
    return "".join(listOfSequence)


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    a = get_permutations("ABC")
    print(a)