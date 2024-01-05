# coding: UTF-8

###
# This code was created by Kota Sugai.
###

import sqlite3 as sq
from typing import Union
import numpy as np
import csv

###
# Starting that defines the constants.
###

class CharacterInformationConstant:
    """
    This class holds constants that describe the basic status of the character. 
    Each constant (element) indicates the index number of the list that holds the character information.
    """
    def __init__(self):
        self.number = 0
        self.name = 1
        self.rarity = 2
        self.cls = 3
        self.element = 4
        self.title = 5
        self.HP = 6
        self.ATK = 7
        self.MAT = 8
        self.DEF = 9
        self.MDF = 10
        self.SPD = 11
        self.LUK = 12
        self.limited = 13
        self.distributed = 14
        self.friendship = 15
        self.level = 16
        self.location = 17
        self.charge = 18
        self.delay = 19
        self.stan_gauge = 20
        self.hate = 21
        self.stan_coefficient = 22
        self.status_dict = {}
        self.name_dict = {}
        self.title_dict = {}
        self.limited_dict = {0 : "恒常キャラ", 1 : "配布キャラ",2 : "クリスマス", 3 : "お正月", 4 : "バレンタイン", 5 : "ひな祭り", 6 : "水着", 7 : "限定キャラ", 8 : "運動会", 9 : "舶来の魔術師", 10 : "荒野の旅人", 11 : "荒野に咲く",12 : "ハロウィン", 13 : "マンガ版", 14 : "メイド", 15 : "七夕",16 : "シナモロール", 17 : "ポムポムプリン", 18 : "マイメロディ", 19 : "クロミ", 20 : "ハローキティ", 21 : "ぐでたま", 22 : "クロスキャラ", 23 : "第二部", 24 : "ホワイトデー", 25 : "温泉", 26 : "ブライダル", 27 : "しあわせの郵便屋さん", 28 : "成長版", 29 : "イースター"}


class CharacterElementConstant:
    """
    This Class holds constants that indicate the character's element.
    """
    def __init__(self):
        self.flame = 0
        self.water = 1
        self.soil = 2
        self.wind = 3
        self.moon = 4
        self.sun = 5
        self.element_dict = {0 : "ほのお", 1 : "みず", 2 : "つち", 3 : "かぜ", 4 : "つき", 5 : "よう"}
        

class CharacterRarityConstant:
    """
    This Class holds constants that indicate the character's element.
    """
    def __init__(self):
        self.star1 = -2
        self.star2 = -1
        self.star3 = 0
        self.star4 = 1
        self.star5 = 2
        self.rarity_dict = {-2 : "星1", -1 : "星2", 0 : "星3", 1 : "星4", 2 : "星5"}
        
        
class CharacterClassConstant:
    """
    This Class holds constants that indicate the character's class.
    """
    def __init__(self):
        self.warrier = 0
        self.wizard = 1
        self.monk = 2
        self.knight = 3
        self.alchemist = 4
        self.class_dict = {0 : "せんし", 1 : "まほうつかい", 2 : "そうりょ", 3 : "ナイト", 4 : "アルケミスト"}
        
        
class CharacterStatusConstant:
    """
    This Class holds constants that indicate the character's main status.
    """
    def __init__(self):
        self.HP = 0
        self.ATK = 1
        self.MAT = 2
        self.DEF = 3
        self.MDF = 4
        self.SPD = 5
        self.LUK = 6
        self.DEFHP = 7
        self.DEFATK = 8
        self.DEFMAT = 9
        self.DEFDEF = 10
        self.DEFMDF = 11
        self.DEFSPD = 12
        self.DEFLUK = 13
        self.critical_damage = 14
        self.hate = 15
        self.abnormal_resistivity = 16
        self.flame_resistivity = 17
        self.water_resistivity = 18
        self.soil_resistivity = 19
        self.wind_resistivity = 20
        self.moon_resistivity = 21
        self.sun_resistivity = 22
        self.weak_bonus = 23
        self.quick_draw = 24
        self.status_dict = {0 : "HP", 1 : "ATK", 2 : "MAT", 3 : "DEF", 4 : "MDF", 5 : "SPD", 6 : "LUK", 14 : "クリティカルダメージ", 15 : "狙われやすさ", 16 : "状態異常耐性", 17 : "炎属性耐性", 18 : "水属性耐性", 19 : "土属性耐性", 20 : "風属性耐性", 21 : "月属性耐性", 22 : "陽属性耐性", 23 : "有利属性ボーナス", 24 : "クイックドロウ"}
        

class CharacterAbnormalConstant:
    """
    This Class holds constants that indicate the character's abnormal.
    """
    def __init__(self):
        self.confusion = 0
        self.paralysis = 1
        self.poison = 2
        self.bearish = 3
        self.sleep = 4
        self.unhappy = 5
        self.silence = 6
        self.isolation = 7
        self.abnormal_dict = {0 : "こんらん", 1 : "かなしばり", 2 : "腹ペコ", 3 : "よわき", 4 : "ねむり", 5 : "ふこう", 6 : "ちんもく", 7 : "こりつ"}
        
        
class CharacterConditionConstant:
    """
    This Class holds constants that indicate the character's condition.
    """
    def __init__(self):
        self.ATK_NEXT_buff = 0
        self.MAT_NEXT_buff = 1
        self.LUK_NEXT_buff = 2
        self.stan = 3
        self.barrier = 4
        self.recovery = 5
        self.patience = 6
        self.abnormal_invalid = 7
        self.status_change_invalid = 8
        self.condition_dict = {}
        
        
class CharacterSkillConstant:
    """
    This Class holds constants that indicate the character's skill.
    """
    def __init__(self):
        self.first_skill_name = 0
        self.first_skill_type = 1
        self.second_skill_name = 2
        self.second_skill_type = 3
        self.jamp_skill_name = 4
        self.jamp_skill_type = 5
        self.unevolved_skill_name = 6
        self.unevolved_skill_type = 7
        self.evolved_skill_name = 8
        self.evolved_skill_type = 9
        self.auto_skill = 10
        self.skill_dict = {}
        
        
class CharacterSkillInformationConstant:
    """
    This Class holds constants that indicate the character's skill information.
    """
    def __init__(self):
        self.skill_name = 0
        self.skill_type = 1
        self.skill_delay = 2
        self.skill_recast = 3
        self.skill_charge = 4
        self.skill_info = 5
        self.skill_rate = 6
        self.status_type = 7
        self.reset_bool = 8
        self.skill_prob = 9
        self.abnormal_type = 10
        self.barrier_num = 11
        self.skill_card_info = 12
        self.skill_card_rate = 13
        self.skill_card_delay = 14
        self.skill_card_charge = 15
        self.skill_card_num = 16
        self.skill_data_dict = {}
   
   
class EnemyStatusInformationConstant:
    """
    This Class holds constants that indicate the enemy's status information.
    """
    def __init__(self):
        self.enemy_status_dict = {0 : ["A enemy with s enemy number of 0 does not exist."]}
        with open("Data/kirafan_enemy_status.csv", "r") as f:
            reader = csv.reader(f)
            for status in reader:
                self.enemy_status_dict[int(status[0])] = [float(i) for i in status[1:]]

 
class Constant:
    """
    Controls all constants and returns the specified constant.
    """
    def __init__(self):
        self.info = CharacterInformationConstant()
        self.element = CharacterElementConstant()
        self.rarity = CharacterRarityConstant()
        self.cls = CharacterClassConstant()
        self.status = CharacterStatusConstant()
        self.abnormal = CharacterAbnormalConstant()
        self.condition = CharacterConditionConstant()
        self.skill = CharacterSkillConstant()
        self.skill_info = CharacterSkillInformationConstant()
        self.enemy_status = EnemyStatusInformationConstant()
        self.data_make()
        
    def get(self, constant_type: str = "") -> Union[int, dict]:
        """
        Gets the corresponding constant using the specified argument.
        constant_type : The kind of constant you want to get.
        Example:
        Constant().get("number") -> CharacterInformationConstant().number
        """
        if (constant_type == "number"):
            return self.info.number
        elif (constant_type == "name"):
            return self.info.name
        elif (constant_type == "rarity"):
            return self.info.rarity
        elif (constant_type == "class"):
            return self.info.cls
        elif (constant_type == "element"):
            return self.info.element
        elif (constant_type == "title"):
            return self.info.title
        elif (constant_type == "HP"):
            return self.info.HP
        elif (constant_type == "ATK"):
            return self.info.ATK
        elif (constant_type == "DEF"):
            return self.info.DEF
        elif (constant_type == "MDF"):
            return self.info.MDF
        elif (constant_type == "SPD"):
            return self.info.SPD
        elif (constant_type == "LUK"):
            return self.info.LUK
        elif (constant_type == "limited"):
            return self.info.limited
        elif (constant_type == "distributed"):
            return self.info.distributed
        elif (constant_type == "friendship"):
            return self.info.friendship
        elif (constant_type == "level"):
            return self.info.level
        
        elif (constant_type == "flame"):
            return self.element.flame
        elif (constant_type == "water"):
            return self.element.water
        elif (constant_type == "soil"):
            return self.element.soil
        elif (constant_type == "wind"):
            return self.element.wind
        elif (constant_type == "moon"):
            return self.element.moon
        elif (constant_type == "sun"):
            return self.element.sun
        elif (constant_type == "element_dict"):
            return self.element.element_dict
        
        elif (constant_type == "star1"):
            return self.rarity.star1
        elif (constant_type == "star2"):
            return self.rarity.star2
        elif (constant_type == "star3"):
            return self.rarity.star3
        elif (constant_type == "star4"):
            return self.rarity.star4
        elif (constant_type == "star5"):
            return self.rarity.star5
        elif (constant_type == "rarity_dict"):
            return self.rarity.rarity_dict
        
        elif (constant_type == "warrier"):
            return self.cls.warrier
        elif (constant_type == "wizard"):
            return self.cls.wizard
        elif (constant_type == "monk"):
            return self.cls.monk
        elif (constant_type == "knight"):
            return self.cls.knight
        elif (constant_type == "alchemist"):
            return self.cls.alchemist
        elif (constant_type == "class_dict"):
            return self.cls.class_dict
        
        elif (constant_type == "confusion"):
            return self.abnormal.confusion
        elif (constant_type == "paralysis"):
            return self.abnormal.paralysis
        elif (constant_type == "poison"):
            return self.abnormal.poison
        elif (constant_type == "bearish"):
            return self.abnormal.bearish
        elif (constant_type == "sleep"):
            return self.abnormal.sleep
        elif (constant_type == "unhappy"):
            return self.abnormal.unhappy
        elif (constant_type == "silence"):
            return self.abnormal.silence
        elif (constant_type == "isolation"):
            return self.abnormal.isolation
        
        elif (constant_type == "ATK_next"):
            return self.condition.ATK_NEXT_buff
        elif (constant_type == "MAT_next"):
            return self.condition.MAT_NEXT_buff
        elif (constant_type == "LUK_next"):
            return self.condition.LUK_NEXT_buff
        elif (constant_type == "stan"):
            return self.condition.stan
        elif (constant_type == "barrier"):
            return self.condition.barrier
        elif (constant_type == "recovery"):
            return self.condition.recovery
        elif (constant_type == "patience"):
            return self.condition.patience
        elif (constant_type == "abnormal_invalid"):
            return self.condition.abnormal_invalid
        elif (constant_type == "status_invalid"):
            return self.condition.status_change_invalid
        
        elif (constant_type == "skill_name"):
            return self.skill_info.skill_name
        elif (constant_type == "skill_type"):
            return self.skill_info.skill_type
        elif (constant_type == "skill_delay"):
            return self.skill_info.skill_delay
        elif (constant_type == "skill_recast"):
            return self.skill_info.skill_recast
        elif (constant_type == "skill_charge"):
            return self.skill_info.skill_charge
        elif (constant_type == "skill_info"):
            return self.skill_info.skill_info
        elif (constant_type == "skill_rate"):
            return self.skill_info.skill_rate
        elif (constant_type == "status_type"):
            return self.skill_info.status_type
        elif (constant_type == "reset_bool"):
            return self.skill_info.reset_bool
        elif (constant_type == "skill_prob"):
            return self.skill_info.skill_prob
        elif (constant_type == "abnormal_type"):
            return self.skill_info.abnormal_type
        elif (constant_type == "barrier_num"):
            return self.skill_info.barrier_num
        elif (constant_type == "skill_card_info"):
            return self.skill_info.skill_card_info
        elif (constant_type == "skill_card_rate"):
            return self.skill_info.skill_card_rate
        elif (constant_type == "skill_card_delay"):
            return self.skill_info.skill_card_delay
        elif (constant_type == "skill_card_charge"):
            return self.skill_info.skill_card_charge
        elif (constant_type == "skill_card_num"):
            return self.skill_info.skill_card_num
        
        elif (constant_type == "first_skill_name"):
            return self.skill.first_skill_name
        elif (constant_type == "first_skill_type"):
            return self.skill.first_skill_type
        elif (constant_type == "second_skill_name"):
            return self.skill.second_skill_name
        elif (constant_type == "second_skill_type"):
            return self.skill.second_skill_type
        elif (constant_type == "jamp_skill_name"):
            return self.skill.jamp_skill_name
        elif (constant_type == "jamp_skill_type"):
            return self.skill.jamp_skill_type
        elif (constant_type == "unevolved_skill_name"):
            return self.skill.unevolved_skill_name
        elif (constant_type == "unevolved_skill_type"):
            return self.skill.unevolved_skill_type
        elif (constant_type == "evolved_skill_name"):
            return self.skill.evolved_skill_name
        elif (constant_type == "evolved_skill_type"):
            return self.skill.evolved_skill_type
        elif (constant_type == "auto_skill"):
            return self.skill.auto_skill
        
        elif (constant_type == "name_dict"):
            return self.info.name_dict
        elif (constant_type == "status_dict"):
            return self.info.status_dict
        elif (constant_type == "skill_dict"):
            return self.skill.skill_dict
        elif (constant_type == "skill_data_dict"):
            return self.skill_info.skill_data_dict
        elif (constant_type == "enemy_status_dict"):
            return self.enemy_status.enemy_status_dict
        elif (constant_type == "status_dict"):
            return self.status.status_dict
        elif (constant_type == "abnormal_dict"):
            return self.abnormal.abnormal_dict
          
    def data_make(self):
        """
        This function makes a dict of data for each element.
        """
        CHARACTER_INFORMATION_PATH = "Data/Character_Information.db"
        INFO_NAME = "Character_Information_Table"
        CHARACTER_NAME_PATH = "Data/Character_Name.db"
        NAME_NAME = "Character_Name_Table"
        CHARACTER_TITLE_PATH = "Data/Character_Title.db"
        TITLE_NAME = "Character_TITLE_Table"
        SKILL_INFORMATION_PATH = "Data/Skill_Information.db"
        SKILL_NAME = "Skill_Information_Table"
        CHARACTER_SKILL_INFORMATION_PATH = "Data/Character_Skill_Information.db"
        CHR_SKILL_NAME = "Character_Skill_Information_Table"
        path_list = [CHARACTER_INFORMATION_PATH, CHARACTER_NAME_PATH, CHARACTER_TITLE_PATH, SKILL_INFORMATION_PATH, CHARACTER_SKILL_INFORMATION_PATH]
        table_name_list = [INFO_NAME, NAME_NAME, TITLE_NAME, SKILL_NAME, CHR_SKILL_NAME]
        dict_list = [self.info.status_dict, self.info.name_dict, self.info.title_dict, self.skill_info.skill_data_dict, self.skill.skill_dict]
        
        for path, table,dic in zip(path_list, table_name_list, dict_list):
            con = sq.connect(path)
            cur = con.cursor()
            cur.execute("SELECT * FROM " + table)
            for i in cur:
                dic[i[0]] = i[1:]
                

