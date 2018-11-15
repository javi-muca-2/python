"""
Primeros ejercicios
"""
import re
import copy
import collections
import random
import amino_dicts


# 1
def is_dna_strand(strand: str) -> bool:
    "Checks if sequence is valid (ACTG characters)"
    checker = False
    strand = strand.replace(' ', '')
    if strand:
        if isinstance(strand, str):
            pattern = r'^[actgCAGT]+$'
            valid = re.search(pattern, strand)
            if valid:
                checker = True
    return checker


# 2
def reverse_strand(strand: str) -> str:
    "Reverses a strand"
    dna = copy.copy(strand)
    dna = dna.replace(' ', '')
    if dna:
        if isinstance(dna, str):
            dna = dna[::-1]
    return dna


# 3
def make_complementary_strand(strand: str) -> str:
    "Converts a DNA sequence into complementary"
    dna = copy.copy(strand)
    dna = dna.replace(' ', '')
    if dna:
        if isinstance(dna, str):
            dnac = dna.translate(str.maketrans('actgACTG', 'tgacTGAC'))
    return dnac


# 4
def make_reverse_complementary_strand(strand: str)-> str:
    "Reverse complementary strand from a DNA sequence"
    dna = copy.copy(strand)
    dna = dna.replace(' ', '')
    if dna:
        if isinstance(dna, str):
            complementary = make_complementary_strand(dna)
            cdna = reverse_strand(complementary)
    return cdna


# 5
def is_dna_palindrome(strand: str) -> bool:
    "Checks if the strain is palindromic"
    checker = False
    if strand == make_reverse_complementary_strand(strand):
        checker = True
    return checker


# 6.a
def transcribe_from_coding_strand(strand: str) -> str:
    "cdna? transcription to RNA"
    dna = copy.copy(strand)
    dna = dna.replace(' ', '')
    rna = dna.translate(str.maketrans('tT', 'uU'))
    return rna


# 6.b
def transcribe_from_complementary_strand(strand: str) -> str:
    "cdna? transcription"
    rna = copy.copy(strand)
    rna = rna.replace(' ', '')
    rna = rna.translate(str.maketrans('aAtTcCgG', 'uUaAgGcC'))
    return rna


# 7
def get_pretty_codons(strand: str) -> str:
    "Inserts a whitespace every 3 characters of the strand to read it properly for a human"
    codons = copy.copy(strand)
    codons = codons.replace(' ', '')
    codons = ' '.join([codons[i:i+3] for i in range(0, len(codons), 3)])
    return codons


# 8.a
def translate_str(strand: str) -> str:
    "RNA translation to aminoacids"
    rna = copy.copy(strand).upper()
    rna = rna.replace(' ', '')
    proteins = ""

    if len(rna) % 3 == 0:
        for i in range(0, len(rna), 3):
            codon = rna[i:i+3]
            proteins += amino_dicts.single_letter[codon]
    else:
        proteins += "-"
    return proteins


# 8.c
def translate_arr(codon_list: list) -> []:
    "RNA translation to aminoacids"
    output_array = []
    for codon in codon_list:
        rna_strand = copy.copy(codon).upper()
        rna_strand = rna_strand.replace(' ', '')
        if len(rna_strand) % 3 == 0:
            for i in range(0, len(rna_strand), 3):
                codon = rna_strand[i:i+3]
                output_array.append(amino_dicts.single_letter[codon])
        else:
            output_array.append('-')
    return output_array


# 9
def get_actg_stats(strand: str) -> {}:
    "Show the number of nucleotids on a given strand"
    dna = copy.copy(strand)
    dna = dna.replace(' ', '')
    stats = {'a': 0, 'c': 0, 't': 0, 'g': 0}
    for i in dna:
        if i in ('a', 'A'):
            stats['a'] += 1
        elif i in ('c', 'C'):
            stats['c'] += 1
        elif i in ('t', 'T'):
            stats['t'] += 1
        elif i in ('g', 'G'):
            stats['g'] += 1
    return stats


# 9.pablo.pro
def get_actg_stats_pro(strand: str) -> {}:
    "Show the number of nucleotids on a given strand"
    nucleotides = ['A', 'C', 'T', 'G']
    histogram = collections.Counter(strand)

    # ensure all characters are valid nucleotides
    for nucl in nucleotides:
        # whutsgoinon, TypeError: unhashable type: 'list' -> pasar a array?
        histogram[nucl] = histogram.get(nucleotides, 0)

    # removes all letters that are not nucleotides
    keys = list(histogram.keys())
    for letter in keys:
        if letter not in nucleotides:
            del histogram[letter]

    return histogram


# 10
def get_codon_dict(amino_dict_in: {}) -> {}:
    "Makes a dictionary for each aminoacid and his codons"
    amino_dict = {}
    aminoacids = set(amino_dict_in.values())

    for aminoacid in aminoacids:
        amino_dict[aminoacid] = []

    for codon, amino in amino_dict_in.items():
        amino_dict[amino].append(codon)

    return amino_dict


# 11
def get_amino_stats(protein: str)-> {}:
    "Makes a dictionary of aminoacids from a protein sequence"
    aminoacids = set(amino_dicts.single_letter.values())

    # cuenta cada elemento y le asigna cuantas veces se repite
    # esto en realidad ya lo haría, pero no pone a 0 los aminoacidos que no aparecen y no valida
    amino_dict = collections.Counter(protein)

    # default value for not existing aminoacids
    for aminoacid in aminoacids:
        amino_dict[aminoacid] = amino_dict.get(aminoacid, 0)

    # deleting non existing aminoacids
    keys = list(amino_dict.keys())
    for letter in keys:
        if letter not in aminoacids:
            del amino_dict[letter]

    # deleting stop aminoacid
    del amino_dict['*']
    return dict(amino_dict)


# 12
def make_random_dna_strand(length_in: int) ->str:
    "Makes a random DNA strand"
    nucleotids = ["A", "C", "T", "G"]
    random.seed(5)
    return ''.join(random.choice(nucleotids) for i in range(length_in))


# 13
def get_first_substr(amino_seq_in: str)-> {}:
    "Returns the index of the first met, stop and the substring between them"
    met_indx = amino_seq_in.index('M')
    stop_indx = amino_seq_in.index('*', met_indx)
    substr = amino_seq_in[met_indx:stop_indx+1]
    return met_indx, stop_indx, substr


# 13 con regex
def get_first_substr_regex(amino_seq_in: str)-> {}:
    "Returns the index of the first met, stop and the substring between them"
    patt = r'^[M]'
    #result = re.match(patt, amino_seq_in)
    re.search("M", amino_seq_in).start()
    return dict(amino_seq_in)


# 13 con regex y devolviendo all matches
def get_first_substr_regex_2(amino_seq_in: str)-> {}:
    "Returns the index of the first met, stop and the substring between them"
    return dict(amino_seq_in)


# 14
def read_fasta(filename_in: str):
    "Reads a fasta file returns a string with the nucleotids"
    return filename_in
