# TEdistribute

TEdistribute is a tool for gene ontology enrichment analyses on transposable element (TE) insertions within and between assembled genomes. It requires a standard output table from RepeatMasker (see https://www.repeatmasker.org/) and corresponding genomic fasta and annotation files as input. It then defragments TEs and  performs ontology enrichment tests for insertions within and/or surrounding user defined regions of genes. Enrichment tests can be independently performed on TE families or specific elements. Tests can be performed either within a genome or, more powerfully, comparatively between genomes of different species to identify potential relationships between specific TE families or general TE distributions and regulation of specific gene networks or processes.

### Dependencies 

"One code to find them all"
http://doua.prabi.fr/software/one-code-to-find-them-all
https://mobilednajournal.biomedcentral.com/articles/10.1186/1759-8753-5-13

GOATOOLS
https://github.com/tanghaibao/goatools
https://www.nature.com/articles/s41598-018-28948-z

### Installation

You can run the install script which contains the following or download each requirement on your own.

```

#Download "One code to find them all"
wget http://doua.prabi.fr/software/onecodetofindthemall_data/Onecodetofindthemall.zip
unzip Onecodetofindthemall.zip

#Download goatools and install dependencies
git clone https://github.com/tanghaibao/goatools.git
pip install --user goatools
pip install --user statsmodels


```

### Workflow

```
perl ./tools/Onecodetofindthemall/build_dictionary.pl --unknown --rm repeat_masker.out.filtered > ltr_dic.out
```

```
perl tools/Onecodetofindthemall/one_code_to_find_them_all.pl --strict --unknown --rm repeat_masker.out.filtered  --ltr ltr_dic.ou --fasta assembly.fasta
```

```
makeGOannotation.py
```

```
associateTEs.py
```

-two tailed association when on two species, then parse output

-integrate GREAT https://www.nature.com/articles/nbt.1630

### Reference
in progress
