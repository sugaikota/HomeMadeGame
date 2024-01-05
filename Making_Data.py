# coding: UTF-8
import sqlite3
import csv
from pprint import pprint

###
# Data.
###

title_dict = {
                0 : "ひだまりスケッチ", 1 : "ゆゆ式", 2 : "がっこうぐらし！", 3 : "Aチャンネル", 4 : "きんいろモザイク", 
                5 : "NEW_GAME!",6 : "ステラのまほう", 7 : "うらら迷路帖", 8 : "キルミーベイベー", 9 : "桜Trick", 
                10 : "ブレンド・S", 11 : "夢喰いメリー", 12 : "スロウスタート",13 : "ゆるキャン△", 14 : "ハナヤマタ", 
                15 : "こみっくがーるず", 16 : "あんハピ♪", 17 : "けいおん！",18 : "はるかなレシーブ",19 : "ご注文はうさぎですか？", 
                20 : "アニマエール",21 : "きららファンタジア",22 : "三者三葉", 23 : "GA 芸術科アートデザインクラス",24 : "棺担ぎのクロ。～懐中旅話～",
                25 : "まちカドまぞく", 26 : "はるみーねしょん", 27 : "幸腹グラフィティ", 28 : "恋する小惑星",29 : "球詠",
                30 : "あっちこっち", 31 : "おちこぼれフルーツタルト",32 : "ぱわーおぶすまいる。", 33 : "こはる日和。", 34 : "まんがタイム", 
                35 : "スローループ", 36 : "RPG不動産", 37 : "ぼっちざろっく"
             }


character_name_dict = {
                        0: "ゆの", 1 : "宮子", 2 : "ヒロ", 3 : "沙英", 4 : "乃莉", 5 : "なずな", 
                        6 : "野々原ゆずこ", 7 : "櫟井唯", 8 : "日向縁", 9 : "松本頼子", 10 : "相川千穂", 73 : "長谷川ふみ", 95 : "岡野佳", 
                        11 : "丈槍由紀", 12 : "恵比須沢胡桃", 13 : "若狭悠里", 14 : "直樹美紀", 15 : "佐倉慈", 170 : "祠堂圭", 228 : "大人の丈槍由紀", 229 : "大人の直樹美紀", 230 : "大人の恵比須沢胡桃", 231 : "大人の若狭悠里", 
                        16 : "トオル", 17 : "るん", 18 : "ユー子", 19 : "ナギ", 51 : "ミホ", 120 : "鬼頭紀美子", 147 : "ユタカ", 
                        20 : "九条カレン", 21 : "アリス・カータレット", 22 : "大宮忍", 23 : "小路綾", 24 : "猪熊陽子", 25 : "松原穂乃果", 46 : "大宮勇", 58 : "烏丸さくら", 74 : "久世橋朱里", 211 : "日暮香奈", 
                        26 : "涼風青葉", 27 : "滝本ひふみ", 28 : "篠田はじめ", 29 : "飯島ゆん", 30 : "八神コウ", 31 : "遠山りん", 47 : "望月紅葉", 54 : "鳴海ツバメ", 57 : "桜ねね", 67 : "阿波根うみこ", 94 : "星川ほたる", 124 : "葉月しずく", 
                        32 : "本田珠輝", 33 : "村上椎奈", 34 : "関あやめ", 35 : "布田裕美音", 36 : "藤川歌夜", 72 : "百武照", 112 : "飯野水葉", 115 : "池谷乃々", 158 : "鶴瀬まつり", 172 : "稲葉兎和", 
                        37 : "千矢", 38 : "巽紺", 39 : "雪見小梅", 40 : "棗ノノ", 41 : "色井佐久", 42 : "棗ニナ", 78 : "二条臣", 207 : "花原椿", 216 : "マリ・キスピルクエット", 
                        43 : "ソーニャ", 52 : "折部やすな", 53 : "呉織あぎり", 
                        44 : "高山春香", 45 : "園田優", 59 : "南しずく", 60 : "野田コトネ", 61 : "池野楓",62 : "飯塚ゆず", 100 : "乙川 澄", 167 : "園田美月", 
                        48 : "桜ノ宮苺香", 49 : "日向夏帆", 50 : "星川麻冬", 79 : "天野美雨", 98 : "神崎ひでり", 99 : "桜ノ宮愛香", 
                        55 : "メリー・ナイトメア", 56 : "橘勇魚", 146 : "エンギ・スリーピース", 189 : "光凪由衣", 220 : "クリオネ", 
                        63 : "一之瀬花名", 64 : "千石冠", 65 : "十倉栄依子", 66 : "百地たまて", 119 : "万年大会", 156 : "京塚志温", 171 : "榎並清瀬", 196 : "十倉光希", 
                        68 : "志摩リン", 69 : "各務原なでしこ", 70 : "大垣千秋", 71 : "犬山あおい", 103 : "斎藤恵那", 222 : "土岐綾乃", 237 : "大人の志摩リン", 
                        75 : "関谷なる", 76 : "ハナ・N・フォンテーンスタンド", 77 : "笹目ヤヤ", 166 : "西御門多美", 212 : "常盤真智", 
                        80 : "萌田薫子", 81 : "恋塚小夢", 82 : "色川琉姫", 83 : "勝木翼", 145 : "怖浦すず", 155 : "色川美姫", 206 : "虹野美晴", 238 : "編沢まゆ", 
                        84 : "花小泉杏", 101 : "雲雀丘瑠璃", 102 : "久米川牡丹", 149 : "萩生響", 150 : "江古田蓮", 165 : "狭山椿", 
                        85 : "平沢唯", 86 : "中野梓", 87 : "秋山澪", 88 : "田井中律", 89 : "琴吹紬", 96 : "平沢憂", 243 : "山中さわ子", 
                        90 : "大空遥", 91 : "比嘉かなた", 92 : "トーマス・紅愛", 93 : "トーマス・恵美理", 134 : "大城あかり", 173 : "遠井成美", 174 : "立花彩紗", 
                        104 : "ココア", 105 : "チノ", 114 : "リゼ", 129 : "千夜", 130 : "シャロ", 142 : "マヤ", 143 : "メグ", 161 : "モカ", 221 : "青山ブルーマウンテン", 
                        106 : "鳩谷こはね", 107 : "有馬ひづめ", 108 : "猿渡宇希", 109 : "舘島虎徹", 110 : "牛久花和", 
                        111 : "ランプ", 113 : "アルシーヴ", 116 : "シュガー", 117 : "ポルカ", 118 : "コルク", 131 : "ジンジャー", 135 : "セサミ", 136 : "クレア", 141 : "ソルト", 148 : "きらら", 154 : "ライネ", 162 : "フェンネル", 163 : "カンナ", 178 : "カルダモン", 190 : "ハッカ", 219 : "ソラ", 223 : "メディア", 227 : "住良木うつつ", 244 : "エニシダ", 245 : "ハイプリス", 246 : "サンストーン", 
                        121 : "西川葉子", 122 : "小田切双葉", 123 : "葉山照", 164 : "西山芹奈", 179 : "薗部篠", 194 : "近藤亜紗子", 195 : "葉山光", 
                        125 : "山口如月", 127 : "野田ミキ", 128 : "友兼", 132 : "大道雅", 133 : "野崎奈三子", 
                        126 : "クロ", 
                        137 : "吉田優子", 138 : "千代田桃", 139 : "リリス", 140 : "陽夏木ミカン", 157 : "吉田良子", 
                        144 : "細野はるみ", 191 : "坂本香樹", 192 : "高橋ユキ", 197 : "細野あるみ", 
                        151 : "町子リョウ", 152 : "森野きりん", 153 : "椎名", 205 : "内木ユキ", 
                        159 : "木ノ幡みら", 160 : "真中あお", 184 : "猪瀬舞", 209 : "桜井美影", 210 : "森野真理", 
                        168 : "武田詠深", 169 : "山崎珠姫", 193 : "川口芳乃", 217 : "中村希", 
                        175 : "御庭つみき", 176 : "春野姫", 177 : "片瀬真宵", 208 : "桜川キクヱ", 
                        180 : "桜イノ", 181 : "関野ロコ", 182 : "貫井はゆ", 183 : "前原仁菜", 213 : "緑へも", 
                        185 : "篠華まゆ", 186 : "虎道環", 218 : "叢園寺 観久", 
                        187 : "小野坂こはる", 188 : "橘ニナ", 
                        214 : "北沢みさき", 215 : "牧之瀬ひまり", 236 : "小野坂さおり", 198 : "里中チエ", 199 : "白井麗子", 200 : "倉橋莉子", 201 : "真木夏緒", 202 : "小森しゅり", 203 : "西鳥めぐみ", 204 : "根岸まさ子", 
                        224 : "海凪ひより", 225 : "海凪小春", 226 : "吉永恋", 
                        232 : "風色琴音", 233 : "ファー", 234 : "ルフリア", 235 : "ラキラ", 
                        239 : "後藤ひとり", 240 : "伊地知虹夏", 241 : "山田リョウ", 242 : "喜多郁代"
}


