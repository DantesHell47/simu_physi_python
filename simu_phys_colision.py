from vpython import *
# Desenho do plano 
plano = box(pos=vector(0, -0.5, 0), size=vector(10, 0.1, 10), color=color.white)

# A função sphere desenha as esferas (bolinhas). Só precisa passa a posição e o raio
bola1 = sphere(pos=vector(-1, 0, 0), radius=0.5, color=color.blue)
bola2 = sphere(pos=vector(1, 0, 0), radius=0.5, color=color.green)


# Velocidades iniciais das bolinhas
bola1.velocity = vector(0.1, 0, 0)
bola2.velocity = vector(-0.1, 0, 0)

# Aqui no loop  while é que a magia acontece (Animação)
while True:
    rate(60)  # Limita a taxa de atualização para 60 quadros por segundo

    # Atualiza as posições das bolinhas
    bola1.pos += bola1.velocity
    bola2.pos += bola2.velocity

    # Estas são as codições de colisão nas bodas do plano

    if (bola1.pos.x < -plano.size.x / 2 + bola1.radius) or (bola1.pos.x > - bola1.radius + plano.size.x / 2):
        bola1.velocity *= -1 
    if (bola2.pos.x < -plano.size.x / 2 + bola2.radius) or (bola2.pos.x > plano.size.x / 2 - bola2.radius):
        bola2.velocity *= -1 
    
    # E estas aaqui são as coidções de colisões entre as bolinhas
    
    if mag(bola1.pos - bola2.pos) < 2 * bola1.radius:
        bola1.velocity *= -1
        bola2.velocity *= -1