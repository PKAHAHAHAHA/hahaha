import pygame
import sys

# 初始化 Pygame
pygame.init()

# 設定視窗大小
width, height = 600, 400

# 建立視窗
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Example")

# 設定方塊初始位置和速度
x, y = 50, 50
speed = 5

# 遊戲迴圈
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 檢測按鍵輸入
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # 清除畫面
    screen.fill((255, 255, 255))

    # 繪製方塊
    pygame.draw.rect(screen, (0, 128, 255), (x, y, 50, 50))

    # 更新畫面
    pygame.display.flip()

    # 控制遊戲迴圈更新速率
    pygame.time.Clock().tick(30)


