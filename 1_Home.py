import os
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Meu Portfólio", page_icon=":briefcase:", layout="wide")

# Página de apresentação
st.markdown("""# Sejam bem vindos ao meu portfólio.""")
st.write("Aqui vocês terão acesso aos meus projetos mais relevantes que construi, minha experiência profissional e um pouco sobre mim.")

st.subheader("Sobre mim")

if 'show_tldr' not in st.session_state:
    st.session_state.show_tldr = False

# Função para alternar o estado
def toggle_tldr():
    st.session_state.show_tldr = not st.session_state.show_tldr

# Botão TL;DR
st.button('TLDR', on_click=toggle_tldr, type='primary')

# Exibir ou esconder o resumo com base no estado
if st.session_state.show_tldr:
    tldr = """
    <div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px;">
        <b>- Nome:</b> Luis Gustavo Ribeiro Andrade.<br>
        <b>- Formação:</b> Conclusão do Ensino Médio na EPCAR (2019);<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Estudante de Economia na FGV EPGE (Conclusão em 2024).<br>
        <b>- Experiência:</b> Estágio no Banco BOCOM BBM (BackOffice - Automação de rotinas).<br>
        <b>- Habilidades:</b> Python, SQL, Excel (Macro/VBA), Streamlit, PowerBI.<br>
        <b>- Interesses:</b> Transição para áreas mais de acordo com a área de eletivas escolhidas, Finanças Quantitativas.<br>
        <b>- Objetivos Futuros:</b> Certificação CFA.
    </div>
    """
    st.markdown(tldr, unsafe_allow_html=True)
    
# Texto completo 
st.write("""
Meu nome é **Luis Gustavo Ribeiro Andrade** e sou estudante de Economia na Fundação Getúlio Vargas (FGV EPGE) no Rio de Janeiro. Desde cedo, desenvolvi uma paixão por resolver problemas complexos e por programação, o que me levou a conquistar quatro medalhas na Olimpíada Brasileira de Matemática das Escolas Públicas (OBMEP) e uma medalha de ouro na Olimpíada de Física, além de medalhas em Astronomia e Robótica.

Minha jornada na programação começou aos 14 anos, quando me juntei a uma equipe de robótica na minha escola em São Tiago, cidade onde nasci. Foi lá que aprendi a programar, o que despertou meu interesse por tecnologia e inovação. Entre 2017 e 2019, mudei-me para Barbacena, Minas Gerais, para completar meu ensino médio na Escola Preparatória de Cadetes do Ar (EPCAR), uma instituição de formação de oficiais da Aeronáutica. Durante esse período, iniciei o projeto de um clube de robótica, onde pude compartilhar meu conhecimento e continuar desenvolvendo minhas habilidades.

Em 2020, ingressei na FGV e me formo ao final de 2024. Ao longo do curso, fui incentivado a desenvolver pequenos projetos, o que me levou a aprofundar minhas habilidades em programação, especialmente em Python. Durante minha graduação, me especializei em áreas como Finanças, Econometria, e Machine Learning, participando de cursos e laboratórios que fortaleceram meu perfil técnico. Alguns dos cursos que mais contribuíram para meu desenvolvimento foram Análise de Dados em Python, Análise de Dados em R, Machine Learning, Derivativos, e Quantitative Finance.

Atualmente, estagio no Banco BOCOM BBM, na área de BackOffice dos Fundos da Asset, onde trabalho no desenvolvimento de projetos de automação de rotinas e outras soluções voltadas para os fundos (por questões de confidencialidade, detalhes específicos não podem ser mencionados). 

Minhas habilidades técnicas abrangem o uso de Python para diversas finalidades, como coleta de dados online via web scraping e APIs, processamento de dados armazenados localmente, tratamento e visualização de dados. Além disso, desenvolvo projetos em Excel utilizando Macro/VBA e linguagem M com Power Query para criar soluções acessíveis a usuários sem conhecimentos de programação. Também possuo experiência em bases de dados SQL e na criação de dashboards interativos em PowerBI, embora recentemente tenha preferido o uso da biblioteca Streamlit em Python devido à sua capacidade de oferecer sistemas mais completos e interativos, com atualizações em tempo real.

Estou em busca de oportunidades que me permitam aplicar minhas habilidades em finanças quantitativas em um ambiente dinâmico e desafiador, onde eu possa continuar a crescer profissionalmente e contribuir de forma significativa. Tenho interesse em migrar da área de BackOffice para uma função no FrontOffice, onde poderei aprofundar ainda mais as especializações desenvolvidas ao longo do meu curso. Além disso, estou empenhado em continuar meus estudos e futuramente realizar os exames para obter a certificação CFA, o que me permitirá expandir meu conhecimento e expertise no campo financeiro.
""")

st.sidebar.subheader("Contato")

st.sidebar.write("""
:email:**Email**: [lgandrade35@gmail.com](mailto:lgandrade35@gmail.com)
""")

st.sidebar.write("""
Você também pode me encontrar nas redes sociais:\n
:link:[LinkedIn](https://www.linkedin.com/in/luisgrandrade/)
""")
