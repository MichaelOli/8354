import streamlit as st
import pandas as pd
import groq


# Defina sua chave da API
client = groq.Client(api_key="sua-chave-da-api")  

# Título da aplicação
st.title("Análise de Dados da Planilha")

# Upload do arquivo
uploaded_file = st.file_uploader("Carregue sua planilha", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Verifica o tipo do arquivo e carrega os dados sem forçar dtype
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Garantindo que CODCLI e CODMOTORISTA sejam inteiros, tratando erros
    df["CODCLI"] = pd.to_numeric(df["CODCLI"], errors="coerce").fillna(0).astype(int)
    df["CODMOTORISTA"] = pd.to_numeric(df["CODMOTORISTA"], errors="coerce").fillna(0).astype(int)

    # Exibe os primeiros registros
    st.subheader("Pré-visualização dos Dados da planilha:")
    st.write(df.head())

    # Informações básicas
    #st.subheader("Informações Gerais")
    #st.write(df.describe())

    # Qual vendedor com maior devolução por supervisão
    st.subheader("Qual vendedor com maior devolução por supervisão")
    vendedor_maior_devolucao = df.groupby(["CODSUPERVISOR", "CODUSUR", "VENDEDOR"])['VLDEVOL'].sum().reset_index()
    vendedor_maior_devolucao = vendedor_maior_devolucao.sort_values(by='VLDEVOL', ascending=True)
    st.write(vendedor_maior_devolucao)

    # Valor total devolução por supervisão
    st.subheader("Valor Total Devolução por Supervisão")
    devolucao_por_supervisao = df.groupby('CODSUPERVISOR')['VLDEVOL'].sum().reset_index()
    devolucao_por_supervisao = devolucao_por_supervisao.sort_values(by='VLDEVOL', ascending=True)
    st.write(devolucao_por_supervisao)

    # Qual cliente com maior devolução
    st.subheader("Qual Cliente com Maior Devolução")
    cliente_maior_devolucao = df.groupby(['CODCLI', 'CLIENTE'])['VLDEVOL'].sum().reset_index()
    cliente_maior_devolucao = cliente_maior_devolucao.sort_values(by='VLDEVOL', ascending=True)
    st.write(cliente_maior_devolucao.style.format({"CODCLI": "{}".format}))


    # Qual motorista com maior número de devoluções
    st.subheader("Qual Motorista com Maior Número de Devoluções")
    motorista_maior_devolucao = df.groupby(['CODMOTORISTA', 'NOMEMOTORISTA'])['VLDEVOL'].count().reset_index()
    motorista_maior_devolucao = motorista_maior_devolucao.sort_values(by='VLDEVOL', ascending=True)
    st.write(motorista_maior_devolucao.style.format({"CODMOTORISTA": "{}".format, "CODCLI": "{}".format}))


    # Qual maior motivo de observação
    st.subheader("Qual Maior Motivo de Observação")

    def analisar_obs(df):
        obs_text = ". ".join(df['OBS'].dropna().astype(str).unique())
        prompt = f"Analisar os motivos de devolução com base nas seguintes observações:\n\n{obs_text}"

        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
            temperature=0.7
        )

        return response.choices[0].message.content.strip()

    motivo_maior_obs = analisar_obs(df)
    st.write(motivo_maior_obs)

else:
    st.warning("Nenhum arquivo carregado.")
