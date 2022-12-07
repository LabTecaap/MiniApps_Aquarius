import streamlit as st


def Temperatura():
    st.write('Temperatura:',(str(temp)),'°C',)
    if temp >= temp_minima and temp <= temp_maxima:
        return ('A temperatura está ideal para o cultivo dessa espécie.')
    else :
        return ('Esta temperatura não é ideal para o cultivo dessa espécie.')
        
def Ph():
    st.write('PH:',(str(ph)))    
    if ph >= ph_minimo and ph <= ph_maximo:
        return ('O pH é ideal para o cultivo dessa espécie.')
    else :
        return ('Este pH não é ideal para o cultivo dessa espécie')
    
def Turbidez():
    st.write('Turbidez:', (str(turb)))
    if option == 'Pirarucu':
        if turb > turb_minima :
            return ('A turbidez está ideal para o cultivo dessa espécie.')
        else :
            return ('Esta turbidez não é ideal para o cultivo dessa espécie.')    
    if option == 'Tilápia' or 'Tambaqui':
        if turb >= turb_minima and turb <= turb_maxima:
            return ('A turbidez está ideal para o cultivo dessa espécie.')
        else :
            return ('Esta turbidez não é ideal para o cultivo dessa espécie') 
                  
def Oxigênio():
    st.write('Oxigênio:', (str(oxe)))
    if option == 'Tilápia' or option == 'Pirarucu':
        if oxe >= oxe_minimo and oxe <= oxe_maximo:
            return ('A concentração de oxigênio dissolvido está ideal para o cultivo dessa espécie.')
        else :
            return ('A concentração de oxigênio dissolvido não é ideal para o cultivo dessa espécie.')
    else:
        if oxe >= oxe_minimo: 
            return ('A concentração de oxigênio dissolvido está ideal para o cultivo dessa espécie. ')
        else :
            return ('A concentração de oxigênio dissolvido não é ideal para o cultivo dessa espécie.')
    
def Acalinidade():
    st.write('Alcalinidade:', (str(alca)))
    if alca == alca_maxino :
        return ('O valor de alcalinidade está ideal para o cultivo dessa espécie.')
    else :
        return ('O  valor de alcalinidade não é ideal para o cultivo dessa espécie ')
    
def Amonia():
    st.write('Amônia:', (str(amon))) 
    if amon <= amon_maximo:
        return ('Esta faixa de amônia é ideal para o cultivo dessa espécie.')
    else :
        return ('Esta faixa de amônia não é ideal para o cultivo dessa espécie')
    
def Nitrito():
    st.write('Nitrito:', (str(ntri)))
    if ntri <= ntri_maximo :
        return ('Esta faixa de nitrito é ideal para o cultivo dessa espécie.')
    else :
        return ('Esta faixa de nitrito não é ideal para o cultivo dessa espécie')

def Nitrato():
    st.write('Nitrato:', (str(ntra)))
    if ntra <= ntra_maximo :
        return ('Esta faixa de nitrato é ideal para o cultivo dessa espécie.')
    else :
        return ('Esta faixa de nitrato não é ideal para o cultivo dessa espécie.')

st.title('Aquarius')

option = st.selectbox('Qual especie ?',('','Tambaqui', 'Tilápia', 'Pirarucu'))
st.write('Especie escolhida',option)

if option == 'Tambaqui':
    temp_minima = 25
    temp_maxima = 32
    ph_minimo = 6.5
    ph_maximo = 8.5
    oxe_minimo = 4
    amon_maximo = 2
    alca_minimo = 20
    alca_maxino =300
    turb_minima = 15
    turb_maxima = 40
    ntra_maximo = 5
    ntri_maximo = 0.5 
    st.header('Insira os paramentros da agua')
    
    temp = st.slider('Temperatura da agua em °C ?', 0, 40, 20)
    ph = st.slider('Ph da agua em °C ?', 0, 14, 7)
    turb = st.number_input(' Turbidez ')
    oxe = st.number_input(' Oxigenio dissolvido       ')
    alca = st.number_input(' Alcalinidade ')
    amon = st.number_input('Amonia')
    ntri = st.number_input('Nitrito')
    ntra = st.number_input('Nitrato')
    
if option == 'Tilápia':
    temp_minima = 27
    temp_maxima = 32
    ph_minimo = 6.5
    ph_maximo = 9
    oxe_minimo = 0.7
    oxe_maximo = 1.6
    amon_maximo = 0.24
    alca_minimo = 30
    alca_maxino = 300
    turb_minima = 15
    turb_maxima = 40
    ntra_maximo = 5
    ntri_maximo = 0.5
    
    st.header('Insira os paramentros da agua')
    temp = st.slider('Temperatura da agua em °C ?', 0, 40, 20)
    
    ph = st.slider('Ph da agua em °C ?', 0, 14, 7)
    turb = st.number_input('Turbidez')
    oxe = st.number_input('Oxigenio dissolvido')
    alca = st.number_input('Alcalinidade')
    amon = st.number_input('Amonia')
    ntri = st.number_input('Nitrito')
    ntra = st.number_input('Nitrato')
    
if option == 'Pirarucu':
    temp_minima = 28
    temp_maxima = 30
    ph_minimo = 5
    ph_maximo = 11.5
    oxe_minimo = 1.5
    oxe_maximo = 9.4
    amon_maximo = 2.4
    alca_minimo = 30
    alca_maxino = 300
    turb_minima = 60
    #turb_maxima = 40
    ntra_maximo = 5
    ntri_maximo = 0.5
    
    st.header('Insira os paramentros da agua')
    temp = st.slider('Temperatura da agua em °C ?', 0, 40, 20)
    ph = st.slider('Ph da agua em °C ?', 0, 14, 7)
    turb = st.number_input('Turbidez')
    oxe = st.number_input('Oxigenio dissolvido')
    alca = st.number_input('Alcalinidade')
    amon = st.number_input('Amonia')
    ntri = st.number_input('Nitrito')
    ntra = st.number_input('Nitrato')
    
if st.button('Calcular'): 
       
    st.header('Resultados')            
    st.write(Temperatura())                 
    st.write(Ph())
    st.write(Turbidez())
    st.write(Oxigênio())
    st.write(Acalinidade())
    st.write(Amonia())
    st.write(Nitrito())
    st.write(Nitrato())           