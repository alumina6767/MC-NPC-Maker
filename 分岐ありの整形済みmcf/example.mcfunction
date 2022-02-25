#region [meta] プログラムが使用するメタデータゾーン
## !ID=test_npc
#endregion

#region [etc] こまごまとしたコマンドゾーン (mcf2のプログラム類で処理されません)
## 召喚コマンド
summon villager ~ ~ ~ {Invulnerable: 1b, NoAI: 1b, CustomName: '[{"text":"[","color":"#ede353"},{"text":"ムキムキのお兄さん","color":"white"},{"text":"]","color":"#ede353"}]', VillagerData: {profession: "minecraft:weaponsmith", type: "minecraft:taiga"}, Offers: {}}
#endregion

#region [if] 条件分岐ゾーン (上から順に条件コマンドの結果が真なら該当のシーンのみが再生されます helpコマンドは常に真を表します)
## !if=シーン１
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run clear @p stone_button 0
## !if=シーン２
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run clear @p oak_button 0
## !if=シーン３
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run clear @p acacia_button 0
## !if=シーン４
help
#endregion

#region [scene] 会話シーンコマンドゾーン
## !scene=シーン１
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"おお","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"石のボタンを持ってきたのか","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"ありがとよ","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] rotated ~ 0 run setblock ^ ^ ^1 acacia_button[face=floor]
## !scene=シーン２
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"おまえ..","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"オークのボタンを持ってるけど","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"ほしいのは石のボタンなんだよなぁ...","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] rotated ~ 0 run setblock ^ ^ ^1 acacia_button[face=floor]
## !scene=シーン３
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"あー","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"アカシアのボタンじゃないんすよ","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] rotated ~ 0 run setblock ^ ^ ^1 acacia_button[face=floor]
## !scene=シーン４
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"ねえ君","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"暇なら、石のボタンを持ってきてくれないか？","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] rotated ~ 0 run setblock ^ ^ ^1 acacia_button[face=floor]
#endregion

