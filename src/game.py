from ast import arg
import threading
from pygame import Vector2
import client.renderCycle as renderCycle
from data.exposed import addEntity
from modules.entity import entity
from modules.gui.guiFrame import guiFrame
from modules.gui.textLabel import textLabel
from modules.gui.textButton import textButton

entities: dict[str, entity] = {}

def createEntity(position: Vector2, size: Vector2, imagePath: str, walkLogicOverride: callable = None):
    ent = entity(position, size, imagePath)

    addEntity(ent.id, ent)

    if walkLogicOverride:
        ent.walkLogic = walkLogicOverride

    renderCycle.addTaskToRenderCycle(ent.walkLogic, '_mainUpdateY')

    entities[ent.id] = ent

    return ent

def createFrame(position: Vector2, size: Vector2) -> guiFrame:
    t = guiFrame()
    t.setPosition(position)
    t.setSize(size)
    return t

def createButton(position: Vector2, size: Vector2, text: str, parent: guiFrame = None) -> textButton:
    t = textButton(parent)
    t.setPosition(position)
    t.setSize(size)
    t.setText(text)
    return t

def createLabel() -> textLabel:
    t = textLabel()
    return t