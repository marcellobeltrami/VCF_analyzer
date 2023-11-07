 # VCF_analyzer :dna:
This pipeline has been developed by: Marcello Beltrami, Reuben Kumar, Shiyi ....

A pipeline aiming at analyzing a VCF file to determine relevance of De Novo mutations. 
## Important 
This pipeline only requires to run main.py to execute installation and analysis. 
After first run, installation section in main.py should be commented by the user.

#### Input expected
A VCF file mapped using human_g1k_v37 human genome as a reference. In case, such fasta genome is provided in hg1_v37 folder. 

#### Results expected
Results will be stored in Results directory. 

**snpEff**
    >Trio.ann.vcf || Contains all annotations in VCF format

    >snpEff_summary.html || Summary output of snpEff in html format. 

    >Genes.txt || Is a tabix format table with relative annotatio scores for ease of read.

    For more info, here is the tool repo: 
    https://pcingola.github.io/SnpEff/snpeff/outputsummary/ 
    
**DVRSeq**
    >VCF_summary_out.html || HTML cointaining a summary of raw (unfiltered) vcf file. 
    The tool conducts further filtering, and allows visual comparison of VCF filtered and unfiltered


