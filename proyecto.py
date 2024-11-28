#!/usr/bin/env python
# coding: utf-8

# In[2]:

######################
# Import libraries
######################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

######################
# Page Title
######################

image = Image.open('imagen3.png')

# Actualización: Cambié use_column_width a use_container_width
st.image(image, use_container_width=True)
st.write("""
<style>
h1 {
    color: #09e043;
    font-size: 32px;
    text-align: center;
    margin-bottom: 20px;
}

h2 {
    color: #09e043;
    font-size: 24px;
    margin-bottom: 10px;
}

.subheader {
    color: #09e043;
    font-size: 18px;
    margin-bottom: 5px;
}

.output {
    margin-top: 30px;
}

table.dataframe {
    border-collapse: collapse;
    margin-top: 10px;
}

table.dataframe th, table.dataframe td {
    border: 1px solid #09e043;
    padding: 8px;
    text-align: left;
}

table.dataframe th {
    background-color: #09e043;
}

.chart {
    margin-top: 20px;
}

/* Cambiar color verde para títulos específicos */
h3#gráfico-barras, h3#gráfico-circular {
    color: #09e043;
}
</style>
""", unsafe_allow_html=True)

st.write("""
# Aplicación web de recuento de nucleótidos de ADN
Esta app es una forma rápida y sencilla de obtener un desglose de la composición nucleotídica de tu ADN.
Los resultados de esta app pueden utilizarse para diversos fines, como la investigación o la salud personal.
***
""")

######################
# Input Text Box
######################

#st.sidebar.header('Enter DNA sequence')
st.header('Introducir secuencia de ADN')

sequence2_input = ">Secuencia ADN\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence2_input, height=250)
sequence2 = st.text_area("Secuencia input", sequence2_input, height=250)
sequence2 = sequence2.splitlines()
sequence2 = sequence2[1:] # Skips the sequence name (first line)
sequence2 = ''.join(sequence2) # Concatenates list to string

st.write("""
***
""")

## DNA nucleotide count
st.header('OUTPUT (DNA nucleotide composición)')

