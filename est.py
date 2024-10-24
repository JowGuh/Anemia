import pandas as pd
import streamlit as st
import plotly.express as px

# Carregar os dados dos arquivos Excel
df_anna = pd.read_excel('anna.xlsx')
df_anna4 = pd.read_excel('anna4.xlsx')

colors = px.colors.qualitative.Pastel1

colors2 = px.colors.qualitative.Dark24


# Gráfico 1: População de cada país
with st.expander("População de Cada País", expanded=True):
        
        st.title('População de Cada País')
        st.write("""
        **Este gráfico apresenta os dados da população aproximada de cada país analisado, fornecendo uma base para comparação proporcional dos casos de anemia falciforme.**
    """)
        fig1 = px.bar(df_anna, x='País', y='População Aproximada', title='',color='País', color_discrete_sequence=colors)
        fig1.update_layout(xaxis_title='País', yaxis_title='População Aproximada', xaxis_tickangle=-45)
        st.plotly_chart(fig1, use_container_width=True)

        

    # Gráfico 2: Número de pessoas com anemia falciforme em 2021 por país
with st.expander("Número de Pessoas com Anemia Falciforme em 2021", expanded=True):
        st.title('Número de Pessoas com Anemia Falciforme em 2021')
        st.write("""
        **Este gráfico exibe os dados da pesquisa mais recente (2021), publicada pela revista The Lancet, que mostra o número de pessoas diagnosticadas com anemia falciforme em cada país. Observa-se que a Nigéria tem o maior número de casos, seguida pelo Brasil, Índia e República Democrática do Congo.**
    """)
        fig2 = px.bar(df_anna, x='País', y='Número Estimado de Pessoas com DF (2021)', title='', color='País', color_discrete_sequence=colors)
        fig2.update_layout(xaxis_title='País', yaxis_title='Número de Pessoas com DF em 2021', xaxis_tickangle=-45)
        st.plotly_chart(fig2, use_container_width=True)

    # Gráfico 3: Aumento da anemia falciforme (2015 - 2021)
with st.expander("Aumento da Anemia Falciforme (2015 - 2021)", expanded=True):
        st.title('Aumento da Anemia Falciforme (2015 - 2021)')
        st.write("""
        **Este gráfico ilustra o aumento percentual dos casos de anemia falciforme em cada país entre 2015 e 2021. Nota-se que o aumento acompanha o padrão dos países com maior número de pessoas afetadas, com destaque para Nigéria, Brasil, Índia e República Democrática do Congo.**
    """)
        fig3 = px.line(df_anna, x='País', y=['Número Estimado de Pessoas com DF (2015)', 'Número Estimado de Pessoas com DF (2021)'], 
                title='',  color_discrete_sequence=colors)
        fig3.update_layout(xaxis_title='País', yaxis_title='Número Estimado de Pessoas com DF', xaxis_tickangle=-45)
        st.plotly_chart(fig3, use_container_width=True)

with st.expander("PIB e IDH por País", expanded=True):
        st.title('PIB e IDH por País')
        st.write("""              
**O Índice de Desenvolvimento Humano (IDH) e o Produto Interno Bruto (PIB) de cada país foram analisados para entender como fatores socioeconômicos, como desigualdade de renda e acesso à educação e serviços de saúde, afetam a saúde da população e a prevalência de doenças como a anemia falciforme.**
    """)
        fig18 = px.bar(df_anna4, x='País', y='PIB (USD)', title='PIB de cada País',color='País', color_discrete_sequence=colors)
        fig18.update_layout(xaxis_title='País', yaxis_title='PIB de cada País', xaxis_tickangle=-45)
        st.plotly_chart(fig18, use_container_width=True)

        
        st.title('')
        fig19 = px.bar(df_anna4, x='País', y='IDH', title='IDH de cada País',color='País', color_discrete_sequence=colors)
        fig19.update_layout(xaxis_title='País', yaxis_title='IDH de cada País', xaxis_tickangle=-45)
        st.plotly_chart(fig19, use_container_width=True)

map_acesso_saude2 = {
    'Muito limitado': 10,
    'Limitado': 20,
    'Variado': 30,
    'Noderado': 40
}
df_anna4['Acesso à Saúde Numérico'] = df_anna4['Acesso a Sistema de Saúde'].map(map_acesso_saude2)

    # Gráfico 6: Acesso ao sistema de saúde por país
