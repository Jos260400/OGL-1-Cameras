#Universidad del Valle de Guatemala
#Graficas por Computadoras
#Fernando José Garavito Ovando 18071
#OGL 1: Cameras

#Import
import pygame
from pygame.locals import *
from gl import Renderer
import shaders

deltaTime = 0.0

pygame.init()
clock = pygame.time.Clock()
screensize = (960, 540)
screen = pygame.display.set_mode(screensize, DOUBLEBUF | OPENGL)

r = Renderer(screen)
r.setShaders(shaders.vertex_shader, shaders.fragment_shader)
r.createobjects()

cubo1 = 0
cubo2 = 0

isRunning = True
while isRunning:

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        cubo1 -= 2 * deltaTime
    if keys[pygame.K_d]:
        cubo1 += 2 * deltaTime
    if keys[pygame.K_w]:
        cubo2 -= 2 * deltaTime
    if keys[pygame.K_s]:
        cubo2 += 2 * deltaTime

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode
            elif ev.key == pygame.K_ESCAPE:
                isRunning = False

    r.translatecube(cubo1, 0, cubo2)

    r.render()
    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000

pygame.quit()
