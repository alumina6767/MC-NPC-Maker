#region [meta] プログラムが使用するメタデータゾーン
## !ID=ED1
#endregion

#region [etc] こまごまとしたコマンドゾーン (mcf2のプログラム類で処理されません)
## 召喚コマンド
summon villager ~ ~ ~ {Invulnerable: 1b, NoAI: 1b, CustomName: '[{"text":"[","color":"#c71585"},{"text":"領主","color":"white"},{"text":"]","color":"#c71585"}]', VillagerData: {profession: "minecraft:weaponsmith", type: "minecraft:taiga"}, Offers: {}}
## 召喚コマンド
summon villager ~ ~ ~ {Invulnerable: 1b, NoAI: 1b, CustomName: '[{"text":"[","color":"#2348eb"},{"text":"運営","color":"white"},{"text":"]","color":"#2348eb"}]', VillagerData: {profession: "minecraft:weaponsmith", type: "minecraft:taiga"}, Offers: {}}
## 召喚コマンド
summon villager ~ ~ ~ {Invulnerable: 1b, NoAI: 1b, CustomName: '[{"text":"[","color":"#574f42"},{"text":"？？？","color":"white"},{"text":"]","color":"#574f42"}]', VillagerData: {profession: "minecraft:weaponsmith", type: "minecraft:taiga"}, Offers: {}}
## 召喚コマンド
summon villager ~ ~ ~ {Invulnerable: 1b, NoAI: 1b, CustomName: '[{"text":"[","color":"#FFFFFF"},{"text":"システム","color":"white"},{"text":"]","color":"#FFFFFF"}]', VillagerData: {profession: "minecraft:weaponsmith", type: "minecraft:taiga"}, Offers: {}}
## 召喚コマンド
summon villager ~ ~ ~ {Invulnerable: 1b, NoAI: 1b, CustomName: '[{"text":"[","color":"#FF55FF"},{"text":"再起メッセージ","color":"white"},{"text":"]","color":"#FF55FF"}]', VillagerData: {profession: "minecraft:weaponsmith", type: "minecraft:taiga"}, Offers: {}}
#endregion

#region [if] 条件分岐ゾーン (上から順に条件コマンドの結果が真なら該当のシーンのみが再生されます helpコマンドは常に真を表します)
## !if=シーン１
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run clear @p stone_sword 0
## !if=シーン２
help
#endregion


#region [scene] 会話シーンコマンドゾーン
## !scene=シーン１
execute at @e[type=villager, name="[運営]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#2348eb"}, {"text":" 運営 "}, {"text":">  ","color":"#2348eb"} ,{"text":"皆様、エッグハントお疲れ様でした！","color":"#d5d5f0"}]
execute at @e[type=villager, name="[運営]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#2348eb"}, {"text":" 運営 "}, {"text":">  ","color":"#2348eb"} ,{"text":"集めたたまごを、チームバナーのチェストに納品してくださいませ！","color":"#d5d5f0"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"皆さん、お疲れ様。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"たまごは沢山集まったかな？","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"どれどれ、私も見てみよう。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"……","color":"#d49fc0"}]
execute at @e[type=villager, name="[運営]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#2348eb"}, {"text":" 運営 "}, {"text":">  ","color":"#2348eb"} ,{"text":"では今から集計を行いますので、広場で少々お待ちください！","color":"#d5d5f0"}]

