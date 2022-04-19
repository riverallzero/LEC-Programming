import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc

sns.set_context("talk")
sns.set_style("white")
font_title = {"color": "gray"}

font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df_popkr = pd.read_csv("202203_202203_연령별인구현황_월간.csv", encoding="euc-kr")
df_popkr.head()
df_popkr["행정구역"] = df_popkr["행정구역"].str.split("(").str[0]
df_popkr.head()
df_popkr.replace(",", "", regex=True, inplace=True)
df_popkr.replace(" ", "", regex=True, inplace=True)
df_popkr.head()
df_popkrM = df_popkr.filter(like="남").filter(like="세")
df_popkrM.head()
df_popkrMT = df_popkrM.T
df_popkrMT.columns = df_popkr["행정구역"].values
df_popkrMT = df_popkrMT.astype(int)
df_popkrMT.head()
df_popkrMT["나이"] = df_popkrMT.index.str.split("_").str[2]
df_popkrMT.reset_index(drop=True, inplace=True)
df_popkrMT
df_popkrF = df_popkr.filter(like="여").filter(like="세")
df_popkrFT = df_popkrF.T
df_popkrFT.columns = df_popkr["행정구역"].values
df_popkrFT = df_popkrFT.astype(int)
df_popkrFT["나이"] = df_popkrFT.index.str.split("_").str[2]
df_popkrFT.reset_index(drop=True, inplace=True)
df_popkrFT.head(3)

df_popkrMT.to_pickle("df_popkrMT.pkl")
df_popkrFT.to_pickle("df_popkrFT.pkl")

def plot_pop(loc, popmax=6e6, poptick=1e6):
    fig, axs = plt.subplots(ncols=2, sharey=True, figsize=(10, 5), gridspec_kw={"wspace": 0})

    c_M = "green"
    c_F = "darkorange"
    axs[0].barh(df_popkrMT["나이"], df_popkrMT[loc], color=c_M)
    axs[1].barh(df_popkrFT["나이"], df_popkrFT[loc], color=c_F)

    if loc == '전라북도':
        popmax = 2e5
        poptick = 5e4
    elif loc == '전라북도전주시':
        popmax = 9e4
        poptick = 1.5e4
    elif loc == '전라북도고창군':
        popmax = 7e4
        poptick = 1e4
    elif loc == '전라북도부안군':
        popmax = 6e3
        poptick = 1e3
    elif loc == '전라북도익산시':
        popmax = 3e5
        poptick = 1.5e4
    elif loc == '전라북도군산시':
        popmax = 3e4
        poptick = 1e4
    elif loc == '전라북도김제시':
        popmax = 1e4
        poptick = 1e3
    elif loc == '전라북도남원시':
        popmax = 9e3
        poptick = 1e3
    elif loc == '전라북도완주군':
        popmax = 1e4
        poptick = 1e3
    elif loc == '전라북도전주시덕진구':
        popmax = 4e4
        poptick = 1e4
    elif loc == '전라북도전주시완산구':
        popmax = 4e4
        poptick = 1e4
    elif loc == '전라북도정읍시':
        popmax = 1.5e4
        poptick = 5e3
    else:
        popmax = 5e3
        poptick = 1e3

    axs[0].set_xlim(popmax, 0)
    axs[1].set_xlim(0, popmax)

    xticks = np.arange(0, popmax, poptick)
    if poptick >= 1e6:
        factor, unit = 1e-6, "백만"
    elif 1e5 <= poptick < 1e6:
        factor, unit = 1e-5, "십만"
    elif 1e4 <= poptick < 2e5:
        factor, unit = 1e-4, "만"
    elif 1e3 <= poptick < 2e4:
        factor, unit = 1e-3, "천"

    for ax, title in zip(axs, ["남성", "여성"]):
        ax.set_xticks(xticks)
        ax.set_xticklabels([f"{int(x * factor)}{unit}" if x != 0 else "0" for x in xticks])
        ax.grid(axis="x", c="lightgray")
        ax.set_title(title, color="gray", fontweight="bold", pad=16)

    for ax in axs:
        for i, p in enumerate(ax.patches):
            w = p.get_width()
            if ax == axs[0]:
                ha = "right"
                c = c_M
            else:
                ha = "left"
                c = c_F

            ax.text(w, i, f" {format(w, ',')} ",
                    c=c, fontsize="x-small", va="center", ha=ha,
                    fontweight="bold", alpha=0.5)

    fig.suptitle(f"                 {loc}", fontweight="bold")
    fig.tight_layout()

    return fig

def main():
    loc = input('지역명을 입력하세요(예:전라북도전주시): ')
    fig = plot_pop(loc)
    fig.show()
    fig.savefig('{}.png' .format(loc))

if __name__ == '__main__':
    main()
