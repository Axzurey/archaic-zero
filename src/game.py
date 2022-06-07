from ast import arg
import threading
from pygame import Vector2
import client.renderCycle as renderCycle
from data.exposed import addEntity
from modules.entity import entity
from modules.gui.guiFrame import guiFrame
from modules.gui.textLabel import textLabel
from modules.gui.textButton import textButton
from modules.udim2 import udim2

entities: dict[str, entity] = {}

def createEntity(position: Vector2, size: Vector2, imagePath: str, walkLogicOverride: callable = None):
    ent = entity(position, size, imagePath)

    addEntity(ent.id, ent)

    if walkLogicOverride:
        ent.walkLogic = walkLogicOverride

    renderCycle.addTaskToRenderCycle(ent.walkLogic, '_mainUpdateY')

    entities[ent.id] = ent

    return ent

def createFrame(position: udim2, size: udim2, parent) -> guiFrame:
    t = guiFrame(parent)
    t.position = position
    t.size = size
    return t

def createButton(position: udim2, size: udim2, text: str, parent: guiFrame = None) -> textButton:
    t = textButton(parent)
    t.position = position
    t.size = size
    t.setText(text)
    return t

def createLabel() -> textLabel:
    t = textLabel()
    return t