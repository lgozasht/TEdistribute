
import glob

id = 0
famDic = {}
typeDic = {}

for file in glob.glob('*.elem_sorted.csv'):

    with open(file,'r') as f:
        next(f)
        for line in f:
            if len(line) > 3 and '###' in line:
                sp = line.split('\t')
                id += 1
                start = sp[5]
                stop = sp[6]
                chrm = sp[4]
                fam = sp[9]
                type = sp[10]
                if chrm not in famDic:
                    famDic[chrm] = {}

                if fam not in famDic[chrm]:

                    famDic[chrm][fam] = [int(start)]                 
                else:
                    famDic[chrm][fam].append(int(start))

                if chrm not in typeDic:
                    typeDic[chrm] = {}
                if type not in typeDic[chrm]:

                    typeDic[chrm][type] = [int(start)]
                else:
       	       	    typeDic[chrm][type].append(int(start))


peroGenes = {}

with open('/n/holylfs03/LABS/hoekstra_lab/Lab/PUBLIC/ANNOTATIONS/Pman2.1_chr_NCBI/Pman2.1_chr_NCBI.corrected.merged-with-Apollo.Aug19.sorted.gff3','r') as f:
    for line in f:
        if '#' not in line:
            sp = line.split('\t')
            if 'gene' in sp[2]:
                
                if int(sp[4]) > int(sp[3]):
                    if sp[0] not in peroGenes:
                        peroGenes[sp[0]] = [[sp[-1].split(';')[1].split('=')[-1],int(sp[3]),int(sp[4])]]   
                    else:
                        peroGenes[sp[0]].append([sp[-1].split(';')[1].split('=')[-1],int(sp[3]),int(sp[4])])
                else:
                    if sp[0] not in peroGenes:
                        peroGenes[sp[0]] = [[sp[-1].split(';')[1].split('=')[-1],int(sp[4]),int(sp[3])]]
                    else:
                        peroGenes[sp[0]].append([sp[-1].split(';')[1].split('=')[-1],int(sp[4]),int(sp[3])])

with open('population.txt','w') as f:
    for chrm in peroGenes:
        for gene in peroGenes[chrm]:
            f.write(gene[0])

output = 'TEGenicInsertions'

print(famDic)

for chrm in peroGenes:
    for gene in peroGenes[chrm]:
        for fam in famDic[chrm]:
            for i in famDic[chrm][fam]:
                if gene[1] < i and i < gene[2]:
                    with open('{0}/allTEGenicInsertions.txt'.format(output),'a') as f:
                        f.write(gene[0])
                    with open('{0}/fam/{1}_GenicInsertions.txt'.format(output,fam.replace('/','_')),'a') as f:
       	       	        f.write(gene[0])
                
        for type in typeDic[chrm]:
            for i in typeDic[chrm][type]:

                if gene[1] < i and i < gene[2]:
                    with open('{0}/type/{1}_GenicInsertions.txt'.format(output,type.replace('/','_')),'a') as f:
                        f.write(gene[0])

