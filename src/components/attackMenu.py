from struct import calcsize
import pygame
import client.renderCycle as renderCycle
from game import  createButton, createEntity, createFrame, createImage
from modules.udim2 import udim2
from worldClass import worldRoot

def createAttackMenu():

    attackBar = createFrame(udim2.fromScale(.75, .75), udim2.fromScale(.2, .2), worldRoot)

    attackBar.backgroundColor = '#00FFFF' #NOT WORKING!

    attack1 = createButton(udim2.fromScale(0, 0), udim2.fromScale(.35, .2), 'HELLO WORLD!', attackBar)

    attack1.backgroundColor = '#BAD6FF'

    attack1.textColor = '#000000'

    attack1.backgroundColorHover = "#00FFFF"

    attack1.font = 'fasterOne'

    attack1.shape = 'rounded_rectangle'

    attack1.cornerRadius = 5

    attack1.borderWidth = 2

    attack1.fontSize = 25

    attack1.text = 'THIS IS MY ATTACK!'

    topBar = createFrame(udim2.fromOffset(0, 0), udim2.fromScale(1, .1), worldRoot)

    topBar.backgroundColor = '#3f3f3f'

    topBar.transparency = 1

    enemyImage = createImage(udim2.fromScale(.2, .5), udim2.fromOffset(50, 50)), 'src/images/enemy.png', topBar)

   # print(attackBar.parent, attackBar.children)

   # print(attack1.parent, attack1.children)

   # print(worldRoot.children)
    