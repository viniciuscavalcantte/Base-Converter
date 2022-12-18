import tkinter as tk

# Função chamada quando o botão é clicado
def converter():
  # Obtém o número, a base de origem e a base destino informados pelo usuário
  numero = numero_entry.get()
  base_origem = int(base_origem_entry.get())
  base_destino = int(base_destino_entry.get())

  # Realiza a conversão do número da base de origem para a base destino
  numero_convertido = int(numero, base_origem)

  # Realiza a conversão do número convertido para a base destino
  if base_destino == 2:
    resultado = bin(numero_convertido)[2:]
  elif base_destino == 8:
    resultado = oct(numero_convertido)[2:]
  elif base_destino == 16:
    resultado = hex(numero_convertido)[2:]
  else:
    resultado = str(numero_convertido)

  resultado_texto.insert(tk.END, "O número {} na base {} é igual a {} na base {}.\n".format(numero, base_origem, resultado, base_destino))

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora de bases numéricas")

# Cria os campos de texto para informar o número, a base de origem e a base destino
numero_label = tk.Label(janela, text="Número:")
numero_label.pack()
numero_entry = tk.Entry(janela)
numero_entry.pack()
base_origem_label = tk.Label(janela, text="Base de origem:")
base_origem_label.pack()
base_origem_entry = tk.Entry(janela)
base_origem_entry.pack()
base_destino_label = tk.Label(janela, text="Base destino:")
base_destino_label.pack()
base_destino_entry = tk.Entry(janela)
base_destino_entry.pack()

# Cria o botão para realizar a conversão
converter_botao = tk.Button(janela, text="Converter", command=converter)
converter_botao.pack()

# Cria a área de texto para exibir o resultado
resultado_texto = tk.Text(janela)
resultado_texto.pack()

# Inicia a janela principal
janela.mainloop()

