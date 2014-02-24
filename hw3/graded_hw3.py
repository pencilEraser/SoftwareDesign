# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Neal S.  

Appreciation and credit to Abe Kim for his patience and assistance.
        
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from random import shuffle


# import gene_finder
# reload(gene_finder)

def segment_sequence(dna):

    remainder = len(dna) % 3
    length_of_seq = len(dna)
    seq = []
    i = 0
    while (i < (length_of_seq-remainder)):
        seq.append(dna[i] + dna[i+1] + dna[i+2])
        i += 3

    if remainder == 1:
        seq.append(dna[length_of_seq-1])
    elif remainder == 2:
        seq.append(dna[length_of_seq-2] + dna[length_of_seq-1])
        
    return seq   


def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    
    # YOUR IMPLEMENTATION HERE
#    acids = ''
#    dna_to_compare = ''
#    for i in range(0, len(dna)-2, 3):
#        dna_to_compare = dna[i] + dna[i+1] + dna[i+2]
#        for j in range(len(codons)):
#            if dna_to_compare in codons[j]:
#                acids += aa[ j ]
#    return acids

    acids = ''
    dna_triplets = segment_sequence(dna)
    print dna_triplets
    for triplet in dna_triplets:
        for i in range(len(codons)):    
            if triplet in codons[i]:
                acids += aa[i]
                print acids
    return acids
    
    
def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
        
    # YOUR IMPLEMENTATION HERE

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    # YOUR IMPLEMENTATION HERE    
    
    dna = dna.upper()[::-1]
    dna_reverse_complement = ''
    for i in range(len(dna)):
        if dna[i] == 'A':
            dna_reverse_complement += 'T'
        elif dna[i] == 'T':
            dna_reverse_complement += 'A'
        elif dna[i] == 'C':
            dna_reverse_complement += 'G'
        else:
            dna_reverse_complement += 'C'

    return dna_reverse_complement
    
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    # YOUR IMPLEMENTATION HERE    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
    """

    dna_triplets = segment_sequence(dna)
    sequence = ''
    i = 0
    while dna_triplets[i] != "ATG":
        i += 1
        if i == len(dna_triplets):
            return
        
    while (i < len(dna_triplets)):
        if dna_triplets[i] in ['TAA', 'TAG', 'TGA']:
            return sequence #stop codon reached so return string up to the point.
        sequence += dna_triplets[i]
        i += 1
    return sequence #no stop codon reached, return whole string.
            
    
    
    
        
    

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    # YOUR IMPLEMENTATION HERE
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """



    sequence = []
    i = 0
    
    while (i < len(dna)-2):
        start_codon = dna[i] + dna[i+1] + dna[i+2]
        if start_codon == 'ATG':
            sequence.append(rest_of_ORF(dna[i:]))
#            print "sequence is "            
#            print sequence
            i += len(sequence[-1])
        i += 3
        
    return sequence   


     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    # YOUR IMPLEMENTATION HERE

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    return find_all_ORFs_oneframe(dna[0:]) + find_all_ORFs_oneframe(dna[1:]) + find_all_ORFs_oneframe(dna[2:])
     

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    return find_all_ORFs(dna) + find_all_ORFs(get_reverse_complement(dna))

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    # YOUR IMPLEMENTATION HERE

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string        
    """
    
    strands = find_all_ORFs_both_strands(dna)
    longest = 0
    i = 0
    while (i < len(strands) ):
        if len(strands[i]) > len(strands[i-1]):
            longest = strands[i]
        i += 1
        
    return longest
    


def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    # YOUR IMPLEMENTATION HERE

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    dna_list = []
    dna_list = list(dna)
    i = 0    
    longest_old = ''
    while (i < num_trials):
        shuffle(dna_list)
        dna_string = collapse(dna_list)                
        longest = longest_ORF(dna_string)
        if (len(longest) > len(longest_old)):
            longest_old = longest
        dna_list = list(dna_string)
        i += 1
    return len(longest_old)
    
    
def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    amino_acid_sequences = []
    orf_list = find_all_ORFs_both_strands(dna)
    
    for orf in orf_list:
        if len(orf) > threshold:
            amino_acid_sequences.append(coding_strand_to_AA(orf))
    return amino_acid_sequences
        
        
        