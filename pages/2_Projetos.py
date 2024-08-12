import streamlit as st
import random as rd

cores = ['#F0F8FF', '#F8F8FF', '#FFFAFA', '#FFF5EE', '#FFFAF0', '#F5F5F5', '#F5F5DC', '#FDF5E6', '#FFFFF0', '#FAF0E6', '#FFF8DC', '#FAEBD7', '#FFEBCD', '#FFE4C4', '#FFFACD', '#FAFAD2', '#FFEFD5', '#FFDAB9', '#FFE4B5', '#EEE8AA', '#FFE4E1', '#FFF0F5', '#E6E6FA', '#D8BFD8', '#F0FFFF', '#E0FFFF', '#E0FFFF', '#E0FFFF', '#F0FFF0', '#F5FFFA']
i = 0


st.set_page_config(page_title="Meus Projetos", page_icon=":briefcase:", layout="wide")

# sidebar
st.sidebar.subheader("Contato")

st.sidebar.write("""
:email:**Email**: [lgandrade35@gmail.com](mailto:lgandrade35@gmail.com)
""")

st.sidebar.write("""
Você também pode me encontrar nas redes sociais:\n
:link:[LinkedIn](https://www.linkedin.com/in/luisgrandrade/)
""")

# Funções para criação
def criar_card(titulo, descricao, link, cores):
    global i
    cor_fundo = cores[i]
    i = i+1
    card = f"""
    <div style="background-color: {cor_fundo}; padding: 15px; border-radius: 10px; margin: 10px 0;">
        <h3 style="color: #333333;">{titulo}</h3>
        <p style="color: #555555;">{descricao}</p>
        <a href="{link}" style="text-decoration: none; color: #0066cc;" target="_blank">Ver mais</a>
    </div>
    """
    st.markdown(card, unsafe_allow_html=True)

#Início da página
st.header("Meus projetos")
st.write("Aqui, apresentarei alguns dos meus projetos. Muitos desses projetos foram produzidos com o objetivo de serem entregas de algum dos meus cursos de faculdade.")

col1, col2, col3 = st.columns(3)

with col1:
    criar_card(titulo="Análise de Dados do Brasileirão",
           descricao="Este projeto foi produzido durante o curso de análise de dados em Python na faculdade. Aqui, faço uma análise dos dados do Brasileirão e analiso os melhores e piores aproveitamentos dentro e fora de casa.",
           link= 'https://github.com/1conto/TrabalhoA1Python/blob/main/PythonA1.ipynb',
           cores=cores)
    
with col2:
    criar_card(titulo="Análise de Dados com R",
           descricao="Ao longo do curso de Análise de Dados em R na faculdade, foi preciso produzir dois dados, um com uma análise mais técnica, sendo esse projeto, o com maior domínio técnico de filtros e tratamentos. A base de dados é um base popular da kaggle.",
           link= 'https://1conto.github.io/TrabalhoR/',
           cores=cores)
    
with col3:
    criar_card(titulo="Dashboards em R",
           descricao="Outro projeto do curso de Análise de Dados em R. Aqui, o objetivo era trabalharmos com dados reais da população. Com isso, eu e meu grupo decidimos usar os dashboards do R. Minha parte do trabalho foi focada na visualização dos dados",
           link= 'https://1conto.github.io/TrabalhoA2R/',
           cores=cores)
    
with col1:
    criar_card(titulo="Dados Econométricos (Séries Temporais)",
               descricao="Esse projeto foi produzido ao longo do curso de Econometria II, utilizando técnicas de séries temporais para previsão. O modelo usado é o ARMA, muito utilizado para séries temporais. Tal projeto é o primeiro produzido durante o curso",
               link = 'https://colab.research.google.com/drive/1jHBmJSjET4nj20h5Xd7bD1ESmacdzRMd?usp=sharing',
               cores=cores)
    
with col2:
    criar_card(titulo="Mapeando desempenho de Fundos de Investimento em Ações",
               descricao="Projeto final apresentado em Econometria II. Utilizo de técnicas do Modelo GARCH para avaliar a rentabilidade e retorno de dois fundos de ação. Analisando a cota do fundo. Como os fundos não apresentam MtM, os modelos de Rentabilidade foram ajustados diariamente para considerarmos a variação da cota como a variação dos ativos presentes diariamente.",
               link = 'https://github.com/1conto/TrabalhoEconometriaFinal/blob/main/st%20(1).pdf',
               cores = cores)
    
with col3:
    criar_card(titulo="Criação de Portfólios com séries históricas dos ativos",
               descricao='Este código recebe uma lista de ativos pré-definidos, analisa as séries históricas comparando volatilidade e retorno histórico desses ativos, e define com o Índice de Sharpe os 5 melhores retornos dos ativos, escolhendo tal portfólio',
               link = 'https://github.com/1conto/LabFinancas/blob/main/A1%20labfin.ipynb',
               cores = cores)