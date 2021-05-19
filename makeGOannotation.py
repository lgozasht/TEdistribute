
geneDic = {}
peroGenes = {}
with open('mgi.gaf','r') as f:
    for line in f:
        if '!' not in line:
            sp = line.split('\t')
            if sp[2] not in geneDic:
                geneDic[sp[2]] = [sp[4]]
            else:
                geneDic[sp[2]].append(sp[4])

with open(annotation,'r') as f:
    for line in f:
        if '#' not in line:
            sp = line.split('\t')
            if 'gene' in sp[2]:

                peroGenes[sp[-1].split(';')[1].split('=')[-1]] = ''

with open(geneToGo,'w') as f:
    for gene in geneDic:
        if gene in peroGenes:
            f.write('{0}\t{1}\n'.format(gene,';'.join(geneDic[gene]))) 
