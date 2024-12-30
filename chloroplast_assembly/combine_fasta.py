# -*- coding: UTF-8 -*-
import os
from Bio import SeqIO
file_path = "plastome_assemble_results/"#这里填写组装结果目录
plastid_fasta_list = []
ref_fasta = SeqIO.read("assembly_plastome/ref.fasta","fasta")#填写NCBI下载参考序列，要fasta格式！！！
plastid_fasta_list.append(ref_fasta)

for current,dirs,files in os.walk(file_path):
    for file in files:
        the_path = current+'/'+file
        if file == 'embplant_pt.K105.complete.graph1.1.path_sequence.fasta':
            indiv_name = the_path.split('/')[-2]
            fasta = SeqIO.read(the_path,"fasta")
            fasta.id = indiv_name+'.1'
            fasta.name = ""
            fasta.description = ""
            plastid_fasta_list.append(fasta)
        elif file == 'embplant_pt.K105.complete.graph1.2.path_sequence.fasta':
            indiv_name = the_path.split('/')[-2]
            fasta = SeqIO.read(the_path,"fasta")
            fasta.id = indiv_name+'.2'
            fasta.name = ""
            fasta.description = ""
            plastid_fasta_list.append(fasta)
        else:
            pass
SeqIO.write(plastid_fasta_list,"assembly_plastome/all.plastid.fasta","fasta")#填写输出的fasta结果文件