translate Japanese label:
    label ch5_main:
        stop music fadeout 2.0
        scene bg residential_day
        with dissolve_scene_full
        "今日はとうとう文化祭の日だ。"
        "今日こそはサヨリと一緒に学校に登校できるだろうと思っていた。"
        "しかし、サヨリは電話には出ない。"
        "俺はサヨリを起こしに彼女の家に行くことも考えたが、それは少しやりすぎかと思ったので遠慮した。"
        "一方、文化祭の準備はほとんど出来ている。"
        if ch4_scene == "natsuki":
            "なんとかトレーを重ねて慎重に運び、一人で全てのカップケーキを運ぶ。"
            "ナツキからは何件もメッセージが届いているが、両手がふさがっていて返信できない。"
        else:
            "俺は昨日ユリと描いた横幕を丁寧に丸めて持って来た。"
            "彼女から何も忘れないように、と丁寧なメッセージが届いたので大丈夫だ、と送り返した。"
        "おかしなことに、俺はもしかすると文化祭についてナツキと同じ事を考えているのかもしれない。"
        "どちらかと言えば、さっさと文芸部の方を終わらせてサヨリや[ch4_name!t]と一緒に文化祭を楽しみたいのだ。"
        "まあモニカのことだから、きっと文芸部の出し物も良いものなんだろうけど。"
        scene bg club_day with wipeleft_scene
        show monika 5 zorder 2 at t11
        m "「[player]君！」"
        m "「あなたが一番乗りなのね」"
        m "「早めに来てくれて嬉しいわ！」"
        mc "「変だな、少なくともユリはもう来てると思ってたんだが」"
        "モニカは小冊子を教室の机1つ1つの上に並べている。"
        "おそらく俺たちが発表する詩が載っているのだろう。"
        "結局、俺はモニカが好きそうな詩を適当にネットから見つけてきて、それを提出した。"
        "だから俺はそれを発表することになっている。"
        m 1d "「サヨリと一緒に来ると思ってたんだけど意外ね」"
        mc "「ああ、あいつまた寝坊しちまって」"
        mc "「なにやってるんだか」"
        mc "「今日は大事な文化祭の日なんだし、ちょっとは頑張ると思ったんだけどなあ……」"
        "そう口に出してすぐ、サヨリが昨日言っていたことを思い出した。"
        "そして彼女にとってはそう単純な問題ではないことに気づき、ひどい罪悪感に苛まれる。"
        "俺はただいつもそういう風に捉えていたからそう発言してしまったのだ。"
        "でも……"
        "もしかしたら起こしに行った方が良かったのだろうか？"
        m 1k "「ふふっ」"
        m 4b "「[player]君はもうちょっと責任を持った方がいいかもしれないわ！」"
        m "「昨日あんなやり取りも交わしたばかりのに……」"
        m "「今朝まであの子を宙ぶらりんにさせちゃって」"
        show monika 4a
        mc "「やり取り……？」"
        mc "「モニカ――まさかお前知ってるのか？」"
        m 2a "「もちろんよ！」"
        m "「なんてったってこの文芸部の部長なんだから」"
        mc "「で、でも――！」"
        "恥ずかしくなって、言葉に詰まってしまう。"
        "サヨリはもうモニカに言ったのか？"
        if sayori_confess:
            "俺たちが付き合い始めたことを……？"
            "俺はまだ、誰にも言うつもりなんか無かったのに……"
        else:
            "どうやって彼女を振ったのかも？"
            "そうだとしたら俺はかなり悪い立場にいることになる。"
            "でもあいつにとって何が最善は俺が一番知っているはずだ。"
        mc "「えっと……」"
        mc "「それでも全部知ってるわけじゃないよな、なら……」"
        m 2j "「心配しないで」"
        m "「あなたが思ってるより色々知ってるのよ？私」"
        mc "「えっ……？」"
        "いつものように気さくなモニカだが、その言葉を聞いて何故か背筋が寒くなった。"
        m 5 "「ねえ、パンフレット確認しない？」"
        m "「とってもいい感じに仕上がったから！」"
        mc "「ああ、そうするよ」"
        "机にある小冊子を一部取る。"
        mc "「ほんとだ、いい感じだ」"
        mc "「これなら、みんなもっとこの部活のことを真剣に見てくれるだろうな」"
        m "「ええ、私もそう思うわ！」"
        show monika zorder 1 at thide
        hide monika
        "ページをぱらぱらとめくっていく。"
        "それぞれのメンバーの詩が、まるでプロの仕事のような鮮やかさで印刷されている。"
        "ナツキとユリの詩は、二人が練習の時に読んだものと同じみたいだ。"
        mc "「ん？ なんだこれ……」"
        "俺はサヨリのページを開いた。"
        "そこには彼女が練習で読んでいたものとは違う詩が載っていた。"
        "それに俺が今まで読んだことのない……"
        call showpoem (poem_s3, music=False)
        mc "「なっ――」"
        "これは何だ……？"
        "この詩を読むと、とても胸がざわつく。"
        show monika 1d zorder 2 at t11
        m "「[player]君？」"
        m "「どうかしたの？」"
        mc "「いや、なんでも……」"
        "この詩はどう考えても、いつものサヨリの詩と何もかも違っている。"
        "だが、それよりも……"
        mc "「ご、ごめん、ちょっと気が変わった」"
        mc "「やっぱりサヨリのこと迎えに行ってくるから……」"
        m "「あー……」"
        m 1b "「分かったわ」"
        m "「あんまり遅くならないでね？」"
        scene bg corridor with wipeleft
        "俺は急いで教室から出た。"
        m "「無理しないでね～」"
        "モニカが呼びかけるのが聞こえる。"
        "どんどんペースを上げていく。"
        scene bg residential_day with wipeleft_scene
        "俺は何を考えていたんだ？"
        "もう少しサヨリのために頑張るべきだった。"
        "彼女を待つことや、朝起こしてやることなんて簡単なことじゃないか。"
        "単に一緒に学校に行くだけでもサヨリは幸せになるのに。"
        "しかも……"
        "俺はつい昨日、いつも通りの日常を共に過ごすとあいつに言ったばかりじゃないか。"
        "彼女にはそれが必要で、俺もそうしてやりたかった。"
        scene bg house with wipeleft
        "俺はサヨリの家に着いて、ドアをノックした。"
        "電話にも出ていないから、返事がないのも当然だろう。"
        "昨日のようにドアを開けて入った。"
        scene black with wipeleft
        mc "「サヨリ？」"
        "あいつ、本当にぐっすり寝てるな……"
        "唾を飲む。"
        "こんな事をしている自分が信じられない。"
        "彼女の家に上がり込んで起こすとか……"
        if sayori_confess:
            "そんなのまさに彼氏のすることじゃないか。"
        else:
            "彼氏がするようなことじゃないか……？"
        "なんにせよ……"
        "これが正しいと思う。"
        "サヨリの部屋の前に着いた俺はドアをノックした。"
        mc "「サヨリ？」"
        mc "「早く起きろよ、ねぼすけ」"
        "反応は無い。"
        "こんな感じで彼女の部屋には入りたくなかったんだが……"
        "なんだか、プライバシーの侵害みたいじゃないか？"
        "でも他に選択はない。"
        "俺はゆっくりとドアを開ける。"
        mc "{cps=30}……サヨ{/cps}{nw}"
        $ persistent.playthrough = 1
        $ persistent.anticheat = renpy.random.randint(100000, 999999)
        $ delete_character("sayori")
        $ in_sayori_kill = True
        window hide(None)
        window auto
        play music td
        show s_kill_bg2
        show s_kill2
        show s_kill_bg as s_kill_bg at s_kill_bg_start
        show s_kill as s_kill at s_kill_start
        pause 3.75
        show s_kill_bg2 as s_kill_bg
        show s_kill2 as s_kill
        pause 0.01
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        hide s_kill_bg
        hide s_kill
        show s_kill_bg_zoom zorder 1
        show s_kill_bg2_zoom zorder 1
        show s_kill_zoom zorder 3
        show s_kill2_zoom zorder 3
        show s_kill as s_kill_zoom_trans zorder 3:
            truecenter
            alpha 0.5
            zoom 2.0 xalign 0.5 yalign 0.05
            pause 0.5
            dizzy(1, 1.0)
        pause 2.0
        show noise zorder 3:
            alpha 0.0
            linear 3.0 alpha 0.25
        show vignette zorder 3:
            alpha 0.0
            linear 3.0 alpha 0.75
        pause 1.5
        show white zorder 2
        show splash_glitch zorder 2
        pause 1.5
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.2
        stop sound
        hide screen tear
        pause 4.0
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.2
        stop sound
        hide screen tear
        hide splash_glitch
        show splash_glitch2 zorder 2
        show splash_glitch_m zorder 2
        show splash_glitch_n zorder 2
        show splash_glitch_y zorder 2
        pause 0.75
        hide white
        hide splash_glitch2
        hide splash_glitch_m
        hide splash_glitch_n
        hide splash_glitch_y
        show exception_bg zorder 2
        show fake_exception zorder 2:
            xpos 0.1 ypos 0.05
        show fake_exception2 zorder 2:
            xpos 0.1 ypos 0.15
        python:
            try: sys.modules['renpy.error'].report_exception("あらまあ……何か壊れちゃったりしたかしら？ちょっと待って、これなら多分……直せそう……\nでもこれって、あの子を削除した方がよっぽど簡単じゃない？ややこしい事態にしたのはあの子なんだし。あははっ！それじゃあ、ちょっと試してみましょうか。", False)
            except: pass
        pause 6.0
        "……"
        hide fake_exception
        hide fake_exception2
        hide exception_bg
        "なんだよこれ……？"
        "{i}なんなんだよこれ？？{/i}"
        "これは悪夢なのか？"
        "そうに……そうに違いない。"
        "こんなの現実じゃない。"
        "こんなこと現実のはずがない。"
        "サヨリがこんなことするわけない。"
        "ほんの数日前まで、何もかもいつも通りだったじゃないか。"
        "だからこそ、今目の前に広がってる光景が信じられない。"
        scene black with dissolve_cg
        "吐きそうになるのを必死に堪える。"
        "つい昨日……"
        "ずっと傍にいてやるって言ったばかりなのに。"
        "サヨリの望みはわかってるから何も問題ないって言ったばかりなのに。"
        "だったら何で……？"
        "何であいつはこんなことを……？"
        "なんて俺は無力なんだ？"
        "俺は何を間違えたんだ？"
        if sayori_confess:
            "あいつに告白したこと……か？"
            "俺は告白なんてするべきじゃなかったんだ。"
            "あいつはそんなこと望んでなかった……"
            "他人から気にかけられる事がどれだけ苦しいか言ってたじゃないか！"
            "じゃあなんで俺は、告白なんかしてあいつの心をさらに傷つけてしまったんだ？"
        else:
            "告白を受け入れなかったこと……"
            "それがあいつの心を壊してしまったのかもしれない。"
            "彼女の苦悶の叫びがいまだに耳の中に残る。"
            "なんでサヨリは俺を最も必要としてくれたのにあんな事をしたんだ？"
        "なんて俺は自分勝手だったんだ。"
        "全部俺のせいじゃないか……！"
        "どうすればこんなことにならなかったのか、頭の中で飛び交ってる考えがずっと俺の中で共鳴している。"
        "もし、もっと一緒に過ごしていたら。"
        "一緒に学校に行っていれば。"
        if sayori_confess:
            "そして、今までのようにあいつと友達のままだったら……"
        else:
            "そして、あいつが今までの関係から期待していたことをしてあげられたなら。"
        "……そうすればこんなことには……"
        "こんなことにはならなかったはずだ！"
        "文芸部なんてもう知るか。"
        "文化祭なんてもう知るか。"
        "俺は今、一番の友達を失ったんだ。"
        "小さいころからずっと一緒だった友達を。"
        "サヨリは死んでしまったんだ。"
        "あいつを取り戻す方法なんて何もない。"
        "ゲームじゃないからリセットしてやり直すなんてこともできやしないんだ。"
        "たった一度しかないチャンスだったのに、うかつだったんだ。"
        "そして死ぬまでこの罪を背負っていくんだ。"
        "俺の人生でサヨリより価値のあるものなんて無かった……"
        "でもあいつがして欲しかったことができなかった。"
        "そして今……"
        "もう取り戻すことはできない。"
        "絶対に。"
        "絶対に。"
        "絶対に。"
        "絶対に。"
        "絶対に……"
        $ in_sayori_kill = False
        return

translate Japanese image:
    image fake_exception:
        Text("例外が発生しました。", size=40, style="_default")

    image fake_exception2:
        Text("ファイル \"game/script-ch5.rpy\"、307行\n詳しくはtraceback.txt を確認してください。", size=20, style="_default")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
