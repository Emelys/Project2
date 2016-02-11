# -*- coding: utf-8 -*-

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
        return container.description + ''.join(description)
    
    
#персонаж: местонахождение, инвентарь, комната в которой он находится
class Character():
    def __init__(self, x, y, inventary, environment):
        self.inventary = inventary
        self.environment = environment
        self.x = x
        self.y = y           
        self.experience = 0
        
    def description_inventary(container):
            description = []
            for obj in container(inventary):
                description.append(obj.long_description)
            return ''.join(description)
        
        
class Actions():
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
            
    
            
            
            
            
            
chear = Object("Стул", 10, 20, 'room1', 'Маленький стул. ', 'Очень маленький стул с едой. ', 'unknown')
room1 = Container([chear], 'Старая комната без стульев. ')
print(chear)
print(Object.long_description(chear))
print(Container.description_container(room1))
print(Object.location(chear))
         



    
    
        
    
    