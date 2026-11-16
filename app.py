import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("esus-vepi.LeitoOcupacao_2020.csv", sep=";")


df["mes"] = df["dataNotificacao"].astype(str).str[5:7]

st.set_page_config(page_title="📊COVID-19 em 2020 - Minas Gerais", layout="wide")

df_filtrado = df[
    (df["estado"].isin(["Minas Gerais"]))
].copy()


df_tabela = df_filtrado[["estado", "mes","ocupacaoConfirmadoUti"]]


st.title("Painel COVID-19 de Minas Gerais")

st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])

if opcao == "Tabela":
    st.header("Tabela Leito Ocupação")
    st.dataframe(df_tabela, use_container_width=True, hide_index=True)

elif opcao == "Gráficos":
    st.header("Gráfico CTI por COVID-19")

    st.subheader("1. Gráfico de Linha")
    df_minas = df_tabela[df_tabela["estado"] == "Minas Gerais"]

    fig_linha_minas = px.line(
        df_filtrado,
        x="mes",
        y="ocupacaoConfirmadoUti",
        markers=True,
        title="CTI por COVID-19 confirmada",
        template="plotly_dark"
    )
    fig_linha_minas.update_traces(line_color="#FF6B6B", line_width=3, marker_size=8)
    fig_linha_minas.update_xaxes(type="category")
    fig_linha_minas.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_linha_minas, use_container_width=True)












st.markdown("---")
st.caption("Fonte dos dados: — https://opendatasus.saude.gov.br/")