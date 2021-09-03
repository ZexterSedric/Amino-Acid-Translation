codondict={'TTT':'Phe','TTC':'Phe','TTA':'Leu','TTG':'Leu','TCT':'Ser','TCC':'Ser','TCA':'Ser','TCG':'Ser','TAT':'Tyr','TAC':'Tyr','TAA':'Stop','TAG':'Stop','TGT':'Cys','TGC':'Cys','TGA':'Stop','TGG':'Trp','CTT':'Leu','CTC':'Leu','CTA':'Leu','CTG':'Leu','CCT':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro','CAT':'His','CAC':'His','CAA':'Gln','CAG':'Gln','CGT':'Arg','CGC':'Arg','CGA':'Arg','CGG':'Arg','ATT':'Ile','ATC':'Ile','ATA':'Ile','ATG':'Met','ACT':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr','AAT':'Asn','AAC':'Asn','AAA':'Lys','AAG':'Lys','AGT':'Ser','AGC':'Ser','AGA':'Arg','AGG':'Arg','GTT':'Val','GTC':'Val','GTA':'Val','GTG':'Val','GCT':'Ala','GCC':'Ala','GCA':'Ala','GCG':'Ala','GAT':'Asp','GAC':'Asp','GAA':'Glu','GAG':'Glu','GGT':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly'}
RNA=input('Enter desired RNA string:\n')
RNA=RNA.upper()
if len(RNA)%3==0:
    f=int(len(RNA)/3)
    for i in range(0,f):
        codon=RNA[3*i:3*(i+1)]
        print(codondict[codon],end=' ')
else:
    print('The RNA string cannot be fTlly translated dTe to lack of final codon triplets')
print()
proteindict={'Phe':'Phenylalanine','Leu':'Leucine','Ser':'Serine','Tyr':'Tyrosine','Stop':'\'Termination of translation\'','Cys':'Cysteine','Trp':'Tryptophan','Pro':'Proline','His':'Histidine','Gln':'Glutamine','Arg':'Arginine','Asn':'Asparagine','Ile':'Isoleucine','Met':'Methionine','Thr':'Threonine','Lys':'Lysine','Val':'Valine','Ala':'Alanine','Asp':'Aspartic Acid','Glu':'Glutamic Acid','Gly':'Glycine','Gln':'Glutamine'}
if0=input('Hey noob, Wanna know what these mean ?? y or n\n')
if if0=='y':
    print('These mean that the following proteins are synthesised:')
    f=int(len(RNA)/3)
    for i in range(0,f):
        codon=RNA[3*i:3*(i+1)]
        print(proteindict[codondict[codon]],end=', ')
else:
    print('OK piro')