###
# Finished that defines the constants.
###

class Character:
    def get():
        pass
    
class Enemy:
    pass

class SkillCard:
    pass

class SkillFunction:
    pass

###
# Starting that defines the character class.
###
CONSTANTS = Constant()

class StatusChangeRate:
    """
    This class represents status changes.
    Which status, how much it changes, and how long it lasts.
    
    Args:
        typ (int) : Which status will be changed.
        rate (float) : Amount of change in status.
    
    Vars:
        typ (int) : Which status will be changed.
        rate (float) : Amount of change in status.
        turn (int) : The number of turns that the status change lasts.
        exist (bool) : Information on whether the status change exists.
        
    Functions:
        add(typ, rate) : Adds the specified value to the value of the specified parameter.
        get(typ) : Gets the value of the specified parameter.
        set(typ, rate) : Sets the specified value to the value of the specified parameter.
    """
    def __init__(self, typ: int, rate: float):
        self.typ: int = typ
        self.rate: float = rate
        self.turn: int = 3
        self.exist: bool = True
    
    def add(self, typ: str, rate: float) -> None:
        """
        Adds the specified value to the value of the specified parameter.
        
        Args:
            typ (str) : Which status will be changed.
            rate (float) : Amount of change in status.
        """
        if (typ == "type"):
            self.typ += rate
        elif (typ == "rate"):
            self.rate += rate
        elif (typ == "turn"):
            if (self.exist == True):
                if (self.turn > 0):
                    self.turn += rate
                elif (self.turn <= 0):
                    self.exist = False
        elif (typ == "exist"):
            self.exist += rate
        
    def get(self, typ: str) -> int:
        """
        Gets the value of the specified parameter.
        
        Args:
            typ (str) : Which status will be changed.
            
        Returns:
            int : Got value and type.
        """
        if (typ == "type"):
            return self.typ
        elif (typ == "rate"):
            return self.rate
        elif (typ == "turn"):
            return self.turn
        elif (typ == "exist"):
            return self.exist
        
    def set(self, typ: str, rate: float) -> None:
        """
        Sets the specified value to the value of the specified parameter.
        
        Args:
            typ (str) : Which status will be changed.
            rate (float) : Amount of change in status.
        """
        if (typ == "type"):
            self.typ = rate
        elif (typ == "rate"):
            self.rate = rate
        elif (typ == "turn"):
            self.turn = rate
        elif (typ == "exist"):
            self.exist = rate
            
        
class AbnormalStatus:
    """
    This class represents a character's abnormal status.
    Which abnormal status, how much it changes, and how long it lasts.
    
    Args:
        typ (int) : Which abnormal will be set.
    
    Vars:
        typ (int) : Which abnormal will be set.
        rate (float) : Amount of abnormal.
        turn (int) : The number of turns that the abnormal lasts.
        exist (bool) : Information on whether the abnormal exists.
        
    Functions:
        add(typ, rate) : Adds the specified value to the value of the specified parameter.
        get(typ) : Gets the value of the specified parameter.
        set(typ, rate) : Sets the specified value to the value of the specified parameter.
    """
    def __init__(self, typ: int):
        self.typ = typ
        self.turn = 3
        self.exist = False
        
    def add(self, typ: str, rate: float):
        """
        Adds the specified value to the value of the specified parameter.
        
        Args:
            typ (int) : Which abnormal will be set.
            rate (float) : Amount of abnormal.
        """
        if (typ == "type"):
            self.typ += rate
        elif (typ == "turn"):
            if (self.exist == True):
                if (self.turn > 0):
                    self.turn += rate
                elif (self.turn <= 0):
                    self.exist = False
        elif (typ == "exist"):
            self.exist += rate
        
    def get(self, typ: str) -> int:
        """
        Gets the value of the specified parameter.
        
        Args:
            typ (int) : Which abnormal will be set.
            
        Returns:
            int : Got value and type.
        """
        if (typ == "type"):
            return self.typ
        elif (typ == "turn"):
            return self.turn
        elif (typ == "exist"):
            return self.exist
        
    def set(self, typ: str, rate: float):
        """
        Sets the specified value to the value of the specified parameter.
        
        Args:
            typ (int) : Which abnormal will be set.
            rate (float) : Amount of abnormal.
        """
        if (typ == "type"):
            self.typ = rate
        elif (typ == "turn"):
            self.turn = rate
        elif (typ == "exist"):
            self.exist = rate
        

class ConditionStatus:
    """
    This class represents a character's condition status.
    Which condition status, how much it changes, and how long it lasts.
    
    Args:
        typ (int) : Which condition will be set.
        rate (float) : Amount of condition.
        turn (int) : The number of turns that the condition lasts.
    
    Vars:
        typ (int) : Which condition will be set.
        rate (float) : Amount of condition.
        turn (int) : The number of turns that the condition lasts.
        exist (bool) : Information on whether the condition exists.
        
    Returns:
        int : Got value and type.
    
    Functions:
        add(typ, rate) : Adds the specified value to the value of the specified parameter.
        get(typ) : Gets the value of the specified parameter.
        set(typ, rate) : Sets the specified value to the value of the specified parameter.
    """
    def __init__(self, typ: int, rate: int = 0.0, turn: int = 3):
        self.typ = typ
        self.rate = rate
        self.turn = turn
        self.exist = False
    
    def add(self, typ: str, rate: float):
        """
        Adds the specified value to the value of the specified parameter.
        
        Args:
            typ (str) : Which condition will be set.
            rate (float) : Amount of condition.
        """
        if (typ == "type"):
            self.typ += rate
        elif (typ == "rate"):
            self.rate += rate
        elif (typ == "turn"):
            if (self.exist == True):
                if (self.turn > 0):
                    self.turn += rate
                elif (self.turn <= 0):
                    self.exist = False
        elif (typ == "exist"):
            self.exist += rate
        
    def get(self, typ: str) -> int:
        """
        Gets the value of the specified parameter.
        
        Args:
            typ (str) : Which condition will be set.
            
        Returns:
            int : Got value and type.
        """
        if (typ == "type"):
            return self.typ
        elif (typ == "rate"):
            return self.rate
        elif (typ == "turn"):
            return self.turn
        elif (typ == "exist"):
            return self.exist
        
    def set(self, typ: str, rate: float):
        """
        Sets the specified value to the value of the specified parameter.
        
        Args:
            typ (int) : Which condition will be set.
            rate (float) : Amount of condition.
        """
        if (typ == "type"):
            self.typ = rate
        elif (typ == "rate"):
            self.rate = rate
        elif (typ == "turn"):
            self.turn = rate
        elif (typ == "exist"):
            self.exist = rate
        
        
