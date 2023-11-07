#imports dependencies and main.py objects
import main
import sys
import subprocess


#2) Use annovar to annotate
subset_vcf =main.subset_trio
# Run VCF for ANNOVAR analysis 
perl_script = r"C:\Users\marce\OneDrive\Desktop\VCF_analyzer\annovar\table_annovar.pl"
arguments = ["-vcfinput {subset_vcf}", "humandb/", "-buildver hg19", "-out my_annotation", 
            "-remove", "-protocol refGene,cytoBand,exac03,avsnp147,dbnsfp30a", "-operation g,r,f,f,f", "-nastring ." ,"-vcfinput", "-polish" ]

# Create the command
command = ["perl", perl_script] + arguments
subprocess.run(command)


#3) Depending on output from 2, infer role of mutation programmatically or by hand.   