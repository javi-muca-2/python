# Url:
# https://www.khanacademy.org/science/biology/gene-expression-central-dogma/central-dogma-transcription/a/the-genetic-code-discovery-and-properties


full_name = {
  'UCA': 'Serine',
  'UCC': 'Serine',
  'UCG': 'Serine',
  'UCU': 'Serine',
  'UUC': 'Phenylalanine',
  'UUU': 'Phenylalanine',
  'UUA': 'Leucine',
  'UUG': 'Leucine',
  'UAC': 'Tyrosine',
  'UAU': 'Tyrosine',
  'UAA': 'Stop',
  'UAG': 'Stop',
  'UGC': 'Cysteine',
  'UGU': 'Cysteine',
  'UGA': 'Stop',
  'UGG': 'Tryptophan',
  'CUA': 'Leucine',
  'CUC': 'Leucine',
  'CUG': 'Leucine',
  'CUU': 'Leucine',
  'CCA': 'Proline',
  'CAU': 'Histidine',
  'CAA': 'Glutamine',
  'CAG': 'Glutamine',
  'CGA': 'Arginine',
  'CGC': 'Arginine',
  'CGG': 'Arginine',
  'CGU': 'Arginine',
  'AUA': 'Isoleucine',
  'AUC': 'Isoleucine',
  'AUU': 'Isoleucine',
  'AUG': 'Methionine',
  'ACA': 'Threonine',
  'ACC': 'Threonine',
  'ACG': 'Threonine',
  'ACU': 'Threonine',
  'AAC': 'Asparagine',
  'AAU': 'Asparagine',
  'AAA': 'Lysine',
  'AAG': 'Lysine',
  'AGC': 'Serine',
  'AGU': 'Serine',
  'AGA': 'Arginine',
  'AGG': 'Arginine',
  'CCC': 'Proline',
  'CCG': 'Proline',
  'CCU': 'Proline',
  'CAC': 'Histidine',
  'GUA': 'Valine',
  'GUC': 'Valine',
  'GUG': 'Valine',
  'GUU': 'Valine',
  'GCA': 'Alanine',
  'GCC': 'Alanine',
  'GCG': 'Alanine',
  'GCU': 'Alanine',
  'GAC': 'Aspartic Acid',
  'GAU': 'Aspartic Acid',
  'GAA': 'Glutamic Acid',
  'GAG': 'Glutamic Acid',
  'GGA': 'Glycine',
  'GGC': 'Glycine',
  'GGG': 'Glycine',
  'GGU': 'Glycine',
}


three_letters = {
  'UCA': 'Ser', # Serine
  'UCC': 'Ser', # Serine
  'UCG': 'Ser', # Serine
  'UCU': 'Ser', # Serine
  'UUC': 'Phe', # Phenylalanine
  'UUU': 'Phe', # Phenylalanine
  'UUA': 'Leu', # Leucine
  'UUG': 'Leu', # Leucine
  'UAC': 'Tyr', # Tyrosine
  'UAU': 'Tyr', # Tyrosine
  'UAA': '***', # Stop
  'UAG': '***', # Stop
  'UGC': 'Cys', # Cysteine
  'UGU': 'Cys', # Cysteine
  'UGA': '***', # Stop
  'UGG': 'Trp', # Tryptophan
  'CUA': 'Leu', # Leucine
  'CUC': 'Leu', # Leucine
  'CUG': 'Leu', # Leucine
  'CUU': 'Leu', # Leucine
  'CCA': 'Pro', # Proline
  'CAU': 'His', # Histidine
  'CAA': 'Gln', # Glutamine
  'CAG': 'Gln', # Glutamine
  'CGA': 'Arg', # Arginine
  'CGC': 'Arg', # Arginine
  'CGG': 'Arg', # Arginine
  'CGU': 'Arg', # Arginine
  'AUA': 'Ile', # Isoleucine
  'AUC': 'Ile', # Isoleucine
  'AUU': 'Ile', # Isoleucine
  'AUG': 'Met', # Methionine, Start
  'ACA': 'Thr', # Threonine
  'ACC': 'Thr', # Threonine
  'ACG': 'Thr', # Threonine
  'ACU': 'Thr', # Threonine
  'AAC': 'Asn', # Asparagine
  'AAU': 'Asn', # Asparagine
  'AAA': 'Lys', # Lysine
  'AAG': 'Lys', # Lysine
  'AGC': 'Ser', # Serine
  'AGU': 'Ser', # Serine
  'AGA': 'Arg', # Arginine
  'AGG': 'Arg', # Arginine
  'CCC': 'Pro', # Proline
  'CCG': 'Pro', # Proline
  'CCU': 'Pro', # Proline
  'CAC': 'His', # Histidine
  'GUA': 'Val', # Valine
  'GUC': 'Val', # Valine
  'GUG': 'Val', # Valine
  'GUU': 'Val', # Valine
  'GCA': 'Ala', # Alanine
  'GCC': 'Ala', # Alanine
  'GCG': 'Ala', # Alanine
  'GCU': 'Ala', # Alanine
  'GAC': 'Asp', # Aspartic Acid
  'GAU': 'Asp', # Aspartic Acid
  'GAA': 'Glu', # Glutamic Acid
  'GAG': 'Glu', # Glutamic Acid
  'GGA': 'Gly', # Glycine
  'GGC': 'Gly', # Glycine
  'GGG': 'Gly', # Glycine
  'GGU': 'Gly', # Glycine
}


