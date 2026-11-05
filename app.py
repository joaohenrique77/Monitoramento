from src import funcoes
import customtkinter as ctk
from src import funcoes

# Configurações do tema CustomTkinter
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class GerenciadorDeTarefasFront(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configurações da Janela Principal
        self.title("Gerenciador de Tarefas")
        self.geometry("950x600")
        self.minsize(800, 500)

        # Buscar dados iniciais do sistema através do backend
        self.info_sys = funcoes.informacoes_sistema()

        # Grid principal da janela (Menu lateral | Conteúdo)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # 1. MENU LATERAL
        self.criar_sidebar()

        # 2. CONTAINER DE CONTEÚDO
        self.container_principal = ctk.CTkFrame(self, corner_radius=10)
        self.container_principal.grid(
            row=0, column=1, padx=15, pady=15, sticky="nsew"
        )
        self.container_principal.grid_rowconfigure(0, weight=1)
        self.container_principal.grid_columnconfigure(0, weight=1)

        # Construir as telas/abas
        self.criar_aba_desempenho()
        self.criar_aba_disco()
        self.criar_aba_sistema()

        # Iniciar na aba de Desempenho
        self.mostrar_aba_desempenho()

        # Iniciar loop de atualização em tempo real (chamando o backend)
        self.atualizar_dados_loop()

    def criar_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(
            self.sidebar,
            text="⚡ Task Manager",
            font=ctk.CTkFont(size=18, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 20))

        self.btn_desempenho = ctk.CTkButton(
            self.sidebar,
            text="📊 Desempenho",
            anchor="w",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            command=self.mostrar_aba_desempenho,
        )
        self.btn_desempenho.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.btn_disco = ctk.CTkButton(
            self.sidebar,
            text="💾 Armazenamento",
            anchor="w",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            command=self.mostrar_aba_disco,
        )
        self.btn_disco.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.btn_sistema = ctk.CTkButton(
            self.sidebar,
            text="💻 Sistema",
            anchor="w",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            command=self.mostrar_aba_sistema,
        )
        self.btn_sistema.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

    def criar_aba_desempenho(self):
        self.frame_desempenho = ctk.CTkFrame(
            self.container_principal, fg_color="transparent"
        )

        # Card CPU
        card_cpu = ctk.CTkFrame(self.frame_desempenho, corner_radius=10)
        card_cpu.pack(fill="x", padx=15, pady=10)

        ctk.CTkLabel(
            card_cpu,
            text="Processador (CPU)",
            font=ctk.CTkFont(size=16, weight="bold"),
        ).pack(anchor="w", padx=15, pady=(10, 2))

        self.lbl_cpu_percent = ctk.CTkLabel(
            card_cpu,
            text="Uso: 0%",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#3B82F6",
        )
        self.lbl_cpu_percent.pack(anchor="w", padx=15)

        self.progress_cpu = ctk.CTkProgressBar(card_cpu, height=12)
        self.progress_cpu.pack(fill="x", padx=15, pady=(5, 15))
        self.progress_cpu.set(0)

        # Card Memória RAM
        card_mem = ctk.CTkFrame(self.frame_desempenho, corner_radius=10)
        card_mem.pack(fill="x", padx=15, pady=10)

        ctk.CTkLabel(
            card_mem,
            text="Memória RAM",
            font=ctk.CTkFont(size=16, weight="bold"),
        ).pack(anchor="w", padx=15, pady=(10, 2))

        self.lbl_mem_percent = ctk.CTkLabel(
            card_mem,
            text="Uso: 0%",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#10B981",
        )
        self.lbl_mem_percent.pack(anchor="w", padx=15)

        self.progress_mem = ctk.CTkProgressBar(
            card_mem, height=12, progress_color="#10B981"
        )
        self.progress_mem.pack(fill="x", padx=15, pady=5)
        self.progress_mem.set(0)

        self.lbl_mem_detalhes = ctk.CTkLabel(
            card_mem, text="Usado: 0 GB | Disponível: 0 GB | Total: 0 GB"
        )
        self.lbl_mem_detalhes.pack(anchor="w", padx=15, pady=(0, 15))

    def criar_aba_disco(self):
        self.frame_disco = ctk.CTkScrollableFrame(
            self.container_principal, fg_color="transparent"
        )

    def criar_aba_sistema(self):
        self.frame_sistema = ctk.CTkFrame(
            self.container_principal, fg_color="transparent"
        )

        ctk.CTkLabel(
            self.frame_sistema,
            text="Informações do Sistema",
            font=ctk.CTkFont(size=20, weight="bold"),
        ).pack(anchor="w", padx=20, pady=(20, 15))

        if "erro" in self.info_sys:
            ctk.CTkLabel(
                self.frame_sistema, text=f"Erro: {self.info_sys['erro']}"
            ).pack(anchor="w", padx=20)
            return

        detalhes = [
            ("Nome do Computador:", self.info_sys.get("nome")),
            ("Sistema Operacional:", self.info_sys.get("sistema")),
            ("Versão do SO:", self.info_sys.get("versao")),
            ("Arquitetura:", self.info_sys.get("arquitetura")),
            ("Processador:", self.info_sys.get("processador")),
            ("Memória Total Instalada:", f"{self.info_sys.get('memoria_total')} GB"),
        ]

        for titulo, valor in detalhes:
            item_frame = ctk.CTkFrame(self.frame_sistema, corner_radius=6)
            item_frame.pack(fill="x", padx=20, pady=5)

            ctk.CTkLabel(
                item_frame, text=titulo, font=ctk.CTkFont(weight="bold")
            ).pack(side="left", padx=15, pady=10)
            ctk.CTkLabel(
                item_frame, text=str(valor), text_color="gray70"
            ).pack(side="right", padx=15, pady=10)

    def esconder_abas(self):
        self.frame_desempenho.pack_forget()
        self.frame_disco.pack_forget()
        self.frame_sistema.pack_forget()

        for btn in [self.btn_desempenho, self.btn_disco, self.btn_sistema]:
            btn.configure(fg_color="transparent")

    def mostrar_aba_desempenho(self):
        self.esconder_abas()
        self.btn_desempenho.configure(fg_color=("gray75", "gray25"))
        self.frame_desempenho.pack(fill="both", expand=True)

    def mostrar_aba_disco(self):
        self.esconder_abas()
        self.btn_disco.configure(fg_color=("gray75", "gray25"))
        self.frame_disco.pack(fill="both", expand=True)

    def mostrar_aba_sistema(self):
        self.esconder_abas()
        self.btn_sistema.configure(fg_color=("gray75", "gray25"))
        self.frame_sistema.pack(fill="both", expand=True)

    def atualizar_dados_loop(self):
        try:
            # Chama a função central do seu módulo backend
            dados = funcoes.atualizar_dados()

            # 1. Atualizar CPU
            cpu_pct = dados.get("cpu", {}).get("uso_percentual", 0)
            self.lbl_cpu_percent.configure(text=f"Uso: {cpu_pct:.1f}%")
            self.progress_cpu.set(cpu_pct / 100)

            # 2. Atualizar Memória
            mem = dados.get("memoria", {})
            mem_pct = mem.get("percentual", 0)
            self.lbl_mem_percent.configure(text=f"Uso: {mem_pct:.1f}%")
            self.progress_mem.set(mem_pct / 100)
            self.lbl_mem_detalhes.configure(
                text=f"Usado: {mem.get('usada_gb', 0)} GB  |  Disponível: {mem.get('disponivel_gb', 0)} GB  |  Total: {mem.get('total_gb', 0)} GB"
            )

            # 3. Atualizar Discos Dinamicamente
            armazenamento = dados.get("armazenamento", [])
            for widget in self.frame_disco.winfo_children():
                widget.destroy()

            ctk.CTkLabel(
                self.frame_disco,
                text="Unidades de Armazenamento",
                font=ctk.CTkFont(size=20, weight="bold"),
            ).pack(anchor="w", padx=10, pady=(10, 15))

            if isinstance(armazenamento, list):
                for d in armazenamento:
                    card_d = ctk.CTkFrame(self.frame_disco, corner_radius=8)
                    card_d.pack(fill="x", padx=10, pady=6)

                    ctk.CTkLabel(
                        card_d,
                        text=f"Unidade: {d.get('unidade', '')}",
                        font=ctk.CTkFont(weight="bold"),
                    ).pack(anchor="w", padx=15, pady=(10, 2))

                    ctk.CTkLabel(
                        card_d,
                        text=f"{d.get('usado_gb', 0)} GB usados de {d.get('total_gb', 0)} GB ({d.get('livre_gb', 0)} GB livres)",
                        text_color="gray70",
                    ).pack(anchor="w", padx=15)

                    p_bar = ctk.CTkProgressBar(card_d, height=10)
                    p_bar.pack(fill="x", padx=15, pady=(5, 12))
                    pct = d.get("percentual", 0)
                    p_bar.set(pct / 100)

                    if pct > 85:
                        p_bar.configure(progress_color="#EF4444")
                    else:
                        p_bar.configure(progress_color="#3B82F6")

        except Exception as e:
            print(f"Erro ao atualizar dados: {e}")

        # Repete a execução a cada 3 segundo (3000 ms)
        self.after(3000, self.atualizar_dados_loop)


if __name__ == "__main__":
    app = GerenciadorDeTarefasFront()
    app.mainloop()