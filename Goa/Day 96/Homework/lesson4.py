def garda_mesamis(sia):
    axali_sia = []
    for s in sia:
        if len(s) > 3:
            axali_sia.append(s)
    return axali_sia


print(garda_mesamis(["hi", "hello", "ok", "python", "yes"]))  
