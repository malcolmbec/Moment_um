label dialogue:
    scene bg bar
    show cat sad at behind_bar_left_cat
    show smol meh at behind_bar_right_smol
    show bar

    s"Now we have some options!"

    menu:
        "Option 1":
            jump opt1

    label opt1:
        jump ending

    label ending:
        jump endscene