def DNA_nucleotide_count(seq2):
    d = dict([ 
        ('A', seq2.count('A')),
        ('T', seq2.count('T')),
        ('G', seq2.count('G')),
        ('C', seq2.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence2)

# Des
st.subheader('Descripción de la cantidad de nucleotidos')
st.write('Existen ' + str(X['A']) + ' de adenina (A) en la secuencia')
st.write('Existen ' + str(X['T']) + ' de timina (T) en la secuencia')
st.write('Existen ' + str(X['G']) + ' de guanina (G) en la secuencia')
st.write('Existen ' + str(X['C']) + ' de citosina (C) en la secuencia')

# 3. Display DataFrame
st.subheader('3. Mostrar DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})

# Add CSS styling for subheaders
st.markdown(
    """
    <style>
    .stHeader > .deco-btn-container > div {
        display: inline-block;
        margin-right: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 4. Display Bar Chart using Altair
######################
st.subheader('4. Gráfico de barras', anchor="gráfico-barras")

# Mejorar el diseño del gráfico de barras
p = alt.Chart(df).mark_bar(color='#09e043').encode(  # Cambiar color a verde
    x=alt.X('nucleotide', title='Nucleótidos', sort=None),  # Ajustar título y sort
    y=alt.Y('count', title='Cantidad de nucleótidos'),  # Título eje Y
    tooltip=['nucleotide', 'count']  # Información del tooltip
).configure_axis(
    labelFontSize=16,  # Ajustar tamaño de la fuente de las etiquetas
    titleFontSize=18  # Ajustar tamaño de la fuente de los títulos
).properties(
    width=600,  # Aumentar ancho de las barras
    height=400  # Aumentar la altura del gráfico
).configure_mark(
    opacity=0.9  # Aumentar opacidad de las barras
)

st.write(p)

st.header('Contacto')
st.markdown('Integrantes: Andrei,Grecia,Paola')

# In[<Parte 2 GEY----------------------------------------------------------]:
st.title('WELCOME TO MY GENOMI APP')

#image = Image.open('chroma.jpg')
#st.image(image, use_column_width=True)

col1, col2 = st.beta_columns(2)

st.header('Enter Sequence')

sequence = st.text_area("", height=25)
sequence = sequence.upper()
nott = '\n'
sequence = sequence.replace(nott, '')
sequencer = ' '.join(sequence)

DNA = st.button('DNA')
RNA = st.button('RNA')

def dna_dna():
    replica = ''
    for nucleotide in sequence:
        if nucleotide == 'A':
            nucleotide = 'T '
        elif nucleotide == 'T':
            nucleotide = 'A '
        elif nucleotide == 'C':
            nucleotide = 'G '
        elif nucleotide == 'G':
            nucleotide = 'C '
        else:
            break
        replica+=nucleotide
    
    return replica

def transcription():
    transcript = ''
    for nucleotide in sequence:
        if nucleotide == 'A':
            nucleotide = 'U '
        elif nucleotide == 'T':
            nucleotide = 'A '
        elif nucleotide == 'C':
            nucleotide = 'G '
        elif nucleotide == 'G':
            nucleotide = 'C '
        else:
            break
        transcript+=nucleotide
    return transcript

def central():
    sequence2 = ''
    for nucleotide in sequence:
        if nucleotide == 'A':
            nucleotide = 'U'
        elif nucleotide == 'T':
            nucleotide = 'A'
        elif nucleotide == 'C':
            nucleotide = 'G'
        elif nucleotide == 'G':
            nucleotide = 'C'
        sequence2 += nucleotide

    RNA_sequence = []
    n = 0
    k = 1
    for seq in sequence2:
        RNA_sequence.append(sequence2[n]+sequence2[n+1]+sequence2[n+2])
        if len(sequence2)//3 > k:
            n += 3
            k += 1
        else:
            break

    amino_sequence = ''
    for codon in RNA_sequence:
        if codon == 'UUU' or codon == 'UUC':
            codon = 'Phe-'
        elif codon == 'UUA' or codon == 'UUG' or codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG':
            codon = 'Leu-'
        elif codon == 'AUU' or codon == 'AUC' or codon == 'AUA':
            codon = 'Ile-'
        elif codon == 'AUG':
            codon = 'Met-'
        elif codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or codon == 'GUG':
            codon = 'Val-'
        elif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG' or codon == 'AGU' or codon == 'AGC':
            codon = 'Ser-'
        elif codon == 'CCU' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
            codon = 'Pro-'
        elif codon == 'ACU' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
            codon = 'Thr-'
        elif codon == 'GCU' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
            codon = 'Ala-'
        elif codon == 'UAU' or codon == 'UAC':
            codon = 'Tyr-'
        elif codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
            codon = 'STOP'
            break
        elif codon == 'UAU' or codon == 'UAC':
            codon = 'Tyr-'
        elif codon == 'CAU' or codon == 'CAC':
            codon = 'His-'
        elif codon == 'CAA' or codon == 'CAG':
            codon = 'Gln-'
        elif codon == 'AAU' or codon == 'AAC':
            codon = 'Asn-'
        elif codon == 'AAA' or codon == 'AAG':
            codon = 'Lys-'
        elif codon == 'GAU' or codon == 'GAC':
            codon = 'Asp-'
        elif codon == 'GAA' or codon == 'GAG':
            codon = 'Glu-'
        elif codon == 'UGU' or codon == 'UGC':
            codon = 'Cys-'
        elif codon == 'UGG':
            codon = 'Trp-'
        elif codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
            codon = 'Arg-'
        elif codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
            codon = 'Gly-'
        amino_sequence+=codon
    return amino_sequence

aminoAcids = central()

def gc():
    gc = sequence.count('G') + sequence.count('C')
    total = len(sequence)
    content = ''
    try:
        content = str(int(gc/total*100))+'%'
    except ZeroDivisionError:
        pass
    return content

def total_count():
    duuh = str(len(sequence))
    return duuh

def percentaged():
    d = dict([
    ('A ', sequence.count('A')),
    ('G ', sequence.count('G')),
    ('C ', sequence.count('C')),
    ('T ', sequence.count('T'))
    ])
    return d

def percentager():
    r = dict([
    ('A ', sequence.count('A')),
    ('G ', sequence.count('G')),
    ('C ', sequence.count('C')),
    ('U ', sequence.count('U'))
    ])
    return r

def aminod(seq):
    acid = dict([
    ('Phe ', seq.count('Phe')),
    ('Leu ', seq.count('Leu')),
    ('Ile ', seq.count('Ile')),
    ('Met ', seq.count('Met')),
    ('Val ', seq.count('Val')),
    ('Ser ', seq.count('Ser')),
    ('Pro ', seq.count('Pro')),
    ('Thr ', seq.count('Thr')),
    ('Ala ', seq.count('Ala')),
    ('Tyr ', seq.count('Tyr')),
    ('His ', seq.count('HIs')),
    ('Gln ', seq.count('Gln')),
    ('Asn ', seq.count('Asn')),
    ('Lys ', seq.count('Lys')),
    ('Asp ', seq.count('Asp')),
    ('Glu ', seq.count('Glu')),
    ('Cys ', seq.count('Cys')),
    ('Trp ', seq.count('Trp')),
    ('Arg ', seq.count('Arg')),
    ('Gly ', seq.count('Gly'))
    ])
    return acid
number = aminod(aminoAcids)

def graphd():
    X = percentaged()
    X_label = list(X)
    X_values = list(X.values())

    df = pd.DataFrame.from_dict(X, orient='index')
    df = df.rename({0: 'count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns = {'index': 'nucleotide'})
    return df

def graphr():
    X = percentager()
    X_label = list(X)
    X_values = list(X.values())

    df = pd.DataFrame.from_dict(X, orient='index')
    df = df.rename({0: 'count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns = {'index': 'nucleotide'})
    return df

def chartd():
    X = percentaged()
    X_label = list(X)
    X_values = list(X.values())

    df = pd.DataFrame.from_dict(X, orient='index')
    df = df.rename({0: 'count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns = {'index': 'nucleotide'})
    

    p = alt.Chart(df).mark_bar().encode(
        x = 'nucleotide',
        y = 'count'
    )

    p = p.properties(
        width = alt.Step(80)
    )
    return p

def chartr():
    X = percentager()
    X_label = list(X)
    X_values = list(X.values())

    df = pd.DataFrame.from_dict(X, orient='index')
    df = df.rename({0: 'count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns = {'index': 'nucleotide'})
    

    p = alt.Chart(df).mark_bar().encode(
        x = 'nucleotide',
        y = 'count'
    )

    p = p.properties(
        width = alt.Step(80)
    )
    return p

def charta(num):
    X = num
    X_label = list(X)
    X_values = list(X.values())

    df = pd.DataFrame.from_dict(X, orient='index')
    df = df.rename({0: 'count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns = {'index': 'amino-acid'})
    

    p = alt.Chart(df).mark_bar().encode(
        x = 'amino-acid',
        y = 'count'
    )

    p = p.properties(
        width = alt.Step(20)
    )
    return p
chacha = charta(number)

def percentager():
    r = dict([
    ('A ', sequence.count('A')),
    ('G ', sequence.count('G')),
    ('C ', sequence.count('C')),
    ('U ', sequence.count('U'))
    ])
    return r

def translation():
    RNA_sequence = []
    n = 0
    k = 1
    for seq in sequence:
        RNA_sequence.append(sequence[n]+sequence[n+1]+sequence[n+2])
        if len(sequence)//3 > k:
            n += 3
            k += 1
        else:
            break

    amino_sequence = ''
    for codon in RNA_sequence:
        if codon == 'UUU' or codon == 'UUC':
            codon = 'Phe-'
        elif codon == 'UUA' or codon == 'UUG' or codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG':
            codon = 'Leu-'
        elif codon == 'AUU' or codon == 'AUC' or codon == 'AUA':
            codon = 'Ile-'
        elif codon == 'AUG':
            codon = 'Met-'
        elif codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or codon == 'GUG':
            codon = 'Val-'
        elif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG' or codon == 'AGU' or codon == 'AGC':
            codon = 'Ser-'
        elif codon == 'CCU' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
            codon = 'Pro-'
        elif codon == 'ACU' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
            codon = 'Thr-'
        elif codon == 'GCU' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
            codon = 'Ala-'
        elif codon == 'UAU' or codon == 'UAC':
            codon = 'Tyr-'
        elif codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
            codon = 'STOP'
            break
        elif codon == 'UAU' or codon == 'UAC':
            codon = 'Tyr-'
        elif codon == 'CAU' or codon == 'CAC':
            codon = 'His-'
        elif codon == 'CAA' or codon == 'CAG':
            codon = 'Gln-'
        elif codon == 'AAU' or codon == 'AAC':
            codon = 'Asn-'
        elif codon == 'AAA' or codon == 'AAG':
            codon = 'Lys-'
        elif codon == 'GAU' or codon == 'GAC':
            codon = 'Asp-'
        elif codon == 'GAA' or codon == 'GAG':
            codon = 'Glu-'
        elif codon == 'UGU' or codon == 'UGC':
            codon = 'Cys-'
        elif codon == 'UGG':
            codon = 'Trp-'
        elif codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
            codon = 'Arg-'
        elif codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
            codon = 'Gly-'
        amino_sequence+=codon
    return amino_sequence

aminoAcid = translation()
numbers = aminod(aminoAcid)
chachas = charta(numbers)

def rna_rna():
    replica = ''
    for nucleotide in sequence:
        if nucleotide == 'A':
            nucleotide = 'U '
        elif nucleotide == 'U':
            nucleotide = 'A '
        elif nucleotide == 'C':
            nucleotide = 'G '
        elif nucleotide == 'G':
            nucleotide = 'C '
        replica += nucleotide
    return replica

def rna_dna():
    reverse = ''
    for nucleotide in sequence:
        if nucleotide == 'A':
            nucleotide = 'T '
        elif nucleotide == 'U':
            nucleotide = 'A '
        elif nucleotide == 'C':
            nucleotide = 'G '
        elif nucleotide == 'G':
            nucleotide = 'C '
        reverse += nucleotide
    return reverse

replication = dna_dna()
transcription = transcription()
gc_content = gc()
total_count = total_count()
percentages1 = graphd()
percentages2 = chartd()
amino_chart = charta(number)

rnaReplication = rna_rna()
reverse_transcription = rna_dna()
translation = translation()
percentagesa = graphr()
percentagesb = chartr()

def valid():
    chance = 0
    for nucleotide in sequence:
        if nucleotide == 'A' or nucleotide == 'T' or nucleotide == 'G' or nucleotide == 'C':
            chance+=1
        elif nucleotide == ' ':
            nucleotide = ''
            chance+=1
        else:
            st.error('Invalid input in nucleotide number '+ str(sequence.index(nucleotide)+1))
            break
            chance-=1
    
    if len(sequence) == 0:
        st.warning("Hey don't just look there, Enter something")

    if chance == len(sequence) and chance > 0:
        st.success('Your DNA is fantastic')
        st.write('dna sequence   \n',  sequencer)
        st.write('dna replicon   \n', replication)
        st.write('dna transcript   \n ', transcription)
        st.write('AMINO ACIDS   \n', aminoAcids)
        st.write(percentages1)
        st.write(percentages2)
        st.write('The G-C content in the sequence is ', gc_content)
        st.write('The total number of nucleotides is ', total_count)
        st.write(chacha)

    
        
def valir():
    chance = 0
    for nucleotide in sequence:
        if nucleotide == 'A' or nucleotide == 'U' or nucleotide == 'G' or nucleotide == 'C':
            chance+=1
        elif nucleotide == ' ':
            nucleotide = ''
            chance+=1
        else:
            st.error('Invalid input in nucleotide number '+ str(sequence.index(nucleotide)+1))
            break
            chance-=1
    
    if len(sequence) == 0:
        st.warning("Hey don't just look there, Enter something")

    if chance == len(sequence) and chance > 0:
        st.success('Your RNA is fantastic')
        st.write('rna sequence   \n',  sequencer)
        st.write('rna replicon   \n', rnaReplication)
        st.write('reverse transript   \n', reverse_transcription)
        st.write('Amino acids   \n', translation)
        st.write(percentagesa)
        st.write(percentagesb)
        st.write('The G-C content in the sequence is ', gc_content)
        st.write('The total number of nucleotides is ', total_count)
        st.write(chachas)
        
if DNA:
    valid() 
if RNA:
    valir()
