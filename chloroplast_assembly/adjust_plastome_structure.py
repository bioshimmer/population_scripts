import os
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
inputfile = "/work/test/plastome/output/JM2023072401_2A2_1.adjust.fa"
outfile = "/work/test/plastome/output/JM2023072401_2A2_1.adjust2.fa"
out_seq_id = "JM2023072401_2A2_1.adjust2"
seq_list = [x for x in SeqIO.parse(inputfile,"fasta")]
if len(seq_list) == 1:
    goal_seq = seq_list[0]
else:
    goal_seq1 = seq_list[0]
    goal_seq2 = seq_list[1]
    print(goal_seq1.id)
    print(goal_seq2.id)
    print(f"sequence more than one.")
"""
a = goal_seq1.seq[0:106729]
b = goal_seq1.seq[106729::]
c = goal_seq1.seq[0:24905]
d = goal_seq2.seq[0:13]
e = goal_seq2.seq[13:17280]
f = goal_seq2.seq[17280::]
adjust_seq = a[::-1]+b+d+e+f+c
"""

a = goal_seq.seq[0:193]
b = goal_seq.seq[193:149380]
c = goal_seq.seq[156658:156888]

adjust_seq = a+b+c

total_plastome_genome = SeqRecord(seq=adjust_seq,id =out_seq_id,name ="",annotations=None,description="")
SeqIO.write(total_plastome_genome,outfile,"fasta")