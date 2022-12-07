from PIL import Image
import streamlit as st

image = Image.open('Aquarius.jpg')

st.image(image, width = 400)
st.title('Aquarius informativo ')
st.header('Bem vindo, tudo bem?')
st.subheader('Caro piscicultor, chegamos para facilitar sua vida')
st.subheader('Vamos começar!')


st.markdown('Com o Aquarius você irá analisar os parâmetros físicos-químicos dos seus viveiros ou tanques e anotar tudo na nossa tela inicial,' 
        'por fim nosso banco de dados lhe dará um resultado final se a qualidade de água está propícia ou não para criação dos seus peixes.'
        'Por enquanto iremos começar apenas com algumas espécies(Tambaqui, Tilápia e Pirarucu).')

st.subheader('PARAMETROS FÍSICO-QUÍMICOS ADEQUADO DA ÁGUA PARA CULTIVO DE TILÁPIAS')
st.markdown('Temperatura:  Entre 27°C a 32ºC')
st.markdown('pH:  6,5 a 9')
st.markdown('Oxigênio dissolvido:  0,7 a 1,6 mg.L -1')
st.markdown('Alcalinidade: Maior ou igual 30 mg/L a menor ou igual a 300 mg/L.')
st.markdown('Turbidez: Em torno de 15 a 40 cm.')
st.markdown('Amônia : Abaixo de 0,24 mg/L')
st.markdown('Nitrito:Menor ou igual a 0,5 mg L-1.')
st.markdown('Nitrato: Menor ou igual a 5,0 mg L-1')

st.subheader('PARAMETROS FÍSICO-QUÍMICOS ADEQUADO DA ÁGUA PARA CULTIVO DE TAMBAQUI')
st.markdown('Temperatura:  Entre 25oC a 32ºC')
st.markdown('pH:  6,5 a 8,5')
st.markdown('Oxigênio dissolvido:  acima de 4 mg L-1')
st.markdown('Alcalinidade: maior ou igual 20 mg/L a menor ou igual a 300 mg/L')
st.markdown('Turbidez:  em torno de 15 a 40 cm')
st.markdown('Amônia :abaixo de  2,0 mg L-1')
st.markdown('Nitrito:Menor ou igual a 0,5 mg L-1.')
st.markdown('Nitrato: Menor ou igual a 5,0 mg L-1')

st.subheader('PARAMETROS FÍSICO-QUÍMICOS ADEQUADO DA ÁGUA PARA CULTIVO DE PIRARUCU')
st.markdown('Temperatura: Entre 28°C e 30°C')
st.markdown('Ph: 5,0 a 11,5')
st.markdown('Oxigênio dissolvido: Maior ou igual a 1,5 a menor ou igual a 9,4 mg/L')
st.markdown('Alcalinidade: Maior ou igual 30 mg/L a menor ou igual a 300 mg/L')
st.markdown('Turbidez: Maior que 60 cm.')
st.markdown('Amônia: Abaixo de 2,4 mg/L.')
st.markdown('Nitrito:Menor ou igual a 0,5 mg L-1.')
st.markdown('Nitrato: Menor ou igual a 5,0 mg L-1')
