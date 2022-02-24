# 召喚コマンド
summon villager ~ ~ ~ {Invulnerable: 1b, NoAI: 1b, CustomName: '[{"text":"[","color":"#ede353"},{"text":"ムキムキのお兄さん","color":"white"},{"text":"]","color":"#ede353"}]', VillagerData: {profession: "minecraft:weaponsmith", type: "minecraft:taiga"}, Offers: {}}

# !ID=test_npc
# !scene=シーン１
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"おお","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"石のボタンを持ってきたのか","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"ありがとよ","color":"#faf8de"}]
execute at @e[type=villager,name="[ムキムキのお兄さん]",distance=0..,limit=1] run summon item ^ ^1.5 ^1 {NoGravity:1b,Glowing:1b,PickupDelay:60,Motion:[0.0,-0.05,0.0],Item:{id:"written_book",tag:{pages:['{"text":"おお\\n\\n石のボタンを持ってきたのか\\n\\nありがとよ\\n\\n"}'],title:"シーン１",author:"logbook"},Count:5b}}
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] rotated ~ 0 run setblock ^ ^ ^1 acacia_button[face=floor]
# !scene=シーン２
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"おまえ..","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"オークのボタンを持ってるけど","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"ほしいのは石のボタンなんだよなぁ...","color":"#faf8de"}]
execute at @e[type=villager,name="[ムキムキのお兄さん]",distance=0..,limit=1] run summon item ^ ^1.5 ^1 {NoGravity:1b,Glowing:1b,PickupDelay:60,Motion:[0.0,-0.05,0.0],Item:{id:"written_book",tag:{pages:['{"text":"おまえ..\\n\\nオークのボタンを持ってるけど\\n\\nほしいのは石のボタンなんだよなぁ...\\n\\n"}'],title:"シーン２",author:"logbook"},Count:5b}}
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] rotated ~ 0 run setblock ^ ^ ^1 acacia_button[face=floor]
# !scene=シーン３
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"あー","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"アカシアのボタンじゃないんすよ","color":"#faf8de"}]
execute at @e[type=villager,name="[ムキムキのお兄さん]",distance=0..,limit=1] run summon item ^ ^1.5 ^1 {NoGravity:1b,Glowing:1b,PickupDelay:60,Motion:[0.0,-0.05,0.0],Item:{id:"written_book",tag:{pages:['{"text":"あー\\n\\nアカシアのボタンじゃないんすよ\\n\\n"}'],title:"シーン３",author:"logbook"},Count:5b}}
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] rotated ~ 0 run setblock ^ ^ ^1 acacia_button[face=floor]
# !scene=シーン４
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"ねえ君","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"暇なら、石のボタンを持ってきてくれないか？","color":"#faf8de"}]
execute at @e[type=villager,name="[ムキムキのお兄さん]",distance=0..,limit=1] run summon item ^ ^1.5 ^1 {NoGravity:1b,Glowing:1b,PickupDelay:60,Motion:[0.0,-0.05,0.0],Item:{id:"written_book",tag:{pages:['{"text":"ねえ君\\n\\n暇なら、石のボタンを持ってきてくれないか？\\n\\n"}'],title:"シーン４",author:"logbook"},Count:5b}}
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] rotated ~ 0 run setblock ^ ^ ^1 acacia_button[face=floor]
