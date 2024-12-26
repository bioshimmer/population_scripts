# -*- coding: UTF-8 -*-
import os
def get_fq_path(file_path):
    for i in os.listdir(file_path):
        if '_1.clean.fq.gz' in i:
            fq1 = file_path+i
        elif '_2.clean.fq.gz' in i:
            fq2 = file_path+i
        else:
            pass
            #print("path parse error!")
    if fq1 and fq2:
        return fq1,fq2
    else:
        print(file_path+" parse error!")
        return 0,0
def main() :
    raws_path_file:str = "/work/test/plastome_adjust/raws_path"
    goal_path:str = "/work/test/plastome_adjust/plastome_assemble_results/"
    cmdtxt:str = "/work/test/plastome_adjust/plastome_assembly.sh"
    time_path = "/home/test/software/time/1.9/bin/time"
    cpu_num:int = 10
    file_list:list = []
    cmd_list:list = []
    with open(raws_path_file,"r") as f:
        for line in f.readlines():
            file_list.append(line.rstrip())
    #print(file_list)
    for i in file_list:
        indiv_name = i.split('/')[-2]
        timefile = f'{goal_path}00time_log/{indiv_name}.plast_assembly.time'
        outpath = f'{goal_path}{indiv_name}/'#如果文件夹不存在，get_organellele会自己创建
        log_file = f'{goal_path}00time_log/{indiv_name}.plast_assembly.log'
        error_file = f'{goal_path}00time_log/{indiv_name}.plast_assembly.err'
        fq1,fq2 = get_fq_path(i)
        if fq1==0 and fq2 == 0:
            print('parse error!')
            exit(1)
        #cmdline = f"{time_path} -vo {timefile} get_organelle_from_reads.py -1 {fq1} -2 {fq2} -o {outpath} -t {cpu_num} -R 15 -k 21,45,65,85,105 -F embplant_pt 1> {log_file} 2> {error_file}"
        #对于没有成环的个体，调整参数重新跑，改成-R 30 -w 95
        cmdline = f"{time_path} -vo {timefile} get_organelle_from_reads.py -1 {fq1} -2 {fq2} -o {outpath} -t {cpu_num} -R 30 -k 21,45,65,85,105 --overwrite -F embplant_pt 1> {log_file} 2> {error_file}"        
        cmd_list.append(cmdline)
    with open(cmdtxt,"w") as f:
        for i in cmd_list:
            f.write(i+'\n')
if __name__ == '__main__':
    main()
    exit(0)