with st.expander("Acesso ao Sistema de Saúde por País", expanded=True):
        st.title('Acesso ao Sistema de Saúde por País')
        st.write("""
        **Este gráfico analisa o acesso ao sistema de saúde em cada país. Entre os países com maior prevalência de anemia falciforme, a maioria está classificada como tendo "acesso limitado" ou "muito limitado" aos serviços de saúde, o que contribui para a dificuldade no diagnóstico e tratamento adequados.**
    """)
        fig6 = px.bar(df_anna4, x='País', y='Acesso a Sistema de Saúde', title='', color='País', color_discrete_sequence=colors)
        fig6.update_layout(xaxis_title='País', 
                              yaxis_title='Acesso a Sistema de Saúde',
                              xaxis_tickangle=-45,
                              yaxis=dict(
                                  tickvals=[10, 20, 30, 40],
                                  ticktext=['Muito Limitado', 'Limitado', 'Variado', 'Moderado']
                              ))
        st.plotly_chart(fig6, use_container_width=True)


map_acesso_saude3 = {
    'Montonhoso': 10,
    'Desértico': 20,
    'Seco': 30,
    'Variado': 40,
    'Tropical': 50
}
df_anna4['Clima por País'] = df_anna4['Clima'].map(map_acesso_saude3)
    # Gráfico 7: Clima por país
with st.expander("Clima por País", expanded=True):
        st.title('Clima por País')
        st.write("""
        **Esta análise considera o clima em cada país, categorizado como variado, tropical, montanhoso, desértico e seco. “A maior prevalência da anemia falciforme ocorre em países com clima variado, o que pode estar relacionado à histórica presença da malária nessas regiões. A anemia falciforme é mais comum onde a malária é endêmica, pois o traço falciforme confere resistência à malária, perpetuando a presença da doença em climas tropicais e úmidos.**
    """)
        fig7 = px.bar(df_anna4, x='País', y='Clima', title='', color='País', color_discrete_sequence=colors)
        fig7.update_layout(xaxis_title='País', 
                              yaxis_title='Clima',
                              xaxis_tickangle=-45,
                              yaxis=dict(
                                  tickvals=[10, 20, 30, 40, 50],
                                  ticktext=['Montonhoso', 'Desértico', 'Seco', 'Variado', 'Tropical']
                              ))
        st.plotly_chart(fig7, use_container_width=True)

    


# Carregar os dados dos arquivos Excel
df_anna2 = pd.read_excel('anna2.xlsx')
df_anna3 = pd.read_excel('anna3.xlsx')



    # Gráfico 1: Número de pessoas com anemia falciforme em cada estado (2021)
with st.expander("Número de Pessoas com Anemia Falciforme por Estado (2021)", expanded=True):
        st.title('Número de Pessoas com Anemia Falciforme por Estado (2021)')
        st.write("""
        **Este gráfico apresenta os dados mais recentes (2021) sobre o número de pessoas com anemia falciforme em cada estado do Brasil. São Paulo lidera em número de casos, seguido por Santa Catarina, Minas e Bahia.**
    """)
        fig1_brasil = px.bar(df_anna2, x='Estado', y='Prevalência em 2021 (casos novos)', title='', color='Estado', color_discrete_sequence=colors2)
        fig1_brasil.update_layout(xaxis_title='Estado', yaxis_title='Prevalência em 2021 (casos novos)', xaxis_tickangle=-45)
        st.plotly_chart(fig1_brasil, use_container_width=True)

    # Gráfico 2: Aumento da anemia falciforme - 2015 vs 2021
with st.expander("Aumento da Anemia Falciforme por Estado (2015 - 2021)", expanded=True):
        st.title('Aumento da Anemia Falciforme por Estado (2015 - 2021)')
        st.write("""
        **Este gráfico mostra o aumento percentual de novos casos de anemia falciforme em cada estado brasileiro entre 2015 e 2021. Observa-se que o crescimento é proporcional aos estados com maior incidência de casos.**
    """)
        fig2_brasil = px.line(df_anna2, x='Estado', y=['Prevalência em 2015 (casos novos)', 'Prevalência em 2021 (casos novos)'], 
                        title='',  color_discrete_sequence=colors2)
        fig2_brasil.update_layout(xaxis_title='Estado', yaxis_title='Prevalência de Casos Novos', xaxis_tickangle=-45)
        st.plotly_chart(fig2_brasil, use_container_width=True)

    # Gráfico 3: Idade média das pessoas por estado
