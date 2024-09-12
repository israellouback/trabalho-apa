from PIL import Image, ImageDraw, ImageFont
import numpy as np
import graph

# Defina a matriz que você deseja converter em uma imagem
def plota_matriz(matrix):
# matrix = graph.matriz_binaria_adjacencia()

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
    for j in range(num_cols):
            x = (j + 1) * cell_size
            text = f'V{j + 1}'
            text_bbox = draw.textbbox((x, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_x = x + (cell_size - text_width) / 2
            text_y = (cell_size - text_height) / 2
            draw.text((text_x, text_y), text, fill=index_color, font=font)

            # Desenhe os índices das linhas à esquerda
            for i in range(num_rows):
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
            img.save('matrix_with_colored_indices.png')

            # Exiba a imagem (opcional)
            img.show()



