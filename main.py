#import Package
import streamlit as st
import pandas as pd
import pydeck as pdk

#Upload File
df = pd.read_cssv("criminalidade_sp_2.csv")

#dashboard
st.title("Dados da criminalidade em São Paulo")

st.markdown("""
    Estatísticas mensais das ocorrências policiais na 
    capital paulista divulgadas pela Secretaria de Estado 
    da Segurança Pública de São Paulo é usada por Cientistas
    de Dados para ajudar entender os números e gerar insights
    que direcionem ações capazes de diminuir o índice de
    criminalidade na cidade.  
""")

# Info
st.sidebar.info("Foram carregadas {} linhas de ocorrências".format(df.shape[0]))


if st.sidebar.checkbox("Ver dados em Gráfico"):
    st.header("Dados de Entrada")
    st.write(df)

df.time = pd.to_datetime(df.time)
ano_selecionado = st.sidebar.slider("Selecione um ano", 2010, 2018, 2015)
df_selected = df[df.time.dt.year == ano_selecionado]

st.subheader("Mapa das Ocorrências")
st.map(df_selected)

st.pydeck_chart(pdk.Deck(
     initial_view_state=pdk.ViewState(
         latitude=-23.567145	,
         longitude=-46.648936,
         zoom=8,
         pitch=50
     ),
     layers=[
         pdk.Layer(
             'HexagonLayer',
             data=df_selected[['latitude', 'longitude']],
             get_position='[longitude,latitude]',
             auto_highlight=True,
             elevation_scale=50,
             pickable=True,
             elevation_range=[0, 3000],
             extruded=True,
             coverage=1
         )
     ],
 ))