with st.expander("Idade Média das Pessoas por Estado", expanded=True):
        st.title('Idade Média das Pessoas por Estado')
        st.write("""
        **Este gráfico revela que a maioria das pessoas afetadas pela anemia falciforme no Brasil está na infância, adolescência e início da vida adulta, sendo menos comum em idades mais avançadas.**
    """)
        fig3_brasil = px.bar(df_anna2, x='Estado', y='Idade das Pessoas Mais Afetadas', title='', color='Estado', color_discrete_sequence=colors2)
        fig3_brasil.update_layout(xaxis_title='Estado', yaxis_title='Idade Média', xaxis_tickangle=-45)
        st.plotly_chart(fig3_brasil, use_container_width=True)

   

map_acesso_saude = {
    'Muito limitado': 10,
    'Limitado': 20,
    'Moderado': 30,
    'Bom': 40
}
df_anna3['Acesso à Saúde Numérico'] = df_anna3['Acesso à Saúde'].map(map_acesso_saude)

    # Gráfico 5: Acesso ao sistema de saúde por estado
with st.expander("Acesso ao Sistema de Saúde por Estado", expanded=True):
    st.title('Acesso ao Sistema de Saúde por Estado')
    st.write("""
        **Analisamos também o acesso ao sistema de saúde nos estados brasileiros. Observou-se que muitos estados com "acesso limitado" ao sistema de saúde não estão entre aqueles com maior prevalência de anemia falciforme, destacando uma possível lacuna no atendimento médico especializado.**
    """)
    
    # Gráfico de barras empilhadas
    fig5_stacked = px.bar(df_anna3, x='Estado', y='Acesso à Saúde', 
                          color='Estado', 
                          title='',
                          color_discrete_sequence=colors2)
    
    # Ajustar o layout
    fig5_stacked.update_layout(xaxis_title='Estado', 
                              yaxis_title='Acesso à Saúde',
                              xaxis_tickangle=-45,
                              yaxis=dict(
                                  tickvals=[10, 20, 30, 40],
                                  ticktext=['Muito Limitado', 'Limitado', 'Moderado', 'Bom']
                              ))
    
    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig5_stacked, use_container_width=True)

map_acesso_saude4 = {
    'Diversificado': 10,
    'Amazonico': 20,
    'Semiárido': 30,
    'Temperado': 40,
    'Equatorial': 50,
    'SubTropical': 60,
    'Tropical': 70
}
df_anna3['Clima por Estado'] = df_anna3['Clima'].map(map_acesso_saude4)



    # Gráfico 6: Clima por estado
with st.expander("Clima por Estado", expanded=True):
        st.title('Clima por Estado')
        st.write("""
        **Os estados com maior prevalência de anemia falciforme estão localizados em regiões com clima tropical e diversificado. Esse padrão pode ser explicado pela maior prevalência do traço falciforme em áreas historicamente afetadas pela malária, onde a mutação genética oferece resistência à doença. Isso perpetua a alta incidência da anemia falciforme em climas tropicais.**
    """)
        fig6_brasil = px.bar(df_anna3, x='Estado', y='Clima', title='', color='Estado', color_discrete_sequence=colors2)
        fig6_brasil.update_layout(xaxis_title='Estado', 
                              yaxis_title='Clima',
                              xaxis_tickangle=-45,
                              yaxis=dict(
                                  tickvals=[10, 20, 30, 40, 50, 50, 70],
                                  ticktext=['Diversificado', 'Amazonico', 'Semiárido', 'Temperado', 'Equatorial','SubTropical','Tropical' ]
                              ))
        st.plotly_chart(fig6_brasil, use_container_width=True)