class StatusChangeRates:
    """
    This class holds the status changes for characters.
    Which status should be changed and by how much.
    
    Vars:
        ATK_change_rates (list[StatusChangeRate]) : Maintain changes in ATK status.
        MAT_change_rates (list[StatusChangeRate]) : 
        DEF_change_rates (list[StatusChangeRate]) : 
        MDF_change_rates (list[StatusChangeRate]) : 
        SPD_change_rates (list[StatusChangeRate]) : 
        LUK_change_rates (list[StatusChangeRate]) : 
        critical_damage_change_rates (list[StatusChangeRate]) : 
        hate_change_rates (list[StatusChangeRate]) : 
        abnormal_resistivity_change_rates (list[StatusChangeRate]) : 
        FLAME_element_resistivity_change_rates (list[StatusChangeRate]) : 
        WATER_element_resistivity_change_rates (list[StatusChangeRate]) : 
        SOIL_element_resistivity_change_rates (list[StatusChangeRate]) : 
        WIND_element_resistivity_change_rates (list[StatusChangeRate]) : 
        MOON_element_resistivity_change_rates (list[StatusChangeRate]) : 
        SUN_element_resistivity_change_rates (list[StatusChangeRate]) : 
        weak_bonus_change_rates (list[StatusChangeRate]) : 
        quick_draw_change_rates (list[StatusChangeRate]) : 
    
    Functions:
        add(typ, rate) : Adds the specified value to the value of the specified parameter.
        get(typ) : Gets the value of the specified parameter.
        set(typ, rate) : Sets the specified value to the value of the specified parameter.
    """
    def __init__(self):
        self.ATK_change_rates: list[StatusChangeRate] = []
        self.MAT_change_rates: list[StatusChangeRate] = []
        self.DEF_change_rates: list[StatusChangeRate] = []
        self.MDF_change_rates: list[StatusChangeRate] = []
        self.SPD_change_rates: list[StatusChangeRate] = []
        self.LUK_change_rates: list[StatusChangeRate] = []
        self.critical_damage_change_rates: list[StatusChangeRate] = []
        self.hate_change_rates: list[StatusChangeRate] = []
        self.abnormal_resistivity_change_rates: list[StatusChangeRate] = []
        self.FLAME_element_resistivity_change_rates: list[StatusChangeRate] = []
        self.WATER_element_resistivity_change_rates: list[StatusChangeRate] = []
        self.SOIL_element_resistivity_change_rates: list[StatusChangeRate] = []
        self.WIND_element_resistivity_change_rates: list[StatusChangeRate] = []
        self.MOON_element_resistivity_change_rates: list[StatusChangeRate] = []
        self.SUN_element_resistivity_change_rates: list[StatusChangeRate] = []
        self.weak_bonus_change_rates: list[StatusChangeRate] = []
        self.quick_draw_change_rates: list[StatusChangeRate] = []
 
    def turn_calc(self):
        """
        Calculates the turn of changed status.
        """
        change_rate_list: list[list[StatusChangeRate]] = [self.ATK_change_rates, self.MAT_change_rates, self.DEF_change_rates, self.MDF_change_rates, self.SPD_change_rates, self.LUK_change_rates, self.hate_change_rates, self.critical_damage_change_rates, self.abnormal_resistivity_change_rates, self.FLAME_element_resistivity_change_rates, self.WATER_element_resistivity_change_rates, self.SOIL_element_resistivity_change_rates, self.WIND_element_resistivity_change_rates, self.MOON_element_resistivity_change_rates, self.SUN_element_resistivity_change_rates, self.weak_bonus_change_rates, self.quick_draw_change_rates]
        for status_rates in change_rate_list:
            for status_rate in status_rates:
                status_rate.add("turn", -1)

    def status_calc(self, original_status_list: list[float]) -> list[float]:
        """
        Calculates the changed status from the given StatusChangeRate.
        """
        for status_rate in self.hate_change_rates:
            status_rate.add("turn", -1)
            if (status_rate.get("exist") == False):
                self.hate_change_rates.remove(status_rate)
        
        change_rate_list: list[list[StatusChangeRate]] = [self.ATK_change_rates, self.MAT_change_rates, self.DEF_change_rates, self.MDF_change_rates, self.SPD_change_rates, self.LUK_change_rates, self.critical_damage_change_rates, self.abnormal_resistivity_change_rates, self.FLAME_element_resistivity_change_rates, self.WATER_element_resistivity_change_rates, self.SOIL_element_resistivity_change_rates, self.WIND_element_resistivity_change_rates, self.MOON_element_resistivity_change_rates, self.SUN_element_resistivity_change_rates, self.weak_bonus_change_rates, self.quick_draw_change_rates]
        calc_status = []
        for status_rates, original_status in zip(change_rate_list, original_status_list):
            rate = 0
            for status_rate in status_rates:
                status_rate.add("turn", -1)
                if (status_rate.get("exist") == False):
                    status_rates.remove(status_rate)
                else:
                    rate += status_rate.get("rate")
            rate = (1 + (rate/100))
            if (rate <= 0.5):
                rate = 0.5
            elif (rate >= 2.5):
                rate = 2.5
            calc_status.append(np.floor(original_status * rate))
        return calc_status
    
    def add(self, typ: str, rate: StatusChangeRate):
        """
        Adds the specified value to the value of the specified parameter.
        
        Args:
            typ (str) : Which status change will be changed.
            rate (StatusChangeRate) : Status change rate to add.
        """
        if (typ == "ATK"):
            self.ATK_change_rates.append(rate)
        elif (typ == "MAT"):
            self.MAT_change_rates.append(rate)
        elif (typ == "DEF"):
            self.DEF_change_rates.append(rate)
        elif (typ == "MDF"):
            self.MDF_change_rates.append(rate)
        elif (typ == "SPD"):
            self.SPD_change_rates.append(rate)
        elif (typ == "LUK"):
            self.LUK_change_rates.append(rate)
        elif (typ == "critical_damage"):
            self.critical_damage_change_rates.append(rate)
        elif (typ == "hate"):
            self.hate_change_rates.append(rate)
        elif (typ == "abnormal"):
            self.abnormal_resistivity_change_rates.append(rate)
        elif (typ == "flame"):
            self.FLAME_element_resistivity_change_rates.append(rate)
        elif (typ == "water"):
            self.WATER_element_resistivity_change_rates.append(rate)
        elif (typ == "soil"):
            self.SOIL_element_resistivity_change_rates.append(rate)
        elif (typ == "wind"):
            self.WIND_element_resistivity_change_rates.append(rate)
        elif (typ == "moon"):
            self.MOON_element_resistivity_change_rates.append(rate)
        elif (typ == "sun"):
            self.SUN_element_resistivity_change_rates.append(rate)
        elif (typ == "weak_bonus"):
            self.weak_bonus_change_rates.append(rate)
        elif (typ == "quick_draw"):
            self.quick_draw_change_rates.append(rate)
        
    def get(self, typ: str) -> list[StatusChangeRate]:
        """
        Gets the value of the specified parameter.
        
        Args:
            typ (str) : Which status change will be changed.
                
        Returns:
            list[StatusChangeRate] : Got value and type.
        """
        if (typ == "ATK"):
            return self.ATK_change_rates
        elif (typ == "MAT"):
            return self.MAT_change_rates
        elif (typ == "DEF"):
            return self.DEF_change_rates
        elif (typ == "MDF"):
            return self.MDF_change_rates
        elif (typ == "SPD"):
            return self.SPD_change_rates
        elif (typ == "LUK"):
            return self.LUK_change_rates
        elif (typ == "critical_damage"):
            return self.critical_damage_change_rates
        elif (typ == "hate"):
            return self.hate_change_rates
        elif (typ == "abnormal"):
            return self.abnormal_resistivity_change_rates
        elif (typ == "flame"):
            return self.FLAME_element_resistivity_change_rates
        elif (typ == "water"):
            return self.WATER_element_resistivity_change_rates
        elif (typ == "soil"):
            return self.SOIL_element_resistivity_change_rates
        elif (typ == "wind"):
            return self.WIND_element_resistivity_change_rates
        elif (typ == "moon"):
            return self.MOON_element_resistivity_change_rates
        elif (typ == "sun"):
            return self.SUN_element_resistivity_change_rates
        elif (typ == "weak_bonus"):
            return self.weak_bonus_change_rates
        elif (typ == "quick_draw"):
            return self.quick_draw_change_rates
        
    def set(self, typ: str, rate: float):
        """
        Sets the specified value to the value of the specified parameter.
        
        Args:
            typ (str) : Which status change will be changed.
            rate (StatusChangeRate) : Status change rate to add.
        """
        if (typ == "ATK"):
            self.ATK_change_rates = [rate]
        elif (typ == "MAT"):
            self.MAT_change_rates = [rate]
        elif (typ == "DEF"):
            self.DEF_change_rates = [rate]
        elif (typ == "MDF"):
            self.MDF_change_rates = [rate]
        elif (typ == "SPD"):
            self.SPD_change_rates = [rate]
        elif (typ == "LUK"):
            self.LUK_change_rates = [rate]
        elif (typ == "critical_damage"):
            self.critical_damage_change_rates = [rate]
        elif (typ == "hate"):
            self.hate_change_rates = [rate]
        elif (typ == "abnormal"):
            self.abnormal_resistivity_change_rates = [rate]
        elif (typ == "flame"):
            self.FLAME_element_resistivity_change_rates = [rate]
        elif (typ == "water"):
            self.WATER_element_resistivity_change_rates = [rate]
        elif (typ == "soil"):
            self.SOIL_element_resistivity_change_rates = [rate]
        elif (typ == "wind"):
            self.WIND_element_resistivity_change_rates = [rate]
        elif (typ == "moon"):
            self.MOON_element_resistivity_change_rates = [rate]
        elif (typ == "sun"):
            self.SUN_element_resistivity_change_rates = [rate]
        elif (typ == "weak_bonus"):
            self.weak_bonus_change_rates = [rate]
        elif (typ == "quick_draw"):
            self.quick_draw_change_rates = [rate]
        
        
class Skill:
    """
    This class represents information about the skills possessed by a character.
    Which skills, what effects, and what data.   
    """
    def __init__(self):
        self.name = ""
        self.effect = ""
        self.info = ""
        self.data = []
        self.recast = 0
        self.def_recast = 0
        self.function: list[SkillFunction] = []
        
    def add(self, typ: str, rate: float):
        """
        Adds the specified value to the value of the specified parameter.
        """
        if (typ == "name"):
            self.name += rate
        elif (typ == "effect"):
            self.effect += rate
        elif (typ == "info"):
            self.info += rate
        elif (typ == "data"):
            self.data.append(rate)
        elif (typ == "recast"):
            self.recast += rate
            if (self.recast <= 0):
                self.recast = 0
        elif (typ == "function"):
            self.function.append(rate)
        
    def get(self, typ: str) -> int:
        """
        Gets the value of the specified parameter.
        """
        if (typ == "name"):
            return self.name
        elif (typ == "effect"):
            return self.effect
        elif (typ == "info"):
            return self.info
        elif (typ == "data"):
            return self.data
        elif (typ == "recast"):
            return self.recast
        elif (typ == "function"):
            return self.function
        
    def set(self, typ: str, rate: float):
        """
        Sets the specified value to the value of the specified parameter.
        """
        if (typ == "name"):
            self.name = rate
        elif (typ == "effect"):
            self.effect = rate
        elif (typ == "info"):
            self.info = rate
        elif (typ == "data"):
            self.data = [rate]
        elif (typ == "recast"):
            self.recast = rate
        elif (typ == "function"):
            self.function = [rate]
        
    def skill_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]]):
        """
        Activate the skill.
        """
        act_log = ""
        for skill, data in zip(self.function, self.data):
            act_log += skill(chr, chrs, enes, TL, data)
        return act_log

    
class Weapon:
    """
    This class represents information about the skills possessed by a character.
    Which skills, what effects, and what data.   
    """
    def __init__(self, num: int):
        self.name = CONSTANTS.skill.skill_dict[num][CONSTANTS.skill.evolved_skill_name]
        self.type = CONSTANTS.skill.skill_dict[num][CONSTANTS.skill.evolved_skill_type]
        self.data = []
        self.function = []
        skill_type_dict = {0 : SkillFunction().physics_attack_function, 1 : SkillFunction().magic_attack_function, 2 : SkillFunction().recover_function, 3 : SkillFunction().status_change_function, 4 : SkillFunction().status_change_reset_function, 5 : SkillFunction().status_change_invalid_function, 6 : SkillFunction().abnormal_function, 7 : SkillFunction().abnormal_recover_function, 8 : SkillFunction().abnormal_invalid_function, 9 : SkillFunction().status_change_function, 10 : SkillFunction().status_change_function, 11 : SkillFunction().status_change_function, 12 : SkillFunction().next_buff_finction, 13 : SkillFunction().next_buff_finction, 14 : SkillFunction().next_buff_finction, 15 : SkillFunction().barrier_function, 16 : SkillFunction().recast_change_function, 17 : SkillFunction().jamp_gauge_change_function, 18 : SkillFunction().status_change_function, 19 : SkillFunction().enemy_charge_change_function, 20 : SkillFunction().skill_card_function, 21 : SkillFunction().recovery_function, 22 : SkillFunction().status_change_function, 23 : SkillFunction().patience_function, 24 : SkillFunction().status_change_function}
        
        for type, data in CONSTANTS.skill_info.skill_data_dict.items():
            if (type in self.type):
                data = list(data)
                self.function.append(skill_type_dict[data[0]])
                if (len(self.data) == 0):
                    self.data.append(data)
                else:
                    data[CONSTANTS.skill_info.skill_delay-1] = 5
                    data[CONSTANTS.skill_info.skill_charge-1] = 3
                    data[CONSTANTS.skill_info.skill_recast-1] = 5
                    self.data.append(data)
                    
    def skill_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]]) -> str:
        """
        Activate the skill.
        """
        for skill, data in zip(self.function, self.data):
            act_log = skill(chr, chrs, enes, TL, data)
        return act_log
    

