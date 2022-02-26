
# MC NPC Maker

注意: 完全に身内用なので、共通認識の確認が抜けてるかもしれません。  
このプログラム群はプレーンテキスト(普通の文章)からマイクラコマンドを作るものです。  
コマンドは、コマンドブロックでの運用を想定した１コマンドで完結するものです。  
NPCに話させるイメージ。  
Python3、pyperclipが必要。  

機能は

- プレーンテキスト > JSON
- JSON > summon (NPCを作る)
- JSON > tellraw (NPCが話す)
~~- JSON > give (NPCの話のログブックをプレイヤーにゆっくり渡す。正確にはsummon)~~

例えばこのようなJSONを用意すると、  

```json
{
    "name_color": "#ede353",
    "text_color": "#faf8de",
    "name": "ムキムキのお兄さん",
    "author": "logbook",
    "texts": {
        "シーン１": [
            "「君たち、エッグハントしてるんだって？",
            "今日は領主様、いつもより張り切って準備してたからね。",
            "沢山見つけられるよう頑張って！",
            "ああ、そうだ！ たまご探しをするなら、一回町を見渡すといいかもしれないね。",
            "新しい視点で物事を見つめるって、実はすごく大事なことなんだよ？",
            "僕のおすすめは風車かな！",
            "『ちくわ大明神』",
            "ちょっと登るにはコツがいるんだけど、見晴らしはとってもいいよ！",
            "それにほら、頑張って登ったら僕みたいにムキムキになれるかもよ？",
            "なーんてね！」"
        ],
        "シーン２" :
        [
            "abbbabababababa^^"
        ]
    },
    "profession": "weaponsmith",
    "biome": "taiga"
}
```

次のコマンド群を自動生成します。  

## JSON > summon (NPCを作る)

```mcfunction
# 召喚コマンド
summon villager ~ ~ ~ {Invulnerable: 1b, NoAI: 1b, CustomName: '[{"text":"[","color":"#ede353"},{"text":"ムキムキのお兄さん","color":"white"},{"text":"]","color":"#ede353"}]', VillagerData: {profession: "minecraft:weaponsmith", type: "minecraft:taiga"}, Offers: {}}
```

## JSON > tellraw (NPCが話す)

```mcfunction
# 台詞
## シーン１
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"君たち、エッグハントしてるんだって？","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"今日は領主様、いつもより張り切って準備してたからね。","color":"#faf8de"}]
 
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"沢山見つけられるよう頑張って！","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"ああ、そうだ！ たまご探しをするなら、一回町を見渡すといいかもしれないね。","color":"#faf8de"}]
 
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"新しい視点で物事を見つめるって、実はすごく大事なことなんだよ？","color":"#faf8de"}]
 
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"僕のおすすめは風車かな！","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"『ちくわ大明神』","color":"#faf8de"}]
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"ちょっと登るにはコツがいるんだけど、見晴らしはとってもいいよ！","color":"#faf8de"}]
 
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"それにほら、頑張って登ったら僕みたいにムキムキになれるかもよ？","color":"#faf8de"}]
 
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"なーんてね！","color":"#faf8de"}]
## シーン２
execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#ede353"}, {"text":" ムキムキのお兄さん "}, {"text":">  ","color":"#ede353"} ,{"text":"abbbabababababa^^","color":"#faf8de"}]
```

## JSON > give (ログブックをゆっくり渡す。正確にはsummon)

**非常に不安定なため非推奨。**

