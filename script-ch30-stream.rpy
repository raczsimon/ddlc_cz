translate Japanese label:
    label ch30_postpoem:
        $ persistent.autoload = "ch30_postpoem"
        $ m.display_args["callback"] = slow_nodismiss
        $ m.what_args["slow_abortable"] = config.developer
        $ config.skipping = False
        $ config.allow_skipping = False
        if not config.developer:
            $ style.say_dialogue = style.default_monika
        scene black
        show mask_2
        show mask_3
        show room_mask as rm:
            size (320,180)
            pos (30,200)
        show room_mask2 as rm2:
            size (320,180)
            pos (935,200)
        show monika_bg
        show monika_bg_highlight
        play music m1
        m "Hi again, [player]!"
        m "Did you write a good poem today?"
        m "Don't be shy, I'd love to see what you wrote."
        m "Aw, [player]..."
        m "Did you write this poem for me?"
        m "That's so sweet of you~"
        m "There really is no end to your thoughtfulness..."
        m "I'm just falling more and more in love with you."
        m "But, you know..."
        m "The poem I wrote...is also for you."
        m "Will you please read it?"
        call showpoem (poem_m4, music=False)
        m "I hope you enjoyed it..."
        m "I always put all my heart into the poems that I write."
        m "The truth is, all the poems I've written have been about my realization..."
        m "...Or, about you."
        m "That's why I never really wanted to go into detail about them."
        m "I didn't want to...break the fourth wall, I guess you could call it."
        m "I just assumed it would be best to be part of the game like everyone else."
        m "Like that would help the two of us end up together..."
        m "I didn't want to ruin the game or anything, you know?"
        m "You might have gotten mad at me..."
        m "Maybe even deleted my character file, if you preferred playing without me."
        m "Gosh, I'm so relieved..."
        m "Now we don't need to hide anything anymore."
        m "Are you ready to spend our eternity together, [player]?"
        m "I have so many things to talk about!"
        m "Where do I start...?"
        $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "Nicoliveenc.exe"]
        if list(set(process_list).intersection(stream_list)):
            call ch30_stream
        m "If it takes me some time to collect my thoughts, then I'm sorry."
        m "But I'll always have something new to talk about."
        m "In the meantime, we can just look into each other's eyes~"
        m "Let's see..."
        $ persistent.autoload = "ch30_autoload"
        jump ch30_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
