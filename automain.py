import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from login import login
from centro_custo import acessar_centro_custo
from pdf_excel import converter_pdf_para_excel

# Função para iniciar o processo
def iniciar_processo():
    user_esst = user_esst_entry.get()
    senha = senha_entry.get()
    cc_list = cc_entry.get().split(',')
    dt_inicial = dt_inicial_entry.get()
    dt_final = dt_final_entry.get()
    email = "Email ESST"
    chrome_driver_path = 'chromedriver\chromedriver.exe'

    if not (user_esst and senha and cc_list and dt_inicial and dt_final):
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
        return

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = Service(executable_path=chrome_driver_path)
    
    try:
        log_text.insert(tk.END, "Iniciando WebDriver...\n")
        driver = webdriver.Chrome(service=service, options=options)
        log_text.insert(tk.END, "Realizando login...\n")
        login(driver, email, user_esst, senha)

        for cc in cc_list:
            log_text.insert(tk.END, f"Acessando centro de custo: {cc.strip()}\n")
            acessar_centro_custo(driver, cc.strip(), dt_inicial, dt_final)
            converter_pdf_para_excel(driver)
            log_text.insert(tk.END, f"Centro de custo {cc.strip()} processado com sucesso.\n")

    except Exception as e:
        log_text.insert(tk.END, f"Erro: {e}\n")
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
    finally:
        driver.quit()
        log_text.insert(tk.END, "WebDriver encerrado.\n")

# Criando a interface principal
root = tk.Tk()
root.title("Relatório ASO'S - ESST")
root.geometry("600x500")
root.configure(bg="darkgrey")

# Título estilizado
titulo = tk.Label(root, text="Robo José", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Frame para entradas
frame_inputs = ttk.LabelFrame(root, text="Dados de Entrada")
frame_inputs.pack(fill="x", padx=10, pady=10)

# Campos de entrada
ttk.Label(frame_inputs, text="Usuário ESST:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
user_esst_entry = ttk.Entry(frame_inputs, width=30)
user_esst_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="Senha:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
senha_entry = ttk.Entry(frame_inputs, show="*", width=30)
senha_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="Centros de Custo (separados por vírgulas):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
cc_entry = ttk.Entry(frame_inputs, width=50)
cc_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="Data Inicial:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
dt_inicial_entry = ttk.Entry(frame_inputs, width=20)
dt_inicial_entry.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="Data Final:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
dt_final_entry = ttk.Entry(frame_inputs, width=20)
dt_final_entry.grid(row=4, column=1, padx=5, pady=5)

# Botão para iniciar o processo
start_btn = ttk.Button(root, text="Iniciar Processo", command=iniciar_processo)
start_btn.pack(pady=10)

# Área de logs
log_frame = ttk.LabelFrame(root, text="Logs")
log_frame.pack(fill="both", expand=True, padx=10, pady=10)
log_text = tk.Text(log_frame, height=15)
log_text.pack(fill="both", expand=True, padx=5, pady=5)

root.mainloop()
