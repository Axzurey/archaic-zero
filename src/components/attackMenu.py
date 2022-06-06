from struct import calcsize
import pygame
import client.renderCycle as renderCycle
from game import  createButton, createEntity, createFrame
from modules.quark import fromUdim
from modules.udim2 import udim2

def createAttackMenu():

    attackBar = createFrame(udim2.fromOffset(0, 0), udim2.fromScale(.7, .5))

    attack1 = createButton(udim2.fromScale(.1, .2), udim2.fromScale(.5, .5), 'HELLO WORLD!', attackBar)

    attack1.backgroundColor = '#BAD6FF'

    attack1.textColor = '#000000'

    attack1.backgroundColorHover = "#00FFFF"

    attack1.shape = 'rounded_rectangle'

    attack1.cornerRadius = 5

    attack1.borderWidth = 2

    attack1.fontSize = 15

    print('FINE', attack1.parent, attackBar.parent, attack1.children, attackBar.children)
    #<modules.gui.guiFrame.guiFrame object at 0x000001CC81CCFB50> <modules.gui.guiFrame.guiFrame object at 0x000001CC81CCFB50> 
    # [<modules.gui.textButton.textButton object at 0x000001CC81D11300>] [<modules.gui.textButton.textButton object at 0x000001CC81D11300>]

    #this is wrong. fix whatever is happening!

    