``` mcfunction
# 本
## シーン１
execute at @e[type=villager,name="[ムキムキのお兄さん]",distance=0..,limit=1] run summon item ^ ^1.5 ^1 {NoGravity:1b,Glowing:1b,PickupDelay:60,Motion:[0.0,-0.05,0.0],Item:{id:"minecraft:written_book",tag:{pages:['{"text":"君たち、エッグハントしてるんだって？\\n\\n今日は領主様、いつもより張り切って準備してたからね。\\n\\n沢山見つけられるよう頑張って！\\n\\nああ、そうだ！ たまご探しをするなら、一回町を見渡すといいかもしれないね。\\n\\n"}','{"text":"新しい視点で物事を見つめるって、実はすごく大事なことなんだよ？\\n\\n僕のおすすめは風車かな！\\n\\n『ちくわ大明神』\\n\\nちょっと登るにはコツがいるんだけど、見晴らしはとってもいいよ！\\n\\n"}','{"text":"それにほら、頑張って登ったら僕みたいにムキムキになれるかもよ？\\n\\nなーんてね！\\n\\n"}'],title:"シーン１",author:"logbook"},Count:5b}}
## シーン２
execute at @e[type=villager,name="[ムキムキのお兄さん]",distance=0..,limit=1] run summon item ^ ^1.5 ^1 {NoGravity:1b,Glowing:1b,PickupDelay:60,Motion:[0.0,-0.05,0.0],Item:{id:"minecraft:written_book",tag:{pages:['{"text":"abbbabababababa^^\\n\\n"}'],title:"シーン２",author:"logbook"},Count:5b}}
```

# 前準備

## 台詞

プレーンテキストはふつーに書きます。  
プログラムによって「」は消されるので、セリフ内セリフは『』を使ってください。  
最終的にマイクラ内で1行に表示したい所で改行させます。  

### 台詞の例

「君たち、エッグハントしてるんだって？  
今日は領主様、いつもより張り切って準備してたからね。  
沢山見つけられるよう頑張って！  
ああ、そうだ！ たまご探しをするなら、一回町を見渡すといいかもしれないね。  
新しい視点で物事を見つめるって、実はすごく大事なことなんだよ？  
僕のおすすめは風車かな！  
『ちくわ大明神』  
ちょっと登るにはコツがいるんだけど、見晴らしはとってもいいよ！  
それにほら、頑張って登ったら僕みたいにムキムキになれるかもよ？  
なーんてね！」  

## NPCの名前と見た目

NPCは村人を使う想定でいくつか決めます。  
決めるだけでJSONに直接記入とかでもいいです。  
スプレッドシートとかで管理しといてJSONに書き換えとかでもいいかもしれないね。  

- NPCの名前
- 名前の色 (名前表示時に名前を囲むカッコの色。カーソルを村人に合わせたときと、tellraw時)
- 台詞の色 (tellrawの台詞部分の色。)
- ログブックの著者
- 村人の職業 (職業。https://minecraft.fandom.com/wiki/Villager#Professions)
- 村人の服装 (バイオームによる指定。https://minecraft.fandom.com/wiki/Villager#Professions)

## JSONを書く

プレーンテキストをJSONに書き換えることで、プログラムでの誤作動を減らします。  
JSONはinuputフォルダの中に作ってください。  
テンプレはtemplate.jsonに、例はinput/example.jsonにあります。  
色は16進数指定、職業とバイオームは英語wikiのやつ全部小文字。  
scene1やscene2の値は変更、増やすことができます。  
同じNPCに昼と夜違うことを話せるとか、シーンの違う場合でも同じファイルに入れるための仕組みです。  
マイクラ上ではシーン名はログブックのタイトルとして使用されます。  

### 台詞の変換 (clipboard2json)

プレーンテキストを""で囲ってカンマを付けるプログラムを用意しています。  
台詞の1シーンをコピーした状態でclipboard2json.pyを実行することで結果をクリップボードに保存します。  
そのままJSONファイルにペーストしてください。  
ただ、""で囲うだけなのでJSONとしての整形は必要です。  

## プログラムの実行

json2commands.py を実行するとinputフォルダ内にある全てのJSONファイルに対して
summon、tellraw、giveのコマンドが生成されます。  
結果は、コンソールとcommandフォルダに保存されます。  

## プログラムのカスタマイズ

各プログラムには冒頭に大文字の定数宣言があります。  
若干はいじっても大丈夫です。