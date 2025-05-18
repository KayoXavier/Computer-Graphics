# Kayo Xavier Nascimento Cavalcante Leite - 21.2.4095

def rgb_to_hsv():
    try:
        r = int(input("Digite o valor de R (0-255): "))
        g = int(input("Digite o valor de G (0-255): "))
        b = int(input("Digite o valor de B (0-255): "))
    except ValueError:
        print("Entrada inválida! Por favor, insira números inteiros.")
        return None

    # Normaliza os valores para a faixa [0, 1]
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0
    print(f"Valores normalizados: r={r_norm:.2f}, g={g_norm:.2f}, b={b_norm:.2f}")

    # Calcula o máximo, mínimo e a diferença (delta)
    cmax = max(r_norm, g_norm, b_norm)
    cmin = min(r_norm, g_norm, b_norm)
    delta = cmax - cmin
    print(f"Cmax={cmax:.2f}, Cmin={cmin:.2f}, Delta={delta:.2f}")

    # Calcula o Hue (H)
    if delta == 0:
        h = 0
        print("Delta é 0, definindo H = 0°")
    elif cmax == r_norm:
        h = 60 * (((g_norm - b_norm) / delta) % 6)
        print("R é o valor máximo, calculando H para o caso R")
    elif cmax == g_norm:
        h = 60 * (((b_norm - r_norm) / delta) + 2)
        print("G é o valor máximo, calculando H para o caso G")
    elif cmax == b_norm:
        h = 60 * (((r_norm - g_norm) / delta) + 4)
        print("B é o valor máximo, calculando H para o caso B")

    # Calcula a Saturação (S)
    if cmax == 0:
        s = 0
        print("Cmax é 0, definindo S = 0")
    else:
        s = delta / cmax
        print(f"Calculado S = {s:.2f}")

    # O Value (V) é o valor máximo
    v = cmax
    print(f"Calculado V = {v:.2f}")

    print(f"\nRGB convertido para HSV:")
    print(f"H = {h:.2f}°")
    print(f"S = {s*100:.2f}%")
    print(f"V = {v*100:.2f}%")
    return h, s, v

def main():
    rgb_to_hsv()
   

if __name__ == '__main__':
    main()
