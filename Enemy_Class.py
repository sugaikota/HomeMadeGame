# coding: UTF-8

###
# This code was created by Kota Sugai.
###

from Character_Class import *
from typing import Union
import numpy as np

###
# Started that defines the character class.
###

class Enemy:
    """
    This class holds information about all enemy's information.
    """
    def __init__(self, number: int, location: int):
        self.information = CharacterInformation(number, location)
        self.status = CharacterStatus()
        self.abnormal_status = CharacterAbnormal()
        self.condition_status = CharacterCondition()

    def get(self, typ: str) -> Union[CharacterInformation, CharacterStatus, CharacterAbnormal, CharacterCondition, CharacterSkill]:
        """
        Gets the value of the specified parameter.
        """
        if (typ == "info"):
            return self.information
        elif (typ == "status"):
            return self.status
        elif (typ == "abnormal"):
            return self.abnormal_status
        elif (typ == "condition"):
            return self.condition_status
        
    def information_make(self, level_correction: bool):
        """
        Make the information of character's information.
        """
        status_list = CONSTANTS.get("enemy_status_dict")[self.information.get("number")]
        if (level_correction == True):
            HP, ATK, MAT, DEF, MDF, SPD = np.array(status_list[:6]) * (self.information.get("level")-1)
        else:
            HP, ATK, MAT, DEF, MDF, SPD = np.array(status_list[:6])
        self.status.set("HP", HP)
        self.status.set("ATK", ATK)
        self.status.set("MAT", MAT)
        self.status.set("DEF", DEF)
        self.status.set("MDF", MDF)
        self.status.set("SPD", SPD)
        self.status.set("DEFHP", HP)
        self.status.set("DEFATK", ATK)
        self.status.set("DEFMAT", MAT)
        self.status.set("DEFDEF", DEF)
        self.status.set("DEFMDF", MDF)
        self.status.set("DEFSPD", SPD)
        self.status.set("LUK", status_list[6])
        self.status.set("DEFLUK", status_list[6])
        self.information.set("stan_coefficient", status_list[7])
        self.information.set("max_charge", status_list[8])
        self.information.set("delay", SkillFunction().delay_calc(self, 100))
        
    def status_calc(self):
        """
        Calculate the actual status from status change.
        """
        self.status.status_calc()
        self.abnormal_status.abnormal_turn_calc()
        self.condition_status.condition_turn_calc()

    def character_selecte(self, chr_list: list[Character], priority_cls: int):
        """
        This function selects a character depending on the priority of the selected character.
        """
        random = np.random.randint(1, 101)
        for c in chr_list:
            if (c.information._class == priority_cls and random == 50):
                return c
        return None


