# Kayo Xavier Nascimento Cavalcante Leite - 21.2.4095

def rgb_to_cmyk():
    try:
        r = int(input("Digite o valor de R (0-255): "))
        g = int(input("Digite o valor de G (0-255): "))
        b = int(input("Digite o valor de B (0-255): "))
    except ValueError:
        print("Por favor, insira números inteiros.")
        return
    print(f"Convertendo a cor RGB({r}, {g}, {b}) para o modelo CMYK...")
    # Normaliza os valores para a faixa [0, 1]
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    # Calcula o valor de K (preto)
    k = 1 - max(r_norm, g_norm, b_norm)
    if k == 1:
        c = m = y = 0
    else:
        c = (1 - r_norm - k) / (1 - k)
        m = (1 - g_norm - k) / (1 - k)
        y = (1 - b_norm - k) / (1 - k)
    print(f"CMYK: C={c:.2f}, M={m:.2f}, Y={y:.2f}, K={k:.2f}")
    return 

def main():
    rgb_to_cmyk()
      

if __name__ == '__main__':
    main()
