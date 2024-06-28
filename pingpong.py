import pygame
import random

# Initialisation de Pygame
pygame.init()


# Paramètres de la fenêtre
info = pygame.display.Info()
screen_height = info.current_h - 150
screen_width = screen_height * 0.6
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ping pong")

FPS = 60
BOT = 14 * 30 / FPS * screen_height // 1000
POINTS = 2
POLICE = "C:/Users/marti/Dropbox/Codage/Python/nasalization-rg.otf"

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 150, 255)

# Paramètres du joueur 1 
player1_width = 100 * screen_height // 1000
player1_height = 20 * screen_height // 1000
player1_x = (screen_width - player1_width) // 2
player1_y = 110 * screen_height // 1000
player1_speed = 30 * screen_height // 1000 * 30 / FPS

# Paramètres du joueur 2 
player2_width = 100 * screen_height // 1000
player2_height = 20 * screen_height // 1000
player2_x = (screen_width - player2_width) // 2
player2_y = screen_height - player2_height - 10 * screen_height // 1000
player2_speed = 30 * screen_height // 1000 * 30 / FPS

# Paramètres de l'objet
object_width = 30 * screen_height // 1000
object_height = 30 * screen_height // 1000
object_x = (screen_width - object_width) // 2
object_y = (screen_width - object_width) // 2
object_speed = 10 * screen_height // 1000 * 30 / FPS
object_random = 0 
collision = 0 
sol = 0

# Score et vies
score = 0
lives = 3
blueScore = 0
redScore = 0
maxScore = 0 

rota1 = -7 * 30 // FPS
rota2 = 7 * 30 // FPS

choiceScreen = True 
choice = 0 
choice0Color = WHITE
choice1Color = WHITE
choice2Color = WHITE
click = 0 

attente = 0 

