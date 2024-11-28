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

sequence_input = ">Secuencia ADN\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Secuencia input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
""")

## DNA nucleotide count
st.header('OUTPUT (DNA nucleotide composición)')

def DNA_nucleotide_count(seq):
    d = dict([ 
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

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

# In[ ]:
