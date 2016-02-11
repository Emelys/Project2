# -*- coding: utf-8 -*-

import sys, pygame
from pygame.locals import * 

EROR_IN_QUESTION = "I can't understand you"

#класс для всех объектов: имя, координаты, комната/инвентарь,
#короткое описание, длинное 
#статус: неизвестен, известен
class Object():
    def __init__(self, name, x, y, environment, short_description, long_description, status):        
        self.name = name
        self.environment = environment
        self.x = x
        self.y = y        
        self.short_description = short_description
        self.long_description = long_description
        self.status = status
        
    def __str__(obj):
        return obj.name
    
    def short_description(obj):
        return obj.short_description
    
    def long_description(obj):
        return obj.long_description    
    
    def location(obj):
        return obj.x, obj.y
    
    
#комната: местонахождение и инвентарь
class Container():
    def __init__(self, inventary, description):        
        self.inventary = inventary
        self.description = description
        
    def description_container(container):
        description = []
        for obj in (container.inventary):
            description.append(obj.short_description)
            
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_e:
                    font = pygame.font.Font(None, 25)
                    text = font.render(container.description + ''.join(description), True, black)        
        return text
    
    
#персонаж: местонахождение, инвентарь, комната в которой он находится
class Character():
    def __init__(self, x, y, inventary, environment):
        self.inventary = inventary
        self.environment = environment
        self.x = 0
        self.y = 0           
        self.experience = 0
        
    def description_inventary(container):
            description = []
            for obj in container(inventary):
                description.append(obj.long_description)
                
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        font = pygame.font.Font(None, 25)
                        text = font.render(''.join(description), True, black)             
            return text
        
    def moving_hero(self, x1, y1, texture_size):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    y1 -= texture_size
                if event.key == K_DOWN:
                    y1 += texture_size
                if event.key == K_RIGHT:
                    x1 += texture_size
                if event.key == K_LEFT:
                    x1 -= texture_size
        Hero.x = x1
        Hero.y = y1
        return x1, y1       
    
    def near(obj1, obj2):
            if abs(obj1 - obj2) <= 2:
                return True
            else:
                return False 
            
    def explore_obj(obj):
        if obj.status == 'known' and obj.environment == character.environment:
            obj.status = good_known
            return obj.long_description
        else:
            return EROR_IN_QUESTION    
        
    def take_obj(obj):
        if near(obj.x, character.x) and near(obj.x == character.x):
            obj.status = known
            obj.environment = character
            character.inventary.append(obj)         
        
        
    
     
            
            
Hero = Character(0, 0, [], 'room1')     
chear = Object(u"Стул", 10, 20, 'room1', u'Маленький стул. ', u'Маленький стул с едой. ', 'unknown')
room1 = Container([chear], u'Старая комната со стульями. ')            
print(Object.long_description(chear))
#print(Container.description_container(room1))
#print(Object.location(chear))
         



    
    
        
    
    