import collections
import random
import first_exercices as fe
import amino_dicts

# 1


def test_is_dna_strand():
    assert fe.is_dna_strand('ACTG') == True
    assert fe.is_dna_strand('A') == True
    assert fe.is_dna_strand('ACT') == True
    assert fe.is_dna_strand('ACTX') == False
    assert fe.is_dna_strand('XCTG') == False


# 2
def test_reverse_strand():
    assert fe.reverse_strand('ACTG') == 'GTCA'
    assert fe.reverse_strand('ACGTAGTCCGTA') == 'ATGCCTGATGCA'


# 3
def test_make_complementary_strand():
    assert fe.make_complementary_strand('acTg') == 'tgAc'


# 4
def test_make_reverse_complementary_strand():
    assert fe.make_reverse_complementary_strand('ACTG') == 'CAGT'


# 5
def test_is_dna_palindrome():
    assert fe.is_dna_palindrome('GAATTC') == True


# 6.a
def test_transcribe_from_coding_strand():
    assert fe.transcribe_from_coding_strand('ACATAGC') == 'ACAUAGC'


# 6.b
def test_transcribe_from_complementary_strand():
    assert fe.transcribe_from_complementary_strand(
        'TACAGA') == 'AUGUCU'


# 7
def test_get_pretty_codons():
    assert fe.get_pretty_codons('ACAGTCCCT') == 'ACA GTC CCT'


# 8.a
def test_translate_str():
    assert fe.translate_str('AUC') == 'I'
    assert fe.translate_str('GU') == '-'


# 8.b
def test_translate_arr():
    assert fe.translate_arr(['AUC', 'GUC', 'UUU']) == ['I', 'V', 'F']
    assert fe.translate_arr(['AGUU', 'GUU', 'G']) == ['-', 'V', '-']


# 9
def test_get_actg_stats():
    assert fe.get_actg_stats('ACTGGC') == {
        'a': 1, 'c': 2, 't': 1, 'g': 2}


# 10
def test_get_codon_dict():
    dict_in = {'AGA': 'Arg',
               'AGG': 'Arg'}
    assert fe.get_codon_dict(dict_in) == {'Arg': ['AGA', 'AGG']}


# 11
def test_get_amino_stats():
    assert fe.get_amino_stats(
        "AMAZING IS THE TRUK") == {'A': 2, 'M': 1, 'I': 2, 'N': 1, 'G': 1, 'S': 1, 'T': 2, 'H': 1, 'E': 1, 'R': 1, 'K': 1, 'D': 0, 'L': 0, 'W': 0, 'Q': 0, 'C': 0, 'F': 0, 'V': 0, 'P': 0, 'Y': 0}


# 12
def test_make_random_dna_strand():
    random.seed(5)
    assert fe.make_random_dna_strand(5) == "TTAGC"


# 13 a mi me gusta con el stop, ok?
def test_get_first_substr():
    assert fe.get_first_substr("KLZMHOSMTIA*") == (3, 11, "MHOSMTIA*")


# 13.a regex
def test_get_first_substr_regex():
    assert fe.get_first_substr_regex(
        "KLZMHOSMTIA*") == (3, 11, "MHOSMTIA")


# 13.b all matches
def test_get_first_substr_regex_matches():
    assert fe.get_first_substr_regex_match(
        'MA*MA*MA*') == [(0, 2, 'MA'), (3, 5, 'MA'), (6, 8, 'MA')]
