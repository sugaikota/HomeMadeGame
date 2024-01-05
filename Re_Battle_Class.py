# coding: UTF-8

###
# This code was created by Kota Sugai.
# Tokyo University of Technology.
# Faculty of Computer Science.
# Department of Computer Science.
# Department of Artificial Intelligence.
# C0B21087 Kota Sugai
###

import Re_Character_Class as character
import Re_Enemy_Class as enemy
from time import *
import numpy as np
import pygame as pg
import sys
from typing import Union
import os
import shutil
from copy import *


###
# Starting that defines the constants.
###

class PygameConstant:
    """
    This class holds constants that describe the pygame.
    
    Vars:
        black (tuple) : An RGB tuple representing black.
        white (tuple) : An RGB tuple representing white.
        red (tuple) : An RGB tuple representing red.
        blue (tuple) : An RGB tuple representing bule.
        screen_size_x (int) : Size of the screen in the X direction.
        screen_size_y (int) : Size of the screen in the Y direction.
    """
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.screen_size_x = 1200
        self.screen_size_y = 600


class ScreenConstant:
    """
    This class holds constants that describe the screen mode.
    
    Vars:
        title_screen (int) : This means the screen that displays the Title.
        home_screen (int) : This means the screen that displays the Home.
        quest_screen (int) : This means the screen that displays the Quest.
        seleted_character_screen (int) : This means the screen that displays the selected_character.
        battle_screen (int) : This means the screen that displays the battle.
        village_screen (int) : This means the screen that displays the village.
        room_screen (int) : This means the screen that displays the room.
        gacha_screen (int) : This means the screen that displays the gacha.
        traning_screen (int) : This means the screen that displays the traning.
        main_quest_screen (int) : This means the screen that displays the main_quest.
        event_quest_screen (int) : This means the screen that displays the event_quest.
        writer_quest_screen (int) : This means the screen that displays the writer_quest.
        day_quest_screen (int) : This means the screen that displays the day_quest.
        challenge_quest_screen (int) : This means the screen that displays the challenge_quest.
        memorials_quest_screen (int) : This means the screen that displays the memorials_quest.
        craft_quest_screen (int) : This means the screen that displays the craft_quest.
        support_screen (int) : This means the screen that displays the support.
    """
    def __init__(self):
        self.title_screen = 0
        self.home_screen = 1
        self.quest_screen = 2
        self.seleted_character_screen = 3
        self.battle_screen = 4
        self.village_screen = 5
        self.room_screen = 6
        self.gacha_screen = 7
        self.traning_screen = 8
        
        self.main_quest_screen = 10
        self.event_quest_screen = 11
        self.writer_quest_screen = 12
        self.day_quest_screen = 13
        self.challenge_quest_screen = 14
        self.memorials_quest_screen = 15
        self.craft_quest_screen = 16
        self.support_screen = 17
    
    
class BattleConstant:
    """
    This class holds constants that describe the all constants.
    
    Vars:
        pygame_constant (PygameConstant) : An instance of the constant class for pygame.
        screen_constant (ScreenConstant) : An instance of the constant class for screen.
    
    Functions:
        get(typ) : Returns a constant corresponding to the specified argument(typ).
    """
    def __init__(self):
        self.pygame_constant = PygameConstant()
        self.screen_constant = ScreenConstant()
        
    def get(self, typ: str) -> Union[int, tuple[int, int, int]]:
        """
        Returns a constant corresponding to the specified argument(typ).
        
        Args:
            typ (str) : Which constants do you get.
        
        Returns:
            int or tuple : You get constants.
        """
        if (typ == "black"):
            return self.pygame_constant.black
        elif (typ == "white"):
            return self.pygame_constant.white
        elif (typ == "red"):
            return self.pygame_constant.red
        elif (typ == "blue"):
            return self.pygame_constant.blue
        elif (typ == "x"):
            return self.pygame_constant.screen_size_x
        elif (typ == "y"):
            return self.pygame_constant.screen_size_y
        
        elif (typ == "title"):
            return self.screen_constant.title_screen
        elif (typ == "home"):
            return self.screen_constant.home_screen
        elif (typ == "quest"):
            return self.screen_constant.quest_screen
        elif (typ == "selecte_chr"):
            return self.screen_constant.seleted_character_screen
        elif (typ == "battle"):
            return self.screen_constant.battle_screen
        elif (typ == "village"):
            return self.screen_constant.village_screen
        elif (typ == "room"):
            return self.screen_constant.room_screen
        elif (typ == "gacha"):
            return self.screen_constant.gacha_screen
        elif (typ == "traning"):
            return self.screen_constant.traning_screen
        
        elif (typ == "main"):
            return self.screen_constant.main_quest_screen
        elif (typ == "event"):
            return self.screen_constant.event_quest_screen
        elif (typ == "writer"):
            return self.screen_constant.writer_quest_screen
        elif (typ == "day"):
            return self.screen_constant.day_quest_screen
        elif (typ == "challenge"):
            return self.screen_constant.challenge_quest_screen
        elif (typ == "memorials"):
            return self.screen_constant.memorials_quest_screen
        elif (typ == "craft"):
            return self.screen_constant.craft_quest_screen
        elif (typ == "support"):
            return self.screen_constant.support_screen


BATTLECONSTANTS = BattleConstant()
CHARACTERCONSTANTS = character.Constant()

###
# Finishing that defines the constants.
###

###
# Starting that defines the class.
###


