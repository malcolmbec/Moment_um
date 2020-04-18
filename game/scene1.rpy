label scene1:
    show bartender friendly at right
    b"Now we have some options!"

    menu:
        "Option 1":
            jump opt1
        "Option 2":
            jump opt2
        "Option 3":
            jump opt3
        "Option 4":
            jump opt3

    label opt1:
        $ n = 1
        jump done

    label opt2:
        $ n = 2
        jump done

    label opt3:
        $ n = 3
        jump done

    label opt4:
        $ n = 4
        jump done

    label done:
        jump endscene1
