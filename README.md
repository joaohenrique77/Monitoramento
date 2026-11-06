# ⚡ Task Manager (Gerenciador de Tarefas)

Um aplicativo desktop moderno e intuitivo desenvolvido em Python para monitorar em tempo real a performance do sistema, incluindo uso de CPU, memória RAM, unidades de armazenamento e informações de hardware e sistema operacional.

---

## 💻 Sobre o Projeto

O **Task Manager** é dividido em uma arquitetura modular entre interface gráfica (Front-end) e coleta de métricas (Back-end):
- **Interface Gráfica (`app.py`):** Desenvolvida com `customtkinter`, oferecendo um design moderno com suporte nativo ao modo escuro (Dark Mode) e navegação por abas em menu lateral.
- **Mapeamento do Sistema (`src/funcoes.py`):** Utiliza as bibliotecas `psutil`, `platform` e `socket` para coletar métricas de hardware de forma contínua e assíncrona.

---

## 🎯 Funcionalidades

- 📊 **Desempenho em Tempo Real:** 
  - Acompanhamento do uso percentual do processador (CPU) com barra de progresso visual.
  - Monitoramento da memória RAM (porcentagem, GBs usados, disponíveis e totais).
  - Atualização automática a cada 3 segundos.
- 💾 **Gerenciamento de Armazenamento:** 
  - Listagem dinâmica de todas as unidades de disco conectadas.
  - Exibição do espaço consumido, livre e limite de capacidade.
  - Alertas visuais na barra de progresso quando o disco ultrapassa 85% de uso.
- 💻 **Informações do Sistema:**
  - Exibição de dados do computador como nome da máquina, Sistema Operacional, versão, arquitetura e modelo do processador.

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3](https://www.python.org/):** Linguagem principal do projeto.
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter):** Interface gráfica moderna e customizável baseada em Tkinter.
- **[psutil](https://github.com/giampaolo/psutil):** Biblioteca para obtenção de informações sobre processos e utilização do sistema (CPU, memória, discos).

---

## 📂 Estrutura do Projeto

```text
├── src/
│   └── funcoes.py      # Back-end: Funções de coleta de dados do sistema
├── app.py              # Front-end: Interface gráfica com CustomTkinter
└── README.md           # Documentação do projeto
```


## Crie o ambiente virtual (venv)
   ```bash
   python -m venv venv
   ```
## Ative o ambiente virtual
   ```bash
   .\venv\Scripts\Activate.ps1
   ```
## Instale as dependências
   ```bash
   pip install -r requirements.txt
   ```
## Execute a aplicação
   ```bash
   python app.py
   ```

## Creditos
Criado por João Figueiró e Filipe Nonemacher