class BattleDirector:
    """
    This class is director who controls the battle.
    
    Args:
        *args (tuple) : This is an argument used when copying, and contains a tuple of each variable. When used for purposes other than copying, set *args = (None).
    
    Vars:
        stage_dict (dict[character_location(int) : character_information(Character)]) : Maintains information about the character's position on the stage and the character at that position.
        act_character_dict (dict[character_location(int) : character_information(Character)]) : Maintains information about the character's position on the battle and the character at that position.
        act_enemy_dict (dict[enemy_location(int) : enemy_information(Enemy)]) : Maintains information about the enemy's position on the battle and the enemy at that position.
        time_line_list (list) : Maintains the time line, which is the order of characters' actions.
        now_act_character (Character or Enemy or SkillCard) : Maintains information about the character currently acting.
        act_log_list (list) : Maintains a log of character's actions.
        total_turn (int) : Maintains the number of turns that have passed due to battle.
        jamp_gauge (int) : Maintains jump gauge built up by character's actions.
        selected_skill (Skill) : Maintains the skills of the character selected by the player.
        selected_character (list) : Retains the characters of the character selected by the player.
        auto_mode (bool) : Maintains auto mode information.
        shift_mode (bool) : Maintains shift mode information.
        support_mode (bool) : Maintains support mode information.

    Functions:
        stage_dict_make() : Make the character dictionary, act character dictionary and time line.
        time_line_make() : Make the time line.
        hate_list_make() : This function calculates the ease of selection of an automatically selected character based on the character's "hate rate".
        enemy_dict_make(ene_list) : Make the enemy dict for enemy list.
        selected_skill_set(skill_type) : This function sets the skill selected by the character from the skill type in the argument into a "selected skill".
        selected_character_set(character_loc) : This function selects the character that Enemy should automatically select.
        character_update() : This function deletes the selected character, skills,...
        enemy_update() : This function deletes the selected character, skills,...
        character_recast_calc() : Calculate the character's skill recast.
        character_act() : Act the character action.
        character_auto_act() : Auto act the character action.
        winning_check() : Check the winner or loser of a battle.
        __copy__() : This function is a special method called by the copy.copy() function.

    """
    def __init__(self, *args):
        if (args[0] == None):
            self.stage_dict: dict[int, Union[character.Character, character.Enemy]] = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}
            self.act_character_dict: dict[int, character.Character] = {}
            self.act_enemy_dict: dict[int, character.Enemy] = {}
            self.time_line_list: list[Union[character.Character, character.Enemy, character.SkillCard]] = []
            self.now_act_character: Union[character.Character, character.Enemy, character.SkillCard] = None
            self.act_log_list: list[str] = ["0 : ゲーム開始!"]
            self.total_turn: int = 1
            self.jamp_gauge: int = 0
            self.selected_stage: int = -1
            self.selected_skill: character.Skill = None
            self.selected_character: list[list[Union[character.Character, character.Enemy]]] = [[None], [None], [None]]   # [selected_character, selected_enemy, time_line]
            self.auto_mode: bool = False
            self.shift_mode: bool = False
            self.support_mode: bool = False
            self.win_check: bool = False
            self.lose_check: bool = False
        
        else:
            self.stage_dict: dict[int, Union[character.Character, character.Enemy]] = args[0]
            self.act_character_dict: dict[int, character.Character] = args[1]
            self.act_enemy_dict: dict[int, character.Enemy] = args[2]
            self.time_line_list: list[Union[character.Character, character.Enemy, character.SkillCard]] = args[3]
            self.now_act_character: Union[character.Character, character.Enemy, character.SkillCard] = args[4]
            self.act_log_list: list[str] = args[5]
            self.total_turn: int = args[6]
            self.jamp_gauge: int = args[7]
            self.selected_stage: int = args[8]
            self.selected_skill: character.Skill = args[9]
            self.selected_character: list[list[Union[character.Character, character.Enemy]]] = args[10]   # [selected_character, selected_enemy, time_line]
            self.auto_mode: bool = args[11]
            self.shift_mode: bool = args[12]
            self.support_mode: bool = args[13]
            self.win_check: bool = args[14]
            self.lose_check: bool = args[15]
        
    def stage_dict_make(self) -> None:
        """
        Make the character dictionary, act character dictionary and time line.
        """
        for loc, _chr in self.stage_dict.items():
            if (type(_chr) == character.Character):
                if (loc == 1) or (loc == 2) or (loc == 3):
                    self.act_character_dict[loc] = _chr
            else:
                self.act_enemy_dict[loc] = _chr
        
    def time_line_make(self) -> None:
        """
        Make the time line.
        """
        l: list[Union[character.Character, character.Enemy]] = [chr for chr in list(self.act_character_dict.values())+list(self.act_enemy_dict.values()) if chr != None]
        self.time_line_list = sorted(l, key=lambda x:x.information.get("delay"), reverse=False)
        self.now_act_character = self.time_line_list[0]

    def hate_list_make(self) -> list[int]:
        """
        This function calculates the ease of selection of an automatically selected character based on the character's "hate rate".
        """
        chr_list: list[character.Character] = [c for c in self.act_character_dict.values() if c != None]
        hate_list = []
        True_hate_list = []
        rate_change = [False, False, False]
        rate_change_num = 0
        rate_over_num = 0
        rate_over = [False, False, False]
        
        if len(chr_list) == 1:
            return [1.0]
        
        for i, chr in enumerate(chr_list):
            hate = chr.information.get("hate")
            hate_list.append(hate)
            True_hate_list.append(hate)
            if chr.status.status_rates.get("hate") != []:
                rate_change[i] = True
                rate_change_num += 1
            if hate >= 100:
                rate_over[i] = True
                rate_over_num += 1
                
        if rate_change_num == 1 and rate_over_num == 1:
            for i, j in enumerate(rate_over):
                if j == True:
                    True_hate_list[i] = 100
                else:
                    True_hate_list[i] = 0
        
        if rate_change_num == 1 and rate_over_num == 0:
            m = max(hate_list)
            x = 100 - m
            True_hate_list = hate_list.copy()
            l = [[1, 2], [0, 2], [0, 1]]
            for i in range(2):
                if rate_change[i] == True:
                    for j in zip([2/3, 1/3], l[i]):
                        True_hate_list[j[1]] = j[0] * x

        if rate_change_num == 2:
            for i, j in enumerate(zip(hate_list, rate_change)):
                True_hate_list[i] = j[0] * j[1]
                
            s = sum(True_hate_list)
            x = s - 100
            if x > 0:
                for i, j in enumerate(rate_change):
                    True_hate_list[i] -= (j * (x / 2))
            if x < 0:
                for i, j in enumerate(rate_change):
                    if j == False:
                        True_hate_list[i] = -1 * x

        for i in range(len(True_hate_list)):
            True_hate_list[i] = round(True_hate_list[i], 1) / 100
            
        if sum(True_hate_list) != 1:
            l = (1 - sum(True_hate_list))/len(chr_list)
            for i in range(len(chr_list)):
                True_hate_list[i] += l
            
        return True_hate_list

    def enemy_dict_make(self, ene_list: list[character.Enemy]) -> None:
        """
        Make the enemy dict for enemy list.
        
        Vars:
            ene_list (list) : Enemy information from stage information.
        """
        for ene in ene_list:
            try:
                self.stage_dict[ene.information.location] = ene
            except:
                pass
        
    def selected_skill_set(self, skill_type: str) -> None:
        """
        This function sets the skill selected by the character from the skill type in the argument into a "selected skill".
        
        Vars:
            skill_type (str) : Information about which skill was selected.
        """
        try:
            if (skill_type == "通常"):
                self.selected_skill = self.now_act_character.skill.normal_skill
            elif (skill_type == "スキル1"):
                self.selected_skill = self.now_act_character.skill.first_skill
            elif (skill_type == "スキル2"):
                self.selected_skill = self.now_act_character.skill.second_skill
            # elif (skill_type == "ぶきスキル"):
            #     self.selected_skill = self.now_act_character.weapon.skill
            elif (skill_type == "とっておき"):
                self.selected_skill = self.now_act_character.skill.jamp_skill
        except:
            pass
        
    def selected_character_set(self, chr_loc: int = -1) -> None:
        """
        This function sets the character selected by the character from the character location in the argument into a "selected character".
        
        Vars:
            chr_loc (int) : Information about which character was selected.
        """
        self.selected_character[2] = self.time_line_list
        try:
            skill_info = self.selected_skill.info
            if ("chr_single" in skill_info):
                self.selected_character[0] = [self.act_character_dict[chr_loc]]
            elif ("chr_whole" in skill_info):
                self.selected_character[0] = [c for c in self.act_character_dict.values() if c != None]
            elif ("ene_single" in skill_info):
                self.selected_character[1] = [self.act_enemy_dict[chr_loc]]
            elif ("ene_whole" in skill_info):
                self.selected_character[1] = [c for c in self.act_enemy_dict.values() if c != None]
            elif ("self" in skill_info):
                self.selected_character[0] = [self.now_act_character]
        except:
            pass
        
    def selected_character_auto_set(self):
        """
        This function selects the character that Enemy should automatically select.
        """
        self.selected_character[2] = self.time_line_list
        try:
            skill_info = self.selected_skill.info
            if ("chr_single" in skill_info):
                chr_loc = np.random.choice([loc for loc, c in self.act_character_dict.items() if c != None])
                self.selected_character[1] = [self.act_character_dict[chr_loc]]
            elif ("chr_whole" in skill_info):
                self.selected_character[1] = [c for c in self.act_character_dict.values() if c != None]
            elif ("ene_single" in skill_info):
                chr_loc = np.random.choice([loc for loc, c in self.act_enemy_dict.items() if c != None])
                self.selected_character[0] = [self.act_enemy_dict[chr_loc]]
            elif ("ene_whole" in skill_info):
                self.selected_character[0] = [c for c in self.act_enemy_dict.values() if c != None]
            elif ("self" in skill_info):
                self.selected_character[0] = [self.now_act_character]
        except:
            pass
        
    def character_update(self):
        """
        This function deletes the selected character, skills,...
        """
        for loc, _chr in self.stage_dict.items():
            if (_chr.status.get("HP") <= 0):
                self.stage_dict[loc] = None
                try:
                    self.act_enemy_dict[loc] = None
                except:
                    self.act_character_dict[loc] = None
        
        self.selected_skill = None
        self.selected_character = [[None], [None], [None]]
        self.total_turn += 1
        self.jamp_gauge += self.now_act_character.information.get("charge")
        self.now_act_character.information.set("charge", 0)
        self.time_line_make()
        self.character_recast_calc()
        if (len(self.act_log_list) >= 6):
            del self.act_log_list[0]
        
    def enemy_update(self):
        """
        This function deletes the selected character, skills,...
        """
        for loc, _chr in self.stage_dict.items():
            if (_chr != None):
                if (_chr.status.get("HP") <= 0):
                    self.stage_dict[loc] = None
                    try:
                        self.act_enemy_dict[loc] = None
                    except:
                        self.act_character_dict[loc] = None
        
        self.selected_skill = None
        self.selected_character = [[None], [None], [None]]
        self.total_turn += 1
        self.time_line_make()
        self.character_recast_calc()
        if (len(self.act_log_list) >= 6):
            del self.act_log_list[0]
     
    def character_recast_calc(self):
        """
        Calculate the character's skill recast.
        """
        for c in [c for c in self.act_character_dict.values() if c != None]:
            if (c.skill.first_skill.recast >= 1):
                c.skill.first_skill.recast -= 1
            if (c.skill.second_skill.recast >= 1):
                c.skill.second_skill.recast -= 1
                
            if (c.skill.first_skill.recast == -1):
                c.skill.first_skill.recast = c.skill.first_skill.def_recast
            if (c.skill.second_skill.recast == -1):
                c.skill.second_skill.recast = c.skill.second_skill.def_recast
      
    def character_act(self):
        """
        Act the character action.
        """
        if (type(self.now_act_character) == character.Character):   # If the character currently acting is Character.
            act_log = f"{self.total_turn} : "
            skill = self.selected_skill
            act_chr = self.now_act_character
            selected_chr = self.selected_character
            act_log += skill.skill_function(act_chr, *selected_chr)
            self.act_log_list.append(act_log[:-1].replace("\n", ", "))
            # print(self.act_log_list)
            self.character_update()
            self.winning_check()

        elif (issubclass(type(self.now_act_character), enemy.Enemy) == True):   # If the character currently acting is Enemy.
            act_log = f"{self.total_turn} : "
            chr_list, ene_list, turn = [c for c in self.act_character_dict.values() if c != None], [c for c in self.act_enemy_dict.values() if c != None], self.total_turn
            skill = self.now_act_character.skill_function(chr_list, ene_list, turn)
            self.selected_character_auto_set()
            act_log += skill(self.now_act_character, *self.selected_character, chr_list, ene_list, turn)
            self.act_log_list.append(act_log[:-1].replace("\n", ", "))
            self.enemy_update()
            self.winning_check()
            sleep(1)

    def character_auto_act(self):
        """
        Auto act the character action.
        """
        now_act_chr_skill: list[character.Skill] = [self.now_act_character.skill.normal_skill, self.now_act_character.skill.first_skill, self.now_act_character.skill.second_skill]
        actionable_skill: list[character.Skill] = []
        for skill in now_act_chr_skill:
            if (skill.recast == 0):
                actionable_skill.append(skill)
                
        self.selected_skill = np.random.choice(actionable_skill)
        self.selected_character_auto_set()
        self.character_act() 

    def character_ai_act(self):
        """
        Actions are determined by AI.
        """
        AI = AStarSearchAlgorithm()
        ai_selected = AI.A_star_search(copy(self))
        ai_selected_skill = None
        ai_selected_character = []
        ai_selected_enemy = []
        
        try:
            if (ai_selected[0] == "通常"):
                ai_selected_skill = self.now_act_character.skill.normal_skill
            elif (ai_selected[0] == "スキル1"):
                ai_selected_skill = self.now_act_character.skill.first_skill
            elif (ai_selected[0] == "スキル2"):
                ai_selected_skill = self.now_act_character.skill.second_skill
            # elif (ai_selected[0] == "ぶきスキル"):
            #     ai_selected_skill = self.now_act_character.weapon.skill
            elif (ai_selected[0] == "とっておき"):
                ai_selected_skill = self.now_act_character.skill.jamp_skill
        except:
            pass
        
        for c in ai_selected[1] + ai_selected[2]:
            try:
                loc = c.information.location
                sel_c = self.stage_dict[loc]
                if isinstance(sel_c, character.Character):
                    ai_selected_character.append(sel_c)
                else:
                    ai_selected_enemy.append(sel_c)
            except:
                pass
        
        print(ai_selected_skill)
        print(ai_selected_character, ai_selected_enemy)
        self.selected_skill = ai_selected_skill
        self.selected_character[0] = ai_selected_character
        self.selected_character[1] = ai_selected_enemy
        self.character_act()
        
    def winning_check(self):
        """
        Check the winner or loser of a battle.
        """
        if (len([chr for chr in self.act_character_dict.values() if (chr != None)]) == 0):
            self.lose_check = True
            
        elif (len([chr for chr in self.act_enemy_dict.values() if (chr != None)]) == 0):
            self.win_check = True

    def __copy__(self):
        """
        This function is a special method called by the copy.copy() function.
        """
        # If you copy the character information as is, the reference sources will be the same, and the original(reference sources) information will be changed during the search.
        copy_stage_dict = {key:deepcopy(c) for key, c in self.stage_dict.items()}
        copy_act_character_dict = {}
        copy_act_enemy_dict = {}
        copy_time_line_list = []
        copy_now_act_character = None
        
        for loc, c in copy_stage_dict.items():
            if (isinstance(c, character.Character)):
                if (loc == 1) or (loc == 2) or (loc == 3):
                    copy_act_character_dict[loc] = c
                
            else:
                copy_act_enemy_dict[loc] = c

        chr_list: list[Union[character.Character, character.Enemy]] = [chr for chr in list(copy_act_character_dict.values())+list(copy_act_enemy_dict.values()) if chr != None]
        copy_time_line_list = sorted(chr_list, key=lambda x:x.information.get("delay"), reverse=False)
        copy_now_act_character = self.time_line_list[0]
        
        return BattleDirector(copy_stage_dict, copy_act_character_dict, copy_act_enemy_dict, copy_time_line_list, copy_now_act_character, self.act_log_list, self.total_turn, self.jamp_gauge, self.selected_stage, self.selected_skill, self.selected_character, self.auto_mode, self.shift_mode, self.support_mode, self.win_check, self.lose_check)


class SceneNode:
    def __init__(self):
        self.parent = None
        self.scene: BattleDirector = None
        self.depth: int = 0
        self.skill: character.Skill = None
        self.selected_character: list[character.Character] = None
        self.selected_enemy: list[enemy.Enemy] = None
        self.g_cost: int = 0
        self.h_value: int = 0
        self.f_cost: int = 0

class SceneNode:
    """
    Node used in search using game tree.
    
    Args:
        node_parent (SceneNode) : Parent node of the node. (from which node the node appeared)
        scene (battleDirector) : Information on the current situation.
        depth (int) : Depth of search.
        skill_type (str) : Skills information for moving to the next scene.
        sel_chr (list[character.Character]) : Selected character for moving to the next scene.
        sel_ene (list[enemy.Enemy]) : Selected enemy for moving to the next scene.
        g_cost (int) : Route cost.
        h_value (int) : Estimated value
        f_cost (int) : F cost.

    Vars:
        node_parent (SceneNode) : Parent node of the node. (from which node the node appeared)
        scene (battleDirector) : Information on the current situation.
        depth (int) : Depth of search.
        skill_type (str) : Skills information for moving to the next scene.
        selected_character (list[character.Character]) : Selected character for moving to the next scene.
        selected_enemy (list[enemy.Enemy]) : Selected enemy for moving to the next scene.
        g_cost (int) : Route cost.
        h_value (int) : Estimated value
        f_cost (int) : F cost.
    """
    def __init__(self, node_parent: SceneNode, scene: BattleDirector, depth: int, skill: str = None, sel_chr: list[character.Character] = [None], sel_ene: list[enemy.Enemy] = [None], g_cost: int=0, h_value: int=0, f_cost: int=0):
        self.parent = node_parent
        self.scene = scene
        self.depth = depth
        self.skill_type = skill
        self.selected_character = sel_chr
        self.selected_enemy = sel_ene
        self.g_cost = g_cost
        self.h_value = h_value
        self.f_cost = f_cost
        
    def __eq__(self, other: SceneNode):
        return id(self) == id(other)
    
    def __str__(self) -> str:
        return f"depth : {self.depth}, g cost : {self.g_cost}, h value : {self.h_value}, f cost : {self.f_cost}"
    
        
