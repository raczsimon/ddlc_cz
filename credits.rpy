translate Japanese strings:
    old "Concept & Game Design"
    new "構想 & デザイン"

    old "Character Art"
    new "キャラクターデザイン"

    old "Background Art"
    new "背景画"

    old "Writing"
    new "脚本"

    old "Music"
    new "音楽"

    old "Vocals"
    new "歌"

    old "Special Thanks"
    new "スペシャルサンクス"

    old "Error: Script file is missing or corrupt.\nPlease reinstall the game."
    new "エラー: スクリプトファイルが見つからないか破損しています。\nゲームを再インストールして下さい。"

image mcredits_1a_tl:
    ypos credits_ypos_tl
    xoffset -340
    "black"
    10.33
    Text("毎日", style="monika_credits_text_tl") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_1b_tl:
    ypos credits_ypos_tl
    xoffset -55
    "black"
    11.75
    Text("あなたと一緒にいられる", style="monika_credits_text_tl") with ImageDissolve("images/menu/wipeleft.png", 5.0, ramplen=4, alpha=False)
image mcredits_1c_tl:
    ypos credits_ypos_tl
    xoffset 290
    "black"
    13.76
    Text("未来を思う", style="monika_credits_text_tl") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_2a_tl:
    ypos credits_ypos_tl + 50
    xoffset -270
    "black"
    19.45
    Text("私の手には", style="monika_credits_text_tl") with ImageDissolve("images/menu/wipeleft.png", 8.0, ramplen=4, alpha=False)
image mcredits_2b_tl:
    ypos credits_ypos_tl + 50
    xoffset -20
    "black"
    20.9
    Text("あなたと私の", style="monika_credits_text_tl") with ImageDissolve("images/menu/wipeleft.png", 12.0, ramplen=4, alpha=False)
image mcredits_2c_tl:
    ypos credits_ypos_tl + 50
    xoffset 255
    "black"
    23.27
    Text("詩を書くペン", style="monika_credits_text_tl") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_3_tl:
    ypos credits_ypos_tl + 100
    "black"
    28.35
    Text("インクが流れ落ちて暗い水たまりになる", style="monika_credits_text_tl") with ImageDissolve("images/menu/wipeleft.png", 6.5, ramplen=4, alpha=False)
image mcredits_4_tl:
    ypos credits_ypos_tl + 150
    xoffset -5
    "black"
    32.9
    Text("ただ手を動かして――彼の心へ書き進もう！", style="monika_credits_text_tl") with ImageDissolve("images/menu/wipeleft.png", 5.0, ramplen=4, alpha=False)
image mcredits_5_tl:
    ypos credits_ypos_tl + 200
    "black"
    37.5
    Text("でも無限の選択肢が連なるこの世界で", style="monika_credits_text_tl") with ImageDissolve("images/menu/wipeleft.png", 6.5, ramplen=4, alpha=False)
image mcredits_6a_tl:
    ypos credits_ypos_tl + 250
    xoffset -235
    "black"
    42.0
    Text("何をすれば", style="monika_credits_text_tl") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_6b_tl:
    ypos credits_ypos_tl + 250
    xoffset 115
    "black"
    43.47
    Text("特別な日は見つかるの？", style="monika_credits_text_tl") with ImageDissolve("images/menu/wipeleft.png", 6.0, ramplen=4, alpha=False)

image subtitles:
    ypos 680
    xoffset -25
    "null.png"
    9.3
    Text("聞こえる……？",style="normal") with Dissolve( 0.5 ,alpha= True)
    1.8
    "null.png" with Dissolve( 0.5 ,alpha= True)
    1.9
    Text("やっほー、私よ",style="normal") with Dissolve( 0.5 ,alpha= True)
    1.8
    "null.png" with Dissolve( 0.5 ,alpha= True)
    1.7
    Text("えっと……私がピアノを練習したりしてたのは知ってるでしょ？",style="normal") with Dissolve( 0.5 ,alpha= True)
    4.4
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("まぁ……まだ全然上手くないんだけど、ほんとに、全然",style="normal") with Dissolve( 0.5 ,alpha= True)
    4.3
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("でもあなたのために歌を作ったから",style="normal") with Dissolve( 0.5 ,alpha= True)
    2.2
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("できれば聞いてもらえたらって思って",style="normal") with Dissolve( 0.5 ,alpha= True)
    2.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("すっごく……すっごく頑張って作ったから",style="normal") with Dissolve( 0.5 ,alpha= True)
    3.2
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("だから……ね！",style="normal") with Dissolve( 0.5 ,alpha= True)
    1.8
    "null.png" with Dissolve( 0.5 ,alpha= True)

image lyrics:
    ypos 650
    xoffset -25
    "null.png"
    9.5
    Text("Have I found everybody a fun assignment to do today?",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    5.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    3.5
    Text("When you're here, everything that we do is fun for them anyway",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    5.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    3.5
    Text("When I can't even read my own feelings",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("What good are words when a smile says it all?",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("And if this world won't write me an ending",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("What will it take just for me to have it all?",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    19.5
    Text("Does my pen only write bitter words for those who are dear to me?",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    5.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    4.0
    Text("Is it love if I take you, or is it love if I set you free?",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    5.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    8.0
    Text("The ink flows down into a dark puddle",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("How can I write love into reality?",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    3.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("If I can't hear the sound of your heartbeat",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("What do you call love in your reality?",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    3.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("And in your reality, if I don't know how to love you",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    5.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    3.5
    Text("I'll leave you be",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    2.0
    "null.png" with Dissolve( 0.5 ,alpha= True)

image lyrics_tl:
    ypos 680
    xoffset -25
    "null.png"
    9.5
    Text("今日はみんなが楽しめる課題を見つけられたかな？",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    5.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    3.5
    Text("君がいると、みんなは何をしても楽しむけれど",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    5.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    3.5
    Text("自分の気持ちすら読めない時に",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("笑顔で全て語れるなら、言葉は何の役に立つの？",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("そして私にエンディングを書いてくれないこの世界で",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("何をすれば全てが手に入れられるの？",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    19.5
    Text("私のペンは大切な人たちへ辛辣な言葉しか書かないの？",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    5.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    4.0
    Text("あなたを捕まえるのと自由にするのとでは、どちらが愛なの？",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    5.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    8.0
    Text("インクが流れ落ちて暗い水たまりになる",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("どうすれば愛を現実に書けるの？",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    3.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("鼓動が聞こえないのなら",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("あなたの現実では何を愛と呼ぶの？",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    3.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("あなたの現実で、愛し方が分からないのなら",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    5.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    3.5
    Text("あなたをそのままにする",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    2.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
