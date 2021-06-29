import glob
import os

PmanPath = '/n/holyscratch01/hoekstra_lab/landen/mobile_elements/Onecodetofindthemall_output/TEGenicInsertions/fam/'
mergeFile = '/n/holyscratch01/hoekstra_lab/landen/mobile_elements/merged_geneToGO.tsv'
outPath = '/n/holyscratch01/hoekstra_lab/landen/mobile_elements/compare/fam/'

outPathReverse = '/n/holyscratch01/hoekstra_lab/landen/mobile_elements/compare_reverse/fam/'
PpolPath = '/n/holyscratch01/hoekstra_lab/landen/mobile_elements/Ppol/TEGenicInsertions/fam/' 




insDic = {}
geneDic = {}
for i in glob.glob('{0}/*.txt'.format(PmanPath)):
    file = i.split('/')[-1]
    element = file.replace('.txt','')
    with open(i,'r') as f: 
        for line in f:
            line = line.strip()
            if element not in insDic:
                insDic[element] = 0
            insDic[element] += 1

            if line not in geneDic:
                geneDic[line] = 0
            geneDic[line] += 1



for i in glob.glob('{0}/*.txt'.format(PpolPath)):
    file = i.split('/')[-1]
    element = file.replace('.txt','')
    with open(i,'r') as f: 
       	for line in f:
       	    line = line.strip()
            if element not in insDic:
                insDic[element] = 0
            insDic[element] -= 1

            if line not in geneDic:
                geneDic[line] = 0
            geneDic[line] -= 1

geneList,countList = (list(i) for i in zip(*sorted(zip(list(insDic.values()), list(insDic.keys())),reverse=True)))
for i in range(len(geneList)):
    print(geneList[i],countList[i])


geneList,countList = (list(i) for i in zip(*sorted(zip(list(geneDic.values()), list(geneDic.keys())),reverse=True)))
for i in range(len(geneList)):
    print(geneList[i],countList[i])

'''
elementList = []
sigList = []
geneCounts = {}
newFam = False

for i in glob.glob('{0}/*.out'.format(outPathReverse)):
    file = i.split('/')[-1]
    element = file.replace('.out','')
    newFam = True
    with open(i,'r') as f:
        next(f)
        for line in f:
            sp = line.strip().split('\t')
            try:
                if float(sp[6]) < 0.05 and float(sp[9]) < 0.05 and sp[2] == 'e':
                    elementList.append(element)
                    sigList.append(line.strip())
                    for gene in sp[10].split(' '):
                        if gene.strip(',') not in geneCounts:
                            geneCounts[gene.strip(',')] = 1
                        elif newFam == True:
                            geneCounts[gene.strip(',')] += 1
                    newFam = False

            except IndexError:
                pass


geneList,countList = (list(i) for i in zip(*sorted(zip(list(geneCounts.values()), list(geneCounts.keys())),reverse=True))) 
for i in range(len(geneList)):
    print(geneList[i],countList[i])

with open('expansions_fam_Ppol.tsv','w') as f:
    for i in range(len(sigList)):
        f.write('{0}\t{1}\n'.format(elementList[i],sigList[i]))


'''
