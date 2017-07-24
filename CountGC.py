#!/usr/bin/python
import string
import sys

def Compute_GC (seq):
    GC = 0
    total =0
    for i in range(0, len(seq)):
        if string.upper(seq[i]) in ['A','T','G','C']:
            total = total +1
        if string.upper(seq[i]) in ['G', 'C']:
            GC = GC+1
    return float(GC)/total*100

if len(sys.argv) == 4:
    bedfile=sys.argv[1]
    fadir=sys.argv[2]
else:
    print("[usage] "+ sys.argv[0]+" bedfile fafiledir outputfile")
    print("Tips: fadir including fafile, named format: chr1.fa;chr2.fa...")
    print("      bedfile:Chr Start End Name(arbitrary)")
    print("Return: a list file: Chr Start End Name gcContent")
    sys.exit(-1)
outfile=open(sys.argv[3],'w+')
f = open(bedfile,'r')
TmpChr=""
for eachline in f:
   lst=eachline.strip().split(" ")
   Chr=lst[0]
   Start=int(lst[1])
   End=int(lst[2])
   Ampl=lst[3]
   if Chr != TmpChr:
       TmpChr=Chr
       faseq=""
       fafile=open(fadir+"/"+Chr+".fa",'r')
       fafile.readline()
       for fadt in fafile:
           faseq = faseq + fadt.strip()
   seq=faseq[Start-1:End]
   GC=Compute_GC(seq)
   outfile.write("%s\t%d\t%d\t%s\t%f\n" % (Chr,Start,End,Ampl,GC))
f.close()
fafile.close()
outfile.close()