"""
skill_name : skill_type, skill_delay, skill_recast, skill_charge, skill_info, skill_rate, status_type, reset_bool, skill_prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num]
敵単体に物理の小ダメージ (0, 115, 0, 1, 'ene_single_physics_attack', 1457, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
敵単体に炎属性の小ダメージ (1, 115, 0, 1, 'ene_single_magic_attack', 1492, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
味方単体を小回復 (2, 125, 0, 1, 'chr_single_recover', 42.0, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
味方単体のATKが一定ターン小アップ (3, 65, 0, 1, 'chr_single_status_change', 22.2, 1, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
味方単体の一定ターンATKアップ効果を解除 (4, 0, 1, 8, 'chr_single_status_reset', 'None', 1, '1', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
味方単体の一定ターンステータスダウン効果を一定ターン無効化 (5, 80, 16, 9, 'chr_single_status_invalid', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
味方単体に低確率でこんらんを付与 (6, 90, 0, 1, 'chr_single_set_abnormal', 'None', 'None', 'None', 30, 0, 'None', 'None', 'None', 'None', 'None', 'None')  
味方単体のこんらんを解除 (7, 90, 0, 1, 'self_abnormal_reset', 'None', 'None', 'None', 'None', 0, 'None', 'None', 'None', 'None', 'None', 'None')
味方単体の状態異常を一定ターン無効化 (8, 80, 0, 1, 'chr_single_abnormal_invalid', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
味方単体の状態異常耐性が一定ターン小アップ (9, 90, 0, 1, 'chr_single_abnormal_probability_change', -10.0, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
味方単体の炎属性耐性が一定ターン小アップ (10, 65, 0, 1, 'chr_single_element_resistance_change', 14.8, 17, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
味方単体の有利属性へのダメージが一定ターンアップ (11, 65, 0, 1, 'chr_single_status_change', 35.0, 23, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
味方単体の物理攻撃が一度だけ小アップ (12, 55, 0, 1, 'chr_single_set_NEXTbuff', 51.8, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
味方単体の魔法攻撃が一度だけ小アップ (13, 55, 0, 1, 'chr_single_set_NEXTbuff', 51.8, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
味方単体の攻撃が一度だけクリティカルになる (14, 55, 0, 1, 'chr_single_set_NEXTbuff', 1.0, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
味方単体に1回だけ攻撃を完全カットするバリアを張る (15, 140, 0, 1, 'chr_single_set_barrier', 100.0, 'None', 'None', 'None', 'None', 1, 'None', 'None', 'None', 'None', 'None')
味方単体のリキャストをかなり減らす (16, 75, 0, 1, 'chr_single_recast_change', -35.0, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
とっておきゲージをかなり増やす (17, 130, 0, 1, 'jamp_gauge_change', 66.0, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None') 
味方単体の狙われやすさが一定ターン小アップ (18, 120, 0, 1, 'chr_single_status_change', 20, 15, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
敵単体のチャージカウントを減らす(-10) (19, 70, 0, 1, 'ene_single_charge_change', 10, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
味方全体を小回復するスキルカードを3枚設置 (20, 120, 0, 1, 'set_skillcard', 'None', 'None', 'None', 'None', 'None', 'None', 'chr_whole_recover', 19.0, 100, 13, 3)
自身にリカバリーを付与 (21, 140, 0, 1, 'self_set_recovery', 39.0, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
自身にクイックドロウを付与 (22, 45, 0, 1, 'self_status_change', -82.5, 24, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
味方単体にがまんを付与 (23, 85, 0, 1, 'chr_single_set_patience', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')  
味方単体のクリティカル時ダメージが一定ターン小アップ (24, 65, 0, 1, 'chr_single_status_change', 17.0, 14, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
敵単体に物理の特殊ダメージを与える (25, 80, 0, 1, 'chr_single_fixed_damage', 2500, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
"""