class AStarSearchAlgorithm:
    """
    This class performs a A-Star search.
    
    Vars:
        MAX_DEPTH (int) : Maximum search depth.
        queue (list[ScenNode]) : Queue of nodes.
        visited_list (list[SceneNode]) : Visited nodes.
        
    Functions:
        A_star_search(scene) : Perform A* search.
        ai_move(scene, node, skill, skill_type, time_line, now_act_chr, sel_chr, sel_ene) : Make the character act based on the information in the argument.
        next_move_get(goal_node) : Returns search results from goal node.
        g_cost_calc(skill) : Calculate g cost.
        h_value_calc(scene) : Calculate h value.
        scene_back(scene, skill, now_act_chrm time_line, sel_chr, sel_ene) : After making the character act, I take my hand back. (Return the board to the state before the action.)
        character_update(scene) : Update character information.
        character_act(scene) : Make the character take action.
        enemy_update(scene) : Update enemy character information.
        enemy_act(scene) : Make the enemy character take action.
        selected_character_set(scene, sel_chr, sel_ene) : Set the selected character or enemy.
        selected_skill_set(scene, sel_skill) : Set the selected skill.
        next_skill_get(scene) : Gets actionable skills.
        next_selected_character_get(scene, skill_info) : Character that can be got from skill_info.
    """
    def __init__(self):
        self.MAX_DEPTH = 3
        self.queue: list[SceneNode] = []
        self.visited_list: list[SceneNode] = []
        
    def A_star_search(self, first_scene: BattleDirector) -> tuple[str, list[character.Character], list[enemy.Enemy]]:
        """
        Perform A-Star search.
        """
        self.queue = [SceneNode(None, first_scene, 0)]
        
        while (len(self.queue) > 0):
            first_node = self.queue.pop(0)
            
            if (first_node.depth > self.MAX_DEPTH):
                return self.next_move_get()
            
            elif (first_node.scene.win_check == True or first_node.scene.lose_check == True):
                return self.next_move_get(first_node)
                            
            else:
                self.visited_list.append(first_node)
                first_scene = first_node.scene
                time_line_list = first_scene.time_line_list
                now_act_chr = first_scene.now_act_character

                if (isinstance(now_act_chr, character.Character)):   # When now_act_character is character class.
                    skill_list = self.next_skill_get(first_scene)   # Skills that can be got from now_act_character.
                    
                    for skill, skill_info, skill_type in skill_list:
                        self.selected_skill_set(first_scene, skill)
                        selected_character_list, selected_enemy_list = self.next_selected_character_get(first_scene, skill_info)   # Selected character selected enemy that can be got from now_act_character.

                        next_node_list: list[SceneNode] = []
                        if (len(selected_character_list) == 0) and (len(selected_enemy_list) > 0):
                            for sel_ene in selected_enemy_list:
                                next_node = self.ai_move(first_scene, first_node, skill, skill_type, time_line_list, now_act_chr, sel_ene=sel_ene)
                                next_node_list.append(next_node)
                        
                        elif (len(selected_enemy_list) == 0) and (len(selected_character_list) > 0):
                            for sel_chr in selected_character_list:
                                next_node = self.ai_move(first_scene, first_node, skill, skill_type, time_line_list, now_act_chr, sel_chr=sel_chr)
                                next_node_list.append(next_node)
                        
                        else:
                            for sel_chr in selected_character_list:
                                for sel_ene in selected_enemy_list:
                                    next_node = self.ai_move(first_scene, first_node, skill, skill_type, time_line_list, now_act_chr, sel_chr=sel_chr, sel_ene=sel_ene)
                                    next_node_list.append(next_node)
                        
                        if (len(next_node_list) > 0):
                            self.queue.append(max(next_node_list, key=lambda x:x.f_cost))
                
                else:   # When now_act_character is enemy class.
                    self.enemy_act(first_scene)
                    next_node = SceneNode(first_node, first_scene, first_node.depth+1)
                    self.queue.append(next_node)
                      
    def ai_move(self, scene: BattleDirector, node: SceneNode, skill: character.Skill, skill_type: str, time_line: list[Union[character.Character, enemy.Enemy]], now_act_chr: character.Character, sel_chr=[None], sel_ene=[None]) -> SceneNode:
        """
        Make the AI act based on the information provided. Returns the next node got.
        
        Args:
            scene (BattleDirector) : Current scene.
            node (SceneNode) : Current node.
            skill (character.Skill) : Selected skill.
            skill_type (str) : Selected skill information.
            time_line (list[Union[character.Character, enemy.Enemy]]) : Current time line list.
            now_act_chr (character.Character) :  Current now actionable character.
            sel_chr (list[character.Character]) : Selected character.
            sel_ene (list[enemy.Enemy]) : Selected enemy.
            
        Returns:
            SceneNode : the next node got
        """
        self.selected_character_set(scene, selected_character_list=sel_chr, selected_enemy_list=sel_ene)
        self.character_act(scene)
        next_node = SceneNode(node, scene, node.depth+1, skill=skill_type, sel_chr=sel_chr, sel_ene=sel_ene, f_cost=node.f_cost)
        self.scene_back(scene, skill=skill, now_act_chr=now_act_chr, time_line_list=time_line)
        
        is_queue = (next_node in self.queue)
        is_visited = (next_node in self.visited_list)
        
        if (is_queue == True):
            for node in self.queue:
                if (node == next_node):
                    g_cost = self.g_cost_calc(skill)
                    if (node.g_cost > g_cost):
                        node.g_cost = g_cost
                        node.parent = next_node

        if (is_visited == False):
            g_cost = self.g_cost_calc(skill)
            next_node.g_cost = g_cost
            next_node.h_value = self.h_value_calc(scene)
            next_node.f_cost += next_node.g_cost + next_node.h_value
            
        if (is_queue == False) and (is_visited == False):
            return next_node
           
    def next_move_get(self, goal_node: SceneNode = None) -> tuple[str, list[character.Character], list[enemy.Enemy]]:
        """
        The search is finished and you know what action to take next.
        
        Args:
            goal_node (SceneNode) : The node where you finished.
            
        Returns:
            tuple[character.Skill, list[character.Character], list[enemy.Enemy]] : Returns the selected skill, selected character, and enemy.
        """
        if (goal_node == None):
            max_depth_node_list: list[SceneNode] = []
            for node in self.visited_list:
                if (node.depth == self.MAX_DEPTH):
                    max_depth_node_list.append(node)
            
            max_node = max(max_depth_node_list, key=lambda x:x.f_cost)
            ans_route: list[SceneNode] = []
            while (True):
                if (max_node.depth == 0):   # If node could go back to the beginning.
                    break
                
                ans_route.append(max_node)
                max_node = max_node.parent
                
            ai_act = ans_route[::-1][0]
            return ai_act.skill_type, ai_act.selected_character, ai_act.selected_enemy
        
        else:
            ans_route: list[SceneNode] = []
            while (True):
                if (goal_node.depth == 0):
                    break
                
                ans_route.append(goal_node)
                goal_node = goal_node.parent
                
            ai_act = ans_route[::-1][0]
            return ai_act.skill, ai_act.selected_character, ai_act.selected_enemy
                  
    def g_cost_calc(self, skill: character.Skill) -> int:
        """
        Calculate g-cost.
        g cost takes a large value when skill delay is small.
        Conversely, g-cost takes a small value when skill delay is large.
        
        Args:
            skill (character.Skill) : Skill to calculate g cost.
            
        Returns:
            int : Calculated g cost.
        """
        return 120 - skill.data[0][1]
    
    def h_value_calc(self, scene: BattleDirector) -> int:
        """
        Calculate h-value.
        h value becomes smaller when the character's HP is low.
        Conversely, h value increases when the enemy's HP is low.
        
        Args:
            scene (BattleDirector) : Current scene.
            
        Returns:
            int : Calculated h value.
        """
        h_value = 0
        hp_rate = 1000
        
        for chr in list(scene.act_character_dict.values()):
            try:
                h_value -= hp_rate * (1 - (chr.status.HP)/(chr.status.DEFHP))   # Make the score low when the character's HP is low.
            except:
                pass
        
        for ene in list(scene.act_enemy_dict.values()):
            try:
                h_value += 1.3 * hp_rate * (1 - (ene.status.HP)/(ene.status.DEFHP))   # Make the score high when the enemy's HP is low.
            except:
                pass
        
        return round(h_value, 2)
          
    def scene_back(self, scene: BattleDirector, skill: character.Skill = None, now_act_chr: character.Character = None, time_line_list: list[Union[character.Character, enemy.Enemy]] = None, sel_chr: list[character.Character] = [None], sel_ene: list[enemy.Enemy] = [None]) -> None:
        """
        After the character takes an action, back to the previous scene.
        
        Args:
            scene (BattleDirector) : Current scene.
        """
        scene.time_line_list = time_line_list
        scene.selected_skill = skill
        scene.now_act_character = now_act_chr
        scene.selected_character[0] = sel_chr
        scene.selected_character[1] = sel_ene
        scene.selected_character[2] = time_line_list
    
    def character_update(self, scene: BattleDirector) -> None:
        """
        This function deletes the selected character, skills,...
        
        Args:
            scene (BattleDirector) : Current scene.
        """
        for loc, c in scene.stage_dict.items():
            try:
                if (c.status.get("HP") <= 0):
                    # scene.stage_dict[loc] = None
                    try:
                        scene.act_enemy_dict[loc] = None
                    except:
                        scene.act_character_dict[loc] = None
            except:
                pass
        
        scene.total_turn += 1
        scene.jamp_gauge += scene.now_act_character.information.get("charge")
        scene.now_act_character.information.set("charge", 0)
        scene.time_line_make()
        scene.character_recast_calc()
        
    def character_act(self, scene: BattleDirector) -> None:
        """
        Perform the character's actions.
        
        Args:
            scene (BattleDirector) : Current scene.
        """
        act_log = f"{scene.total_turn} : "
        skill = scene.selected_skill
        act_chr = scene.now_act_character
        selected_chr = scene.selected_character
        act_log += skill.skill_function(act_chr, *selected_chr)
        self.character_update(scene)
        scene.winning_check()
      
    def enemy_update(self, scene: BattleDirector) -> None:
        for loc, _chr in scene.stage_dict.items():
            if (_chr != None):
                if (_chr.status.get("HP") <= 0):
                    # scene.stage_dict[loc] = None
                    try:
                        scene.act_enemy_dict[loc] = None
                    except:
                        scene.act_character_dict[loc] = None
        
        scene.selected_skill = None
        scene.selected_character = [[None], [None], [None]]
        scene.total_turn += 1
        scene.time_line_make()
        scene.character_recast_calc()
      
    def enemy_act(self, scene: BattleDirector) -> None:
        act_log = f"{scene.total_turn} : "
        chr_list, ene_list, turn = [c for c in scene.act_character_dict.values() if c != None], [c for c in scene.act_enemy_dict.values() if c != None], scene.total_turn
        skill = scene.now_act_character.skill_function(chr_list, ene_list, turn)
        scene.selected_character_auto_set()
        act_log += skill(scene.now_act_character, *scene.selected_character, chr_list, ene_list, turn)
        self.enemy_update(scene)
        scene.winning_check()
        
    def selected_character_set(self, scene: BattleDirector, selected_character_list: list[character.Character] = [None], selected_enemy_list: list[enemy.Enemy] = [None]) -> None:
        """
        Set selected character or enemy.
        
        Args:
            scene (BattleDirector) : Current scene.
            selected_character_list (list[character.Character]) : List of selected character.
            selected_enemy_list (list[enemy.Enemy]) : List of selected enemy.
        """
        scene.selected_character[0] = selected_character_list
        scene.selected_character[1] = selected_enemy_list
        scene.selected_character[2] = scene.time_line_list
                
    def selected_skill_set(self, scene: BattleDirector, selected_skill: character.Skill) -> None:
        """
        Set selected skill.
        
        Args:
            scene (BattleDirector) : Current scene.
            selected_skill (character.Skill) : Selected skill.
        """
        scene.selected_skill = selected_skill
                
    def next_skill_get(self, scene: BattleDirector) -> list[tuple[character.Skill, str, str]]:
        """
        Get actionable actions from the scene.
        
        Args:
            scene (BattleDirector) : Current scene.
            
        Returns:
            list[character.Skill, str] : Skills that can be got in the Current scene.
        """
        actionable_skill: list[character.Skill] = []
        
        if (isinstance(scene.now_act_character, character.Character) == True):
            now_act_chr_skill: dict[str, character.Skill] = {"通常" : scene.now_act_character.skill.normal_skill, "スキル1" : scene.now_act_character.skill.first_skill, "スキル2" : scene.now_act_character.skill.second_skill, "とっておき" : scene.now_act_character.skill.jamp_skill}
            
            for typ, skill in now_act_chr_skill.items():
                if (typ == "とっておき"):
                    if (scene.jamp_gauge >= 100):
                        actionable_skill.append((skill, skill.info, typ))
                else:
                    if (skill.recast == 0):
                        actionable_skill.append((skill, skill.info, typ))
        
        else:
            chr_list, ene_list, turn = [c for c in scene.act_character_dict.values() if c != None], [c for c in scene.act_enemy_dict.values() if c != None], scene.total_turn
            skill = scene.now_act_character.skill_function(chr_list, ene_list, turn)
            actionable_skill.append((skill, scene.now_act_character.skill_type, skill.__name__))
            
        return actionable_skill
    
    def next_selected_character_get(self, scene: BattleDirector, skill_info: str) -> tuple[list[list[character.Character]], list[list[enemy.Enemy]]]:
        """
        Get selected character from the scene.
        
        Args:
            scene (BattleDirector) : Current scene.
            skill_info (str) : Skill's infomation.
            
        Returns:
            list[list[Union[character.Character, enemy.Enemy]]] : Characters that can be got in the Current scene.
        """
        selected_chr_list: list[list[character.Character]]= []
        selected_ene_list: list[list[enemy.Enemy]] = []
        try:
            if ("chr_single" in skill_info):
                selected_chr_list = [[c] for loc, c in scene.act_character_dict.items() if c != None]
                
            if ("chr_whole" in skill_info):
                selected_chr_list.append([c for c in scene.act_character_dict.values() if c != None])
               
            if ("ene_single" in skill_info):
                selected_ene_list = [[c] for loc, c in scene.act_enemy_dict.items() if c != None]
              
            if ("ene_whole" in skill_info):
                selected_ene_list.append([c for c in scene.act_enemy_dict.values() if c != None])
                
            if ("self" in skill_info):
                selected_chr_list.append([scene.now_act_character])
        except:
            pass
        
        return selected_chr_list, selected_ene_list

        
