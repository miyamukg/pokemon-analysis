import csv
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname=r'c:\Windows\Fonts\meiryo.ttc')


def main():
    NAME_COL = 1
    TYPE1_COL = 2
    TYPE2_COL = 3
    SUM_COL = 13

    HYPHEN = '-'

    with open('../dataset/pokemon_status.csv') as f:
        reader = csv.reader(f)
        csv_list = [i for i in reader]

    csv_list.pop(0)
    type_dict = {}

    max_sum = 0
    min_sum = 0

    # 最大・最小の合計値を持つポケモンのリスト
    max_poke_list = []
    min_poke_list = []

    for index_row, row in enumerate(csv_list):
        # メガシンカを省く
        if HYPHEN in csv_list[index_row][0]:
            continue

        for index_col, col in enumerate(row):
            # タイプ集計処理
            if index_col == TYPE1_COL:
                if col not in type_dict:
                    type_dict[col] = 0
                type_dict[col] += 1

            if index_col == TYPE2_COL and col:
                if col not in type_dict:
                    type_dict[col] = 0
                type_dict[col] += 1

            # 合計列（最大・最小）の処理
            if index_col == SUM_COL and col.isdecimal():
                if index_row == 0:
                    max_sum = col
                    min_sum = col
                    continue

                if max_sum < col:
                    max_sum = col
                    max_poke_list = []
                    max_poke_list.append(row[NAME_COL])
                elif min_sum > col:
                    min_sum = col
                    min_poke_list = []
                    min_poke_list.append(row[NAME_COL])
                elif max_sum == col:
                    max_poke_list.append(row[NAME_COL])
                elif min_sum == col:
                    min_poke_list.append(row[NAME_COL])

    print("合計値が一番高いポケモン : " + ','.join(max_poke_list))
    print("合計値が一番低いポケモン : " + ','.join(min_poke_list))

    # グラフを表示する
    label, height = zip(*[(type[0], type[1]) for type in type_dict.items()])
    left = list(range(len(label)))
    plt.figure(figsize=(14.0, 6.0))
    plt.xticks(fontproperties=fp, fontsize=8)
    plt.bar(left, height, tick_label=label, align="center")
    plt.show()


if __name__ == "__main__":
    main()
