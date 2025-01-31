# Análise de Dados com Streamlit

## Descrição
Este projeto é uma aplicação web desenvolvida com **Streamlit** para analisar dados de devoluções a partir de uma planilha. Ele permite carregar um arquivo Excel ou CSV e exibir informações relevantes através de tabelas e gráficos, incluindo:

- **Vendedor com maior devolução por supervisão**
- **Valor total de devolução por supervisão**
- **Cliente com maior devolução**
- **Motorista com maior número de devoluções**
- **Análise de motivos de devolução utilizando IA**

## Tecnologias Utilizadas
- **Python**
- **Pandas** (para manipulação de dados)
- **Streamlit** (para a interface web)
- **Groq API** (para análise de texto via IA)

## Estrutura do Projeto
```
projeto-analise-streamlit/
├── main.py               # Script principal da aplicação
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
```

## Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/MichaelOli/8345.git
   cd 8345
   ```
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a aplicação:
   ```bash
   streamlit run main.py
   ```
5. Acesse a aplicação no navegador pelo link exibido no terminal.

## Uso
- Carregue um arquivo **Excel (.xlsx)** ou **CSV (.csv)**.
- Acompanhe as análises e insights gerados.
- Explore as tabelas e gráficos interativos.

## Melhorias Futuras
- Implementar mais gráficos dinâmicos.
- Melhorar a interface visual da aplicação.
- Criar opções de download para relatórios gerados.

## Autor
MICHAEL OLIVEIRA RIBEIRO

---
Este projeto foi desenvolvido para facilitar a análise de devoluções e gerar insights valiosos a partir dos dados!

