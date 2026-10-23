import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

OUT = "report/assets"

# Timing shown is the focused A=13, B=7 case: reset is released after two
# rising edges, then the inputs are captured and the product appears two
# rising edges later.
fig, ax = plt.subplots(figsize=(12, 5.4), constrained_layout=True)
fig.patch.set_facecolor("#fbfcfe")
ax.set_facecolor("#fbfcfe")
ax.set_xlim(0, 56)
ax.set_ylim(-0.65, 5.7)
ax.set_yticks([0, 1, 2, 3, 4])
ax.set_yticklabels(["clk", "rst_n", "a[3:0]", "b[3:0]", "p[7:0]"],
                   fontsize=11, fontweight="bold")
ax.set_xticks(range(0, 56, 5))
ax.set_xlabel("Time (ns)")
ax.grid(axis="x", color="#dce3ec", linewidth=0.8)
for y in range(5):
    ax.axhline(y + 0.5, color="#edf1f5", linewidth=0.7)

def digital(y, values, color, label=None, height=0.48):
    for start, end, value, text_value in values:
        level = y + (height if value else 0)
        ax.plot([start, end], [level, level], color=color, linewidth=2.5,
                solid_capstyle="butt")
        if start > 0:
            prev = [v for v in values if v[1] == start]
            if prev and prev[-1][2] != value:
                old = y + (height if prev[-1][2] else 0)
                ax.plot([start, start], [old, level], color=color, linewidth=1.5)
        if text_value:
            ax.text((start + end) / 2, y + 0.24, text_value,
                    ha="center", va="center", fontsize=10,
                    color="#243247", bbox=dict(facecolor="#fbfcfe", edgecolor="none", pad=1))

# Clock starts low and has a 10 ns period.
clk = []
for t in range(0, 56, 5):
    clk.append((t, min(t + 5, 56), (t // 5) % 2 == 1, ""))
digital(0, clk, "#087e8b")
digital(1, [(0, 20, 0, "0"), (20, 56, 1, "1")], "#d1495b")
digital(2, [(0, 30, 0, "0000"), (30, 56, 1, "1101 (13)")], "#356ae6")
digital(3, [(0, 30, 0, "0000"), (30, 56, 1, "0111 (7)")], "#805ad5")
digital(4, [(0, 45, 0, "00000000"), (45, 56, 1, "01011011 (91)")], "#15966a")

for x, lab in [(5, "reset edge 1"), (15, "reset edge 2"),
               (35, "input edge 1"), (45, "input edge 2")]:
    ax.axvline(x, color="#9aa8b8", linestyle="--", linewidth=1)
    ax.text(x, 5.05, lab, ha="center", va="bottom", fontsize=8.5,
            color="#46566b", rotation=0)
ax.annotate("2-cycle registered latency", xy=(45, 4.92), xytext=(30, 4.92),
            arrowprops=dict(arrowstyle="<->", color="#b42332", lw=1.8),
            ha="center", va="bottom", color="#b42332", fontsize=10)
ax.set_title("Focused RTL waveform: A = 13, B = 7, product = 91",
             fontsize=15, fontweight="bold", color="#182230", pad=22)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color("#98a2b3")
ax.tick_params(axis="y", length=0, pad=10)
fig.savefig(f"{OUT}/waveform_A13_B7.png", dpi=180)
plt.close(fig)

# Structural block diagram with the required conceptual counts.
fig, ax = plt.subplots(figsize=(13, 6), constrained_layout=True)
fig.patch.set_facecolor("#fbfcfe")
ax.set_facecolor("#fbfcfe")
ax.set_xlim(0, 13)
ax.set_ylim(0, 6)
ax.axis("off")
ax.text(6.5, 5.68, "4-bit unsigned array multiplier", ha="center",
        fontsize=17, fontweight="bold", color="#182230")

def box(x, y, w, h, title, sub, color):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.08",
                       facecolor=color, edgecolor="#46566b", linewidth=1.4)
    ax.add_patch(p)
    ax.text(x + w/2, y + h*0.62, title, ha="center", va="center",
            fontsize=11, fontweight="bold", color="#182230")
    ax.text(x + w/2, y + h*0.32, sub, ha="center", va="center",
            fontsize=9.5, color="#344054")

def arrow(x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", lw=1.8, color="#53657c"))

box(0.3, 3.75, 1.55, 0.9, "Input A", "4 bits", "#e7efff")
box(0.3, 2.15, 1.55, 0.9, "Input B", "4 bits", "#efe9ff")
box(2.15, 3.75, 1.7, 0.9, "A register", "4 flip-flops", "#d8e6ff")
box(2.15, 2.15, 1.7, 0.9, "B register", "4 flip-flops", "#e6ddff")
arrow(1.85, 4.2, 2.15, 4.2)
arrow(1.85, 2.6, 2.15, 2.6)

ax.text(5.3, 5.0, "16 partial-product AND gates", ha="center",
        fontsize=11, fontweight="bold", color="#182230")
for r in range(4):
    for c in range(4):
        x, y = 4.2 + c*0.56, 3.65 - r*0.58
        ax.add_patch(Rectangle((x, y), 0.42, 0.32, facecolor="#fff1cc",
                               edgecolor="#b45309", linewidth=1.2))
        ax.text(x+0.21, y+0.16, "AND", ha="center", va="center",
                fontsize=6.8, fontweight="bold", color="#713f12")
ax.text(5.3, 1.0, "4 × 4 partial products", ha="center", fontsize=9, color="#53657c")
arrow(3.85, 4.2, 4.15, 4.2)
arrow(3.85, 2.6, 4.15, 2.6)

ax.text(8.6, 5.0, "12 full adders (3 rows × 4)", ha="center",
        fontsize=11, fontweight="bold", color="#182230")
for r in range(3):
    for c in range(4):
        x, y = 7.45 + c*0.56, 3.65 - r*0.78
        ax.add_patch(Rectangle((x, y), 0.42, 0.40, facecolor="#dcfce7",
                               edgecolor="#15803d", linewidth=1.2))
        ax.text(x+0.21, y+0.20, "FA", ha="center", va="center",
                fontsize=9, fontweight="bold", color="#14532d")
    if r < 2:
        ax.annotate("carry row", xy=(7.65, 3.65-(r+1)*0.78+0.46),
                    xytext=(7.65, 3.65-r*0.78-0.06), ha="center", va="center",
                    fontsize=7.5, color="#53657c",
                    arrowprops=dict(arrowstyle="-|>", lw=1.1, color="#53657c"))
arrow(6.55, 3.4, 7.35, 3.4)
box(10.65, 2.65, 2.0, 1.0, "Product register", "8 flip-flops, P[7:0]", "#d5f5f6")
arrow(9.75, 3.4, 10.65, 3.4)
ax.text(6.5, 0.34,
        "Input and product registers create a two-cycle latency; one result is produced each cycle.",
        ha="center", fontsize=10, color="#53657c")
fig.savefig(f"{OUT}/array_multiplier_block_diagram.png", dpi=180)
plt.close(fig)
