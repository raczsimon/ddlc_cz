init python:
    config.language = "Japanese"

pass







translate Japanese style _default:
    font "gui/font/MTLc3m.ttf"

translate Japanese style edited:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style poemgame_text:
    font "gui/font/Mikachan.ttf"

translate Japanese style navigation_button_text:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style game_menu_label_text:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style pref_label_text:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style check_button_text:
    font "gui/font/Mikachan.ttf"

translate Japanese style radio_button_text:
    font "gui/font/Mikachan.ttf"

translate Japanese strings:
    old "History"
    new "Historie"

    old "Skip"
    new "Přeskočit"

    old "Auto"
    new "Automaticky"

    old "Save"
    new "Uložit"

    old "Load"
    new "Nahrát"

    old "Settings"
    new "Nastavení"

    old "??n??≫?t?A????i≪"
    new "??n??≫?t?A????i≪"

    old "New Game"
    new "Nová hra"

    old "Save Game"
    new "Uložit hru"

    old "Load Game"
    new "Pokračovat"

    old "End Replay"
    new "Ukončit replay"

    old "Main Menu"
    new "Hlavní menu"

    old "Help"
    new "Pomoc"

    old "Quit"
    new "Ukončit"

    old "Return"
    new "Vrátit se"

    old "About"
    new "O hře"

    old "Version [config.version!t]\n"
    new "Verze [config.version!t]\n"

    old "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"
    new "Vytvořeno pomocí {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"

    old "{#file_time}%A, %B %d %Y, %H:%M"
    new "{#file_time}%B %d %Y, %H:%M"

    old "empty slot"
    new "prázdný slot"

    old "Display"
    new "Zobrazení"

    old "Window"
    new "Okno"

    old "Fullscreen"
    new "Fullscreen"

    old "Rollback Side"
    new "ロールバック\nサイド"

    old "Disable"
    new "Nepovolit"

    old "Left"
    new "Vlevo"

    old "Right"
    new "Napravo"

    old "Unseen Text"
    new "Nepřečtený text"

    old "After Choices"
    new "Po volbě"

    old "Text Speed"
    new "Rychlost textu"

    old "Auto-Forward Time"
    new "Prodlení v automatickém režimu"

    old "Music Volume"
    new "Hlasitost hudby"

    old "Sound Volume"
    new "Hlasitost zvuků"

    old "Test"
    new "Test"

    old "Voice Volume"
    new "Hlasitost hlasů"

    old "Mute All"
    new "Vypnout zvuk"

    old "The dialogue history is empty."
    new "Historie dialogů je prázdná."

    old "OK"
    new "OK"

    old "Yes"
    new "Ano"

    old "No"
    new "Ne"

    old "Skipping"
    new "Přeskakuji"

    old "Please enter your name"
    new "Vyplň svoje jméno"

    old "The help file has been opened in your browser."
    new "Pomocný soubor byl otevřen ve vašem prohlížeči."

    old "File error: \"characters/sayori.chr\"\n\nThe file is missing or corrupt."
    new "File error: Soubor \"characters/sayori.chr\"\n\n nebyl nalezen, nebo je poškozen."

    old "The save file is corrupt. Starting a new game."
    new "Soubor s vaší předchozí hrou byl poškozen. Začněte novou hru."

    old "There's no point in saving anymore.\nDon't worry, I'm not going anywhere."
    new "Už nemá cenu nic ukládat.\nNeboj se, já ti nikam neuteču."

translate Japanese screen:
    screen name_input(message, ok_action):
        modal True
        zorder 200
        style_prefix "confirm"
        add "gui/overlay/confirm.png"
        key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]
        frame:
            has vbox:
                xalign .5
                yalign .5
                spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            input default "" value VariableInputValue("player") length 12 pixel_width 168
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("OK") action ok_action
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
