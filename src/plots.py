from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Defina a matriz que você deseja converter em uma imagem
def plota_matriz(matrix):

# Configurações da imagem
    cell_size = 50  # Tamanho de cada célula em pixels
    font_size = 20
    num_rows, num_cols = matrix.shape

    # Calcule o tamanho da imagem
    image_width = (num_cols + 1) * cell_size
    image_height = (num_rows + 1) * cell_size

    # Crie uma nova imagem branca
    img = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(img)

    # Carregue uma fonte (pode precisar ajustar o caminho dependendo do seu sistema)
    font = ImageFont.truetype('arial.ttf', font_size)

    # Cor dos índices
    index_color = 'blue'

    # Desenhe os índices das colunas no topo
    for j in range(num_rows):
            x = (j + 1) * cell_size
            text = f'V{j + 1}'
            text_bbox = draw.textbbox((x, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_x = x + (cell_size - text_width) / 2
            text_y = (cell_size - text_height) / 2
            draw.text((text_x, text_y), text, fill=index_color, font=font)

            # Desenhe os índices das linhas à esquerda
            for i in range(num_cols):
                y = (i + 1) * cell_size
                text = f'V{i + 1}'
                text_bbox = draw.textbbox((0, y), text, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]
                text_x = (cell_size - text_width) / 2
                text_y = y + (cell_size - text_height) / 2
                draw.text((text_x, text_y), text, fill=index_color, font=font)

            # Desenhe a matriz na imagem
            for i in range(num_rows):
                for j in range(num_cols):
                    # Calcule as coordenadas da célula
                    x = (j + 1) * cell_size
                    y = (i + 1) * cell_size

                    # Desenhe o retângulo da célula
                    draw.rectangle([x, y, x + cell_size, y + cell_size], outline='black')

                    # Desenhe o número na célula
                    text = str(matrix[i, j])
                    text_bbox = draw.textbbox((x, y), text, font=font)
                    text_width = text_bbox[2] - text_bbox[0]
                    text_height = text_bbox[3] - text_bbox[1]
                    text_x = x + (cell_size - text_width) / 2
                    text_y = y + (cell_size - text_height) / 2
                    draw.text((text_x, text_y), text, fill='black', font=font)

            # Desenhe a linha e a coluna de índices (borda)
            for i in range(num_rows + 1):
                draw.line([(0, i * cell_size), (image_width, i * cell_size)], fill='black')

            for j in range(num_cols + 1):
                draw.line([(j * cell_size, 0), (j * cell_size, image_height)], fill='black')

            # Salve a imagem
            img.save('matriz_adjacencia.png')

            # Exiba a imagem (opcional)
            img.show()

def plota_vetor(vetor,FLAG):
    # Configurações da imagem
    cell_size = 50  # Tamanho de cada célula em pixels
    font_size = 20
    num_rows = len(vetor)  # Número de elementos no vetor (4950)
    
    # Definimos o número de colunas para dividir o vetor em múltiplas colunas para melhor visualização
    max_rows_per_col = 100  # Limite de linhas por coluna para não gerar uma imagem muito longa
    num_cols = (num_rows + max_rows_per_col - 1) // max_rows_per_col  # Calcula o número de colunas necessárias
    
    # Calcule o tamanho da imagem
    image_width = num_cols * cell_size  # Cada coluna tem uma célula
    image_height = min(num_rows, max_rows_per_col) * cell_size  # Cada célula é de tamanho fixo

    # Crie uma nova imagem branca
    img = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(img)

    # Carregue uma fonte (pode precisar ajustar o caminho dependendo do seu sistema)
    font = ImageFont.truetype('arial.ttf', font_size)

    # Desenhe o vetor na imagem, dividindo-o em colunas para evitar que a imagem seja muito alta
    for idx, valor in enumerate(vetor):
        col = idx // max_rows_per_col  # Determina a coluna onde o valor será colocado
        row = idx % max_rows_per_col   # Determina a linha dentro da coluna
        
        x = col * cell_size  # Posição x
        y = row * cell_size  # Posição y

        # Desenhe o retângulo da célula
        draw.rectangle([x, y, x + cell_size, y + cell_size], outline='black')

        # Desenhe o valor dentro da célula
        text = str(valor)
        text_bbox = draw.textbbox((x, y), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = x + (cell_size - text_width) / 2
        text_y = y + (cell_size - text_height) / 2
        draw.text((text_x, text_y), text, fill='black', font=font)

    # Desenhar linhas de grade
    for i in range(min(num_rows, max_rows_per_col) + 1):
        draw.line([(0, i * cell_size), (image_width, i * cell_size)], fill='black')

    for j in range(num_cols + 1):
        draw.line([(j * cell_size, 0), (j * cell_size, image_height)], fill='black')

    # Salve a imagem
    if FLAG == 1:
        img.save('vetor_binario.png')
    else:
        img.save('vetor_compactado.png')

    # Exiba a imagem (opcional)
    img.show()





