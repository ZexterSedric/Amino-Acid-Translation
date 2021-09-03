codondict={'UUU':'Phe','UUC':'Phe','UUA':'Leu','UUG':'Leu','UCU':'Ser','UCC':'Ser','UCA':'Ser','UCG':'Ser','UAU':'Tyr','UAC':'Tyr','UAA':'Stop','UAG':'Stop','UGU':'Cys','UGC':'Cys','UGA':'Stop','UGG':'Trp','CUU':'Leu','CUC':'Leu','CUA':'Leu','CUG':'Leu','CCU':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro','CAU':'His','CAC':'His','CAA':'Gin','CAG':'Gin','CGU':'Arg','CGC':'Arg','CGA':'Arg','CGG':'Arg','AUU':'Ile','AUC':'Ile','AUA':'Ile','AUG':'Met','ACU':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr','AAU':'Asn','AAC':'Asn','AAA':'Lys','AAG':'Lys','AGU':'Ser','AGC':'Ser','AGA':'Arg','AGG':'Arg','GUU':'Val','GUC':'Val','GUA':'Val','GUG':'Val','GCU':'Ala','GCC':'Ala','GCA':'Ala','GCG':'Ala','GAU':'Asp','GAC':'Asp','GAA':'Glu','GAG':'Glu','GGU':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly'}
RNA=input('Enter desired RNA string:\n')
RNA=RNA.upper()
if len(RNA)%3==0:
    f=int(len(RNA)/3)
    for i in range(0,f):
        codon=RNA[3*i:3*(i+1)]
        print(codondict[codon],end=' ')
else:
    print('The RNA string cannot be fully translated due to lack of final codon triplets')
print()
proteindict={'Phe':'Phenylalanine','Leu':'Leucine','Ser':'Serine','Tyr':'Tyrosine','Stop':'\'Termination of translation\'','Cys':'Cysteine','Trp':'Tryptophan','Pro':'Proline','His':'Histidine','Gln':'Glutamine','Arg':'Arginine','Asn':'Asparagine','Ile':'Isoleucine','Met':'Methionine','Thr':'Threonine','Lys':'Lysine','Val':'Valine','Ala':'Alanine','Asp':'Aspartic Acid','Glu':'Glutamic Acid','Gly':'Glycine'}
if0=input('Additional information about the output ?? y or n\n')
if if0=='y':
    print('These mean that the following proteins are synthesised:')
    f=int(len(RNA)/3)
    for i in range(0,f):
        codon=RNA[3*i:3*(i+1)]
        print(proteindict[codondict[codon]],end=', ')
else:
    print('Translation Process Terminated')