with st.expander("", expanded=True):
    st.title('Conclusão')
    st.write("""
        **A análise do caso clínico de S.S., uma criança de 6 anos diagnosticada com anemia falciforme, ilustra a complexidade da doença no Brasil, onde a prevalência varia significativamente entre os estados, destacando a Bahia e Minas Gerais, que apresentam taxas de até 1 a cada 650 nascimentos. Dados globais indicam que o Brasil é um dos países com o maior número de casos de anemia falciforme, atrás apenas da Nigéria, Índia e República Democrática do Congo, conforme a pesquisa da The Lancet de 2021. 
Como apresentado nos dados,  muitas áreas com alta prevalência de anemia falciforme têm acesso "limitado" ou "muito limitado" a serviços de saúde, dificultando o diagnóstico e tratamento.
O caso de S.S. não é um evento isolado, mas sim uma manifestação de um problema de saúde pública que requer uma abordagem abrangente e coordenada para enfrentar as dificuldades enfrentadas por pacientes em contextos semelhantes.**
    """)
    st.title('Referências')
    st.write("""
        ANVISA. Doença Falciforme. Disponível em: https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/medicamentos/biodisponibilidade-e-bioequivalencia/doenca-falciforme. Acesso em: 01 out. 2024.

BRASIL. Diretrizes básicas para a linha de cuidado da anemia falciforme. Brasília: Ministério da Saúde, 2018. Disponível em: https://bvsms.saude.gov.br/bvs/publicacoes/doenca_falciforme_diretrizes_basicas_linha_cuidado.pdf. Acesso em: 01 out. 2024.

BRASIL. Experiência brasileira e África: uma comparação da assistência à saúde na anemia falciforme. Brasília: Ministério da Saúde, 2019. Disponível em: https://bvsms.saude.gov.br/bvs/publicacoes/doenca_falciforme_experiencia_brasileira_africa.pdf. Acesso em: 01 out. 2024.

BARRIOS, R. C.; ESTEVES, R. R. A doença falciforme em países da África Subsaariana: revisão integrativa da literatura. Revista Brasileira de Hematologia e Hemoterapia, v. 41, n. 4, p. 366-371, 2019. Disponível em: https://inisa.ufms.br/files/2019/04/A-DOEN%C3%87A-FALCIFORME-EM-PA%C3%8DS-DA-%C3%81FRICA-SUBSAARIANA-revis%C3%A3o-integrativa-da-literatura.pdf. Acesso em: 01 out. 2024.

KASSEBAUM, N. J. et al. Global, regional, and national prevalence and mortality burden of sickle cell disease, 2000–2021: a systematic analysis from the Global Burden of Disease Study 2021. Lancet Haematology, v. 10, p. e585–99, 2023. DOI: 10.1016/S2352-3026(23)00118-7.

MELLO, S. D. et al. Anemia falciforme: tudo o que você precisa saber sobre a doença através do artigo do Manual MSD. Suprema.edu.br. Disponível em: https://www.suprema.edu.br/noticia/anemia-falciforme-tudo-que-voce-precisa-saber-sobre-a-doenca-atraves-do-artigo-do-manual-msd. Acesso em: 01 out. 2024.

BRASIL. Protocolo Clínico e Diretrizes Terapêuticas para Doença Falciforme. Brasília: CONITEC, 2018. Disponível em: https://www.gov.br/conitec/pt-br/midias/protocolos/pcdt_doencafalciforme_2018-1.pdf. Acesso em: 01 out. 2024.

HASSELL, K. L. Population estimates of sickle cell disease in the United States. Blood, v. 115, n. 22, p. 1802-1808, 2010. DOI: 10.1182/blood-2009-07-234413.

KAMBOUROVA, V. S.; BILAL, D. H. The role of hydroxyurea in the management of sickle cell disease: an overview. Therapeutic Advances in Hematology, v. 6, n. 6, p. 299-305, 2015. DOI: 10.1177/2040620715610484.

PLATT, O. S. et al. Mortality in sickle cell disease: life expectancy and risk factors for early death. New England Journal of Medicine, v. 330, n. 23, p. 1639-1644, 1994. DOI: 10.1056/NEJM199406093302303.

PAPPA, S. et al. Sickle cell disease: current concepts in management. British Journal of Hospital Medicine, v. 80, n. 6, p. 1-8, 2019. DOI: 10.12968/hmed.2019.80.6.1.

REES, D. C.; WILLIAMS, T. N.; GLADWIN, M. T. Sickle-cell disease. The Lancet, v. 390, n. 10091, p. 453-465, 2017. DOI: 10.1016/S0140-6736(17)30193-7.

SCIELO. Anemia falciforme: um estudo de caso. Disponível em: https://www.scielo.sa.cr/scielo.php?pid=S1409-45682020000200027&script=sci_arttext. Acesso em: 01 out. 2024.

HEMOCORD. Sangue de cordão para curar anemia falciforme em menina de dois anos. Disponível em: https://hemocord.com.br/sangue-de-cordao-para-curar-anemia-falciforme-em-menina-de-dois-anos/. Acesso em: 01 out. 2024.
    """)