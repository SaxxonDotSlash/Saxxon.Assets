import pygame
import sys
import random
import json

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20
PADDLE_SPEED = 5

# Random initial ball speeds
ball_speed_choices = [i for i in range(-5, 6) if i < -2 or i > 2]
BALL_SPEED_X = random.choice(ball_speed_choices)
BALL_SPEED_Y = random.choice(ball_speed_choices)
BALL_SPEED_INCREMENT = 1

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong Game')

# Paddles and Ball
player_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
bot_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Game states
MAIN_MENU = 0
PLAYING = 1
PAUSED = 2
SCORES = 3
game_state = MAIN_MENU

# Main menu options
main_menu_options = ["Start", "Scores", "Quit"]
selected_main_menu_option = 0

# Pause menu options
pause_options = ["Resume", "Main Menu", "Restart"]
selected_pause_option = 0

# Paddle hit counter
paddle_hit_count = 0

# High scores file path
HIGH_SCORES_FILE = "high_scores.json"

# Load high scores
def load_high_scores():
    try:
        with open(HIGH_SCORES_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save high scores
def save_high_scores(high_scores):
    with open(HIGH_SCORES_FILE, "w") as file:
        json.dump(high_scores, file)

# Initialize high scores
high_scores = load_high_scores()

# Scores
player_score = 0
high_scores = []

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def reset_game():
    global ball, BALL_SPEED_X, BALL_SPEED_Y, paddle_hit_count, player_score
    ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
    BALL_SPEED_X = random.choice(ball_speed_choices)
    BALL_SPEED_Y = random.choice(ball_speed_choices)
    paddle_hit_count = 0
    player_score = 0

def update_high_scores(score):
    global high_scores
    if len(high_scores) < 10 or score > min(high_scores):
        if len(high_scores) >= 10:
            high_scores.remove(min(high_scores))
        high_scores.append(score)
        high_scores = sorted(high_scores, reverse=True)
        save_high_scores(high_scores)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state == MAIN_MENU:
                if event.key == pygame.K_UP:
                    selected_main_menu_option = (selected_main_menu_option - 1) % len(main_menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_main_menu_option = (selected_main_menu_option + 1) % len(main_menu_options)
                elif event.key == pygame.K_RETURN:
                    if main_menu_options[selected_main_menu_option] == "Start":
                        game_state = PLAYING
                    elif main_menu_options[selected_main_menu_option] == "Scores":
                        game_state = SCORES
                    elif main_menu_options[selected_main_menu_option] == "Quit":
                        running = False
            elif game_state == PLAYING:
                if event.key == pygame.K_ESCAPE:
                    game_state = PAUSED
            elif game_state == PAUSED:
                if event.key == pygame.K_ESCAPE:
                    game_state = PLAYING
                elif event.key == pygame.K_UP:
                    selected_pause_option = (selected_pause_option - 1) % len(pause_options)
                elif event.key == pygame.K_DOWN:
                    selected_pause_option = (selected_pause_option + 1) % len(pause_options)
                elif event.key == pygame.K_RETURN:
                    if pause_options[selected_pause_option] == "Resume":
                        game_state = PLAYING
                    elif pause_options[selected_pause_option] == "Main Menu":
                        game_state = MAIN_MENU
                    elif pause_options[selected_pause_option] == "Restart":
                        reset_game()
                        game_state = PLAYING
            elif game_state == SCORES:
                if event.key == pygame.K_ESCAPE:
                    game_state = MAIN_MENU

    if game_state == MAIN_MENU:
        screen.fill(BLACK)
        draw_text('Pong Game', font, WHITE, screen, WIDTH // 2 - 150, HEIGHT // 2 - 150)
        for i, option in enumerate(main_menu_options):
            color = WHITE if i == selected_main_menu_option else (100, 100, 100)
            draw_text(option, small_font, color, screen, WIDTH // 2 - 60, HEIGHT // 2 - 50 + i * 40)
    elif game_state == PLAYING:
        # Player paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_paddle.top > 0:
            player_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
            player_paddle.y += PADDLE_SPEED

        # Bot paddle movement
        if bot_paddle.centery < ball.centery and bot_paddle.bottom < HEIGHT:
            bot_paddle.y += PADDLE_SPEED
        if bot_paddle.centery > ball.centery and bot_paddle.top > 0:
            bot_paddle.y -= PADDLE_SPEED

        # Ball movement
        ball.x += BALL_SPEED_X
        ball.y += BALL_SPEED_Y

        # Ball collision with top and bottom walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            BALL_SPEED_Y = -BALL_SPEED_Y

        # Ball collision with paddles
        if ball.colliderect(player_paddle) or ball.colliderect(bot_paddle):
            BALL_SPEED_X = -BALL_SPEED_X
            paddle_hit_count += 1
            if ball.colliderect(player_paddle):
                player_score += 1
            if paddle_hit_count % 5 == 0:
                BALL_SPEED_X += BALL_SPEED_INCREMENT if BALL_SPEED_X > 0 else -BALL_SPEED_INCREMENT
                BALL_SPEED_Y += BALL_SPEED_INCREMENT if BALL_SPEED_Y > 0 else -BALL_SPEED_INCREMENT

        # Ball out of bounds
        if ball.left <= 0 or ball.right >= WIDTH:
            update_high_scores(player_score)
            reset_game()

        # Drawing
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player_paddle)
        pygame.draw.rect(screen, WHITE, bot_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
        draw_text(f'Score: {player_score}', small_font, WHITE, screen, WIDTH // 2 - 50, 10)
    elif game_state == PAUSED:
        screen.fill(BLACK)
        draw_text('Paused', font, WHITE, screen, WIDTH // 2 - 100, HEIGHT // 2 - 150)
        for i, option in enumerate(pause_options):
            color = WHITE if i == selected_pause_option else (100, 100, 100)
            draw_text(option, small_font, color, screen, WIDTH // 2 - 60, HEIGHT // 2 - 50 + i * 40)
    elif game_state == SCORES:
        screen.fill(BLACK)
        draw_text('High Scores', font, WHITE, screen, WIDTH // 2 - 150, HEIGHT // 2 - 150)
        for i, score in enumerate(high_scores):
            draw_text(f'{i + 1}. {score}', small_font, WHITE, screen, WIDTH // 2 - 60, HEIGHT // 2 - 50 + i * 40)
        draw_text('Press Esc to return', small_font, WHITE, screen, WIDTH // 2 - 120, HEIGHT - 50)

    # Update display
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()