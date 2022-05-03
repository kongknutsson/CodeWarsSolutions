""" 
This has quite a long list of rules, so you can view them here instead of in the code: 
https://www.codewars.com/kata/5941c545f5c394fef900000c
"""

class Warrior():    
    def __init__(self):
        self.level = 1
        self.rank = "Pushover"
        self.experience = 100
        self.achievements = []
        
    def update_warrior(self):
        ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.level = self.experience // 100
        self.level = 100 if self.level > 100 else self.level
        if self.experience > 10000:
            self.experience = 10000
        self.rank = ranks[self.level // 10]
        
    def battle(self, enemy_level):
        enemy_rank = enemy_level // 10
        if enemy_level > 100 or enemy_level < 1:
            return "Invalid level"
        elif (self.level // 10) < enemy_rank and self.level + 5 <= enemy_level:
            return "You've been defeated"
        elif self.level == enemy_level:
            self.experience += 10
            self.update_warrior()
            return "A good fight"
        elif self.level - 1 == enemy_level:
            self.experience += 5  
            self.update_warrior()
            return "A good fight"
        elif self.level - 2 >= enemy_level:
            return "Easy fight"  
        elif self.level < enemy_level:
            self.experience += 20 * (self.level - enemy_level)**2
            self.update_warrior()
            return "An intense fight"
        
    def training(self, arr):
        desc, exp, level = arr[0], arr[1], arr[2]
        if self.level >= level:
            self.experience += exp
            self.achievements.append(desc)
            self.update_warrior()
            return desc
        else:
            return "Not strong enough"