class TitleUIDirector:
    """
    This class is director who controls the title UI.
    
    Vars:
        screen_mode (int) : The screen number currently being displayed or to be displayed next.
    
    Functions:
        title_text_show(display, mouse_button, keyboard_pressed) : Displays the title text and button.
        UI_show(display, mouse_button, keyboard_pressed) : Displays the title UI.
    """
    def __init__(self):
        self.screen_mode: int = BATTLECONSTANTS.get("title")
    
    def title_text_show(self, display: pg.Surface, mouse_button: tuple[bool, bool, bool], keyboard_pressed: bool) -> None:
        """
        Displays the title text and button.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 100)
        text = font.render("Game Start", True, BATTLECONSTANTS.get("black"))
        size_x, size_y = font.size("Game Start")
        display.blit(text, ((BATTLECONSTANTS.get("x")-size_x)/2, (BATTLECONSTANTS.get("y")-size_y)/2))
        
        font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 30)
        text = font.render("Press something on your keyboard or click with your mouse.", True, BATTLECONSTANTS.get("black"))
        size_x, size_y = font.size("Press something on your keyboard or click with your mouse.")
        display.blit(text, ((BATTLECONSTANTS.get("x")-size_x)/2, (BATTLECONSTANTS.get("y")-size_y)/2 + 200))
        
        if (keyboard_pressed == True):
            self.screen_mode = BATTLECONSTANTS.get("home")
        elif ((True in mouse_button) == True):
            self.screen_mode = BATTLECONSTANTS.get("home")
        else:
            self.screen_mode = BATTLECONSTANTS.get("title")
        
    def UI_show(self, display: pg.Surface, mouse_button: tuple[bool, bool, bool], keyboard_pressed: bool) -> int:
        """
        Displays the title UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed
        
        Returns:
            int : The type of screen that should be displayed next.
        """
        self.title_text_show(display, mouse_button, keyboard_pressed)
        return self.screen_mode


class HomeUIDirector:
    """
    This class is director who controls the home UI.
    
    Vars:
        screen_mode (int) : The screen number currently being displayed or to be displayed next.
    
    Functions:
        home_button_show(display, mouse_button, keyboard_pressed) : Displays the home text and button.
        UI_show(display, mouse_button, keyboard_pressed) : Displays the home UI.
    """
    def __init__(self):
        self.screen_mode: int = BATTLECONSTANTS.get("home")
        self.home_button_list = [(50, 50, "トレーニング"), (850, 50, "ルーム"), (50, 450, "召喚"), (850, 450, "村"), (450, 250, "クエスト")]
        self.font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 30)
        
    def home_button_show(self, display: pg.Surface, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the home screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        for x, y, txt in self.home_button_list:
            if (x <= mouse_pos[0] <= x+300 and y <= mouse_pos[1] <= y+100):
                color = "blue"
                if (True in mouse_button):
                    if (txt == "トレーニング"):
                        self.screen_mode = BATTLECONSTANTS.get("traning")
                    elif (txt == "ルーム"):
                        self.screen_mode = BATTLECONSTANTS.get("room")
                    elif (txt == "召喚"):
                        self.screen_mode = BATTLECONSTANTS.get("gacha")
                    elif (txt == "村"):
                        self.screen_mode = BATTLECONSTANTS.get("village")
                    elif (txt == "クエスト"):
                        self.screen_mode = BATTLECONSTANTS.get("quest")
            else:
                if (self.screen_mode == BATTLECONSTANTS.get("home")):
                    self.screen_mode = BATTLECONSTANTS.get("home")
                color = "black"
                        
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 300, 100)))
            text = self.font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = self.font.size(txt)
            display.blit(text, ((x+150-(size_x/2)), (y+size_y)))
        
    def UI_show(self, display: pg.Surface, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> int:
        """
        Displays the home UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed
        Returns:
            int : The type of screen that should be displayed next.
        """
        self.home_button_show(display, mouse_button, mouse_pos)
        return self.screen_mode
        

class QuestUIDirector:
    """
    This class is director who controls the quest UI.
    
    Vars:
        screen_mode (int) : The screen number currently being displayed or to be displayed next.
    
    Functions:
        quest_button_show(display, mouse_button, keyboard_pressed) : Displays the quest text and button.
        UI_show(display, mouse_button, keyboard_pressed) : Displays the quest UI.
    """
    def __init__(self):
        self.screen_mode = BATTLECONSTANTS.get("quest")
        self.quest_list = ["メインクエスト", "イベントクエスト", "作家クエスト", "曜日クエスト", "チャレンジクエスト", "メモリアルクエスト", "クラフトクエスト"]
        self.font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 30)
        
    def quest_button_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the quest screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        for i, txt in enumerate(self.quest_list):
            x = 800
            y = 87*i
            if (x <= mouse_pos[0] <= x+300 and y <= mouse_pos[1] <= y+75):
                color = "blue"
                if (True in mouse_button):
                    if (txt == "メインクエスト"):
                        self.screen_mode = BATTLECONSTANTS.get("main")
                        battle_director.selected_stage = BATTLECONSTANTS.get("main")
                    elif (txt == "イベントクエスト"):
                        self.screen_mode = BATTLECONSTANTS.get("event")
                        battle_director.selected_stage = BATTLECONSTANTS.get("event")
                    elif (txt == "作家クエスト"):
                        self.screen_mode = BATTLECONSTANTS.get("writer")
                        battle_director.selected_stage = BATTLECONSTANTS.get("writer")
                    elif (txt == "曜日クエスト"):
                        self.screen_mode = BATTLECONSTANTS.get("day")
                        battle_director.selected_stage = BATTLECONSTANTS.get("day")
                    elif (txt == "チャレンジクエスト"):
                        self.screen_mode = BATTLECONSTANTS.get("challenge")
                        battle_director.selected_stage = BATTLECONSTANTS.get("challenge")
                    elif (txt == "メモリアルクエスト"):
                        self.screen_mode = BATTLECONSTANTS.get("memorials")
                        battle_director.selected_stage = BATTLECONSTANTS.get("memorials")
                    elif (txt == "クラフトクエスト"):
                        self.screen_mode = BATTLECONSTANTS.get("craft")
                        battle_director.selected_stage = BATTLECONSTANTS.get("craft")
            else:
                color = "black"
                        
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 300, 75)))
            text = self.font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = self.font.size(txt)
            display.blit(text, ((x+150-(size_x/2)), (y+size_y)))
        
    def UI_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> int:
        """
        Displays the quest UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed
        
        Returns:
            int : The type of screen that should be displayed next.
        """
        self.quest_button_show(display, battle_director, mouse_button, mouse_pos)
        return self.screen_mode
    
    
class MainQuestUIDirector:
    """
    This class is director who controls the main quest UI.
    
    Vars:
        screen_mode (int) : The screen number currently being displayed or to be displayed next.
    
    Functions:
        main_quest_button_show(display, mouse_button, keyboard_pressed) : Displays the main quest text and button.
        UI_show(display, mouse_button, keyboard_pressed) : Displays the main quest UI.
    """
    def __init__(self):
        self.screen_mode = BATTLECONSTANTS.get("main")
        self.main_quest_list = ["メインクエスト1", "メインクエスト2"]
        self.font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 30)
        
    def main_quest_button_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the main quest screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        for i, txt in enumerate(self.main_quest_list):
            x = 800
            y = 100*i
            if (x <= mouse_pos[0] <= x+300 and y <= mouse_pos[1] <= y+90):
                color = "blue"
                if (True in mouse_button):
                    if (txt == "メインクエスト1"):
                        self.screen_mode = BATTLECONSTANTS.get("selecte_chr")
                        battle_director.enemy_dict_make([enemy.Kuromon(100, 1, 6)])
                    elif (txt == "メインクエスト2"):
                        self.screen_mode = BATTLECONSTANTS.get("selecte_chr")
                        battle_director.enemy_dict_make([enemy.Kuromon(100, 2, 6)])
            else:
                color = "black"
                        
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 300, 90)))
            text = self.font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = self.font.size(txt)
            display.blit(text, ((x+150-(size_x/2)), (y+size_y)))
        
    def UI_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> int:
        """
        Displays the main quest UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        
        Returns:
            int : The type of screen that should be displayed next.
        """
        self.main_quest_button_show(display, battle_director, mouse_button, mouse_pos)
        return self.screen_mode
    

class EventQuestUIDirector:
    """
    This class is director who controls the event quest UI.
    
    Vars:
        screen_mode (int) : The screen number currently being displayed or to be displayed next.
    
    Functions:
        event_button_show(display, mouse_button, keyboard_pressed) : Displays the event quest text and button.
        UI_show(display, mouse_button, keyboard_pressed) : Displays the event quest UI.
    """
    def __init__(self):
        self.screen_mode = BATTLECONSTANTS.get("event")
        self.event_quest_list = ["イベントクエスト1", "イベントクエスト2"]
        self.font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 30)
        
    def event_quest_button_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the event quest screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        for i, txt in enumerate(self.event_quest_list):
            x = 800
            y = 100*i
            if (x <= mouse_pos[0] <= x+300 and y <= mouse_pos[1] <= y+90):
                color = "blue"
                if (True in mouse_button):
                    if (txt == "イベントクエスト1"):
                        self.screen_mode = BATTLECONSTANTS.get("selecte_chr")
                        battle_director.enemy_dict_make([enemy.Kuromon(100, 1, 6)])
                    elif (txt == "イベントクエスト2"):
                        self.screen_mode = BATTLECONSTANTS.get("selecte_chr")
                        battle_director.enemy_dict_make([enemy.Kuromon(100, 2, 6)])
            else:
                color = "black"
                        
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 300, 90)))
            text = self.font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = self.font.size(txt)
            display.blit(text, ((x+150-(size_x/2)), (y+size_y)))
        
    def UI_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> int:
        """
        Displays the event quest UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        
        Returns:
            int : The type of screen that should be displayed next.
        """
        self.event_quest_button_show(display, battle_director, mouse_button, mouse_pos)
        return self.screen_mode
    
    
class WriterQuestUIDirector:
    """
    This class is director who controls the writer quest UI.
    
    Vars:
        screen_mode (int) : The screen number currently being displayed or to be displayed next.
    
    Functions:
        writer_quest_button_show(display, mouse_button, keyboard_pressed) : Displays the writer quest text and button.
        UI_show(display, mouse_button, keyboard_pressed) : Displays the writer quest UI.
    """
    def __init__(self):
        self.screen_mode = BATTLECONSTANTS.get("writer")
        self.writer_quest_list = ["作家クエスト1", "作家クエスト2"]
        self.font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 30)
        
    def writer_quest_button_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the writer quest screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        for i, txt in enumerate(self.writer_quest_list):
            x = 800
            y = 100*i
            if (x <= mouse_pos[0] <= x+300 and y <= mouse_pos[1] <= y+90):
                color = "blue"
                if (True in mouse_button):
                    if (txt == "作家クエスト1"):
                        self.screen_mode = BATTLECONSTANTS.get("selecte_chr")
                        battle_director.enemy_dict_make([enemy.Kuromon(100, 1, 6)])
                    elif (txt == "作家クエスト2"):
                        self.screen_mode = BATTLECONSTANTS.get("selecte_chr")
                        battle_director.enemy_dict_make([enemy.Kuromon(100, 2, 6)])
            else:
                color = "black"
                        
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 300, 90)))
            text = self.font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = self.font.size(txt)
            display.blit(text, ((x+150-(size_x/2)), (y+size_y)))
        
    def UI_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> int:
        """
        Displays the writer quest UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        
        Returns:
            int : The type of screen that should be displayed next.
        """
        self.writer_quest_button_show(display, battle_director, mouse_button, mouse_pos)
        return self.screen_mode
    
    
class DayQuestUIDirector:
    """
    This class is director who controls the day quest UI.
    
    Vars:
        screen_mode (int) : The screen number currently being displayed or to be displayed next.
    
    Functions:
        day_quest_show(display, mouse_button, keyboard_pressed) : Displays the dat quest text and button.
        UI_show(display, mouse_button, keyboard_pressed) : Displays the day quest UI.
    """
    def __init__(self):
        self.screen_mode = BATTLECONSTANTS.get("day")
        self.day_quest_list = ["曜日クエスト1", "曜日クエスト2"]
        self.font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 30)
        
    def day_quest_button_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the day quest screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        for i, txt in enumerate(self.day_quest_list):
            x = 800
            y = 100*i
            if (x <= mouse_pos[0] <= x+300 and y <= mouse_pos[1] <= y+90):
                color = "blue"
                if (True in mouse_button):
                    if (txt == "曜日クエスト1"):
                        self.screen_mode = BATTLECONSTANTS.get("selecte_chr")
                        battle_director.enemy_dict_make([enemy.Kuromon(100, 1, 6)])
                    elif (txt == "曜日クエスト2"):
                        self.screen_mode = BATTLECONSTANTS.get("selecte_chr")
                        battle_director.enemy_dict_make([enemy.Kuromon(100, 2, 6)])
            else:
                color = "black"
                        
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 300, 90)))
            text = self.font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = self.font.size(txt)
            display.blit(text, ((x+150-(size_x/2)), (y+size_y)))
        
    def UI_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> int:
        """
        Displays the dat quest UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        
        Returns:
            int : The type of screen that should be displayed next.
        """
        self.day_quest_button_show(display, battle_director, mouse_button, mouse_pos)
        return self.screen_mode
    
    
class ChallengeQuestUIDirector:
    """
    This class is director who controls the challenge quest UI.
    
    Vars:
        screen_mode (int) : The screen number currently being displayed or to be displayed next.
    
    Functions:
        challenge_quest_button_show(display, mouse_button, keyboard_pressed) : Displays the challenge quest text and button.
        UI_show(display, mouse_button, keyboard_pressed) : Displays the challenge quest UI.
    """
    def __init__(self):
        self.screen_mode = BATTLECONSTANTS.get("challenge")
        self.challenge_quest_list = ["チャレンジクエスト1", "チャレンジクエスト2"]
        self.font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 30)
        
    def challenge_quest_button_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the challenge quest screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        for i, txt in enumerate(self.challenge_quest_list):
            x = 800
            y = 100*i
            if (x <= mouse_pos[0] <= x+300 and y <= mouse_pos[1] <= y+90):
                color = "blue"
                if (True in mouse_button):
                    if (txt == "チャレンジクエスト1"):
                        self.screen_mode = BATTLECONSTANTS.get("selecte_chr")
                        battle_director.enemy_dict_make([enemy.EtwaliaShark(6)])
                    elif (txt == "チャレンジクエスト2"):
                        self.screen_mode = BATTLECONSTANTS.get("selecte_chr")
                        battle_director.enemy_dict_make([enemy.EtwaliaShark(6)])
            else:
                color = "black"
                        
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 300, 90)))
            text = self.font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = self.font.size(txt)
            display.blit(text, ((x+150-(size_x/2)), (y+size_y)))
        
    def UI_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> int:
        """
        Displays the challenge quest UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        
        Returns:
            int : The type of screen that should be displayed next.
        """
        self.challenge_quest_button_show(display, battle_director, mouse_button, mouse_pos)
        return self.screen_mode
    
    
class MemorialsQuestUIDirector:
    """
    This class is director who controls the memorials quest UI.
    
    Vars:
        screen_mode (int) : The screen number currently being displayed or to be displayed next.
    
    Functions:
        memorials_quest_button_show(display, mouse_button, keyboard_pressed) : Displays the memorials quest text and button.
        UI_show(display, mouse_button, keyboard_pressed) : Displays the memorials quest UI.
    """
    def __init__(self):
        self.screen_mode = BATTLECONSTANTS.get("memorials")
        self.memorial_quest_list = ["メモリアルクエスト1", "メモリアルクエスト2"]
        self.font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 30)
        
    def memorial_quest_button_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the memorial quest screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        for i, txt in enumerate(self.memorial_quest_list):
            x = 800
            y = 100*i
            if (x <= mouse_pos[0] <= x+300 and y <= mouse_pos[1] <= y+90):
                color = "blue"
                if (True in mouse_button):
                    if (txt == "メモリアルクエスト1"):
                        self.screen_mode = BATTLECONSTANTS.get("selecte_chr")
                        battle_director.enemy_dict_make([enemy.Kuromon(100, 1, 6)])
                    elif (txt == "メモリアルクエスト2"):
                        self.screen_mode = BATTLECONSTANTS.get("selecte_chr")
                        battle_director.enemy_dict_make([enemy.Kuromon(100, 2, 6)])
            else:
                color = "black"
                        
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 300, 90)))
            text = self.font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = self.font.size(txt)
            display.blit(text, ((x+150-(size_x/2)), (y+size_y)))
        
    def UI_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> int:
        """
        Displays the memorials quest UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        
        Returns:
            int : The type of screen that should be displayed next.
        """
        self.memorial_quest_button_show(display, battle_director, mouse_button, mouse_pos)
        return self.screen_mode
    
    
class CraftQuestUIDirector:
    """
    This class is director who controls the craft quest UI.
    
    Vars:
        screen_mode (int) : The screen number currently being displayed or to be displayed next.
    
    Functions:
        craft_quest_button_show(display, mouse_button, keyboard_pressed) : Displays the craft quest text and button.
        UI_show(display, mouse_button, keyboard_pressed) : Displays the craft quest UI.
    """
    def __init__(self):
        self.screen_mode = BATTLECONSTANTS.get("craft")
        self.craft_quest_list = ["クラフトクエスト1", "クラフトクエスト2"]
        self.font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 30)
        
    def craft_quest_button_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the craft quest screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        for i, txt in enumerate(self.craft_quest_list):
            x = 800
            y = 100*i
            if (x <= mouse_pos[0] <= x+300 and y <= mouse_pos[1] <= y+90):
                color = "blue"
                if (True in mouse_button):
                    if (txt == "クラフトクエスト1"):
                        self.screen_mode = BATTLECONSTANTS.get("selecte_chr")
                        battle_director.enemy_dict_make([enemy.Kuromon(100, 1, 6)])
                    elif (txt == "クラフトクエスト2"):
                        self.screen_mode = BATTLECONSTANTS.get("selecte_chr")
                        battle_director.enemy_dict_make([enemy.Kuromon(100, 2, 6)])
            else:
                color = "black"

            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 300, 90)))
            text = self.font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = self.font.size(txt)
            display.blit(text, ((x+150-(size_x/2)), (y+size_y)))
        
    def UI_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> int:
        """
        Displays the craft quest UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        
        Returns:
            int : The type of screen that should be displayed next.
        """
        self.craft_quest_button_show(display, battle_director, mouse_button, mouse_pos)
        return self.screen_mode
    

class SelectedCharacterUIDirector:
    """
    This class is director who controls the selected character UI.
    Vars:
        screen_mode (int) : The screen number currently being displayed or to be displayed next.
        selected_chr (int) : Maintains information about the selected character.
        selected_loc (int) : Miantains information about the selected location.
        page_num (int) : Maintains number of page.
    
    Functions:
        character_table_show(display, mouse_button, keyboard_pressed) : Displays the character table screen's button and text.
        selected_character_show(display, mouse_button, keyboard_pressed) : Displays the selelcted character screen's button and text.
        page_button_show(display, mouse_button, keyboard_pressed) : Displays the page button screen's button and text.
        back_and_go_button_show(display, mouse_button, keyboard_pressed) : Displays the screen back and go screen's button and text.
        UI_show(display, mouse_button, keyboard_pressed) : Displays the selected character screen UI.
    """
    def __init__(self):
        self.screen_mode = BATTLECONSTANTS.get("selecte_chr")
        
        self.character_dict = {}
        self.character_list = []
        chr_info_d = CHARACTERCONSTANTS.info.status_dict
        chr_name_d = CHARACTERCONSTANTS.info.name_dict
        chr_title_d = CHARACTERCONSTANTS.info.title_dict
        chr_element_d = CHARACTERCONSTANTS.element.element_dict
        chr_rarity_d = CHARACTERCONSTANTS.rarity.rarity_dict
        chr_class_d = CHARACTERCONSTANTS.cls.class_dict
        chr_skill_d = CHARACTERCONSTANTS.skill.skill_dict
        for number in chr_skill_d.keys():
            chr_status = chr_info_d[number]
            name, name_num = chr_name_d[chr_status[CHARACTERCONSTANTS.get("name")-1]], chr_status[CHARACTERCONSTANTS.get("name")-1]
            title, title_num = chr_title_d[chr_status[CHARACTERCONSTANTS.get("title")-1]], chr_status[CHARACTERCONSTANTS.get("title")-1]
            element, element_num = chr_element_d[chr_status[CHARACTERCONSTANTS.get("element")-1]], chr_status[CHARACTERCONSTANTS.get("element")-1]
            rarity, rarity_num = chr_rarity_d[chr_status[CHARACTERCONSTANTS.get("rarity")-1]], chr_status[CHARACTERCONSTANTS.get("rarity")-1]
            cls, cls_num = chr_class_d[chr_status[CHARACTERCONSTANTS.get("class")-1]], chr_status[CHARACTERCONSTANTS.get("class")-1]
            self.character_dict[number] = ((name, title, element, rarity, cls), (name_num, title_num, element_num, rarity_num, cls_num))
            self.character_list.append((number, (name, title, element, rarity, cls), (name_num, title_num, element_num, rarity_num, cls_num)))
        
        self.rect_pos_loc_list = [[80, 500, 'EMPTY'], [290, 500, 'EMPTY'], [500, 500, 'EMPTY'], [710, 500, 'EMPTY'], [920, 500, 'EMPTY']]
        self.rect_pos_chr_list: list[tuple[int, int, str, str, str, str]] = [(x, y, c[0], c[1][0], c[1][3], c[1][4]) for (x, y), c in zip([(110, 0), (110, 110), (110, 220), (110, 330), (220, 0), (220, 110), (220, 220), (220, 330), (330, 0), (330, 110), (330, 220), (330, 330), (440, 0), (440, 110), (440, 220), (440, 330), (550, 0), (550, 110), (550, 220), (550, 330), (660, 0), (660, 110), (660, 220), (660, 330), (770, 0), (770, 110), (770, 220), (770, 330), (880, 0), (880, 110), (880, 220), (880, 330), (990, 0), (990, 110), (990, 220), (990, 330)], self.character_list[:36])]
        
        self.selected_chr = None
        self.selected_loc = None
        self.page_num = 0
        
    def character_table_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the character table screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 30)
        for i, (x, y, txt) in enumerate(self.rect_pos_loc_list, 1):
            if (battle_director.stage_dict[i] != None):
                chr_number = battle_director.stage_dict[i].get("info").get("number")
                rarity, name, cls = self.character_dict[chr_number][0][3], self.character_dict[chr_number][0][0], self.character_dict[chr_number][0][4]
                txt1, txt2, txt3 = f"""[{rarity.replace("'", "")}]""", f"""{name[0].replace("'", "")}""", f"""({cls.replace("'", "")})"""
                self.rect_pos_loc_list[i-1][2] = [txt1, txt2, txt3]
                    
            if (x <= mouse_pos[0] <= x+200 and y <= mouse_pos[1] <= y+100):
                color = "blue"
                if (True in mouse_button):
                    self.selected_loc = i
                else:
                    if (self.selected_loc == None):
                        color = "blue"
                if (self.selected_loc == i):
                    color = "red"
            else:
                if (self.selected_loc == i):
                    color = "red"
                else:
                    color = "black"
                        
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 200, 100)))
            if (txt == "EMPTY"):
                text = font.render(txt, True, BATTLECONSTANTS.get("white"))
                size_x, size_y = font.size(txt)
                display.blit(text, ((x+100-(size_x/2)), (y+size_y)))
            else:
                for j, _txt in enumerate(txt):
                    text = font.render(_txt, True, BATTLECONSTANTS.get("white"))
                    size_x, size_y = font.size(_txt)
                    display.blit(text, ((x+100-(size_x/2)), (y+30*j)))
        
    def selected_character_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the selelcted character screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 15)
        for x, y, number, name, rarity, cls in self.rect_pos_chr_list:
            txt1, txt2, txt3 = f"""[{rarity.replace("'", "")}]""", f"""{name[0].replace("'", "")}""", f"""({cls.replace("'", "")})"""
            
            if (x <= mouse_pos[0] <= x+100 and y <= mouse_pos[1] <= y+100):
                color = "blue"
                if (True in mouse_button):
                    if (self.selected_loc != None):
                        self.selected_chr = number
                        battle_director.stage_dict[self.selected_loc] = character.Character(number, self.selected_loc)
                        self.selected_loc, self.selected_chr = None, None
                else:
                    if (self.selected_chr == None):
                        color = "blue"
                if (self.selected_chr == number):
                    color = "red"
            else:
                if (self.selected_chr == number):
                    color = "red"
                else:
                    color = "black"
                        
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 100, 100)))
            text_1, text_2, text_3 = font.render(txt1, True, BATTLECONSTANTS.get("white")), font.render(txt2, True, BATTLECONSTANTS.get("white")), font.render(txt3, True, BATTLECONSTANTS.get("white"))
            (size_1_x, size_1_y), (size_2_x, size_2_y), (size_3_x, size_3_y) = font.size(txt1), font.size(txt2), font.size(txt3)
            display.blit(text_1, ((x+50-(size_1_x/2)), (y+size_1_y)))
            display.blit(text_2, ((x+50-(size_2_x/2)), (y+size_2_y+20)))
            display.blit(text_3, ((x+50-(size_3_x/2)), (y+size_3_y+40)))
        
    def page_button_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the page button screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 15)
        for x, y, txt in [(10, 0, "back"), (1100, 0, "next"), (1100, 100, f"ページ{self.page_num+1}")]:
            if (x <= mouse_pos[0] <= x+90 and y <= mouse_pos[1] <= y+25):
                color = "blue"
                if (True in mouse_button):
                    if (txt == "back"):
                        self.page_num -= 1
                        if (self.page_num <= 0):
                            self.page_num = 0
                    elif (txt == "next"):
                        self.page_num += 1
                        if (self.page_num >= 16):
                            self.page_num = 16
                    self.rect_pos_chr_list: list[tuple[int, int, str, str, str, str]] = [(x, y, c[0], c[1][0], c[1][3], c[1][4]) for (x, y), c in zip([(110, 0), (110, 110), (110, 220), (110, 330), (220, 0), (220, 110), (220, 220), (220, 330), (330, 0), (330, 110), (330, 220), (330, 330), (440, 0), (440, 110), (440, 220), (440, 330), (550, 0), (550, 110), (550, 220), (550, 330), (660, 0), (660, 110), (660, 220), (660, 330), (770, 0), (770, 110), (770, 220), (770, 330), (880, 0), (880, 110), (880, 220), (880, 330), (990, 0), (990, 110), (990, 220), (990, 330)], self.character_list[36*self.page_num:36*(self.page_num+1)])]
            else:
                color = "black"
                
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 90, 25)))
            text = font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = font.size(txt)
            display.blit(text, ((x+25-(size_x/2)), (y)))
    
    def back_and_go_button_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the screen back and go screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 15)
        for x, y, txt in [(0, 500, "戻る"), (1150, 500, "出撃")]:
            if (x <= mouse_pos[0] <= x+50 and y <= mouse_pos[1] <= y+100):
                color = "blue"
                if (True in mouse_button):
                    if (txt == "戻る"):
                        self.screen_mode = battle_director.selected_stage
                        
                    elif (txt == "出撃"):
                        self.screen_mode = BATTLECONSTANTS.get("battle")
                        battle_director.stage_dict_make()
                        battle_director.time_line_make()
                        battle_director.hate_list_make()
                    self.rect_pos_chr_list: list[tuple[int, int, str, str, str, str]] = [(x, y, c[0], c[1][0], c[1][3], c[1][4]) for (x, y), c in zip([(110, 0), (110, 110), (110, 220), (110, 330), (220, 0), (220, 110), (220, 220), (220, 330), (330, 0), (330, 110), (330, 220), (330, 330), (440, 0), (440, 110), (440, 220), (440, 330), (550, 0), (550, 110), (550, 220), (550, 330), (660, 0), (660, 110), (660, 220), (660, 330), (770, 0), (770, 110), (770, 220), (770, 330), (880, 0), (880, 110), (880, 220), (880, 330), (990, 0), (990, 110), (990, 220), (990, 330)], self.character_list[36*self.page_num:36*(self.page_num+1)])]
            else:
                color = "black"
                
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 50, 100)))
            text = font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = font.size(txt)
            display.blit(text, ((x+25-(size_x/2)), (y)))
    
    def UI_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> int:
        """
        Displays the selected character screen UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        Returns:
            int : The type of screen that should be displayed next.
        """
        self.character_table_show(display, battle_director, mouse_button, mouse_pos)
        self.selected_character_show(display, battle_director, mouse_button, mouse_pos)
        self.page_button_show(display, battle_director, mouse_button, mouse_pos)
        self.back_and_go_button_show(display, battle_director, mouse_button, mouse_pos)
        return self.screen_mode


class TraningUIDirector:
    """
    This class is director who controls the traning UI.
    
    Vars:
        screen_mode (int) : The screen number currently being displayed or to be displayed next.
    
    Functions:
        traning_button_show(display, mouse_button, keyboard_pressed) : Displays the traning text and button.
        UI_show(display, mouse_button, keyboard_pressed) : Displays the traning UI.
    """
    def __init__(self):
        self.screen_mode = BATTLECONSTANTS.get("quest")
        
    def training_button_show(self, display: pg.Surface, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the traning screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        rect_pos_list = [(50, 50, "トレーニング"), (850, 50, "ルーム"), (50, 450, "召喚"), (850, 450, "村"), (450, 250, "クエスト")]
        font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 30)
        for x, y, txt in rect_pos_list:
            if (x <= mouse_pos[0] <= x+300 and y <= mouse_pos[1] <= y+100):
                color = "blue"
                if (True in mouse_button):
                    if (txt == "トレーニング"):
                        self.screen_mode = BATTLECONSTANTS.get("traning")
                    elif (txt == "ルーム"):
                        self.screen_mode = BATTLECONSTANTS.get("room")
                    elif (txt == "召喚"):
                        self.screen_mode = BATTLECONSTANTS.get("gacha")
                    elif (txt == "村"):
                        self.screen_mode = BATTLECONSTANTS.get("village")
                    elif (txt == "クエスト"):
                        self.screen_mode = BATTLECONSTANTS.get("quest")
            else:
                if (self.screen_mode == BATTLECONSTANTS.get("home")):
                    self.screen_mode = BATTLECONSTANTS.get("home")
                color = "black"
                        
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 300, 100)))
            text = font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = font.size(txt)
            display.blit(text, ((x+150-(size_x/2)), (y+size_y)))
        
    def UI_show(self, display: pg.Surface, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> int:
        """
        Displays the traning UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        
        Returns:
            int : The type of screen that should be displayed next.
        """
        self.training_button_show(display, mouse_button, mouse_pos)
        return self.screen_mode
    

class RoomUIDirector:
    """
    This class is director who controls the room UI.
    
    Vars:
        screen_mode (int) : The screen number currently being displayed or to be displayed next.
    
    Functions:
        room_button_show(display, mouse_button, keyboard_pressed) : Displays the room text and button.
        UI_show(display, mouse_button, keyboard_pressed) : Displays the room UI.
    """
    def __init__(self):
        self.screen_mode = BATTLECONSTANTS.get("quest")
        
    def room_button_show(self, display: pg.Surface, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the room screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        rect_pos_list = [(50, 50, "トレーニング"), (850, 50, "ルーム"), (50, 450, "召喚"), (850, 450, "村"), (450, 250, "クエスト")]
        font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 30)
        for x, y, txt in rect_pos_list:
            if (x <= mouse_pos[0] <= x+300 and y <= mouse_pos[1] <= y+100):
                color = "blue"
                if (True in mouse_button):
                    if (txt == "トレーニング"):
                        self.screen_mode = BATTLECONSTANTS.get("traning")
                    elif (txt == "ルーム"):
                        self.screen_mode = BATTLECONSTANTS.get("room")
                    elif (txt == "召喚"):
                        self.screen_mode = BATTLECONSTANTS.get("gacha")
                    elif (txt == "村"):
                        self.screen_mode = BATTLECONSTANTS.get("village")
                    elif (txt == "クエスト"):
                        self.screen_mode = BATTLECONSTANTS.get("quest")
            else:
                if (self.screen_mode == BATTLECONSTANTS.get("home")):
                    self.screen_mode = BATTLECONSTANTS.get("home")
                color = "black"
                        
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 300, 100)))
            text = font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = font.size(txt)
            display.blit(text, ((x+150-(size_x/2)), (y+size_y)))
        
    def UI_show(self, display: pg.Surface, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> int:
        """
        Displays the room UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        
        Returns:
            int : The type of screen that should be displayed next.
        """
        self.room_button_show(display, mouse_button, mouse_pos)
        return self.screen_mode


class GachaUIDirector:
    """
    This class is director who controls the gacha UI.
    
    Vars:
        screen_mode (int) : The screen number currently being displayed or to be displayed next.
    
    Functions:
        gacha_button_show(display, mouse_button, keyboard_pressed) : Displays the gacha text and button.
        UI_show(display, mouse_button, keyboard_pressed) : Displays the gacha UI.
    """
    def __init__(self):
        self.screen_mode = BATTLECONSTANTS.get("quest")
        
    def gacha_button_show(self, display: pg.Surface, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the gacha screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        rect_pos_list = [(50, 50, "トレーニング"), (850, 50, "ルーム"), (50, 450, "召喚"), (850, 450, "村"), (450, 250, "クエスト")]
        font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 30)
        for x, y, txt in rect_pos_list:
            if (x <= mouse_pos[0] <= x+300 and y <= mouse_pos[1] <= y+100):
                color = "blue"
                if (True in mouse_button):
                    if (txt == "トレーニング"):
                        self.screen_mode = BATTLECONSTANTS.get("traning")
                    elif (txt == "ルーム"):
                        self.screen_mode = BATTLECONSTANTS.get("room")
                    elif (txt == "召喚"):
                        self.screen_mode = BATTLECONSTANTS.get("gacha")
                    elif (txt == "村"):
                        self.screen_mode = BATTLECONSTANTS.get("village")
                    elif (txt == "クエスト"):
                        self.screen_mode = BATTLECONSTANTS.get("quest")
            else:
                if (self.screen_mode == BATTLECONSTANTS.get("home")):
                    self.screen_mode = BATTLECONSTANTS.get("home")
                color = "black"
                        
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 300, 100)))
            text = font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = font.size(txt)
            display.blit(text, ((x+150-(size_x/2)), (y+size_y)))
        
    def UI_show(self, display: pg.Surface, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> int:
        """
        Displays the gacha UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        
        Returns:
            int : The type of screen that should be displayed next.
        """
        self.gacha_button_show(display, mouse_button, mouse_pos)
        return self.screen_mode


class VillageUIDirector:
    """
    This class is director who controls the village UI.
    
    Vars:
        screen_mode (int) : The screen number currently being displayed or to be displayed next.
    
    Functions:
        village_button_show(display, mouse_button, keyboard_pressed) : Displays the village text and button.
        UI_show(display, mouse_button, keyboard_pressed) : Displays the village UI.
    """
    def __init__(self):
        self.screen_mode = BATTLECONSTANTS.get("quest")
        
    def village_button_show(self, display: pg.Surface, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> None:
        """
        Displays the village screen's button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        """
        rect_pos_list = [(50, 50, "トレーニング"), (850, 50, "ルーム"), (50, 450, "召喚"), (850, 450, "村"), (450, 250, "クエスト")]
        font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 30)
        for x, y, txt in rect_pos_list:
            if (x <= mouse_pos[0] <= x+300 and y <= mouse_pos[1] <= y+100):
                color = "blue"
                if (True in mouse_button):
                    if (txt == "トレーニング"):
                        self.screen_mode = BATTLECONSTANTS.get("traning")
                    elif (txt == "ルーム"):
                        self.screen_mode = BATTLECONSTANTS.get("room")
                    elif (txt == "召喚"):
                        self.screen_mode = BATTLECONSTANTS.get("gacha")
                    elif (txt == "村"):
                        self.screen_mode = BATTLECONSTANTS.get("village")
                    elif (txt == "クエスト"):
                        self.screen_mode = BATTLECONSTANTS.get("quest")
            else:
                if (self.screen_mode == BATTLECONSTANTS.get("home")):
                    self.screen_mode = BATTLECONSTANTS.get("home")
                color = "black"
                        
            pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((x, y, 300, 100)))
            text = font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = font.size(txt)
            display.blit(text, ((x+150-(size_x/2)), (y+size_y)))
        
    def UI_show(self, display: pg.Surface, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> int:
        """
        Displays the village UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            mouse_button (tuple) : Which button on the mouse is pressed.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        
        Returns:
            int : The type of screen that should be displayed next.
        """
        self.village_button_show(display, mouse_button, mouse_pos)
        return self.screen_mode


class BattleUIDirector:
    """
    This class is director who controls the battle UI.
    
    Vars:
        screen_mode (int) : The number of the currently displayed screen or the next screen to be displayed.
        character_skill_flag (int) : Information about which skill the mouse cursor is on.
        character_skill_put_flag (Skill) : Information about which skill the player has selected.
        character_flag (int) : Information about which character the player has selected.
    
    Functions:
        character_skill_button_show(display, battle_director, mouse_button, mouse_pos) : 
        character_skill_information_show(display, battle_director, mouse_button, mouse_pos) : 
        character_button_show(display, battle_director, mouse_button, mouse_pos) : 
        time_line_show(display, battle_director, mouse_button, mouse_pos) : 
        character_action_log_show(display, battle_director, mouse_button, mouse_pos) : 
        character_jamp_gauge_show(display, battle_director, mouse_button, mouse_pos) : 
        character_selected_name_show(display, battle_director, mouse_button, mouse_pos) : 
        character_selected_name_show(display, battle_director, mouse_button, mouse_pos) : 
        auto_button_show(display, battle_director, mouse_button, mouse_pos) : 
        UI_show(display, battle_director, mouse_button, mouse_pos) : 

    """
    def __init__(self):
        self.screen_mode = BATTLECONSTANTS.get("battle")
        self.font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 20)
        self.chr_info_d = CHARACTERCONSTANTS.info.status_dict
        self.chr_name_d = CHARACTERCONSTANTS.info.name_dict
        self.chr_title_d = CHARACTERCONSTANTS.info.title_dict
        self.chr_element_d = CHARACTERCONSTANTS.element.element_dict
        self.chr_rarity_d = CHARACTERCONSTANTS.rarity.rarity_dict
        self.chr_class_d = CHARACTERCONSTANTS.cls.class_dict
        self.chr_skill_d = CHARACTERCONSTANTS.skill_info.skill_data_dict
        
        self.character_skill_list: list[tuple[int, str]] = [(0, "サポート"), (200, "とっておき"), (500, "スキル2"), (650, "スキル1"), (800, "通常"), (1100, "交代")]   # (350, "ぶきスキル")
        self.character_skill_flag: int = None
        self.character_skill_put_flag: character.Skill = None
        
        self.character_list: list[int] = [760, 910, 1060, 300, 150, 0]
        self.character_location_list: list[int] = [1, 2, 3, 6, 7, 8]
        self.character_flag: int = None
        
    def character_skill_button_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]):
        """
        Displays the character's skill button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            battle_director (BattleDirector) : Maintains BatteDirector information.
            mouse_button (tuple) : Which button on the mouse is pressed.
            mouse_button (tuple) : Where is the mouse position.
        """
        for x, txt in self.character_skill_list:
            if (txt == "スキル1"):
                txt = ["スキル1", f"{battle_director.now_act_character.skill.first_skill.recast}/{battle_director.now_act_character.skill.first_skill.def_recast}"]
            elif (txt == "スキル2"):
                txt = ["スキル2", f"{battle_director.now_act_character.skill.second_skill.recast}/{battle_director.now_act_character.skill.second_skill.def_recast}"]
            
            if (x <= mouse_pos[0] <= x+100 and 500 <= mouse_pos[1] <= 500+100):
                if (txt == "通常"):
                    self.character_skill_put_flag = battle_director.now_act_character.skill.normal_skill
                elif ("スキル1" in txt):
                    self.character_skill_put_flag = battle_director.now_act_character.skill.first_skill
                elif ("スキル2" in txt):
                    self.character_skill_put_flag = battle_director.now_act_character.skill.second_skill
                # elif (x == "ぶきスキル"):
                #     self.character_skill_put_flag = battle_director.now_act_character.weapon.skill
                elif (txt == "とっておき"):
                    self.character_skill_put_flag = battle_director.now_act_character.skill.jamp_skill
        
                if (True in mouse_button):
                    if (self.character_skill_flag == x and ((None not in battle_director.selected_character[0]) or (None not in battle_director.selected_character[1]))):
                        if ("スキル1" in txt):
                            battle_director.now_act_character.skill.first_skill.recast = -1
                        elif ("スキル2" in txt):
                            battle_director.now_act_character.skill.second_skill.recast = -1

                        battle_director.character_act()
                        self.character_flag = None
                        self.character_skill_flag = None
                        self.character_skill_put_flag = None
                    
                    if (txt == "サポート"):
                        pass
                    elif (txt == "交代"):
                        pass
                    else:
                        if ("スキル1" in txt):
                            if (battle_director.now_act_character.skill.first_skill.recast == 0):
                                self.character_skill_flag = x
                                battle_director.selected_skill_set("スキル1")
                        elif ("スキル2" in txt):
                            if (battle_director.now_act_character.skill.second_skill.recast == 0):
                                self.character_skill_flag = x
                                battle_director.selected_skill_set("スキル2")
                        else:
                            self.character_skill_flag = x
                            battle_director.selected_skill_set(txt)
                        
                if (self.character_skill_flag == x):
                    skill_color = "red"
                else:
                    skill_color = "blue"
            else:
                if (self.character_skill_flag == x):
                    skill_color = "red"
                else:
                    skill_color = "black"
                        
            pg.draw.rect(display, BATTLECONSTANTS.get(skill_color), pg.Rect((x, 500, 100, 100)))
            if (type(txt) == str):
                text = self.font.render(txt, True, BATTLECONSTANTS.get("white"))
                size_x, size_y = self.font.size(txt)
                display.blit(text, ((x+50-(size_x/2)), (500+size_y+20)))
            else:
                for i, t in enumerate(txt):
                    text = self.font.render(t, True, BATTLECONSTANTS.get("white"))
                    size_x, size_y = self.font.size(t)
                    display.blit(text, ((x+50-(size_x/2)), (500+size_y+20+(i*20))))
        
    def character_skill_information_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]):
        """
        Displays the character's skill information button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            battle_director (BattleDirector) : Maintains BatteDirector information.
            mouse_button (tuple) : Which button on the mouse is pressed.
            mouse_pos (tuple) : Where is the mouse position.
        """
        try:
            if (battle_director.selected_skill != None):
                txt = battle_director.selected_skill.effect
            else:
                txt = self.character_skill_put_flag.effect
        except:
            txt = ""
        
        pg.draw.rect(display, BATTLECONSTANTS.get("black"), pg.Rect((100, 460, 900, 30)))
        text = self.font.render(txt, True, BATTLECONSTANTS.get("white"))
        display.blit(text, (100, (460+5)))
        
    def character_button_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]):
        """
        Displays the character button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            battle_director (BattleDirector) : Maintains BatteDirector information.
            mouse_button (tuple) : Which button on the mouse is pressed.
            mouse_pos (tuple) : Where button on the mouse is position.
        """
        for x, loc, c in zip(self.character_list, self.character_location_list, list(battle_director.act_character_dict.values())+list(battle_director.act_enemy_dict.values())):
            if (c == None):
                pass
            else:
                if (x <= mouse_pos[0] <= x+140 and 200 <= mouse_pos[1] <= 200+100):
                    if (True in mouse_button):
                        self.character_flag = loc
                        battle_director.selected_character_set(loc)
                    if (self.character_flag == loc):
                        chr_color = "red"
                    else:
                        chr_color = "blue"
                else:
                    if (self.character_flag == loc):
                        chr_color = "red"
                    else:
                        chr_color = "black"
                    
                try:
                    name_txt = [f"""[{self.chr_rarity_d[c.information.get("rare")]}]""", f"""{self.chr_name_d[c.information.get("name")][0]}""", f"""({self.chr_class_d[c.information.get("class")]})"""]
                except:
                    name_txt = [f"""{c.information.get("name")}"""]
                
                font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 15)
                pg.draw.rect(display, BATTLECONSTANTS.get(chr_color), pg.Rect((x, 200, 140, 100)))
                for i, txt in enumerate(name_txt):
                    txt = txt.replace("'", "")
                    text = font.render(txt, True, BATTLECONSTANTS.get("white"))
                    size_x, size_y = font.size(txt)
                    display.blit(text, ((x+70-(size_x/2)), (200+size_y+i*20)))
                
                font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 15)
                hp_txt = f"""{int(c.status.get("HP"))}/{c.status.get("DEFHP")}"""
                pg.draw.rect(display, BATTLECONSTANTS.get(chr_color), pg.Rect((x, 110, 140, 50)))
                text = font.render(hp_txt, True, BATTLECONSTANTS.get("white"))
                size_x, size_y = font.size(hp_txt)
                display.blit(text, ((x+70-(size_x/2)), (110)))
                
                stan_txt = f"""stan : {round(c.information.get("stan"), 1)}"""
                text = self.font.render(stan_txt, True, BATTLECONSTANTS.get("white"))
                size_x, size_y = self.font.size(stan_txt)
                display.blit(text, ((x+70-(size_x/2)), (110+20)))
            
    def time_line_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]):
        """
        Displays the time line button and text.

        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            battle_director (BattleDirector) : Maintains BatteDirector information.
            mouse_button (tuple) : Which button on the mouse is pressed.
            mouse_pos (tuple) : Where button on the mouse is position.
        """
        x = 1050
        for c in battle_director.time_line_list:
            try:
                txt = f"""{self.chr_name_d[c.information.get("name")][0]}{c.information.get("location")}"""
            except:
                txt = c.information.get("name") + str(c.information.get("location"))
            if (x == 1050):
                pg.draw.rect(display, BATTLECONSTANTS.get("red"), pg.Rect((x, 400, 150, 50)))
            else:
                pg.draw.rect(display, BATTLECONSTANTS.get("black"), pg.Rect((x, 400, 150, 50)))
                
            font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 10)
            text = font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = font.size(txt)
            display.blit(text, ((x+50-(size_x/2)), (400)))
            
            txt = str(int(c.information.get("delay")))
            text = self.font.render(txt, True, BATTLECONSTANTS.get("white"))
            size_x, size_y = self.font.size(txt)
            display.blit(text, ((x+50-(size_x/2)), (400+20)))
            x -= 160
        
    def character_action_log_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]):
        """
        Displays the character's action logging button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            battle_director (BattleDirector) : Maintains BatteDirector information.
            mouse_button (tuple) : Which button on the mouse is pressed.
            mouse_pos (tuple) : Where button on the mouse is position.
        """
        font = pg.font.Font("Data/ipaexg00401/ipaexg.ttf", 15)
        pg.draw.rect(display, BATTLECONSTANTS.get("black"), pg.Rect((0, 0, 1050, 100)))
        for i, log in enumerate(battle_director.act_log_list):
            display.blit(font.render(log, True, BATTLECONSTANTS.get("white")), (1, i*15))
        
    def character_jamp_gauge_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]):
        """
        Displays the character's jamp gauge button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            battle_director (BattleDirector) : Maintains BatteDirector information.
            mouse_button (tuple) : Which button on the mouse is pressed.
            mouse_pos (tuple) : Where button on the mouse is position.
        """
        pg.draw.rect(display, BATTLECONSTANTS.get("black"), pg.Rect((0, 350, 200, 50)))
        display.blit(self.font.render("とっておき : " + str(battle_director.jamp_gauge), True, BATTLECONSTANTS.get("white")), (1, 350))
        
    def character_selected_skill_name_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]):
        """
        Displays the character's selected skill name button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            battle_director (BattleDirector) : Maintains BatteDirector information.
            mouse_button (tuple) : Which button on the mouse is pressed.
            mouse_pos (tuple) : Where button on the mouse is position.
        """
        pg.draw.rect(display, (0, 0, 0), pg.Rect(300, 360, 700, 30))
        try:
            if (battle_director.selected_skill != None):
                skill_name = battle_director.selected_skill.name
            else:
                skill_name = self.character_skill_put_flag.name
            display.blit(self.font.render(skill_name, True, BATTLECONSTANTS.get("white")), (301, 363))
        except:
            pass
        
    def character_selected_character_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]):
        """
        Displays the character's selected character button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            battle_director (BattleDirector) : Maintains BatteDirector information.
            mouse_button (tuple) : Which button on the mouse is pressed.
            mouse_pos (tuple) : Where button on the mouse is position.
        """
        pg.draw.rect(display, BATTLECONSTANTS.get("black"), pg.Rect((450, 150, 300, 200)))
        display.blit(self.font.render("選択されたキャラクター", True, BATTLECONSTANTS.get("white")), (451, 150))
        for i, chr in enumerate(battle_director.selected_character[0]+battle_director.selected_character[1], 1):
            if (chr == None):
                pass
            else:
                try:
                    txt = f"""{self.chr_name_d[chr.information.get("name")][0]}{chr.information.get("location")}"""
                except:
                    txt = chr.information.get("name") + str(chr.information.get("location"))
                display.blit(self.font.render(txt, True, BATTLECONSTANTS.get("white")), (451, 150 + (i*15)))
                
    def auto_button_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]):
        """
        Displays the auto button and text.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            battle_director (BattleDirector) : Maintains BatteDirector information.
            mouse_button (tuple) : Which button on the mouse is pressed.
            mouse_pos (tuple) : Where button on the mouse is position.
        """
        if (1100 <= mouse_pos[0] <= 1100+100 and 0 <= mouse_pos[1] <= 50):
            if (True in mouse_button):
                if (battle_director.auto_mode == True):
                    battle_director.auto_mode = False
                else:
                    battle_director.auto_mode = True
            color = "blue"
        else:
            color = "black"
            
        if (battle_director.auto_mode == True):
            color = "red"
            
        pg.draw.rect(display, BATTLECONSTANTS.get(color), pg.Rect((1100, 0, 100, 50)))
        display.blit(self.font.render("AUTO", True, BATTLECONSTANTS.get("white")), (1101, 0))
        
    def UI_show(self, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int, int]) -> int:
        """
        Displays the title UI.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            battle_director (BattleDirector) : Maintains BatteDirector information.
            mouse_button (tuple) : Which button on the mouse is pressed.
            mouse_pos (tuple) : Where button on the mouse is position.
        
        Returns:
            int : The type of screen that should be displayed next.
        """
        try:
            self.character_skill_button_show(display, battle_director, mouse_button, mouse_pos)
            self.character_skill_information_show(display, battle_director, mouse_button, mouse_pos)
            self.character_button_show(display, battle_director, mouse_button, mouse_pos)
            self.time_line_show(display, battle_director, mouse_button, mouse_pos)
            self.character_action_log_show(display, battle_director, mouse_button, mouse_pos)
            self.character_jamp_gauge_show(display, battle_director, mouse_button, mouse_pos)
            self.character_selected_skill_name_show(display, battle_director, mouse_button, mouse_pos)
            self.character_selected_character_show(display, battle_director, mouse_button, mouse_pos)
            self.auto_button_show(display, battle_director, mouse_button, mouse_pos)
        except:
            self.character_button_show(display, battle_director, mouse_button, mouse_pos)
            self.time_line_show(display, battle_director, mouse_button, mouse_pos)
            self.character_action_log_show(display, battle_director, mouse_button, mouse_pos)
            self.character_jamp_gauge_show(display, battle_director, mouse_button, mouse_pos)
            self.character_selected_character_show(display, battle_director, mouse_button, mouse_pos)
            self.auto_button_show(display, battle_director, mouse_button, mouse_pos)
            battle_director.character_act()
        return self.screen_mode