def skill_information_dict():
    skill_attack_skill_type = {'敵単体に物理の小ダメージ': [1457, 115, 13, 17, 'ene_single_physics_attack'], '敵単体に物理の中ダメージ': [1894, 120, 16, 17, 'ene_single_physics_attack'], '敵単体に物理の大ダメージ': [2234, 135, 23, 17, 'ene_single_physics_attack'], '敵単体に物理の特大ダメージ': [2575, 135, 27, 17, 'ene_single_physics_attack'], '敵単体に物理の超特大ダメージ': [2828, 140, 30, 17, 'ene_single_physics_attack'], '敵単体に炎属性の小ダメージ': [1492, 115, 14, 17, 'ene_single_magic_attack'], '敵単体に水属性の小ダメージ': [1492, 115, 14, 17, 'ene_single_magic_attack'], '敵単体に土属性の小ダメージ': [1492, 115, 14, 17, 'ene_single_magic_attack'], '敵単体に風属性の小ダメージ': [1492, 115, 14, 17, 'ene_single_magic_attack'], '敵単体に陽属性の小ダメージ': [1492, 115, 14, 17, 'ene_single_magic_attack'], '敵単体に月属性の小ダメージ': [1492, 115, 14, 17, 'ene_single_magic_attack'], '敵単体に炎属性の中ダメージ': [1805, 120, 16, 17, 'ene_single_magic_attack'], '敵単体に水属性の中ダメージ': [1805, 120, 16, 17, 'ene_single_magic_attack'], '敵単体に土属性の中ダメージ': [1805, 120, 16, 17, 'ene_single_magic_attack'], '敵単体に風属性の中ダメージ': [1805, 120, 16, 17, 'ene_single_magic_attack'], '敵単体に陽属性の中ダメージ': [1805, 120, 16, 17, 'ene_single_magic_attack'], '敵単体に月属性の中ダメージ': [1805, 120, 16, 17, 'ene_single_magic_attack'], '敵単体に炎属性の大ダメージ': [2125, 120, 23, 17, 'ene_single_magic_attack'], '敵単体に水属性の大ダメージ': [2125, 120, 23, 17, 'ene_single_magic_attack'], '敵単体に土属性の大ダメージ': [2125, 120, 23, 17, 'ene_single_magic_attack'], '敵単体に風属性の大ダメージ': [2125, 120, 23, 17, 'ene_single_magic_attack'], '敵単体に陽属性の大ダメージ': [2125, 120, 23, 17, 'ene_single_magic_attack'], '敵単体に月属性の大ダメージ': [2125, 120, 23, 17, 'ene_single_magic_attack'], '敵単体に炎属性の特大ダメージ': [2468, 135, 28, 17, 'ene_single_magic_attack'], '敵単体に水属性の特大ダメージ': [2468, 135, 28, 17, 'ene_single_magic_attack'], '敵単体に土属性の特大ダメージ': [2468, 135, 28, 17, 'ene_single_magic_attack'], '敵単体に風属性の特大ダメージ': [2468, 135, 28, 17, 'ene_single_magic_attack'], '敵単体に陽属性の特大ダメージ': [2468, 135, 28, 17, 'ene_single_magic_attack'], '敵単体に月属性の特大ダメージ': [2468, 135, 28, 17, 'ene_single_magic_attack'], '敵単体に炎属性の超特大ダメージ': [2793, 140, 31, 17, 'ene_single_magic_attack'], '敵単体に水属性の超特大ダメージ': [2793, 140, 31, 17, 'ene_single_magic_attack'], '敵単体に土属性の超特大ダメージ': [2793, 140, 31, 17, 'ene_single_magic_attack'], '敵単体に風属性の超特大ダメージ': [2793, 140, 31, 17, 'ene_single_magic_attack'], '敵単体に陽属性の超特大ダメージ': [2793, 140, 31, 17, 'ene_single_magic_attack'], '敵単体に月属性の超特大ダメージ': [2793, 140, 31, 17, 'ene_single_magic_attack'], '敵全体に物理の小ダメージ': [1065, 115, 21, 17, 'ene_whole_physics_attack'], '敵全体に物理の中ダメージ': [1272, 120, 25, 17, 'ene_whole_physics_attack'], '敵全体に物理の大ダメージ': [1568, 135, 35, 17, 'ene_whole_physics_attack'], '敵全体に物理の特大ダメージ': [1805, 135, 41, 17, 'ene_whole_physics_attack'], '敵全体に物理の超特大ダメージ': [2078, 140, 44, 17, 'ene_whole_physics_attack'], '敵全体に炎属性の小ダメージ': [1065, 115, 21, 17, 'ene_whole_magic_attack'], '敵全体に水属性の小ダメージ': [1065, 115, 21, 17, 'ene_whole_magic_attack'], '敵全体に土属性の小ダメージ': [1065, 115, 21, 17, 'ene_whole_magic_attack'], '敵全体に風属性の小ダメージ': [1065, 115, 21, 17, 'ene_whole_magic_attack'], '敵全体に陽属性の小ダメージ': [1065, 115, 21, 17, 'ene_whole_magic_attack'], '敵全体に月属性の小ダメージ': [1065, 115, 21, 17, 'ene_whole_magic_attack'], '敵全体に炎属性の中ダメージ': [1332, 120, 25, 17, 'ene_whole_magic_attack'], '敵全体に水属性の中ダメージ': [1332, 120, 25, 17, 'ene_whole_magic_attack'], '敵全体に土属性の中ダメージ': [1332, 120, 25, 17, 'ene_whole_magic_attack'], '敵全体に風属性の中ダメージ': [1332, 120, 25, 17, 'ene_whole_magic_attack'], '敵全体に陽属性の中ダメージ': [1332, 120, 25, 17, 'ene_whole_magic_attack'], '敵全体に月属性の中ダメージ': [1332, 120, 25, 17, 'ene_whole_magic_attack'], '敵全体に炎属性の大ダメージ': [1568, 135, 35, 17, 'ene_whole_magic_attack'], '敵全体に水属性の大ダメージ': [1568, 135, 35, 17, 'ene_whole_magic_attack'], '敵全体に土属性の大ダメージ': [1568, 135, 35, 17, 'ene_whole_magic_attack'], '敵全体に風属性の大ダメージ': [1568, 135, 35, 17, 'ene_whole_magic_attack'], '敵全体に陽属性の大ダメージ': [1568, 135, 35, 17, 'ene_whole_magic_attack'], '敵全体に月属性の大ダメージ': [1568, 135, 35, 17, 'ene_whole_magic_attack'], '敵全体に炎属性の特大ダメージ': [1805, 135, 41, 17, 'ene_whole_magic_attack'], '敵全体に水属性の特大ダメージ': [1805, 135, 41, 17, 'ene_whole_magic_attack'], '敵全体に土属性の特大ダメージ': [1805, 135, 41, 17, 'ene_whole_magic_attack'], '敵全体に風属性の特大ダメージ': [1805, 135, 41, 17, 'ene_whole_magic_attack'], '敵全体に陽属性の特大ダメージ': [1805, 135, 41, 17, 'ene_whole_magic_attack'], '敵全体に月属性の特大ダメージ': [1805, 135, 41, 17, 'ene_whole_magic_attack'], '敵全体に炎属性の超特大ダメージ': [2078, 140, 44, 17, 'ene_whole_magic_attack'], '敵全体に水属性の超特大ダメージ': [2078, 140, 44, 17, 'ene_whole_magic_attack'], '敵全体に土属性の超特大ダメージ': [2078, 140, 44, 17, 'ene_whole_magic_attack'], '敵全体に風属性の超特大ダメージ': [2078, 140, 44, 17, 'ene_whole_magic_attack'], '敵全体に陽属性の超特大ダメージ': [2078, 140, 44, 17, 'ene_whole_magic_attack'], '敵全体に月属性の超特大ダメージ': [2078, 140, 44, 17, 'ene_whole_magic_attack']}
    recover_skill_type = {"味方単体を小回復" : [42.0, 125, 33, 22, "chr_single_recover"], "味方単体を中回復" : [65.0, 120, 39, 22, "chr_single_recover"], "味方単体を大回復" : [88.0, 135, 46, 22, "chr_single_recover"], "味方単体を特大回復" : [111.0, 140, 51, 22, "chr_single_recover"], "味方全体を小回復" : [24.0, 125, 42, 22, "chr_whole_recover"], "味方全体を中回復" : [48.0, 125, 50, 22, "chr_whole_recover"], "味方全体を大回復" : [72.0, 140, 56, 22, "chr_whole_recover"], "味方全体を特大回復" : [96.0, 145, 61, 22, "chr_whole_recover"]}   # 回復スキル. {説明 : [rate, delay, recast, charge, skill_types]}
    status_change_skill_type = {
                                "味方単体のATKが一定ターン小アップ" : ["ATK", 22.2, 65, 21, 10, "chr_single_status_change"], "味方単体のATKが一定ターン中アップ" : ["ATK", 34.0, 65, 27, 10, "chr_single_status_change"], "味方単体のATKが一定ターン大アップ" : ["ATK", 44.4, 65, 34, 10, "chr_single_status_change"], "味方単体のATKが一定ターン特大アップ" : ["ATK", 68.8, 65, 40, 10, "chr_single_status_change"], 
                                "味方単体のMATが一定ターン小アップ" : ["MAT", 22.2, 65, 21, 10, "chr_single_status_change"], "味方単体のMATが一定ターン中アップ" : ["MAT", 34.0, 65, 27, 10, "chr_single_status_change"], "味方単体のMATが一定ターン大アップ" : ["MAT", 44.4, 65, 34, 10, "chr_single_status_change"], "味方単体のMATが一定ターン特大アップ" : ["MAT", 68.8, 65, 40, 10, "chr_single_status_change"], 
                                "味方単体のDEFが一定ターン小アップ" : ["DEF", 34.0, 65, 21, 10, "chr_single_status_change"], "味方単体のDEFが一定ターン中アップ" : ["DEF", 42.9, 65, 27, 10, "chr_single_status_change"], "味方単体のDEFが一定ターン大アップ" : ["DEF", 51.8, 65, 34, 10, "chr_single_status_change"], "味方単体のDEFが一定ターン特大アップ" : ["DEF", 60.7, 65, 40, 10, "chr_single_status_change"], 
                                "味方単体のMDFが一定ターン小アップ" : ["MDF", 34.0, 65, 21, 10, "chr_single_status_change"], "味方単体のMDFが一定ターン中アップ" : ["MDF", 42.9, 65, 27, 10, "chr_single_status_change"], "味方単体のMDFが一定ターン大アップ" : ["MDF", 51.8, 65, 34, 10, "chr_single_status_change"], "味方単体のMDFが一定ターン特大アップ" : ["MDF", 60.7, 65, 40, 10, "chr_single_status_change"], 
                                "味方単体のSPDが一定ターン小アップ" : ["SPD", 21.1, 65, 21, 10, "chr_single_status_change"], "味方単体のSPDが一定ターン中アップ" : ["SPD", 30.0, 65, 27, 10, "chr_single_status_change"], "味方単体のSPDが一定ターン大アップ" : ["SPD", 42.5, 65, 34, 10, "chr_single_status_change"], "味方単体のSPDが一定ターン特大アップ" : ["SPD", 55.0, 65, 40, 10, "chr_single_status_change"], 
                                "味方単体のLUKが一定ターン小アップ" : ["LUK", 74.0, 65, 21, 10, "chr_single_status_change"], "味方単体のLUKが一定ターン中アップ" : ["LUK", 162.8, 65, 27, 10, "chr_single_status_change"], "味方単体のLUKが一定ターン大アップ" : ["LUK", 296.0, 65, 34, 10, "chr_single_status_change"], "味方単体のLUKが一定ターン特大アップ" : ["LUK", 384.0, 65, 40, 10, "chr_single_status_change"], 
                                "味方単体のATKが一定ターン小ダウン" : ["ATK", -10.0, 65, 21, 10, "chr_single_status_change"], "味方単体のATKが一定ターン中ダウン" : ["ATK", -15.0, 65, 27, 10, "chr_single_status_change"], "味方単体のATKが一定ターン大ダウン" : ["ATK", -20.0, 65, 34, 10, "chr_single_status_change"], "味方単体のATKが一定ターン特大ダウン" : ["ATK", -25.0, 65, 21, 10, "chr_single_status_change"], 
                                "味方単体のMATが一定ターン小ダウン" : ["MAT", -10.0, 65, 21, 10, "chr_single_status_change"], "味方単体のMATが一定ターン中ダウン" : ["MAT", -15.0, 65, 27, 10, "chr_single_status_change"], "味方単体のMATが一定ターン大ダウン" : ["MAT", -20.0, 65, 34, 10, "chr_single_status_change"], "味方単体のMATが一定ターン特大ダウン" : ["MAT", -25.0, 65, 40, "chr_single_status_change"], 
                                "味方単体のDEFが一定ターン小ダウン" : ["DEF", -10.0, 65, 21, 10, "chr_single_status_change"], "味方単体のDEFが一定ターン中ダウン" : ["DEF", -15.0, 65, 27, 10, "chr_single_status_change"], "味方単体のDEFが一定ターン大ダウン" : ["DEF", -20.0, 65, 34, 10, "chr_single_status_change"], "味方単体のDEFが一定ターン特大ダウン" : ["DEF", -25.0, 65, 40, 10, "chr_single_status_change"], 
                                "味方単体のMDFが一定ターン小ダウン" : ["MDF", -10.0, 65, 21, 10, "chr_single_status_change"], "味方単体のMDFが一定ターン中ダウン" : ["MDF", -15.0, 65, 27, 10, "chr_single_status_change"], "味方単体のMDFが一定ターン大ダウン" : ["MDF", -20.0, 65, 34, 10, "chr_single_status_change"], "味方単体のMDFが一定ターン特大ダウン" : ["MDF", -10.0, 65, 40, 10, "chr_single_status_change"], 
                                "味方単体のSPDが一定ターン小ダウン" : ["SPD", -10.0, 65, 21, 10, "chr_single_status_change"], "味方単体のSPDが一定ターン中ダウン" : ["SPD", -15.0, 65, 27, 10, "chr_single_status_change"], "味方単体のSPDが一定ターン大ダウン" : ["SPD", -20.0, 65, 34, 10, "chr_single_status_change"], "味方単体のSPDが一定ターン特大ダウン" : ["SPD", -25.0, 65, 40, 10, "chr_single_status_change"], 
                                "味方単体のLUKが一定ターン小ダウン" : ["LUK", -10.0, 65, 21, 10, "chr_single_status_change"], "味方単体のLUKが一定ターン中ダウン" : ["LUK", -15.0, 65, 27, 10, "chr_single_status_change"], "味方単体のLUKが一定ターン大ダウン" : ["LUK", -20.0, 65, 34, 10, "chr_single_status_change"], "味方単体のLUKが一定ターン特大ダウン" : ["LUK", -25.0, 65, 40, 10, "chr_single_status_change"], 
                                "味方全体のATKが一定ターン小アップ" : ["ATK", 22.2, 75, 23, 10, "chr_whole_status_change"], "味方全体のATKが一定ターン中アップ" : ["ATK", 34.0, 75, 30, 10, "chr_whole_status_change"], "味方全体のATKが一定ターン大アップ" : ["ATK", 44.4, 75, 38, 10, "chr_whole_status_change"], "味方全体のATKが一定ターン特大アップ" : ["ATK", 68.8, 75, 45, 10, "chr_whole_status_change"], 
                                "味方全体のMATが一定ターン小アップ" : ["MAT", 22.2, 75, 23, 10, "chr_whole_status_change"], "味方全体のMATが一定ターン中アップ" : ["MAT", 34.0, 75, 30, 10, "chr_whole_status_change"], "味方全体のMATが一定ターン大アップ" : ["MAT", 44.4, 75, 38, 10, "chr_whole_status_change"], "味方全体のMATが一定ターン特大アップ" : ["ATK", 68.8, 75, 45, 10, "chr_whole_status_change"], 
                                "味方全体のDEFが一定ターン小アップ" : ["DEF", 34.0, 75, 23, 10, "chr_whole_status_change"], "味方全体のDEFが一定ターン中アップ" : ["DEF", 42.9, 75, 30, 10, "chr_whole_status_change"], "味方全体のDEFが一定ターン大アップ" : ["DEF", 51.8, 75, 38, 10, "chr_whole_status_change"], "味方全体のDEFが一定ターン特大アップ" : ["DEF", 60.7, 75, 45, 10, "chr_whole_status_change"], 
                                "味方全体の物理防御が一定ターン小アップ" : ["DEF", 34.0, 75, 23, 10, "chr_whole_status_change"], "味方全体の物理防御が一定ターン中アップ" : ["DEF", 42.9, 75, 30, 10, "chr_whole_status_change"], "味方全体の物理防御が一定ターン大アップ" : ["DEF", 51.8, 75, 38, 10, "chr_whole_status_change"], "味方全体の物理防御が一定ターン特大アップ" : ["DEF", 60.7, 75, 45, 10, "chr_whole_status_change"], 
                                "味方全体のMDFが一定ターン小アップ" : ["MDF", 34.0, 75, 23, 10, "chr_whole_status_change"], "味方全体のMDFが一定ターン中アップ" : ["MDF", 42.9, 75, 30, 10, "chr_whole_status_change"], "味方全体のMDFが一定ターン大アップ" : ["MDF", 51.8, 75, 38, 10, "chr_whole_status_change"], "味方全体のMDFが一定ターン特大アップ" : ["MDF", 60.7, 75, 45, 10, "chr_whole_status_change"], 
                                "味方全体のSPDが一定ターン小アップ" : ["SPD", 21.1, 75, 23, 10, "chr_whole_status_change"], "味方全体のSPDが一定ターン中アップ" : ["SPD", 30.0, 75, 30, 10, "chr_whole_status_change"], "味方全体のSPDが一定ターン大アップ" : ["SPD", 42.5, 75, 38, 10, "chr_whole_status_change"], "味方全体のSPDが一定ターン特大アップ" : ["SPD", 55.0, 75, 45, 10, "chr_whole_status_change"], 
                                "味方全体のLUKが一定ターン小アップ" : ["LUK", 74.0, 75, 23, 10, "chr_whole_status_change"], "味方全体のLUKが一定ターン中アップ" : ["LUK", 162.8, 75, 30, 10, "chr_whole_status_change"], "味方全体のLUKが一定ターン大アップ" : ["LUK", 296.0, 75, 38, 10, "chr_whole_status_change"], "味方全体のLUKが一定ターン特大アップ" : ["LUK", 384.0, 75, 45, 10, "chr_whole_status_change"], 
                                "味方全体のATKが一定ターン小ダウン" : ["ATK", -10.0, 75, 23, 10, "chr_whole_status_change"], "味方全体のATKが一定ターン中ダウン" : ["ATK", -15.0, 75, 30, 10, "chr_whole_status_change"], "味方全体のATKが一定ターン大ダウン" : ["ATK", -20.0, 75, 38, 10, "chr_whole_status_change"], "味方全体のATKが一定ターン特大ダウン" : ["ATK", -25.0, 75, 45, 10, "chr_whole_status_change"], 
                                "味方全体のMATが一定ターン小ダウン" : ["MAT", -10.0, 75, 23, 10, "chr_whole_status_change"], "味方全体のMATが一定ターン中ダウン" : ["MAT", -15.0, 75, 30, 10, "chr_whole_status_change"], "味方全体のMATが一定ターン大ダウン" : ["MAT", -20.0, 75, 38, 10, "chr_whole_status_change"], "味方全体のMATが一定ターン特大ダウン" : ["MAT", -25.0, 75, 45, 10, "chr_whole_status_change"], 
                                "味方全体のDEFが一定ターン小ダウン" : ["DEF", -10.0, 75, 23, 10, "chr_whole_status_change"], "味方全体のDEFが一定ターン中ダウン" : ["DEF", -15.0, 75, 30, 10, "chr_whole_status_change"], "味方全体のDEFが一定ターン大ダウン" : ["DEF", -20.0, 75, 38, 10, "chr_whole_status_change"], "味方全体のDEFが一定ターン特大ダウン" : ["DEF", -25.0, 75, 45, 10, "chr_whole_status_change"], 
                                "味方全体のMDFが一定ターン小ダウン" : ["MDF", -10.0, 75, 23, 10, "chr_whole_status_change"], "味方全体のMDFが一定ターン中ダウン" : ["MDF", -15.0, 75, 30, 10, "chr_whole_status_change"], "味方全体のMDFが一定ターン大ダウン" : ["MDF", -20.0, 75, 38, 10, "chr_whole_status_change"], "味方全体のMDFが一定ターン特大ダウン" : ["MDF", -25.0, 75, 45, 10, "chr_whole_status_change"], 
                                "味方全体のSPDが一定ターン小ダウン" : ["SPD", -10.0, 75, 23, 10, "chr_whole_status_change"], "味方全体のSPDが一定ターン中ダウン" : ["SPD", -15.0, 75, 30, 10, "chr_whole_status_change"], "味方全体のSPDが一定ターン大ダウン" : ["SPD", -20.0, 75, 38, 10, "chr_whole_status_change"], "味方全体のSPDが一定ターン特大ダウン" : ["SPD", -25.0, 75, 45, 10, "chr_whole_status_change"], 
                                "味方全体のLUKが一定ターン小ダウン" : ["LUK", -10.0, 75, 23, 10, "chr_whole_status_change"], "味方全体のLUKが一定ターン中ダウン" : ["LUK", -15.0, 75, 30, 10, "chr_whole_status_change"], "味方全体のLUKが一定ターン大ダウン" : ["LUK", -20.0, 75, 38, 10, "chr_whole_status_change"], "味方全体のLUKが一定ターン特大ダウン" : ["LUK", -25.0, 75, 45, 10, "chr_whole_status_change"], 
                                "敵単体のATKが一定ターン小アップ" : ["ATK", 10.0, 65, 21, 10, "ene_single_status_change"], "敵単体のATKが一定ターン中アップ" : ["ATK", 15.0, 65, 27, 10, "ene_single_status_change"], "敵単体のATKが一定ターン大アップ" : ["ATK", 20.0, 65, 34, 10, "ene_single_status_change"], "敵単体のATKが一定ターン特大アップ" : ["ATK", 25.0, 65, 40, 10, "ene_single_status_change"], 
                                "敵単体のMATが一定ターン小アップ" : ["MAT", 10.0, 65, 21, 10, "ene_single_status_change"], "敵単体のMATが一定ターン中アップ" : ["MAT", 15.0, 65, 27, 10, "ene_single_status_change"], "敵単体のMATが一定ターン大アップ" : ["MAT", 20.0, 65, 34, 10, "ene_single_status_change"], "敵単体のMATが一定ターン特大アップ" : ["MAT", 25.0, 65, 40, 10, "ene_single_status_change"], 
                                "敵単体のDEFが一定ターン小アップ" : ["DEF", 10.0, 65, 21, 10, "ene_single_status_change"], "敵単体のDEFが一定ターン中アップ" : ["DEF", 15.0, 65, 27, 10, "ene_single_status_change"], "敵単体のDEFが一定ターン大アップ" : ["DEF", 20.0, 65, 34, 10, "ene_single_status_change"], "敵単体のDEFが一定ターン特大アップ" : ["DEF", 25.0, 65, 40, 10, "ene_single_status_change"], 
                                "敵単体のMDFが一定ターン小アップ" : ["MDF", 10.0, 65, 21, 10, "ene_single_status_change"], "敵単体のMDFが一定ターン中アップ" : ["MDF", 15.0, 65, 27, 10, "ene_single_status_change"], "敵単体のMDFが一定ターン大アップ" : ["MDF", 20.0, 65, 34, 10, "ene_single_status_change"], "敵単体のMDFが一定ターン特大アップ" : ["MDF", 25.0, 65, 40, 10, "ene_single_status_change"], 
                                "敵単体のSPDが一定ターン小アップ" : ["SPD", 10.0, 65, 21, 10, "ene_single_status_change"], "敵単体のSPDが一定ターン中アップ" : ["SPD", 15.0, 65, 27, 10, "ene_single_status_change"], "敵単体のSPDが一定ターン大アップ" : ["SPD", 20.0, 65, 34, 10, "ene_single_status_change"], "敵単体のSPDが一定ターン特大アップ" : ["SPD", 25.0, 65, 40, 10, "ene_single_status_change"], 
                                "敵単体のLUKが一定ターン小アップ" : ["LUK", 10.0, 65, 21, 10, "ene_single_status_change"], "敵単体のLUKが一定ターン中アップ" : ["LUK", 15.0, 65, 27, 10, "ene_single_status_change"], "敵単体のLUKが一定ターン大アップ" : ["LUK", 20.0, 65, 34, 10, "ene_single_status_change"], "敵単体のLUKが一定ターン特大アップ" : ["LUK", 25.0, 65, 40, 10, "ene_single_status_change"], 
                                "敵単体のATKが一定ターン小ダウン" : ["ATK", -14.8, 65, 21, 10, "ene_single_status_change"], "敵単体のATKが一定ターン中ダウン" : ["ATK", -22.2, 65, 27, 10, "ene_single_status_change"], "敵単体のATKが一定ターン大ダウン" : ["ATK", -29.6, 65, 34, 10, "ene_single_status_change"], "敵単体のATKが一定ターン特大ダウン" : ["ATK", -37.0, 65, 40, 10, "ene_single_status_change"], 
                                "敵単体のMATが一定ターン小ダウン" : ["MAT", -14.8, 65, 21, 10, "ene_single_status_change"], "敵単体のMATが一定ターン中ダウン" : ["MAT", -22.2, 65, 27, 10, "ene_single_status_change"], "敵単体のMATが一定ターン大ダウン" : ["MAT", -29.6, 65, 34, 10, "ene_single_status_change"], "敵単体のMATが一定ターン特大ダウン" : ["MAT", -37.0, 65, 40, 10, "ene_single_status_change"], 
                                "敵単体のDEFが一定ターン小ダウン" : ["DEF", -14.8, 65, 21, 10, "ene_single_status_change"], "敵単体のDEFが一定ターン中ダウン" : ["DEF", -25.2, 65, 27, 10, "ene_single_status_change"], "敵単体のDEFが一定ターン大ダウン" : ["DEF", -29.6, 65, 34, 10, "ene_single_status_change"], "敵単体のDEFが一定ターン特大ダウン" : ["DEF", -37.0, 65, 40, 10, "ene_single_status_change"], 
                                "敵単体のMDFが一定ターン小ダウン" : ["MDF", -14.8, 65, 21, 10, "ene_single_status_change"], "敵単体のMDFが一定ターン中ダウン" : ["MDF", -25.2, 65, 27, 10, "ene_single_status_change"], "敵単体のMDFが一定ターン大ダウン" : ["MDF", -29.6, 65, 34, 10, "ene_single_status_change"], "敵単体のMDFが一定ターン特大ダウン" : ["DEF", -37.0, 65, 40, 10, "ene_single_status_change"], 
                                "敵単体のSPDが一定ターン小ダウン" : ["SPD", -28.5, 65, 21, 10, "ene_single_status_change"], "敵単体のSPDが一定ターン中ダウン" : ["SPD", -41.6, 65, 27, 10, "ene_single_status_change"], "敵単体のSPDが一定ターン大ダウン" : ["SPD", -52.5, 65, 34, 10, "ene_single_status_change"], "敵単体のSPDが一定ターン特大ダウン" : ["SPD", -63.4, 65, 40, 10, "ene_single_status_change"], 
                                "敵単体のLUKが一定ターン小ダウン" : ["LUK", -14.8, 65, 21, 10, "ene_single_status_change"], "敵単体のLUKが一定ターン中ダウン" : ["LUK", -25.2, 65, 27, 10, "ene_single_status_change"], "敵単体のLUKが一定ターン大ダウン" : ["LUK", -29.6, 65, 34, 10, "ene_single_status_change"], "敵単体のLUKが一定ターン特大ダウン" : ["LUK", -37.0, 65, 40, 10, "ene_single_status_change"], 
                                "敵全体のATKが一定ターン小アップ" : ["ATK", 10.0, 75, 23, 10, "ene_whole_status_change"], "敵全体のATKが一定ターン中アップ" : ["ATK", 15.0, 75, 30, 10, "ene_whole_status_change"], "敵全体のATKが一定ターン大アップ" : ["ATK", 20.0, 75, 38, 10, "ene_whole_status_change"], "敵全体のATKが一定ターン特大アップ" : ["ATK", 25.0, 75, 45, 10, "ene_whole_status_change"], 
                                "敵全体のMATが一定ターン小アップ" : ["MAT", 10.0, 75, 23, 10, "ene_whole_status_change"], "敵全体のMATが一定ターン中アップ" : ["MAT", 15.0, 75, 30, 10, "ene_whole_status_change"], "敵全体のMATが一定ターン大アップ" : ["MAT", 20.0, 75, 38, 10, "ene_whole_status_change"], "敵全体のMATが一定ターン特大アップ" : ["MAT", 25.0, 75, 45, 10, "ene_whole_status_change"], 
                                "敵全体のDEFが一定ターン小アップ" : ["DEF", 10.0, 75, 23, 10, "ene_whole_status_change"], "敵全体のDEFが一定ターン中アップ" : ["DEF", 15.0, 75, 30, 10, "ene_whole_status_change"], "敵全体のDEFが一定ターン大アップ" : ["DEF", 20.0, 75, 38, 10, "ene_whole_status_change"], "敵全体のDEFが一定ターン特大アップ" : ["DEF", 25.0, 75, 45, 10, "ene_whole_status_change"], 
                                "敵全体のMDFが一定ターン小アップ" : ["MDF", 10.0, 75, 23, 10, "ene_whole_status_change"], "敵全体のMDFが一定ターン中アップ" : ["MDF", 15.0, 75, 30, 10, "ene_whole_status_change"], "敵全体のMDFが一定ターン大アップ" : ["MDF", 20.0, 75, 38, 10, "ene_whole_status_change"], "敵全体のMDFが一定ターン特大アップ" : ["MDF", 25.0, 75, 45, 10, "ene_whole_status_change"], 
                                "敵全体のSPDが一定ターン小アップ" : ["SPD", 10.0, 75, 23, 10, "ene_whole_status_change"], "敵全体のSPDが一定ターン中アップ" : ["SPD", 15.0, 75, 30, 10, "ene_whole_status_change"], "敵全体のSPDが一定ターン大アップ" : ["SPD", 20.0, 75, 38, 10, "ene_whole_status_change"], "敵全体のSPDが一定ターン特大アップ" : ["SPD", 25.0, 75, 45, 10, "ene_whole_status_change"], 
                                "敵全体のLUKが一定ターン小アップ" : ["LUK", 10.0, 75, 23, 10, "ene_whole_status_change"], "敵全体のLUKが一定ターン中アップ" : ["LUK", 15.0, 75, 30, 10, "ene_whole_status_change"], "敵全体のLUKが一定ターン大アップ" : ["LUK", 20.0, 75, 38, 10, "ene_whole_status_change"], "敵全体のLUKが一定ターン特大アップ" : ["LUK", 25.0, 75, 45, 10, "ene_whole_status_change"], 
                                "敵全体のATKが一定ターン小ダウン" : ["ATK", -14.8, 75, 23, 10, "ene_whole_status_change"], "敵全体のATKが一定ターン中ダウン" : ["ATK", -22.2, 75, 30, 10, "ene_whole_status_change"], "敵全体のATKが一定ターン大ダウン" : ["ATK", -29.6, 75, 38, 10, "ene_whole_status_change"], "敵全体のATKが一定ターン特大ダウン" : ["ATK", -37.0, 75, 45, 10, "ene_whole_status_change"], 
                                "敵全体のMATが一定ターン小ダウン" : ["MAT", -14.8, 75, 23, 10, "ene_whole_status_change"], "敵全体のMATが一定ターン中ダウン" : ["MAT", -22.2, 75, 30, 10, "ene_whole_status_change"], "敵全体のMATが一定ターン大ダウン" : ["MAT", -29.6, 75, 38, 10, "ene_whole_status_change"], "敵全体のMATが一定ターン特大ダウン" : ["MAT", -37.0, 75, 45, 10, "ene_whole_status_change"], 
                                "敵全体のDEFが一定ターン小ダウン" : ["DEF", -14.8, 75, 23, 10, "ene_whole_status_change"], "敵全体のDEFが一定ターン中ダウン" : ["DEF", -25.2, 75, 30, 10, "ene_whole_status_change"], "敵全体のDEFが一定ターン大ダウン" : ["DEF", -29.6, 75, 38, 10, "ene_whole_status_change"], "敵全体のDEFが一定ターン特大ダウン" : ["DEF", -37.0, 75, 45, 10, "ene_whole_status_change"], 
                                "敵全体のMDFが一定ターン小ダウン" : ["MDF", -14.8, 75, 23, 10, "ene_whole_status_change"], "敵全体のMDFが一定ターン中ダウン" : ["MDF", -25.2, 75, 30, 10, "ene_whole_status_change"], "敵全体のMDFが一定ターン大ダウン" : ["MDF", -29.6, 75, 38, 10, "ene_whole_status_change"], "敵全体のMDFが一定ターン特大ダウン" : ["MDF", -37.0, 75, 45, 10, "ene_whole_status_change"], 
                                "敵全体のSPDが一定ターン小ダウン" : ["SPD", -28.5, 75, 23, 10, "ene_whole_status_change"], "敵全体のSPDが一定ターン中ダウン" : ["SPD", -41.6, 75, 30, 10, "ene_whole_status_change"], "敵全体のSPDが一定ターン大ダウン" : ["SPD", -52.5, 75, 38, 10, "ene_whole_status_change"], "敵全体のSPDが一定ターン特大ダウン" : ["SPD", -63.7, 75, 45, 10, "ene_whole_status_change"], 
                                "敵全体のLUKが一定ターン小ダウン" : ["LUK", -14.8, 75, 23, 10, "ene_whole_status_change"], "敵全体のLUKが一定ターン中ダウン" : ["LUK", -25.2, 75, 30, 10, "ene_whole_status_change"], "敵全体のLUKが一定ターン大ダウン" : ["LUK", -29.6, 75, 38, 10, "ene_whole_status_change"], "敵全体のLUKが一定ターン特大ダウン" : ["LUK", -37.0, 75, 45, 10, "ene_whole_status_change"], 
                                "自身のATKが一定ターン小アップ" : ["ATK", 22.2, 65, 21, 10, "self_status_change"], "自身のATKが一定ターン中アップ" : ["ATK", 34.0, 65, 27, 10, "self_status_change"], "自身のATKが一定ターン大アップ" : ["ATK", 44.4, 65, 34, 10, "self_status_change"], "自身のATKが一定ターン特大アップ" : ["ATK", 68.8, 65, 40, 10, "self_status_change"], 
                                "自身のMATが一定ターン小アップ" : ["MAT", 22.2, 65, 21, 10, "self_status_change"], "自身のMATが一定ターン中アップ" : ["MAT", 34.0, 65, 27, 10, "self_status_change"], "自身のMATが一定ターン大アップ" : ["MAT", 44.4, 65, 34, 10, "self_status_change"], "自身のMATが一定ターン特大アップ" : ["MAT", 68.8, 65, 40, 10, "self_status_change"], 
                                "自身のDEFが一定ターン小アップ" : ["DEF", 34.0, 65, 21, 10, "self_status_change"], "自身のDEFが一定ターン中アップ" : ["DEF", 42.9, 65, 27, 10, "self_status_change"], "自身のDEFが一定ターン大アップ" : ["DEF", 51.8, 65, 34, 10, "self_status_change"], "自身のDEFが一定ターン特大アップ" : ["DEF", 60.7, 65, 40, 10, "self_status_change"], 
                                "自身のMDFが一定ターン小アップ" : ["MDF", 34.0, 65, 21, 10, "self_status_change"], "自身のMDFが一定ターン中アップ" : ["MDF", 42.9, 65, 27, 10, "self_status_change"], "自身のMDFが一定ターン大アップ" : ["MDF", 51.8, 65, 34, 10, "self_status_change"], "自身のMDFが一定ターン特大アップ" : ["MDF", 60.7, 65, 40, 10, "self_status_change"], 
                                "自身のSPDが一定ターン小アップ" : ["SPD", 21.1, 65, 21, 10, "self_status_change"], "自身のSPDが一定ターン中アップ" : ["SPD", 30.0, 65, 27, 10, "self_status_change"], "自身のSPDが一定ターン大アップ" : ["SPD", 42.5, 65, 34, 10, "self_status_change"], "自身のSPDが一定ターン特大アップ" : ["SPD", 55.0, 65, 40, 10, "self_status_change"], 
                                "自身のLUKが一定ターン小アップ" : ["LUK", 74.0, 65, 21, 10, "self_status_change"], "自身のLUKが一定ターン中アップ" : ["LUK", 162.8, 65, 27, 10, "self_status_change"], "自身のLUKが一定ターン大アップ" : ["LUK", 296.0, 65, 34, 10, "self_status_change"], "自身のLUKが一定ターン特大アップ" : ["LUK", 384.0, 65, 40, 10, "self_status_change"], 
                                "自身のATKが一定ターン小ダウン" : ["ATK", -10.0, 65, 21, 10, "self_status_change"], "自身のATKが一定ターン中ダウン" : ["ATK", -15.0, 65, 27, 10, "self_status_change"], "自身のATKが一定ターン大ダウン" : ["ATK", -20.0, 65, 34, 10, "self_status_change"], "自身のATKが一定ターン特大ダウン" : ["ATK", -25.0, 65, 40, 10, "self_status_change"], 
                                "自身のMATが一定ターン小ダウン" : ["MAT", -10.0, 65, 21, 10, "self_status_change"], "自身のMATが一定ターン中ダウン" : ["MAT", -15.0, 65, 27, 10, "self_status_change"], "自身のMATが一定ターン大ダウン" : ["MAT", -20.0, 65, 34, 10, "self_status_change"], "自身のMATが一定ターン特大ダウン" : ["MAT", -25.0, 65, 40, 10, "self_status_change"], 
                                "自身のDEFが一定ターン小ダウン" : ["DEF", -10.0, 65, 21, 10, "self_status_change"], "自身のDEFが一定ターン中ダウン" : ["DEF", -15.0, 65, 27, 10, "self_status_change"], "自身のDEFが一定ターン大ダウン" : ["DEF", -20.0, 65, 34, 10, "self_status_change"], "自身のDEFが一定ターン特大ダウン" : ["DEF", -25.0, 65, 40, 10, "self_status_change"], 
                                "自身のMDFが一定ターン小ダウン" : ["MDF", -10.0, 65, 21, 10, "self_status_change"], "自身のMDFが一定ターン中ダウン" : ["MDF", -15.0, 65, 27, 10, "self_status_change"], "自身のMDFが一定ターン大ダウン" : ["MDF", -20.0, 65, 34, 10, "self_status_change"], "自身のMDFが一定ターン特大ダウン" : ["MDF", -25.0, 65, 40, 10, "self_status_change"], 
                                "自身のSPDが一定ターン小ダウン" : ["SPD", -10.0, 65, 21, 10, "self_status_change"], "自身のSPDが一定ターン中ダウン" : ["SPD", -15.0, 65, 27, 10, "self_status_change"], "自身のSPDが一定ターン大ダウン" : ["SPD", -20.0, 65, 34, 10, "self_status_change"], "自身のSPDが一定ターン特大ダウン" : ["SPD", -25.0, 65, 40, 10, "self_status_change"], 
                                "自身のLUKが一定ターン小ダウン" : ["LUK", -10.0, 65, 21, 10, "self_status_change"], "自身のLUKが一定ターン中ダウン" : ["LUK", -15.0, 65, 27, 10, "self_status_change"], "自身のLUKが一定ターン大ダウン" : ["LUK", -20.0, 65, 34, 10, "self_status_change"], "自身のLUKが一定ターン特大ダウン" : ["LUK", -25.0, 65, 40, 10, "self_status_change"]
                                }   # ステータス変化スキル. {説明 : [type, rate, delay, recast, charge, skill_types]}
    status_change_reset_skill_type = {
                                    "味方単体の一定ターンATKアップ効果を解除" : ["1", "ATK", 80, 15, 8, "chr_single_status_reset"], "味方単体の一定ターンMATアップ効果を解除" : ["1", "MAT", 80, 15, 8, "chr_single_status_reset"], "味方単体の一定ターンDEFアップ効果を解除" : ["1", "DEF", 80, 15, 8, "chr_single_status_reset"], "味方単体の一定ターンMDFアップ効果を解除" : ["1", "MDF", 80, 15, 8, "chr_single_status_reset"], "味方単体の一定ターンSPDアップ効果を解除" : ["1", "SPD", 80, 15, 8, "chr_single_status_reset"], "味方単体の一定ターンLUKアップ効果を解除" : ["1", "LUK", 80, 15, 8, "chr_single_status_reset"], "味方単体のすべてのステータスアップをリセット" : ["1", "ALL", 80, 15, 8, "chr_single_status_reset"], 
                                    "味方全体の一定ターンATKアップ効果を解除" : ["1", "ATK", 90, 17, 8, "chr_whole_status_reset"], "味方全体の一定ターンMATアップ効果を解除" : ["1", "MAT", 90, 17, 8, "chr_whole_status_reset"], "味方全体の一定ターンDEFアップ効果を解除" : ["1", "DEF", 90, 17, 8, "chr_whole_status_reset"], "味方全体の一定ターンMDFアップ効果を解除" : ["1", "MDF", 90, 17, 8, "chr_whole_status_reset"], "味方全体の一定ターンSPDアップ効果を解除" : ["1", "SPD", 90, 17, 8, "chr_whole_status_reset"], "味方全体の一定ターンLUKアップ効果を解除" : ["1", "LUK", 90, 17, 8, "chr_whole_status_reset"], "味方全体のすべてのステータスアップをリセット" : ["1", "ALL", 90, 17, 8, "chr_whole_status_reset"], 
                                    "味方単体の一定ターンATKダウン効果を解除" : ["0", "ATK", 80, 15, 8, "chr_single_status_reset"], "味方単体の一定ターンMATダウン効果を解除" : ["0", "MAT", 80, 15, 8, "chr_single_status_reset"], "味方単体の一定ターンDEFダウン効果を解除" : ["0", "DEF", 80, 15, 8, "chr_single_status_reset"], "味方単体の一定ターンMDFダウン効果を解除" : ["0", "MDF", 80, 15, 8, "chr_single_status_reset"], "味方単体の一定ターンSPDダウン効果を解除" : ["0", "SPD", 80, 15, 8, "chr_single_status_reset"], "味方単体の一定ターンLUKダウン効果を解除" : ["0", "LUK", 80, 15, 8, "chr_single_status_reset"], "味方単体のすべてのステータスダウンをリセット" : ["0", "ALL", 80, 15, 8, "chr_single_status_reset"], 
                                    "味方全体の一定ターンATKダウン効果を解除" : ["0", "ATK", 90, 17, 8, "chr_whole_status_reset"], "味方全体の一定ターンMATダウン効果を解除" : ["0", "MAT", 90, 17, 8, "chr_whole_status_reset"], "味方全体の一定ターンDEFダウン効果を解除" : ["0", "DEF", 90, 17, 8, "chr_whole_status_reset"], "味方全体の一定ターンMDFダウン効果を解除" : ["0", "MDF", 90, 17, 8, "chr_whole_status_reset"], "味方全体の一定ターンSPDダウン効果を解除" : ["0", "SPD", 90, 17, 8, "chr_whole_status_reset"], "味方全体の一定ターンLUKダウン効果を解除" : ["0", "LUK", 90, 17, 8, "chr_whole_status_reset"], "味方全体のすべてのステータスダウンをリセット" : ["0", "ALL", 90, 17, 8, "chr_whole_status_reset"],                               
                                    "敵単体の一定ターンATKアップをリセット" : ["1", "ATK", 80, 15, 8, "ene_single_status_reset"], "敵単体の一定ターンMATアップをリセット" : ["1", "MAT", 80, 15, 8, "ene_single_status_reset"], "敵単体の一定ターンDEFアップをリセット" : ["1", "DEF", 80, 15, 8, "ene_single_status_reset"], "敵単体の一定ターンMDFアップをリセット" : ["1", "MDF", 80, 15, 8, "ene_single_status_reset"], "敵単体の一定ターンSPDアップをリセット" : ["1", "SPD", 80, 15, 8, "ene_single_status_reset"], "敵単体の一定ターンLUKアップをリセット" : ["1", "LUK", 80, 15, 8, "ene_single_status_reset"], "敵単体のすべてのステータスアップをリセット" : ["1", "ALL", 80, 15, 8, "ene_single_status_reset"], 
                                    "敵全体の一定ターンATKアップをリセット" : ["1", "ATK", 90, 17, 8, "ene_whole_status_reset"], "敵全体の一定ターンMATアップをリセット" : ["1", "MAT", 90, 17, 8, "ene_whole_status_reset"], "敵全体の一定ターンDEFアップをリセット" : ["1", "DEF", 90, 17, 8, "ene_whole_status_reset"], "敵全体の一定ターンMDFアップをリセット" : ["1", "MDF", 90, 17, 8, "ene_whole_status_reset"], "敵全体の一定ターンSPDアップをリセット" : ["1", "SPD", 90, 17, 8, "ene_whole_status_reset"], "敵全体の一定ターンLUKアップをリセット" : ["1", "LUK", 90, 17, 8, "ene_whole_status_reset"], "敵全体のすべてのステータスアップをリセット" : ["1", "ALL", 90, 17, 8, "ene_whole_status_reset"], 
                                    "自身の一定ターンATKダウン効果を解除" : ["0", "ATK", 80, 15, 8, "self_status_reset"], "自身の一定ターンMATダウン効果を解除" : ["0", "MAT", 80, 15, 8, "self_status_reset"], "自身の一定ターンDEFダウン効果を解除" : ["0", "DEF", 80, 15, 8, "self_status_reset"], "自身の一定ターンMDFダウン効果を解除" : ["0", "MDF", 80, 15, 8, "self_status_reset"], "自身の一定ターンSPDダウン効果を解除" : ["0", "SPD", 80, 15, 8, "self_status_reset"], "自身の一定ターンLUKダウン効果を解除" : ["0", "LUK", 80, 15, 8, "self_status_reset"], "自身のすべてのステータスダウンをリセット" : ["0", "ALL", 80, 15, 8, "self_status_reset"],
                                    "自身の一定ターンATKアップ効果を解除" : ["1", "ATK", 80, 15, 8, "self_status_reset"], "自身の一定ターンMATアップ効果を解除" : ["1", "MAT", 80, 15, 8, "self_status_reset"], "自身の一定ターンDEFアップ効果を解除" : ["1", "DEF", 80, 15, 8, "self_status_reset"], "自身の一定ターンMDFアップ効果を解除" : ["1", "MDF", 80, 15, 8, "self_status_reset"], "自身の一定ターンSPDアップ効果を解除" : ["1", "SPD", 80, 15, 8, "self_status_reset"], "自身の一定ターンLUKアップ効果を解除" : ["1", "LUK", 80, 15, 8, "self_status_reset"], "自身のすべてのステータスアップをリセット" : ["1", "ALL", 80, 15, 8, "self_status_reset"]
                                    }   # ステータス変化リセットスキル. {説明 : [type, types, delay, recast, charge, skill_types]}   # typeはアップ解除(1)か、ダウン解除(0). typesはどのステータスを解除するか
    status_down_invaild_skill_type = {"味方単体の一定ターンステータスダウン効果を一定ターン無効化" : [80, 16, 9, "chr_single_status_invalid"], "味方全体の一定ターンステータスダウン効果を一定ターン無効化" : [90, 19, 9, "chr_single_status_invalid"], "自身の一定ターンステータスダウン効果を一定ターン無効化" : [80, 16, 9, "chr_single_status_invalid"]}   # ステータスダウン無効スキル. {説明 : [delay, recast, charge, skill_types]}
    abnormal_skill_type = {
                        "味方単体に低確率でこんらんを付与" : [30, "混乱", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に中確率でこんらんを付与" : [50, "混乱", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に高確率でこんらんを付与" : [90, "混乱", 90, 19, 10, "chr_single_set_abnormal"], "味方単体にこんらんを付与" : [100, "混乱", 90, 19, 10, "chr_single_set_abnormal"], 
                        "味方単体に低確率でかなしばりを付与" : [30, "金縛り", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に中確率でかなしばりを付与" : [50, "金縛り", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に高確率でかなしばりを付与" : [90, "金縛り", 90, 19, 10, "chr_single_set_abnormal"], "味方単体にかなしばりを付与" : [100, "金縛り", 90, 19, 10, "chr_single_set_abnormal"], 
                        "味方単体に低確率ではらぺこを付与" : [30, "腹ペコ", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に中確率ではらぺこを付与" : [50, "腹ペコ", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に高確率ではらぺこを付与" : [90, "腹ペコ", 90, 19, 10, "chr_single_set_abnormal"], "味方単体にはらぺこを付与" : [100, "腹ペコ", 90, 19, 10, "chr_single_set_abnormal"], 
                        "味方単体に低確率でよわきを付与" : [30, "弱気", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に中確率でよわきを付与" : [50, "弱気", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に高確率でよわきを付与" : [90, "弱気", 90, 19, 10, "chr_single_set_abnormal"], "味方単体によわきを付与" : [100, "弱気", 90, 19, 10, "chr_single_set_abnormal"], 
                        "味方単体に低確率でねむりを付与" : [30, "眠り", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に中確率でねむりを付与" : [50, "眠り", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に高確率でねむりを付与" : [90, "眠り", 90, 19, 10, "chr_single_set_abnormal"], "味方単体にねむりを付与" : [100, "眠り", 90, 19, 10, "chr_single_set_abnormal"], 
                        "味方単体に低確率でふこうを付与" : [30, "不幸", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に中確率でふこうを付与" : [50, "不幸", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に高確率でふこうを付与" : [90, "不幸", 90, 19, 10, "chr_single_set_abnormal"], "味方単体にふこうを付与" : [100, "不幸", 90, 19, 10, "chr_single_set_abnormal"], 
                        "味方単体に低確率でちんもくを付与" : [30, "沈黙", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に中確率でちんもくを付与" : [50, "沈黙", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に高確率でちんもくを付与" : [90, "沈黙", 90, 19, 10, "chr_single_set_abnormal"], "味方単体にちんもくを付与" : [100, "沈黙", 90, 19, 10, "chr_single_set_abnormal"], 
                        "味方単体に低確率でこりつを付与" : [30, "孤立", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に中確率でこりつを付与" : [50, "孤立", 90, 19, 10, "chr_single_set_abnormal"], "味方単体に高確率でこりつを付与" : [90, "孤立", 90, 19, 10, "chr_single_set_abnormal"], "味方単体にこりつを付与" : [100, "孤立", 90, 19, 10, "chr_single_set_abnormal"],  
                        "味方全体に低確率でこんらんを付与" : [30, "混乱", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に中確率でこんらんを付与" : [50, "混乱", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に高確率でこんらんを付与" : [95, "混乱", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体にこんらんを付与" : [100, "混乱", 95, 21, 10, "chr_whole_set_abnormal"], 
                        "味方全体に低確率でかなしばりを付与" : [30, "金縛り", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に中確率でかなしばりを付与" : [50, "金縛り", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に高確率でかなしばりを付与" : [95, "金縛り", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体にかなしばりを付与" : [100, "金縛り", 95, 21, 10, "chr_whole_set_abnormal"], 
                        "味方全体に低確率ではらぺこを付与" : [30, "腹ペコ", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に中確率ではらぺこを付与" : [50, "腹ペコ", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に高確率ではらぺこを付与" : [95, "腹ペコ", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体にはらぺこを付与" : [100, "腹ペコ", 95, 21, 10, "chr_whole_set_abnormal"], 
                        "味方全体に低確率でよわきを付与" : [30, "弱気", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に中確率でよわきを付与" : [50, "弱気", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に高確率でよわきを付与" : [95, "弱気", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体によわきを付与" : [100, "弱気", 95, 21, 10, "chr_whole_set_abnormal"], 
                        "味方全体に低確率でねむりを付与" : [30, "眠り", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に中確率でねむりを付与" : [50, "眠り", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に高確率でねむりを付与" : [95, "眠り", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体にねむりを付与" : [100, "眠り", 95, 21, 10, "chr_whole_set_abnormal"], 
                        "味方全体に低確率でふこうを付与" : [30, "不幸", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に中確率でふこうを付与" : [50, "不幸", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に高確率でふこうを付与" : [95, "不幸", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体にふこうを付与" : [100, "不幸", 95, 21, 10, "chr_whole_set_abnormal"], 
                        "味方全体に低確率でちんもくを付与" : [30, "沈黙", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に中確率でちんもくを付与" : [50, "沈黙", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に高確率でちんもくを付与" : [95, "沈黙", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体にちんもくを付与" : [100, "沈黙", 95, 21, 10, "chr_whole_set_abnormal"], 
                        "味方全体に低確率でこりつを付与" : [30, "孤立", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に中確率でこりつを付与" : [50, "孤立", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体に高確率でこりつを付与" : [95, "孤立", 95, 21, 10, "chr_whole_set_abnormal"], "味方全体にこりつを付与" : [100, "孤立", 95, 21, 10, "chr_whole_set_abnormal"], 
                        "敵単体に低確率でこんらんを付与" : [30, "混乱", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に中確率でこんらんを付与" : [50, "混乱", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に高確率でこんらんを付与" : [90, "混乱", 90, 19, 10, "ene_single_set_abnormal"], "敵単体にこんらんを付与" : [100, "混乱", 90, 19, 10, "ene_single_set_abnormal"], 
                        "敵単体に低確率でかなしばりを付与" : [30, "金縛り", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に中確率でかなしばりを付与" : [50, "金縛り", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に高確率でかなしばりを付与" : [90, "金縛り", 90, 19, 10, "ene_single_set_abnormal"], "敵単体にかなしばりを付与" : [100, "金縛り", 90, 19, 10, "ene_single_set_abnormal"], 
                        "敵単体に低確率ではらぺこを付与" : [30, "腹ペコ", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に中確率ではらぺこを付与" : [50, "腹ペコ", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に高確率ではらぺこを付与" : [90, "腹ペコ", 90, 19, 10, "ene_single_set_abnormal"], "敵単体にはらぺこを付与" : [100, "腹ペコ", 90, 19, 10, "ene_single_set_abnormal"], 
                        "敵単体に低確率でよわきを付与" : [30, "弱気", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に中確率でよわきを付与" : [50, "弱気", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に高確率でよわきを付与" : [90, "弱気", 90, 19, 10, "ene_single_set_abnormal"], "敵単体によわきを付与" : [100, "弱気", 90, 19, 10, "ene_single_set_abnormal"], 
                        "敵単体に低確率でねむりを付与" : [30, "眠り", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に中確率でねむりを付与" : [50, "眠り", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に高確率でねむりを付与" : [90, "眠り", 90, 19, 10, "ene_single_set_abnormal"], "敵単体にねむりを付与" : [100, "眠り", 90, 19, 10, "ene_single_set_abnormal"], 
                        "敵単体に低確率でふこうを付与" : [30, "不幸", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に中確率でふこうを付与" : [50, "不幸", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に高確率でふこうを付与" : [90, "不幸", 90, 19, 10, "ene_single_set_abnormal"], "敵単体にふこうを付与" : [100, "不幸", 90, 19, 10, "ene_single_set_abnormal"], 
                        "敵単体に低確率でちんもくを付与" : [30, "沈黙", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に中確率でちんもくを付与" : [50, "沈黙", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に高確率でちんもくを付与" : [90, "沈黙", 90, 19, 10, "ene_single_set_abnormal"], "敵単体にちんもくを付与" : [100, "沈黙", 90, 19, 10, "ene_single_set_abnormal"], 
                        "敵単体に低確率でこりつを付与" : [30, "孤立", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に中確率でこりつを付与" : [50, "孤立", 90, 19, 10, "ene_single_set_abnormal"], "敵単体に高確率でこりつを付与" : [90, "孤立", 90, 19, 10, "ene_single_set_abnormal"], "敵単体にこりつを付与" : [100, "孤立", 90, 19, 10, "ene_single_set_abnormal"], 
                        "敵全体に低確率でこんらんを付与" : [30, "混乱", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に中確率でこんらんを付与" : [50, "混乱", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に高確率でこんらんを付与" : [95, "混乱", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体にこんらんを付与" : [100, "混乱", 95, 21, 10, "ene_whole_set_abnormal"], 
                        "敵全体に低確率でかなしばりを付与" : [30, "金縛り", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に中確率でかなしばりを付与" : [50, "金縛り", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に高確率でかなしばりを付与" : [95, "金縛り", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体にかなしばりを付与" : [100, "金縛り", 95, 21, 10, "ene_whole_set_abnormal"], 
                        "敵全体に低確率ではらぺこを付与" : [30, "腹ペコ", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に中確率ではらぺこを付与" : [50, "腹ペコ", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に高確率ではらぺこを付与" : [95, "腹ペコ", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体にはらぺこを付与" : [100, "腹ペコ", 95, 21, 10, "ene_whole_set_abnormal"], 
                        "敵全体に低確率でよわきを付与" : [30, "弱気", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に中確率でよわきを付与" : [50, "弱気", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に高確率でよわきを付与" : [95, "弱気", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体によわきを付与" : [100, "弱気", 95, 21, 10, "ene_whole_set_abnormal"], 
                        "敵全体に低確率でねむりを付与" : [30, "眠り", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に中確率でねむりを付与" : [50, "眠り", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に高確率でねむりを付与" : [95, "眠り", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体にねむりを付与" : [100, "眠り", 95, 21, 10, "ene_whole_set_abnormal"], 
                        "敵全体に低確率でふこうを付与" : [30, "不幸", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に中確率でふこうを付与" : [50, "不幸", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に高確率でふこうを付与" : [95, "不幸", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体にふこうを付与" : [100, "不幸", 95, 21, 10, "ene_whole_set_abnormal"], 
                        "敵全体に低確率でちんもくを付与" : [30, "沈黙", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に中確率でちんもくを付与" : [50, "沈黙", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に高確率でちんもくを付与" : [95, "沈黙", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体にちんもくを付与" : [100, "沈黙", 95, 21, 10, "ene_whole_set_abnormal"], 
                        "敵全体に低確率でこりつを付与" : [30, "孤立", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に中確率でこりつを付与" : [50, "孤立", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体に高確率でこりつを付与" : [95, "孤立", 95, 21, 10, "ene_whole_set_abnormal"], "敵全体にこりつを付与" : [100, "孤立", 95, 21, 10, "ene_whole_set_abnormal"], 
                        "自身に低確率でこんらんを付与" : [30, "混乱", 90, 19, 10, "self_set_abnormal"], "自身に中確率でこんらんを付与" : [50, "混乱", 90, 19, 10, "self_set_abnormal"], "自身に高確率でこんらんを付与" : [90, "混乱", 90, 19, 10, "self_set_abnormal"], "自身にこんらんを付与" : [100, "混乱", 90, 19, 10, "self_set_abnormal"], 
                        "自身に低確率でかなしばりを付与" : [30, "金縛り", 90, 19, 10, "self_set_abnormal"], "自身に中確率でかなしばりを付与" : [50, "金縛り", 90, 19, 10, "self_set_abnormal"], "自身に高確率でかなしばりを付与" : [90, "金縛り", 90, 19, 10, "self_set_abnormal"], "自身にかなしばりを付与" : [100, "金縛り", 90, 19, 10, "self_set_abnormal"], 
                        "自身に低確率ではらぺこを付与" : [30, "腹ペコ", 90, 19, 10, "self_set_abnormal"], "自身に中確率ではらぺこを付与" : [50, "腹ペコ", 90, 19, 10, "self_set_abnormal"], "自身に高確率ではらぺこを付与" : [90, "腹ペコ", 90, 19, 10, "self_set_abnormal"], "自身にはらぺこを付与" : [100, "腹ペコ", 90, 19, 10, "self_set_abnormal"], 
                        "自身に低確率でよわきを付与" : [30, "弱気", 90, 19, 10, "self_set_abnormal"], "自身に中確率でよわきを付与" : [50, "弱気", 90, 19, 10, "self_set_abnormal"], "自身に高確率でよわきを付与" : [90, "弱気", 90, 19, 10, "self_set_abnormal"], "自身によわきを付与" : [100, "弱気", 90, 19, 10, "self_set_abnormal"], 
                        "自身に低確率でねむりを付与" : [30, "眠り", 90, 19, 10, "self_set_abnormal"], "自身に中確率でねむりを付与" : [50, "眠り", 90, 19, 10, "self_set_abnormal"], "自身に高確率でねむりを付与" : [90, "眠り", 90, 19, 10, "self_set_abnormal"], "自身にねむりを付与" : [100, "眠り", 90, 19, 10, "self_set_abnormal"], 
                        "自身に低確率でふこうを付与" : [30, "不幸", 90, 19, 10, "self_set_abnormal"], "自身に中確率でふこうを付与" : [50, "不幸", 90, 19, 10, "self_set_abnormal"], "自身に高確率でふこうを付与" : [90, "不幸", 90, 19, 10, "self_set_abnormal"], "自身にふこうを付与" : [100, "不幸", 90, 19, 10, "self_set_abnormal"], 
                        "自身に低確率でちんもくを付与" : [30, "沈黙", 90, 19, 10, "self_set_abnormal"], "自身に中確率でちんもくを付与" : [50, "沈黙", 90, 19, 10, "self_set_abnormal"], "自身に高確率でちんもくを付与" : [90, "沈黙", 90, 19, 10, "self_set_abnormal"], "自身にちんもくを付与" : [100, "沈黙", 90, 19, 10, "self_set_abnormal"], 
                        "自身に低確率でこりつを付与" : [30, "孤立", 90, 19, 10, "self_set_abnormal"], "自身に中確率でこりつを付与" : [50, "孤立", 90, 19, 10, "self_set_abnormal"], "自身に高確率でこりつを付与" : [90, "孤立", 90, 19, 10, "self_set_abnormal"], "自身にこりつを付与" : [100, "孤立", 90, 19, 10, "self_set_abnormal"]
                        }   # 状態異常付与スキル. {説明 : [prob, type, delay, recast, charge, skill_types]}. probは確率. typeは{"confusion" : "混乱", "paralysis" : "金縛り", "poison" : "腹ペコ", "bearish" : "弱気", "sleep" : "眠り", "unhappy" : "不幸", "silence" : "沈黙", "isolation" : "孤立"}
    abnormal_recover_skill_type = {"味方単体のこんらんを解除" : ["混乱", 90, 18, 10, "chr_single_abnormal_reset"], "味方単体のかなしばりを解除" : ["金縛り", 90, 18, 10, "chr_single_abnormal_reset"], "味方単体のはらぺこを解除" : ["腹ペコ", 90, 18, 10, "chr_single_abnormal_reset"], "味方単体のよわきを解除" : ["弱気", 90, 18, 10, "chr_single_abnormal_reset"], "味方単体のねむりを解除" : ["眠り", 90, 18, 10, "chr_single_abnormal_reset"], "味方単体のふこうを解除" : ["不幸", 90, 18, 10, "chr_single_abnormal_reset"], "味方単体のちんもくを解除" : ["沈黙", 90, 18, 10, "chr_single_abnormal_reset"], "味方単体のこりつを解除" : ["孤立", 90, 18, 10, "chr_single_abnormal_reset"], "味方全体のこんらんを解除" : ["混乱", 95, 20, 10, "chr_whole_abnormal_reset"], "味方全体のかなしばりを解除" : ["金縛り", 95, 20, 10, "chr_whole_abnormal_reset"], "味方全体のはらぺこを解除" : ["腹ペコ", 95, 20, 10, "chr_whole_abnormal_reset"], "味方全体のよわきを解除" : ["弱気", 95, 20, 10, "chr_whole_abnormal_reset"], "味方全体のねむりを解除" : ["眠り", 95, 20, 10, "chr_whole_abnormal_reset"], "味方全体のふこうを解除" : ["不幸", 95, 20, 10, "chr_whole_abnormal_reset"], "味方全体のちんもくを解除" : ["沈黙", 95, 20, 10, "chr_whole_abnormal_reset"], "味方全体のこりつを解除" : ["孤立", 95, 20, 10, "chr_whole_abnormal_reset"], "敵単体のこんらんを解除" : ["混乱", 90, 18, 10, "ene_single_abnormal_reset"], "敵単体のかなしばりを解除" : ["金縛り", 90, 18, 10, "ene_single_abnormal_reset"], "敵単体のはらぺこを解除" : ["腹ペコ", 90, 18, 10, "ene_single_abnormal_reset"], "敵単体のよわきを解除" : ["弱気", 90, 18, 10, "ene_single_abnormal_reset"], "敵単体のねむりを解除" : ["眠り", 90, 18, 10, "ene_single_abnormal_reset"], "敵単体のふこうを解除" : ["不幸", 90, 18, 10, "ene_single_abnormal_reset"], "敵単体のちんもくを解除" : ["沈黙", 90, 18, 10, "ene_single_abnormal_reset"], "敵単体のこりつを解除" : ["孤立", 90, 18, 10, "ene_single_abnormal_reset"], "敵全体のこんらんを解除" : ["混乱", 95, 20, 10, "ene_whole_abnormal_reset"], "敵全体のかなしばりを解除" : ["金縛り", 95, 20, 10, "ene_whole_abnormal_reset"], "敵全体のはらぺこを解除" : ["腹ペコ", 95, 20, 10, "ene_whole_abnormal_reset"], "敵全体のよわきを解除" : ["弱気", 95, 20, 10, "ene_whole_abnormal_reset"], "敵全体のねむりを解除" : ["眠り", 95, 20, 10, "ene_whole_abnormal_reset"], "敵全体のふこうを解除" : ["不幸", 95, 20, 10, "ene_whole_abnormal_reset"], "敵全体のちんもくを解除" : ["沈黙", 95, 20, 10, "ene_whole_abnormal_reset"], "敵全体のこりつを解除" : ["孤立", 95, 20, 10, "ene_whole_abnormal_reset"], "味方単体のこんらんを解除" : ["混乱", 90, 18, 10, "self_abnormal_reset"], "味方単体のかなしばりを解除" : ["金縛り", 90, 18, 10, "self_abnormal_reset"], "味方単体のはらぺこを解除" : ["腹ペコ", 90, 18, 10, "self_abnormal_reset"], "味方単体のよわきを解除" : ["弱気", 90, 18, 10, "self_abnormal_reset"], "味方単体のねむりを解除" : ["眠り", 90, 18, 10, "self_abnormal_reset"], "味方単体のふこうを解除" : ["不幸", 90, 18, 10, "self_abnormal_reset"], "味方単体のちんもくを解除" : ["沈黙", 90, 18, 10, "self_abnormal_reset"], "味方単体のこりつを解除" : ["孤立", 90, 18, 10, "self_abnormal_reset"], "味方単体の状態異常を回復" : ["ALL", 90, 18, 10, "chr_single_abnormal_reset"], "味方全体の状態異常を回復" : ["ALL", 90, 18, 10, "chr_whole_abnormal_reset"], "自身の状態異常を回復" : ["ALL", 90, 18, 10, "self_abnormal_reset"]}   # 状態異常回復スキル. {説明 : [types, delay, recast, charge, skill_types]}. typesは["confusion", "paralysis", "poison", "bearish", "sleep", "unhappy", "silence", "isolation"]の内のどれか.
    abnormal_invalid_skill_type = {"味方単体の状態異常を一定ターン無効化" : [80, 17, 8, "chr_single_abnormal_invalid"], "味方全体の状態異常を一定ターン無効化" : [90, 21, 8, "chr_whole_abnormal_invalid"], "自身の状態異常を一定ターン無効化" : [80, 17, 8, "self_abnormal_invalid"]}   # 状態異常無効スキル. {説明 : [delay, recast, charge, skill_types]}
    abnormal_probability_change_skill_type = {
                                            "味方単体の状態異常耐性が一定ターン小アップ" : [10.0, 90, 12, 10, "chr_single_abnormal_probability_change"], "味方単体の状態異常耐性が一定ターン中アップ" : [20.0, 92, 14, 10, "chr_single_abnormal_probability_change"], "味方単体の状態異常耐性が一定ターン大アップ" : [30.0, 94, 16, 10, "chr_single_abnormal_probability_change"], "味方単体の状態異常耐性が一定ターン特大アップ" : [40.0, 96, 18, 10, "chr_single_abnormal_probability_change"], 
                                            "味方単体の状態異常耐性が一定ターン小アップ" : [-10.0, 90, 12, 10, "chr_single_abnormal_probability_change"], "味方単体の状態異常耐性が一定ターン中アップ" : [-20.0, 92, 14, 10, "chr_single_abnormal_probability_change"], "味方単体の状態異常耐性が一定ターン大アップ" : [-30.0, 94, 16, 10, "chr_single_abnormal_probability_change"], "味方単体の状態異常耐性が一定ターン特大アップ" : [-40.0, 96, 18, 10, "chr_single_abnormal_probability_change"], 
                                            "味方全体の状態異常耐性が一定ターン小アップ" : [10.0, 96, 12, 10, "chr_whole_abnormal_probability_change"], "味方全体の状態異常耐性が一定ターン中アップ" : [20.0, 98, 14, 10, "chr_whole_abnormal_probability_change"], "味方全体の状態異常耐性が一定ターン大アップ" : [30.0, 100, 16, 10, "chr_whole_abnormal_probability_change"], "味方全体の状態異常耐性が一定ターン特大アップ" : [40.0, 102, 18, 10, "chr_whole_abnormal_probability_change"], 
                                            "味方全体の状態異常耐性が一定ターン小アップ" : [-10.0, 96, 12, 10, "chr_whole_abnormal_probability_change"], "味方全体の状態異常耐性が一定ターン中アップ" : [-20.0, 98, 14, 10, "chr_whole_abnormal_probability_change"], "味方全体の状態異常耐性が一定ターン大アップ" : [-30.0, 100, 16, 10, "chr_whole_abnormal_probability_change"], "味方全体の状態異常耐性が一定ターン特大アップ" : [-40.0, 102, 18, 10, "chr_whole_abnormal_probability_change"], 
                                            "敵単体の状態異常耐性が一定ターン小アップ" : [10.0, 90, 12, 10, "ene_single_abnormal_probability_change"], "敵単体の状態異常耐性が一定ターン中アップ" : [20.0, 92, 14, 10, "ene_single_abnormal_probability_change"], "敵単体の状態異常耐性が一定ターン大アップ" : [30.0, 94, 16, 10, "ene_single_abnormal_probability_change"], "敵単体の状態異常耐性が一定ターン特大アップ" : [40.0, 96, 18, 10, "ene_single_abnormal_probability_change"], 
                                            "敵単体の状態異常耐性が一定ターン小アップ" : [-10.0, 90, 12, 10, "ene_single_abnormal_probability_change"], "敵単体の状態異常耐性が一定ターン中アップ" : [-20.0, 92, 14, 10, "ene_single_abnormal_probability_change"], "敵単体の状態異常耐性が一定ターン大アップ" : [-30.0, 94, 16, 10, "ene_single_abnormal_probability_change"], "敵単体の状態異常耐性が一定ターン特大アップ" : [-40.0, 96, 18, 10, "ene_single_abnormal_probability_change"], 
                                            "敵全体の状態異常耐性が一定ターン小アップ" : [10.0, 96, 12, 10, "ene_whole_abnormal_probability_change"], "敵全体の状態異常耐性が一定ターン中アップ" : [20.0, 98, 14, 10, "ene_whole_abnormal_probability_change"], "敵全体の状態異常耐性が一定ターン大アップ" : [30.0, 100, 16, 10, "ene_whole_abnormal_probability_change"], "敵全体の状態異常耐性が一定ターン特大アップ" : [40.0, 102, 18, 10, "ene_whole_abnormal_probability_change"], 
                                            "敵全体の状態異常耐性が一定ターン小アップ" : [-10.0, 96, 12, 10, "ene_whole_abnormal_probability_change"], "敵全体の状態異常耐性が一定ターン中アップ" : [-20.0, 98, 14, 10, "ene_whole_abnormal_probability_change"], "敵全体の状態異常耐性が一定ターン大アップ" : [-30.0, 100, 16, 10, "ene_whole_abnormal_probability_change"], "敵全体の状態異常耐性が一定ターン特大アップ" : [-40.0, 102, 18, 10, "ene_whole_abnormal_probability_change"], 
                                            "自身の状態異常耐性が一定ターン小アップ" : [10.0, 90, 12, 10, "self_abnormal_probability_change"], "自身の状態異常耐性が一定ターン中アップ" : [20.0, 92, 14, 10, "self_abnormal_probability_change"], "自身の状態異常耐性が一定ターン大アップ" : [30.0, 94, 16, 10, "self_abnormal_probability_change"], "自身の状態異常耐性が一定ターン特大アップ" : [40.0, 96, 18, 10, "self_abnormal_probability_change"], 
                                            "自身の状態異常耐性が一定ターン小アップ" : [-10.0, 90, 12, 10, "self_abnormal_probability_change"], "自身の状態異常耐性が一定ターン中アップ" : [-20.0, 92, 14, 10, "self_abnormal_probability_change"], "自身の状態異常耐性が一定ターン大アップ" : [-30.0, 94, 16, 10, "self_abnormal_probability_change"], "自身の状態異常耐性が一定ターン特大アップ" : [-40.0, 96, 18, 10, "self_abnormal_probability_change"]
                                            }   # 状態異常付与確率補正変化スキル. {説明 : [rate, delay, recast, charge, skill_types]}
    element_resistance_change_skill_type = {
                                            "味方単体の炎属性耐性が一定ターン小アップ" : [0, 14.8, 65, 21, 10, "chr_single_element_resistance_change"], "味方単体の炎属性耐性が一定ターン中アップ" : [0, 29.6, 65, 27, 10, "chr_single_element_resistance_change"], "味方単体の炎属性耐性が一定ターン大アップ" : [0, 44.4, 65, 34, 10, "chr_single_element_resistance_change"], "味方単体の炎属性耐性が一定ターン特大アップ" : [0, 59.2, 65, 40, 10, "chr_single_element_resistance_change"], 
                                            "味方単体の水属性耐性が一定ターン小アップ" : [1, 14.8, 65, 21, 10, "chr_single_element_resistance_change"], "味方単体の水属性耐性が一定ターン中アップ" : [1, 29.6, 65, 27, 10, "chr_single_element_resistance_change"], "味方単体の水属性耐性が一定ターン大アップ" : [1, 44.4, 65, 34, 10, "chr_single_element_resistance_change"], "味方単体の水属性耐性が一定ターン特大アップ" : [1, 59.2, 65, 40, 10, "chr_single_element_resistance_change"], 
                                            "味方単体の土属性耐性が一定ターン小アップ" : [2, 14.8, 65, 21, 10, "chr_single_element_resistance_change"], "味方単体の土属性耐性が一定ターン中アップ" : [2, 29.6, 65, 27, 10, "chr_single_element_resistance_change"], "味方単体の土属性耐性が一定ターン大アップ" : [2, 44.4, 65, 34, 10, "chr_single_element_resistance_change"], "味方単体の土属性耐性が一定ターン特大アップ" : [2, 59.2, 65, 40, 10, "chr_single_element_resistance_change"], 
                                            "味方単体の風属性耐性が一定ターン小アップ" : [3, 14.8, 65, 21, 10, "chr_single_element_resistance_change"], "味方単体の風属性耐性が一定ターン中アップ" : [3, 29.6, 65, 27, 10, "chr_single_element_resistance_change"], "味方単体の風属性耐性が一定ターン大アップ" : [3, 44.4, 65, 34, 10, "chr_single_element_resistance_change"], "味方単体の風属性耐性が一定ターン特大アップ" : [3, 59.2, 65, 40, 10, "chr_single_element_resistance_change"], 
                                            "味方単体の月属性耐性が一定ターン小アップ" : [4, 14.8, 65, 21, 10, "chr_single_element_resistance_change"], "味方単体の月属性耐性が一定ターン中アップ" : [4, 29.6, 65, 27, 10, "chr_single_element_resistance_change"], "味方単体の月属性耐性が一定ターン大アップ" : [4, 44.4, 65, 34, 10, "chr_single_element_resistance_change"], "味方単体の月属性耐性が一定ターン特大アップ" : [4, 59.2, 65, 40, 10, "chr_single_element_resistance_change"], 
                                            "味方単体の陽属性耐性が一定ターン小アップ" : [5, 14.8, 65, 21, 10, "chr_single_element_resistance_change"], "味方単体の陽属性耐性が一定ターン中アップ" : [5, 29.6, 65, 27, 10, "chr_single_element_resistance_change"], "味方単体の陽属性耐性が一定ターン大アップ" : [5, 44.4, 65, 34, 10, "chr_single_element_resistance_change"], "味方単体の陽属性耐性が一定ターン特大アップ" : [5, 59.2, 65, 40, 10, "chr_single_element_resistance_change"], 
                                            "味方単体の炎属性耐性が一定ターン小ダウン" : [0, -14.8, 65, 21, 10, "chr_single_element_resistance_change"], "味方単体の炎属性耐性が一定ターン中ダウン" : [0, -29.6, 65, 27, 10, "chr_single_element_resistance_change"], "味方単体の炎属性耐性が一定ターン大ダウン" : [0, -44.4, 65, 34, 10, "chr_single_element_resistance_change"], "味方単体の炎属性耐性が一定ターン特大ダウン" : [0, -59.2, 65, 40, 10, "chr_single_element_resistance_change"], 
                                            "味方単体の水属性耐性が一定ターン小ダウン" : [1, -14.8, 65, 21, 10, "chr_single_element_resistance_change"], "味方単体の水属性耐性が一定ターン中ダウン" : [1, -29.6, 65, 27, 10, "chr_single_element_resistance_change"], "味方単体の水属性耐性が一定ターン大ダウン" : [1, -44.4, 65, 34, 10, "chr_single_element_resistance_change"], "味方単体の水属性耐性が一定ターン特大ダウン" : [1, -59.2, 65, 40, 10, "chr_single_element_resistance_change"], 
                                            "味方単体の土属性耐性が一定ターン小ダウン" : [2, -14.8, 65, 21, 10, "chr_single_element_resistance_change"], "味方単体の土属性耐性が一定ターン中ダウン" : [2, -29.6, 65, 27, 10, "chr_single_element_resistance_change"], "味方単体の土属性耐性が一定ターン大ダウン" : [2, -44.4, 65, 34, 10, "chr_single_element_resistance_change"], "味方単体の土属性耐性が一定ターン特大ダウン" : [2, -59.2, 65, 40, 10, "chr_single_element_resistance_change"], 
                                            "味方単体の風属性耐性が一定ターン小ダウン" : [3, -14.8, 65, 21, 10, "chr_single_element_resistance_change"], "味方単体の風属性耐性が一定ターン中ダウン" : [3, -29.6, 65, 27, 10, "chr_single_element_resistance_change"], "味方単体の風属性耐性が一定ターン大ダウン" : [3, -44.4, 65, 34, 10, "chr_single_element_resistance_change"], "味方単体の風属性耐性が一定ターン特大ダウン" : [3, -59.2, 65, 40, 10, "chr_single_element_resistance_change"], 
                                            "味方単体の月属性耐性が一定ターン小ダウン" : [4, -14.8, 65, 21, 10, "chr_single_element_resistance_change"], "味方単体の月属性耐性が一定ターン中ダウン" : [4, -29.6, 65, 27, 10, "chr_single_element_resistance_change"], "味方単体の月属性耐性が一定ターン大ダウン" : [4, -44.4, 65, 34, 10, "chr_single_element_resistance_change"], "味方単体の月属性耐性が一定ターン特大ダウン" : [4, -59.2, 65, 40, 10, "chr_single_element_resistance_change"], 
                                            "味方単体の陽属性耐性が一定ターン小ダウン" : [5, -14.8, 65, 21, 10, "chr_single_element_resistance_change"], "味方単体の陽属性耐性が一定ターン中ダウン" : [5, -29.6, 65, 27, 10, "chr_single_element_resistance_change"], "味方単体の陽属性耐性が一定ターン大ダウン" : [5, -44.4, 65, 34, 10, "chr_single_element_resistance_change"], "味方単体の陽属性耐性が一定ターン特大ダウン" : [5, -59.2, 65, 40, 10, "chr_single_element_resistance_change"], 
                                            "味方全体の炎属性耐性が一定ターン小アップ" : [0, 14.8, 75, 23, 10, "chr_whole_element_resistance_change"], "味方全体の炎属性耐性が一定ターン中アップ" : [0, 29.6, 75, 29, 10, "chr_whole_element_resistance_change"], "味方全体の炎属性耐性が一定ターン大アップ" : [0, 44.4, 75, 36, 10, "chr_whole_element_resistance_change"], "味方全体の炎属性耐性が一定ターン特大アップ" : [0, 59.2, 75, 42, 10, "chr_whole_element_resistance_change"], 
                                            "味方全体の水属性耐性が一定ターン小アップ" : [1, 14.8, 75, 23, 10, "chr_whole_element_resistance_change"], "味方全体の水属性耐性が一定ターン中アップ" : [1, 29.6, 75, 29, 10, "chr_whole_element_resistance_change"], "味方全体の水属性耐性が一定ターン大アップ" : [1, 44.4, 75, 36, 10, "chr_whole_element_resistance_change"], "味方全体の水属性耐性が一定ターン特大アップ" : [1, 59.2, 75, 42, 10, "chr_whole_element_resistance_change"], 
                                            "味方全体の土属性耐性が一定ターン小アップ" : [2, 14.8, 75, 23, 10, "chr_whole_element_resistance_change"], "味方全体の土属性耐性が一定ターン中アップ" : [2, 29.6, 75, 29, 10, "chr_whole_element_resistance_change"], "味方全体の土属性耐性が一定ターン大アップ" : [2, 44.4, 75, 36, 10, "chr_whole_element_resistance_change"], "味方全体の土属性耐性が一定ターン特大アップ" : [2, 59.2, 75, 42, 10, "chr_whole_element_resistance_change"], 
                                            "味方全体の風属性耐性が一定ターン小アップ" : [3, 14.8, 75, 23, 10, "chr_whole_element_resistance_change"], "味方全体の風属性耐性が一定ターン中アップ" : [3, 29.6, 75, 29, 10, "chr_whole_element_resistance_change"], "味方全体の風属性耐性が一定ターン大アップ" : [3, 44.4, 75, 36, 10, "chr_whole_element_resistance_change"], "味方全体の風属性耐性が一定ターン特大アップ" : [3, 59.2, 75, 42, 10, "chr_whole_element_resistance_change"], 
                                            "味方全体の月属性耐性が一定ターン小アップ" : [4, 14.8, 75, 23, 10, "chr_whole_element_resistance_change"], "味方全体の月属性耐性が一定ターン中アップ" : [4, 29.6, 75, 29, 10, "chr_whole_element_resistance_change"], "味方全体の月属性耐性が一定ターン大アップ" : [4, 44.4, 75, 36, 10, "chr_whole_element_resistance_change"], "味方全体の月属性耐性が一定ターン特大アップ" : [4, 59.2, 75, 42, 10, "chr_whole_element_resistance_change"], 
                                            "味方全体の陽属性耐性が一定ターン小アップ" : [5, 14.8, 75, 23, 10, "chr_whole_element_resistance_change"], "味方全体の陽属性耐性が一定ターン中アップ" : [5, 29.6, 75, 29, 10, "chr_whole_element_resistance_change"], "味方全体の陽属性耐性が一定ターン大アップ" : [5, 44.4, 75, 36, 10, "chr_whole_element_resistance_change"], "味方全体の陽属性耐性が一定ターン特大アップ" : [5, 59.2, 75, 42, 10, "chr_whole_element_resistance_change"], 
                                            "味方全体の炎属性耐性が一定ターン小ダウン" : [0, -14.8, 75, 23, 10, "chr_whole_element_resistance_change"], "味方全体の炎属性耐性が一定ターン中ダウン" : [0, -29.6, 75, 29, 10, "chr_whole_element_resistance_change"], "味方全体の炎属性耐性が一定ターン大ダウン" : [0, -44.4, 75, 36, 10, "chr_whole_element_resistance_change"], "味方全体の炎属性耐性が一定ターン特大ダウン" : [0, -59.2, 75, 42, 10, "chr_whole_element_resistance_change"], 
                                            "味方全体の水属性耐性が一定ターン小ダウン" : [1, -14.8, 75, 23, 10, "chr_whole_element_resistance_change"], "味方全体の水属性耐性が一定ターン中ダウン" : [1, -29.6, 75, 29, 10, "chr_whole_element_resistance_change"], "味方全体の水属性耐性が一定ターン大ダウン" : [1, -44.4, 75, 36, 10, "chr_whole_element_resistance_change"], "味方全体の水属性耐性が一定ターン特大ダウン" : [1, -59.2, 75, 42, 10, "chr_whole_element_resistance_change"], 
                                            "味方全体の土属性耐性が一定ターン小ダウン" : [2, -14.8, 75, 23, 10, "chr_whole_element_resistance_change"], "味方全体の土属性耐性が一定ターン中ダウン" : [2, -29.6, 75, 29, 10, "chr_whole_element_resistance_change"], "味方全体の土属性耐性が一定ターン大ダウン" : [2, -44.4, 75, 36, 10, "chr_whole_element_resistance_change"], "味方全体の土属性耐性が一定ターン特大ダウン" : [2, -59.2, 75, 42, 10, "chr_whole_element_resistance_change"], 
                                            "味方全体の風属性耐性が一定ターン小ダウン" : [3, -14.8, 75, 23, 10, "chr_whole_element_resistance_change"], "味方全体の風属性耐性が一定ターン中ダウン" : [3, -29.6, 75, 29, 10, "chr_whole_element_resistance_change"], "味方全体の風属性耐性が一定ターン大ダウン" : [3, -44.4, 75, 36, 10, "chr_whole_element_resistance_change"], "味方全体の風属性耐性が一定ターン特大ダウン" : [3, -59.2, 75, 42, 10, "chr_whole_element_resistance_change"], 
                                            "味方全体の月属性耐性が一定ターン小ダウン" : [4, -14.8, 75, 23, 10, "chr_whole_element_resistance_change"], "味方全体の月属性耐性が一定ターン中ダウン" : [4, -29.6, 75, 29, 10, "chr_whole_element_resistance_change"], "味方全体の月属性耐性が一定ターン大ダウン" : [4, -44.4, 75, 36, 10, "chr_whole_element_resistance_change"], "味方全体の月属性耐性が一定ターン特大ダウン" : [4, -59.2, 75, 42, 10, "chr_whole_element_resistance_change"], 
                                            "味方全体の陽属性耐性が一定ターン小ダウン" : [5, -14.8, 75, 23, 10, "chr_whole_element_resistance_change"], "味方全体の陽属性耐性が一定ターン中ダウン" : [5, -29.6, 75, 29, 10, "chr_whole_element_resistance_change"], "味方全体の陽属性耐性が一定ターン大ダウン" : [5, -44.4, 75, 36, 10, "chr_whole_element_resistance_change"], "味方全体の陽属性耐性が一定ターン特大ダウン" : [5, -59.2, 75, 42, 10, "chr_whole_element_resistance_change"], 
                                            "敵単体の炎属性耐性が一定ターン小アップ" : [0, 14.8, 65, 21, 10, "ene_single_element_resistance_change"], "敵単体の炎属性耐性が一定ターン中アップ" : [0, 29.6, 65, 27, 10, "ene_single_element_resistance_change"], "敵単体の炎属性耐性が一定ターン大アップ" : [0, 44.4, 65, 34, 10, "ene_single_element_resistance_change"], "敵単体の炎属性耐性が一定ターン特大アップ" : [0, 59.2, 65, 40, 10, "ene_single_element_resistance_change"], 
                                            "敵単体の水属性耐性が一定ターン小アップ" : [1, 14.8, 65, 21, 10, "ene_single_element_resistance_change"], "敵単体の水属性耐性が一定ターン中アップ" : [1, 29.6, 65, 27, 10, "ene_single_element_resistance_change"], "敵単体の水属性耐性が一定ターン大アップ" : [1, 44.4, 65, 34, 10, "ene_single_element_resistance_change"], "敵単体の水属性耐性が一定ターン特大アップ" : [1, 59.2, 65, 40, 10, "ene_single_element_resistance_change"], 
                                            "敵単体の土属性耐性が一定ターン小アップ" : [2, 14.8, 65, 21, 10, "ene_single_element_resistance_change"], "敵単体の土属性耐性が一定ターン中アップ" : [2, 29.6, 65, 27, 10, "ene_single_element_resistance_change"], "敵単体の土属性耐性が一定ターン大アップ" : [2, 44.4, 65, 34, 10, "ene_single_element_resistance_change"], "敵単体の土属性耐性が一定ターン特大アップ" : [2, 59.2, 65, 40, 10, "ene_single_element_resistance_change"], 
                                            "敵単体の風属性耐性が一定ターン小アップ" : [3, 14.8, 65, 21, 10, "ene_single_element_resistance_change"], "敵単体の風属性耐性が一定ターン中アップ" : [3, 29.6, 65, 27, 10, "ene_single_element_resistance_change"], "敵単体の風属性耐性が一定ターン大アップ" : [3, 44.4, 65, 34, 10, "ene_single_element_resistance_change"], "敵単体の風属性耐性が一定ターン特大アップ" : [3, 59.2, 65, 40, 10, "ene_single_element_resistance_change"], 
                                            "敵単体の月属性耐性が一定ターン小アップ" : [4, 14.8, 65, 21, 10, "ene_single_element_resistance_change"], "敵単体の月属性耐性が一定ターン中アップ" : [4, 29.6, 65, 27, 10, "ene_single_element_resistance_change"], "敵単体の月属性耐性が一定ターン大アップ" : [4, 44.4, 65, 34, 10, "ene_single_element_resistance_change"], "敵単体の月属性耐性が一定ターン特大アップ" : [4, 59.2, 65, 40, 10, "ene_single_element_resistance_change"], 
                                            "敵単体の陽属性耐性が一定ターン小アップ" : [5, 14.8, 65, 21, 10, "ene_single_element_resistance_change"], "敵単体の陽属性耐性が一定ターン中アップ" : [5, 29.6, 65, 27, 10, "ene_single_element_resistance_change"], "敵単体の陽属性耐性が一定ターン大アップ" : [5, 44.4, 65, 34, 10, "ene_single_element_resistance_change"], "敵単体の陽属性耐性が一定ターン特大アップ" : [5, 59.2, 65, 40, 10, "ene_single_element_resistance_change"], 
                                            "敵単体の炎属性耐性が一定ターン小ダウン" : [0, -14.8, 65, 21, 10, "ene_single_element_resistance_change"], "敵単体の炎属性耐性が一定ターン中ダウン" : [0, -29.6, 65, 27, 10, "ene_single_element_resistance_change"], "敵単体の炎属性耐性が一定ターン大ダウン" : [0, -44.4, 65, 34, 10, "ene_single_element_resistance_change"], "敵単体の炎属性耐性が一定ターン特大ダウン" : [0, -59.2, 65, 40, 10, "ene_single_element_resistance_change"], 
                                            "敵単体の水属性耐性が一定ターン小ダウン" : [1, -14.8, 65, 21, 10, "ene_single_element_resistance_change"], "敵単体の水属性耐性が一定ターン中ダウン" : [1, -29.6, 65, 27, 10, "ene_single_element_resistance_change"], "敵単体の水属性耐性が一定ターン大ダウン" : [1, -44.4, 65, 34, 10, "ene_single_element_resistance_change"], "敵単体の水属性耐性が一定ターン特大ダウン" : [1, -59.2, 65, 40, 10, "ene_single_element_resistance_change"], 
                                            "敵単体の土属性耐性が一定ターン小ダウン" : [2, -14.8, 65, 21, 10, "ene_single_element_resistance_change"], "敵単体の土属性耐性が一定ターン中ダウン" : [2, -29.6, 65, 27, 10, "ene_single_element_resistance_change"], "敵単体の土属性耐性が一定ターン大ダウン" : [2, -44.4, 65, 34, 10, "ene_single_element_resistance_change"], "敵単体の土属性耐性が一定ターン特大ダウン" : [2, -59.2, 65, 40, 10, "ene_single_element_resistance_change"], 
                                            "敵単体の風属性耐性が一定ターン小ダウン" : [3, -14.8, 65, 21, 10, "ene_single_element_resistance_change"], "敵単体の風属性耐性が一定ターン中ダウン" : [3, -29.6, 65, 27, 10, "ene_single_element_resistance_change"], "敵単体の風属性耐性が一定ターン大ダウン" : [3, -44.4, 65, 34, 10, "ene_single_element_resistance_change"], "敵単体の風属性耐性が一定ターン特大ダウン" : [3, -59.2, 65, 40, 10, "ene_single_element_resistance_change"], 
                                            "敵単体の月属性耐性が一定ターン小ダウン" : [4, -14.8, 65, 21, 10, "ene_single_element_resistance_change"], "敵単体の月属性耐性が一定ターン中ダウン" : [4, -29.6, 65, 27, 10, "ene_single_element_resistance_change"], "敵単体の月属性耐性が一定ターン大ダウン" : [4, -44.4, 65, 34, 10, "ene_single_element_resistance_change"], "敵単体の月属性耐性が一定ターン特大ダウン" : [4, -59.2, 65, 40, 10, "ene_single_element_resistance_change"], 
                                            "敵単体の陽属性耐性が一定ターン小ダウン" : [5, -14.8, 65, 21, 10, "ene_single_element_resistance_change"], "敵単体の陽属性耐性が一定ターン中ダウン" : [5, -29.6, 65, 27, 10, "ene_single_element_resistance_change"], "敵単体の陽属性耐性が一定ターン大ダウン" : [5, -44.4, 65, 34, 10, "ene_single_element_resistance_change"], "敵単体の陽属性耐性が一定ターン特大ダウン" : [5, -59.2, 65, 40, 10, "ene_single_element_resistance_change"], 
                                            "敵全体の炎属性耐性が一定ターン小アップ" : [0, 14.8, 75, 23, 10, "ene_whole_element_resistance_change"], "敵全体の炎属性耐性が一定ターン中アップ" : [0, 29.6, 75, 29, 10, "ene_whole_element_resistance_change"], "敵全体の炎属性耐性が一定ターン大アップ" : [0, 44.4, 75, 36, 10, "ene_whole_element_resistance_change"], "敵全体の炎属性耐性が一定ターン特大アップ" : [0, 59.2, 75, 42, 10, "ene_whole_element_resistance_change"], 
                                            "敵全体の水属性耐性が一定ターン小アップ" : [1, 14.8, 75, 23, 10, "ene_whole_element_resistance_change"], "敵全体の水属性耐性が一定ターン中アップ" : [1, 29.6, 75, 29, 10, "ene_whole_element_resistance_change"], "敵全体の水属性耐性が一定ターン大アップ" : [1, 44.4, 75, 36, 10, "ene_whole_element_resistance_change"], "敵全体の水属性耐性が一定ターン特大アップ" : [1, 59.2, 75, 42, 10, "ene_whole_element_resistance_change"], 
                                            "敵全体の土属性耐性が一定ターン小アップ" : [2, 14.8, 75, 23, 10, "ene_whole_element_resistance_change"], "敵全体の土属性耐性が一定ターン中アップ" : [2, 29.6, 75, 29, 10, "ene_whole_element_resistance_change"], "敵全体の土属性耐性が一定ターン大アップ" : [2, 44.4, 75, 36, 10, "ene_whole_element_resistance_change"], "敵全体の土属性耐性が一定ターン特大アップ" : [2, 59.2, 75, 42, 10, "ene_whole_element_resistance_change"], 
                                            "敵全体の風属性耐性が一定ターン小アップ" : [3, 14.8, 75, 23, 10, "ene_whole_element_resistance_change"], "敵全体の風属性耐性が一定ターン中アップ" : [3, 29.6, 75, 29, 10, "ene_whole_element_resistance_change"], "敵全体の風属性耐性が一定ターン大アップ" : [3, 44.4, 75, 36, 10, "ene_whole_element_resistance_change"], "敵全体の風属性耐性が一定ターン特大アップ" : [3, 59.2, 75, 42, 10, "ene_whole_element_resistance_change"], 
                                            "敵全体の月属性耐性が一定ターン小アップ" : [4, 14.8, 75, 23, 10, "ene_whole_element_resistance_change"], "敵全体の月属性耐性が一定ターン中アップ" : [4, 29.6, 75, 29, 10, "ene_whole_element_resistance_change"], "敵全体の月属性耐性が一定ターン大アップ" : [4, 44.4, 75, 36, 10, "ene_whole_element_resistance_change"], "敵全体の月属性耐性が一定ターン特大アップ" : [4, 59.2, 75, 42, 10, "ene_whole_element_resistance_change"], 
                                            "敵全体の陽属性耐性が一定ターン小アップ" : [5, 14.8, 75, 23, 10, "ene_whole_element_resistance_change"], "敵全体の陽属性耐性が一定ターン中アップ" : [5, 29.6, 75, 29, 10, "ene_whole_element_resistance_change"], "敵全体の陽属性耐性が一定ターン大アップ" : [5, 44.4, 75, 36, 10, "ene_whole_element_resistance_change"], "敵全体の陽属性耐性が一定ターン特大アップ" : [5, 59.2, 75, 42, 10, "ene_whole_element_resistance_change"], 
                                            "敵全体の炎属性耐性が一定ターン小ダウン" : [0, -14.8, 75, 23, 10, "ene_whole_element_resistance_change"], "敵全体の炎属性耐性が一定ターン中ダウン" : [0, -29.6, 75, 29, 10, "ene_whole_element_resistance_change"], "敵全体の炎属性耐性が一定ターン大ダウン" : [0, -44.4, 75, 36, 10, "ene_whole_element_resistance_change"], "敵全体の炎属性耐性が一定ターン特大ダウン" : [0, -59.2, 75, 42, 10, "ene_whole_element_resistance_change"], 
                                            "敵全体の水属性耐性が一定ターン小ダウン" : [1, -14.8, 75, 23, 10, "ene_whole_element_resistance_change"], "敵全体の水属性耐性が一定ターン中ダウン" : [1, -29.6, 75, 29, 10, "ene_whole_element_resistance_change"], "敵全体の水属性耐性が一定ターン大ダウン" : [1, -44.4, 75, 36, 10, "ene_whole_element_resistance_change"], "敵全体の水属性耐性が一定ターン特大ダウン" : [1, -59.2, 75, 42, 10, "ene_whole_element_resistance_change"], 
                                            "敵全体の土属性耐性が一定ターン小ダウン" : [2, -14.8, 75, 23, 10, "ene_whole_element_resistance_change"], "敵全体の土属性耐性が一定ターン中ダウン" : [2, -29.6, 75, 29, 10, "ene_whole_element_resistance_change"], "敵全体の土属性耐性が一定ターン大ダウン" : [2, -44.4, 75, 36, 10, "ene_whole_element_resistance_change"], "敵全体の土属性耐性が一定ターン特大ダウン" : [2, -59.2, 75, 42, 10, "ene_whole_element_resistance_change"], 
                                            "敵全体の風属性耐性が一定ターン小ダウン" : [3, -14.8, 75, 23, 10, "ene_whole_element_resistance_change"], "敵全体の風属性耐性が一定ターン中ダウン" : [3, -29.6, 75, 29, 10, "ene_whole_element_resistance_change"], "敵全体の風属性耐性が一定ターン大ダウン" : [3, -44.4, 75, 36, 10, "ene_whole_element_resistance_change"], "敵全体の風属性耐性が一定ターン特大ダウン" : [3, -59.2, 75, 42, 10, "ene_whole_element_resistance_change"], 
                                            "敵全体の月属性耐性が一定ターン小ダウン" : [4, -14.8, 75, 23, 10, "ene_whole_element_resistance_change"], "敵全体の月属性耐性が一定ターン中ダウン" : [4, -29.6, 75, 29, 10, "ene_whole_element_resistance_change"], "敵全体の月属性耐性が一定ターン大ダウン" : [4, -44.4, 75, 36, 10, "ene_whole_element_resistance_change"], "敵全体の月属性耐性が一定ターン特大ダウン" : [4, -59.2, 75, 42, 10, "ene_whole_element_resistance_change"], 
                                            "敵全体の陽属性耐性が一定ターン小ダウン" : [5, -14.8, 75, 23, 10, "ene_whole_element_resistance_change"], "敵全体の陽属性耐性が一定ターン中ダウン" : [5, -29.6, 75, 29, 10, "ene_whole_element_resistance_change"], "敵全体の陽属性耐性が一定ターン大ダウン" : [5, -44.4, 75, 36, 10, "ene_whole_element_resistance_change"], "敵全体の陽属性耐性が一定ターン特大ダウン" : [5, -59.2, 75, 42, 10, "ene_whole_element_resistance_change"], 
                                            "自身の炎属性耐性が一定ターン小アップ" : [0, 14.8, 65, 21, 10, "self_element_resistance_change"], "自身の炎属性耐性が一定ターン中アップ" : [0, 29.6, 65, 27, 10, "self_element_resistance_change"], "自身の炎属性耐性が一定ターン大アップ" : [0, 44.4, 65, 34, 10, "self_element_resistance_change"], "自身の炎属性耐性が一定ターン特大アップ" : [0, 59.2, 65, 40, 10, "self_element_resistance_change"], 
                                            "自身の水属性耐性が一定ターン小アップ" : [1, 14.8, 65, 21, 10, "self_element_resistance_change"], "自身の水属性耐性が一定ターン中アップ" : [1, 29.6, 65, 27, 10, "self_element_resistance_change"], "自身の水属性耐性が一定ターン大アップ" : [1, 44.4, 65, 34, 10, "self_element_resistance_change"], "自身の水属性耐性が一定ターン特大アップ" : [1, 59.2, 65, 40, 10, "self_element_resistance_change"], 
                                            "自身の土属性耐性が一定ターン小アップ" : [2, 14.8, 65, 21, 10, "self_element_resistance_change"], "自身の土属性耐性が一定ターン中アップ" : [2, 29.6, 65, 27, 10, "self_element_resistance_change"], "自身の土属性耐性が一定ターン大アップ" : [2, 44.4, 65, 34, 10, "self_element_resistance_change"], "自身の土属性耐性が一定ターン特大アップ" : [2, 59.2, 65, 40, 10, "self_element_resistance_change"], 
                                            "自身の風属性耐性が一定ターン小アップ" : [3, 14.8, 65, 21, 10, "self_element_resistance_change"], "自身の風属性耐性が一定ターン中アップ" : [3, 29.6, 65, 27, 10, "self_element_resistance_change"], "自身の風属性耐性が一定ターン大アップ" : [3, 44.4, 65, 34, 10, "self_element_resistance_change"], "自身の風属性耐性が一定ターン特大アップ" : [3, 59.2, 65, 40, 10, "self_element_resistance_change"], 
                                            "自身の月属性耐性が一定ターン小アップ" : [4, 14.8, 65, 21, 10, "self_element_resistance_change"], "自身の月属性耐性が一定ターン中アップ" : [4, 29.6, 65, 27, 10, "self_element_resistance_change"], "自身の月属性耐性が一定ターン大アップ" : [4, 44.4, 65, 34, 10, "self_element_resistance_change"], "自身の月属性耐性が一定ターン特大アップ" : [4, 59.2, 65, 40, 10, "self_element_resistance_change"], 
                                            "自身の陽属性耐性が一定ターン小アップ" : [5, 14.8, 65, 21, 10, "self_element_resistance_change"], "自身の陽属性耐性が一定ターン中アップ" : [5, 29.6, 65, 27, 10, "self_element_resistance_change"], "自身の陽属性耐性が一定ターン大アップ" : [5, 44.4, 65, 34, 10, "self_element_resistance_change"], "自身の陽属性耐性が一定ターン特大アップ" : [5, 59.2, 65, 40, 10, "self_element_resistance_change"], 
                                            "自身の炎属性耐性が一定ターン小ダウン" : [0, -14.8, 65, 21, 10, "self_element_resistance_change"], "自身の炎属性耐性が一定ターン中ダウン" : [0, -29.6, 65, 27, 10, "self_element_resistance_change"], "自身の炎属性耐性が一定ターン大ダウン" : [0, -44.4, 65, 34, 10, "self_element_resistance_change"], "自身の炎属性耐性が一定ターン特大ダウン" : [0, -59.2, 65, 40, 10, "self_element_resistance_change"], 
                                            "自身の水属性耐性が一定ターン小ダウン" : [1, -14.8, 65, 21, 10, "self_element_resistance_change"], "自身の水属性耐性が一定ターン中ダウン" : [1, -29.6, 65, 27, 10, "self_element_resistance_change"], "自身の水属性耐性が一定ターン大ダウン" : [1, -44.4, 65, 34, 10, "self_element_resistance_change"], "自身の水属性耐性が一定ターン特大ダウン" : [1, -59.2, 65, 40, 10, "self_element_resistance_change"], 
                                            "自身の土属性耐性が一定ターン小ダウン" : [2, -14.8, 65, 21, 10, "self_element_resistance_change"], "自身の土属性耐性が一定ターン中ダウン" : [2, -29.6, 65, 27, 10, "self_element_resistance_change"], "自身の土属性耐性が一定ターン大ダウン" : [2, -44.4, 65, 34, 10, "self_element_resistance_change"], "自身の土属性耐性が一定ターン特大ダウン" : [2, -59.2, 65, 40, 10, "self_element_resistance_change"], 
                                            "自身の風属性耐性が一定ターン小ダウン" : [3, -14.8, 65, 21, 10, "self_element_resistance_change"], "自身の風属性耐性が一定ターン中ダウン" : [3, -29.6, 65, 27, 10, "self_element_resistance_change"], "自身の風属性耐性が一定ターン大ダウン" : [3, -44.4, 65, 34, 10, "self_element_resistance_change"], "自身の風属性耐性が一定ターン特大ダウン" : [3, -59.2, 65, 40, 10, "self_element_resistance_change"], 
                                            "自身の月属性耐性が一定ターン小ダウン" : [4, -14.8, 65, 21, 10, "self_element_resistance_change"], "自身の月属性耐性が一定ターン中ダウン" : [4, -29.6, 65, 27, 10, "self_element_resistance_change"], "自身の月属性耐性が一定ターン大ダウン" : [4, -44.4, 65, 34, 10, "self_element_resistance_change"], "自身の月属性耐性が一定ターン特大ダウン" : [4, -59.2, 65, 40, 10, "self_element_resistance_change"], 
                                            "自身の陽属性耐性が一定ターン小ダウン" : [5, -14.8, 65, 21, 10, "self_element_resistance_change"], "自身の陽属性耐性が一定ターン中ダウン" : [5, -29.6, 65, 27, 10, "self_element_resistance_change"], "自身の陽属性耐性が一定ターン大ダウン" : [5, -44.4, 65, 34, 10, "self_element_resistance_change"], "自身の陽属性耐性が一定ターン特大ダウン" : [5, -59.2, 65, 40, 10, "self_element_resistance_change"]
                                            }   # 属性耐性変化スキル. {説明 : [ele, rate, delay, recast, charge, skill_types]}. eleはどの属性耐性を変化させるか. 
    weak_element_bonus_change_skill_type = {"味方単体の有利属性へのダメージが一定ターンアップ" : ["weak_bonus", 35.0, 65, 21, 10, "chr_single_status_change"],"味方全体の有利属性へのダメージが一定ターンアップ" : ["weak_bonus", 35.0, 75, 23, 10, "chr_whole_status_change"],"味方全体の有利属性へのダメージが一定ターンアップ" : ["weak_bonus", 35.0, 65, 21, 10, "self_status_change"]}   # 有利属性ボーナス変化スキル. {説明 : [type, rate, delay, recast, charge, skill_types]}
    next_baff_skill_type = {
                            "味方単体の物理攻撃が一度だけ小アップ" : ["ATK", 51.8, 55, 23, 17, "chr_single_set_NEXTbuff"], "味方単体の物理攻撃が一度だけ中アップ" : ["ATK", 74.0, 55, 25, 17, "chr_single_set_NEXTbuff"], "味方単体の物理攻撃が一度だけ大アップ": ["ATK", 88.8, 55, 27, 17, "chr_single_set_NEXTbuff"], "味方単体の物理攻撃が一度だけ特大アップ" : ["ATK", 135.0, 55, 23, 17, "chr_single_set_NEXTbuff"], 
                            "味方単体の魔法攻撃が一度だけ小アップ" : ["MAT", 51.8, 55, 23, 17, "chr_single_set_NEXTbuff"], "味方単体の魔法攻撃が一度だけ中アップ" : ["MAT", 74.0, 55, 25, 17, "chr_single_set_NEXTbuff"], "味方単体の魔法攻撃が一度だけ大アップ": ["MAT", 88.8, 55, 27, 17, "chr_single_set_NEXTbuff"], "味方単体の魔法攻撃が一度だけ特大アップ" : ["MAT", 135.0, 55, 23, 17, "chr_single_set_NEXTbuff"], 
                            "味方全体の物理攻撃が一度だけ小アップ" : ["ATK", 51.8, 65, 25, 17, "chr_whole_set_NEXTbuff"], "味方全体の物理攻撃が一度だけ中アップ" : ["ATK", 74.0, 65, 27, 17, "chr_whole_set_NEXTbuff"], "味方全体の物理攻撃が一度だけ大アップ": ["ATK", 88.8, 55, 29, 17, "chr_whole_set_NEXTbuff"], "味方全体の物理攻撃が一度だけ特大アップ" : ["ATK", 135.0, 65, 25, 17, "chr_whole_set_NEXTbuff"], 
                            "味方全体の魔法攻撃が一度だけ小アップ" : ["MAT", 51.8, 65, 25, 17, "chr_whole_set_NEXTbuff"], "味方全体の魔法攻撃が一度だけ中アップ" : ["MAT", 74.0, 65, 27, 17, "chr_whole_set_NEXTbuff"], "味方全体の魔法攻撃が一度だけ大アップ": ["MAT", 88.8, 55, 29, 17, "chr_whole_set_NEXTbuff"], "味方全体の魔法攻撃が一度だけ特大アップ" : ["MAT", 135.0, 65, 25, 17, "chr_whole_set_NEXTbuff"], 
                            "自身の物理攻撃が一度だけ小アップ" : ["ATK", 51.8, 55, 23, 17, "self_set_NEXTbuff"], "自身の物理攻撃が一度だけ中アップ" : ["ATK", 74.0, 55, 25, 17, "self_set_NEXTbuff"], "自身の物理攻撃が一度だけ大アップ": ["ATK", 88.8, 55, 27, 17, "self_set_NEXTbuff"], "自身の物理攻撃が一度だけ特大アップ" : ["ATK", 135.0, 55, 23, 17, "self_set_NEXTbuff"], 
                            "自身の魔法攻撃が一度だけ小アップ" : ["MAT", 51.8, 55, 23, 17, "self_set_NEXTbuff"], "自身の魔法攻撃が一度だけ中アップ" : ["MAT", 74.0, 55, 25, 17, "self_set_NEXTbuff"], "自身の魔法攻撃が一度だけ大アップ": ["MAT", 88.8, 55, 27, 17, "self_set_NEXTbuff"], "自身の魔法攻撃が一度だけ特大アップ" : ["MAT", 135.0, 55, 23, 17, "self_set_NEXTbuff"]
                        }   # 次回の攻撃威力アップスキル. {説明 : [type, rate, delay, recast, charge, skill_types]}
    next_luk_baff_skill_type = {"味方単体の攻撃が一度だけクリティカルになる" : ["LUK", 1.0, 55, 23, 17, "chr_single_set_NEXTbuff"], "味方全体の攻撃が一度だけクリティカルになる" : ["LUK", 1.0, 65, 25, 17, "chr_whole_set_NEXTbuff"], "自身の攻撃が一度だけクリティカルになる" : ["LUK", 1.0, 55, 23, 17, "self_set_NEXTbuff"]}   # 次回の攻撃クリティカル確定スキル. {説明 : [type, rate, delay, recast, charge, skill_types]}
    barrier_skill_type = {"味方単体に1回だけ攻撃を完全カットするバリアを張る" : [100.0, 1, 140, 31, 8, "chr_single_set_barrier"], "味方単体に3回だけ攻撃を完全カットするバリアを張る" : [100.0, 3, 140, 31, 8, "chr_single_set_barrier"], "味方単体に1回だけ攻撃を大きくカットするバリアを張る" : [99.0, 1, 135, 27, 8, "chr_single_set_barrier"], "味方単体に3回だけ攻撃を大きくカットするバリアを張る" : [99.0, 3, 135, 27, 8, "chr_single_set_barrier"], "味方単体に1回だけ攻撃をカットするバリアを張る" : [74.0, 1, 130, 24, 8, "chr_single_set_barrier"], "味方単体に3回だけ攻撃をカットするバリアを張る" : [74.0, 3, 130, 24, 8, "chr_single_set_barrier"], "味方単体に1回だけ攻撃をすこしカットするバリアを張る" : [29.6, 1, 125, 22, 8, "chr_single_set_barrier"], "味方単体に3回だけ攻撃をすこしカットするバリアを張る" : [29.6, 3, 130, 22, 8, "chr_single_set_barrier"], "味方全体に1回だけ攻撃を完全カットするバリアを張る" : [100.0, 1, 150, 40, 8, "chr_whole_set_barrier"], "味方全体に3回だけ攻撃を完全カットするバリアを張る" : [100.0, 3, 150, 40, 8, "chr_whole_set_barrier"], "味方全体に1回だけ攻撃を大きくカットするバリアを張る" : [99.0, 1, 115, 37, 8, "chr_whole_set_barrier"], "味方全体に3回だけ攻撃を大きくカットするバリアを張る" : [99.0, 3, 145, 37, 8, "chr_whole_set_barrier"], "味方全体に1回だけ攻撃をカットするバリアを張る" : [74.0, 1, 140, 34, 8, "chr_whole_set_barrier"], "味方全体に3回だけ攻撃をカットするバリアを張る" : [74.0, 3, 140, 34, 8, "chr_whole_set_barrier"], "味方全体に1回だけ攻撃をすこしカットするバリアを張る" : [29.6, 1, 135, 32, 8, "chr_whole_set_barrier"], "味方全体に3回だけ攻撃をすこしカットするバリアを張る" : [29.6, 3, 135, 32, 8, "chr_whole_set_barrier"], "自身に1回だけ攻撃を完全カットするバリアを張る" : [100.0, 1, 140, 31, 8, "self_set_barrier"], "自身に3回だけ攻撃を完全カットするバリアを張る" : [100.0, 3, 140, 31, 8, "self_set_barrier"], "自身に1回だけ攻撃を大きくカットするバリアを張る" : [99.0, 1, 135, 27, 8, "self_set_barrier"], "自身に3回だけ攻撃を大きくカットするバリアを張る" : [99.0, 3, 135, 27, 8, "self_set_barrier"], "自身に1回だけ攻撃をカットするバリアを張る" : [74.0, 1, 130, 24, 8, "self_set_barrier"], "自身に3回だけ攻撃をカットするバリアを張る" : [74.0, 3, 130, 24, 8, "self_set_barrier"], "自身に1回だけ攻撃をすこしカットするバリアを張る" : [29.6, 1, 125, 22, 8, "self_set_barrier"], "自身に3回だけ攻撃をすこしカットするバリアを張る" : [29.6, 3, 130, 22, 8, "self_set_barrier"]}   # バリア付与スキル. {説明 : [rate, num, delay, recast, charge, skill_types]}
    recast_change_skill_type = {
                                "味方単体のリキャストをかなり減らす" : [-35.0, 75, 40, 8, "chr_single_recast_change"], "味方単体のリキャストを減らす" : [-25.0, 75, 36, 8, "chr_single_recast_change"], "味方単体のリキャストをすこし減らす" : [-15.0, 75, 32, 8, "chr_single_recast_change"], 
                                "味方全体のリキャストをかなり減らす" : [-35.0, 85, 43, 8, "chr_whole_recast_change"], "味方全体のリキャストを減らす" : [-25.0, 85, 39, 8, "chr_whole_recast_change"], "味方全体のリキャストをすこし減らす" : [-15.0, 85, 35, 8, "chr_whole_recast_change"], 
                                "味方単体のリキャストをかなり増やす" : [35.0, 75, 40, 8, "chr_single_recast_change"], "味方単体のリキャストを増やす" : [25.0, 75, 36, 8, "chr_single_recast_change"], "味方単体のリキャストをすこし増やす" : [15.0, 75, 32, 8, "chr_single_recast_change"], 
                                "味方全体のリキャストをかなり増やす" : [35.0, 85, 43, 8, "chr_whole_recast_change"], "味方全体のリキャストを増やす" : [25.0, 85, 39, 8, "chr_whole_recast_change"], "味方全体のリキャストをすこし増やす" : [15.0, 85, 35, 8, "chr_whole_recast_change"], 
                                "自身のリキャストをかなり減らす" : [-35.0, 75, 40, 8, "self_recast_change"], "自身のリキャストを減らす" : [-25.0, 75, 36, 8, "self_recast_change"], "自身のリキャストをすこし減らす" : [-15.0, 75, 32, 8, "self_recast_change"], 
                                "自身のリキャストをかなり増やす" : [35.0, 75, 40, 8, "self_recast_change"], "自身のリキャストを増やす" : [25.0, 75, 36, 8, "self_recast_change"], "自身のリキャストをすこし増やす" : [15.0, 75, 32, 8, "self_recast_change"]
                                }   # リキャスト変化スキル. {説明 : [rate, delay, recast, charge, skill_types]}
    jamp_gauge_change_skill_type = {"とっておきゲージをかなり増やす" : [66.0, 130, 34, 12, "jamp_gauge_change"], "とっておきゲージを増やす" : [50.0, 125, 32, 12, "jamp_gauge_change"], "とっておきゲージをすこし増やす" : [33.0, 120, 30, 12, "jamp_gauge_change"], }   # とっておきゲージ変化スキル. {説明 : [rate, delay, recast, charge, skill_types]}
    hate_change_skill_type = {"味方単体の狙われやすさが一定ターン小アップ" : ["hate", 20, 120, 29, 10, "chr_single_status_change"], "味方単体の狙われやすさが一定ターン中アップ" : ["hate", 40, 125, 31, 10, "chr_single_status_change"], "味方単体の狙われやすさが一定ターン大アップ" : ["hate", 60, 130, 33, 10, "chr_single_status_change"], "味方単体の狙われやすさが一定ターン特大アップ" : ["hate", 80, 140, 37, 10, "chr_single_status_change"], "味方単体の狙われやすさが一定ターン小ダウン" : ["hate", -20, 120, 29, 10, "chr_single_status_change"], "味方単体の狙われやすさが一定ターン中ダウン" : ["hate", -40, 120, 29, 10, "chr_single_status_change"], "味方単体の狙われやすさが一定ターン大ダウン" : ["hate", -60, 120, 29, 10, "chr_single_status_change"], "味方単体の狙われやすさが一定ターン特大ダウン" : ["hate", -80, 120, 29, 10, "chr_single_status_change"], "自身の狙われやすさが一定ターン小アップ" : ["hate", 20, 120, 29, 10, "self_status_change"], "自身の狙われやすさが一定ターン中アップ" : ["hate", 40, 125, 31, 10, "self_status_change"], "自身の狙われやすさが一定ターン大アップ" : ["hate", 60, 130, 33, 10, "self_status_change"], "自身の狙われやすさが一定ターン特大アップ" : ["hate", 80, 140, 37, 10, "self_status_change"], "自身の狙われやすさが一定ターン小ダウン" : ["hate", -20, 120, 29, 10, "self_status_change"], "自身の狙われやすさが一定ターン中ダウン" : ["hate", -40, 120, 29, 10, "self_status_change"], "自身の狙われやすさが一定ターン大ダウン" : ["hate", -60, 120, 29, 10, "self_status_change"], "自身の狙われやすさが一定ターン特大ダウン" : ["hate", -80, 120, 29, 10, "self_status_change"]}   # ヘイト変化スキル. {説明 : [rate, delay, recast, charge, skill_types]}
    charge_change_skill_type = {"敵単体のチャージカウントを減らす(-10)" : [10, 70, 23, 8, "ene_single_charge_change"], "敵単体のチャージカウントを大きく減らす(-2)" : [2, 70, 21, 8, "ene_single_charge_change"], "敵単体のチャージカウントを減らす" : [1, 70, 19, 8, "ene_single_charge_change"], "敵全体のチャージカウントを減らす(-10)" : [10, 80, 25, 8, "ene_whole_charge_change"], "敵全体のチャージカウントを大きく減らす(-2)" : [2, 70, 23, 8, "ene_whole_charge_change"], "敵全体のチャージカウントを減らす" : [1, 80, 21, 8, "ene_whole_charge_change"]}   # (敵の)チャージ量変化スキル. {説明 : [rate, delay, recast, charge, skill_types]}
    skill_card_skill_type = {
                            "味方全体を小回復するスキルカードを3枚設置" : ["chr_whole_recover", 19.0, 100, 3, 120, 40, 10, "set_skillcard"], "味方全体を中回復するスキルカードを3枚設置" : ["chr_whole_recover", 29.0, 100, 3, 120, 40, 10, "set_skillcard"], "味方全体を大回復するスキルカードを3枚設置" : ["chr_whole_recover", 39.0, 100, 3, 130, 50, 10, "set_skillcard"], "味方全体を特大回復するスキルカードを3枚設置" : ["chr_whole_recover", 49.0, 100, 3, 130, 50, 10, "set_skillcard"], 
                            "敵全体に炎属性の小ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 740.0, 100, 3, 120, 40, 10, "set_skillcard"], "敵全体に炎属性の中ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 1480.0, 100, 3, 120, 40, 10, "set_skillcard"], "敵全体に炎属性の大ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 2220.0, 100, 3, 130, 43, 10, "set_skillcard"], "敵全体に炎属性の特大ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 2960.0, 100, 3, 130, 43, 10, "set_skillcard"],
                            "敵全体に水属性の小ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 740.0, 100, 3, 120, 40, 10, "set_skillcard"], "敵全体に水属性の中ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 1480.0, 100, 3, 120, 40, 10, "set_skillcard"], "敵全体に水属性の大ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 2220.0, 100, 3, 130, 43, 10, "set_skillcard"], "敵全体に水属性の特大ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 2960.0, 100, 3, 130, 43, 10, "set_skillcard"],
                            "敵全体に土属性の小ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 740.0, 100, 3, 120, 40, 10, "set_skillcard"], "敵全体に土属性の中ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 1480.0, 100, 3, 120, 40, 10, "set_skillcard"], "敵全体に土属性の大ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 2220.0, 100, 3, 130, 43, 10, "set_skillcard"], "敵全体に土属性の特大ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 2960.0, 100, 3, 130, 43, 10, "set_skillcard"],
                            "敵全体に風属性の小ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 740.0, 100, 3, 120, 40, 10, "set_skillcard"], "敵全体に風属性の中ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 1480.0, 100, 3, 120, 40, 10, "set_skillcard"], "敵全体に風属性の大ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 2220.0, 100, 3, 130, 43, 10, "set_skillcard"], "敵全体に風属性の特大ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 2960.0, 100, 3, 130, 43, 10, "set_skillcard"],
                            "敵全体に月属性の小ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 740.0, 100, 3, 120, 40, 10, "set_skillcard"], "敵全体に月属性の中ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 1480.0, 100, 3, 120, 40, 10, "set_skillcard"], "敵全体に月属性の大ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 2220.0, 100, 3, 130, 43, 10, "set_skillcard"], "敵全体に月属性の特大ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 2960.0, 100, 3, 130, 43, 10, "set_skillcard"],
                            "敵全体に陽属性の小ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 740.0, 100, 3, 120, 40, 10, "set_skillcard"], "敵全体に陽属性の中ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 1480.0, 100, 3, 120, 40, 10, "set_skillcard"], "敵全体に陽属性の大ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 2220.0, 100, 3, 130, 43, 10, "set_skillcard"], "敵全体に陽属性の特大ダメージを与えるスキルカードを3枚設置" : ["ene_whole_attack", 2960.0, 100, 3, 130, 43, 10, "set_skillcard"],
                            "味方全体に1回だけ攻撃をすこしカットするスキルカードを3枚設置" : ["chr_whole_set_barrier", 30.0, 100, 3, 130, 50, 10, "set_skillcard"]
                            }   # スキルカード設置スキル. {説明 : [type, rate, skill_delay, skill_charge, num, delay, recast, charge, skill_types]}
    recovery_skill_type = {"自身にリカバリーを付与" : [39.0, 140, 24, 8, "self_set_recovery"], "味方単体にリカバリーを付与" : [39.0, 140, 24, 8, "chr_single_set_recovery"], "味方全体にリカバリーを付与" : [39.0, 150, 30, 8, "chr_whole_set_recovery"]}   # リカバリー付与スキル. {説明 : [rate, delay, recast, charge, skill_types]}
    quick_draw_skill_type = {"自身にクイックドロウを付与" : ["quick_draw", -82.5, 45, 27, 8, "self_status_change"], "味方単体にクイックドロウを付与" : ["quick_draw", -82.5, 45, 27, 8, "chr_single_status_change"], "味方全体にクイックドロウを付与" : ["quick_draw", -82.5, 55, 30, 8, "chr_whole_status_change"]}   # クイックドロウスキル. {説明 : [rate, delay, recast, charge, skill_types]}
    # random_status_change_skill_type = {"味方全体のステータスのいずれかが一定ターン大アップ" : [[["ATK", 44.4], ["MAT", 44.4], ["DEF", 51.8], ["MDF", 51.8], ["SPD", 42.5], ["LUK", 296.0]], 75, 27, 8, "chr_whole_random_status_change"], "敵全体のステータスのいずれかが一定ターン大ダウン" : [[["ATK", -29.6], ["MAT", -29.6], ["DEF", -29.6], ["MDF", -29.6], ["SPD", -52.5]], 75, 27, 8, "ene_whole_random_status_change"], "自身のMATが一定ターン小～大アップ" : [[["MAT", 22.2], ["MAT", 34.0], ["MAT", 44.4]], 75, 27, 8, "self_random_status_change"], "自身のATKが一定ターン小～大アップ" : [[["ATK", 22.2], ["ATK", 34.0], ["ATK", 44.4]], 75, 27, 8, "self_random_status_change"]}   # ランダムステータス変化スキル. {説明 : [rates, delay, recast, charge, skill_types]}
    set_patience_skill_type = {"味方単体にがまんを付与" : [85, 27, 10, "chr_single_set_patience"], "味方全体にがまんを付与" : [90, 30, 10, "chr_whole_set_patience"], "自身にがまんを付与" : [85, 27, 10, "self_set_patience"]}   # 我慢付与スキル. {説明 : [delay, recast, charge, skill_types]}
    critical_damage_change_skill_type = {"味方単体のクリティカル時ダメージが一定ターン小アップ" : ["cri_dam", 17.0, 65, 21, 10, "chr_single_status_change"], "味方単体のクリティカル時ダメージが一定ターン中アップ" : ["cri_dam", 33.0, 65, 27, 10, "chr_single_status_change"], "味方単体のクリティカル時ダメージが一定ターン大アップ" : ["cri_dam", 49.0, 65, 34, 10, "chr_single_status_change"], "味方単体のクリティカル時ダメージが一定ターン特大アップ" : ["cri_dam", 65.0, 65, 38, 10, "chr_single_status_change"], "味方全体のクリティカル時ダメージが一定ターン小アップ" : ["cri_dam", 17.0, 75, 23, 10, "chr_whole_status_change"], "味方全体のクリティカル時ダメージが一定ターン中アップ" : ["cri_dam", 33.0, 75, 29, 10, "chr_whole_status_change"], "味方全体のクリティカル時ダメージが一定ターン大アップ" : ["cri_dam", 17.0, 75, 36, 10, "chr_whole_status_change"], "味方全体のクリティカル時ダメージが一定ターン特大アップ" : ["cri_dam", 65.0, 65, 40, 10, "chr_whole_status_change"], "自身のクリティカル時ダメージが一定ターン小アップ" : ["cri_dam", 17.0, 65, 21, 10, "self_status_change"], "自身のクリティカル時ダメージが一定ターン中アップ" : ["cri_dam", 33.0, 65, 27, 10, "self_status_change"], "自身のクリティカル時ダメージが一定ターン大アップ" : ["cri_dam", 49.0, 65, 34, 10, "self_status_change"], "自身のクリティカル時ダメージが一定ターン特大アップ" : ["cri_dam", 65.0, 65, 38, 10, "self_status_change"]}   # クリティカルダメージ変化スキル. {説明 : [rate, delay, recast, charge, skill_types]}
    d = skill_attack_skill_type | recover_skill_type | status_change_skill_type | status_change_reset_skill_type | status_down_invaild_skill_type | abnormal_skill_type | abnormal_recover_skill_type | abnormal_invalid_skill_type | abnormal_probability_change_skill_type | element_resistance_change_skill_type | weak_element_bonus_change_skill_type | next_baff_skill_type | next_luk_baff_skill_type | barrier_skill_type | recast_change_skill_type | jamp_gauge_change_skill_type | hate_change_skill_type | charge_change_skill_type | skill_card_skill_type | recovery_skill_type | quick_draw_skill_type | set_patience_skill_type | critical_damage_change_skill_type
    return d


skill_type_dict = {0 : "物理攻撃スキル", 1 : "魔法攻撃スキル", 2 : "回復スキル", 3 : "ステータス変化スキル", 4 : "ステータス変化リセットスキル", 5 : "ステータスダウン無効スキル", 6 : "状態異常スキル", 7 : "状態異常リセットスキル", 8 : "状態異常無効スキル", 9 : "状態異常耐性スキル", 10 : "属性耐性スキル", 11 : "有利属性ボーナススキル", 12 : "物理ネクストバフスキル", 13 : "魔法ネクストバフスキル", 14 : "クリティカルネクストバフスキル", 15 : "バリアスキル", 16 : "リキャスト変化スキル", 17 : "とっておきゲージ変化スキル", 18 : "ヘイトスキル", 19 : "チャージ変化スキル", 20 : "スキルカードスキル", 21 : "リカバリースキル", 22 : "クイックドロウスキル", 23 : "がまんスキル", 24 : "クリティカルダメージスキル"}
skill_info_dict = {}
for key, value in skill_information_dict().items():
    skill_name, skill_type, skill_delay, skill_recast, skill_charge, skill_info, skill_rate, status_type, reset_bool, skill_prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num = [None for i in range(17)]
    skill_name = key
    if ("physics_attack" in value[-1]):
        skill_type = 0
        skill_rate = value[0]
        skill_delay = value[1]
        skill_recast = value[2]
        skill_charge = value[3]
        skill_info = value[4]
        
    elif ("magic_attack" in value[-1]):
        skill_type = 1
        skill_rate = value[0]
        skill_delay = value[1]
        skill_recast = value[2]
        skill_charge = value[3]
        skill_info = value[4]
        
    elif ("recovery" in value[-1]):
        skill_type = 21
        skill_rate = value[0]
        skill_delay = value[1]
        skill_recast = value[2]
        skill_charge = value[3]
        skill_info = value[4]
        
    elif ("recover" in value[-1]):
        skill_type = 2
        skill_rate = value[0]
        skill_delay = value[1]
        skill_recast = value[2]
        skill_charge = value[3]
        skill_info = value[4]
        
    elif ("status_change" in value[-1]):
        skill_type = 3
        if (value[0] == "ATK"):
            status_type = 1
        elif (value[0] == "MAT"):
            status_type = 2
        elif (value[0] == "DEF"):
            status_type = 3
        elif (value[0] == "MDF"):
            status_type = 4
        elif (value[0] == "SPD"):
            status_type = 5
        elif (value[0] == "LUK"):
            status_type = 6
        elif (value[0] == "cri_dam"):
            skill_type = 24
            status_type = 14
        elif (value[0] == "hate"):
            skill_type = 18
            status_type = 15
        elif (value[0] == "weak_bonus"):
            skill_type = 11
            status_type = 23
        elif (value[0] == "quick_draw"):
            skill_type = 22
            status_type = 24
        
        skill_rate = value[1]
        skill_delay = value[2]
        skill_recast = value[3]
        skill_charge = value[4]
        skill_info = value[-1]
        
    elif ("status_reset" in value[-1]):
        skill_type = 4
        reset_bool = value[0]
        if (value[1] == "ATK"):
            status_type = 1
        elif (value[1] == "MAT"):
            status_type = 2
        elif (value[1] == "DEF"):
            status_type = 3
        elif (value[1] == "MDF"):
            status_type = 4
        elif (value[1] == "SPD"):
            status_type = 5
        elif (value[1] == "LUK"):
            status_type = 6
        elif (value[1] == "ALL"):
            status_type = 25
            
        skill_delay = value[2]
        skill_recast = value[3]
        skill_charge = value[4]
        skill_info = value[5]
        
    elif ("status_invalid" in value[-1]):
        skill_type = 5
        skill_delay = value[0]
        skill_recast = value[1] 
        skill_charge = value[2]
        skill_info = value[3]
        
    elif ("set_abnormal" in value[-1]):
        skill_type = 6
        skill_prob = value[0]
        if (value[1] == "混乱"):
            abnormal_type = 0
        elif (value[1] == "金縛り"):
            abnormal_type = 1
        elif (value[1] == "腹ペコ"):
            abnormal_type = 2
        elif (value[1] == "弱気"):
            abnormal_type = 3
        elif (value[1] == "眠り"):
            abnormal_type = 4
        elif (value[1] == "不幸"):
            abnormal_type = 5
        elif (value[1] == "沈黙"):
            abnormal_type = 6
        elif (value[1] == "孤立"):
            abnormal_type = 7
        skill_delay = value[2]
        skill_recast = value[3]
        skill_charge = value[4]
        skill_info = value[5]
    
    elif ("abnormal_reset" in value[-1]):
        skill_type = 7
        if (value[0] == "混乱"):
            abnormal_type = 0
        elif (value[0] == "金縛り"):
            abnormal_type = 1
        elif (value[0] == "腹ペコ"):
            abnormal_type = 2
        elif (value[0] == "弱気"):
            abnormal_type = 3
        elif (value[0] == "眠り"):
            abnormal_type = 4
        elif (value[0] == "不幸"):
            abnormal_type = 5
        elif (value[0] == "沈黙"):
            abnormal_type = 6
        elif (value[0] == "孤立"):
            abnormal_type = 7
        skill_delay = value[1]
        skill_recast = value[2]
        skill_charge = value[3]
        skill_info = value[4]
    
    elif ("abnormal_invalid" in value[-1]):
        skill_type = 8
        skill_delay = value[0]
        skill_recast = value[1]
        skill_charge = value[2]
        skill_info = value[3]

    elif ("probability" in value[-1]):
        skill_type = 9
        skill_rate = value[0]
        skill_delay = value[1]
        skill_recast = value[2]
        skill_charge = value[3]
        skill_info = value[4]
        
    elif ("element" in value[-1]):
        skill_type = 10
        if (value[0] == 0):
            status_type = 17
        elif (value[0] == 1):
            status_type = 18
        elif (value[0] == 2):
            status_type = 19
        elif (value[0] == 3):
            status_type = 20
        elif (value[0] == 4):
            status_type = 21
        elif (value[0] == 5):
            status_type = 22
        skill_rate = value[1]
        skill_delay = value[2]
        skill_recast = value[3]
        skill_charge = value[4]
        skill_info = value[5]
        
    elif ("NEXTbuff" in value[-1]):
        if (value[0] == "ATK"):
            skill_type = 12
        elif (value[0] == "MAT"):
            skill_type = 13
        elif (value[0] == "LUK"):
            skill_type = 14
        skill_rate = value[1]
        skill_delay = value[2]
        skill_recast = value[3]
        skill_charge = value[4]
        skill_info = value[5]
        
    elif ("barrier" in value[-1]):
        skill_type = 15
        skill_rate = value[0]
        barrier_num = value[1]
        skill_delay = value[2]
        skill_recast = value[3]
        skill_charge = value[4]
        skill_info = value[5]
        
    elif ("recast_change" in value[-1]):
        skill_type = 16
        skill_rate = value[0]
        skill_delay = value[1]
        skill_recast = value[2]
        skill_charge = value[3]
        skill_info = value[4]
        
    elif ("gauge_change" in value[-1]):
        skill_type = 17
        skill_rate = value[0]
        skill_delay = value[1]
        skill_recast = value[2]
        skill_charge = value[3]
        skill_info = value[4]
        
    elif ("charge_change" in value[-1]):
        skill_type = 19
        skill_rate = value[0]
        skill_delay = value[1]
        skill_recast = value[2]
        skill_charge = value[3]
        skill_info = value[4]
        
    elif ("skillcard" in value[-1]):
        skill_type = 20
        skill_card_info = value[0]
        skill_card_rate = value[1]
        skill_card_delay = value[2]
        if ("recover" in value[0]):
            skill_card_charge = 13
        elif ("attack" in value[0]):
            skill_card_charge = 33
        elif ("barrier" in value[0]):
            skill_card_charge = 25
        skill_card_num = value[3]
        skill_delay = value[4]
        skill_recast = value[5]
        skill_charge = value[6]
        skill_info = value[7]
    
    elif ("patience" in value[-1]):
        skill_type = 23
        skill_delay = value[0]
        skill_recast = value[1]
        skill_charge = value[2]
        skill_info = value[3]
    
    
    skill_info_dict[skill_name] = [skill_type, skill_delay, skill_recast, skill_charge, skill_info, skill_rate, status_type, reset_bool, skill_prob, abnormal_type, barrier_num, skill_card_info, skill_card_rate, skill_card_delay, skill_card_charge, skill_card_num]
    


###
# Data.
###

###
# My Function of sqlite.
###

def sq_print(cur: sqlite3.Cursor, table_name: str):
    """
    Show the table.
    """
    cur.execute("SELECT * FROM " + table_name)
    for i in cur:
        print(i)

def sq_create(cur: sqlite3.Cursor, table_name: str, table_arg: list[str]):
    """
    Create the table
    """
    sql = "CREATE TABLE " + table_name + "("
    arg_len = len(table_arg)
    
    for num, arg in enumerate(table_arg, 1):
        if (num == arg_len):
            sql += arg + ")"
        else:
            sql += arg + ", "
            
    try:
        cur.execute(sql)
        print("A new table will be created because the already created table does not exist.")
    except:
        print("A table has already been created and cannot be created.")

def sq_insert(con: sqlite3.Connection, cur: sqlite3.Cursor, table_name: str, data_path: str = "", data_dict: dict = {}):
    """
    Insert data from a CSV data file.
    """
    if (len(data_dict) == 0):
        with open(data_path, "r") as f:
            reader = csv.reader(f)
            for data_column in reader:
                sql = "INSERT INTO " + table_name + " values("
                try:
                    data_l = [int(i) for i in data_column]
                    data_len = len(data_l)
                    for i, data in enumerate(data_l, 1):
                        if (i == data_len):
                            sql += str(data) + ")"
                        else:
                            sql += str(data) + ", "
                            
                    cur.execute(sql)
                    con.commit()
                
                except:
                    _len = len(data_column)
                    for num, data in enumerate(data_column, 1):
                        try:
                            if (num == _len):
                                sql += str(int(data)) + ")"
                            else:
                                sql += str(int(data)) + ", "
                        except:
                            if (data == None):
                                data = "None"
                            
                            if (num == _len):
                                sql += "'" + data + "'" + ")"
                            else:
                                sql+= "'" + data + "'" + ", "
                    
                    cur.execute(sql)
                    con.commit()

    else:
        for key, value in data_dict.items():
            sql = "INSERT INTO " + table_name + "  values("
            if (type(key) == int or type(key) == float):
                    sql += str(key) + ", "
            elif (type(key) == str):
                sql += "'" + key + "', "
                    
            if (type(value) == list):
                _len = len(value)
                for num, data in enumerate(value, 1):
                    if (type(data) == int or type(data) == float):
                        if (num == _len):
                            sql += str(data) + ")"
                        else:
                            sql += str(data) + ", "
                    elif (type(data) == str):
                        if (num == _len):
                            sql += "'" + data + "')"
                        else:
                            sql += "'" + data + "', "
                    elif (data == None):
                        if (num == _len):
                            sql += "'" + "None" + "')"
                        else:
                            sql += "'" + "None" + "', "
                            
            elif (type(value) == str):
                sql += "'" + value + "')"
            
            cur.execute(sql)
            con.commit()
            
            
###
# My Function of sqlite.
###

###
# Making Data.
###

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

# con = sqlite3.connect(SKILL_INFORMATION_PATH)
# cur = con.cursor()
# sq_print(cur, SKILL_NAME)

"""
# # Finished Making Character's Information. Character's Information is character's status, character's name, ... etc.
# con = sqlite3.connect(CHARACTER_INFORMATION_PATH)
# cur = con.cursor()

# arg_l = ["number", "name", "rarity", "class", "element", "title", "HP", "ATK", "MAT", "DEF", "MDF", "SPD", "limited", "distribution", "LUK", "friendship", "level"]
# sq_create(cur, INFO_NAME, arg_l)
# sq_insert(con, cur, INFO_NAME, data_path="Data/kirafan_character_status.csv")
# sq_print(cur, INFO_NAME)

# cur.close()
# con.close()


# # Finished Making data that associates numbers and character's name.
# con = sqlite3.connect(CHARACTER_NAME_PATH)
# cur = con.cursor()

# arg_l = ["number", "name"]
# sq_create(cur, NAME_NAME, arg_l)
# sq_insert(con, cur, NAME_NAME, data_dict=character_name_dict)
# sq_print(cur, NAME_NAME)

# cur.close()
# con.close()


# # Finished Making data that associates numbers and character's title.
# con = sqlite3.connect(CHARACTER_TITLE_PATH)
# cur = con.cursor()

# arg_l = ["number", "title"]
# sq_create(cur, TITLE_NAME, arg_l)
# sq_insert(con, cur, TITLE_NAME, data_dict=title_dict)
# sq_print(cur, TITLE_NAME)

# cur.close()
# con.close()


# # Finished Making character's skill information. Information is skill type, skill delay, ... etc.
# con = sqlite3.connect(SKILL_INFORMATION_PATH)
# cur = con.cursor()

# arg_l = ["name", "type", "delay", "recast", "charge", "info", "rate", "status_type", "reset_bool", "prob", "abnormal_type", "barrier_num", "skill_card_info", "skill_card_rate", "skill_card_delay", "skill_card_charge", "skill_card_num"]
# sq_create(cur, SKILL_NAME, arg_l)
# sq_insert(con, cur, SKILL_NAME, data_dict=skill_info_dict)
# sq_print(cur, SKILL_NAME)

# cur.close()
# con.close()

# # Finished Making Character's skill Information. skill name, skill effect.
# con = sqlite3.connect(CHARACTER_SKILL_INFORMATION_PATH)
# cur = con.cursor()

# arg_l = ["number", "skill1_name", "skill1_information", "skill2_name", "skill2_information", "jamp_name", "jamp_information", "unevolved_name", "unevolved_information", "evolved_name", "evolved_information", "auto_information"]
# sq_create(cur, CHR_SKILL_NAME, arg_l)
# sq_insert(con, cur, CHR_SKILL_NAME, data_path="Data/kirafan_character_skill_type.csv")
# sq_print(cur, CHR_SKILL_NAME)

# cur.close()
# con.close()
"""

###
# Making Data.
###