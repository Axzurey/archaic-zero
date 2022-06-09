import time
from pygame import Vector2
import pygame
from circ.thrd import createThread
import client.renderCycle as renderCycle
from data.exposed import addEntity, addSprite
from modules.entity import entity
from modules.gui.guiFrame import guiFrame
from modules.gui.textLabel import textLabel
from modules.gui.textButton import textButton
from modules.models.playerEntity import playerEntity
from modules.sprite import sprite
from modules.udim2 import udim2
from worldClass import worldRoot
import client.uiService as uiService

spriteGroups = {
    'worldModel': pygame.sprite.Group(),
    'character': pygame.sprite.Group(),
    'otherEntities': pygame.sprite.Group()
}

updatableUI = {

}

entities: dict[str, entity] = {}

sprites: dict[str, sprite] = {}

lastupd = time.time()

def drawAllSpriteGroups():

    global lastupd

    for v in spriteGroups.values():
        v.update(spriteGroups)

    screenCol = (255, 0, 255)
    screen = renderCycle.getScreen()

    screen.fill(screenCol)

    for v in spriteGroups.values():
        v.draw(renderCycle.getScreen())

    lastupd = time.time()

    worldRoot.update(time.time() - lastupd, renderCycle.lastEvents) #cause of jitters

    pygame.display.flip()

renderCycle.addTaskToRenderCycle(drawAllSpriteGroups, 'process:drawAllSpriteGroups')

def createPlayer(position: Vector2, size: Vector2, imagePath: str):
    plr = playerEntity(position, size, imagePath)

    addEntity(plr.id, plr)

    entities[plr.id] = plr

    spriteGroups['character'].add(plr.sprite)

    renderCycle.addTaskToRenderCycle(plr.update, f'{plr.id}:update')

    return plr

def createEntity(position: Vector2, size: Vector2, imagePath: str):
    ent = entity(position, size, imagePath)

    addEntity(ent.id, ent)

    entities[ent.id] = ent

    spriteGroups['otherEntities'].add(ent.sprite)

    return ent

def createSprite(position: Vector2, size: Vector2, imagePath: str) -> sprite:
    s = sprite(position, size, imagePath)
    sprites[s.id] = s

    addSprite(s.id, s)

    #renderCycle.addTaskToRenderCycle(s.draw, f'{s.id}:draw')
    return s

def createFrame(position: udim2, size: udim2, parent) -> guiFrame:
    t = guiFrame(parent)
    t.position = position
    t.size = size

    updatableUI[t.mid] = t
    return t

def createButton(position: udim2, size: udim2, text: str, parent: guiFrame = None) -> textButton:
    t = textButton(parent)
    t.position = position
    t.size = size
    t.setText(text)

    updatableUI[t.mid] = t
    return t

def createLabel() -> textLabel:
    t = textLabel()
    return t