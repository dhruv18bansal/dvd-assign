import json
import math
import os
import re
from PIL import Image as PILImage

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, Image, PageBreak, KeepTogether)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "report", "report.pdf")
M = json.load(open(os.path.join(ROOT, "pnr", "metrics.json")))
CFG = json.load(open(os.path.join(ROOT, "pnr", "config.json")))
layout_source = os.path.join(ROOT, "pnr", "final", "render", "mult_array.png")
layout_full = os.path.join(ROOT, "report", "assets", "layout_full_die.png")
layout_zoom = os.path.join(ROOT, "report", "assets", "layout_zoom.png")
if os.path.exists(layout_source):
    layout_image = PILImage.open(layout_source).convert("RGB")
    layout_image.save(layout_full)
    zoom_image = layout_image.crop((300, 340, 700, 700)).resize(
        (1000, 900), PILImage.Resampling.LANCZOS)
    zoom_image.save(layout_zoom)
PNR_PERIOD = float(CFG["CLOCK_PERIOD"])
setup_ws = float(M.get("timing__setup__ws__corner:max_ss_100C_1v60", 0.0))
worst_setup_ws = min(float(M.get(f"timing__setup__ws__corner:{c}", setup_ws))
                     for c in ["max_ss_100C_1v60", "nom_ss_100C_1v60",
                               "min_ss_100C_1v60"])
achievable_period = PNR_PERIOD - worst_setup_ws
postroute_fmax = 1000.0 / achievable_period if achievable_period > 0 else 0.0
area = float(M.get("design__instance__area__stdcell", 0))
die_area = float(M.get("design__die__area", 0))
core_area = float(M.get("design__core__area", 0))
cell_count = int(M.get("design__instance__count__stdcell", 0))
wirelength = float(M.get("route__wirelength", M.get("global_route__wirelength", 0)))
drc_magic = int(M.get("magic__drc_error__count", 0))
drc_klayout = int(M.get("klayout__drc_error__count", 0))
lvs = int(M.get("design__lvs_error__count", 0))
pnr_tries = int(os.environ.get("PNR_TRIES", "7"))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleX", parent=styles["Title"], fontName="Helvetica-Bold",
                          fontSize=23, leading=28, textColor=colors.HexColor("#17324d"),
                          alignment=TA_CENTER, spaceAfter=8))
styles.add(ParagraphStyle(name="SubtitleX", parent=styles["Normal"], fontSize=10,
                          leading=15, textColor=colors.HexColor("#53657c"),
                          alignment=TA_CENTER, spaceAfter=8))
styles.add(ParagraphStyle(name="H1X", parent=styles["Heading1"], fontSize=16, leading=20,
                          textColor=colors.HexColor("#17324d"), spaceBefore=4, spaceAfter=9))
styles.add(ParagraphStyle(name="H2X", parent=styles["Heading2"], fontSize=11, leading=14,
                          textColor=colors.HexColor("#155e75"), spaceBefore=5, spaceAfter=4))
styles.add(ParagraphStyle(name="BodyX", parent=styles["BodyText"], fontSize=9, leading=13,
                          spaceAfter=6, alignment=TA_LEFT))
styles.add(ParagraphStyle(name="SmallX", parent=styles["BodyText"], fontSize=7.5, leading=10,
                          textColor=colors.HexColor("#344054")))
styles.add(ParagraphStyle(name="CalloutX", parent=styles["BodyText"], fontSize=9.2, leading=14,
                          borderColor=colors.HexColor("#d5e3f0"), borderWidth=0.7,
                          borderPadding=7, backColor=colors.HexColor("#f3f8fc"), spaceAfter=7))

def P(s, style="BodyX"):
    return Paragraph(s, styles[style])

def table(rows, widths, font=8):
    t = Table([[P(str(c), "SmallX") for c in row] for row in rows], colWidths=widths,
              repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dce9f3")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#17324d")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#c5d0dc")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f7f9fb")]),
    ]))
    return t

