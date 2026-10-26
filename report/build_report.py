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
          PageBreak(), P("Short answers", "H1X")]
answers = [
    ("1. Why does synthesis not report 16 AND gates and 12 full adders?", "Those are conceptual RTL building blocks. The mapper decomposes the full adders into available standard cells, uses compound gates for sum/carry logic, and optimizes shared or redundant logic. Here it reports 61 mapped cells, including 16 sequential cells and 45 combinational cells."),
    ("2. What is the critical path and how does it compare with the expected 2N trend?", "The worst register path starts at a_reg[1] and ends at p[6], passing through eight mapped combinational cells (including compound majority and XOR/XNOR cells). The path crosses several serial carry/sum functions, consistent with ripple-like array accumulation; the exact cell depth differs from an idealized count of about 2N full-adder delays because synthesis combines Boolean functions."),
    ("3. Why is flip-flop area a large fraction of total area?", "The design uses 16 resettable flip-flops for the registered 4-bit operands and 8-bit product. Their combined 400.384 µm² is 52.89% of the 756.976 µm² mapped area, because the datapath is small while each resettable sequential cell has substantial area."),
    ("4. Why can physical-design Fmax be lower, and what cells are added?", f"Placement and routing add clock-tree and timing-repair buffers and parasitic interconnect, which affect setup timing. The Part C pre-route estimate is 358.808 MHz; the post-route estimate is {postroute_fmax:.2f} MHz. Placement and routing add clock-tree and timing-repair buffers and parasitic interconnect, which affect setup timing. This run also includes tap and filler cells for physical requirements."),
    ("5. What do DRC and LVS check?", "Design-rule checking verifies layout geometry against foundry rules such as width, spacing, enclosure, and overlap. Layout-versus-schematic compares extracted devices and connectivity with the reference netlist. Both checks report zero errors/differences for this run."),
    ("6. How does an 8-bit array multiplier scale?", "For two N-bit operands, a basic array has N² partial-product AND terms and approximately N(N−1) full adders. At N=8 this is 64 partial-product terms and about 56 full adders, compared with 16 and 12 for N=4. Using the assignment’s approximately 2N full-adder-delay estimate, path depth grows from about 8 such delays at N=4 to about 16 at N=8. Area grows approximately quadratically.")]
for q, a in answers:
    story.append(KeepTogether([P(q, "H2X"), P(a, "BodyX")]))

# Project scope, assignment coverage, final evidence, and team contribution.
story += [PageBreak(), P("Assignment scope and evidence", "H1X"),
          P("This submission implements and documents a registered unsigned 4-bit array multiplier from RTL through SKY130A standard-cell physical design. The table maps the assignment's main requirements to the implementation and the evidence included with the deliverables.")]
story += [table([["Requirement", "Implementation / evidence", "Status"],
                 ["RTL architecture", "16 partial products, 12 full adders, operand registers, and an 8-bit product register in rtl/.", "Complete"],
                 ["Functional verification", "10 ns testbench clock; reset asserted for two rising edges; all 256 input pairs checked; PASS result and VCD waveform.", "Complete"],
                 ["Hand calculation and fault check", "A=13, B=7 gives P=91; temporary sum fault is detected by the exhaustive testbench.", "Complete"],
                 ["Synthesis", "Yosys SKY130A mapped netlist and statistics report; 61 cells and 756.976 um^2 area.", "Complete"],
                 ["Gate-level verification", "Mapped netlist simulated with SKY130 functional cell models; 256 vectors pass.", "Complete"],
                 ["Static timing", "OpenSTA typical-corner reports at 10.00 ns and 2.79 ns, including the critical path and slack.", "Complete"],
                 ["Physical design", "LibreLane fixed 150 um x 150 um die; final metrics and GDSII; signoff DRC and LVS results.", "Complete"],
                 ["Written analysis", "Design overview, results tables, layout views, and answers to the six assignment questions in this report.", "Complete"]],
                [43*mm, 101*mm, 16*mm]),
          Spacer(1, 4*mm), P("Scope and assumptions", "H2X"),
          P("The implemented function is unsigned multiplication of two 4-bit operands, producing an 8-bit product. The interface registers both operands and the product. The report's 8-bit discussion is an architectural scaling estimate, not a separately implemented or measured 8-bit design. Timing figures are based on the stated SKY130A corners and constraints; frequency values are derived estimates, not silicon measurements.")]