class Kuromon(Enemy):
    """
    This class holds information about "Kuromon", which is one of the Enemy.
    """
    def __init__(self, level: int, element: int, loc: int):
        """
        Hold the Kuromon(one of the Enemy) information.
        """
        super().__init__(1, loc)
        self.information.set("level", level)
        self.information.set("element", element)
        self.information.set("name", "クロモン")
        self.information_make(True)
        
        self.skill_type: str = None
        self.skill_data: list[int] = None
        self.function = None
        self.function_list: list = [self.act1, self.act2, self.act3]
     
    def act1(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], chr_list: list[Character], ene_list: list[Enemy], turn: int, jamp_rate: float = 1.0):
        """
        This function is one of the actions of this Enemy, which inflicts a mini physical attack to an character.
        This action is the default action and will be triggered with a probability of 85[%].
        """
        self.skill_data = (0, 75, 0, 1, 'chr_single_physics_attack', 200, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        return SkillFunction().physics_attack_function(chr, chrs, enes, TL, self.skill_data)
        
    def act2(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], chr_list: list[Character], ene_list: list[Enemy], turn: int, jamp_rate: float = 1.0):
        """
        This function is one of the actions of this Enemy, which inflicts a mini recover to itself.
        This action is the default action and will be triggered with a probability of this action 15[%].
        """
        self.skill_data = (2, 40, 0, 1, 'self_recover', 4.0, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        return SkillFunction().recover_function(chr, chrs, enes, TL, self.skill_data)
        
    def act3(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], chr_list: list[Character], ene_list: list[Enemy], turn: int, jamp_rate: float = 1.0):
        """
        This function is one of the actions of this Enemy, which inflicts a big physical attack to an character.
        This action is activated when the Enemy is Enemy's charge is maximum.
        """
        self.skill_data = (0, 140, 0, 0, 'chr_single_physics_attack', 350, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        return SkillFunction().physics_attack_function(chr, chrs, enes, TL, self.skill_data)
        
    def skill_function(self, chr_list: list[Character], ene_list: list[Enemy], turn: int) -> SkillFunction:
        """
        This function is the action that is called by battle mode and has the Enemy action algorithm.
        """
        random = np.random.randint(1, 101)
        
        if self.abnormal_status.get("confusion") == True:
            if 1 <= random <= 51:
                self.skill_type = "chr_single_physics_attack"
                self.function = self.act1
                return self.function 
            else:
                self.skill_type = "self_single_physics_attack"
                self.function = self.act1
                return self.function 
        
        if self.information.get("charge") == 4:
            self.skill_type = "chr_single_physics_sttack"
            self.function = self.act3
            self.information.set("chrage", 0)
            return self.function 
                
        if 1 <= random <= 15:
            self.skill_type = "self_single_recover"
            self.function = self.act2
            return self.function 
        else:
            self.skill_type = "chr_single_physics_sttack"
            self.function = self.act1
            return self.function 


class EtwaliaShark(Enemy):
    """
    This class holds information about "Etwalia Shark", which is one of the Enemy.
    """
    def __init__(self, loc: int):
        """
        Hold the Kuromon(one of the Enemy) information.
        233485, 52649, 52649, 235, 138, 137, 45, 0.8
        """
        super().__init__(421, loc)
        self.information.set("level", 80)
        self.information.set("element", CONSTANTS.element.flame)
        self.information.set("name", "エトワリアシャーク")
        self.information_make(False)
        
        self.skill_type: str = None
        self.skill_data: list[int] = None
        self.function = None
        self.fumction_list = [self.act1, self.act2, self.act3, self.act4, self.act5, self.act6, self.act7, self.act8, self.act9, self.act10, self.act11, self.act12]
        
        self.act_5_flag = False
        self.act_6_flag = False
        self.act_8_flag = False
        self.act_9_flag = False
        self.act_10_flag = False
        self.act_12_flag = 0
        self.flag_1 = False
        self.flag_2 = False
        
    def act1(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], chr_list: list[Character], ene_list: list[Enemy], turn: int, jamp_rate: float = 1.0) -> str:
        """
        This function is one of the actions of this Enemy, which inflicts a physical attack and ATK status change to an character.
        his action is the default action and will be triggered with a probability of 70[%].
        """
        act_log = ""
        self.skill_data = (1, 80, 0, 1, 'chr_whole_magic_attack', 300, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().magic_attack_function(chr, chrs, enes, TL, self.skill_data)
        self.skill_data = (3, 0, 0, 0, 'chr_whole_status_change', -15.0, 1, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().status_change_function(chr, chrs, enes, TL, self.skill_data)
        return act_log
    
    def act2(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], chr_list: list[Character], ene_list: list[Enemy], turn: int, jamp_rate: float = 1.0) -> str:
        """
        This function is one of the actions of this Enemy, which inflicts a big physical attack and ATK status change to an character.
        his action is the default action and will be triggered with a probability of 30[%].
        """
        c = self.character_selecte(chr_list, CONSTANTS.cls.warrier)
        if (c == None):
            pass
        else:
            chrs = [c]
        act_log = ""
        self.skill_data = (0, 80, 0, 1, 'chr_single_magic_attack', 200, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().physics_attack_function(chr, chrs, enes, TL, self.skill_data)
        self.skill_data = (3, 0, 0, 0, 'chr_single_status_change', -20.0, 1, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().status_change_function(chr, chrs, enes, TL, self.skill_data)
        return act_log
    
    def act3(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], chr_list: list[Character], ene_list: list[Enemy], turn: int, jamp_rate: float = 1.0) -> str:
        """
        This function is one of the actions of this Enemy, which inflicts a fixed damage to an character.
        This action is activated when the two character has "Paralysis".
        """
        c = self.character_selecte(chr_list, CONSTANTS.cls.knight)
        if (c == None):
            pass
        else:
            chrs = [c]
        act_log = ""
        self.skill_data = (25, 80, 0, 1, 'chr_single_fixed_damage', 2500, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().fixed_damage_function(chr, chrs, enes, TL, self.skill_data)
        return act_log
    
    def act4(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], chr_list: list[Character], ene_list: list[Enemy], turn: int, jamp_rate: float = 1.0) -> str:
        """
        This function is one of the actions of this Enemy, which inflicts a magic attack and set barrier to an character.
        This action is activated when the number of elapsed turns reaches a multiple of 5.
        """
        act_log = ""
        self.skill_data = (1, 80, 0, 1, 'chr_whole_magic_attack', 500, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().magic_attack_function(chr, chrs, enes, TL, self.skill_data)
        self.skill_data = (15, 140, 0, 1, 'self_set_barrier', 30.0, 'None', 'None', 'None', 'None', 1, 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().barrier_function(chr, chrs, enes, TL, self.skill_data)
        return act_log

    def act5(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], chr_list: list[Character], ene_list: list[Enemy], turn: int, jamp_rate: float = 1.0) -> str:
        """
        This function is one of the actions of this Enemy, which inflicts a physics attack, set abnormal, recover and status change to an character.
        This action will be activated when your HP is below 30[%].
        """
        c = self.character_selecte(chr_list, CONSTANTS.cls.alchemist)
        if (c == None):
            pass
        else:
            chrs = [c]
        act_log = ""
        self.skill_data = (1, 80, 0, 1, 'chr_single_physics_attack', 500, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().physics_attack_function(chr, chrs, enes, TL, self.skill_data)
        self.skill_data = (6, 0, 0, 1, 'chr_single_set_abnormal', 'None', 'None', 'None', 100, CONSTANTS.abnormal.isolation, 'None', 'None', 'None', 'None', 'None', 'None')  
        act_log += SkillFunction().abnormal_function(chr, chrs, enes, TL, self.skill_data)
        self.skill_data = (2, 0, 0, 0, 'self_recover', 10.0, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().recover_function(chr, chrs, enes, TL, self.skill_data)
        self.skill_data = (3, 0, 0, 0, 'chr_single_status_change', 10.0, CONSTANTS.status.SPD, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().status_change_function(chr, chrs, enes, TL, self.skill_data)
        return act_log
    
    def act6(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], chr_list: list[Character], ene_list: list[Enemy], turn: int, jamp_rate: float = 1.0) -> str:
        """
        This function is one of the actions of this Enemy, which inflicts a physics attack, set abnormal, recover and status change to an character.
        This action will be activated when your HP is below 50[%].
        """
        c = self.character_selecte(chr_list, CONSTANTS.cls.alchemist)
        if (c == None):
            pass
        else:
            chrs = [c]
        act_log = ""
        self.skill_data = (1, 80, 0, 1, 'chr_single_physics_attack', 500, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().physics_attack_function(chr, chrs, enes, TL, self.skill_data)
        self.skill_data = (6, 0, 0, 1, 'chr_single_set_abnormal', 'None', 'None', 'None', 100, CONSTANTS.abnormal.isolation, 'None', 'None', 'None', 'None', 'None', 'None')  
        act_log += SkillFunction().abnormal_function(chr, chrs, enes, TL, self.skill_data)
        self.skill_data = (2, 0, 0, 0, 'self_recover', 10.0, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().recover_function(chr, chrs, enes, TL, self.skill_data)
        self.skill_data = (3, 0, 0, 0, 'chr_single_status_change', 10.0, CONSTANTS.status.SPD, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().status_change_function(chr, chrs, enes, TL, self.skill_data)
        return act_log

    def act7(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], chr_list: list[Character], ene_list: list[Enemy], turn: int, jamp_rate: float = 1.0) -> str:
        """
        This function is one of the actions of this Enemy, which inflicts a physics attack, set abnormal, recover and status change to an character.
        This action is activated when the SPD debuff exists and Flag 1 does not exist.
        """
        act_log = ""
        self.skill_data = (3, 80, 0, 1, 'self_status_change', -10.0, CONSTANTS.status.DEF, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().status_change_function(chr, chrs, enes, TL, self.skill_data)
        self.skill_data = (3, 0, 0, 0, 'self_status_change', -10.0, CONSTANTS.status.MDF, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().status_change_function(chr, chrs, enes, TL, self.skill_data)
        return act_log
        
    def act8(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], chr_list: list[Character], ene_list: list[Enemy], turn: int, jamp_rate: float = 1.0) -> str:
        """
        This function is one of the actions of this Enemy, which inflicts a physics attack, set abnormal, recover and status change to an character.
        This action is activated when 50 or more turns have passed and this action has never occurred.
        """
        act_log = ""
        self.skill_data = (3, 80, 0, 1, 'self_status_change', -25.0, CONSTANTS.status.DEF, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().status_change_function(chr, chrs, enes, TL, self.skill_data)
        self.skill_data = (3, 0, 0, 0, 'self_status_change', -25.0, CONSTANTS.status.MDF, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().status_change_function(chr, chrs, enes, TL, self.skill_data)
        return act_log
    
    def act9(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], chr_list: list[Character], ene_list: list[Enemy], turn: int, jamp_rate: float = 1.0) -> str:
        """
        This function is one of the actions of this Enemy, which inflicts a physics attack, set abnormal, recover and status change to an character.
        This action is activated when the charge is 0 and this action has never occurred.
        """
        act_log = ""
        self.skill_data = (0, 80, 0, 1, 'chr_single_magic_attack', 200, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().physics_attack_function(chr, chrs, enes, TL, self.skill_data)
        self.skill_data = (3, 0, 0, 0, 'chr_single_status_change', -15.0, 1, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().status_change_function(chr, chrs, enes, TL, self.skill_data)
        return act_log
        
    def act10(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], chr_list: list[Character], ene_list: list[Enemy], turn: int, jamp_rate: float = 1.0) -> str:
        """
        This function is one of the actions of this Enemy, which inflicts a physics attack, set abnormal, recover and status change to an character.
        This action is activated when flag 2 is present and this action has never occurred.
        """
        act_log = ""
        self.skill_data = (5, 80, 0, 1, 'self_status_invalid', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().status_change_invalid_function(chr, chrs, enes, TL, self.skill_data, turn=1024)
        self.skill_data = (3, 0, 0, 0, 'self_status_change', 15.0, 1, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().status_change_function(chr, chrs, enes, TL, self.skill_data, turn=1024)
        self.skill_data = (3, 0, 0, 0, 'self_status_change', 15.0, CONSTANTS.status.MAT, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().status_change_function(chr, chrs, enes, TL, self.skill_data, turn=1024)
        self.skill_data = (3, 0, 0, 0, 'self_status_change', 5.0, CONSTANTS.status.SPD, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().status_change_function(chr, chrs, enes, TL, self.skill_data, turn=1024)
        return act_log
    
    def act11(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], chr_list: list[Character], ene_list: list[Enemy], turn: int, jamp_rate: float = 1.0) -> str:
        """
        This function is one of the actions of this Enemy, which inflicts a magic attack and set abnormal to an character.
        This action is activated when the charge is 4 and this action has not occurred more than once.
        """
        act_log = ""
        self.skill_data = (1, 115, 0, 1, 'ene_single_magic_attack', 500, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().magic_attack_function(chr, chrs, enes, TL, self.skill_data)
        self.skill_data = (6, 0, 0, 0, 'chr_single_set_abnormal', 'None', 'None', 'None', 15, CONSTANTS.abnormal.paralysis, 'None', 'None', 'None', 'None', 'None', 'None')  
        act_log += SkillFunction().status_change_function(chr, chrs, enes, TL, self.skill_data)
        return act_log
    
    def act12(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], chr_list: list[Character], ene_list: list[Enemy], turn: int, jamp_rate: float = 1.0) -> str:
        """
        This function is one of the actions of this Enemy, which inflicts a magic attack and set abnormal to an character.
        This action is activated when the charge is 4.
        """
        act_log = ""
        self.skill_data = (1, 115, 0, 1, 'ene_single_magic_attack', 800, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
        act_log += SkillFunction().magic_attack_function(chr, chrs, enes, TL, self.skill_data)
        self.skill_data = (6, 0, 0, 0, 'chr_single_set_abnormal', 'None', 'None', 'None', 40, CONSTANTS.abnormal.paralysis, 'None', 'None', 'None', 'None', 'None', 'None')  
        act_log += SkillFunction().status_change_function(chr, chrs, enes, TL, self.skill_data)
        return act_log
        
    def skill_function(self, chr_list: list[Character], ene_list: list[Enemy], turn: int) -> SkillFunction:
        """
        This function is the action that is called by battle mode and has the Enemy action algorithm.
        """
        random = np.random.randint(1, 101)
        if (len([i for i in chr_list if (i.abnormal_status.paralysis.get("exist"))]) >= 2):
            self.skill_type = "chr_single_fixed_damage"
            self.function = self.act3
            return self.function
        
        if ((turn % 5) == 0):
            self.skill_type = "chr_single_magic_damage" + "self_set_barrier"
            self.function = self.act4
            return self.function
        
        if (0 <= self.status.HP <= self.status.DEFHP*0.3 and self.act_5_flag == False):
            self.skill_type = "chr_single_physics_damage" + "chr_single_set_abnormal" + "self_recover" + "self_status_change"
            self.function = self.act5
            self.act_5_flag = True
            return self.function
        
        if (0 <= self.status.HP <= self.status.DEFHP*0.5 and self.act_6_flag == False):
            self.skill_type = "chr_single_physics_damage" + "chr_single_set_abnormal" + "self_recover" + "self_status_change"
            self.function = self.act6
            self.act_6_flag = True
            return self.function
        
        if (len([s for s in self.status.status_rates.SPD_change_rates if (s.rate <= 0)]) != 0 and self.flag_1 == False):
            self.skill_type = "self_status_change"
            self.function = self.act7
            self.flag_1 = True
            return self.function
        
        if (turn >= 50 and self.act_8_flag == False):
            self.skill_type = "self_status_change"
            self.function = self.act8
            self.act_8_flag = True
            return self.function
        
        if (self.information.charge == 0 and self.act_9_flag == False):
            self.skill_type = "chr_whole_magic_attack" + "chr_whole_status_change"
            self.function = self.act9
            self.act_9_flag = True
            return self.function
        
        if (self.flag_2 == True and self.act_10_flag == False):
            self.skill_type = "self_status_change" + "self_status_invalid"
            self.function = self.act10
            self.act_10_flag = True
            return self.function
        
        if (self.information.charge == 4 and self.act_12_flag <= 2):
            self.skill_type = "self_status_change" + "self_status_invalid"
            self.function = self.act11
            self.flag_1 = False
            self.act_12_flag += 1
            self.information.charge = 0
            return self.function
        
        elif (self.information.charge == 4):
            self.skill_type = "chr_whole_magic_attack" + "chr_whole_set_abnormal"
            self.function = self.act12
            self.flag_1 = False
            self.flag_2 = True
            self.information.charge = 0
            return self.function
        
        if (1 <= random <= 30):
            self.skill_type = "chr_single_physics_attack" + "chr_single_status_change"
            self.function = self.act2
            return self.function
        else:
            self.skill_tyoe = "chr_whole_magic_attack" + "chr_whole_status_change"
            self.function = self.act1
            return self.function
        
        

###
# Finished that defines the character class.
###

###
# Test
###

if __name__ == "__main__":
    pass

###
# Test
###
