from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()
Sky()

# Lista de blocos disponíveis
block_textures = ['grass.png', 'stone.jpg', 'brick.png', 'dirt.png']
selected_block = 0  # Começa com o bloco de grama

boxes = []
for i in range(20):
    for j in range(20):
        box = Button(color=color.white, model='cube', position=(j,0,i),
                     texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(box)

def input(key):
    global selected_block

    # Mudar bloco selecionado
    if key == '1':
        selected_block = 0
    if key == '2':
        selected_block = 1
    if key == '3':
        selected_block = 2
    if key == '4':
        selected_block = 3

    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                             texture=block_textures[selected_block], parent=scene, origin_y=0.5)
                boxes.append(new)
            if key == 'right mouse down':
                boxes.remove(box)
                destroy(box)

def update():
    if player.y < -10:
        player.position = (10, 10, 10)

app.run()