class CharacterInformation:
    """
    This class holds the character's basic information and other status information.
    """
    def __init__(self, number: int, location: int):
        self.number: int = number
        self.name: int = 0
        self.title: int = 0
        self._class: int = 0
        self.element: int = 0
        self.rare: int = 0
        self.friendship = 7
        self.level = 100
        self.location: int = location
        self.charge: float = 0
        self.max_charge: float = 1000000
        self.delay: float = 0
        self.stan_gauge: float = 0
        self.hate = 0
        self.stan_coefficient = 1.2
        
    def add(self, typ: str, rate: float):
        """
        Adds the specified value to the value of the specified parameter.
        """
        if (typ == "charge"):
            self.charge += rate
            if (self.charge <= 0):
                self.charge = 0
            elif (self.charge >= self.max_charge):
                self.charge = self.max_charge
        elif (typ == "delay"):
            self.delay += rate
        elif (typ == "stan"):
            self.stan_gauge += rate
            if (self.stan_gauge <= 0):
                self.stan_gauge = 0
            elif (self.stan_gauge >= 1):
                self.stan_gauge = 1
        elif (typ == "hate"):
            self.hate += rate
        
    def get(self, typ: str) -> int:
        """
        Gets the value of the specified parameter.
        """
        if (typ == "number"):
            return self.number
        elif (typ == "name"):
            return self.name
        elif (typ == "title"):
            return self.title
        elif (typ == "class"):
            return self._class
        elif (typ == "element"):
            return self.element
        elif (typ == "rare"):
            return self.rare
        elif (typ == "friend"):
            return self.friendship
        elif (typ == "level"):
            return self.level
        elif (typ == "location"):
            return self.location
        elif (typ == "charge"):
            return self.charge
        elif (typ == "max_charge"):
            return self.max_charge
        elif (typ == "delay"):
            return self.delay
        elif (typ == "stan"):
            return self.stan_gauge
        elif (typ == "hate"):
            return self.hate
        elif (typ == "stan_coefficient"):
            return self.stan_coefficient
        
    def set(self, typ: str, rate: float):
        """
        Sets the specified value to the value of the specified parameter.
        """
        if (typ == "number"):
            self.number = rate
        elif (typ == "name"):
            self.name = rate
        elif (typ == "title"):
            self.title = rate
        elif (typ == "class"):
            self._class = rate
        elif (typ == "element"):
            self.element = rate
        elif (typ == "rare"):
            self.rare = rate
        elif (typ == "friend"):
            self.friendship = rate
        elif (typ == "level"):
            self.level = rate
        elif (typ == "location"):
            self.location = rate
        elif (typ == "charge"):
            self.charge = rate
        elif (typ == "max_charge"):
            self.max_charge = rate
        elif (typ == "delay"):
            self.delay = rate
        elif (typ == "stan"):
            self.stan_gauge = rate
        elif (typ == "hate"):
            self.hate = rate
        elif (typ == "stan_coefficient"):
            self.stan_coefficient = rate
        
    def information_make(self):
        """
        Make the character's information.
        """
        chr_status_list = CONSTANTS.info.status_dict[self.number]
        
        self.name = chr_status_list[CONSTANTS.get("name")-1]
        self.title = chr_status_list[CONSTANTS.get("title")-1]
        self._class = chr_status_list[CONSTANTS.get("class")-1]
        self.element = chr_status_list[CONSTANTS.get("element")-1]
        self.rare = chr_status_list[CONSTANTS.get("rarity")-1]
        
        