class UIdirector:
    """
    This class is director who controls the all UI.
    
    Vars:
        title_UI (Title_UIDirector) : Maintains the specified UI information.
        home_UI (HomeUIDirector) : Maintains the specified UI information.
        training_UI (TraningUIDirector) : Maintains the specified UI information.
        room_UI (RoomUIDirector) : Maintains the specified UI information.
        village_UI (VillageUIDirector) : Maintains the specified UI information.
        gacha_UI (GachaUIDirector) : Maintains the specified UI information.
        quest_UI (QuestUIDirector) : Maintains the specified UI information.
        main_quest_UI (MainQuestUIDirector) : Maintains the specified UI information.
        event_quest_UI (EventQuestUIDirector) : Maintains the specified UI information.
        writer_quest_UI (WriterQuestUIDirector) : Maintains the specified UI information.
        day_quest_UI (DayQuestUIDirector) : Maintains the specified UI information.
        challenge_quest_UI (ChallengeQuestUIDirector) : Maintains the specified UI information.
        memorials_quest_UI (MemorialsQuestUIDirector) : Maintains the specified UI information.
        craft_quest_UI (CraftQuestUIDirector) : Maintains the specified UI information.
        selected_character_UI (SelectedCharacterUIDirector) : Maintains the specified UI information.
        battle_UI (BattleUIDirector) : Maintains the specified UI information.
        
    Functions:
        UI_show(screen_mode, display, battle_director, mouse_button, mouse_pos, keyboard_pressed) : Displays the UI that should be displayed based on the current screen state.
    """
    def __init__(self):
        self.title_UI = TitleUIDirector()
        self.home_UI = HomeUIDirector()
        self.traning_UI = TraningUIDirector()
        self.room_UI = RoomUIDirector()
        self.village_UI = VillageUIDirector()
        self.gacha_UI = GachaUIDirector()
        self.quest_UI = QuestUIDirector()
        self.main_quest_UI = MainQuestUIDirector()
        self.event_quest_UI = EventQuestUIDirector()
        self.writer_quest_UI = WriterQuestUIDirector()
        self.day_quest_UI = DayQuestUIDirector()
        self.challenge_quest_UI = ChallengeQuestUIDirector()
        self.memorials_quest_UI = MemorialsQuestUIDirector()
        self.craft_quest_UI = CraftQuestUIDirector()
        self.selected_character_UI = SelectedCharacterUIDirector()
        self.battle_UI = BattleUIDirector()
        
    def UI_show(self, screen_mode: int, display: pg.Surface, battle_director: BattleDirector, mouse_button: tuple[bool, bool, bool], mouse_pos: tuple[int, int], keyboard_pressed: bool) -> int:
        """
        Displays the UI that should be displayed based on the current screen state.
        
        Args:
            display (pg.Surface) : The Surface instance displaying the screen.
            battle_director (BattleDirector) : Maintains BatteDirector information.
            mouse_button (tuple) : Which button on the mouse is pressed.
            mouse_pos (tuple) : Where button on the mouse is position.
            keyboard_pressed (bool) : Which button on the keyboard is pressed.
        
        Returns:
            int : The type of screen that should be displayed next.
        """
        if (screen_mode == BATTLECONSTANTS.get("title")):
            pg.display.set_caption("Title Mode")
            return self.title_UI.UI_show(display, mouse_button, keyboard_pressed)
        
        elif (screen_mode == BATTLECONSTANTS.get("home")):
            pg.display.set_caption("Home Mode")
            return self.home_UI.UI_show(display, mouse_button, mouse_pos)
        elif (screen_mode == BATTLECONSTANTS.get("village")):
            pg.display.set_caption("Village Mode")
        elif (screen_mode == BATTLECONSTANTS.get("room")):
            pg.display.set_caption("Room Mode")
        elif (screen_mode == BATTLECONSTANTS.get("gacha")):
            pg.display.set_caption("Gacha Mode")
        elif (screen_mode == BATTLECONSTANTS.get("traning")):
            pg.display.set_caption("Traning Mode")
        elif (screen_mode == BATTLECONSTANTS.get("quest")):
            pg.display.set_caption("Quest Mode")
            return self.quest_UI.UI_show(display, battle_director, mouse_button, mouse_pos)
        
        elif (screen_mode == BATTLECONSTANTS.get("main")):
            self.main_quest_UI = MainQuestUIDirector()
            pg.display.set_caption("Main Quest Mode")
            return self.main_quest_UI.UI_show(display, battle_director, mouse_button, mouse_pos)
        elif (screen_mode == BATTLECONSTANTS.get("event")):
            self.event_quest_UI = EventQuestUIDirector()
            pg.display.set_caption("Event Quest Mode")
            return self.event_quest_UI.UI_show(display, battle_director, mouse_button, mouse_pos)
        elif (screen_mode == BATTLECONSTANTS.get("writer")):
            self.writer_quest_UI = WriterQuestUIDirector()
            pg.display.set_caption("Writer Quest Mode")
            return self.writer_quest_UI.UI_show(display, battle_director, mouse_button, mouse_pos)
        elif (screen_mode == BATTLECONSTANTS.get("day")):
            self.day_quest_UI = DayQuestUIDirector()
            pg.display.set_caption("Day Quest Mode")
            return self.day_quest_UI.UI_show(display, battle_director, mouse_button, mouse_pos)
        elif (screen_mode == BATTLECONSTANTS.get("challenge")):
            self.challenge_quest_UI = ChallengeQuestUIDirector()
            pg.display.set_caption("Challenge Quest Mode")
            return self.challenge_quest_UI.UI_show(display, battle_director, mouse_button, mouse_pos)
        elif (screen_mode == BATTLECONSTANTS.get("memorials")):
            self.memorials_quest_UI = MemorialsQuestUIDirector()
            pg.display.set_caption("Memorial Quest Mode")
            return self.memorials_quest_UI.UI_show(display, battle_director, mouse_button, mouse_pos)
        elif (screen_mode == BATTLECONSTANTS.get("craft")):
            self.craft_quest_UI = CraftQuestUIDirector()
            pg.display.set_caption("Craft Quest Mode")
            return self.craft_quest_UI.UI_show(display, battle_director, mouse_button, mouse_pos)

        elif (screen_mode == BATTLECONSTANTS.get("selecte_chr")):
            self.selected_character_UI.screen_mode = BATTLECONSTANTS.get("selecte_chr")
            pg.display.set_caption("Selected Character Mode")
            return self.selected_character_UI.UI_show(display, battle_director, mouse_button, mouse_pos)
            
        elif (screen_mode == BATTLECONSTANTS.get("battle")):
            pg.display.set_caption("Battle Mode")
            return self.battle_UI.UI_show(display, battle_director, mouse_button, mouse_pos)
         
   