# Affichage de l'écran d'accueil
while choiceScreen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            choiceScreen = False

    screen.fill(BLACK)
    font = pygame.font.Font(POLICE, 35 * screen_height // 1000)
    accueil = font.render("PING PONG", True, WHITE)
    instructions1 = font.render("rouge : utilisez Q et D", True, WHITE)
    instructions2 = font.render("bleu : utilsez les fleches", True, WHITE)
    choix0 = font.render("0 joueur", True, choice0Color)
    choix1 = font.render("1 joueur", True, choice1Color)
    choix2 = font.render("2 joueurs", True, choice2Color)
    confirmation = font.render("utilisez espace pour confimer", True, WHITE)
    screen.blit(accueil, (200 * screen_height // 1000, 200 * screen_height // 1000))
    screen.blit(instructions1, (110 * screen_height // 1000, 300 * screen_height // 1000))
    screen.blit(instructions2, (110 * screen_height // 1000, 350 * screen_height // 1000))
    screen.blit(choix0, (210 * screen_height // 1000, 450 * screen_height // 1000))
    screen.blit(choix1, (210 * screen_height // 1000, 500 * screen_height // 1000))
    screen.blit(choix2, (210 * screen_height // 1000, 550 * screen_height // 1000))
    screen.blit(confirmation, (50 * screen_height // 1000, 700 * screen_height // 1000))
    keys = pygame.key.get_pressed()
    if click > 0: 
        click -= 1 
    if click <= 0: 
        if keys[pygame.K_UP]: 
            choice -= 1
            click = 50 
        if keys[pygame.K_DOWN]: 
            choice += 1
            click = 50 
    if keys[pygame.K_SPACE]: 
        choiceScreen = False
    if choice > 2: 
        choice = 0 
    if choice < 0: 
        choice = 2 
    if choice == 0: 
        choice0Color = RED
        choice1Color = WHITE
        choice2Color = WHITE
    if choice == 1: 
        choice0Color = WHITE
        choice1Color = RED
        choice2Color = WHITE
    if choice == 2: 
        choice0Color = WHITE
        choice1Color = WHITE
        choice2Color = RED
        
    pygame.display.update()


# Boucle principale du jeu
running = True
clock = pygame.time.Clock()
verification = 0 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    # MOUVEMENT DES JOUEURS 
    if choice == 1 or choice == 2:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player2_x > 0:
            player2_x -= player2_speed
        if keys[pygame.K_RIGHT] and player2_x < (screen_width - player2_width):
            player2_x += player2_speed 

    if choice == 2:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and player1_x > 0:
            player1_x -= player1_speed
        if keys[pygame.K_d] and player1_x < screen_width - player1_width:
            player1_x += player1_speed 


    # mouse_pos = pygame.mouse.get_pos()
    # mouse_x, mouse_y = mouse_pos
    # player_x = mouse_x

    if object_x > 570 * screen_height // 1000 or object_x < 0:
        if object_random > 0:
            object_random = (-object_random)

    if object_x < 0:
        if object_random < 0: 
            object_random = (-object_random)

    # Mouvement de l'objet
    object_y += object_speed
    object_x += object_random
    # TAS 
    # player1_x = player2_x = (object_x - object_width)

    # BOT 
    if choice == 0 or choice == 1: 
        if (object_x - 30 * screen_height // 1000 < player1_x): 
            player1_x -= BOT
        if (object_x - 30 * screen_height // 1000 > player1_x): 
            player1_x += BOT
    if choice == 0:
        if (object_x - 30 * screen_height // 1000 < player2_x): 
            player2_x -= BOT
        if (object_x - 30 * screen_height // 1000 > player2_x): 
            player2_x += BOT

    #  
    # Vérifier si l'objet touche le joueur 2
    if (collision == 0):
        if (player2_x < object_x < player2_x + player2_width or player2_x < object_x + object_width < player2_x + player2_width) and object_y + object_height > player2_y:
            if (object_speed < 60 * screen_height // 1000 * 30 / FPS):
                object_speed += 1 * screen_height / 1000 * 30 / FPS
            object_speed = (-object_speed)
            object_random += random.randint(rota1, rota2) * screen_height / 1000
            score += 1
            collision = 7 *  FPS // 30
            

        if (player1_x < object_x < player1_x + player1_width or player1_x < object_x + object_width < player1_x + player1_width) and object_y - object_height < player1_y:
            if (object_speed > -60 * screen_height // 1000 * 30 / FPS):
                object_speed -= 1 * screen_height / 1000 * 30 / FPS
            object_speed = (-object_speed)
            object_random += random.randint (rota1, rota2) * screen_height / 1000
            score += 1
            collision = 7 * FPS // 30
            

    if (collision > 0): 
        collision -= 1 

    if sol > 0:
        sol -= 1

    if attente >= 0: 
        attente -= 1 
    # Vérifier si l'objet touche le sol
    # if (verification % 10 != 0):
    if sol <= 0:
        if object_y > screen_height :
            redScore += 1
            player1_x = (screen_width - player1_width) // 2
            player2_x = (screen_width - player2_width) // 2
            sol = 40
            object_x = (screen_width - object_width) // 2
            object_y = (screen_width - object_width) // 2
            object_speed = 10 * screen_height // 1000 * 30 / FPS
            object_random = 0
            if (score > maxScore): 
                maxScore = score 
            score = 0 
            attente = 2
            if attente == 0: 
                pygame.time.delay (1000) 

        if object_y - 90 * screen_height // 1000 < -object_height :
            blueScore += 1
            player1_x = (screen_width - player1_width) // 2
            player2_x = (screen_width - player2_width) // 2
            sol = 40 
            object_x = (screen_width - object_width) // 2
            object_y = (screen_width - object_width) // 2
            object_speed = -10 * screen_height // 1000 * 30 / FPS
            object_random = 0
            if (score > maxScore): 
                maxScore = score 
            score = 0 
            attente = 1 
            if attente == 1: 
                pygame.time.delay (1000) 

        

    # Vérifier si le jeu est terminé
    if (verification % 25 == 0):
        if ((redScore >= POINTS) or (blueScore >= POINTS)):
            if (blueScore - redScore >= 2 or redScore - blueScore >= 2):
                screen.fill(BLACK)
                font = pygame.font.Font(POLICE, 50 * screen_height // 1000)
                score_text = font.render(f"Score max : {maxScore}", True, WHITE)
                score_red = font.render(f"Rouge : {redScore}", True, WHITE)
                score_blue = font.render(f"Bleu : {blueScore}", True, WHITE)
                screen.blit(score_text, (screen_width // 2 - 150 * screen_height // 1000, screen_height // 2 - 80 * screen_height // 1000))
                screen.blit(score_red, (screen_width // 2 - 150 * screen_height // 1000, screen_height // 2 -20 * screen_height // 1000))
                screen.blit(score_blue, (screen_width // 2 - 150 * screen_height // 1000, screen_height // 2 + 40 * screen_height // 1000))
                pygame.display.update()
                pygame.time.delay (5000)
                if (blueScore > redScore):
                    player2_width -= 20 * screen_height // 1000
                if (blueScore < redScore):
                    player1_width -= 20 * screen_height // 1000
                player1_x = (screen_width - player1_width) // 2
                player2_x = (screen_width - player2_width) // 2
                blueScore = 0
                redScore = 0
                if (player2_width <= 40 * screen_height // 1000):
                    screen.fill(BLACK) 
                    font = pygame.font.Font(POLICE, 75 * screen_height // 1000)
                    score_text = font.render(f"Bleu gagne", True, WHITE)
                    screen.blit(score_text, (screen_width // 2 - 150 * screen_height // 1000, screen_height // 2 -20 * screen_height // 1000))
                    pygame.display.update()
                    pygame.time.delay (5000)
                    running = False
                if (player1_width <= 40 * screen_height // 1000): 
                    screen.fill(BLACK) 
                    font = pygame.font.SysFont(None, 75)
                    score_text = font.render(f"Rouge gagne", True, WHITE)
                    screen.blit(score_text, (screen_width // 2 - 150 * screen_height // 1000, screen_height // 2 -20 * screen_height // 1000))
                    pygame.display.update()
                    pygame.time.delay (5000)
                    running = False

                
            # running = False

    # Affichage des éléments à l'écran
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (player2_x, player2_y, player2_width, player2_height))
    pygame.draw.rect(screen, RED, (player1_x, player1_y, player1_width, player1_height))
    pygame.draw.rect(screen, WHITE, (object_x, object_y, object_width, object_height))
    pygame.draw.rect(screen, WHITE, (0, 90 * screen_height // 1000, 600 * screen_height // 1000, 5 * screen_height // 1000))

    # Affichage du score et des vies
    if (verification % 25 == 0):
        font = pygame.font.Font(POLICE, 35 * screen_height // 1000)
        score_text = font.render(f"Score: {score}", True, WHITE)
        score_red = font.render(f"Rouge: {redScore}", True, WHITE)
        score_blue = font.render(f"Bleu: {blueScore}", True, WHITE)
    screen.blit(score_text, (210 * screen_height // 1000, 10 * screen_height // 1000))
    screen.blit(score_red, (30 * screen_height // 1000, 50 * screen_height // 1000))
    screen.blit(score_blue, (400 * screen_height // 1000, 50 * screen_height // 1000))
    verification += 1
    
    if (verification > 25):
        verification = 0 

    pygame.display.flip()
    clock.tick(FPS)

print(maxScore)
pygame.quit()