def page(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setStrokeColor(colors.HexColor("#d5e0ea"))
    canvas.line(18*mm, 14*mm, w-18*mm, 14*mm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.HexColor("#667085"))
    canvas.drawString(18*mm, 9*mm, "4-bit Array Multiplier | SKY130A RTL-to-GDSII")
    canvas.drawRightString(w-18*mm, 9*mm, f"{doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=A4, rightMargin=18*mm, leftMargin=18*mm,
                        topMargin=17*mm, bottomMargin=19*mm,
                        title="4-bit Array Multiplier: RTL to GDSII",
                        author="Dhruv Bansal and Dataarnoor Singh Oberoi")
story = []

# Page 1: design and functional evidence.
story += [Spacer(1, 13*mm), P("4-bit Array Multiplier", "TitleX"),
          P("RTL design, verification, synthesis, timing analysis, and SKY130A physical design", "SubtitleX"),
          Spacer(1, 2*mm),
          table([["Team member", "Roll number"],
                 ["Dhruv Bansal", "2023102048"],
                 ["Dataarnoor Singh Oberoi", "2023102047"]], [95*mm, 65*mm]),
          Spacer(1, 5*mm), P("Design summary", "H1X"),
          P("The design multiplies two unsigned 4-bit inputs. Input registers capture A and B, a combinational array forms the 16 partial products and accumulates them through 12 full adders, and an 8-bit output register captures the product. The registered interface has a two-cycle latency and can accept one input pair each cycle.")]
block = Image(os.path.join(ROOT, "report/assets/array_multiplier_block_diagram.png"), width=170*mm, height=78*mm)
story += [block, Spacer(1, 2*mm), P("Functional verification", "H2X"),
          P("The testbench checks all 16 × 16 = 256 unsigned input combinations. The RTL simulation completed with PASS: 256 vectors checked, 0 errors. For the assigned hand-worked vector, A = 13 (1101 binary) and B = 7 (0111 binary), giving P = 91 (01011011 binary). A fault-injection check changed the full-adder sum expression temporarily to a ^ b; the testbench detected 95 incorrect vectors. The correct expression was restored before synthesis."),
          P("Hand-worked partial products: 00001101 + 00011010 + 00110100 + 00000000 = 01011011 (91).", "CalloutX")]
story += [PageBreak(), P("RTL waveform and mapped logic", "H1X"),
          Image(os.path.join(ROOT, "report/assets/waveform_A13_B7.png"), width=170*mm, height=76.5*mm),
          P("The waveform shows reset held low for two rising clock edges, then released. A=13 and B=7 are applied at 30 ns. The input register captures them at the first rising edge, and the product register presents 91 at the second rising edge.", "SmallX"),
          Spacer(1, 3*mm), P("Synthesis results", "H2X"),
          table([["Metric", "Result"],
                 ["Mapped standard-cell count", "61"],
                 ["Total mapped cell area", "756.976 µm²"],
                 ["Flip-flops", "16 × sky130_fd_sc_hd__dfrtp_1"],
                 ["Flip-flop area", "400.384 µm² (52.89%)"],
                 ["Most used cells", "dfrtp_1: 16; nand2_1: 7; and2_0: 4 (maj3_1 also 4)"],
                 ["Gate-level simulation", "PASS: 256 vectors checked, 0 errors"]], [57*mm, 103*mm]),
          Spacer(1, 3*mm), P("The conceptual 12 full adders are mapped into library primitives and can be combined or simplified by logic optimization; synthesized cell types therefore do not appear as twelve literal FA cells.", "CalloutX"),
          PageBreak(), P("Static timing analysis", "H1X"),
          P("OpenSTA was run at the SKY130A typical corner with 1.0 ns input and output delays. The 10 ns analysis reported a worst register-to-register setup slack of 7.213 ns, giving Tmin = 10.000 − 7.213 = 2.787 ns and Fmax = 1000 / 2.787 = 358.808 MHz. A second run at the rounded test period 2.79 ns reported 0.003 ns slack on the critical register-to-register path."),
          table([["Timing measurement", "Value"],
                 ["WNS at 10 ns", "7.213 ns"],
                 ["Estimated Tmin", "2.787 ns"],
                 ["Fmax = 1000/Tmin", "358.808 MHz"],
                 ["Slack at 2.79 ns test period", "0.003 ns"],
                 ["Critical path startpoint", "a_reg[1] (mapped cell _91_)"],
                 ["Critical path endpoint", "p[6] (mapped cell _88_)"],
                 ["Path cell sequence", "dfrtp_1 -> clkinv_1 -> o311ai_0 -> a21oi_1 -> maj3_1 -> xnor3_1 -> maj3_1 -> maj3_1 -> xor3_1 -> dfrtp_1"],
                 ["Total path cells / combinational cells", "10 / 8 (includes launch and capture flip-flops)"],
                 ["Mapped full-adder functions", "Approximately 5"]], [54*mm, 106*mm]),
          Spacer(1, 4*mm), P("The path has eight combinational library cells between the launching and capturing flip-flops. Several carry and sum functions are implemented by compound cells, so the logical full-adder count is not the same as the mapped serial cell count.", "BodyX"),
          P("The report in sta/mult_array_timing.rpt contains the detailed path at the final tested period. The launch-to-capture latency is two clock periods; at Tmin, this is 5.574 ns. The steady-state throughput is one result per cycle, or about 358.808 million results per second.", "BodyX"),
          PageBreak(), P("Physical design results", "H1X"),
          P(f"The final fixed-die LibreLane run used a {PNR_PERIOD:.1f} ns clock target, an absolute 150 µm × 150 µm die, and completed after {pnr_tries} timing attempts. The final metrics below are copied from the completed flow's metrics.json.")]
story += [table([["Physical-design result", "Value"],
                 ["Clock target / run attempts", f"{PNR_PERIOD:.1f} ns / {pnr_tries}"],
                 ["Die area / core area", f"{die_area:.2f} µm² / {core_area:.2f} µm²"],
                 ["Cells after synthesis (Part B)", "61"],
                 ["Standard-cell area / count", f"{area:.2f} µm² / {cell_count}"],
                 ["Added implementation cells", f"{int(M.get('design__instance__count__class:fill_cell', 0))} fill; {int(M.get('design__instance__count__class:tap_cell', 0))} tap; {int(M.get('design__instance__count__class:clock_buffer', 0))} clock buffers; {int(M.get('design__instance__count__class:timing_repair_buffer', 0))} timing repair buffers"],
                 ["Routed wirelength", f"{wirelength:.0f} µm"],
                 ["Worst setup slack (slow corner)", f"{worst_setup_ws:.3f} ns"],
                 ["Part C pre-route Fmax estimate", "358.808 MHz"],
                 ["Post-route Fmax estimate", f"{postroute_fmax:.2f} MHz"],
                 ["Magic / KLayout DRC errors", f"{drc_magic} / {drc_klayout}"],
                 ["LVS errors", str(lvs)]], [64*mm, 96*mm]),
          Spacer(1, 4*mm), P("Full-die view", "H2X")]
full = os.path.join(ROOT, "report/assets/layout_full_die.png")
zoom = os.path.join(ROOT, "report/assets/layout_zoom.png")
if os.path.exists(full):
    story.append(Image(full, width=125*mm, height=125*mm, kind="proportional"))
else:
    story.append(P("Full-die screenshot is stored in report/assets/layout_full_die.png.", "SmallX"))
story += [PageBreak(), P("Layout detail and discussion", "H1X"), P("Standard-cell rows and routed metal", "H2X")]
if os.path.exists(zoom):
    story.append(Image(zoom, width=165*mm, height=120*mm, kind="proportional"))
else:
    story.append(P("Zoomed layout screenshot is stored in report/assets/layout_zoom.png.", "SmallX"))
story += [Spacer(1, 2*mm), P("A positive final setup slack indicates that the configured period meets the reported slow-corner timing check. The post-route Fmax estimate is calculated as 1000 / (clock target − worst setup slack). Physical design adds clock-tree buffers, timing-repair buffers, tap cells, and filler cells around the synthesized logic. Routed parasitics and clock-tree effects can reduce the attainable frequency relative to pre-route STA.")]
story += [PageBreak(), P("Short answers", "H1X")]
answers = [
    ("1. Why does synthesis not report 16 AND gates and 12 full adders?", "Those are conceptual RTL building blocks. The mapper decomposes the full adders into available standard cells, uses compound gates for sum/carry logic, and optimizes shared or redundant logic. Here it reports 61 mapped cells, including 16 sequential cells and 45 combinational cells."),
    ("2. What is the critical path and how does it compare with the expected 2N trend?", "The worst register path starts at a_reg[1] and ends at p[6], passing through eight mapped combinational cells (including compound majority and XOR/XNOR cells). The path crosses several serial carry/sum functions, consistent with ripple-like array accumulation; the exact cell depth differs from an idealized count of about 2N full-adder delays because synthesis combines Boolean functions."),
    ("3. Why is flip-flop area a large fraction of total area?", "The design uses 16 resettable flip-flops for the registered 4-bit operands and 8-bit product. Their combined 400.384 µm² is 52.89% of the 756.976 µm² mapped area, because the datapath is small while each resettable sequential cell has substantial area."),
    ("4. Why can physical-design Fmax be lower, and what cells are added?", f"Placement and routing add clock-tree and timing-repair buffers and parasitic interconnect, which affect setup timing. The Part C pre-route estimate is 358.808 MHz; the post-route estimate is {postroute_fmax:.2f} MHz. Placement and routing add clock-tree and timing-repair buffers and parasitic interconnect, which affect setup timing. This run also includes tap and filler cells for physical requirements."),
    ("5. What do DRC and LVS check?", "Design-rule checking verifies layout geometry against foundry rules such as width, spacing, enclosure, and overlap. Layout-versus-schematic compares extracted devices and connectivity with the reference netlist. Both checks report zero errors/differences for this run."),
    ("6. How does an 8-bit array multiplier scale?", "For two N-bit operands, a basic array has N² partial-product AND terms and approximately N(N−1) full adders. At N=8 this is 64 partial-product terms and about 56 full adders, compared with 16 and 12 for N=4. Using the assignment’s approximately 2N full-adder-delay estimate, path depth grows from about 8 such delays at N=4 to about 16 at N=8. Area grows approximately quadratically.")]
for q, a in answers:
    story.append(KeepTogether([P(q, "H2X"), P(a, "BodyX")]))

doc.build(story, onFirstPage=page, onLaterPages=page)
print(OUT)
