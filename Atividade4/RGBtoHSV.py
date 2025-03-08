import colorsys

def rgb_to_hsv():
    try:
        r = int(input("Digite o valor de R (0-255): "))
        g = int(input("Digite o valor de G (0-255): "))
        b = int(input("Digite o valor de B (0-255): "))
    except ValueError:
        print("Por favor, insira números inteiros.")
        return

    # Normaliza os valores para a faixa [0, 1]
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    h, s, v = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)
    # Converte h para graus e s, v para porcentagem
    h_degrees = h * 360
    s_pct = s * 100
    v_pct = v * 100

    print(f"RGB({r}, {g}, {b}) convertido para HSV: ({h_degrees:.2f}°, {s_pct:.2f}%, {v_pct:.2f}%)")

if __name__ == '__main__':
    print("Iniciando conversão de RGB para HSV...")
    rgb_to_hsv()
    print("Conversão finalizada.")