class GameDirector:
    """
    This class is director who controls the all game screen.
    
    Vars:
        battle_director (battleDirector) : Maintains BattleDirector information.
        UI_director (UIDirector) : Maintains UIDirector information.
        clock_obj (pg.time.Clock) : Maintains information on the Clock Instagram of python's time module.
        mouse_button (tuple) : Which button on the mouse is pressed.
        mouse_pos (tuple) : Where button on the mouse is position.
        keyboard_pressed (bool) : Which button on the keyboard is pressed.
        screen_flag (int) : The screen number currently being displayed or to be displayed next.
    
    Functions:
        screen_show() : Display the specified screen.
        pygame_event_get() : Get pygame events and get mouse position, input, and keyboard input.
    """
    def __init__(self):
        pg.init()
        self.battle_director: BattleDirector = BattleDirector(None)
        self.UI_director: UIdirector = UIdirector()
        self.clock_obj = pg.time.Clock().tick(30)
        self.mouse_position: tuple[float, float] = (0.0, 0.0)
        self.mouse_button: tuple[bool, bool, bool] = (False, False, False)
        self.keyboard_pressed: tuple = ()
        self.screen_flag: int = BATTLECONSTANTS.get("battle")
        
        self.battle_director.stage_dict: dict[int, Union[character.Character, enemy.Kuromon]] = {1 : character.Character(1, 1), 2 : character.Character(1, 2), 3 : character.Character(1, 3), 4 : character.Character(1, 4), 5 : character.Character(1, 5), 6 : enemy.Kuromon(100, 1, 6), 7 : enemy.Kuromon(90, 2, 7), 8 : enemy.Kuromon(80, 3, 8)}
        self.battle_director.stage_dict_make()
        self.battle_director.time_line_make()
        
    def screen_show(self) -> None:
        """
        Show game UI.
        """
        while (True):
            pg.init()
            self.pygame_event_get()
            display = pg.display.set_mode((1200, 600))
            display.fill(BATTLECONSTANTS.get("white"))
               
            self.screen_flag = self.UI_director.UI_show(self.screen_flag, display, self.battle_director, self.mouse_button, self.mouse_position, self.keyboard_pressed)
            
            pg.display.update()
            pg.display.update()
          
    def auto_directory_delete(self) -> None:
        """
        Delete the folder that is automatically generated when the python file is executed. In particular, delete the temp folder and pycache folder. 
        
        The respective folder paths are "kota" and "Script/__pycache__". 
        """
        TEMP_DIR_PATH = "kota"
        PYCACHE_DIR_PATH = "Scripts/__pycache__"
        PYTHON_TEMP_PATH = "Scripts/tempCodeRunnerFile.py"
        
        # print("-" * 150)
        if (os.path.isdir(TEMP_DIR_PATH)):
            shutil.rmtree(TEMP_DIR_PATH)
            # print("tempフォルダの削除に成功しました。")
        if (os.path.isdir(PYCACHE_DIR_PATH)):
            shutil.rmtree(PYCACHE_DIR_PATH)
            # print("pycacheフォルダの削除に成功しました。")
        if (os.path.isfile(PYTHON_TEMP_PATH)):
            os.remove(PYTHON_TEMP_PATH)
            # print("python tempファイルの削除に成功しました。")
        # print("-" * 150)
            
    def pygame_event_get(self) -> None:
        """
        Get information about program termination, keyboard presses, mouse position, and mouse button presses for python events.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.auto_directory_delete()
                pg.quit()
                sys.exit()
                    
            if event.type == pg.KEYDOWN:
                self.keyboard_pressed = True in pg.key.get_pressed()
                if event.key == pg.K_ESCAPE:
                    self.auto_directory_delete()
                    pg.quit()
                    sys.exit()
                        
            if event.type == pg.MOUSEMOTION:
                self.mouse_position = pg.mouse.get_pos()
                    
            if event.type == pg.MOUSEBUTTONDOWN:
                self.mouse_button = pg.mouse.get_pressed()
                    
            elif event.type != pg.MOUSEBUTTONDOWN:
                self.mouse_button = False, False, False


def main():
    game_director = GameDirector()
    game_director.screen_show()

###
# Finishing that defines the class.
###

###
# Test
###


if __name__ == "__main__":
    os.system("cls")
    print("\n")
    
    # battle_director = BattleDirector((None))
    # battle_director.stage_dict = {1 : character.Character(1, 1), 2 : character.Character(2, 2)}
    # e1, e2 = enemy.Kuromon(90, 1, 6), enemy.Kuromon(90, 2, 7)
    # ADDING_HP = 10000000
    # e1.status.HP += ADDING_HP
    # e2.status.HP += ADDING_HP
    # e1.status.DEFHP += ADDING_HP
    # e2.status.DEFHP += ADDING_HP
    # battle_director.enemy_dict_make([e1, e2])
    # battle_director.stage_dict_make()
    # battle_director.time_line_make()
    # battle_director.hate_list_make()
    
    # battle_director.character_ai_act()
    
    # GameDirector().auto_directory_delete()
    # main()

###
# Test
###
