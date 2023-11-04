#imports dependencies and main.py objects
import main
import vcf


#1) Parse subset file for mutations and relevant information to be uploaded to database.  
#FILTER: Filter status. “PASS” is left empty in output.
def vcfparser(vcf_file):
    print("Parsing....")
    for record in vcf.Reader(vcf_file): 
        print(record)
        print(record.FILTER)
        

#Reads file_trio 
file_trio = open(main.subset_trio, "r") # Imports vcf from main
print(vcfparser(file_trio))

#2) Use VAPr to annotate (https://vapr.readthedocs.io/en/latest/Introduction.html)


#3) Depending on output from 2, infer role of mutation programmatically or by hand.   