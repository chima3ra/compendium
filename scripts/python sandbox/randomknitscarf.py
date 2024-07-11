import random

def generate_scarf_pattern(stlen,rows):
    pattern = []
    for i in range(rows):
        for i in range(stlen):
            row = ['K']
            for i in range(1,stlen//2):
                stitch = random.choices(['K','YO','SSK'], weights = [1, 2, 2])[0]
                row.append(stitch)
            for i in range((stlen//2)-1,-1,-1):
                if row[i] == "YO":
                    row.append("K2Tg")
                elif row[i] == "SSK":
                    row.append("YO")
                else:
                    row.append("K")
        pattern.append(row)
    return(pattern)


generate_scarf_pattern(24, 10)