story += [PageBreak(), P("Final values and interpretation", "H1X"),
          P("The following values summarize the saved simulation, synthesis, STA, and physical-design artifacts. Derived values are shown with their calculation so the basis of comparison is clear.")]
story += [table([["Stage", "Final value", "Meaning"],
                 ["Functional test", "256 / 256 pass", "Exhaustive 4-bit unsigned input space."],
                 ["Fault injection", "95 mismatches detected", "The intentionally incorrect sum logic is observable to the testbench."],
                 ["Mapped synthesis", "61 cells; 756.976 um^2", "16 resettable flip-flops use 400.384 um^2 (52.89%)."],
                 ["Part C timing", "10.00 - 7.213 = 2.787 ns; 1000 / 2.787 = 358.808 MHz", "Tmin and pre-route Fmax estimate from typical-corner STA."],
                 ["STA boundary check", "2.79 ns; 0.003 ns setup slack", "Near-zero positive slack at Tmin rounded to 0.01 ns."],
                 ["Part D floorplan", "150 x 150 um die; 17,759.5 um^2 core", "Absolute die sizing in the final configuration."],
                 ["Part D implementation", "327 standard cells; 1,224.92 um^2; 2,361 um routed wire", "Post-route standard-cell and detailed-route metrics."],
                 ["Part D timing", "6.5 ns target; 0.14985 ns worst slow-corner slack", "Final run after seven clock-period attempts."],
                 ["Post-route frequency", "1000 / (6.5 - 0.14985) = 157.48 MHz", "Estimate using the configured period minus worst slow-corner slack."],
                 ["Signoff", "Magic DRC 0; KLayout DRC 0; LVS errors 0", "Saved metrics indicate clean final signoff."]],
                [35*mm, 61*mm, 64*mm]),
          Spacer(1, 4*mm), P("Physical-design cell additions", "H2X"),
          P("The final metrics record 1,550 filler cells, 245 tap cells, 3 clock buffers, and 17 timing-repair buffers. These implementation cells serve layout, power, clock-tree, and timing-repair needs; they are additional to the 61 cells in the synthesized logical netlist. The final routed wirelength is taken from route__wirelength in pnr/metrics.json.")]

story += [PageBreak(), P("Reproduction and contribution", "H1X"),
          P("The source tree includes the RTL, testbench, Yosys synthesis script and outputs, OpenSTA script and timing report, LibreLane configuration, final metrics and GDSII, report source, and visual evidence. The README gives the ordered commands and expected results for each stage. The per-run working directory is intentionally excluded from the deliverables; the root-level metrics and GDSII are the final copied outputs.")]
story += [table([["Stage", "Reproduction command / input", "Expected artifact"],
                 ["RTL simulation", "iverilog -g2012 -o sim tb/tb_mult.v rtl/full_adder.v rtl/mult_array.v; then vvp sim", "PASS summary; mult.vcd"],
                 ["Synthesis", "yosys -c synth/synth.tcl", "synth/mult_array_netlist.v; synth/mult_array_stat.rpt"],
                 ["STA", "CLOCK_PERIOD=10.0 sta -exit sta/sta.tcl; repeat at 2.79 ns", "sta/mult_array_timing.rpt and critical-path data"],
                 ["Physical design", "LibreLane using pnr/config.json and the selected sky130A PDK", "pnr/metrics.json; pnr/mult_array.gds"],
                 ["Report", "python3 report/build_report.py", "report/report.pdf"]],
                [32*mm, 100*mm, 28*mm]),
          Spacer(1, 7*mm), P("Team contribution statement", "H1X"),
          P("Dhruv Bansal (2023102048) and Dataarnoor Singh Oberoi (2023102047) contributed equally to this assignment. Both members jointly contributed to the RTL design, functional verification, synthesis and timing analysis, physical-design execution, interpretation of results, and preparation of the report.", "CalloutX"),
          Spacer(1, 3*mm), P("Team members", "H2X"),
          table([["Member", "Roll number", "Contribution"],
                 ["Dhruv Bansal", "2023102048", "Equal contribution across the assignment."],
                 ["Dataarnoor Singh Oberoi", "2023102047", "Equal contribution across the assignment."]],
                [53*mm, 34*mm, 73*mm])]

doc.build(story, onFirstPage=page, onLaterPages=page)
print(OUT)
