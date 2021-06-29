import glob
import os

PmanPath = '/n/holyscratch01/hoekstra_lab/landen/mobile_elements/Onecodetofindthemall_output/TEGenicInsertions/type/'
mergeFile = '/n/holyscratch01/hoekstra_lab/landen/mobile_elements/merged_geneToGO.tsv'
outPath = '/n/holyscratch01/hoekstra_lab/landen/mobile_elements/compare/type/'

outPathReverse = '/n/holyscratch01/hoekstra_lab/landen/mobile_elements/compare_reverse/type/'
PpolPath = '/n/holyscratch01/hoekstra_lab/landen/mobile_elements/Ppol/TEGenicInsertions/type/' 


'''
for i in glob.glob('/n/holyscratch01/hoekstra_lab/landen/mobile_elements/Ppol/TEGenicInsertions/type/*_GenicInsertions.txt'):
    file = i.split('/')[-1]
    os.system('python scripts/find_enrichment.py {0}{1} {2} {3} --method fdr --pval=0.05 --compare --outfile {4}{5}'.format(PmanPath,file,i,mergeFile,outPath,file.replace('.txt','.out')))

'''

for i in glob.glob('/n/holyscratch01/hoekstra_lab/landen/mobile_elements/Onecodetofindthemall_output/TEGenicInsertions/type/*_GenicInsertions.txt'):
    file = i.split('/')[-1]
    os.system('python scripts/find_enrichment.py {0}{1} {2} {3} --method fdr --pval=0.05 --compare --outfile {4}{5}'.format(PpolPath,file,i,mergeFile,outPathReverse,file.replace('.txt','.out')))