single_letter = {
  'UCA': 'S', # Serine
  'UCC': 'S', # Serine
  'UCG': 'S', # Serine
  'UCU': 'S', # Serine
  'UUC': 'F', # Phenylalanine
  'UUU': 'F', # Phenylalanine
  'UUA': 'L', # Leucine
  'UUG': 'L', # Leucine
  'UAC': 'Y', # Tyrosine
  'UAU': 'Y', # Tyrosine
  'UAA': '*', # Stop
  'UAG': '*', # Stop
  'UGC': 'C', # Cysteine
  'UGU': 'C', # Cysteine
  'UGA': '*', # Stop
  'UGG': 'W', # Tryptophan
  'CUA': 'L', # Leucine
  'CUC': 'L', # Leucine
  'CUG': 'L', # Leucine
  'CUU': 'L', # Leucine
  'CCA': 'P', # Proline
  'CAU': 'H', # Histidine
  'CAA': 'Q', # Glutamine
  'CAG': 'Q', # Glutamine
  'CGA': 'R', # Arginine
  'CGC': 'R', # Arginine
  'CGG': 'R', # Arginine
  'CGU': 'R', # Arginine
  'AUA': 'I', # Isoleucine
  'AUC': 'I', # Isoleucine
  'AUU': 'I', # Isoleucine
  'AUG': 'M', # Methionine, Start
  'ACA': 'T', # Threonine
  'ACC': 'T', # Threonine
  'ACG': 'T', # Threonine
  'ACU': 'T', # Threonine
  'AAC': 'N', # Asparagine
  'AAU': 'N', # Asparagine
  'AAA': 'K', # Lysine
  'AAG': 'K', # Lysine
  'AGC': 'S', # Serine
  'AGU': 'S', # Serine
  'AGA': 'R', # Arginine
  'AGG': 'R', # Arginine
  'CCC': 'P', # Proline
  'CCG': 'P', # Proline
  'CCU': 'P', # Proline
  'CAC': 'H', # Histidine
  'GUA': 'V', # Valine
  'GUC': 'V', # Valine
  'GUG': 'V', # Valine
  'GUU': 'V', # Valine
  'GCA': 'A', # Alanine
  'GCC': 'A', # Alanine
  'GCG': 'A', # Alanine
  'GCU': 'A', # Alanine
  'GAC': 'D', # Aspartic Acid
  'GAU': 'D', # Aspartic Acid
  'GAA': 'E', # Glutamic Acid
  'GAG': 'E', # Glutamic Acid
  'GGA': 'G', # Glycine
  'GGC': 'G', # Glycine
  'GGG': 'G', # Glycine
  'GGU': 'G', # Glycine
}

