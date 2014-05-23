import math
def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return dna1 > dna2

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(s):
    '''(str) -> bool
    Return True if and only if DNA sequence is valid(that is, it contains no characters other than 'A', 'T', 'C', 'G').
    >>>is_valid_sequence('ATGCGAT')
    True
    >>>is_valid_sequence('ABCTG')
    False
    '''
    num_dna = 0
    for char in s:
        if char in 'ATCG':
            num_dna = num_dna + 1
        else:
            num_dna = num_dna
    return num_dna == len(s)

def insert_sequence(s1, s2, number):
    '''(str, str, int) -> str
     Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index.
     >>>insert_sequence('GTCACTG', 'AG', 3)
     'GTCAGACTG'
     >>>insert_sequence('TGACT', 'CT', 2)
     'TGCTACT'
     '''

    s = s1[:number] + s2 + s1[number:]
    return s

def get_complement(s):
    '''(str) -> str
    Return the nucleotide's complement
    >>>get_complement('T')
    'A'
    >>>get_complement('C')
    'G'
    '''
    if s == 'A':
        return 'T'
    if s == 'T':
        return 'A'
    if s == 'C':
        return 'G'
    if s == 'G':
        return 'C'

def get_complementary_sequence(s):
    '''(str) -> str
    Return the DNA sequence that is complementary to the given DNA sequence.
    >>>get_complementary_sequence('TGAGTC')
    'ACTCAG'
    >>>get_complementary_sequence('GCACTGT')
    'CGTGACA'
    '''
    s1 = ''
    for char in s:
        if char == 'A':
           s1 = s1 + 'T'
        if char == 'T':
           s1 = s1 + 'A'
        if char == 'G':
           s1 = s1 + 'C'
        if char == 'C':
           s1 = s1 + 'G'
        else:
            s1 = s1
    return s1
