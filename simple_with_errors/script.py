from Bio import SeqIO
from Bio.SeqUtils import GC

with open('genomeC.fna', 'rt') as handle:
    for rec in SeqIO.parse(handle, 'fasta'):
        gc_content = GC(rec.seq)

print(gc_content)