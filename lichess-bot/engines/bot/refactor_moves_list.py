import os
import pandas as pd

current_directory = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_directory, 'high_elo_opening.csv')

    # Get all of the SAN notations
# chess_openings = pd.read_csv(file_path, on_bad_lines='skip')

# print(chess_openings)
# for i in chess_openings['moves_list']:
#     print(i)

with (open(r"C:\Users\nikan\Desktop\Chess_bot\lichess-bot\engines\bot\input_openings_3.txt", "r") as f,
      open(r"C:\Users\nikan\Desktop\Chess_bot\lichess-bot\engines\bot\openings3.txt", "w") as g):
    for i in f.readlines()[1:]:
        s = i.strip()[1:-1]
        s = s.split('\',')

        # print(s)
        for k in range(1, 20):
            for j in range(len(s)):
                # print(s[j])
                if len(s[j].split('\'' + str(k) + ".")) > 1:
                    s[j] = s[j].split('\'' + str(k) + ".")[1]
                # print(s[j])

        for j in range(len(s)):
            for k in s[j].split('\''):
                if k != "":
                    s[j] = k
        # print(s)


        g.write(" ".join(s) + '\n')


# with open(r"C:\Users\nikan\Desktop\Chess_bot\lichess-bot\engines\bot\high_elo_opening_result.txt", "w") as g:
#     g.write("Jopa")


def ad(a):
    a.append(2)
    return a

b = [1]
ad(b)

print(b)