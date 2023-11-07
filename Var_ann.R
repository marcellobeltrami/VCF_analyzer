#Installs variant annotation package if required. 
if (!require("BiocManager", quietly = TRUE))
 install.packages("BiocManager")

BiocManager::install("VariantAnnotation")

################################################################################
library(VariantAnnotation)

vcf <- readVcf("C:\\Users\\marce\\OneDrive\\Desktop\\VCF_analyzer\\test.vcf", "hg19")
vcf


