from pathlib import Path

# Path to project and file
path_to_project = Path(".")
project_dir = path_to_project 
fname = project_dir / "seq.txt"
out = project_dir / "aa.txt"

# transcription function turns a single nucleotide (A, C, G, T) of DNA
# into a single nucleotide (U, G, C, A) of RNA
def transcribe(d):
    transcription = {
        "A": "U",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    return transcription[d]

    
# translation function turns a single codon (a 3-letter sequence of RNA)
# into a single amino acid (one of 20 building blocks)
def translate(codon):
    aa = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
        "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }
    return aa[codon]

# DNA to RNA function turns an entire strand of DNA into an entire strand of RNA
# using the transcription function
def dna_to_rna(dna):
    rna = ""
    for nucleotide in dna:
        rna += transcribe(nucleotide)
    return rna

# RNA to AA function turns an entire strand of RNA into an entire protein (amino acid seq)
# using the translation function
def rna_to_aa(rna):
    aa = ""
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        aa += translate(codon)
    return aa

# Load file contents 
with open(fname) as f:
    dna = f.read().strip().upper()

# Turn DNA to RNA to Amino Acids
rna = dna_to_rna(dna)
aa = rna_to_aa(rna)

# Write the string 'aa' to a file called 'aa.txt'. 

##### INSERT CODE #####
amino=open('aa.txt','w')
read= amino.write(aa)
amino.close()