user_attack = input("Choose:")


if user_attack == pc_attack:
    result = (pl_att - pc_def) - (pc_att - pl_def)
    print(result)