execute at @e[type=villager, name="[システム]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#FFFFFF"}, {"text":" システム "}, {"text":">  ","color":"#FFFFFF"} ,{"text":"運営は各チームの卵を回収してください","color":"#FFFFFF"}]
execute at @e[type=villager, name="[システム]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#FFFFFF"}, {"text":" システム "}, {"text":">  ","color":"#FFFFFF"} ,{"text":"想定時間は２分です","color":"#FFFFFF"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"…………","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"……素晴らしい。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"これだけ集められるなら、きっと……","color":"#d49fc0"}]
execute at @e[type=villager, name="[運営]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#2348eb"}, {"text":" 運営 "}, {"text":">  ","color":"#2348eb"} ,{"text":"皆様、お待たせしました～～！","color":"#d5d5f0"}]
execute at @e[type=villager, name="[運営]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#2348eb"}, {"text":" 運営 "}, {"text":">  ","color":"#2348eb"} ,{"text":"ただいま集計が終わりましたわ！","color":"#d5d5f0"}]
execute at @e[type=villager, name="[運営]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#2348eb"}, {"text":" 運営 "}, {"text":">  ","color":"#2348eb"} ,{"text":"それでは、結果の方を発表していきますわ！","color":"#d5d5f0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"本当に素晴らしいよ、君たち！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[運営]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#2348eb"}, {"text":" 運営 "}, {"text":">  ","color":"#2348eb"} ,{"text":"領主様？","color":"#d5d5f0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"初めてだよ！ これだけ沢山のたまごを集めた人たちは！","color":"#d49fc0"}]

execute at @e[type=villager, name="[運営]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#2348eb"}, {"text":" 運営 "}, {"text":">  ","color":"#2348eb"} ,{"text":"あら、そんなに私達は優秀でしたの？","color":"#d5d5f0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"ああ優秀だ！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"君たちの力があれば、きっと……！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"最高のイースター祭…いや、復活祭になる！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[運営]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#2348eb"}, {"text":" 運営 "}, {"text":">  ","color":"#2348eb"} ,{"text":"一体どういうことかしら？","color":"#d5d5f0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"君たちが集めたたまごはね、私がひとつひとつ丁寧に隠している。","color":"#d49fc0"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"そのたまごに、私はいつもおまじないを込めるんだ。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"賢くて、優秀で、勇敢で、素晴らしい魂を引き込むようにと。","color":"#d49fc0"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"今までこんなに沢山のたまごを集めた者は見たことがないよ。","color":"#d49fc0"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"この素晴らしい日に君たちは、選ばれたんだ。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"高貴なる儀式の…生け贄として","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"Ph’nglui mglw’nafh Cthulhu R’lyeh wgah’nagl fhtagn","color":"#d49fc0"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"Ph’nglui mglw’nafh Cthulhu R’lyeh wgah’nagl fhtagn","color":"#d49fc0"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"Ph’nglui mglw’nafh Cthulhu R’lyeh wgah’nagl fhtagn","color":"#d49fc0"}]

execute at @e[type=villager, name="[運営]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#2348eb"}, {"text":" 運営 "}, {"text":">  ","color":"#2348eb"} ,{"text":"何！？ どうなってるの！？","color":"#d5d5f0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"ああ、本当にありがとう！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"皆さんのお陰で、ようやく、ようやく、私の夢が叶う──！","color":"#d49fc0"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"わかるかい？ この素晴らしく愛おしいたまごが。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"このたまごはね、とある優しい旅人からいただいたんだ。","color":"#d49fc0"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"旅人は言ったんだ。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"この土地は理想の地。沢山の力のこもる土地。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"この地でできないことはない。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"このたまごは奇跡のたまご。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"このたまごで、あれが、愛しいあの子が、復活するのだ……!","color":"#d49fc0"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"ほら、見てくれ！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"命だ！！ 愛しい命だ！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"私の、私だけの宝物だ！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"こんなに愛しいものがあろうか！","color":"#d49fc0"}]
execute at @e[type=villager, name="[？？？]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#574f42"}, {"text":" ？？？ "}, {"text":">  ","color":"#574f42"} ,{"text":"b2tjgatnm4ta5w0ato2trtmsev","color":"#d91b02"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"ああ、ああ、聞いたか！？","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"ドクドクと命の音が鳴っている！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"ははは、まるで産声のようだ！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"いや、産声なんだ！！ 私にはわかる！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"ほら、私に語りかけている！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[？？？]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#574f42"}, {"text":" ？？？ "}, {"text":">  ","color":"#574f42"} ,{"text":"jtdgmjpa8vgk35qjdgdk5","color":"#d91b02"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"ああそうだね、会いたかったよ、私もお前に会いたかった。","color":"#d49fc0"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"ああ、ああ、愛しいお前。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"早く生まれたいよな？ 早く遊びたいよな？","color":"#d49fc0"}]
execute at @e[type=villager, name="[？？？]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#574f42"}, {"text":" ？？？ "}, {"text":">  ","color":"#574f42"} ,{"text":"am4wlg3ujoanpd5jd8omjdt","color":"#d91b02"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"ああそうだ！ お前、生き返っても1人じゃさみしいだろう？","color":"#d49fc0"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"なんせこの街にはもう子供がいないから。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"お前の為にこの辺りの子供はみんな使ってしまったからね。","color":"#d49fc0"}]

execute at @e[type=villager, name="[？？？]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#574f42"}, {"text":" ？？？ "}, {"text":">  ","color":"#574f42"} ,{"text":"ajapjg8gekivmtjg5ld8lgd5mq5mtamt","color":"#d91b02"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"そうだ…せっかくならお前の友達も生き返らせよう！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"だって、生贄はこんなにいるのだから！","color":"#d49fc0"}]
execute at @e[type=villager, name="[？？？]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#574f42"}, {"text":" ？？？ "}, {"text":">  ","color":"#574f42"} ,{"text":"jjawojkisg5jwvmpatmgnt6tdagdk3ptamjpd","color":"#d91b02"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"大丈夫だとも、私が叶えてやるさ。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"お前の為なら、私は何だってやってやる……！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"――では、始めようか。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"お前の為の儀式を。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"お前が孵る為の儀式を。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"ここにいる沢山の、優秀な、生贄によって！！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[再起メッセージ]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#FF55FF"}, {"text":" 再起メッセージ "}, {"text":">  ","color":"#FF55FF"} ,{"text":"9時10分にサーバーが再起動されます。安置に移動してログアウトしてください。","color":"#FF55FF"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"……？ 何か別の声も聞こえるな……","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"再起…？ 何の話だ？","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"そもそもこの声は何だ？","color":"#d49fc0"}]
execute at @e[type=villager, name="[運営]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#2348eb"}, {"text":" 運営 "}, {"text":">  ","color":"#2348eb"} ,{"text":"皆様、再起動のアナウンスです。ログアウトをお願いします。","color":"#d5d5f0"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"ああそうか、再起、つまり復活のことか？","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"はははは！！ なるほど、そういうことか！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"私は間違ってなんかいなかった！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"君たちは特別なんだ！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"私を救うためにきてくれたんだろう！？","color":"#d49fc0"}]
execute at @e[type=villager, name="[再起メッセージ]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#FF55FF"}, {"text":" 再起メッセージ "}, {"text":">  ","color":"#FF55FF"} ,{"text":"9時10分にサーバーが再起動されます。安置に移動してログアウトしてください。","color":"#FF55FF"}]

execute at @e[type=villager, name="[システム]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#FFFFFF"}, {"text":" システム "}, {"text":">  ","color":"#FFFFFF"} ,{"text":"運営の退出メッセージ","color":"#FFFFFF"}]
execute at @e[type=villager, name="[運営]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#2348eb"}, {"text":" 運営 "}, {"text":">  ","color":"#2348eb"} ,{"text":"皆様、再起動のアナウンスです。ログアウトをお願いします。","color":"#d5d5f0"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"何、何だ……？ 生贄が消えていく……？","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"一体何が起きているんだ？","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"なあ、お前、もしかしてお前が喋っているのか？","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"なあ、さっきみたいに話しておくれよ。","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"なあ、お前の声を聞かせておくれ！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[再起メッセージ]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#FF55FF"}, {"text":" 再起メッセージ "}, {"text":">  ","color":"#FF55FF"} ,{"text":"9時10分にサーバーが再起動されます。安置に移動してログアウトしてください。","color":"#FF55FF"}]

execute at @e[type=villager, name="[システム]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#FFFFFF"}, {"text":" システム "}, {"text":">  ","color":"#FFFFFF"} ,{"text":"運営の退出メッセージ","color":"#FFFFFF"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"一体どういうことなんだ！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"あと少し！！ あと少しで上手くいったのに！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"お前は誰だ！！ お前が生贄を消しているのか！！","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"くそっ……！！ どうして、どうして上手くいかないんだ……！！","color":"#d49fc0"}]

execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"！？……何だ、このたまごは……！？","color":"#d49fc0"}]
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"こんなたまご、見たことがない……一体これは……？","color":"#d49fc0"}]
execute at @e[type=villager, name="[システム]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#FFFFFF"}, {"text":" システム "}, {"text":">  ","color":"#FFFFFF"} ,{"text":"運営はイベントワールドに残っているプレイヤーをkickしてください","color":"#FFFFFF"}]

## !scene=シーン２
execute at @e[type=villager, name="[領主]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#c71585"}, {"text":" 領主 "}, {"text":">  ","color":"#c71585"} ,{"text":"まだ飯食ってるからまってくれない？","color":"#d49fc0"}]
execute at @e[type=villager, name="[？？？]", distance=0.., limit=1] run tellraw @a[distance=..10] ["", {"text":"<","color":"#574f42"}, {"text":" ？？？ "}, {"text":">  ","color":"#574f42"} ,{"text":"...","color":"#d91b02"}]
#endregion

