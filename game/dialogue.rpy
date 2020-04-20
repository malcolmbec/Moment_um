label dialogue:
    ## Scene 1 #################################################################
    play music "audio/smol_theme.mp3" fadeout 1.0 fadein 1.0
    scene bg bar with dissolve
    show cat sad_animated at behind_bar_left_cat
    show smol normal at behind_bar_right_smol
    show bar

    "You walk up to the mouse and attempt to greet them."
    s"You’re a cat!"
    show smol anger at behind_bar_right_smol_anger
    s"Why is a cat here?"

    ## Menu 1
    show cat sad

    menu:
        "\"Well, I thought it seemed like a cool shop.\"":
            jump opt1_1
        "\"Do you have any drink recommendations?\"":
            jump opt1_2
        "\"I’m trying to make friends.\" ":
            jump opt1_3
    label opt1_1:
        show smol anger_animated
        c"Well, I thought it seemed like a cool shop."
        s"Seems pretty fishy."
        c"I don’t know what you mean."
        s"Well… you’re a cat,{w} and most of us are mice."
        s"Really, you should just leave."
        jump end1
    label opt1_2:
        show smol anger_animated at behind_bar_right_smol_anger
        c"Do you have any drink recommendations?"
        s"Why do you want a drink recommendation from me?"
        c"I thought maybe you came here often."
        s"Because I’m a mouse?!"
        show cat nani at behind_bar_left_cat
        c"Oh, um, no! I just meant…"
        jump end1
    label opt1_3:
        c"I’m trying to make friends."
        show smol anger_animated at behind_bar_right_smol_anger
        s"But you’re a cat,{w} why would you try to make friends here?{w} Seems like you don’t belong here."
        c"Erm, I think maybe we could all learn to be friends?"
        s"Or maybe you’re hiding something!"
        show cat shock
        c"Uh, what?{w} No!"
        jump end1
    label end1:

    show cat blink
    "Seems like befriending this mouse will be harder than you expected.{w} What should you say next?"

    ## Menu 2
    menu:
        "Ask if they’re a regular.":
            jump opt2_1
        "Ask about the usual regulars at the cafe.":
            jump opt2_2
    label opt2_1:
        show cat sad
        c"Are you here often?"
        s"What’s it to you?"
        c"You seem like you know this place well."
        s"So?"
        c"Uh…"
        s"Leave before I fight you!"
        show cat ugh
        "Oh that’s not good, maybe you should try something else."
        ## Submenu 2
        menu:
            "Ask something different.":
                jump opt2_2
            "Maybe it’s best if I talk to someone else...":
                jump end3
    label opt2_2:
        show cat sad
        c"I’ve never been here before, but they seem busy."
        s"You seem too interested in the patrons."
        show cat suprise
        c"What, no, why?"
        show cat sad
        s"You’re a cat, maybe you’re up to something."
        c"I’m just trying to make some friends..."
        jump end2
    label end2:

    show cat ugh
    "Tensions are high, let’s change the topic all together."
    show cat sad
    c"Do you drink a lot of coffee?"
    show smol meh at behind_bar_right_smol_anger
    s"I come here for black coffee a lot"
    show cat nani
    c"Um, isn’t that bitter?"
    show cat sad
    s"The only thing bitter around here is me."
    c"..."
    "Hm, well I guess they’re straight forward at least.{w} How should you respond?"

    ## Menu 3
    menu:
        "\"I’ll try the black coffee then.\"":
            jump opt3_1
        "\"I’m not really a coffee drinker myself.\"":
            jump opt3_2
        "\"Are you okay?\"":
            jump opt3_3
    label opt3_1:
        show cat sad at behind_bar_left_cat
        c"I’ll try the black coffee then."
        show smol meh at behind_bar_right_smol_pull
        s"Wait, seriously? You’ll try even though you think it’s bitter?"
        c"Hm. Maybe I should suggest something you’d definitely enjoy then."
        "Seems the small mouse might be opening up!{w} Maybe you can be friends after all."
        jump end3
    label opt3_2:
        c"I’m not really a coffee drinker myself."
        show smol pfff at behind_bar_right_smol_anger
        s"Why would you come here then?"
        show cat ugh
        c"Well I mean, um, most cafes have other things too."
        show smol anger_animated at behind_bar_right_smol_anger
        s"That makes no sense, it’s a coffee shop, if you’re not going to drink coffee, you should leave."
        ## Submenu 3
        menu:
            "Maybe you should try the coffee?":
                jump opt3_1
            "Might be best to regroup with the bartender and try talking to someone else...":
                jump end3
    label opt3_3:
        c"Are you okay?"
        show smol pull_animated at behind_bar_right_smol_pull
        s"You’re right, I don’t even like coffee."
        c"Why are you drinking it then?"
        s"Because I thought the caffeine would help me."
        show cat wink
        c"Let’s try something new together instead."
        s"I can’t believe you’re being nice to me after all the mean things I’ve said."
        show cat happy
        "See, all the mouse needed was a friend."
        python:
            smol_friend = True
        jump end3
    label end3:

    if smol_friend:
        "You befriended Smol Mouse!"
    else:
        show cat ugh at behind_bar_left_cat
        "You did not make friends with Smol Mouse. :("

    ## Scene 2 #################################################################
    play music "audio/ratdee_theme.mp3" fadeout 1.0 fadein 1.0
    scene bg bar with dissolve
    show cat sad_animated at behind_bar_left_cat
    show ratdee normal at behind_bar_right_rat
    show bar

    r "Aye! I’m RatyDee, mice to meet you! Could I interest you in a friendly pun off?"

    ## Menu 4
    menu:
        "Accept challenge.":
            jump opt4_1
        "Decline.":
            jump opt4_2
    label opt4_1:
        python:
            score = 0;
        r "Awesome! Let the pun off begin!"
        r "Are you Ready?"
        centered "{b}{size=50}{color=#c8ae6e}Round 1{/color}{/size}{/b}"
        r "You, my friend, look like something the cat dragged in."
        python:
            score -= 1

        ## Submenu 4a
        menu:
            "\"You've cat to be kitten me right meow.\"":
                jump opt4a_1
            "\"You should paw-se before saying that.\"":
                jump opt4a_2
            "\"I couldn’t drag myself in.\" ":
                jump opt4a_3
        label opt4a_1:
            c"You've cat to be kitten me right meow."
            python:
                score += 3
            r "Aw, rats. Good comeback."
            jump end4a
        label opt4a_2:
            c"You should paw-se before saying that."
            python:
                score += 1
            r "Quit tea-sing."
            jump end4a
        label opt4a_3:
            c"I couldn’t drag myself in."
            r "Try again pipsqueak."
            jump end4a
        label end4a:

        centered "{b}{size=50}{color=#c8ae6e}Round 2{/color}{/size}{/b}"
        r "How are you feline?"
        python:
            score -= 1

        ## Submenu 4b
        menu:
            "\"Purrty good!\"":
                jump opt4b_1
            "\"Kind of low.\"":
                jump opt4b_2
            "\"Feline fine!\" ":
                jump opt4b_3
        label opt4b_1:
            c"Purrty good!"
            python:
                score += 1
            r "It’s good cats always land on their feet!"
            jump end4b
        label opt4b_2:
            c"Kind of low."
            r "I’m afraid that joke fell flat."
            jump end4b
        label opt4b_3:
            c"Feline fine!"
            python:
                score += 1
            r "Don’t be a cheetah."
            jump end4b
        label end4b:

        centered "{b}{size=50}{color=#c8ae6e}Round 3{/color}{/size}{/b}"

        r "You know I’m quite famous for always mousin’ around."
        python:
            score -= 1

        ## Submenu 4c
        menu:
            "\"I bet your very paw-pular with your puns.\"":
                jump opt4c_1
            "\"You’re hiss-terical!\"":
                jump opt4c_2
            "\"Is that so?\" ":
                jump opt4c_3
        label opt4c_1:
            c"I bet your very paw-pular with your puns."
            python:
                score += 1
            r "Cat's out of the bag."
            jump end4c
        label opt4c_2:
            c"You’re hiss-terical!"
            python:
                score += 1
            r "Cat's out of the bag."
            jump end4c
        label opt4c_3:
            c"Is that so?"
            r "Seems you’re having treble coming up with something."
            jump end4c
        label end4c:

        if score <= 0:
            centered "{b}{size=50}{color=#c8ae6e}You Lose{/color}{/size}{/b}"
            r "Don't get your tail in a twist, it was still a great game!{w} Let’s play again sometime!"
        else:
            centered "{b}{size=50}{color=#c8ae6e}You Win!{/color}{/size}{/b}"
            r "You’re really rat-ical. A purrfect pun off!"
        python:
            ratdee_friend = True
        jump end4
    label opt4_2:
        jump end4
    label end4:

    if ratdee_friend:
        "You befriended RatyDee!"
    else:
        show cat ugh at behind_bar_left_cat
        "You did not make friends with RatyDee. :("

    if smol_friend and ratdee_friend:
        show cat happy_animated at behind_bar_left_cat
        "Wow, you've got a bunch of new friends!"
    elif smol_friend or ratdee_friend:
        "Well, at least we have one new friend..."
    else:
        "This really isn't your day..."

    jump endscene
