from vpython import *
# Desenho do plano 
plano = box(pos=vector(0, -0.5, 0), size=vector(10, 0.1, 10), color=color.white)

# A função sphere desenha as esferas (bolinhas). Só precisa passa a posição e o raio
bola1 = sphere(pos=vector(-1, 0, 0), radius=0.5, color=color.blue, mass=10)
bola2 = sphere(pos=vector(1, 0, 0), radius=0.5, color=color.green, mass=15)

# Velocidades iniciais das bolinhas
bola1.velocity = vector(0.1, 0, 0)
bola2.velocity = vector(-0.1, 0, 0)

# Aqui é a função para verificar a colisao entre as bordas do plano e as bolinhas
def colisao_bolas_planos(bola1, bola2, plano):
    if (bola1.pos.x < -plano.size.x / 2 + bola1.radius) or (bola1.pos.x > - bola1.radius + plano.size.x / 2):
        bola1.velocity *= -1 
    if (bola2.pos.x < -plano.size.x / 2 + bola2.radius) or (bola2.pos.x > plano.size.x / 2 - bola2.radius):
        bola2.velocity *= -1

# Função para colisão entre as bolas
def colisao_elastica(bola1, bola2):
    velocidade1 = (bola1.velocity.x * (bola1.mass - bola2.mass) + 2 * bola2.velocity.x * bola2.mass) / (bola1.mass + bola2.mass)
    velocidade2 = (bola2.velocity.x * (bola2.mass - bola1.mass) + 2 * bola1.velocity.x * bola1.mass) / (bola1.mass + bola2.mass)
    #    bola1.velocity *= -1
    #    bola2.velocity *= -1
    return velocidade1, velocidade2

# Aqui no loop  while é que a magia acontece (Animação)
while True:
    rate(60)  # Limita a taxa de atualização para 60 quadros por segundo

    # Atualiza as posições das bolinhas
    bola1.pos.x += bola1.velocity.x
    bola2.pos.x += bola2.velocity.x

    # Estas são as codições de colisão nas bodas do plano
    colisao_bolas_planos(bola1,bola2, plano)  
    # E estas aaqui são as coidções de colisões entre as bolinhas
    if mag(bola1.pos - bola2.pos) < 2 * bola1.radius:
        bola1.velocity.x, bola2.velocity.x = colisao_elastica(bola1, bola2)