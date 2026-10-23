module mult_array (clk,
    rst_n,
    a,
    b,
    p);
 input clk;
 input rst_n;
 input [3:0] a;
 input [3:0] b;
 output [7:0] p;

 wire _00_;
 wire _01_;
 wire _02_;
 wire _03_;
 wire _04_;
 wire _05_;
 wire _06_;
 wire _07_;
 wire _08_;
 wire _09_;
 wire _10_;
 wire _11_;
 wire _12_;
 wire _13_;
 wire _14_;
 wire _15_;
 wire _16_;
 wire _17_;
 wire _18_;
 wire _19_;
 wire _20_;
 wire _21_;
 wire _22_;
 wire _23_;
 wire _24_;
 wire _25_;
 wire _26_;
 wire _27_;
 wire _28_;
 wire _29_;
 wire _30_;
 wire _31_;
 wire _32_;
 wire _33_;
 wire _34_;
 wire _35_;
 wire _36_;
 wire _37_;
 wire net1;
 wire net2;
 wire net3;
 wire net4;
 wire \a_reg[0] ;
 wire \a_reg[1] ;
 wire \a_reg[2] ;
 wire \a_reg[3] ;
 wire \adder_rows[1].adders[0].fa.sum ;
 wire \adder_rows[2].adders[0].fa.sum ;
 wire \adder_rows[3].adders[0].fa.sum ;
 wire \adder_rows[3].adders[1].fa.sum ;
 wire \adder_rows[3].adders[2].fa.sum ;
 wire \adder_rows[3].adders[3].fa.cout ;
 wire \adder_rows[3].adders[3].fa.sum ;
 wire net5;
 wire net6;
 wire net7;
 wire net8;
 wire \b_reg[0] ;
 wire \b_reg[1] ;
 wire \b_reg[2] ;
 wire \b_reg[3] ;
 wire net10;
 wire net11;
 wire net12;
 wire net13;
 wire net14;
 wire net15;
 wire net16;
 wire net17;
 wire \pp[0][0] ;
 wire net9;
 wire clknet_0_clk;
 wire clknet_1_0__leaf_clk;
 wire clknet_1_1__leaf_clk;

 sky130_fd_sc_hd__decap_3 FILLER_0_103 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_27 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_29 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_55 ();
 sky130_fd_sc_hd__decap_12 FILLER_0_57 ();
 sky130_fd_sc_hd__decap_12 FILLER_0_69 ();
 sky130_fd_sc_hd__decap_3 FILLER_0_81 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_85 ();
 sky130_fd_sc_hd__decap_12 FILLER_0_91 ();
 sky130_fd_sc_hd__fill_1 FILLER_10_105 ();
 sky130_fd_sc_hd__decap_8 FILLER_10_19 ();
 sky130_fd_sc_hd__fill_1 FILLER_10_27 ();
 sky130_fd_sc_hd__decap_12 FILLER_10_29 ();
 sky130_fd_sc_hd__decap_4 FILLER_10_41 ();
 sky130_fd_sc_hd__decap_12 FILLER_10_64 ();
 sky130_fd_sc_hd__decap_12 FILLER_10_7 ();
 sky130_fd_sc_hd__decap_8 FILLER_10_76 ();
 sky130_fd_sc_hd__decap_12 FILLER_10_85 ();
 sky130_fd_sc_hd__decap_8 FILLER_10_97 ();
 sky130_fd_sc_hd__fill_1 FILLER_11_105 ();
 sky130_fd_sc_hd__decap_4 FILLER_11_23 ();
 sky130_fd_sc_hd__fill_1 FILLER_11_27 ();
 sky130_fd_sc_hd__decap_4 FILLER_11_31 ();
 sky130_fd_sc_hd__fill_1 FILLER_11_35 ();
 sky130_fd_sc_hd__fill_2 FILLER_11_39 ();
 sky130_fd_sc_hd__decap_12 FILLER_11_44 ();
 sky130_fd_sc_hd__fill_1 FILLER_11_57 ();
 sky130_fd_sc_hd__decap_4 FILLER_11_66 ();
 sky130_fd_sc_hd__decap_12 FILLER_11_75 ();
 sky130_fd_sc_hd__decap_12 FILLER_11_87 ();
 sky130_fd_sc_hd__decap_6 FILLER_11_99 ();
 sky130_fd_sc_hd__fill_1 FILLER_12_105 ();
 sky130_fd_sc_hd__decap_4 FILLER_12_15 ();
 sky130_fd_sc_hd__fill_2 FILLER_12_26 ();
 sky130_fd_sc_hd__decap_12 FILLER_12_3 ();
 sky130_fd_sc_hd__fill_2 FILLER_12_37 ();
 sky130_fd_sc_hd__decap_6 FILLER_12_42 ();
 sky130_fd_sc_hd__decap_12 FILLER_12_68 ();
 sky130_fd_sc_hd__decap_4 FILLER_12_80 ();
 sky130_fd_sc_hd__decap_12 FILLER_12_85 ();
 sky130_fd_sc_hd__decap_8 FILLER_12_97 ();
 sky130_fd_sc_hd__decap_3 FILLER_13_19 ();
 sky130_fd_sc_hd__decap_8 FILLER_13_29 ();
 sky130_fd_sc_hd__fill_1 FILLER_13_44 ();
 sky130_fd_sc_hd__decap_6 FILLER_13_57 ();
 sky130_fd_sc_hd__fill_1 FILLER_13_63 ();
 sky130_fd_sc_hd__decap_12 FILLER_13_7 ();
 sky130_fd_sc_hd__decap_12 FILLER_13_70 ();
 sky130_fd_sc_hd__decap_4 FILLER_13_82 ();
 sky130_fd_sc_hd__fill_1 FILLER_14_105 ();
 sky130_fd_sc_hd__decap_4 FILLER_14_23 ();
 sky130_fd_sc_hd__fill_1 FILLER_14_27 ();
 sky130_fd_sc_hd__decap_6 FILLER_14_29 ();
 sky130_fd_sc_hd__fill_1 FILLER_14_35 ();
 sky130_fd_sc_hd__decap_8 FILLER_14_51 ();
 sky130_fd_sc_hd__decap_6 FILLER_14_78 ();
 sky130_fd_sc_hd__decap_12 FILLER_14_85 ();
 sky130_fd_sc_hd__decap_8 FILLER_14_97 ();
 sky130_fd_sc_hd__fill_1 FILLER_15_101 ();
 sky130_fd_sc_hd__fill_1 FILLER_15_15 ();
 sky130_fd_sc_hd__decap_12 FILLER_15_3 ();
 sky130_fd_sc_hd__decap_12 FILLER_15_36 ();
 sky130_fd_sc_hd__decap_8 FILLER_15_48 ();
 sky130_fd_sc_hd__decap_12 FILLER_15_57 ();
 sky130_fd_sc_hd__decap_12 FILLER_15_69 ();
 sky130_fd_sc_hd__decap_12 FILLER_15_81 ();
 sky130_fd_sc_hd__decap_8 FILLER_15_93 ();
 sky130_fd_sc_hd__decap_12 FILLER_16_15 ();
 sky130_fd_sc_hd__fill_1 FILLER_16_27 ();
 sky130_fd_sc_hd__decap_8 FILLER_16_29 ();
 sky130_fd_sc_hd__decap_12 FILLER_16_3 ();
 sky130_fd_sc_hd__fill_1 FILLER_16_37 ();
 sky130_fd_sc_hd__decap_12 FILLER_16_64 ();
 sky130_fd_sc_hd__decap_8 FILLER_16_76 ();
 sky130_fd_sc_hd__fill_1 FILLER_16_85 ();
 sky130_fd_sc_hd__fill_1 FILLER_17_101 ();
 sky130_fd_sc_hd__decap_12 FILLER_17_15 ();
 sky130_fd_sc_hd__fill_1 FILLER_17_27 ();
 sky130_fd_sc_hd__decap_8 FILLER_17_29 ();
 sky130_fd_sc_hd__decap_12 FILLER_17_3 ();
 sky130_fd_sc_hd__fill_2 FILLER_17_37 ();
 sky130_fd_sc_hd__decap_12 FILLER_17_43 ();
 sky130_fd_sc_hd__fill_1 FILLER_17_55 ();
 sky130_fd_sc_hd__decap_12 FILLER_17_57 ();
 sky130_fd_sc_hd__decap_12 FILLER_17_69 ();
 sky130_fd_sc_hd__decap_3 FILLER_17_81 ();
 sky130_fd_sc_hd__decap_12 FILLER_17_85 ();
 sky130_fd_sc_hd__decap_4 FILLER_17_97 ();
 sky130_fd_sc_hd__decap_4 FILLER_1_101 ();
 sky130_fd_sc_hd__fill_1 FILLER_1_105 ();
 sky130_fd_sc_hd__fill_1 FILLER_1_15 ();
 sky130_fd_sc_hd__decap_12 FILLER_1_3 ();
 sky130_fd_sc_hd__decap_12 FILLER_1_57 ();
 sky130_fd_sc_hd__decap_12 FILLER_1_89 ();
 sky130_fd_sc_hd__decap_12 FILLER_2_15 ();
 sky130_fd_sc_hd__fill_1 FILLER_2_27 ();
 sky130_fd_sc_hd__decap_12 FILLER_2_29 ();
 sky130_fd_sc_hd__decap_12 FILLER_2_3 ();
 sky130_fd_sc_hd__fill_2 FILLER_2_41 ();
 sky130_fd_sc_hd__decap_12 FILLER_2_47 ();
 sky130_fd_sc_hd__decap_6 FILLER_2_59 ();
 sky130_fd_sc_hd__decap_4 FILLER_2_70 ();
 sky130_fd_sc_hd__decap_4 FILLER_2_80 ();
 sky130_fd_sc_hd__decap_12 FILLER_2_85 ();
 sky130_fd_sc_hd__fill_1 FILLER_2_97 ();
 sky130_fd_sc_hd__fill_2 FILLER_3_15 ();
 sky130_fd_sc_hd__decap_12 FILLER_3_37 ();
 sky130_fd_sc_hd__decap_6 FILLER_3_49 ();
 sky130_fd_sc_hd__fill_1 FILLER_3_55 ();
 sky130_fd_sc_hd__decap_3 FILLER_3_57 ();
 sky130_fd_sc_hd__fill_2 FILLER_3_63 ();
 sky130_fd_sc_hd__decap_6 FILLER_3_69 ();
 sky130_fd_sc_hd__decap_8 FILLER_3_7 ();
 sky130_fd_sc_hd__decap_6 FILLER_3_80 ();
 sky130_fd_sc_hd__fill_1 FILLER_4_105 ();
 sky130_fd_sc_hd__decap_4 FILLER_4_23 ();
 sky130_fd_sc_hd__fill_1 FILLER_4_27 ();
 sky130_fd_sc_hd__decap_12 FILLER_4_29 ();
 sky130_fd_sc_hd__decap_12 FILLER_4_41 ();
 sky130_fd_sc_hd__decap_12 FILLER_4_67 ();
 sky130_fd_sc_hd__decap_4 FILLER_4_79 ();
 sky130_fd_sc_hd__fill_1 FILLER_4_83 ();
 sky130_fd_sc_hd__decap_12 FILLER_4_85 ();
 sky130_fd_sc_hd__decap_8 FILLER_4_97 ();
 sky130_fd_sc_hd__decap_4 FILLER_5_101 ();
 sky130_fd_sc_hd__fill_1 FILLER_5_105 ();
 sky130_fd_sc_hd__decap_12 FILLER_5_15 ();
 sky130_fd_sc_hd__decap_8 FILLER_5_27 ();
 sky130_fd_sc_hd__decap_12 FILLER_5_3 ();
 sky130_fd_sc_hd__fill_1 FILLER_5_35 ();
 sky130_fd_sc_hd__decap_6 FILLER_5_64 ();
 sky130_fd_sc_hd__decap_12 FILLER_5_77 ();
 sky130_fd_sc_hd__decap_12 FILLER_5_89 ();
 sky130_fd_sc_hd__fill_1 FILLER_6_105 ();
 sky130_fd_sc_hd__decap_8 FILLER_6_11 ();
 sky130_fd_sc_hd__fill_2 FILLER_6_19 ();
 sky130_fd_sc_hd__decap_12 FILLER_6_29 ();
 sky130_fd_sc_hd__decap_6 FILLER_6_41 ();
 sky130_fd_sc_hd__decap_12 FILLER_6_55 ();
 sky130_fd_sc_hd__decap_8 FILLER_6_67 ();
 sky130_fd_sc_hd__fill_1 FILLER_6_75 ();
 sky130_fd_sc_hd__decap_4 FILLER_6_80 ();
 sky130_fd_sc_hd__decap_12 FILLER_6_85 ();
 sky130_fd_sc_hd__decap_8 FILLER_6_97 ();
 sky130_fd_sc_hd__fill_1 FILLER_7_101 ();
 sky130_fd_sc_hd__fill_1 FILLER_7_33 ();
 sky130_fd_sc_hd__decap_3 FILLER_7_53 ();
 sky130_fd_sc_hd__decap_12 FILLER_7_57 ();
 sky130_fd_sc_hd__fill_2 FILLER_7_69 ();
 sky130_fd_sc_hd__decap_6 FILLER_7_7 ();
 sky130_fd_sc_hd__fill_2 FILLER_7_81 ();
 sky130_fd_sc_hd__decap_6 FILLER_7_95 ();
 sky130_fd_sc_hd__decap_8 FILLER_8_29 ();
 sky130_fd_sc_hd__decap_3 FILLER_8_37 ();
 sky130_fd_sc_hd__fill_2 FILLER_8_65 ();
 sky130_fd_sc_hd__fill_1 FILLER_8_72 ();
 sky130_fd_sc_hd__decap_4 FILLER_8_79 ();
 sky130_fd_sc_hd__fill_1 FILLER_8_83 ();
 sky130_fd_sc_hd__fill_1 FILLER_8_85 ();
 sky130_fd_sc_hd__fill_1 FILLER_9_105 ();
 sky130_fd_sc_hd__decap_12 FILLER_9_19 ();
 sky130_fd_sc_hd__decap_12 FILLER_9_34 ();
 sky130_fd_sc_hd__decap_8 FILLER_9_46 ();
 sky130_fd_sc_hd__fill_2 FILLER_9_54 ();
 sky130_fd_sc_hd__decap_4 FILLER_9_62 ();
 sky130_fd_sc_hd__decap_12 FILLER_9_7 ();
 sky130_fd_sc_hd__decap_12 FILLER_9_73 ();
 sky130_fd_sc_hd__decap_12 FILLER_9_85 ();
 sky130_fd_sc_hd__decap_8 FILLER_9_97 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_0_Left_18 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_0_Right_0 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_10_Left_28 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_10_Right_10 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_11_Left_29 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_11_Right_11 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_12_Left_30 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_12_Right_12 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_13_Left_31 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_13_Right_13 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_14_Left_32 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_14_Right_14 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_15_Left_33 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_15_Right_15 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_16_Left_34 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_16_Right_16 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_17_Left_35 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_17_Right_17 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_1_Left_19 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_1_Right_1 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_2_Left_20 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_2_Right_2 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_3_Left_21 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_3_Right_3 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_4_Left_22 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_4_Right_4 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_5_Left_23 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_5_Right_5 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_6_Left_24 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_6_Right_6 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_7_Left_25 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_7_Right_7 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_8_Left_26 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_8_Right_8 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_9_Left_27 ();
 sky130_fd_sc_hd__decap_3 PHY_EDGE_ROW_9_Right_9 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_0_36 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_0_37 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_0_38 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_10_52 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_10_53 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_11_54 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_12_55 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_12_56 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_13_57 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_14_58 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_14_59 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_15_60 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_16_61 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_16_62 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_17_63 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_17_64 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_17_65 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_1_39 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_2_40 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_2_41 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_3_42 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_4_43 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_4_44 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_5_45 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_6_46 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_6_47 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_7_48 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_8_49 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_8_50 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_TAPCELL_ROW_9_51 ();
 sky130_fd_sc_hd__inv_1 _38_ (.A(\b_reg[1] ),
    .Y(_00_));
 sky130_fd_sc_hd__inv_1 _39_ (.A(\a_reg[1] ),
    .Y(_01_));
 sky130_fd_sc_hd__o2111ai_1 _40_ (.A1(\a_reg[0] ),
    .A2(\a_reg[2] ),
    .B1(\b_reg[1] ),
    .C1(\b_reg[0] ),
    .D1(\a_reg[1] ),
    .Y(_08_));
 sky130_fd_sc_hd__nand3_1 _41_ (.A(\b_reg[1] ),
    .B(\a_reg[1] ),
    .C(_08_),
    .Y(_09_));
 sky130_fd_sc_hd__and3_1 _42_ (.A(_04_),
    .B(_07_),
    .C(_09_),
    .X(_10_));
 sky130_fd_sc_hd__a21oi_1 _43_ (.A1(_07_),
    .A2(_09_),
    .B1(_04_),
    .Y(_11_));
 sky130_fd_sc_hd__nor2_1 _44_ (.A(_10_),
    .B(_11_),
    .Y(\adder_rows[2].adders[0].fa.sum ));
 sky130_fd_sc_hd__and2_0 _45_ (.A(\a_reg[1] ),
    .B(\b_reg[2] ),
    .X(_12_));
 sky130_fd_sc_hd__nand2_1 _46_ (.A(\a_reg[3] ),
    .B(\b_reg[0] ),
    .Y(_13_));
 sky130_fd_sc_hd__xor2_1 _47_ (.A(_05_),
    .B(_13_),
    .X(_14_));
 sky130_fd_sc_hd__xnor2_1 _48_ (.A(_08_),
    .B(_14_),
    .Y(_15_));
 sky130_fd_sc_hd__xor3_1 _49_ (.A(_11_),
    .B(_12_),
    .C(_15_),
    .X(_16_));
 sky130_fd_sc_hd__and2_0 _50_ (.A(\b_reg[0] ),
    .B(\a_reg[0] ),
    .X(\pp[0][0] ));
 sky130_fd_sc_hd__and3_1 _51_ (.A(\a_reg[0] ),
    .B(\b_reg[3] ),
    .C(_16_),
    .X(_17_));
 sky130_fd_sc_hd__a21oi_1 _52_ (.A1(\a_reg[0] ),
    .A2(\b_reg[3] ),
    .B1(_16_),
    .Y(_18_));
 sky130_fd_sc_hd__nor2_1 _53_ (.A(_17_),
    .B(_18_),
    .Y(\adder_rows[3].adders[0].fa.sum ));
 sky130_fd_sc_hd__nand2_1 _54_ (.A(\a_reg[1] ),
    .B(\b_reg[3] ),
    .Y(_19_));
 sky130_fd_sc_hd__inv_1 _55_ (.A(_19_),
    .Y(_20_));
 sky130_fd_sc_hd__and2_0 _56_ (.A(\a_reg[2] ),
    .B(\b_reg[2] ),
    .X(_21_));
 sky130_fd_sc_hd__a21oi_1 _57_ (.A1(_02_),
    .A2(_05_),
    .B1(_13_),
    .Y(_22_));
 sky130_fd_sc_hd__nand2_1 _58_ (.A(\a_reg[3] ),
    .B(\b_reg[1] ),
    .Y(_23_));
 sky130_fd_sc_hd__a21oi_1 _59_ (.A1(_06_),
    .A2(_23_),
    .B1(_22_),
    .Y(_24_));
 sky130_fd_sc_hd__maj3_1 _60_ (.A(_11_),
    .B(_12_),
    .C(_15_),
    .X(_25_));
 sky130_fd_sc_hd__nand3_1 _61_ (.A(\b_reg[1] ),
    .B(\a_reg[1] ),
    .C(\pp[0][0] ),
    .Y(_02_));
 sky130_fd_sc_hd__xor3_1 _62_ (.A(_21_),
    .B(_24_),
    .C(_25_),
    .X(_26_));
 sky130_fd_sc_hd__xnor2_1 _63_ (.A(_17_),
    .B(_26_),
    .Y(_27_));
 sky130_fd_sc_hd__xnor2_1 _64_ (.A(_20_),
    .B(_27_),
    .Y(\adder_rows[3].adders[1].fa.sum ));
 sky130_fd_sc_hd__nand2_1 _65_ (.A(\a_reg[2] ),
    .B(\b_reg[3] ),
    .Y(_28_));
 sky130_fd_sc_hd__inv_1 _66_ (.A(_28_),
    .Y(_29_));
 sky130_fd_sc_hd__and2_0 _67_ (.A(\a_reg[3] ),
    .B(\b_reg[2] ),
    .X(_30_));
 sky130_fd_sc_hd__maj3_1 _68_ (.A(_21_),
    .B(_24_),
    .C(_25_),
    .X(_31_));
 sky130_fd_sc_hd__xor3_1 _69_ (.A(_22_),
    .B(_30_),
    .C(_31_),
    .X(_32_));
 sky130_fd_sc_hd__maj3_1 _70_ (.A(_17_),
    .B(_20_),
    .C(_26_),
    .X(_33_));
 sky130_fd_sc_hd__xnor2_1 _71_ (.A(_32_),
    .B(_33_),
    .Y(_34_));
 sky130_fd_sc_hd__a22oi_1 _72_ (.A1(\b_reg[0] ),
    .A2(\a_reg[1] ),
    .B1(\a_reg[0] ),
    .B2(\b_reg[1] ),
    .Y(_03_));
 sky130_fd_sc_hd__xnor2_1 _73_ (.A(_29_),
    .B(_34_),
    .Y(\adder_rows[3].adders[2].fa.sum ));
 sky130_fd_sc_hd__nand2_1 _74_ (.A(\a_reg[3] ),
    .B(\b_reg[3] ),
    .Y(_35_));
 sky130_fd_sc_hd__o21a_1 _75_ (.A1(_22_),
    .A2(_31_),
    .B1(_30_),
    .X(_36_));
 sky130_fd_sc_hd__maj3_1 _76_ (.A(_29_),
    .B(_32_),
    .C(_33_),
    .X(_37_));
 sky130_fd_sc_hd__xnor3_1 _77_ (.A(_35_),
    .B(_36_),
    .C(_37_),
    .X(\adder_rows[3].adders[3].fa.sum ));
 sky130_fd_sc_hd__o21ba_1 _78_ (.A1(_36_),
    .A2(_37_),
    .B1_N(_35_),
    .X(\adder_rows[3].adders[3].fa.cout ));
 sky130_fd_sc_hd__a31oi_1 _79_ (.A1(\b_reg[1] ),
    .A2(\a_reg[1] ),
    .A3(\pp[0][0] ),
    .B1(_03_),
    .Y(\adder_rows[1].adders[0].fa.sum ));
 sky130_fd_sc_hd__nand2_1 _80_ (.A(\a_reg[0] ),
    .B(\b_reg[2] ),
    .Y(_04_));
 sky130_fd_sc_hd__nand2_1 _81_ (.A(\b_reg[1] ),
    .B(\a_reg[2] ),
    .Y(_05_));
 sky130_fd_sc_hd__nand4_1 _82_ (.A(\b_reg[1] ),
    .B(\b_reg[0] ),
    .C(\a_reg[1] ),
    .D(\a_reg[2] ),
    .Y(_06_));
 sky130_fd_sc_hd__o311ai_0 _83_ (.A1(_00_),
    .A2(_01_),
    .A3(\a_reg[0] ),
    .B1(\a_reg[2] ),
    .C1(\b_reg[0] ),
    .Y(_07_));
 sky130_fd_sc_hd__dfrtp_1 _84_ (.CLK(clknet_1_0__leaf_clk),
    .D(\pp[0][0] ),
    .RESET_B(net9),
    .Q(net10));
 sky130_fd_sc_hd__dfrtp_1 _85_ (.CLK(clknet_1_0__leaf_clk),
    .D(\adder_rows[1].adders[0].fa.sum ),
    .RESET_B(net9),
    .Q(net11));
 sky130_fd_sc_hd__dfrtp_1 _86_ (.CLK(clknet_1_1__leaf_clk),
    .D(\adder_rows[2].adders[0].fa.sum ),
    .RESET_B(net9),
    .Q(net12));
 sky130_fd_sc_hd__dfrtp_1 _87_ (.CLK(clknet_1_1__leaf_clk),
    .D(\adder_rows[3].adders[0].fa.sum ),
    .RESET_B(net9),
    .Q(net13));
 sky130_fd_sc_hd__dfrtp_1 _88_ (.CLK(clknet_1_1__leaf_clk),
    .D(\adder_rows[3].adders[1].fa.sum ),
    .RESET_B(net9),
    .Q(net14));
 sky130_fd_sc_hd__dfrtp_1 _89_ (.CLK(clknet_1_1__leaf_clk),
    .D(\adder_rows[3].adders[2].fa.sum ),
    .RESET_B(net9),
    .Q(net15));
 sky130_fd_sc_hd__dfrtp_1 _90_ (.CLK(clknet_1_1__leaf_clk),
    .D(\adder_rows[3].adders[3].fa.sum ),
    .RESET_B(net9),
    .Q(net16));
 sky130_fd_sc_hd__dfrtp_1 _91_ (.CLK(clknet_1_1__leaf_clk),
    .D(\adder_rows[3].adders[3].fa.cout ),
    .RESET_B(net9),
    .Q(net17));
 sky130_fd_sc_hd__dfrtp_1 _92_ (.CLK(clknet_1_0__leaf_clk),
    .D(net1),
    .RESET_B(net9),
    .Q(\a_reg[0] ));
 sky130_fd_sc_hd__dfrtp_1 _93_ (.CLK(clknet_1_0__leaf_clk),
    .D(net2),
    .RESET_B(net9),
    .Q(\a_reg[1] ));
 sky130_fd_sc_hd__dfrtp_1 _94_ (.CLK(clknet_1_0__leaf_clk),
    .D(net3),
    .RESET_B(net9),
    .Q(\a_reg[2] ));
 sky130_fd_sc_hd__dfrtp_1 _95_ (.CLK(clknet_1_0__leaf_clk),
    .D(net4),
    .RESET_B(net9),
    .Q(\a_reg[3] ));
 sky130_fd_sc_hd__dfrtp_1 _96_ (.CLK(clknet_1_0__leaf_clk),
    .D(net5),
    .RESET_B(net9),
    .Q(\b_reg[0] ));
 sky130_fd_sc_hd__dfrtp_1 _97_ (.CLK(clknet_1_0__leaf_clk),
    .D(net6),
    .RESET_B(net9),
    .Q(\b_reg[1] ));
 sky130_fd_sc_hd__dfrtp_1 _98_ (.CLK(clknet_1_0__leaf_clk),
    .D(net7),
    .RESET_B(net9),
    .Q(\b_reg[2] ));
 sky130_fd_sc_hd__dfrtp_1 _99_ (.CLK(clknet_1_1__leaf_clk),
    .D(net8),
    .RESET_B(net9),
    .Q(\b_reg[3] ));
 sky130_fd_sc_hd__clkbuf_16 clkbuf_0_clk (.A(clk),
    .X(clknet_0_clk));
 sky130_fd_sc_hd__clkbuf_16 clkbuf_1_0__f_clk (.A(clknet_0_clk),
    .X(clknet_1_0__leaf_clk));
 sky130_fd_sc_hd__clkbuf_16 clkbuf_1_1__f_clk (.A(clknet_0_clk),
    .X(clknet_1_1__leaf_clk));
 sky130_fd_sc_hd__clkbuf_8 clkload0 (.A(clknet_1_1__leaf_clk));
 sky130_fd_sc_hd__buf_2 input1 (.A(a[0]),
    .X(net1));
 sky130_fd_sc_hd__buf_2 input2 (.A(a[1]),
    .X(net2));
 sky130_fd_sc_hd__buf_2 input3 (.A(a[2]),
    .X(net3));
 sky130_fd_sc_hd__buf_2 input4 (.A(a[3]),
    .X(net4));
 sky130_fd_sc_hd__buf_2 input5 (.A(b[0]),
    .X(net5));
 sky130_fd_sc_hd__buf_2 input6 (.A(b[1]),
    .X(net6));
 sky130_fd_sc_hd__buf_2 input7 (.A(b[2]),
    .X(net7));
 sky130_fd_sc_hd__buf_2 input8 (.A(b[3]),
    .X(net8));
 sky130_fd_sc_hd__buf_2 input9 (.A(rst_n),
    .X(net9));
 sky130_fd_sc_hd__buf_2 output10 (.A(net10),
    .X(p[0]));
 sky130_fd_sc_hd__buf_2 output11 (.A(net11),
    .X(p[1]));
 sky130_fd_sc_hd__buf_2 output12 (.A(net12),
    .X(p[2]));
 sky130_fd_sc_hd__buf_2 output13 (.A(net13),
    .X(p[3]));
 sky130_fd_sc_hd__buf_2 output14 (.A(net14),
    .X(p[4]));
 sky130_fd_sc_hd__buf_2 output15 (.A(net15),
    .X(p[5]));
 sky130_fd_sc_hd__buf_2 output16 (.A(net16),
    .X(p[6]));
 sky130_fd_sc_hd__buf_2 output17 (.A(net17),
    .X(p[7]));
endmodule