class CharacterStatus:
    """
    This class holds information about the character's  status.
    """
    def __init__(self):
        self.HP = 0
        self.ATK = 0
        self.MAT = 0
        self.DEF = 0
        self.MDF = 0
        self.SPD = 0
        self.LUK = 0
        self.critical_damage = 0
        self.hate = 0
        self.abnormal_resistivity = 0
        self.FLAME_element_resistivity = 0
        self.WATER_element_resistivity = 0
        self.SOIL_element_resistivity = 0
        self.WIND_element_resistivity = 0
        self.MOON_element_resistivity = 0
        self.SUN_element_resistivity = 0
        self.weak_bonus = 0
        self.quick_draw = 0
        self.status_rates = StatusChangeRates()
        self.DEFHP = 0
        self.DEFATK = 0
        self.DEFMAT = 0
        self.DEFDEF = 0
        self.DEFMDF = 0
        self.DEFSPD = 0
        self.DEFLUK = 0
        
    def add(self, typ: str, rate: float):
        """
        Adds the specified value to the value of the specified parameter.
        """
        if (typ == "HP"):
            self.HP += rate
            if (self.HP <= 0):
                self.HP = 0
            elif (self.HP >= self.DEFHP):
                self.HP = self.DEFHP
        elif (typ == "ATK"):
            self.ATK += rate
        elif (typ == "MAT"):
            self.MAT += rate
        elif (typ == "DEF"):
            self.DEF += rate
        elif (typ == "MDF"):
            self.MDF += rate
        elif (typ == "SPD"):
            self.SPD += rate
        elif (typ == "LUK"):
            self.LUK += rate
        elif (typ == "critical_damage"):
            self.critical_damage += rate
        elif (typ == "hate"):
            self.hate += rate
        elif (typ == "abnormal"):
            self.abnormal_resistivity += rate
        elif (typ == "flame"):
            self.FLAME_element_resistivity += rate
        elif (typ == "water"):
            self.WATER_element_resistivity += rate
        elif (typ == "soil"):
            self.SOIL_element_resistivity += rate
        elif (typ == "wind"):
            self.WIND_element_resistivity += rate
        elif (typ == "moon"):
            self.MOON_element_resistivity += rate
        elif (typ == "sun"):
            self.SUN_element_resistivity += rate
        elif (typ == "weak_bonus"):
            self.weak_bonus += rate
        elif (typ == "quick_draw"):
            self.quick_draw += rate
            
    def get(self, typ: str) -> StatusChangeRate:
        """
        Gets the value of the specified parameter.
        """
        if (typ == "HP"):
            return self.HP
        elif (typ == "ATK"):
            return self.ATK
        elif (typ == "MAT"):
            return self.MAT
        elif (typ == "DEF"):
            return self.DEF
        elif (typ == "MDF"):
            return self.MDF
        elif (typ == "SPD"):
            return self.SPD
        elif (typ == "LUK"):
            return self.LUK
        if (typ == "DEFHP"):
            return self.DEFHP
        elif (typ == "DEFATK"):
            return self.DEFATK
        elif (typ == "DEFMAT"):
            return self.DEFMAT
        elif (typ == "DEFDEF"):
            return self.DEFDEF
        elif (typ == "DEFMDF"):
            return self.DEFMDF
        elif (typ == "DEFSPD"):
            return self.DEFSPD
        elif (typ == "DEFLUK"):
            return self.DEFLUK
        elif (typ == "critical_damage"):
            return self.critical_damage
        elif (typ == "hate"):
            return self.hate
        elif (typ == "abnormal"):
            return self.abnormal_resistivity
        elif (typ == "flame"):
            return self.FLAME_element_resistivity
        elif (typ == "water"):
            return self.WATER_element_resistivity
        elif (typ == "soil"):
            return self.SOIL_element_resistivity
        elif (typ == "wind"):
            return self.WIND_element_resistivity
        elif (typ == "moon"):
            return self.MOON_element_resistivity
        elif (typ == "sun"):
            return self.SUN_element_resistivity
        elif (typ == "weak_bonus"):
            return self.weak_bonus
        elif (typ == "quick_draw"):
            return self.quick_draw
        
    def set(self, typ: str, rate: float):
        """
        Sets the specified value to the value of the specified parameter.
        """
        if (typ == "HP"):
            self.HP = rate
        elif (typ == "ATK"):
            self.ATK = rate
        elif (typ == "MAT"):
            self.MAT = rate
        elif (typ == "DEF"):
            self.DEF = rate
        elif (typ == "MDF"):
            self.MDF = rate
        elif (typ == "SPD"):
            self.SPD = rate
        elif (typ == "LUK"):
            self.LUK = rate
        elif (typ == "DEFHP"):
            self.DEFHP = rate
        elif (typ == "DEFATK"):
            self.DEFATK = rate
        elif (typ == "DEFMAT"):
            self.DEFMAT = rate
        elif (typ == "DEFDEF"):
            self.DEFDEF = rate
        elif (typ == "DEFMDF"):
            self.DEFMDF = rate
        elif (typ == "DEFSPD"):
            self.DEFSPD = rate
        elif (typ == "DEFLUK"):
            self.DEFLUK = rate
        elif (typ == "critical_damage"):
            self.critical_damage = rate
        elif (typ == "hate"):
            self.hate = rate
        elif (typ == "abnormal"):
            self.abnormal_resistivity = rate
        elif (typ == "flame"):
            self.FLAME_element_resistivity = rate
        elif (typ == "water"):
            self.WATER_element_resistivity = rate
        elif (typ == "soil"):
            self.SOIL_element_resistivity = rate
        elif (typ == "wind"):
            self.WIND_element_resistivity = rate
        elif (typ == "moon"):
            self.MOON_element_resistivity = rate
        elif (typ == "sun"):
            self.SUN_element_resistivity = rate
        elif (typ == "weak_bonus"):
            self.weak_bonus = rate
        elif (typ == "quick_draw"):
            self.quick_draw = rate
        
    def status_make(self, number: int, cls: int, level: int):
        """
        Make the status.
        """
        status_list = np.array(CONSTANTS.get("status_dict")[number][5:11])
        character_growth_rate_array = np.array([[5.2, 5.5, 4.0, 8.0, 7.1, 0.1], [5.2, 4.0, 5.5, 7.1, 8.0, 0.1], [6.0, 4.0, 4.0, 8.0, 8.8, 0.1], [4.5, 4.0, 4.0, 9.7, 8.8, 0.1], [4.7, 4.0, 5.0, 7.1, 9.7, 0.1]], dtype = "float")   # Growth in each class.
        character_friendship_rate_array = np.array([[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [5, 5, 5, 5, 5, 2], [8, 8, 8, 8, 8, 4], [10, 10, 10, 10, 10, 4], [12, 12, 12, 10, 10, 4], [15, 15, 15, 10, 10, 4]], dtype = "float")   # Correction value for friendship.
        friendship = 7
        level_rate = (1 + ((character_growth_rate_array[cls] * (level - 1))/100))
        friendship_rate = (1 + (character_friendship_rate_array[friendship-1]/100))
        _HP, _ATK, _MAT, _DEF, _MDF, _SPD = list((status_list * level_rate * friendship_rate).astype(int))
        self.HP = _HP
        self.ATK = _ATK
        self.MAT = _MAT
        self.DEF = _DEF
        self.MDF = _MDF
        self.SPD = _SPD
        self.LUK = 31
        self.DEFHP = _HP
        self.DEFATK = _ATK
        self.DEFMAT = _MAT
        self.DEFDEF = _DEF
        self.DEFMDF = _MDF
        self.DEFSPD = _SPD
        self.DEFLUK = 31

    def status_calc(self):
        """
        Calculate actual stats from status changes.
        self.ATK, self.MAT, self.DEF, self.MDF, self.SPD, self.LUK, self.critical_damage, self.hate, self.abnormal_resistivity, self.FLAME_element_resistivity, self.WATER_element_resistivity, self.SOIL_element_resistivity, self.WIND_element_resistivity, self.MOON_element_resistivity, self.SUN_element_resistivity, self.weak_bonus, self.quick_draw
        """
        self.ATK, self.MAT, self.DEF, self.MDF, self.SPD, self.LUK, self.critical_damage, self.abnormal_resistivity, self.FLAME_element_resistivity, self.WATER_element_resistivity, self.SOIL_element_resistivity, self.WIND_element_resistivity, self.MOON_element_resistivity, self.SUN_element_resistivity, self.weak_bonus, self.quick_draw = self.status_rates.status_calc([self.DEFATK, self.DEFMAT, self.DEFDEF, self.DEFMDF, self.DEFSPD, self.DEFLUK, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


class CharacterAbnormal:
    """
    This class holds information about the character's abnormal status.
    """
    def __init__(self):
        self.confusion = AbnormalStatus(CONSTANTS.get("confusion"))
        self.paralysis = AbnormalStatus(CONSTANTS.get("paralysis"))
        self.poison = AbnormalStatus(CONSTANTS.get("poison"))
        self.bearish = AbnormalStatus(CONSTANTS.get("bearish"))
        self.sleep = AbnormalStatus(CONSTANTS.get("sleep"))
        self.unhappy = AbnormalStatus(CONSTANTS.get("unhappy"))
        self.silence = AbnormalStatus(CONSTANTS.get("silence"))
        self.isolation = AbnormalStatus(CONSTANTS.get("isolation"))
            
    def get(self, typ: str) -> AbnormalStatus:
        """
        Gets the value of the specified parameter.
        """
        if (typ == "confusion"):
            return self.confusion
        elif (typ == "paralysis"):
            return self.paralysis
        elif (typ == "poison"):
            return self.poison
        elif (typ == "bearish"):
            return self.bearish
        elif (typ == "sleep"):
            return self.sleep
        elif (typ == "unhappy"):
            return self.unhappy
        elif (typ == "silence"):
            return self.silence
        elif (typ == "isolation"):
            return self.isolation
        
    def set(self, typ: str, set_typ: str, rate: float):
        """
        Sets the specified value to the value of the specified parameter.
        """
        if (typ == "confusion"):
            self.confusion.set(set_typ, rate)
        elif (typ == "paralysis"):
            self.paralysis.set(set_typ, rate)
        elif (typ == "poison"):
            self.poison.set(set_typ, rate)
        elif (typ == "bearish"):
            self.bearish.set(set_typ, rate)
        elif (typ == "sleep"):
            self.sleep.set(set_typ, rate)
        elif (typ == "unhappy"):
            self.unhappy.set(set_typ, rate)
        elif (typ == "silence"):
            self.silence.set(set_typ, rate)
        elif (typ == "isolation"):
            self.isolation.set(set_typ, rate)
        elif (typ == "all"):
            self.confusion.set(set_typ, rate)
            self.paralysis.set(set_typ, rate)
            self.poison.set(set_typ, rate)
            self.bearish.set(set_typ, rate)
            self.sleep.set(set_typ, rate)
            self.unhappy.set(set_typ, rate)
            self.silence.set(set_typ, rate)
            self.isolation.set(set_typ, rate)
            
    def abnormal_turn_calc(self):
        """
        Calculate abnormal turn.
        """
        self.confusion.add("turn", -1)
        self.paralysis.add("turn", -1)
        self.poison.add("turn", -1)
        self.bearish.add("turn", -1)
        self.sleep.add("turn", -1)
        self.unhappy.add("turn", -1)
        self.silence.add("turn", -1)
        self.isolation.add("turn", -1)


class CharacterCondition:
    """
    This class holds information about the character's condition status.
    """
    def __init__(self):
        self.ATK_nextbuff = ConditionStatus(CONSTANTS.get("ATK_next"), 1.0, 1)
        self.MAT_nextbuff = ConditionStatus(CONSTANTS.get("MAT_next"), 1.0, 1)
        self.LUK_nextbuff = ConditionStatus(CONSTANTS.get("LUK_next"), turn=1)
        self.stan = ConditionStatus(CONSTANTS.get("stan"), turn=1)
        self.barrier = ConditionStatus(CONSTANTS.get("barrier"), 1.0)
        self.recovery = ConditionStatus(CONSTANTS.get("recovery"), rate=0.0)
        self.patience = ConditionStatus(CONSTANTS.get("patience"))
        self.abnormal_invalid = ConditionStatus(CONSTANTS.get("abnormal_invalid"))
        self.status_change_invalid = ConditionStatus(CONSTANTS.get("status_invalid"))
        
    def get(self, typ: str) -> ConditionStatus:
        """
        Gets the value of the specified parameter.
        """
        if (typ == "ATK"):
            return self.ATK_nextbuff
        elif (typ == "MAT"):
            return self.MAT_nextbuff
        elif (typ == "LUK"):
            return self.LUK_nextbuff
        elif (typ == "stan"):
            return self.stan
        elif (typ == "barrier"):
            return self.barrier
        elif (typ == "recovery"):
            return self.recovery
        elif (typ == "patience"):
            return self.patience
        elif (typ == "abnormal"):
            return self.abnormal_invalid
        elif (typ == "status"):
            return self.status_change_invalid
        
    def set(self, typ: str, set_typ: str, rate: float):
        """
        Sets the specified value to the value of the specified parameter.
        """
        if (typ == "ATK"):
            self.ATK_nextbuff.set(set_typ, rate)
        elif (typ == "MAT"):
            self.MAT_nextbuff.set(set_typ, rate)
        elif (typ == "LUK"):
            self.LUK_nextbuff.set(set_typ, rate)
        elif (typ == "stan"):
            self.stan.set(set_typ, rate)
        elif (typ == "barrier"):
            self.barrier.set(set_typ, rate)
        elif (typ == "recovery"):
            self.recovery.set(set_typ, rate)
        elif (typ == "patience"):
            self.patience.set(set_typ, rate)
        elif (typ == "abnormal"):
            self.abnormal_invalid.set(set_typ, rate)
        elif (typ == "status"):
            self.status_change_invalid.set(set_typ, rate)
        
    def condition_turn_calc(self):
        """
        Calculate condition turn.
        """
        self.ATK_nextbuff.add("turn", -1)
        self.MAT_nextbuff.add("turn", -1)
        self.LUK_nextbuff.add("turn", -1)
        self.stan.add("turn", -1)
        self.recovery.add("turn", -1)
        self.patience.add("turn", -1)
        self.abnormal_invalid.add("turn", -1)
        self.status_change_invalid.add("turn", -1)


class CharacterSkill:
    """
    This class holds information about the character's skill.
    """
    def __init__(self):
        self.normal_skill = Skill()
        self.first_skill = Skill()
        self.second_skill = Skill()
        self.jamp_skill = Skill()
    
    def add(self, typ: str, set_typ: str, rate: float):
        """
        Adds the specified value to the value of the specified parameter.
        """
        if (typ == "normal"):
            self.normal_skill.add(set_typ, rate)
        elif (typ == "first"):
            self.first_skill.add(set_typ, rate)
        elif (typ == "second"):
            self.second_skill.add(set_typ, rate)
        elif (typ == "jamp"):
            self.jamp_skill.add(set_typ, rate)
        
    def get(self, typ: str) -> Skill:
        """
        Gets the value of the specified parameter.
        """
        if (typ == "normal"):
            return self.normal_skill
        elif (typ == "first"):
            return self.first_skill
        elif (typ == "second"):
            return self.second_skill
        elif (typ == "jamp"):
            return self.jamp_skill
        
    def set(self, typ: str, set_typ: str, rate: float):
        """
        Sets the specified value to the value of the specified parameter.
        """
        if (typ == "normal"):
            self.normal_skill.set(set_typ, rate)
        elif (typ == "first"):
            self.first_skill.set(set_typ, rate)
        elif (typ == "second"):
            self.second_skill.set(set_typ, rate)
        elif (typ == "jamp"):
            self.jamp_skill.set(set_typ, rate)

    def skill_recast_calc(self):
        """
        Calculate skill's recast.
        """
        self.first_skill.add("recast", -1)
        self.second_skill.add("recast", -1)

    def information_make(self, number: int, cls: int):
        """
        Make the skill's information
        """
        skill_info_data = CONSTANTS.get("skill_data_dict")
        skill_data = CONSTANTS.get("skill_dict")[number]
        skill_type_dict = {0 : SkillFunction().physics_attack_function, 1 : SkillFunction().magic_attack_function, 2 : SkillFunction().recover_function, 3 : SkillFunction().status_change_function, 4 : SkillFunction().status_change_reset_function, 5 : SkillFunction().status_change_invalid_function, 6 : SkillFunction().abnormal_function, 7 : SkillFunction().abnormal_recover_function, 8 : SkillFunction().abnormal_invalid_function, 9 : SkillFunction().status_change_function, 10 : SkillFunction().status_change_function, 11 : SkillFunction().status_change_function, 12 : SkillFunction().next_buff_finction, 13 : SkillFunction().next_buff_finction, 14 : SkillFunction().next_buff_finction, 15 : SkillFunction().barrier_function, 16 : SkillFunction().recast_change_function, 17 : SkillFunction().jamp_gauge_change_function, 18 : SkillFunction().status_change_function, 19 : SkillFunction().enemy_charge_change_function, 20 : SkillFunction().skill_card_function, 21 : SkillFunction().recovery_function, 22 : SkillFunction().status_change_function, 23 : SkillFunction().patience_function, 24 : SkillFunction().status_change_function}
        
        if (cls == CONSTANTS.get("warrier") or cls == CONSTANTS.get("knight")):
            value = (0, 75, 0, 17, 'ene_single_physics_attack', 500, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
            self.normal_skill.name = "通常攻撃"
            self.normal_skill.effect += "敵単体に物理の小ダメージ"
            self.normal_skill.info += value[CONSTANTS.get("skill_info")-1]
            self.normal_skill.data.append(value)
            self.normal_skill.def_recast += value[CONSTANTS.get("skill_recast")-1]
            self.normal_skill.function.append(skill_type_dict[value[CONSTANTS.get("skill_type")-1]])  
        else:
            value = (1, 75, 0, 17, 'ene_single_magic_attack', 1492, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
            self.normal_skill.name = "通常攻撃"
            self.normal_skill.effect += "敵単体に魔法の小ダメージ"
            self.normal_skill.info += value[CONSTANTS.get("skill_info")-1]
            self.normal_skill.data.append(value)
            self.normal_skill.def_recast += value[CONSTANTS.get("skill_recast")-1]
            self.normal_skill.function.append(skill_type_dict[value[CONSTANTS.get("skill_type")-1]])
        
        for key, value in skill_info_data.items():
            if (key in skill_data[CONSTANTS.get("first_skill_type")]):
                self.first_skill.name = skill_data[CONSTANTS.get("first_skill_name")]
                self.first_skill.effect += key
                self.first_skill.info += value[CONSTANTS.get("skill_info")-1]
                
                value = list(value)
                if (len(self.first_skill.data) == 0):
                    self.first_skill.data.append(value)
                else:
                    value[CONSTANTS.skill_info.skill_delay-1] = 5
                    value[CONSTANTS.skill_info.skill_charge-1] = 3
                    value[CONSTANTS.skill_info.skill_recast-1] = 5
                    self.first_skill.data.append(value)
                
                self.first_skill.def_recast += value[CONSTANTS.get("skill_recast")-1]
                self.first_skill.function.append(skill_type_dict[value[CONSTANTS.get("skill_type")-1]])
                
            if (key in skill_data[CONSTANTS.skill.second_skill_type]):
                self.second_skill.name = skill_data[CONSTANTS.get("second_skill_name")]
                self.second_skill.effect += key
                self.second_skill.info += value[CONSTANTS.get("skill_info")-1]
                value = list(value)
                if (len(self.second_skill.data) == 0):
                    self.second_skill.data.append(value)
                else:
                    value[CONSTANTS.skill_info.skill_delay-1] = 5
                    value[CONSTANTS.skill_info.skill_charge-1] = 3
                    value[CONSTANTS.skill_info.skill_recast-1] = 5
                    self.second_skill.data.append(value)
                self.second_skill.def_recast += value[CONSTANTS.get("skill_recast")-1]
                self.second_skill.function.append(skill_type_dict[value[CONSTANTS.get("skill_type")-1]])
                
            if (key in skill_data[CONSTANTS.skill.jamp_skill_type]):
                self.jamp_skill.name = skill_data[CONSTANTS.get("jamp_skill_name")]
                self.jamp_skill.effect += key
                self.jamp_skill.info += value[CONSTANTS.get("skill_info")-1]
                value = list(value)
                if (len(self.jamp_skill.data) == 0):
                    value[CONSTANTS.skill_info.skill_charge-1] = -100
                    value[CONSTANTS.skill_info.skill_recast-1] = 0
                    self.jamp_skill.data.append(value)
                else:
                    value[CONSTANTS.skill_info.skill_delay-1] = 5
                    value[CONSTANTS.skill_info.skill_charge-1] = 0
                    value[CONSTANTS.skill_info.skill_recast-1] = 0
                    self.jamp_skill.data.append(value)
                self.jamp_skill.def_recast += value[CONSTANTS.get("skill_recast")-1]
                self.jamp_skill.function.append(skill_type_dict[value[CONSTANTS.get("skill_type")-1]])

        
class Character:
    """
    This class holds information about all character's information.
    """
    def __init__(self, number: int, location: int):
        self.information = CharacterInformation(number, location)
        self.status = CharacterStatus()
        self.abnormal_status = CharacterAbnormal()
        self.condition_status = CharacterCondition()
        self.skill = CharacterSkill()
        self.information_make()
        
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
        elif (typ == "skill"):
            return self.skill
        
    def information_make(self):
        """
        Make the information of character's information.
        """
        self.information.information_make()
        self.status.status_make(self.information.get("number"), self.information.get("class"), self.information.get("level"))
        self.skill.information_make(self.information.get("number"), self.information.get("class"))
        self.information.set("delay", SkillFunction().delay_calc(self, 100))
        if  (self.information.location == 1):
            self.information.hate = 46.9
        elif (self.information.location == 2):
            self.information.hate = 31.3
        elif (self.information.location == 3):
            self.information.hate = 21.8
          
    def status_calc(self):
        """
        Calculate the actual status from status change.
        """
        self.status.status_calc()
        self.abnormal_status.abnormal_turn_calc()
        self.condition_status.condition_turn_calc()
        
    def skill_function(self, skill_typ: str, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]]) -> str:
        """
        Activate the skill.
        """
        act_log = ""
        if (skill_typ == "normal"):
            for skill, data in zip(self.skill.normal_skill.function, self.skill.normal_skill.data):
                act_log += skill(chr, chrs, enes, TL, data)
        elif (skill_typ == "skill1"):
            for skill, data in zip(self.skill.first_skill.function, self.skill.normal_skill.data):
                act_log += skill(chr, chrs, enes, TL, data)
        elif (skill_typ == "skill2"):
            for skill, data in zip(self.skill.second_skill.function, self.skill.normal_skill.data):
                act_log += skill(chr, chrs, enes, TL, data)
        elif (skill_typ == "jamp"):
            for skill, data in zip(self.skill.jamp_skill.function, self.skill.normal_skill.data):
                act_log += skill(chr, chrs, enes, TL, data)
        return act_log


class Enemy:
    """
    This class holds information about all enemy's information.
    """
    def __init__(self, number: int, location: int):
        self.information = CharacterInformation(number, location)
        self.status = CharacterStatus()
        self.abnormal_status = CharacterAbnormal()
        self.condition_status = CharacterCondition()
        self.skill_type = None
        
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
        
    def information_make(self):
        """
        Make the information of character's information.
        """
        HP, ATK, MAT, DEF, MDF, SPD = np.array(CONSTANTS.get("enemy_status_list")[self.information.get("number")]) * (self.information.get("level")-1)
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
        
    def status_calc(self):
        """
        Calculate the actual status from status change.
        """
        self.status.status_calc()
        self.abnormal_status.abnormal_turn_calc()
        self.condition_status.condition_turn_calc()
        
        
class SkillCard:
    """
    This class holds the skill card for skill.
    """
    def __init__(self, chr: Character, TL: list[Union[Character, Enemy]], data: list):
        self.act_character = chr
        self.skill_info = data[12]
        self.skill_rate = data[13]
        self.skill_delay = data[14]
        self.skill_charge = data[15]
        self.skill_num = data[16]
        self.time_line = TL
        self.exist = True
        self.delay = chr.information.get("delay")
        self.charge = 0
        self.location = 100
        self.data: list[int] = data
        
        for chr in self.time_line:
            if (type(chr) == SkillCard):
                self.location += 1

    def add(self, typ: str, rate: float):
        """
        Adds the specified value to the value of the specified parameter.
        """
        if (typ == "chr"):
            self.act_character += rate
        elif (typ == "info"):
            self.skill_info += rate
        elif (typ == "rate"):
            self.skill_rate += rate
        elif (typ == "skill_delay"):
            self.skill_delay += rate
        elif (typ == "skill_charge"):
            self.skill_charge += rate
        elif (typ == "num"):
            self.skill_num += rate
        elif (typ == "exist"):
            self.exist += rate
        elif (typ ==  "delay"):
            self.delay += rate
        elif (typ == "charge"):
            self.charge += rate
        elif (typ == "location"):
            self.location += rate
        elif (typ == "function"):
            self.functions.append(rate)
        
    def get(self, typ: str) -> int:
        """
        Gets the value of the specified parameter.
        """
        if (typ == "chr"):
            return self.act_character
        elif (typ == "info"):
            return self.skill_info
        elif (typ == "rate"):
            return self.skill_rate
        elif (typ == "skill_delay"):
            return self.skill_delay
        elif (typ == "skill_charge"):
            return self.skill_charge
        elif (typ == "num"):
            return self.skill_num
        elif (typ == "exist"):
            return self.exist
        elif (typ ==  "delay"):
            return self.delay
        elif (typ == "charge"):
            return self.charge
        elif (typ == "location"):
            return self.location
        elif (typ == "function"):
            return self.functions
        
    def set(self, typ: str, rate: float):
        """
        Sets the specified value to the value of the specified parameter.
        """
        if (typ == "chr"):
            self.act_character = rate
        elif (typ == "info"):
            self.skill_info = rate
        elif (typ == "rate"):
            self.skill_rate = rate
        elif (typ == "skill_delay"):
            self.skill_delay = rate
        elif (typ == "skill_charge"):
            self.skill_charge = rate
        elif (typ == "num"):
            self.skill_num = rate
        elif (typ == "exist"):
            self.exist = rate
        elif (typ ==  "delay"):
            self.delay = rate
        elif (typ == "charge"):
            self.charge = rate
        elif (typ == "location"):
            self.location = rate
        elif (typ == "function"):
            self.functions = [rate]
       
    def delay_calc(self, skill_delay):
        """
        Calculate skill delay.
        """
        base_SPD = 124 - ((self.act_character.status.get("SPD"))/2)
        if (base_SPD >= 100):
            base_SPD = 100
        elif (base_SPD <= 0):
            base_SPD = 0
        
        self.delay += np.floor(base_SPD * (skill_delay/100 * (1 - self.act_character.status.get("quick_draw"))))
           
    def skill_function(self, skill_card: SkillCard, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]],):
        """
        Activate the skill.
        """
        act_log = ""
        self.charge += self.skill_charge
        self.delay_calc(self.skill_delay)
        
        for _chr in [c for c in chrs+enes if (c != None)]:
            if ("recover" in self.skill_info):
                recover = SkillFunction().recover_calc(self.act_character, _chr, self.skill_rate)
                if (_chr.abnormal_status.unhappy.get("exist")):
                    recover = 0
                    act_log += f"""スキルカードは{CONSTANTS.get("name_dict")[_chr.get("info").get("name")][0]}に回復を与えられなかった。\n"""
                else:
                    _chr.status.add("HP", recover)
                    act_log += f"""スキルカードは{CONSTANTS.get("name_dict")[_chr.get("info").get("name")][0]}に{recover}回復を与えた。\n"""
            
            elif ("attack" in self.skill_info):
                if (self.act_character.information.get("class") == CONSTANTS.get("wizard") or self.act_character.information.get("class") == CONSTANTS.get("monk")):
                    damage = SkillFunction().magic_damage_calc(self.act_character, _chr, self.skill_rate)
                    ene_info = _chr.get("info")
                    ene_abnormal = _chr.get("abnormal")
                    ene_condition = _chr.get("condition")
                    _chr.get("status").add("HP", -damage)
                    act_log += f"""スキルカードは{ene_info.get("name")}{ene_info.get("location")}に{damage}ダメージを与えた。\n"""
                    stan = SkillFunction().stan_calc(self.act_character, _chr, damage)
                    ene_info.add("stan", stan)
                    
                    if (ene_info.get("stan") >= 1.0):
                        if (ene_condition.get("stan").get("exist") == True):
                            ene_info.add("delay", 20)
                        elif (ene_condition.get("stan").get("exist") == False):
                            ene_condition.set("stan", True)
                            ene_info.add("delay", 100)
                    
                    if (ene_abnormal.get("sleep").get("exist") == True):
                        ene_abnormal.get("sleep").set("exist", False)
                    if (ene_condition.get("patience").get("exist") == True):
                        ene_info.add("charge", ene_condition.get("patience").get("rate"))
                    if (ene_condition.get("barrier").get("exist") == True):
                        ene_condition.get("barrier").add("turn", -1)
                        if (ene_condition.get("barrier").get("turn") <= 0):
                            ene_condition.get("barrier").set("exist", False)
                            ene_condition.get("barrier").set("rate", 1.0)
                            
                else:
                    damage = SkillFunction().physics_damage_calc(self.act_character, _chr, self.skill_rate)
                    ene_info = _chr.get("info")
                    ene_abnormal = _chr.get("abnormal")
                    ene_condition = _chr.get("condition")
                    _chr.get("status").add("HP", -damage)
                    act_log += f"""スキルカードは{ene_info.get("name")}{ene_info.get("location")}に{damage}ダメージを与えた。\n"""
                    stan = SkillFunction().stan_calc(self.act_character, _chr, damage)
                    ene_info.add("stan", stan)
                    
                    if (ene_info.get("stan") >= 1.0):
                        if (ene_condition.get("stan").get("exist") == True):
                            ene_info.add("delay", 20)
                        elif (ene_condition.get("stan").get("exist") == False):
                            ene_condition.set("stan", True)
                            ene_info.add("delay", 100)
                    
                    if (ene_abnormal.get("sleep").get("exist") == True):
                        ene_abnormal.get("sleep").set("exist", False)
                    if (ene_condition.get("patience").get("exist") == True):
                        ene_info.add("charge", ene_condition.get("patience").get("rate"))
                    if (ene_condition.get("barrier").get("exist") == True):
                        ene_condition.get("barrier").add("turn", -1)
                        if (ene_condition.get("barrier").get("turn") <= 0):
                            ene_condition.get("barrier").set("exist", False)
                            ene_condition.get("barrier").set("rate", 1.0)
                            
            elif ("barrier" in self.skill_info):
                barrier = self.skill_rate
                _chr.condition_status.set("barrier", "exist", True)
                _chr.condition_status.set("barrier", "rate", barrier)
                _chr.condition_status.set("barrier", "turn", self.skill_num)
                act_log += f"""スキルカードは{CONSTANTS.get("name_dict")[_chr.get("info").get("name")][0]}にバリアを与えた。\n"""
                
        return act_log
  

class SkillFunction:
    """ 
    Hold the skill function.
    For this class, the following arguments have the following meanings:
    chr : This argument is the character that actually performs the action.
    chrs : This argument is the characters receiving this action.
    enes : This argument is the enemys receiving this action.
    TL : This argument is a time line and is used when you want to add objects directly to this time line.
    recast_dict : This argument contains the recast information of the skill had by the character. Used for actions that directly change recast.
    skill_data : This argument, as the name suggests, has skill data. It is a list of length 17.
    """
    def act_log_make(self, actioner: Union[Character, Enemy], covered_actioner: Union[Character, Enemy]):
        """
        Make the of action logging of character to enemy(character) or enemy to character(enemy)
        """
        act_log = ""
        try:
            act_log += f"""{CONSTANTS.get("name_dict")[actioner.get("info").get("name")][0]}は{CONSTANTS.get("name_dict")[covered_actioner.get("info").get("name")][0]}"""   # Actioner is character. Covered actioner is character.
        except:
            try:
                act_log += f"""{CONSTANTS.get("name_dict")[actioner.get("info").get("name")][0]}は{covered_actioner.get("info").get("name")}{covered_actioner.get("info").get("location")}"""   # Actioner is character. Covered actioner is enemy.
            except:
                try:
                    act_log += f"""{actioner.get("info").get("name")}{actioner.get("info").get("location")}は{CONSTANTS.get("name_dict")[covered_actioner.get("info").get("name")][0]}"""   # Actioner is enemy. Covered actioner is character.
                except:
                    act_log += f"""{actioner.get("info").get("name")}{actioner.get("info").get("location")}は{covered_actioner.get("info").get("name")}{covered_actioner.get("info").get("location")}"""   # Actioner is enemy. Covered actioner is enemy.
     
        return act_log

    def delay_calc(self, chr: Character, skill_delay: float) -> float:
        """
        Calculate the delay by skill's delay
        """
        base_SPD = 124 - ((chr.status.get("SPD"))/2)
        if (base_SPD >= 100):
            base_SPD = 100
        elif (base_SPD <= 0):
            base_SPD = 0
        
        return np.floor(base_SPD * (skill_delay/100 * (1 - chr.status.get("quick_draw"))))
           
    def element_resistance_calc(self, chr: Character, ene: Enemy):
        """
        Calculate the correction value of damage by element.
        """
        element_resistance = 1.0
        FLAME, WATER, SOIL, WIND, MOON, SUN = CONSTANTS.get("flame"), CONSTANTS.get("water"), CONSTANTS.get("soil"), CONSTANTS.get("wind"), CONSTANTS.get("moon"), CONSTANTS.get("sun")
        ene_FLAME_resistivity, ene_WATER_resistivity, ene_SOIL_resistivity, ene_WIND_resistivity, ene_MOON_resistivity, ene_SUN_resistivity = ene.status.get("flame"), ene.status.get("water"), ene.status.get("soil"), ene.status.get("wind"), ene.status.get("moon"), ene.status.get("sun")
        chr_element, ene_element = chr.information.get("element"), ene.information.get("element")
        
        if (chr_element == FLAME):
            element_resistivity = ene_FLAME_resistivity
        elif (chr_element == WATER):
            element_resistivity = ene_WATER_resistivity
        elif (chr_element == SOIL):
            element_resistivity = ene_SOIL_resistivity
        elif (chr_element == WIND):
            element_resistivity = ene_WIND_resistivity
        elif (chr_element == MOON):
            element_resistivity = ene_MOON_resistivity
        elif (chr_element == SUN):
            element_resistivity = ene_SUN_resistivity
            
        weak_bonus = chr.status.get("weak_bonus")
        
        # When the effect is outstanding.
        if (chr_element == FLAME and ene_element == WIND) or (chr_element == WIND and ene_element == SOIL) or (chr_element == SOIL and ene_element == WATER) or (chr_element == WATER and ene_element == FLAME) or (chr_element == 4 and ene_element == 5) or (chr_element == 5 and ene_element == 4):
            element_resistance = 2.0 * (1 - element_resistivity) 
            if element_resistance >= 2.4:
                element_resistance = 2.4
            elif element_resistance <= 1.6:
                element_resistance = 1.6
            element_resistance += weak_bonus
        
        # When the effect is not good enough.
        elif (chr_element == WIND and ene_element == FLAME) or (chr_element == SOIL and ene_element == WIND) or (chr_element == WATER and ene_element == SOIL) or (chr_element == FLAME and ene_element == WATER) :
            element_resistance = 0.5 * (1 - element_resistivity)
            if element_resistance >= 0.9:
                element_resistance = 0.9
            elif element_resistance <= 0.1:
                element_resistance = 0.1
        
        # When the effect is normal.
        else:
            element_resistance = 1.0 * (1 - element_resistivity)
            if element_resistance >= 1.4:
                element_resistance = 1.4
                
            elif element_resistance <= 0.6:
                element_resistance = 0.6

        return element_resistance
           
    def stan_calc(self, chr: Character, ene: Enemy, damage: float) -> float:
        """
        Calculate the stan gauge by action.
        """
        ene_DEFHP, ene_stan_conefficient = ene.status.get("DEFHP"), ene.information.get("stan_coefficient")
        element_resintance = self.element_resistance_calc(chr, ene)
        return round((damage / ene_DEFHP) * ene_stan_conefficient * element_resintance, 2)
    
    def default_function(self, chr: Character, delay: float, charge: float) -> str:
        """
        Actions to do with every action.
        delay : Delay value by action.
        charge : Charge value by action.
        """
        act_log = ""
        chr.status_calc()
        chr.status.status_rates.turn_calc()
        delay = self.delay_calc(chr, delay)
        chr.get("info").add("delay", delay)
        chr.get("info").add("charge", charge)
        chr.get("info").add("stan", -0.2)
        
        if (chr.get("abnormal").get("poison").get("exist") == True):
            poison_damage = chr.get("status").get("DEFHP") * 0.05
            chr.get("status").add("HP", -poison_damage)
            act_log = f"腹ペコにより、{poison_damage}ダメージを受けた。\n"
        if (chr.get("condition").get("recovery").get("exist") == True):
            recovery = chr.get("condition").get("recovery").get("rate")
            chr.get("status").add("HP", recovery)
            act_log += f"リカバリーにより{recovery}回復した。\n"
        
        return act_log
        
    def physics_damage_calc(self, chr: Character, ene: Enemy, skill_rate: float, jamp_rate):
        """
        Calculate physical damage.
        """
        random = (1.00 - 0.85) * np.random.rand() + 0.85   # Random number required for damage calculation.
        chr_ATK, chr_ATK_nextbuff, ene_DEF = chr.status.get("ATK"), chr.condition_status.ATK_nextbuff.get("rate"), ene.status.get("DEF")
        element_resistance = self.element_resistance_calc(chr, ene)
        physics_damage = np.ceil((random/0.06) * (chr_ATK/ene_DEF) * (skill_rate/100) * element_resistance * jamp_rate * chr_ATK_nextbuff)
        return physics_damage
        
    def magic_damage_calc(self, chr: Character, ene: Enemy, skill_rate: float, jamp_rate) -> float:
        """
        Calculate the magic damage.
        """
        random = (1.00 - 0.85) * np.random.rand() + 0.85   # Random number required for damage calculation.
        chr_MAT, chr_MAT_nextbuff, ene_MDF = chr.status.get("MAT"), chr.condition_status.MAT_nextbuff.get("rate"), ene.status.get("MDF")
        element_resistance = self.element_resistance_calc(chr, ene)
        magic_damage = np.ceil((random/0.06) * (chr_MAT/ene_MDF) * (skill_rate/100) * element_resistance * jamp_rate * chr_MAT_nextbuff)
        return magic_damage
        
    def critical_damage_calc(self, chr: Character, ene: Enemy) -> float:
        """
        Calculate the critical damage.
        """
        chr_LUK, ene_LUK, chr_element, ene_element = chr.status.get("LUK"), ene.status.get("LUK"), chr.information.get("element"), ene.information.get("element")

        if (chr_element == 0 and ene_element == 1) or (chr_element == 1 and ene_element == 2) or (chr_element == 2 and ene_element == 3) or (chr_element == 3 and ene_element == 0) or (chr_element == 4 and ene_element == 5) or (chr_element == 5 and ene_element == 4):
            cri_rate = chr_LUK * 1.20 - ene_LUK
        elif (chr_element == 1 and ene_element == 0) or (chr_element == 2 and ene_element == 1) or (chr_element == 3 and ene_element == 2) or (chr_element == 0 and ene_element == 3) :
            cri_rate = 0
        else:
            cri_rate = chr_LUK * 1.32 - ene_LUK
            
        critical_damage = chr.status.get("critical_damage")
        if (chr.condition_status.LUK_nextbuff.get("exist")):
            cri_rate = 1.0
        elif (ene.abnormal_status.bearish.get("exist")):
            cri_rate = 1.0
        elif (ene.condition_status.stan.get("exist")):
            cri_rate = 1.0
        
        if (cri_rate >= 1.0):
            cri_rate = 1.0
        elif (cri_rate <= 0.0):
            cri_rate = 0.0
        
        if (critical_damage <= 1.5):
            critical_damage = 1.5
        elif (critical_damage >= 3.0):
            critical_damage = 3.0
    
        return np.random.choice([critical_damage, 1.0], p=[cri_rate, 1.0-cri_rate])
    
    def recover_calc(self, recovering_chr: Character, recovered_chr: Character, skill_rate: float, jamp_rate=1.0) -> float:
        """
        Calculate the recovering_chr to recovered_chr value of recovery.
        """
        recovering_chr_MAT = 0.92 + recovering_chr.status.get("MAT") * 0.0005   # Make corrections to calculate recovery.
        if (recovering_chr_MAT <= 0.92):
            recovering_chr_MAT = 0.92
        elif (recovering_chr_MAT >= 1.5):
            recovering_chr_MAT = 1.5
            
        if (recovering_chr.information.get("element") == recovered_chr.information.get("element")):
            return np.floor((skill_rate / 100) * recovering_chr_MAT * 1.15 * jamp_rate * recovered_chr.status.get("DEFHP"))
        else:
            return np.floor((skill_rate / 100) * recovering_chr_MAT * 1.00 * jamp_rate * recovered_chr.status.get("DEFHP"))
    
    def abnormal_probability_calc(self, chr: Character, prob: float) -> bool:
        """
        Calculate status abnormal status grant probability.
        """
        random_num, abnormal_status_resistivity = np.random.randint(0, 100), chr.status.get("abnormal")
        abnormal_status_prob = prob - abnormal_status_resistivity
        if (0 <= random_num <= abnormal_status_prob):
            return True
        else:
            return False
    
    def physics_attack_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts physical attacks.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        for ene in [c for c in chrs+enes if (c != None)]:
            ene_info = ene.get("info")
            ene_abnormal = ene.get("abnormal")
            ene_condition = ene.get("condition")
            
            damage = self.physics_damage_calc(chr, ene, rate, jamp_rate) * self.critical_damage_calc(chr, ene) * ene_condition.get("barrier").get("rate")
            ene.get("status").add("HP", -damage)
            act_log += self.act_log_make(chr, ene) + f"""に{damage}ダメージを与えた。\n"""

            stan = self.stan_calc(chr, ene, damage)
            ene_info.add("stan", stan)
            
            if (ene_info.get("stan") >= 1.0):
                if (ene_condition.get("stan").get("exist") == True):
                    ene_info.add("delay", 20)
                elif (ene_condition.get("stan").get("exist") == False):
                    ene_condition.set("stan", "exist", True)
                    ene_info.add("delay", 100)
            
            if (ene_abnormal.get("sleep").get("exist") == True):
                ene_abnormal.get("sleep").set("exist", False)
            if (ene_condition.get("patience").get("exist") == True):
                ene_info.add("charge", ene_condition.get("patience").get("rate"))
            if (ene_condition.get("barrier").get("exist") == True):
                ene_condition.get("barrier").add("turn", -1)
                if (ene_condition.get("barrier").get("turn") <= 0):
                    ene_condition.get("barrier").set("exist", False)
                    ene_condition.get("barrier").set("rate", 1.0)
                    
        chr.get("condition").get("ATK").set("exist", False)
        chr.get("condition").get("ATK").set("rate", 1.0)
        act_log += self.default_function(chr, delay, charge)
        return act_log
        
    def magic_attack_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts magical attacks.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        for ene in [c for c in chrs+enes if (c != None)]:
            ene_info = ene.get("info")
            ene_abnormal = ene.get("abnormal")
            ene_condition = ene.get("condition")
            
            damage = self.magic_damage_calc(chr, ene, rate, jamp_rate) * self.critical_damage_calc(chr, ene) * ene_condition.get("barrier").get("rate")
            ene.get("status").add("HP", -damage)
            act_log += self.act_log_make(chr, ene) + f"""に{damage}ダメージを与えた。\n"""
            
            stan = self.stan_calc(chr, ene, damage)
            ene_info.add("stan", stan)
            
            if (ene_info.get("stan") >= 1.0):
                if (ene_condition.get("stan").get("exist") == True):
                    ene_info.add("delay", 20)
                elif (ene_condition.get("stan").get("exist") == False):
                    ene_condition.set("stan", "exist", True)
                    ene_info.add("delay", 100)
            
            if (ene_abnormal.get("sleep").get("exist") == True):
                ene_abnormal.get("sleep").set("exist", False)
            if (ene_condition.get("patience").get("exist") == True):
                ene_info.add("charge", ene_condition.get("patience").get("rate"))
            if (ene_condition.get("barrier").get("exist") == True):
                ene_condition.get("barrier").add("turn", -1)
                if (ene_condition.get("barrier").get("turn") <= 0):
                    ene_condition.get("barrier").set("exist", False)
                    ene_condition.get("barrier").set("rate", 1.0)
                    
        chr.get("condition").get("MAT").set("exist", False)
        chr.get("condition").get("MAT").set("rate", 1.0)
        act_log += self.default_function(chr, delay, charge)
        return act_log
            
    def recover_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts recover.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        for _chr in [c for c in chrs+enes if (c != None)]:
            recover = self.recover_calc(chr, _chr, rate, jamp_rate)
            if (_chr.abnormal_status.unhappy.get("exist")):
                recover = 0
                act_log += self.act_log_make(chr, _chr) + """回復を与えられなかった。\n"""
            
            else:
                _chr.status.add("HP", recover)
                act_log += self.act_log_make(chr, _chr) + f"""に{recover}回復を与えた。\n"""
            
        act_log += self.default_function(chr, delay, charge)
        return act_log
        
    def status_change_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, turn: int = 3, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts status change.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        status_dict = {0 : "HP", 1 : "ATK", 2 : "MAT", 3 : "DEF", 4 : "MDF", 5 : "SPD", 6 : "LUK", 14 : "critical_damage", 15 : "hate", 16 : "abnormal", 17 : "flame", 18 : "water", 19 : "soil", 20 : "wind", 21 : "moon", 22 : "sun", 23 : "weak_bonus", 24 : "quick_draw"}
        status_rate = StatusChangeRate(status_type, rate)
        status_rate.set("turn", turn)
        for _chr in [c for c in chrs+enes if (c != None)]:
            if (rate <= 0):
                if (_chr.get("condition").get("status").get("exist") == True):
                    act_log += self.act_log_make(chr, _chr) + """にステータスダウンを与えられなかった。\n"""
                else:
                    _chr.status.status_rates.add(status_dict[status_type], status_rate)
                    act_log += self.act_log_make(chr, _chr) + f"""に{status_dict[status_type]}ステータスダウンを与えた。\n"""
            else:
                _chr.status.status_rates.add(status_dict[status_type], status_rate)
                act_log += self.act_log_make(chr, _chr) + f"""に{status_dict[status_type]}ステータスアップを与えた。\n"""
            _chr.status_calc()
        act_log += self.default_function(chr, delay, charge)
        return act_log
    
    def status_change_reset_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts status change reset.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        status_dict = {1 : "ATK", 2 : "MAT", 3 : "DEF", 4 : "MDF", 5 : "SPD", 6 : "LUK"}
        status_rates: list[StatusChangeRate] = []
        for _chr in [c for c in chrs+enes if (c != None)]:
            if (status_type == 1):
                status_rates = _chr.status.status_rates.get("ATK")
            elif (status_type == 2):
                status_rates = _chr.status.status_rates.get("MAT")
            elif (status_type == 3):
                status_rates = _chr.status.status_rates.get("DEF")
            elif (status_type == 4):
                status_rates = _chr.status.status_rates.get("MDF")
            elif (status_type == 5):
                status_rates = _chr.status.status_rates.get("SPD")
            elif (status_type == 6):
                status_rates = _chr.status.status_rates.get("LUK")
            
            for status_rate in status_rates:
                if (reset_bool == 1):   # Status change up.
                    if (status_rate.get("rate") >= 0):
                        status_rate.set("exist", False)
                else:    # status change down.
                    if (status_rate.get("rate") <= 0):
                        status_rate.set("exist", False)
            act_log += self.act_log_make(chr, _chr) + f"""に{status_dict[status_type]}ステータス変化をリセットした。\n"""
        
        act_log += self.default_function(chr, delay, charge)
        return act_log        
        
    def status_change_invalid_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, turn: int = 3, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts status change invalid.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        status_dict = {1 : "ATK", 2 : "MAT", 3 : "DEF", 4 : "MDF", 5 : "SPD", 6 : "LUK"}
        for _chr in [c for c in chrs+enes if (c != None)]:
            _chr.get("condition").set("status", "exist", True)
            _chr.get("condition").set("status", "turn", turn)
            act_log += self.act_log_make(chr, _chr) + f"""にステータス変化無効を与えた。\n"""
        act_log += self.default_function(chr, delay, charge)
        return act_log
        
    def abnormal_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts abnormal status.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        abnormal_dict = {0 : "confusion", 1 : "paralysis", 2 : "poison", 3 : "bearish", 4 : "sleep", 5 : "unhappy", 6 : "silence", 7 : "isolation", 8 : "all"}
        for _chr in [c for c in chrs+enes if (c != None)]:
            if (self.abnormal_probability_calc(_chr, prob) == True):
                if (_chr.condition_status.get("abnormal").get("exist") == True):
                    act_log += self.act_log_make(chr, _chr) + f"""に{CONSTANTS.get("abnormal_dict")[abnormal_type]}を与えられなかった。\n"""
                else:
                    _chr.abnormal_status.set(abnormal_dict[abnormal_type], "exist", True)
                    _chr.abnormal_status.set(abnormal_dict[abnormal_type], "turn", 3)
                    act_log += self.act_log_make(chr, _chr) + f"""に{CONSTANTS.get("abnormal_dict")[abnormal_type]}を与えた。\n"""
            else:
                act_log += self.act_log_make(chr, _chr) + f"""に{CONSTANTS.get("abnormal_dict")[abnormal_type]}を与えられなかった。\n"""
        
        act_log += self.default_function(chr, delay, charge)
        return act_log
        
    def abnormal_recover_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts abnormal recover.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        abnormal_dict = {0 : "confusion", 1 : "paralysis", 2 : "poison", 3 : "bearish", 4 : "sleep", 5 : "unhappy", 6 : "silence", 7 : "isolation", 8 : "all"}
        for _chr in [c for c in chrs+enes if (c != None)]:
            if (_chr.abnormal_status.get(abnormal_dict[abnormal_type]).get("exist") == True):
                _chr.abnormal_status.set(abnormal_dict[abnormal_type], "exist", False)
                _chr.abnormal_status.set(abnormal_dict[abnormal_type], "turn", 0)
                act_log += self.act_log_make(chr, _chr) + f"""の{CONSTANTS.get("abnormal_dict")[abnormal_type]}を回復した。\n"""
                
        act_log += self.default_function(chr, delay, charge)
        return act_log
        
    def abnormal_invalid_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts abnormal invalid.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        for _chr in [c for c in chrs+enes if (c != None)]:
            _chr.get("condition").set("abnormal", "exist", True)
            _chr.get("condition").set("abnormal", "turn", 3)
            act_log += self.act_log_make(chr, _chr) + f"""にステータス変化無効を与えた。\n"""
        act_log += self.default_function(chr, delay, charge)
        return act_log
        
    def next_buff_finction(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts next buff.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        for _chr in [c for c in chrs+enes if (c != None)]:
            if (typ == 12):
                _chr.condition_status.set("ATK", "exist", True)
                _chr.condition_status.set("ATK", "rate", rate)
                act_log += self.act_log_make(chr, _chr) + f"""にATKネクストバフを与えた。\n"""
            elif (typ == 13):
                _chr.condition_status.set("MAT", "exist", True)
                _chr.condition_status.set("MAT", "rate", rate)
                act_log += self.act_log_make(chr, _chr) + f"""にMATネクストバフを与えた。\n"""
            elif (typ == 14):
                _chr.condition_status.set("LUK", "exist", True)
                _chr.condition_status.set("LUK", "rate", rate)
                act_log += self.act_log_make(chr, _chr) + f"""にLUKネクストバフを与えた。\n"""
        
        act_log += self.default_function(chr, delay, charge)
        return act_log
        
    def barrier_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts barrier.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        for _chr in [c for c in chrs+enes if (c != None)]:
            _chr.condition_status.set("barrier", "exist", True)
            _chr.condition_status.set("barrier", "rate", rate)
            _chr.condition_status.set("barrier", "turn", barrier_num)
            act_log += self.act_log_make(chr, _chr) + f"""にバリアを与えた。\n"""
        
        act_log += self.default_function(chr, delay, charge)
        return act_log
 
    def recast_change_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts recast change.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        for _chr in [c for c in chrs+enes if (c != None)]:
            _chr.skill.add("first", "recast", rate/100)
            _chr.skill.add("second", "recast", rate/100)
            act_log += self.act_log_make(chr, _chr) + f"""にリキャスト変化を与えた。\n"""
        
        act_log += self.default_function(chr, delay, charge)
        return act_log
 
    def jamp_gauge_change_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts jamp gauge change.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        chr.information.add("charge", rate)
        act_log += f"""{CONSTANTS.get("name_dict")[chr.get("info").get("name")][0]}はとっておきゲージを増やした。\n"""
        act_log += self.default_function(chr, delay, charge)
        return act_log
        
    def enemy_charge_change_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts enemy charge change.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        for _chr in [c for c in chrs+enes if (c != None)]:
            _chr.information.add("charge", -rate)
            act_log += self.act_log_make(chr, _chr) + f"""のチャージを減らした。\n"""
        
        act_log += self.default_function(chr, delay, charge)
        return act_log
        
    def skill_card_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts skill card.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        skill_card = SkillCard(chr, TL, skill_data)
        TL.append(skill_card)
        try:
            act_log += f"""{CONSTANTS.get("name_dict")[chr.get("info").get("name")][0]}はスキルカードを設置した。\n"""
        except:
            act_log += f"""{chr.get("info").get("name")}{chr.get("info").get("location")}はスキルカードを設置した。\n"""
            
        act_log += self.default_function(chr, delay, charge)
        return act_log
        
    def recovery_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts recovery.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        for _chr in [c for c in chrs+enes if (c != None)]:
            _chr.condition_status.set("recovery", "exist", True)
            recover_rate = self.recover_calc(chr, _chr, rate)
            _chr.condition_status.set("recovery", "rate", recover_rate)
            _chr.condition_status.set("recovery", "turn", 3)
            act_log += self.act_log_make(chr, _chr) + f"""にリカバリーを与えた。\n"""
        
        act_log += self.default_function(chr, delay, charge)
        return act_log
        
    def patience_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts patience.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        for _chr in [c for c in chrs+enes if (c != None)]:
            _chr.condition_status.set("patience", "exist", True)
            _chr.condition_status.set("patience", "turn", 3)
            act_log += self.act_log_make(chr, _chr) + f"""にがまんを与えた。\n"""
        
        act_log += self.default_function(chr, delay, charge)
        return act_log
    
    def fixed_damage_function(self, chr: Character, chrs: list[Character], enes: list[Enemy], TL: list[Union[Character, Enemy]], skill_data: list, jamp_rate: float = 1.0) -> str:
        """
        A function that inflicts fixed damage.
        """
        act_log = ""
        typ, delay, recast, charge, info, rate, status_type, reset_bool, prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = skill_data
        for ene in [c for c in chrs+enes if (c != None)]:
            ene_info = ene.get("info")
            ene_abnormal = ene.get("abnormal")
            ene_condition = ene.get("condition")
            
            damage = rate * ene_condition.get("barrier").get("rate")
            ene.get("status").add("HP", -damage)
            act_log += self.act_log_make(chr, ene) + f"""に{damage}固定ダメージを与えた。\n"""
        
            if (ene_info.get("stan") >= 1.0):
                if (ene_condition.get("stan").get("exist") == True):
                    ene_info.add("delay", 20)
                elif (ene_condition.get("stan").get("exist") == False):
                    ene_condition.set("stan", "exist", True)
                    ene_info.add("delay", 100)
            
            if (ene_abnormal.get("sleep").get("exist") == True):
                ene_abnormal.get("sleep").set("exist", False)
            if (ene_condition.get("barrier").get("exist") == True):
                ene_condition.get("barrier").add("turn", -1)
                if (ene_condition.get("barrier").get("turn") <= 0):
                    ene_condition.get("barrier").set("exist", False)
                    ene_condition.get("barrier").set("rate", 1.0)
                    
        act_log += self.default_function(chr, delay, charge)
        return act_log
        

###
# Finished that defines the character class.
###


###
# Test
###

if __name__ == "__main__":
    c = Character(1, 1)
    print(c.information.name)

###
# Test
###
