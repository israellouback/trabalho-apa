from PIL import Image, ImageDraw, ImageFont
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def plota_matriz(matrix):
    # Configurações da imagem
    cell_size = 50  # pixels
    font_size = 20
    num_rows, num_cols = matrix.shape
    image_width = (num_cols + 1) * cell_size #tamanhos
    image_height = (num_rows + 1) * cell_size #tamanhos

    img = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', font_size)
    index_color = 'blue'

    for j in range(num_cols): #labels no topo
        x = (j + 1) * cell_size
        text = f'V{j + 1}'
        text_bbox = draw.textbbox((x, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = x + (cell_size - text_width) / 2
        text_y = (cell_size - text_height) / 2
        draw.text((text_x, text_y), text, fill=index_color, font=font)

    for i in range(num_rows): #labels na esquerda
        y = (i + 1) * cell_size
        text = f'V{i + 1}'
        text_bbox = draw.textbbox((0, y), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = (cell_size - text_width) / 2
        text_y = y + (cell_size - text_height) / 2
        draw.text((text_x, text_y), text, fill=index_color, font=font)

    for i in range(num_rows): #desenho da matriz
        for j in range(num_cols):
            x = (j + 1) * cell_size
            y = (i + 1) * cell_size
            draw.rectangle([x, y, x + cell_size, y + cell_size], outline='black') #formato dos retangulos
            text = str(matrix[i, j])
            text_bbox = draw.textbbox((x, y), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_x = x + (cell_size - text_width) / 2
            text_y = y + (cell_size - text_height) / 2
            draw.text((text_x, text_y), text, fill='black', font=font)

    
    for i in range(num_rows + 1): #colunas dos índices
        draw.line([(0, i * cell_size), (image_width, i * cell_size)], fill='black')

    for j in range(num_cols + 1): #colunas dos índices
        draw.line([(j * cell_size, 0), (j * cell_size, image_height)], fill='black')

    img.save('matriz_adjacencia.png')
    img.show()


def plota_vetor(vetor, FLAG):
    cell_size = 50  # pixels
    font_size = 20
    num_rows = len(vetor)  # tamanho do vetor
    
    max_values_per_row = 100  #valores por linha
    num_cols = (num_rows + max_values_per_row - 1) // max_values_per_row  
    
    image_width = cell_size * max_values_per_row  #tamanho imagem
    image_height = cell_size * (num_cols + 1) 

    img = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', font_size)


    for col in range(max_values_per_row): #desenho indices
        x = col * cell_size  
        y = 0  
        draw.rectangle([x, y, x + cell_size, y + cell_size], outline='black')

        text = str(col)
        text_bbox = draw.textbbox((x, y), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = x + (cell_size - text_width) / 2
        text_y = y + (cell_size - text_height) / 2
        draw.text((text_x, text_y), text, fill='blue', font=font)

    for idx, valor in enumerate(vetor): #valores do vetor
        row = idx // max_values_per_row  
        col = idx % max_values_per_row   
        x = col * cell_size 
        y = (row + 1) * cell_size 
        draw.rectangle([x, y, x + cell_size, y + cell_size], outline='black')
        text = str(valor)
        text_bbox = draw.textbbox((x, y), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = x + (cell_size - text_width) / 2
        text_y = y + (cell_size - text_height) / 2
        draw.text((text_x, text_y), text, fill='black', font=font)

    for i in range(num_cols + 1):
        draw.line([(0, i * cell_size), (image_width, i * cell_size)], fill='black')  
    for j in range(max_values_per_row + 1):
        draw.line([(j * cell_size, 0), (j * cell_size, image_height)], fill='black')  

    if FLAG == 1:
        img.save('vetor_binario.png')
    else:
        img.save('vetor_compactado.png')
        
    img.show()



