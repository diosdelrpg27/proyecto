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

st.subheader('¿Qué son los nucleótidos?')
st.write('Los nucleótidos son las unidades básicas que componen el ADN. Su composición y organización son fundamentales para entender diversas funciones biológicas.')
st.write('Sus componentes son:')
st.write('Grupo fosfato: Une nucleótidos para formar la estructura de la cadena de ADN.')
st.write('Azúcar desoxirribosa: Una molécula de azúcar de cinco carbonos que da al ADN su nombre.')
st.write('Base nitrogenada: Define el tipo de nucleótido y codifica la información genética.')

image2 = Image.open('imagen4.jpeg')
st.image(image2, use_container_width=True)

st.subheader('Las bases se componen de:')
st.write('Adenina (A)')
st.write('Timina (T)')
st.write('Guanina (G)')
st.write('Citosina (C)')

image3 = Image.open('imagen5.png')
st.image(image3, use_container_width=True)

st.subheader('Composición del ADN')
st.write('Doble hélice: El ADN es una doble cadena en la que las bases están apareadas:')
st.write('Adenina (A) se une con Timina (T) mediante dos enlaces de hidrógeno.')
st.write('Guanina (G) se une con Citosina (C) mediante tres enlaces de hidrógeno.')
st.write("""Polaridad: Las cadenas tienen una dirección (5' a 3' y 3' a 5'), lo que es crucial para la replicación y transcripción.""")

image4 = Image.open('imagen6.jpeg')
st.image(image4, use_container_width=True)

st.subheader('Funciones:')
st.write('Almacén de información genética: Los nucleótidos codifican genes que dirigen la síntesis de proteínas.')
st.write('Regulación de procesos celulares: Secuencias específicas regulan la expresión génica.')
st.write('Replicación: La complementariedad de bases permite copiar la información genética de manera precisa.')

image5 = Image.open('imagen7.mpeg')
st.image(image5, use_container_width=True)

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
st.subheader('Gráfico de barras', anchor="gráfico-barras")

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

