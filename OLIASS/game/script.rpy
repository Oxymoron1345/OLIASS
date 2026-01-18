# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.
label MSCharacter:
    define M = Character("MINATO", color="#44aaec")
    define WAN = Character("MINATO (as enemy soulja WAN)", color="#44aaec")
    define A = Character("AKIYUKI", color="#78cc38")
    define K = Character("KEISUKE", color="#ff0000")
    define HN = Character("HIDEKI", color="#808080")
    define TUU = Character("HIDEKI (as enemy soulja TUU)", color="#808080")
    define R = Character("RORO", color="#808080")
    define C = Character("GREG", color="#808080")
    define MI = Character("MARUIKO", color="#808080")
    define JNE = Character("JEIN", color="#808080")
    define CAM = Character("KAIMON", color="#808080")
    define BM = Character("SEIDOHITO", color="#808080")
    define SDK = Character("SHELDRIEKA", color="#808080")
    define TY = Character("SAKI", color="#808080")
    define EI = Character("GHETTO EI", color="#808080")
    define ONE = Character("SOLDIER ONE", color="#808080")
    define BII = Character("GHETTO BII", color="#808080")
    define TWO = Character("SOLDIER TWO", color="#808080")
    define GNG = Character("JUN", color="#808080")
    define NPB = Character("JUN (as newspaper boy)", color="#808080")
    define SHR = Character("SHEMAR", color="#808080")
    define LYN = Character("RIN", color="#808080")
    define RIN = Character("SUKIKO", color="#808080")
    define TIN = Character("TOMOKO", color="#808080")
    define JEN = Character("JENIFA", color="#808080")
    define RT = Character("SUKIKO & TOMOKO", color="#808080")
    define RR = Character("BERI-SENSEI", color="#808080")
    define HKMR = Character("HIDEKI, KEISUKE, MINATO, RORO", color="#000000")
    define AT = Character("AKIYUKI & RORO", color="#000000")
    define OGZ = Character("ORIGAMI ZODA", color="#808080")
    define FOS = Character("FUMINO-SENSEI", color="#808080")
    define DUE = Character("DAIKI-SENSEI", color="#808080")
    define SEN = Character("SENSEI", color="#808080")
    define BD = Character("BUS DRIVER", color="#808080")
    define MP = Character("MYSTERIOUS PLAYER", color="#808080")
    define BEE = Character("THIRD GRADER GIRL", color="#808080")
    define RF = Character("RORO'S FATHER", color="#808080")
    define MA = Character("MINATO & AKIYUKI", color="#000000")
    define MAK = Character("MINATO, AKIYUKI, KEISUKE", color="#000000")
    define MGO = Character("MOVIE GOER ONE", color="#808080")
    define MGT = Character("MOVIE GOER TWO", color="#808080")
    define ZUR = Character("ZULGAR", color="#808080")
    define CYS = Character("SYSERO", color="#808080")
    define IST = Character("RECEPTIONIST", color="#808080")
    define BP = Character("BACPACK", color="#808080")
    define FA = Character("FARMER A", color="#808080")
    define WOS = Character("WARRIOR OVERSEER", color="#808080")
    define WK = Character("WEST KING", color="#FFD700")
    return
label HSCharacter:
    define MH = Character("MINATO", color="#44aaec")
    define AH = Character("AKIYUKI", color="#78cc38")
    define KH = Character("KEISUKE", color="#ff0000")
    define MK = Character("MINATO & KEISUKE", color="#000000")
    define AK = Character("AKIYUKI & KEISUKE", color="#000000")
    define THO = Character("TANAKA", color="#808080")
    define XC = Character("CHIBA", color="#808080")
    define TET = Character("MISHIMA", color="#808080")
    define ETM = Character("EI & TANAKA & MISHIMA", color="#000000")
    define ALI = Character("ASUKA", color="#808080")
    define RUT = Character("RUMI", color="#808080")
    define ANA = Character("AKANE", color="#808080")
    define ELI = Character("ERIKO", color="#808080")
    define CAT = Character("CHIZURU", color="#808080")
    define AC = Character("ASUKA & CHIZURU", color="#000000")
    define CAR = Character("ASUKA, RUMI, CHIZURU", color="#000000")
    define TRT = Character("THE RIOT", color="#808080")
    define TSB = Character("TSB", color="#808080")
    define BRO = Character("\"BRO\"", color="#808080")
    define STU = Character("STUDENT", color="#808080")
    define HEI = Character("EI", color="#808080")
    define TEI = Character("TWIN EI", color="#808080")
    define HBI = Character("BII", color="#808080")
    define TBI = Character("TWIN BII", color="#808080")
    define TEB = Character("TWIN EI & TWIN BII", color="#000000")
    define TES = Character("TWIN EI, TWIN BII, TSB", color="#000000")
    define DAB = Character("DABURA", color="#808080")
    define ABD = Character("ATSUSHI", color="#808080")
    define KAS = Character("KIYOTAKA", color="#808080")
    define BGF = Character("BLACK, GAY, FIRST-YEAR STUDENT", color="#808080")
    define LAN = Character("RANDORI", color="#808080")
    define TRE = Character("PARUKA", color="#808080")
    define BRE = Character("FEBREEZE", color="#808080")
    define SAE = Character("SAE", color="#808080")
    define HUK = Character("HIRO", color="#808080")
    define DSN = Character("DONALDVILLE", color="#808080")
    define ASN = Character("AKIYUKI & DONALDVILLE", color="#000000")
    define DVD = Character("COACH DAVID", color="#808080")
    define FBA = Character("FUKA", color="#808080")
    define FAT = Character("PRINCIPAL", color="#808080")
    define E = Character("EVERYONE", color="#000000")
    define EEA = Character("EVERYONE EXCEPT AKIYUKI", color="#000000")
    return
label sprites:
    label MS:
        label Minato:
            image M_W = im.Scale("sprites/Minato/M_W.png", 550,650)
            image M_W_frown = im.Scale("sprites/Minato/M_W_frown.png", 550,650)
            image M_W_heartbroken = im.Scale("sprites/Minato/M_W_heartbroken.png", 550,650)
            image M_W_shock = im.Scale("sprites/Minato/M_W_shock.png", 550,650)
            image M_S = im.Scale("sprites/Minato/M_S.png", 550,650)
            image M_S_frown = im.Scale("sprites/Minato/M_S_frown.png", 550,650)
            image M_S_heartbroken = im.Scale("sprites/Minato/M_S_heartbroken.png", 550,650)
            image M_W_shock = im.Scale("sprites/Minato/M_W_shock.png", 550,650)
            image M_G = im.Scale("sprites/Minato/M_G.png", 550,650)
            image M_G_shock = im.Scale("sprites/Minato/M_G_shock.png", 550,650)
            image M_G_startled = im.Scale("sprites/Minato/M_G_startled.png", 550,650)
            image M_C = im.Scale("sprites/Minato/M_C.png", 550,650)
            image M_C_shock = im.Scale("sprites/Minato/M_C_shock.png", 550,650)

        label Akiyuki:
            image A_W = im.Scale("sprites/Akiyuki/A_W.png", 550,650)
            image A_W_frown = im.Scale("sprites/Akiyuki/A_W_frown.png", 550,650)
            image A_W_motivated = im.Scale("sprites/Akiyuki/A_W_motivated.png", 550,650)
            image A_W_shock = im.Scale("sprites/Akiyuki/A_W_shock.png", 550,650)
            image A_S = im.Scale("sprites/Akiyuki/A_S.png", 550,650)
            image A_S_frown = im.Scale("sprites/Akiyuki/A_S_frown.png", 550,650)
            image A_C = im.Scale("sprites/Akiyuki/A_C.png", 550,650)
            image A_C_shock = im.Scale("sprites/Akiyuki/A_C_shock.png", 550,650)
            image A_C_smug = im.Scale("sprites/Akiyuki/A_C_smug.png", 550,650)

        label Keisuke:
            image K_W = im.Scale("sprites/Keisuke/K_W.png", 550,650)
            image K_W_frown = im.Scale("sprites/Keisuke/K_W_frown.png", 550,650)
            image K_W_shock = im.Scale("sprites/Keisuke/K_W_shock.png", 550,650)
            image K_S = im.Scale("sprites/Keisuke/K_S.png", 550,650)
            image K_C = im.Scale("sprites/Keisuke/K_C.png", 550,650)
            image K_C_shock = im.Scale("sprites/Keisuke/K_C_shock.png", 550,650)

        label Greg:
            image C_W = im.Scale("sprites/Greg/C_W.png", 550,650)
            image C_W_asthma = im.Scale("sprites/Greg/C_W_asthma.png", 550,650)
            image C_W_pout = im.Scale("sprites/Greg/C_W_pout.png", 550,650)
            image C_S = im.Scale("sprites/Greg/C_S.png", 550,650)
            image C_S_asthma = im.Scale("sprites/Greg/C_S_asthma.png", 550,650)

        label Roro:
            image R_W = im.Scale("sprites/Roro/R_W.png", 550,650)
            image R_W_shock = im.Scale("sprites/Roro/R_W_shock.png", 550,650)
            image R_W_smile = im.Scale("sprites/Roro/R_W_smile.png", 550,650)
            image R_W_startled = im.Scale("sprites/Roro/R_W_startled.png", 550,650)
            image R_S = im.Scale("sprites/Roro/R_S.png", 550,650)

        label Saki:
            image TY_W = im.Scale("sprites/Saki/TY_W.png", 550,650)
            image TY_W_shy = im.Scale("sprites/Saki/TY_W_shy.png", 550,650)
            image TY_W_smile = im.Scale("sprites/Saki/TY_W_smile.png", 550,650)
            image TY_S = im.Scale("sprites/Saki/TY_S.png", 550,650)
            image TY_S_shy = im.Scale("sprites/Saki/TY_S_shy.png", 550,650)

        label Hideki:
            image HN_W = im.Scale("sprites/Hideki/HN_W.png", 550,650)
            image HN_W_shock = im.Scale("sprites/Hideki/HN_W_shock.png", 550,650)
            image HN_W_startled = im.Scale("sprites/Hideki/HN_W_startled.png", 550,650)
            image HN_S = im.Scale("sprites/Hideki/HN_S.png", 550,650)
            image HN_naked = im.Scale("sprites/Hideki/HN_naked.png", 550,650)

        label Kaimon:
            image CAM_W = im.Scale("sprites/Kaimon/CAM_W.png", 550,650)
            image CAM_W_shock = im.Scale("sprites/Kaimon/CAM_W_shock.png", 550,650)
            image CAM_S = im.Scale("sprites/Kaimon/CAM_S.png", 550,650)
            image CAM_S_shock = im.Scale("sprites/Kaimon/CAM_S_shock.png", 550,650)

        label Jun:
            image GNG_W = im.Scale("sprites/Jun/GNG_W.png", 550,650)
            image GNG_S = im.Scale("sprites/Jun/GNG_S.png", 550,650)

        label Shemar:
            image SHR_W = im.Scale("sprites/Shemar/SHR_W.png", 550,650)

        label Ghetto:
            image GTA_W = im.Scale("sprites/Ghetto/GTA_W.png", 550,650)
            image GTB_W = im.Scale("sprites/Ghetto/GTB_W.png", 550,650)
            image GTA_S = im.Scale("sprites/Ghetto/GTA_S.png", 550,650)
            image GTB_S = im.Scale("sprites/Ghetto/GTB_S.png", 550,650)

        label Seidohito:
            image BM = im.Scale("sprites/Seidohito.png", 550,650)

        label Maruiko:
            image MI_W = im.Scale("sprites/Maruiko/MI_W.png", 550,650)
            image MI_W_angry = im.Scale("sprites/Maruiko/MI_W_angry.png", 550,650)
            image MI_W_pout = im.Scale("sprites/Maruiko/MI_W_pout.png", 550,650)

        label Sheldrieka:
            image SDK_W_shout = im.Scale("sprites/Sheldrieka/SDK_W_shout.png", 550,650)
            image SDK_W_sniff = im.Scale("sprites/Sheldrieka/SDK_W_sniff.png", 550,650)
            image SDK_S_shout = im.Scale("sprites/Sheldrieka/SDK_S_shout.png", 550,650)
            image SDK_S_sniff = im.Scale("sprites/Sheldrieka/SDK_S_sniff.png", 550,650)

        label Sukiko:
            image RIN_W = im.Scale("sprites/Sukiko/RIN_W.png", 550,650)
            image RIN_W_shock = im.Scale("sprites/Sukiko/RIN_W_shock.png", 550,650)

        label Jenifa:
            image JEN_W = im.Scale("sprites/Jenifa/JEN_W.png", 550,650)
            image JEN_W_angry = im.Scale("sprites/Jenifa/JEN_W_angry.png", 550,650)

        label Tomoko:
            image TIN_W = im.Scale("sprites/Tomoko/TIN_W.png", 550,650)
            image TIN_W_shock = im.Scale("sprites/Tomoko/TIN_W_shock.png", 550,650)

        label Jein:
            image JNE_W = im.Scale("sprites/Jein/JNE_W.png", 550,650)
            image JNE_W_pout = im.Scale("sprites/Jein/JNE_W_pout.png", 550,650)

        label Rin:
            image LYN = im.Scale("sprites/Rin.png", 550,650)

        label Fumino:
            image FOS = im.Scale("sprites/Fumino/FOS.png", 980,840)
            image FOS_angry = im.Scale("sprites/Fumino/FOS_angry.png", 980,840)
            image FOS_shout = im.Scale("sprites/Fumino/FOS_shout.png", 980,840)

        label Daiki:
            image DUE = im.Scale("sprites/Daiki/DUE.png", 720,900)
            image DUE_angry = im.Scale("sprites/Daiki/DUE_angry.png", 720,900)
            image DUE_cry = im.Scale("sprites/Daiki/DUE_cry.png", 720,900)
            image DUE_distraught = im.Scale("sprites/Daiki/DUE_distraught.png", 720,900)
            image DUE_shock = im.Scale("sprites/Daiki/DUE_shock.png", 720,900)
            image DUE_smug = im.Scale("sprites/Daiki/DUE_smug.png", 720,900)

        label Beri:
            image RR = im.Scale("sprites/Beri/RR.png", 980,840)
            image RR_angry = im.Scale("sprites/Beri/RR_angry.png", 980,840)
            image RR_shout = im.Scale("sprites/Beri/RR_shout.png", 980,840)

        label ThirdGraderGirl:
            image BEE = im.Scale("sprites/third_grader.png", 550,650)
    label HS:
        label MinatoH:
            image MH_W = im.Scale("sprites/Minato/MH_W.png", 550,650)
            image MH_W_frown = im.Scale("sprites/Minato/MH_W_frown.png", 550,650)
            image MH_W_horny = im.Scale("sprites/Minato/MH_W_horny.png", 550,650)
            image MH_W_heartbroken = im.Scale("sprites/Minato/MH_W_heartbroken.png", 550,650)
            image MH_W_breedable = im.Scale("sprites/Minato/MH_W_breedable.png", 550,650)
            image MH_S = im.Scale("sprites/Minato/MH_S.png", 550,650)
            image MH_S frown = im.Scale("sprites/Minato/MH_S_frown.png", 550,650)
            image MH_S horny = im.Scale("sprites/Minato/MH_S_horny.png", 550,650)
            image MH_S heartbroken = im.Scale("sprites/Minato/MH_S_heartbroken.png", 550,650)
            image MH_S breedable = im.Scale("sprites/Minato/MH_S_breedable.png", 550,650)
            image MH_C_frown = im.Scale("sprites/Minato/MH_C_frown.png", 550,650)
            image MH_C_horny = im.Scale("sprites/Minato/MH_C_horny.png", 550,650)
            image MH_C_heartbroken = im.Scale("sprites/Minato/MH_C_heartbroken.png", 550,650)
            image MH_naked_horny = im.Scale("sprites/Minato/MH_naked_horny.png", 550,650)
        label AkiyukiH:
            image AH_W = im.Scale("sprites/Akiyuki/AH_W.png", 550,650)
            image AH_W_cry = im.Scale("sprites/Akiyuki/AH_W_cry.png", 550,650)
            image AH_S = im.Scale("sprites/Akiyuki/AH_S.png", 550,650)
            image AH_S_frown = im.Scale("sprites/Akiyuki/AH_S_frown.png", 550,650)
            image AH_C = im.Scale("sprites/Akiyuki/AH_C.png", 550,650)
            image AH_C_frown = im.Scale("sprites/Akiyuki/AH_C_frown.png", 550,650)
        label KeisukeH:
            image KH_W = im.Scale("sprites/Keisuke/KH_W.png", 550,650)
            image KH_W_shock = im.Scale("sprites/Keisuke/K_W_shock.png", 550,650)
            image KH_S = im.Scale("sprites/Keisuke/KH_S.png", 550,650)
            image KH_C = im.Scale("sprites/Keisuke/KH_C.png", 550,650)
        label Chiba:
            image XC_W = im.Scale("sprites/Chiba/XC_W.png", 550,650)
            image XC_W_angry = im.Scale("sprites/Chiba/XC_W_angry.png", 550,650)
            image XC_W_shout = im.Scale("sprites/Chiba/XC_W_shout.png", 550,650)
            image XC_S = im.Scale("sprites/Chiba/XC_S.png", 550,650)
            image XC_S_angry = im.Scale("sprites/Chiba/XC_S_angry.png", 550,650)
        label Tanaka:
            image THO_W = im.Scale("sprites/Tanaka/THO_W.png", 550,650)
            image THO_S = im.Scale("sprites/Tanaka/THO_S.png", 550,650)
            image THO_naked = im.Scale("sprites/Tanaka/THO_naked.png", 550,650)
        label Mishima:
            image TET_W = im.Scale("sprites/Mishima/TET_W.png", 550,650)
            image TET_W_frown = im.Scale("sprites/Mishima/TET_W_frown.png", 550,650)
            image TET_S = im.Scale("sprites/Mishima/TET_S.png", 550,650)
            image TET_S_frown = im.Scale("sprites/Mishima/TET_S_frown.png", 550,650)
        label Twins:
            image TN_W = im.Scale("sprites/Twin/TN_W.png", 550,650)
            image TN_S = im.Scale("sprites/Twin/TN_S.png", 550,650)
            image TN_naked = im.Scale("sprites/Twin/TN_naked.png", 550,650)
        label TSBB:
            image TSB_W = im.Scale("sprites/TSBB/TSB_W.png", 550,650)
            image TSB_W_angry = im.Scale("sprites/TSBB/TSB_W_angry.png", 550,650)
            image TSB_W_stalk = im.Scale("sprites/TSBB/TSB_W_stalk.png", 550,650)
            image TSB_S = im.Scale("sprites/TSBB/TSB_S.png", 550,650)
            image TSB_S_angry = im.Scale("sprites/TSBB/TSB_S_angry.png", 550,650)
            image TSB_S_stalk = im.Scale("sprites/TSBB/TSB_S_stalk.png", 550,650)
            image TSB_naked = im.Scale("sprites/TSBB/TSB_naked.png", 550,650)
            image TSB_naked_stalk = im.Scale("sprites/TSBB/TSB_naked_stalk.png", 550,650)
        label TheRiot:
            image TRT_G = im.Scale("sprites/TheRiot/TRT_G.png", 550,650)
            image TRT_G_angry = im.Scale("sprites/TheRiot/TRT_G_angry.png", 550,650)
            image TRT_G_happy = im.Scale("sprites/TheRiot/TRT_G_happy.png", 550,650)
        label Bro:
            image BRO_G = im.Scale("sprites/Bro/BRO_G.png", 550,650)
            image BRO_G_angry = im.Scale("sprites/Bro/BRO_G_angry.png", 550,650)
            image BRO_G_happy = im.Scale("sprites/Bro/BRO_G_happy.png", 550,650)
        label Rumi:
            image RUT_G = im.Scale("sprites/Rumi/RUT_G.png", 550,650)
            image RUT_G_ass = im.Scale("sprites/Rumi/RUT_G_ass.png", 550,650)
            image RUT_G_horny = im.Scale("sprites/Rumi/RUT_G_horny.png", 550,650)
            image RUT_W = im.Scale("sprites/Rumi/RUT_W.png", 550,650)
            image RUT_W_ass = im.Scale("sprites/Rumi/RUT_W_ass.png", 550,650)
            image RUT_W_horny = im.Scale("sprites/Rumi/RUT_W_horny.png", 550,650)
            image RUT_S = im.Scale("sprites/Rumi/RUT_S.png", 550,650)
            image RUT_S_ass = im.Scale("sprites/Rumi/RUT_S_ass.png", 550,650)
            image RUT_S_horny = im.Scale("sprites/Rumi/RUT_S_horny.png", 550,650)
            image RUT_naked = im.Scale("sprites/Rumi/RUT_naked.png", 550,650)
            image RUT_naked_shock = im.Scale("sprites/Rumi/RUT_naked_shock.png", 550,650)
        label Chizuru:
            image CAT_G = im.Scale("sprites/Chizuru/CAT_G.png", 550,650)
            image CAT_W = im.Scale("sprites/Chizuru/CAT_W.png", 550,650)
            image CAT_S = im.Scale("sprites/Chizuru/CAT_S.png", 550,650)
            image CAT_naked = im.Scale("sprites/Chizuru/CAT_naked.png", 550,650)
        label Asuka:
            image ALI_G = im.Scale("sprites/Asuka/ALI_G.png", 550,650)
            image ALI_W = im.Scale("sprites/Asuka/ALI_W.png", 550,650)
            image ALI_W_angry = im.Scale("sprites/Asuka/ALI_W_angry.png", 550,650)
            image ALI__W_lust = im.Scale("sprites/Asuka/ALI_W_lust.png", 550,650)
            image ALI_S = im.Scale("sprites/Asuka/ALI_S.png", 550,650)
            image ALI_S_angry = im.Scale("sprites/Asuka/ALI_S_angry.png", 550,650)
            image ALI_naked = im.Scale("sprites/Asuka/ALI_naked.png", 550,650)
            image ALI_naked_shock = im.Scale("sprites/Asuka/ALI_naked_shock.png", 550,650)
        label Akane:
            image ANA_G = im.Scale("sprites/Akane/ANA_G.png", 550,650)
            image ANA_W = im.Scale("sprites/Akane/ANA_W.png", 550,650)
            image ANA_W_shock = im.Scale("sprites/Akane/ANA_W_shock.png", 550,650)
            image ANA_W_smile = im.Scale("sprites/Akane/ANA_W_smile.png", 550,650)
            image ANA_S = im.Scale("sprites/Akane/ANA_S.png", 550,650)
            image ANA_S_smile = im.Scale("sprites/Akane/ANA_S_smile.png", 550,650)
            image ANA_C = im.Scale("sprites/Akane/ANA_C.png", 550,650)
            image ANA_C_smile = im.Scale("sprites/Akane/ANA_C_smile.png", 550,650)
            image ANA_naked = im.Scale("sprites/Akane/ANA_naked.png", 550,650)
        label Eriko:
            image ELI_W = im.Scale("sprites/Eriko/ELI_W.png", 550,650)
            image ELI_S = im.Scale("sprites/Eriko/ELI_S.png", 550,650)
            image ELI_naked = im.Scale("sprites/Eriko/ELI_naked.png", 550,650)
        label Atsushi:
            image ABD_S = im.Scale("sprites/Atsushi/ABD_S.png", 550,650)
            image ABD_S_hyper = im.Scale("sprites/Atsushi/ABD_S_hyper.png", 550,650)
            image ABD_W = im.Scale("sprites/Atsushi/ABD_W.png", 550,650)
            image ABD_S_hyper = im.Scale("sprites/Atsushi/ABD_W_hyper.png", 550,650)
        label Randori:
            image LAN_W = im.Scale("sprites/Randori/LAN_W.png", 550,650)
            image LAN_W_agony = im.Scale("sprites/Randori/LAN_W_agony.png", 550,650)
        label Kiyotaka:
            image KAS_W = im.Scale("sprites/Kiyotaka/KAS_W.png", 550,650)
        label Paruka:
            image TRE_W = im.Scale("sprites/Paruka/TRE_W.png", 550,650)
            image TRE_S = im.Scale("sprites/Paruka/TRE_S.png", 550,650)
        label Hiro:
            image HUK = im.Scale("sprites/Hiro/HUK.png", 720,900)
        label Donaldville:
            image DSN = im.Scale("sprites/Donaldville/DSN.png", 980,840)
            image DSN_angry = im.Scale("sprites/Donaldville/DSN_angry.png", 980,840)
            image DSN_smug = im.Scale("sprites/Donaldville/DSN_smug.png", 980,840)
        label Fuka:
            image FBA = im.Scale("sprites/Fuka/FBA.png", 980,840)
            image FBA_angry = im.Scale("sprites/Fuka/FBA_angry.png", 980,840)
            image FBA_smug = im.Scale("sprites/Fuka/FBA_smug.png", 980,840)
            image FBA_vomit = im.Scale("sprites/Fuka/FBA_vomit.png", 980,840)
        label Sae:
            image SAE = im.Scale("sprites/Sae/SAE.png", 980,840)
            image SAE_smile = im.Scale("sprites/Sae/SAE_smile.png", 980,840)
            image SAE_shock = im.Scale("sprites/Sae/SAE_shock.png", 980,840)
label backgrounds:
    image ms_classroom_morning = im.Scale("backgrounds/ms_classroom_morning.jpg", 1920,1080)
    image ms_classroom_afternoon = im.Scale("backgrounds/ms_classroom_afternoon.jpg", 1920,1080)
    image ms_classroom_evening = im.Scale("backgrounds/ms_classroom_evening.jpg", 1920,1080)
    image ms_hallway = im.Scale("backgrounds/ms_hallway.jpg", 1920,1080)
    image ms_computer = im.Scale("backgrounds/ms_computer.jpg", 1920,1080)
    image ms_music = im.Scale("backgrounds/ms_music.jpg", 1920,1080)
    image cafeteria = im.Scale("backgrounds/cafeteria.jpg", 1920,1080)
    image ms_play = im.Scale("backgrounds/ms_play.jpg", 1920,1080)
    image ms_gym = im.Scale("backgrounds/ms_gym.jpg", 1920,1080)
    image ms_frontgate = im.Scale("backgrounds/ms_frontgate.jpg", 1920,1080)
    image M_room = im.Scale("backgrounds/M_room.jpg", 1920,1080)
    image bus = im.Scale("backgrounds/bus.jpg", 1920,1080)
    image bus_crash = im.Scale("backgrounds/bus_crash.jpg", 1920,1080)
    image rooftop = im.Scale("backgrounds/rooftop.jpg", 1920,1080)
    image toilet_poop = im.Scale("backgrounds/toilet_poop.jpg", 1920,1080)
    image theater = im.Scale("backgrounds/theater.jpg", 1920,1080)
    image theater_front = im.Scale("backgrounds/theater_front.jpg", 1920,1080)
    image theater_inside = im.Scale("backgrounds/theater_inside.jpg", 1920,1080)
    image toilet = im.Scale("backgrounds/toilet.jpg", 1920,1080)
    image hs_gym = im.Scale("backgrounds/hs_gym.jpg", 1920,1080)
    image hs_frontgate = im.Scale("backgrounds/hs_frontgate.jpg", 1920,1080)
    image hs_classroom = im.Scale("backgrounds/hs_classroom.jpg", 1920,1080)
    image hs_classroom_morning = im.Scale("backgrounds/hs_classroom_morning.jpg", 1920,1080)
    image hs_classroom_front = im.Scale("backgrounds/hs_classroom_front.jpg", 1920,1080)
    image hs_classroom_left = im.Scale("backgrounds/hs_classroom_left.jpg", 1920,1080)
    image hs_classroom_empty = im.Scale("backgrounds/hs_classroom_empty.jpg", 1920,1080)
    image hs_hallway = im.Scale("backgrounds/hs_hallway.jpg", 1920,1080)
    image hs_library = im.Scale("backgrounds/hs_library.jpg", 1920,1080)
    image hs_track = im.Scale("backgrounds/hs_track.jpg", 1920,1080)
    image hotel_front = im.Scale("backgrounds/hotel_front.jpg", 1920,1080)
    image hotel_room = im.Scale("backgrounds/hotel_room.jpg", 1920,1080)
    image onsen = im.Scale("backgrounds/onsen.jpg", 1920,1080)
    image forest = im.Scale("backgrounds/forest.jpg", 1920,1080)
    image forest_inside = im.Scale("backgrounds/forest_inside.jpg", 1920,1080)
    image discord = im.Scale("backgrounds/discord.png", 1920, 1080)
    image skype = im.Scale("backgrounds/skype.png", 1920, 1080)
    image zoom = im.Scale("backgrounds/zoom.png", 1920, 1080)
    return
label positions:
    transform right:
        xalign 0.95
        yalign 0.49
    transform right_two:
        xalign 0.80
        yalign 0.49
    transform right_three:
        xalign 0.65
        yalign 0.49
    transform left:
        xalign 0.05
        yalign 0.49
    transform left_two:
        xalign 0.20
        yalign 0.49
    transform left_three:
        xalign 0.35
        yalign 0.49
    transform center:
        xalign 0.5
        yalign 0.49
    transform Tcenter:
        xalign 0.5
        yalign 0.1
    transform Tleft:
        xalign 0.20
        yalign 0.1
    transform Tright:
        xalign 0.80
        yalign 0.1
    transform TMcenter:
        xalign 0.5
        yalign 0.50
    transform TMleft:
        xalign 0.20
        yalign 0.50
    transform TMright:
        xalign 0.80
        yalign 0.50
    return

# The game starts here.

label start:

    label Script:

        label Syschord_prologue:

            scene discord with Dissolve(1.0)

            "{i}Minato, Akiyuki, and Keisuke are in discord playing Zenith Champions.{/i}"

            MH "Akiyuki, why didn't you drop where Keisuke and me are?"

            AH "What do you mean?" 
            AH "I'm already there."

            MH "No, you're not." 
            MH "I can see you're on the other side of the map."

            AH "Give me like 5 seconds, and I'll be there."

            MH "Keisuke, I see a party up ahead." 
            MH "Come support my offense, I'm gonna rush ‘em."

            KH "Wait a minute, I can't find a gun."

            MH "We've gone by like ten supply bins." 
            MH "You still haven't picked up a gun yet?"

            KH "The ones I went through were filled with ammo and shields, so I couldn't get a gun."

            MH "I literally just saw a mozambique." 
            MH "Grab it and let's rush the other party."

            AH "Oh, I think I see the other party, Minato." 
            AH "I'll use my ultimate on them."

            MH "No, what are you doing?!" 
            MH "Wait for us!"

            KH "I still haven't found a gun yet."

            AH "They don't see me, so I'm gonna go ahead and use my ultimate." 
            AH "Oh shit, I think they do see me." 
            AH "Minato, hurry up!"

            "{i}Akiyuki gets shot by the enemy party and dies alone.{/i}"

            MH "Keisuke, come push with me and we'll avenge Akiyuki."

            KH "I still haven't been able to get a gun."

            "{i}Minato and Keisuke get shot by a different party from behind and die.{/i}"

            AH "This is your guys' fault for not dropping with me."

            MH "No, you–"

            scene zoom with Dissolve(0.5)

            "{i}Meanwhile, on Soom.{/i}"

            FBA "Oh, before I let you guys off the soom, remember that tomorrow is a VERY IMPORTANT day."
            FBA "Chizuru-chan is presenting for the project, and it's VERY IMPORTANT to her."
            FBA "You guys better not miss it, because it means THE WORLD to her."

            scene discord with Dissolve(0.5)

            "{i}The Soom ends.{/i}"

            KH "Are you guys joining tomorrow?"

            AH "No, why would I?"

            KH "Because, it's VERY IMPORTANT."

            AH "I already don't attend my first period class at 8AM, so I don't see why I would go to one of Fuka-sensei's sooms to listen to a kid read off a powerpoint."

            KH "What about you, Minato?"

            MH "I'm still pissed about what happened in the game man."
            MH "Akiyuki, what the hell were you doing?"

            AH "Every time I land with y'all I can never get anything from the supply bins."
            AH "It's because you always end up taking everything."

            KH "That's why I can never find a gun."

            MH "Well I'm sorry. There's a million supply bins where Keisuke and I dropped. You gotta act quick."
            MH "And to answer your question Keisuke, I might."

            AH "I think you guys should've just dropped with me. That way, we would've won."

            MH "I was the drop leader, so that means you're supposed to drop with me. But you decided to go off on your own."
            MH "If you dropped with us, we would've taken out that party."

            KH "You know, this arguing reminds me of that time in middle school."
            KH "You know?"

            AH "Oh yeeeeeaah. You mean..."
            AH "When Minato and I ran against each other in seventh grade?"

            MH "Oooohh, you mean when I won that election?"

            AH "That's only cuz I voted for you."
            AH "If I didn't, it would've ended up in a tie."

            MH "I don't know about that one."

            AH "Trust me, it happened like this..."

        label MSScript:

            label Seven_one:

                scene ms_classroom_morning with Dissolve(1.0)

                "Classroom Morning"

                FOS "Okay class, we're gonna decide the class representatives for the rest of the year."

                show FOS at Tcenter with Dissolve(0.25)

                FOS "Now, who wants to run for the girls?"

                hide FOS with Dissolve(0.25)

                show JNE_W at left with Dissolve(0.25)

                JNE "(whispering) I'll run if you do, okay?"

                show A_W_frown at right with Dissolve(0.25)

                A "(whispering) Yeah, sure, yeah."

                hide JNE_W with Dissolve(0.25)
                hide A_W_frown with Dissolve(0.25)

                "{i}Jein raises her hand.{/i}"

                show JNE_W at center with Dissolve(0.25)

                JNE "I do."

                hide JNE_W with Dissolve(0.25)

                show FOS at Tcenter with Dissolve(0.25)

                FOS "Okay, looks like Jein is the only one."
                FOS "Now for the boys, who wants to run?"

                hide FOS with Dissolve(0.25)

                show A_W_frown at left with Dissolve(0.25)
                show M_W_frown at right with Dissolve(0.5)

                "{i}Akiyuki raises his hand, but Minato raises his own at the same time.{i}"

                hide A_W_frown with Dissolve(0.25)
                hide M_W_frown with Dissolve(0.25)

                show FOS at Tcenter with Dissolve(0.25)

                FOS "Okay, looks like there's two of you that want to run..."
                FOS "Let's have both of you stand at the front of the class and each explain why you're the better candidate."
                FOS "So, who's first?"

                hide FOS with Dissolve(0.25)

                "{i}Minato and Akiyuki decide between themselves that Minato should go first.{/i}"

                show M_W at center with Dissolve(0.25)

                M "I think I'll do a good job because—"

                hide M_W

                show FOS_shout at Tcenter

                FOS "{size=*1.5}MINATO! Stop talking!{/size}"

                hide FOS_shout
                show FOS_angry at Tcenter

                FOS "For that little outburst, you should go first."

                hide FOS_angry with Dissolve(0.25)

                show M_W_frown at center with Dissolve(0.25)

                M "But that was the beginning of my speech..."

                hide M_W_frown with Dissolve(0.25)

                show FOS at Tcenter

                FOS "Oh."
                FOS "Then hurry up and continue."

                hide FOS with Dissolve(0.25)

                show M_W at center with Dissolve(0.25)

                M "As I was saying, I think I'll do a good job because..."
                M "Mi bin live on da street, rake an scrape suh a bobb, nah?"
                M "Den dis kutnee dress like da mafia say. \"Hey boi, yuh wan a play da game ya?\""
                M "Mi pley da gaem n kill lot of skunt man lik ninja mon."
                M "Cowabunga mon go lik crasy."
                M "Ninja mun save mi fro mad docta at de borda ya, killin big mon who lik de collag ball."
                M "(coughs)S-Sorry, I don't know what just happened there."

                "{i}Total silence fills the classroom."
                "{i}Minato sits back down.{/i}"

                hide M_W with Dissolve(0.25)

                "{i}Akiyuki goes up to the front.{/i}"

                show A_W at center with Dissolve(0.25)

                A "How about those shoe lockers huh?"
                A "All old and rusty... Don't even work half the time."
                A "Took me an hour to open mine up."
                A "Fumino-sensei knows what I'm talkin' about."
                A "And did I mention old and rusty?"
                A "Absolutely disgusting."
                A "Vote for me, and we'll get better lockers."

                show M_W_frown at left with Dissolve(0.25)

                M "Can the school even afford new lockers?"
                M "There's less than twenty students in our entire grade."

                hide M_W_frown

                show FOS_shout at Tright

                FOS "{size=*1.5}MINATO! Stop talking!{/size}"

                hide FOS_shout
                show FOS at Tright

                FOS "Okay class, any questions?"
                FOS "No?"
                FOS "Alright then, let's take a vote."

                hide A_W with Dissolve(0.25)

                "{i}Akiyuki sits back down.{/i}"

                hide FOS with Dissolve(0.25)

                show JNE_W at left with Dissolve(0.25)

                JNE "(whispering) That was good, so don't worry, you got this."

                show A_W_frown at right with Dissolve(0.25)

                A "(whispering) We'll see."

                hide JNE_W with Dissolve(0.25)
                hide A_W_frown with Dissolve(0.25)

                "{i}Fumino-sensei collects the votes written on pieces of paper from the class.{/i}"

                show FOS at Tcenter with Dissolve(0.25)

                FOS "Minato won by one vote."

                hide FOS with Dissolve(0.25)

                show JNE_W_pout at left with Dissolve(0.25)

                JNE "(whispering) Darn, you were so close."

                show A_W_frown at right with Dissolve(0.25)

                A "(whispering) I didn't know if I could vote for myself, so I voted for Minato."
                A "(whispering) That probably made the difference."

                hide JNE_W_pout
                show JNE_W at left

                JNE "(whispering) You should tell Fumino-sensei..."
                JNE "I wanna do this with you."

                A "(whispering) Well, it'll just end up being a tie."
                A "(whispering) There's really no point in dragging it out."

                hide JNE_W
                show JNE_W_pout at left

                JNE "(whispering) Yeah, but..."

                A "(whispering) It's not like I didn't wanna win, but I already lost."

                hide A_W_frown
                show A_W at right

                A "(whispering) I'm not cut out for it anyway."
                A "(whispering) I don't see myself trying something like this again."

                JNE "(whispering) You could win if you told her."
                JNE "(whispering) She would recount the votes."

                hide A_W
                show A_W_frown at right

                A "(whispering) What makes you say that?"

                JNE "(whispering) Because... she hates Minato-kun."

                hide JNE_W_pout
                show JNE_W at left

                JNE "(whispering) And I accidentally wrote down the wrong name thinking it was yours."

                hide A_W_frown
                show A_W_shock at right

                A "Jein, what the fu—"

                hide A_W_shock
                hide JNE_W

            label Seven_two:

                scene ms_classroom_morning with Dissolve(1.0)

                "Classroom Morning"

                "{i}A perfectly normal school day is about to begin.{/i}"

                show FOS at Tcenter with Dissolve(0.25)

                FOS "Alright class, I have a couple of announcements to make."
                FOS "I am pregnant, and—"

                hide FOS
                show GTA_S at left with Dissolve(0.25)

                BII "Fat bitches be wildin' my niggas."

                show GTB_S at left_two with Dissolve(0.25)

                EI "Fo' sho, Fo' sho!"

                show CAM_S_shock at left_three with Dissolve(0.25)

                CAM "Crackers, am I right my niggas?"

                show R_S at right_two with Dissolve(0.25)

                R "You know you're white, right?"

                hide CAM_S_shock
                show CAM_S at left_three

                CAM "Nah, my granny was singing in the choir with the niggas."
                CAM "So I got da pass my nigga."

                show GNG_S at right with Dissolve(0.25)

                GNG "Go nigga go!"

                hide GTA_S
                hide GTB_S
                hide CAM_S
                hide R_S
                hide GNG_S

                show M_S_frown at center with Dissolve(0.25)

                M "Stop talking guys."

                hide M_S_frown
                show FOS_shout at Tcenter

                FOS "{size=*1.5}MINATO! Stop talking!{/size}"

                hide FOS_shout
                show FOS_angry at Tcenter

                FOS "If you have something to say, mind sharing it with the rest of the class?"

                hide FOS_angry with Dissolve(0.25)

                show M_S_frown at center with Dissolve(0.25)

                M "But I was just–"

                hide M_S_frown

                show CAM_S_shock at left

                CAM "Man, shut yo' cracker ass up!"

                show GNG_S at left_two with Dissolve(0.25)

                GNG "Go nigga go!"

                show FOS at Tright with Dissolve(0.25)

                FOS "Thank you boys."

                hide CAM_S_shock with Dissolve(0.1)
                hide GNG_S with Dissolve(0.1)

                show FOS at Tcenter with Dissolve(0.25)

                FOS "As I was saying, the class will be reading a book and completing a project afterward."
                FOS "I'm thinking of having it due sometime in December."

                show M_S_frown at left with Dissolve(0.25)

                M "What–"

                hide M_S_frown
                hide FOS
                show FOS_shout at Tcenter

                FOS "{size=*1.5}MINATO! Stop talking!{/size}"

                hide FOS_shout

                show TY_S at left with Dissolve(0.25)

                TY "Fatty-sensei what we reading? \"Hats in the Cats\"?"

                show GTB_S at left_two with Dissolve(0.25)

                BII "Nah, that was a movie, Saki-kun."

                hide GTB_S
                hide TY_S
                show TY_S_shy at center

                TY "I told y'all niggas to stop calling me that!"
                TY "That ain't my name."

                hide TY_S_shy
                show TY_S at center

                TY "It's Toru."

                hide TY_S with Dissolve(0.25)

                show FOS at Tcenter with Dissolve(0.25)

                FOS "That is your name."
                FOS "It says it clearly in my roll sheet."
                FOS "And to answer your question Saki-kun, we will be reading \"Road to Terabithia\"."

                hide FOS with Dissolve(0.25)

                "{i}Bell rings.{/i}"

                show FOS at Tcenter with Dissolve(0.25)

                FOS "Okay, That's all for today."
                FOS "I'll see y'all tomorrow."

                "{i}Fumino exits the classroom."

                hide FOS with Dissolve(0.25)

                "{i}The class moves to the music room."

                scene ms_music with Dissolve(0.5)

                "Music Classroom"

                show DUE at TMcenter with Dissolve(0.25)

                DUE "Hello boys and girls."

                hide DUE
                show DUE_smug at TMcenter

                DUE "Today, we'll be practicing a song that I wrote for our school."

                hide DUE_smug
                show TY_S at left with Dissolve(0.25)

                TY "Ain't nobody wanna listen to some diddy that you cooked up baldy-sensei."

                show CAM_S_shock at right

                CAM "Hold on, my nigga!"

                hide CAM_S_shock
                show CAM_S at right

                CAM "Let him cook."

                hide CAM_S
                hide TY_S

                show DUE_smug at TMcenter with Dissolve(0.25)

                "{i}Daiki plays the school theme song.{/i}"

                hide DUE_smug with Dissolve(0.25)

                show TY_S at center with Dissolve(0.25)

                TY "That shit was a—"

                hide TY_S

                show GTB_S at left

                BII "That was so FIRE!"

                show GTA_S at left_two with Dissolve(0.25)

                EI "Fo' sho, Fo' sho!"

                show CAM_S_shock at right with Dissolve(0.25)

                CAM "This is the type of music that we've been yearning for!"
                CAM "No wonder why you were featured in the local newspaper two years ago."

                hide CAM_S_shock
                hide GTA_S
                hide GTB_S

                show DUE_shock at TMcenter with Dissolve(0.25)

                DUE "Geez Louise, you're all flattering me."

                hide DUE_shock
                show DUE_smug at TMcenter

                DUE "You're making it seem like I could write up a whole school play or something."
                DUE "I mean, what would it even be about?"

                hide DUE_smug
                show DUE at TMcenter

                DUE "It can't be that easy to write something up in a day or two."
                DUE "It'd probably be weeks, months, or even years."
                DUE "I doubt that I'd even have the time for that."

                hide DUE with Dissolve(0.25)

                "{i}Daiki-sensei went hard at work developing a school play.{/i}"

                scene ms_computer with Dissolve(0.5)

                "Computer Classroom"

                "{i}The last class of the day.{/i}"

                show A_S at left with Dissolve(0.25)

                A "Have you guys heard of \"Stellar Crusades\"?"

                show K_S at right with Dissolve(0.25)

                K "Who hasn't?"
                K "You'd have to be an ignoramus to not have heard of \"Stellar Crusades\"."

                show M_S at right_two with Dissolve(0.25)

                M "Keisuke and I have seen every episode of the animated series."
                M "Remember that scene when—"

                hide M_S

                show A_S at left_two

                A "Well apparently, there's a new movie coming out in two years."
                A "We should definitely go see it."

                show M_S_frown at right_two

                M "It sounds like it's gonna be awful."

                hide A_S
                show A_S_frown at left_two

                A "What do you mean?"

                M "What do YOU mean, \"What do you mean\"?"
                M "Giorno Lukas sold \"Stellar Crusades\" to Dosney."
                M "He's most likely going to have no involvement, so it's gonna be ass."
                M "Keisuke, don't you agree?"

                K "The only good movies were the prequels anyway."
                K "Everything else pales in comparison, including the animated series."

                A "That's not true."
                A "The original trilogy is the reason why the prequels even exist."

                show CAM_S_shock at left with Dissolve(0.25)

                CAM "My niggas!"

                hide A_S_frown with Dissolve(0.1)
                hide M_S_frown with Dissolve(0.1)
                hide K_S with Dissolve(0.1)

                CAM "Look at this video I just found!"

                "{i}Kaimon proceeds to play a porn video...{/i}"
                "{i}At max volume.{/i}"

                hide CAM_S_shock

                SEN "{size=*1.5}MINATO!{/size}"
                SEN "That's it!"
                SEN "Everyone, shut down your computers."
                SEN "Remain seated in silence."

                "{i}The class was then banned from the computer lab.{/i}"

            label Seven_three:

                scene ms_classroom_afternoon with Dissolve(1.0)

                "Classsroom Afternoon"

                show RR at Tcenter with Dissolve(0.25)

                RR "Okay class, now we'll—"

                hide RR

                show M_W_frown at center

                M "(breathes)"

                hide M_W_frown

                show RR_shout at Tcenter

                RR "{size=*1.5}MINATO! Stop talking!{/size}"

                hide RR_shout
                show RR_angry at Tcenter

                RR "How many times do I have to tell you, child?!"
                RR "Always disrupting my class."
                RR "You need to stop making such a ruckus in my classroom."

                hide RR_angry
                show RR at Tcenter

                RR "I'm gonna have to separate you from Hideki."
                RR "Go sit in the back of the classroom by yourself."

                hide RR with Dissolve(0.25)

                "{i}Minato, defeated, moves to the back of the classroom.{/i}"

                show RR at Tcenter with Dissolve(0.25)

                RR "(coughs) All that yelling hurt my throat."

                hide RR

                show CAM_W_shock at center with Dissolve(0.25)

                CAM "Pretty sure it was all that smoking behind the school that caused that cough!"

                hide CAM_W_shock

                show RR_shout at Tcenter

                RR "{size=*1.5}MINATO!{/size}"

                hide RR_shout

                show RR_angry at Tcenter

                RR "Are you serious right now?"
                RR "After I just moved you?"

                hide RR_angry

                "{i}Bell rings.{/i}"

                show RR at Tcenter with Dissolve(0.25)

                RR "That's it for today."
                RR "Go and enjoy your lunch."

                hide RR with Dissolve(0.25)

                "{i}Beri exits the classroom.{/i}"

                show HN_W at left with Dissolve(0.25)

                HN "Why didn't you respond to Beri-sensei, Minato?"
                HN "You weren't even doing anything."

                show R_W at left_two with Dissolve(0.25)

                R "Wasn't Kaimon the one talking?"

                show A_W_frown at left_three with Dissolve(0.25)

                A "I'm gonna go use the restroom."

                hide A_W_frown with Dissolve(0.25)

                "{i}Akiyuki exits the classroom.{i}"

                show M_W_heartbroken at right_three with Dissolve(0.25)

                M "What's even the point."
                M "Nothing would've changed even if I responded."

                show K_W at right_two with Dissolve(0.25)

                K "You're not wrong."
                K "I was talking to Akiyuki the whole time she was yelling at you."

                hide M_W_heartbroken
                show M_W_frown at right_three

                M "See?"
                M "You guys were talking, yet I ended up being the one getting moved."
                M "And for what?"
                M "For breathing?"
                M "Breathing!?"
                M "I took one breath and got moved to the back of the classroom."

                show A_W_shock at right

                A "Hey guys!"
                A "You won't believe what I just found in the restroom!"

                HKMR "What?"

                hide A_W_shock

                show A_W at right

                A "I went in to pee, and IT was there in the urinal."
                A "A big piece of shit shaped just like the shit emoji right in the urinal."

                "{i}They all exchange looks, then exit the classroom to go to the boy's restroom.{i}"

                hide A_W
                hide K_W
                hide M_W_frown
                hide R_W
                hide HN_W

                scene toilet_poop with Dissolve(0.5)

                "Restroom"

                show R_W_startled at left with Dissolve(0.25)

                R "You weren't kidding."

                show HN_W_startled at left_two with Dissolve(0.25)

                HN "That's a big piece of shit."

                show K_W_shock at right_three with Dissolve(0.25)

                K "Shaped just like the shit emoji."

                show M_W_shock at right_two with Dissolve(0.25)

                M "Right in the urinal."

                hide R_W_startled
                hide HN_W_startled
                hide K_W_shock
                hide M_W_shock

                show R_W at left 
                show HN_W at left_two
                show K_W at right_three
                show M_W at right_two

                HN "Who could've done this?"

                R "It looks dry as hell."

                show A_W_frown at right with Dissolve(0.25)

                A "It's probably been there for a while."
                A "I'd be surprised if it was someone in a lower grade because of how massive it is."

                R "What are you, some kinda, shit connoisseur?"

                hide R_W
                hide HN_W 
                hide K_W
                hide M_W 
                hide A_W_frown 

                show TY_W at left with Dissolve(0.25)

                "{i}Saki walks into the boy's restroom.{/i}"

                TY "What y'all doing crowding the restroom for?"

                hide TY_W
                show TY_W_shy at left

                "{i}Saki notices the shit emoji in the urinal.{/i}"

                hide TY_W_shy with Dissolve(0.25)

                "{i}He exits the restroom silently soon after.{/i}"

                "{i}Meanwhile...{i}"

                scene ms_hallway with Dissolve(0.5)

                "Hallway"

                show JEN_W at left with Dissolve(0.25)

                JEN "And the girl's bathroom was too far, so..."

                show RIN_W_shock at right_two
                show TIN_W_shock at right

                RT "You went into the boys' restroom and took a shit in the urinal?!"

                hide JEN_W
                show JEN_W_angry at left

                JEN "I really had to go, okay?"

                hide TIN_W_shock
                show TIN_W at right

                RIN "You did not."

                TIN "That's really gross."

                JEN "Just promise you'll never tell anyone!"

                hide JEN_W_angry
                hide RIN_W_shock
                hide TIN_W

            label Seven_four:

                scene ms_classroom_morning with Dissolve(1.0)

                "Classroom Morning"

                show FOS at Tcenter with Dissolve(0.25)

                FOS "Alrighty class, since we finished \"Road to Terabithia\", I'll explain how the project is going to go."
                FOS "You guys are going to make your very own Terabithia out of any material, like MEGO."

                hide FOS

                show R_W at left with Dissolve(0.25)

                R "Can we use paper?"

                show GTB_W at right_three with Dissolve(0.25)

                BII "Nigga, you cheap as hell."

                hide R_W
                show R_W_shock at left

                show GNG_W at right_two with Dissolve(0.25)

                GNG "Go nigga go!"

                hide R_W_shock
                show R_W_startled at left

                show GTA_W at right with Dissolve(0.25)

                EI "Fo' sho, Fo' sho!"

                hide GTB_W with Dissolve(0.1)
                hide GTA_W with Dissolve(0.1)
                hide GNG_W with Dissolve(0.1)

                show R_W at left

                show FOS at Tright with Dissolve(0.25)

                FOS "Yes Roro-kun, like I said, you can use anything."
                FOS "The project will be due in two days."
                FOS "I'll let y'all work on it in class tomorrow."

                hide R_W
                hide FOS

                scene ms_classroom_morning

                "{i}The next day{/i}"

                show FOS at Tcenter with Dissolve(0.25)

                FOS "Okay, now is your free time to start working on your projects."
                FOS "Go ahead and do so."

                hide FOS

                show M_W at left with Dissolve(0.2)
                show R_W at left_three with Dissolve(0.2)

                M "Roro, what are you gonna make?"

                hide M_W
                hide R_W

                show FOS_shout at Tcenter

                FOS "{size=*1.5}MINATO! Stop talking!{/size}"

                hide FOS_shout

                show M_W_frown at left with Dissolve(0.2)
                show R_W at left_three with Dissolve(0.2)

                "{i}Minato and Roro work on their projects in the back of the room."

                hide M_W_frown with Dissolve(0.2)
                hide R_W with Dissolve(0.2)

                show A_W at right with Dissolve(0.2)
                show K_W at right_three with Dissolve(0.2)

                "{i}Akiyuki and Keisuke work in the front.{/i}"

                A "Keisuke, look what I made."
                A "It's a camera to film exotic creatures."

                "{i}Akiyuki shows Keisuke a crudely made paper camera.{/i}"

                K "We're in a classroom."

                hide A_W
                show A_W_motivated at right

                A "Look, there goes a wild panda!"

                "{i}Akiyuki aims his paper camera at his subject.{/i}"

                K "You mean Maruiko?"

                A "Watch this."

                hide K_W with Dissolve(0.25)

                "{i}Akiyuki walks over to Maruiko with his paper camera.{/i}"

                show A_W_motivated at left with Dissolve(0.25)

                show MI_W at right with Dissolve(0.25)

                A "As you can see, I am in the safari."
                A "Sh sh sh."
                A "Do you see? That over there is an endangered species."

                hide MI_W
                show MI_W_pout at right

                A "The panda."
                A "Let's observe it in its natural habitat."

                hide MI_W_pout
                show MI_W_angry at right

                MI "AKIYUKI, WHAT DO YOU THINK YOU'RE DOING?!?!?!?!?!"

                hide A_W_motivated
                show A_W_shock at left

                A "I might have provoked the panda."

                hide A_W_shock
                show A_W at left

                A "I should fall back."
                A "Oh, hey Rin."

                hide MI_W_angry with Dissolve(0.25)

                "{i}Akiyuki waves to Rin, then turns around and retreats back to Keisuke, who made an origami Zoda in the meantime.{/i}"

                show K_W at right with Dissolve(0.25)

                OGZ "A wise endeavor, that was not."

                hide K_W with Dissolve(0.25)
                hide A_W with Dissolve(0.25)

                "{i}Fumino sneaks up behind them and snatches their paper masterpieces.{/i}"

                show FOS_angry at Tcenter with Dissolve(0.25)

                FOS "What are you two doing?"
                FOS "I expected this from Minato, not y'all."

                show M_W_shock at right with Dissolve(0.25)

                M "HUH?!"

                hide M_W_shock

                "{i}Ignoring Minato, Fumino throws the masterpieces in the trash, never to be seen again."
                "{i}Meanwhile, Hideki quietly spends all day working hard on his MEGO project.{/i}"

                scene ms_classroom_morning with Dissolve(1.0)

                "{i}The next day."
                "{i}Presentation day.{/i}"

                show FOS at Tcenter with Dissolve(0.25)

                FOS "Alrighty y'all, get ready to present your projects."
                FOS "Who wants to go first?"

                show GNG_W at right with Dissolve(0.25)

                GNG "Go nigga go!"

                hide GNG_W

                FOS "That's fine, Jun."
                FOS "You can keep working on your project in the meantime."

                show M_W at left with Dissolve(0.25)

                M "Huh?"
                M "She understood that?"

                hide FOS
                show FOS_shout at Tcenter 

                FOS "{size=*1.5}MINATO! Stop talking!{/size}"
                FOS  "For that, you should go first."

                "{i}Minato sighs and goes up to the front with his project."
                
                hide FOS_shout
                show FOS
                show R at right with Dissolve(0.25)

                "{i}Roro comes bursting through the door of the classroom.{/i}" 

                R "Sorry, I'm late."
                R "There were a million squirrels out there!"
                R "But some bronze man shot ‘em down for me."

                FOS "Since you were late, you should go first."

                hide FOS
                show FOS_shout

                FOS "What are you doing, Minato? Sit down!"

                hide M_W

                R "Let me set my stuff down first, then I'll get started."

                "{i}Roro takes off his backpack and prepares to toss it at his chair.{/i}"

                M "Wait Roro, don't try it!"

                R "You underestimate my power..."

                "{i}Roro tosses his backpack at the wrong side of the room and hits Hideki's desk, where his MEGO project was sitting."
                "{i}It falls to the floor and shatters into pieces.{/i}"

                HN "(While sobbing) What did you just do?!"
                HN "I worked all day and night on that!"
                HN "Now it's ruined!"

                R "My bad."
                R "So anyway, I'm ready to present, Fumino-sensei."

                "{i}Roro showcases his paper treehouse to the class as if nothing had happened.{/i}"

            label Seven_five:

                scene ms_music with Dissolve(1.0)

                DUE "(with bags under his eyes and a five o'clock shadow) Hello, boys and girls."
                DUE "Today I have a MAJOR announcement."
                DUE "I finished working on my play, and the principal approved it."
                DUE "Today, we'll be deciding your roles in the play, and then I'll prepare you boys and girls for it."

                "{i}Daiki projects his computer screen onto the board where it shows the roles for his play.{/i}"

                R "What are you guys gonna sign up for?"

                GNG "Go nigga go!"

                DUE "Okay Jun."
                DUE "Come type your name here, next to \"newspaper boy\"."

                K "I think I'll be one of the soldiers."

                R "Nah, that says \"souljas\"."
                R "There's three of them."

                A "Count me in on that."

                R "Okay, I'll go type our names in."

                "{i}Roro makes his way to Daiki's computer and types their names next to the \"souljas\"."

                CAM "Nigga spelt Keisuke's name wrong."

                "{i}Everyone in the class looks at the board.{/i}"

                TY "Nigga, why are all the role names so ghetto?"

                DUE "What do you mean?"
                DUE "That's just how you kids talk these days."

                EI "Fo' sho, Fo' sho!"

                scene ms_play with Dissolve(0.5)

                "{i}Night of premiere."
                "{i}The audience, which consisted solely of parents, eagerly awaits the locally famous Daiki's production."
                "{i}The play begins.{/i}"

                NPB "Go nigga go!"
                NPB "Go nigga go!"

                "{i}The audience gives a standing ovation."
                "{i}The play arrives at the final scene.{/i}"

                WAN "This war is almost over."
                WAN "It's time for the final charge."

                TUU "That's it, I'm goin' commando!"

                "{i}Hideki undresses before the audience."
                "{i}They run away screaming, leaving the seats completely empty."
                "{i}And so ends Daiki's final production.{/i}"

            label Eight_one:

                scene ms_classroom_morning with Dissolve(1.0)

                RR "(coughs) Okay everyone, I'll be your homeroom teacher this year."
                RR "I see we have a few new faces."
                RR "Y'all better not act up."
                RR "Also, I need to mention that Daiki-sensei will be my assistant this year."
                RR "Because of what happened last semester, the superintendent has decided this school has no need for a music department."

                DUE "(sniffling) That wasn't the commando I was referring to..."
                DUE "Ahem, new boys and girls, please go to the front of the class and introduce yourselves."

                BM "I am—"

                R "Oh shit, it's that bronze man."
                R "He's the guy who saved me from those squirrels!"

                GNG "Go nigga go!"

                BM "You're welcome."

                SHR "Uhhh, ma name's Shemar."

                C "I'm Greg."

                "{i}Greg takes out a notecard and reads aloud from it.{/i}"

                C "My mom's a teacher here, and my dad makes a billion dollars an hour."
                C "We live here in the ghettos."

                SDK "(sniffing) Somethin' smells musty up in here."

                RR "Girl, what you talking ‘bout."
                RR "Ain't nothing smelling musty up in here!"
                RR "Go ahead make your introduction!"

                SDK "Nuh uhhh."
                SDK "It smell like one of them musty smokers' smell."
                SDK "Anyways, I'm Sheldrieka."

                BII "Damn, she fine as hell."

                EI "Fo' sho, Fo' sho!"

                TY "Roro, I saw Keisuke lookin' at Sheldrieka."
                TY "I think he likes her."

                R "Wait, he does?"

                "{i}Roro comes up with a masterclass plan to inquire Keisuke about his true feelings."
                "{i}He takes out a piece of paper and writes \"Do you like her?\" in English on the front.{/i}"

                R "Hey Keisuke."
                R "Read this."

                "{i}Roro passes the note to Keisuke."
                "{i}He reads the note and flips it over."
                "{i}Keisuke writes in big letters \"I don't fucking like her.\" in English on the back and passes it back to Roro.{/i}"

                R "(snickering) Okay, okay, I get it."

                M "Hey, what's so funny?"

                R "It's nothing man."

                "{i}Roro gets up and puts the note in the trash.{/i}"

                M "(whispering) Akiyuki, you wanna know what's on that note too, right?"

                "{i}Akiyuki nods his head."
                "{i}Minato stands up and digs through the trashcan to grab the note."
                "{i}He finds it and brings it back to the desk they were sitting at."
                "{i}Minato reads both sides of the note while laughing quietly."
                "{i}Then he passes the note to Akiyuki so he could see it."
                "{i}Akiyuki reads the note and giggles like a madman."

                DUE "Akiyuki, put that note away."

                A "Sorry about that."

                "{i}Akiyuki puts the note in one of his folders."
                "{i}A few seconds later he pulls the note out of the folder to look at it and laughs again.{/i}"

                DUE "Akiyuki, I thought I told you to put that note away."

                A "Yes, sorry sir."

                "{i}Akiyuki puts the note in one of his folders."
                "{i}A few seconds later he pulls the note out of the folder to look at it and laughs again.{/i}"

                DUE "That's it! Give me that note!"

                "{i}Daiki grabs the note from Akiyuki and reads it."
                "{i}He gasps loudly and shouts at the top of his lungs.{/i}"

                DUE "Why, this is blasphemy! Heresy I say!"
                DUE "Who wrote this?"

                A "Wasn't me."

                "{i}From the other side of the classroom, one of the new students speaks up.{/i}"

                C "I saw who wrote it."
                C "It was the two nigga ones."

                DUE "Oh, I see."
                DUE "It was the niglet boys."

                RR "(coughs) What's going on here?"

                "{i}Daiki hands the note to Beri and she reads both sides.{/i}"

                RR "{size=*1.5}MINATO!{/size}"
                RR "No, wait."
                RR "RORO and KEISUKE, detention!"
                RR "Head to the office now!"

                "{i}Keisuke and Roro head to the office with their heads down in shame the whole way.{/i}"

                CAM "Smokey Beri back at it again!"

                GNG "Go nigga go!"

                EI "Fo' sho, Fo' sho!"

                C "(whispers) It's all going according to keikaku."

                "{i}TL Note: Keikaku means plan.{/i}"

            label Eight_two:

                scene ms_classroom_morning with Dissolve(1.0)

                RR "Today we're gonna be readin' as a class from the History textbook."
                RR "Shemar, why don't you start us off?"

                SHR "Uhh..."
                SHR "T-The..."
                SHR "Uhhh..."
                SHR "W-wo..."
                SHR "Uhhh..."
                SHR "The wo-world..."

                "{i}Minato and Keisuke talk quietly in the corner as Shemar struggles to read.{/i}"

                RR "Alright that's enough."
                RR "Let's have someone else read."

                "{i}Beri-sensei scans the room.{/i}"

                RR "{size=*1.5}MINATO! Stop talking!{/size}"
                RR "That's it, I have to separate you two."

                C "Um, Beri-sensei?"

                RR "Yes?"

                C "Can Minato-kun sit next to ME?"

                RR "That's a novel idea."
                RR "Okay, why don't we do that then."
                RR "Minato, go and sit yo' ass down next to Greg."

                M "Yes, sensei."

                "{i}Minato sits down in the empty seat next to Greg.{/i}"

                M "How's it going?"

                C "(giggles) Don't you remember me?"
                C "I'm the one that helped you out."

                M "Huh?"

                C "You don't remember?"
                C "WEll, it's okay."
                C "We'll be acquainted quite nicely very soon."
                C "He he ehe he eh eh eh he he hehe he"

            label Eight_three:

                scene ms_classroom_morning with Dissolve(1.0)

                "{i}Sheldrieka sniffs the room like a bitch.{/i}"

                SDK "OOF!"
                SDK "It smell even mustier than usual up in here!"

                RIN "Was that you, Jenifa?"

                JEN "Why would you think it was me?"
                JEN "It could have been Tomoko."

                TIN "Why me?"

                JEN "Because..."
                JEN "Well..."

                RIN "No, it's safer to assume it's you, the girl who shat in the urinal."

                JEN "I told you to forget about that!"

                RR "Okay, okay, settle down."
                RR "I'll use some lemon scent to sweeten the air."

                "{i}Beri sprays the classroom and fills it with the lemon scent."
                "{i}Greg walks in the class and sits down.{/i}"

                SDK "Thanks Riri, that lemon spray made it less musty."

                "{i}Greg jumps out of his seat after hearing that.{/i}"
                "{i}He gasps for air and clutches his chest.{/i}"

                C "Air!"
                C "I need Air!"
                C "Why'd you spray that?!"
                C "You know I have asthma!"

                RR "Calm down child!"
                RR "Just leave the classroom."

                "{i}Greg runs out of the classroom while breathing exasperatedly.{/i}"

                GNG "Go nigga go!"

                M "What a drama queen."

                A "What do you mean? That could've killed him."

                M "Maybe if he actually had asthma."
                M "I know what asthma looks like, and that wasn't it."
                M "He wouldn't be able to breathe or talk at all if it really was that bad."

                R "Whatever man."
                R "At least the dude's finally gone."

                scene ms_hallway with Dissolve(0.5)

                "{i}Greg looks into the classroom from the hallway.{/i}"

                C "(breathing heavily) I heard that."
                C "I won't forget such insolence... Roro."

            label Eight_four:

                scene cafeteria with Dissolve(1.0)

                M "Guys, I've been playing this new MMORPG."
                M "It's damn good."
                M "I just started it a week ago, so you guys should join me."

                A "What's it called?"

                M "It's called \"Fantasy Quest Worlds\"."
                M "There's unique classes and everything, you guys will definitely love it."

                A "Sure, I'll join ya."

                K "Is there a mage class?"

                M "Yeah, you can pick that one, since I'm a warrior."
                M "How about you, Roro?"

                R "I'll sit this one out."
                R "Not really feeling it."

                M "It's your loss."

                "{i}Greg sneaks up behind them and sits next to Minato.{/i}"

                C "I'll be the cleric."
                C "I'll heal you right up ♡."

                M "Sorry, Greg."
                M "You can only make a party of three."
                M "Keisuke and Akiyuki already agreed."

                R "Why'd you invite me too if only three can play?"

                M "Shut up."

                C "Gee willikers, that's too bad."
                C "Guess I'll have to join next time."

                "{i}One table across.{/i}"

                MI "Hey girls, do you wanna play that MMORPG they're talking about?"

                JEN "Ew, no."

                TIN "No thanks."

                RIN "Don't you hate Akiyuki and them, Maruiko?"
                RIN "Why play the same game?"

                MI "Akiyuki's a dumbass."
                MI "He has nothing to do with it."
                MI "It just sounds fun."
                MI "Rin, I know you'll play it with me."
                MI "The rest of you should think about it too."

                scene M_room with Dissolve(1.0)

                "{i}After school."
                "{i}Minato texts his friends on RYPE.{/i}"

                M "Hey, you guys on RYPE yet?"

                K "Yeah, I'm on."

                A "Gimme five minutes."

                scene skype with Dissolve(1.0)

                "{i}Minato and Keisuke start a call and wait for Akiyuki to join.{/i}"

                M "Okay Keisuke, make your character."
                M "Remember, I'm already a level 6 warrior, so I'm basically a God at this game."
                M "Just follow my lead."

                "{i}Akiyuki joins the call.{/i}"

                A "Hey guys, I'm in the game."
                A "What should I name my character?"

                K "Okay, I finished the tutorial, what now?"

                M "Let's meet up at the main city."
                M "Join room 6969."

                A "Wow, you are SO funny."
                A "I'm almost done with the character creation so wait up a bit."

                "{i}Minato and Keisuke stay in the room spamming dance emotes while waiting for Akiyuki.{/i}"
                "{i}Another low-level player joins the 6969 room and stands behind them menacingly.{/i}"

                M "Is that you Akiyuki?"
                M "We can finally get started for real."

                A "What are you talking about?"
                A "I'm still in the tutorial."

                M "If you're still in the tutorial, then who joined our room?"

                "{i}The mysterious player sends a friend request to Minato.{/i}"

                M "He sent me a friend request."
                M "I'm gonna accept and ask who this guy is."
                M "(texting) Who are you?"

                MP "(texting) I'm your best friend♡."

                "{i}Minato cowers in fear and immediately teleports to his in-game house."
                "{i}He instantly removes the mysterious player from his friends list.{/i}"

                M "Holy shit, that was Greg."

                K "Really?"
                K "How'd he even find us?"

                M "I have no fucking clue."
                M "Keisuke, hurry and teleport to me, so we can just get started already."

                K "I gotta stay and wait for Akiyuki."

                M "Fine, just make sure Greg doesn't follow you."

                K "Don't worry."

                "{i}Akiyuki joins the 6969 room and sends Keisuke a friend request.{/i}"

                K "Okay Minato, we're heading to you now."

                M "Wait, what about Greg?"

                A "It's fine, he's not gonna follow us."

                K "Yeah, he's just standing there, menacingly."

                "{i}Keisuke and Akiyuki teleport to Minato, leaving Greg's motionless character standing there in the room alone, menacingly.{/i}"

                M "Okay, good."
                M "My DANDICAM is all set. We're ready to start rolling."

                A "What the hell are you talking about?"

                M "I already prepped the MeTube."
                M "We're gonna get started on our let's play."
                M "Don't be afraid to speak up."
                M "That means you, Keisuke."

                K "We can just do a silent walkthrough."

                M "No, that's boring."
                M "No one's gonna wanna watch a silent stream of an MMORPG."

                A "So what, we're just gonna play through the story?"

                M "Yes."
                M "We'll stream the story and make a ton of guides on all the classes."
                M "I'll make us famous with this game."

                A "You sure about that?"

                K "Well, it's not like we have anything better to do."

                M "Trust me guys, this is gonna work."
                M "Now let's start the stream..."
                M "Hey everyone, this is Reap–"

                "{i}Minato, Keisuke, and Akiyuki spent the whole night streaming the game's story.{/i}"
                "{i}They only had one concurrent viewer.{/i}"

            label Renaissance_prologue:

                scene ms_classroom_morning with Dissolve(1.0)

                RR "Okay class, the school has a surprise for you guys."
                RR "We'll be going on a field trip to the Camelot Carnival today."

                SDK "We goin' to CC's?"

                M "Oh, CC's?"
                M "I love their pizzas."

                SDK "Nuh uh honey, that's a coffee shop."

                RR "{size=*1.5}MINATO! Stop talking!{/size}"
                RR "For that outburst, you're gonna sit at the back of the bus."

                SDK "Nuh uh honey, I ain't no Rosie Perks."

                EI "Fo' sho, Fo' sho!"

                RR "Of course, of course, I was talking about Minato."

                C "Beri-sensei?"
                C "May I sit in the back, next to Minato, because of my asthma?"

                RR "Fine, whatever."

                scene bus with Dissolve(1.0)

                "{i}The class boards the school bus.{/i}"

                R "Oi, Minato."

                M "What's up?"

                R "I got you something I think you'll need."

                "{i}Roro hands Minato a can of lemon scented spray."

                M "Thanks, but I probably won't need it."

                "{i}Minato sits by himself in the back seat.{/i}"
                "{i}Greg snuggles up next to Minato on the school bus.{/i}"
                "{i}Minato cringes and looks out the window.{/i}"

                M "Is that the KKK (Ki Ki's Kloset)?"

                "{i}A clothing store.{/i}"

                BD "HUH?!"

                scene bus_crash with Dissolve(0.25)

                "{i}The bus driver turns his head to the KKK and swerves into the building."

            label Renaissance:

            label Renaissance_epilogue:

                scene bus with Dissolve(1.0)

                "{i}Minato softly and gently opens his eyes."
                "{i}Then he bashfully fluttered his eyelashes until he could regain his sight.{/i}"

                M "Huh?"
                M "Where am I?"
                M "What's goin' on?"

                A "Hey you."
                A "You're finally awake."

                M "Akiyuki?"
                M "What happened to Greg?"

                A "Who?"
                A "Never heard of anyone named Greg in my life."

                M "Huh?"

                A "Keisuke, do you know who he's talking about?"

                K "Nope, no idea."

                M "I swore all that stuff was real."
                M "I guess it was just a really long dream..."

                "{i}Roro struts in and sits next to Minato.{/i}"

                R "What y'all talkin' ‘bout?"

                M "Oh, it's nothing I guess."
                M "Wait a minute..."

                "{i}Minato observes Roro and notices something that shouldn't be there.{/i}"

                M "Did you always have that scar on your forehead?"

                R "What, this old thang?"
                R "I've had it since I was born, you know that."
                R "No way you're just now noticin' it."

                "{i}Minato furrowed his brows the entire time on the way back to the school, wondering if his adventures were really a dream or not.{/i}"

            label Nine_one:

                scene ms_classroom_morning with Dissolve(1.0)

                RR "Alrighty class, let's get started."
                RR "Today's the start of your grade's last year of middle school."
                RR "A lot of faces have come and gone."
                RR "With that said, what do y'all think happened to the Great Sphinx in Egypt for it to look the way that it does?"

                "{i}A student raises their hand.{/i}"

                RR "Yes?"

                LYN "It is camouflaged, so the robbers won't steal it."

                "{i}Only silence remains in the classroom.{/i}"

                M "Is it because of acid and erosion?"

                RR "Yes... that is correct."
                RR "And Minato..."

                M "Hm?"

                RR "{size=*1.5}Stop talking!{/size}"

                scene ms_classroom_afternoon with Dissolve(0.5)

                "{i}The bell rings.{/i}"
                "{i}Beri exits the classroom, and the class gets ready for lunch.{/i}"

                M "I swear, every time."

                "{i}Minato notices Maruiko leaving for the cafeteria.{/i}"
                "{i}He walks over to her.{/i}"

                scene ms_hallway with Dissolve(0.5)

                M "Maruiko? Do you want to eat lunch together?"

                "{i}Maruiko ignores Minato and continues to the cafeteria.{/i}"

                scene ms_classroom_afternoon with Dissolve(0.5)

                A "Hey, Keisuke."
                A "You noticed how Minato has been trying to get closer to Maruiko lately?"

                K "Yeah."
                K "What about it?"

                A "I wonder why Maruiko is giving him the cold shoulder now."

                K "Bitches be crazy."

                A "I guess."
                A "But they seemed fine up until today."

                "{i}Minato makes his way back to them.{/i}"

                M "Yeah..."
                M "I don't feel like having lunch."

                A "What did you do to Maruiko?"

                M "I didn't do anything."
                M "It's all Roro's fault!"

                K "Beri-sensei said he transferred to another school this year."
                K "How can it be his fault?"

                M "I told Maruiko that Roro liked her hair."
                M "Then Maruiko texted Roro to ask if he liked her and he never responded."
                M "So basically, she hates me now, and she thinks that Akiyuki put me up to it."

                A "I haven't even spoken to her since the \"Paper Camera Incident\" back in seventh grade."
                A "Forget about that."
                A "Are you guys going to try out for the english spelling tournament?"

                K "It's not like we have much of a choice."
                K "Fumino-sensei is gonna hold a mock spelling tournament during class to choose two students in our grade to compete in the english spelling tournament anyway."

                M "I don't really feel like doing anything right now."

                A "Don't get hung up over Maruiko."
                A "There's plenty of fish in the sea."

                K "I don't even get what you see in her."

                "{i}The classroom door opens.{/i}"

                M "What do you mean?"
                M "Maruiko's hot as fuck dawg."
                M "I mean, you're telling me that she's not hot to you?"

                MI "{size=*1.5}MINATO! Stop talking!{/size}"

            label Nine_two:

                scene ms_gym with Dissolve(1.0)

                "{i}All grades in the school were in attendance inside the gymnasium."
                "{i}Akiyuki and Keisuke were chosen to compete in the english spelling tournament for their grade against the other grades.{/i}"

                DUE "We have three students left in the tournament."
                DUE "Two students representing the ninth grade class."
                DUE "And one of MY students representing the third grade class."
                DUE "I believe it's time for me to move onto the more challenging words now."

                "{i}Daiki continues to read off the page with all the easy words."
                "{i}He makes his way to Keisuke.{/i}"

                DUE "Keisuke, your word is \"postpone\"."

                K "What tense is it?"

                DUE "It's a verb."

                K "..."
                K "Can you use it in a sentence?"

                DUE "Uh... The game was POSTPONEd."

                K "Can you repeat that?"

                DUE "Sure."
                DUE "The game was POSTPONEd due to bad weather."

                "{i}Keisuke stares at him in disbelief.{/i}"

                K "Postponed."
                K "P-O-S-T-P-O-N-E-D."
                K "Postponed."

                DUE "That is INCORRECT."
                DUE "We now have TWO students left."

                "{i}Daiki makes his way to Akiyuki.{/i}"

                DUE "Akiyuki, your word is \"euro\"."

                A "Euro."
                A "Capital E-U-R-O."
                A "Euro."

                DUE "That is INCORRECT."

                "{i}Daiki makes his way to the third grade girl.{/i}"

                DUE "If you get this wrong, Akiyuki and Keisuke will be able to come back and the spelling tournament will continue."
                DUE "Your word is \"tomorrow\"."

                BEE "Tomorrow."
                BEE "T-O-M-O-R-R-O-W."
                BEE "Tomorrow."

                DUE "AND WE HAVE A WINNER!"
                DUE "She will now be representing our school and competing in the prefectural spelling tournament against other schools."
                DUE "Please give a round of applause."

                "{i}Everyone in attendance applauds the third grade girl.{/i}"
                "{i}Minato approaches Akiyuki and Keisuke.{/i}"

                M "Y'all are so stupid for losing to a girl in the third grade."

                K "It's not my fault he used a shit sentence and put my word in past tense."
                K "How was I supposed to know?"

                M "You stupid."

                A "It's whatever."
                A "I didn't feel like staying any longer for the spelling tournament than I needed to."
                A "You should be thanking me."
                A "I ended the tournament in time for everyone to leave school."

                M "Excuses."
                M "Can't believe you misspelled \"euro\"."

                "{i}The third grade girl went on to compete in the prefectural spelling tournament as a representative of the school.{/i}"
                "{i}She lost immediately in the first round.{/i}"

            label Nine_three:

                scene theater_front with Dissolve(1.0)

                "{i}The three walk through the doors of the GRAND CINEMA and take a gander at the scenery.{/i}"

                scene theater_inside with Dissolve(0.5)

                A "Are we even at the right place?"

                M "(sniffs) Don't you smell that fresh lemony scent?"
                M "Totally a new theater smell."

                K "You're probably smelling the actual lemons they put in the drinks."

                A "Well, all this talk about lemons makes me gotta piss."
                A "I'm headin' to the toilet."

                "{i}Akiyuki walks to the restroom.{/i}"

                K "Let's just order the tickets already."
                K "The register is over there, Minato."

                M "Fine, I'll go talk to them, like I always do."
                M "You guys better do it next time."

                "{i}Akiyuki busts open the restroom door and shouts at the top of his lungs.{/i}"

                A "Hey guys!"
                A "You gotta see this shit!"

                K "Another one?"

                "{i}Minato and Keisuke follow Akiyuki into the restroom and look at the stall.{/i}"

                scene toilet with Dissolve(0.5)

                A "Looks like somebody forgot to flush."
                A "And there's no sink."
                A "It really IS brand new."

                M "What kinda restroom is this?"

                K "The brand new kind of restroom."

                A "As expected of the GRAND CINEMA."

                "{i}The three order their tickets, and the cashier directs them to the back of the cafe."
                "{i}Then they make their way to the place where they are supposed to turn their phones off and watch the movie.{/i}"

                scene theater with Dissolve(0.5)

                A "I've been all giddy waiting these past two years for this movie."
                A "Are you guys just as excited for the new \"Stellar Crusades\" as I am?"

                M "Actually yeah, I saw on the trailers there was a really hot actress for the protagonist."

                "{i}They make their way up the stairs to the seats in the back row."
                "{i}The entire row of seats is littered with trash.{/i}"

                A "Should we just sit somewhere else?"

                M "What do you mean? These are the best seats in the house."
                M "Hold my drink and popcorn."

                "{i}Minato hands over his drink and popcorn to Akiyuki."
                "{i}He bends over and removes the litter from the seats."
                "{i}Underneath the seats, Minato finds–{/i}"

                M "Are you kidding?"
                M "There's entire buckets of popcorn underneath the seats."

                A "As expected of the GRAND CINEMA."

                K "We really have the place where we are supposed to turn our phones off and watch the movie to ourselves."

                "{i}At that moment, a father and the father's child walked in and seated themselves at the front.{/i}"

                M "Thanks a lot man, you jinxed it."

                K "No I didn't."
                K "They were gonna come in either way."

                A "Let's just sit and watch the movie"

                M "I call the middle."
                M "I don't want y'all to leave me out of the conversation."

                A "Sure, if it means that much to you."

                "{i}They sit down and the movie starts.{/i}"
                "{i}After the movie finishes, the father and the father's child leave the place where they are supposed to turn their phones off and watch the movie, leaving the three alone in the place where they are supposed to turn their phones off and watch the movie.{/i}"

                A "Damn, that was pretty good."
                A "I'd give it a 9/10."

                M "I agree, at least a 9/10."

                K "I'd say it was 7/10."
                K "Not too shabby."

                A "See?"
                A "I told you guys it'd be good."

                "{i}The next day.{/i}"

                scene cafeteria with Dissolve(1.0)

                A "So, about \"Stellar Crusades: the Aura Rises\"..."
                A "Wasn't it crazy when–"

                M "That movie was shit."
                M "I don't even want to acknowledge it exists."
                M "Right, Keisuke?"

                K "Yeah, definitely the worst \"Stellar Crusades\" movie so far."
                K "Complete trash."

                A "What are you guys talking about? I thought y'all liked it."

                M "I thought about it over night and realized it was shit."
                M "Keisuke and I spent the whole night texting about all the flaws of the movie."

                K "Yeah, definitely the worst \"Stellar Crusades\" movie so far."
                K "Complete trash."

                A "You guys are just haters."

            label Nine_four:

                scene rooftop with Dissolve(1.0)

                "{i}Minato, Akiyuki, and Keisuke are eating lunch together on the rooftop."
                "{i}Minato draws on a piece of paper while he eats.{/i}"

                A "Can't believe they left the roof unlocked."

                K "I can."

                M "Hey guys, look what I made."

                "{i}He shows them his magnum opus."
                "{i}It is a drawing of a nigga man with a collar around his neck and his massah holding the end of it."
                "{i}The massah is shouting \"Useless nigger nigga, stop niggaing around you nigger.\""
                "{i}Right before they start laughing, Fumino slams the rooftop door open.{/i}"

                FOS "{size=*1.5}MINATO!{/size}"
                FOS "What are you doing up here?"
                FOS "What's that note?"

                "{i}Fumino-sensei walks over and snatches the note from Minato."
                "{i}She reads it, completely flabbergasted.{/i}"

                FOS "That's it!"
                FOS "You're coming with me to the principal's office, Minato."
                FOS "NOW!"

                "{i}Fumino grabs Minato and drags him to the office.{/i}"

                K "Guess he's getting a detention."

                A "And on black history month?"
                A "So unlucky."

                "{i}The next day.{/i}"

                scene ms_hallway with Dissolve(1.0)

                "{i}Keisuke and Akiyuki are on their way to class.{/i}"

                A "Hey, what do you think ended up happening to Minato?"

                K "Probably got expelled."

                M "Haha, very funny."

                A "Woah, where'd you come from?"

                K "What happened with the note?"

                M "Nothing happened."

                A "Whaddya mean \"Nothing happened\"?"

                M "Whaddya mean, what do I mean?"
                M "They just let me go."

                K "So I get detention for writing a single curse word, but you get off scott free for depicting the most racist shit in history?"
                K "Totally sounds fair to me."

                M "Yeah well, I'm not black."
                M "You are."

            label Nine_five:

                scene ms_classroom_morning with Dissolve(1.0)

                "{i}Daiki walks into the classroom unannounced, interrupting the class.{/i}"

                DUE "The office needs help with moving the canned goods to the storage shed..."
                DUE "I want you three to go, since y'all are exempt from exams."

                "{i}Minato, Keisuke, and Akiyuki leave the class to the office for the keys to the storage shed and the canned goods.{/i}"

                scene ms_hallway with Dissolve(0.5)

                "{i}Then they make their way to the other side of campus.{/i}"

                A "Can you believe from now to next week we're gonna be in high school?"

                M "What the fuck did you just say?"

                K "Hey alright."

                M "Let's just take these cans to the shed already."

                A "Yeah, okay man."

                "{i}They walk towards the restrooms.{/i}"

                A "Hey, remember that time I found shit in the urinal?"

                K "We never did find out who did that."

                M "It looked pretty sexy."
                M "It must've been from a girl."

                A "What the fuck did you just say?"

                K "Hey alright."

                "{i}They walk past the restroom and approach the shoe lockers.{/i}"

                M "Isn't it crazy how so many students left the school?"

                A "Wanna see if we can list them all?"

                M "That's easy."
                M "First, Jein, she left in our first year."

                A "Yeah, I never even got the chance to talk to her again."

                K "Who?"

                M "There were also a bunch in our second year that didn't come back."
                M "Sheldrieka and Jun didn't last until this year either."

                A "Don't forget Sukiko, Jenifa, and Tomoko."
                A "Those three left after the second year too."

                K "You guys are just making names up now."
                K "I think I remember some weird kid leaving though."

                A "Oh, I know who you're talking about."
                A "What was his name again..."

                M "Are you talking about Greg?"
                M "You guys remember him now!?"

                K "Nah, it was Seidohito."

                A "That's what it was!"

                M "R-Right..."
                M "So, it's only been a few that stayed here since the beginning of middle school."

                A "Seems like the school isn't going to get many incoming students either."

                K "I wouldn't be surprised if the school shuts down."

                A "Don't say that, man."
                A "We had so many cherished memories together here."

                M "Yeah, it'd suck if our middle school shut down."

                K "It's not like you need the school to stay open to remember it."
                K "Anyway, are we there yet?"

                M "No."

                "{i}They are still walking across the hallways.{/i}"

                K "Are we there yet?"

                A "Not yet."

                "{i}They are still walking across the hallways."
                "{i}A sign reads \"Three kilometers to the shed.\".{/i}"

                K "Are we there yet?"

                A "No."

                "{i}More time passes and they are walking through more hallways.{/i}"

                K "Are we there yet?"

                M " No!"

                "{i}They are walking through more hallways.{/i}"

                K "Are we there yet?"

                M "Yes."

                K "Really?"

                M "No!!"

                "{i}They pass by more hallways.{/i}"

                K "Are we there yet?"

                A "No!"

                "{i}They pass a sign that reads \"1.5 km to the shed.\".{i}"

                K "Are we there yet?"

                M "No, we are not!"

                "{i}Later as they pass through the hallway, they see a nigga bus driver outside the window.{/i}"

                K "Are we there yet?!"

                MA "No!!"

                "{i}Minato decides to mimic Keisuke.{/i}"

                M "Are we there yet?"

                K "That's not funny."
                K "It's just immature."

                M "See, this is why nobody likes niggers."

                K "Alright, your loss."
                K "I'm just gonna stop talking."

                M "Finally!"

                K "But seriously, this is taking forever."

                M "Outside the school."
                M "That's where we're going, Keisuke."
                M "Out-"
                M "-side"
                M "(whispers) the school."

                K "All right, I get it."
                K "I'm just fucking bored."

                M "Well, find a way to entertain yourself!"

                "{i}Keisuke sighs."
                "{i}Then he makes a popping sound with his fingers."
                "{i}Then pops again."
                "{i}And again.{/i}"

                M "Oh!"
                M "For five minutes..."
                M "Could you not be a nigger..."
                M "For FIVE MINUTES!"

                "{i}Akiyuki leans against the window and looks out."
                "{i}Keisuke braces his fingers and pushes them down."
                "{i}He makes the popping noise again.{/i}"

                M "Gah!!"
                M "Are we there yet?!"

                A "Yes!"

                K "Finally."

                "{i}Off in the distance, near the front gate, they see the shed.{/i}"

                scene ms_frontgate with Dissolve(0.5)

                "{i}The three arrive at the storage shed and drop the cans inside.{/i}"

                A "Hey look, that's a wagon."

                M "Keisuke, you should get on it."
                M "Akiyuki and I'll pull you around."

                K "I guess."

                "{i}Keisuke sits on the wagon with Akiyuki and Minato pulling."

                scene ms_gym with Dissolve(0.5)

                "{i}They go back inside the school building and make their way to the gymnasium.{/i}"

                M "Y'all remember the school play back in first year?"

                A "Wasn't that when Hideki got naked in front of the audience?"

                M "Yeah, he thought \"going commando\" in the script meant getting naked."

                K "What a clown."
                K "It's no wonder he didn't come back the next year."

                A "I'm gonna miss this place guys."
                A "From now to next week, we're gonna be in high school."

                M "Seriously, what the fuck are you saying?"

                K "Do you guys wanna just go home?"
                K "We don't have any exams anyway."

                M "Might as well."

                scene ms_frontgate with Dissolve(0.5)

                "{i}Minato and Akiyuki pull the wagon, with Keisuke still sitting in it, back to the front gate of the middle school.{/i}"

        label HSScript:

            label Ten_one:

                scene hs_gym with Dissolve(1.0)
                        
                "Gym"
                
                "{i}All incoming and current students gather in the gymnasium for the opening ceremony.{/i}"

                show MH_W at left
                MH "Are you getting nervous yet?"
                MH "It's our first day of high school after all."

                show KH_W at right
                KH "It's just middle school but in high school."
                KH "What's there to be nervous about?"

                MH "Look at all the new hotties dawg."
                MH "I can feel my pants getting tighter by the minute."

                KH "Classic Minato."

                MH "Hey, have you seen Akiyuki yet?"

                KH "No, not yet."
                KH "Are you sure he even applied to the same school as us?"

                MH "Yeah, because we applied for the same school."
                MH "Don't you remember?"

                KH "I don't know about that one."
                KH "He could have gone to another school instead."

                MH "Hopefully, the three of us were assigned to the same class and we'll see him then."

                "{i}A teacher places a hand on Minato's back from behind.{/i}"

                SEN "May I have your name?"

                MH "It's Minato."

                SEN "Okay, Minato. Stop talking!"

                FAT "And now, I will have the new student council president, Paruka-kun, come up and say a few words."

                show TRE_W at center
                "{i}From where the students are seated at, the student section, a student levitates to where the principal stood."
                "{i}He was blinding to look at."
                "{i}Too blinding."
                "{i}The human eye would try to adjust its focus but to no avail.{/i}"

                TRE "I, the representative of the student section from where the students are seated at, would like to extend my gratitude..."
                TRE "And I would like to extend my welcome to the new incoming students to this high school that has the name of..."

                MH "Are you seeing what I'm seeing?"
                MH "What is he, some kinda..."
                MH "Some kinda..."
                MH "Some kinda higher being?"
                MH "I think my blue eyes are playing tricks on me."

                KH "All I see is a ray of light wearing a school uniform."
                KH "And what do your blue eyes have to do with it?"

                MH "Don't you know? Blue eyes reflect blue light."

                KH "Huh?"

                "{i}The student body roars in applause after Paruka finishes his speech.{/i}"
                hide TRE_W with dissolve

                scene hs_hallway with Dissolve(1.0)
                "Hallway"
                "{i}Students crowd around the board where the faculty post the classroom assignments.{/i}"

                show MH_W at left
                show KH_W at right
                MH "I don't see Akiyuki's name in the same class as us."

                KH "I told you."
                KH "He's not attending school here."
                KH "That's why we haven't seen him."

                MH "Or..."
                MH "It's because there's so many students around compared to our old middle school."

                KH "Whatever you say man."

                "{i}Minato and Keisuke head to their homeroom classroom.{/i}"

                scene hs_classroom_front with Dissolve(1.0)
                "Classroom Morning"

                show HUK at center
                HUK "Let's see..."
                HUK "We should start with introductions."
                HUK "I'm Hiro-sensei, your homeroom teacher."
                HUK "Now, I'm going to call you kids to the front so you can introduce yourselves."
                HUK "Let's start in alphabetical order."

                "{i}Each student gives their introduction and Hiro-sensei returns to the front.{/i}"

                HUK "Let's see..."
                HUK "We finished introductions."
                HUK "I said, \"I'm Hiro-sensei, your homeroom teacher.\""
                HUK "Oh, I forgot."
                HUK "I would like for our class to do something in June."
                HUK "Anyone care to make a guess?"

                scene hs_classroom with Dissolve(1.0)
                show TSB_W at left
                TSB "Is it a bar mitzvah?"

                HUK "No."

                show RUT_W at right
                RUT "Why would it be a bar mitzvah?"

                show ALI_W at center
                ALI "Yeah, if anything, it should be a bat mitzvah."

                show TRT_G at left_two
                TRT "Why?"

                ALI "Because, women."

                "{i}TL Note: Bar mitzvah is a coming-of-age ritual for young men.{/i}"
                "{i}Bat mitzvah is for young women."
                "{i}They're celebrated in Judaism."
                "{i}This is NOT a Jewish high school.{/i}"

                HUK "We're not a Jewish high school."
                HUK "It would be neither."
                HUK "Any other guesses?"

                show TN_W at right_two
                HBI "Is it a test?"

                HUK "Why would I tell you guys about a test two months from now on the first day of school?"

                HBI "Can we..."
                HBI "Have a test in June?"

                TSB "Bii, quit being a nimrod."

                show CAT_W at left_three
                "{i}Chizuru raises her hand.{/i}"

                HUK "Yes, Chizuru-chan?"

                CAT "Does it have anything to do with bringing supplies from home?"

                HUK "That's pretty close."
                HUK "Since it doesn't look like anyone else will get any closer, I'll just have to say it."
                HUK "I want our class to have a breakfast party."
                HUK "I'm calling it \"Hiro's Dinner Bash\"."
                HUK "I want each of you to bring a breakfast item to class on that day so we can bash our dinner together."
                HUK "Hence, \"Hiro's Dinner Bash\"."

                HBI "Why are we bringing breakfast items to a dinner bash?"

                TSB "Bii, quit being a nimrod."

                HUK "Just trust me."

                scene hs_classroom with Dissolve(1.0)
                "{i}Bell rings.{/i}"

                HUK "Okay kids, have fun with your lunch."
                HUK "Don't forget to try the cafeteria cookies."
                HUK "They taste absolutely divine."
                hide HUK with dissolve

                scene hs_classroom with Dissolve(1.0)
                show MH_W at left
                show KH_W at right
                "{i}Minato goes over to Keisuke.{/i}"

                MH "Did you see that one girl, Asuka-chan?"
                MH "Her ass is huge."

                KH "What the hell are you talking about?"
                KH "She's flatter than my desk."

                MH "You need to get your eyes checked."

                KH "Whatever you say man."

                scene hs_classroom_left with Dissolve(1.0)
                show TRT_G at left
                show ALI_W at center
                show RUT_W at right
                TRT "Hey, Asuka-chan."
                TRT "Do you want to join me, Rumi-chan, and Chizuru-chan for lunch?"

                ALI "Sure, okay."

                show TN_W at left_two
                HBI "TSB-kun, let's eat together."

                show TSB_W at right_two
                TSB "No."
                TSB "I want to eat alone."
                hide TSB_W with dissolve
                "{i}TSB gets up and secretly follows The Riot's group to stalk Rumi.{/i}"

                HBI "That sucks. What about you, Atsushi-kun?"

                show ABD_W at right_two
                ABD "Sure."

                show MH_W at left_three
                MH "Asuka-chan went off with The Riot."
                MH "Do you think they're dating?"

                show KH_W at right_three
                KH "Chill out. It's only the first day of school."

                MH "He's probably trying to snag her."
                MH "I need to make a move before he snags her first."

                KH "Whatever you say man."

            label Ten_two:

                scene hs_frontgate with Dissolve(1.0)

                "Front Gate"

                "{i}Minato and Keisuke arrive at the front gate."
                "{i}Asuka, with a piece of toast hanging out of her mouth, comes running around the corner and crashes into Minato."
                "{i}They both fall to the ground.{/i}"

                MH "Ow!"

                ALI "Move it or lose it. I'm gonna be late for homeroom."

                MH "It's–"

                ALI "I'm in a rush."

                "{i}Asuka leaves around the corner.{/i}"

                MH "I think I'm in love."

                KH "She just ran you over like a bus."
                KH "How does that make you in love?"

                MH "It's love at first sight. And..."
                MH "SHE WAS HOT!"

                KH "No, she was not."
                KH "And you already saw her yesterday."

                MH "What do you know?"
                MH "Let's just hurry and head to class."

                scene hs_hallway with Dissolve(1.0)

                "Hallway"

                "{i}After second period...{/i}"

                MH "A..."
                MH "A..."
                MH "A..."
                MH "Asuka..."

                TRT "Hey Asuka-chan!"
                TRT "Let's walk to third period together."

                ALI "Okay."

                MH "Darn it..."

                scene hs_hallway with Dissolve(1.0)

                "{i}After third period...{/i}"

                MH "Let's get lun..."
                MH "lun..."
                MH "lun..."

                RUT "Asuka-chan!"
                RUT "C'mon, we're gonna be late for lunch."

                MH "{i}Really? Again...{/i}"

                scene hs_hallway with Dissolve(1.0)

                "{i}After fifth period...{/i}"

                MH "A...A...A...Asuka..."
                MH "Do you want to walk ho...ho..."
                MH "ho..."

                CAT "Hey Asuka-chan, let's head to practice together after school."

                ALI "Sure, Chizuru-chan."

                CAT "I heard they're gonna decide on the team captain today."

                ALI "Really? I wonder who it'll be..."

                "{i}Asuka and Chizuru walk away leaving Minato alone in the hallway.{/i}"

                MH "{i}You've gotta be kidding me...{/i}"

                scene rooftop with Dissolve(1.0)

                "{i}After school.{/i}"

                KH "I'm surprised it's really unlocked."

                MH "I just don't get it!"
                MH "Every time I try to approach her, I swear there's this invisible force of nature trying to tear us apart."
                MH "I know she wants me, she just doesn't know it yet."

                KH "Who?"
                KH "What are you even talking about?"

                MH "Were you even listening?"
                MH "Asuka-chan."
                MH "The girl that ran into me this morning before school."

                KH "Oh."
                KH "She's the girl with no ass."

                MH "SHE DOES HAVE AN ASS!"

                "{i}Keisuke looks over to the track field.{/i}"

                KH "Is that her down there?"
                KH "Looks like she's on the track team."

                MH "Yeah, I heard her and Chizuru-chan talking about that earlier."
                MH "Seems like our school is well-known for its track team."
                MH "We placed first place in the prefectural track tournament for the past twenty years."

                KH "I see."
                KH "I also see The Riot talking to Asuka right now."

                MH "WHAT?!"
                MH "WHERE?!"

                "{i}The Riot handed Asuka a water bottle, and they started laughing together.{/i}"

                MH "I can't believe this."
                MH "He really IS trying to snag her."

                KH "They're just talking."

                MH "It's not fair, man."
                MH "He gets to see Asuka-chan every day at track practice."
                MH "At this rate I don't stand a chance."
                MH "If only there was a way for me to consistently meet up with her..."

                scene hs_classroom_front with Dissolve(1.0)

                "Classroom Morning"

                "{i}Next Monday.{/i}"

                HUK "Now, let's decide on who'll be on class duty this week."

                HBI "Hiro-sensei, can I be on class duty?"

                HUK "Bii-kun, you were last week already."

                HBI "Can I do it again?"

                HUK "No, you can't."
                HUK "Just like last week, I'll draw a lottery for two people."

                "{i}Hiro-sensei decides on Minato and Asuka.{/i}"

                HUK "You two will be on class duty for the rest of the week."

                MH "Score! I just hit the jackpot."

                scene hs_classroom_left with Dissolve(1.0)

                "After school."

                MH "Huh?"
                MH "Where'd Asuka-chan go? Don't tell me she skipped..."
                MH "I'm the unluckiest guy on the planet."

                "{i}MH is sweep sweep sweeping the classroom by himself until...{/i}"

                ALI "Sorry I'm late."
                ALI "I had to tell the coach about me being on class duty this week."

                MH "{i}God does exist.{/i}"
                MH "H... He... Hey, A...A...A...Asuka-chan..."
                MH "What's the haps?"

                ALI "What are you saying?"
                ALI "You're strange."

                MH "{i}OMG!{/i}"
                MH "{i}She actually spoke back to me.{/i}"
                MH "Uh..."
                MH "I'm just sweep sweep sweeping."

                ALI "Oh right."
                ALI "Where's the other broom?"

                MH "Uh..."
                MH "I...It's... Uh..."

                "{i}As Minato struggles to remmeber his vernacular, Asuka checks the closet.{/i}"

                ALI "Nevermind, I found it myself."
                ALI "Let's hurry and finish so I can join practice before it ends."

                scene hs_classroom_left with Dissolve(1.0)

                "{i}Two days later.{/i}"

                "{i}After school.{/i}"

                ALI "Let's try to finish this quicker this time."
                ALI "I've been going to practice late."

                MH "O...o...o...okay Asuka-chan."

                ALI "Is there something wrong with you?"
                ALI "You talk normally in class."

                MH "No, nothing's wrong."
                MH "I'm just a little nervous."

                ALI "You're nervous about sweeping?"

                MH "No, it's nothing. Don't worry about it."

                ALI "See, now you're back to normal."

                MH "Huh, I guess so."
                MH "So, how's your practice been going?"

                ALI "I feel like I haven't been improving lately."
                ALI "I want to finish this quickly so I can get back to it."

                MH "I can handle class duty by myself."
                MH "You can go ahead and join practice the rest of the week."

                ALI "No."
                ALI "That's unfair for you."

                MH "{i}OMG!!! She cares about me!{/i}"
                MH "{i}She must have a crush on me!!!{/i}"
                MH "{i}Maybe I actually have a shot at snagging her.{/i}"
                MH "{i}But I have to make sure there's no competition...{/i}"
                MH "So... what do you think of The Riot?"
                MH "He seems... cool."

                ALI "He's aight."
                ALI "Kinda short though."
                ALI "I prefer taller guys honestly."

                MH "OH REALLY."

                ALI "Can we finish up here?"
                ALI "Practice will be over soon."

                MH "Oh right."

                scene hs_classroom with Dissolve(1.0)

                "{i}Two days later.{/i}"

                "{i}After school.{/i}"

                MH "So Asuka-chan... I've noticed you have blue eyes there."

                ALI "Yeah, so what?"

                MH "Did you know that blue eyes reflect blue light?"
                MH "My eyes are blue too."
                MH "We are basically matching..."
                MH "{i}Like a match made in heaven.{/i}"

                ALI "Wow, you really know how to make a girl feel special Minato-kun."
                ALI "For real though, I've been enjoying the time we spend together after class."

                MH "Huh? Really?"
                MH "That's great. Do you want to exchange RYNE's?"

                ALI "Sure."

                MH "Score! I just hit the jackpot again!"

                "{i}Minato and Asuka exchanged RYNE contact information via cellular handheld devices.{/i}"

                ALI "I'll text you after practice."

                MH "Fo' sho, fo' sho!"

                ALI "Huh?"

                MH "Sorry, don't know where that came from."

                scene hs_classroom_front with Dissolve(1.0)

                "{i}Next Monday.{/i}"

                "{i}Bell rings.{/i}"

                HUK "Okay, you kids have fun at lunch."
                HUK "Don't forget about my dinner bash now."

                scene hs_classroom with Dissolve(1.0)

                MH "Hey Asuka-chan, why don't we eat lunch together?"

                ALI "Sorry, I already agreed to go with Rumi-chan and Chizuru-chan."
                ALI "You can join us if you want though."

                MH "No, that's okay."
                MH "Maybe next time then."

                ALI "Sure."

                "{i}Asuka leaves the classroom with Chizuru and Rumi.{/i}"
                "{i}The Riot comes in runnin' at the speed of sound and kabedon's Minato.{/i}"

                "TL Note: Kabedon is whenever someone pins another someone onto the wall by smacking their hand onto it, placing the another someone between the someone and the wall. The another someone is usually taken aback by the proximity and dominance of someone."

                "{i}Anyways...{/i}"

                TRT "What do you think you're playing at, huh?"

                MH "Huh?"

                TRT "Let me clue you in on how things work."
                TRT "There are two kinds of people in this world."
                TRT "The Rizzer and the Rizzie."
                TRT "You aren't either."

                MH "What?"
                MH "What are you even talking about?"

                TRT "Maybe if you joined the track team, you'd be able to be a Rizzer."
                TRT "But since you're a nerd, you can't be one."

                MH "I knew it."
                MH "You ARE trying to snag Asuka-chan."

                TRT "No, I'm not."
                TRT "I just can't allow a nerd to try to Rizz someone on the track team."
                TRT "That's not how it works around here."
                TRT "You should've known the hierarchy whenever you joined this school."

                MH "What if I joined the track team?"
                MH "Then would you let me have her?"

                TRT "Of course."
                TRT "But I can't let a nerd like you join without a test first."
                TRT "If you can beat me, the team captain, in a race, then I'll let you join."

                MH "Okay, you're on!"

                TRT "See you on the field after class today, nerd."

                scene hs_track with Dissolve(1.0)

                "{i}After school.{/i}"

                "{i}Minato and The Riot are in their starting positions.{/i}"
                "{i}A crowd of students gathers around to watch the epic showdown that would surely make history.{/i}"

                HBI "What's going on?"
                HBI "Why's there a commotion on the track field?"

                TSB "The Riot said that he was going to demonstrate the strength of the track team against nimrods like you."

                ABD "AMONGST US?!"

                "TL Note: Amongst us is the astronomical hit game of sus."

                TSB "No, you nimrod."
                TSB "That's not even what I said."

                ELI "I wonder who's going to win."

                KH "Minato is obviously going to lose."

                HBI "Aren't you friends with Minato-kun?"
                HBI "Why are you rooting against him?"

                KH "I'm just stating facts."

                ELI "You're so cruel."

                KH "Kids are cruel, Eriko."
                KH "And I'm very in touch with my inner child."

                "{i}Meanwhile...{/i}"

                RUT "What's even the point of this?"
                RUT "It's not even a contest."
                RUT "Anyone can see that clearly."

                ALI "Well, we won't know until we find out."

                CAT "The Riot is the fastest on the team."
                CAT "And Minato-kun isn't even on the team, so he probably stands no chance."

                ALI "Let's just see what happens."

                "{i}Meanwhile...{/i}"

                TRT "I'm gonna run circles around you Minato-kun."
                TRT "You're gonna know what it feels like to be a dust bunny after you're done eating mine."

                MH "Huh?"

                DVD "On your mark!"
                DVD "Get set!"
                DVD "3"
                DVD "2"
                DVD "1"
                DVD "Go!"

                scene hs_hallway with Dissolve(1.0)

                "{i}The next day.{/i}"

                "Hallway"

                HBI "How about that race, huh?"

                ABD "It might as well have not even happened."

                BII "What do you mean?"

                ABD "Almost feel bad for the guy."
                ABD "He couldn't even run 100 meters in 100 seconds."

                scene hs_classroom with Dissolve(1.0)

                "Classroom Morning"

                MH "I feel so stupid."
                MH "I wasn't even half his speed."

                KH "You really are stupid."
                KH "Why'd you even try to race him?"

                MH "He wasn't gonna let me talk to Asuka-chan unless I beat him and joined the track team."

                KH "You should've known that you'd lose."
                KH "You could have just ignored him and kept talking to Asuka anyway."

                MH "How can I do that?"

                KH "You got her RYNE info, right?"
                KH "He can't stop you from texting her."

                MH "Oh, right."

                scene hs_classroom with Dissolve(1.0)

                "Classroom Morning"

                "{i}Next Monday."
                "{i}Before class.{/i}"

                MH "I've been making so much progress with Asuka-chan."
                MH "We can't talk at school, but we've been texting nonstop."

                KH "Good for you."

                MH "I know, right? It's great."
                MH "I wish these happy days would never end."

                "{i}Hiro-sensei walks in the classroom with a new student.{/i}"

                HUK "Please be seated everyone."
                HUK "Today, we have a transfer student, and he's joining our track team."
                HUK "Go ahead and introduce yourself."

                LAN "Sup."
                LAN "I'm Randori."

                ALI "Ermahgerd, he's so hot."

                TRT "The track team?"
                TRT "A new challenger?"

                MH "He's so tall."
                MH "And he's going to be on the track team."
                MH "I have a bad feeling about this."

                TSB "Rumi-dono sure is looking pretty today, for it as well."
                TSB "I'm gonna write about her in my journal again tonight."
                TSB "Gonna draw her like one of those French girls."

                HUK "That was excellent, OUTSTANDING, Randori-kun."
                HUK "You can sit in the empty seat over there, behind Asuka-chan."

                MH "Oh no."

                scene hs_classroom_front with Dissolve(1.0)

                "{i}Bell rings.{/i}"

                HUK "Okay, you kids have fun at lunch."
                HUK "Don't forget about my dinner bash now."

                "{i}Hiro-sensei leaves the room.{/i}"

                scene hs_classroom_left with Dissolve(1.0)

                ALI "Hey Randori-kun, do you wanna get lunch together?"

                LAN "No thanks. I brought my own."

                ALI "Oh, then can we eat together?"

                LAN "Sure."
                LAN "And who are you?"

                scene hs_classroom with Dissolve(1.0)

                MH "Did you see that, Keisuke?"
                MH "He's trying to snag her!"
                MH "Right in front of me!"

                KH "Asuka was the one going after him."

                MH "What do you know?"
                MH "You haven't been texting her every night."

                KH "Whatever you say man."

                MH "You don't know anything."
                MH "I'm gonna go get a drink from the vending machine in the cafeteria."

                scene hs_classroom_left with Dissolve(1.0)

                "{i}Minato gets up to leave the classroom."
                "{i}Randori stretches his leg out in front of himself and Minato trips onto the floor.{/i}"

                ALI "What happened?"
                ALI "What did you do?"

                MH "Oh, I'm fine. Nothing's wrong."
                MH "I just tripped."

                "{i}Minato leaves the classroom.{/i}"

                LAN "My leg!"

                ALI "What's wrong?"
                ALI "Do you need to go see the nurse?"
                ALI "I don't mind taking you there."

                LAN "Nah, it's fine."
                LAN "I think something hit my leg just now."

                scene hs_classroom_left with Dissolve(1.0)

                "Classroom Evening"
                
                "{i}Two days later.{/i}"

                "{i}At lunch{/i}"

                MH "Hey Asuka-chan."

                ALI "..."

                "{i}Asuka ignores Minato and walks over to Randori.{/i}"

                ALI "Randori-kun, let's eat lunch together again."

                LAN "Okay."

                "{i}Asuka and Randori leave the classroom.{/i}"

                scene hs_classroom with Dissolve(1.0)

                MH "Did you see that, Keisuke?"
                MH "Randori snagged her away again!"

                KH "You should be diagnosed with schizophrenia."

                MH "I'm telling you man, something's wrong."
                MH "I don't know why Asuka-chan is ignoring me."
                MH "She hasn't been texting me either."

                KH "Are you sure you didn't just leave your phone off?"

                MH "No, I never turn it off."
                MH "I'll show you."

                "{i}Minato pulls his phone out of his pocket and shows it to Keisuke.{/i}"

                MH "See?"

                KH "The screen's cracked."

                MH "Huh?"
                MH "Oh shit."

                scene hs_hallway with Dissolve(1.0)

                "Hallway"

                "{i}After school.{/i}"

                MH "You gotta believe me, Asuka-chan."

                ALI "Yeah right."
                ALI "I bet you broke your phone on purpose as an excuse for ghosting me."
                ALI "I gotta head on over to practice."

                "{i}Asuka leaves Minato alone in the hallway.{/i}"

                MH "I can't believe this is happening..."

                scene hs_track with Dissolve(1.0)

                "Track Field"

                "{i}Two days later."

                "{i}Before track practice.{/i}"

                CAT "You're thinking about confessing to Randori-kun?"
                CAT "Weren't you texting Minato-kun every night?"

                ALI "He's been ghosting me."
                ALI "So I'm gonna confess to the man that actually listens to me."

                RUT "I agree, you should just confess to Randori-kun already."
                RUT "I mean, he's tall."
                RUT "And most importantly, he's on the track team."

                "{i}Asuka goes over to Randori.{/i}"

                ALI "Hey Randori-kun, I gotta ask you something."
                ALI "Can you wait by the front gate after everyone leaves?"

                scene hs_frontgate with Dissolve(1.0)

                "Front Gate"

                "{i}Asuka meets up with Randori at the front gate after practice.{/i}"

                LAN "Yeah?"

                ALI "I think I like you."
                ALI "Do you wanna go out with me?"

                LAN "Sorry, I can't."
                LAN "I'm transferring to another school after today."

                ALI "Huh?"

                LAN "Yeah, so I should get going."
                LAN "Goodbye, Akane-chan."

                "{i}Asuka is completely flabbergasted as Randori leaves."

                "{i}Meanwhile, behind a tree...{/i}"

                RUT "I think it went pretty well."
                RUT "She seems smeckledorfed."

                TRT "I don't know about that."

                CAT "That's not even a good thing."

                RUT "Really?"

                CAT "We'll find out next Monday anyway."

                "{i}Meanwhile, behind another tree...{/i}"

                TSB "Since when is Rumi-dono so close to The Riot?"
                TSB "They're practically all over each other."
                TSB "This really grinds my gears."

            label Ten_three:

                scene hs_classroom_front with Dissolve(1.0)

                "Classroom Morning"

                HUK "Sorry class, hope you kids won't miss Randori-kun too much."
                HUK "He was sent back to his old school for underperforming on the track team."

                TRT "I don't get why his times were so bad."
                TRT "His times were great at the high school he went to before this particular high school."

                RUT "He did have a huge bruise on his leg."

                MH "Wait a minute..."
                MH "Was that what I tripped on?"

                ABD "That's crazy."

                ELI "I hope he isn't depressed for being inept."

                HUK "And don't forget, \"Hiro's Dinner Bash\" will be happening in less than a month."
                HUK "I bet you guys are so excited."

                HBI "I sure am, Hiro-sensei!"

                TSB "Silence, you nimrod."

                scene hs_classroom_front with Dissolve(1.0)

                "Next month."

                "Classroom Morning"

                HUK "Okay everyone, I'll explain how this is going to go."
                HUK "I want each of you to bring a breakfast dish to class tomorrow."
                HUK "Then we're going to spend the whole class socializing and having lots of fun together."
                HUK "Since The Riot is the new captain of the track team, I want him to bring the main dish."

                HBI "What's the main dish? Is it made of porcelain?"

                ELI "What kind of breakfast do you eat?"

                TSB "Bii, you nimrod. He was talking about food."

                TRT "What's the main dish, Hiro-sensei?"

                HUK "It will be waffles."

                scene hs_classroom with Dissolve(1.0)

                KH "(whisper) Damn, should've been pancakes."
                KH "(whisper) They're way better than waffles."

                MH "Yeah, sure, whatever."
                MH "Who cares?"

                KH "(whisper) Are you still hung up on Asuka, man?"
                KH "(whisper) You need to get over her."
                KH "(whisper) She wasn't even a decent option."

                MH "You weren't there man. You don't know how much she meant to me."

                KH "(whisper) Whatever you–"

                HUK "Keisuke-kun, you'll bring the salt."
                HUK "Minato-kun, you bring the pepper."

                MH "Why are we bringing condiments?"

                HUK "That's all that was left."
                HUK "Don't fret, they're actually very important."

                KH "At least I got the best condiment."

                "{i}Bell rings.{/i}"

                HUK "Good, so you all know what to bring. Let's resume this tomorrow!"

                scene hs_classroom_front with Dissolve(1.0)

                "The next day"

                "Classroom Morning"

                HUK "You all remembered to bring your dishes, right?"

                scene hs_classroom_left with Dissolve(1.0)
                
                TRT "Yep, bought the waffles from Waffle Shack."

                ALI "Ermahgerd, I love Waffle Shack."

                RUT "Their waffles are the best."

                CAT "You're so smart, The Riot."

                TRT "Ladies, ladies, please calm yourselves."
                TRT "There's enough waffles for everybody."

                CAR "Yay!!!"

                MH "Sigh..."

                KH "What a bunch of clowns."

                HUK "Bii-kun, you brought the plates, right? Set them on the desk at the front."

                HBI "Sure thing, Hiro-sensei!"

                scene hs_classroom_front with Dissolve(1.0)

                "{i}Bii drops the stack of porcelain plates at the front of the desk."
                "{i}Asuka places eggs on the desk with the rest of the dishes.{/i}"

                ALI "I brought the eggs, Hiro-sensei."

                HUK "Good job, Asuka-chan."

                scene hs_classroom with Dissolve(1.0)

                MH "Did you see that, Keisuke?"

                KH "Yeah, Bii really brought porcelain plates."

                MH "No, not that."
                MH "Asuka-chan brought eggs."

                KH "What about it?"

                MH "What do you mean, \"What about it?\"?"
                MH "You know I don't like eggs."
                MH "But I don't want Asuka-chan to think I don't want to eat hers."

                KH "So why are you telling me?"

                MH "I'm gonna put some on my plate and I want you to eat them for me."

                KH "Normally, I'd say you're crazy."
                KH "But I like eggs, so sure."

                scene hs_classroom_front with Dissolve(1.0)

                "{i}Minato grabs a plate and goes over to Asuka.{/i}"

                MH "So Asuka, I saw you brought these eggs."
                MH "I like a girl that can cook."

                ALI "My dad made them."

                MH "Oh."
                MH "Uh..."
                MH "Tell him I said thanks?"

                ALI "Whatever."

                MH "Well that went great."

                scene hs_classroom_left with Dissolve(1.0)

                "{i}Asuka goes back to The Riot, Rumi, and Chizuru.{/i}"

                TRT "Rumi-chan, go get some plates for us."

                RUT "Of course."

                scene hs_classroom_front with Dissolve(1.0)

                "{i}Rumi goes to grab four plates for her friends."
                "{i}TSBB materializes behind her.{/i}"

                TSB "Rumi-dono, do you need help carrying those plates?"

                RUT "Uh, no."
                RUT "Don't talk to me, weirdo."

                TSB "She's so nice..."

                scene hs_classroom_left with Dissolve(1.0)

                HBI "Hey Atsushi-kun, wanna eat together?"

                ABD "Nah, I'm gonna eat with The Riot and the girls."

                HBI "Are you sure they'll let you?"

                ABD "Yeah, that's why I joined the track team."
                ABD "You should join too if you wanna hang out with us."

                "{i}Atsushi goes to sit with The Riot, Asuka, Rumi and Chizuru.{/i}"

                HBI "TSBB, do you–"

                TSB "No."

                "{i}TSBB sits by himself in a corner and watches Rumi.{/i}"

                scene hs_classroom_front with Dissolve(1.0) 

                "{i}Bii goes over to Minato and Keisuke and sits next to them.{/i}"

                HBI "Is this seat taken?"

                KH "I wish it was."

                HBI "Don't be like that."

                "{i}Eriko goes over to them.{/i}"

                ELI "Can I eat with you guys?"

                MH "Whatever."

                KH "Why don't you eat with The Riot like the other girls?"

                ELI "They don't want me to sit with them."
                ELI "They said \"track team only\"."

                HBI "Well, don't mind them."
                HBI "We're an open minded clique."

                KH "Since when were we even friends?"

                MH "Whatever, just sit down."
                MH "I want this day to end already."

            label Ten_four:

                scene hs_classroom_front with Dissolve(1.0)

                "Classroom Morning"

                HUK "I regret to inform you all that the school year is almost over."
                HUK "I want all of you to know I thoroughly enjoyed my time here with you all."

                TRT "Why does it sound like you're dying?"
                CAT "Yeah, we'll be able to see you next year, right Sensei?"

                "{i}Hiro-sensei sheds a tear and hangs his head down low."

                HUK "Unfornately, that won't be the case."
                HUK "I'm leaving after this year."

                TRT "What?"
                TRT "That's terrible!"

                HBI "Say it isn't so, Hiro-sensei!"

                HUK "Regretfully, it is true."
                HUK "So, let's end this year with a bang."
                HUK "One final project, to help you kids build camaraderie with one another."

                E "Awwwwwwww."

                scene hs_classroom with Dissolve(1.0)

                KH "And here I thought the rest would be easy."

                MH "He said this is a group project, right?"
                MH "I have one final chance!"

                KH "Seriously man, you need to get over her."

                MH "Not while there's still hope."

                KH "Hope begets despair."

                MH "That doesn't even make sense."

                scene hs_classroom_front with Dissolve(1.0)

                HUK "I'll go ahead and announce the groups"
                HUK "They'll be determined randomly, so don't complain about your partner."

                scene hs_classroom with Dissolve(1.0)

                MH "{i}Please be Asuka-chan.{i}"
                MH "{i}Please be Asuka-chan.{i}"
                MH "{i}Please be Asuka-chan.{i}"

                scene hs_classroom_front with Dissolve(1.0)

                HUK "First is Asuka-chan..."

                scene hs_classroom with Dissolve(1.0)

                MH "{i}Yes!{i}"

                scene hs_classroom_front with Dissolve(1.0)

                HUK "and Chizuru-chan."

                scene hs_classroom with Dissolve(1.0)

                MH "{i}No!{/i}"

                scene hs_classroom_front with Dissolve(1.0)

                HUK "Next is Minato-kun and The Riot."

                scene hs_classroom with Dissolve(1.0)

                MH "{i}NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!{/i}"

                scene hs_classroom_front with Dissolve(1.0)

                HUK "TSBB and Bii-kun."
                HUK "Rumi-chan and Atsushi-kun."
                HUK "Last but not least, Keisuke-kun and Eriko-chan."
                HUK "I hope there won't be any problems."
                HUK "I'll hand out the outline detailing what you all will be doing for the project."

                scene hs_classroom with Dissolve(1.0)
                
                KH "Good thing Randori left, or else it'd be an odd number."

                MH "My life is over..."

                "{i}The Riot walks over and sits next to Minato.{/i}"

                TRT "You better not hold me back, Minato."

                MH "That's my line, The Riot."

                KH "What a couple of clowns."

                scene hs_classroom_front with Dissolve(1.0)

                "The next day."

                "Classroom Morning"

                HUK "For the next few days, I'm giving you ladies and gentlemen free time to work on your project."
                HUK "Feel free to move the desks and sit together."

                scene hs_classroom_left with Dissolve(1.0)

                HBI "Hey, TSBB, so how are we gonna split the workload?"

                TSB "Don't even think about touching anything, you nimrod."

                HBI "Don't be like that."
                HBI "How can I help?"

                TSB "You can help by leaving me alone, nimrod."
                TSB "{i}I can't believe Rumi-dono is working with that nimrod, Atsushi.{/i}"

                "{i}TSBB stares at Atsushi and Rumi while they work on their project.{/i}"

                TSB "{i}There has to be something I can do...{/i}"

                HBI "There has to be something I can do."

                TSB "Just stop–"
                TSB "Wait a minute..."
                TSB "Actually, there is something you can do."

                HBI "Oh boy, I can't wait!"

                "{i}Let's check on how the main character is doing.{/i}"

                scene hs_classroom with Dissolve(1.0)
                
                MH "Like I said, I'll handle this part."

                TRT "No, that's my expertise."
                TRT "I'll handle it."

                MH "Fine, then I'll do the next one."

                TRT "Nuh uh, I'm better at that too."

                MH "You can't be good at everything."

                TRT "Oh, I know that one."
                TRT "It's called an oxymoron."

                MH "There's definitely a moron somewhere around here."

                TRT "Hey now, don't say that about yourself."
                TRT "I know I'm amazing, but you're not that bad."

                MH "{i}I hate my life.{/i}"

                scene hs_classroom with Dissolve(1.0)

                "{i}The next day.{/i}"

                MH "–and that's how we'd do it."

                TRT "I see, I see."
                TRT "Not bad, I don't think I would've done it that way by myself."
                TRT "You're actually like, pretty smart or something, huh?"

                MH "Naturally."
                MH "But your ideas are pretty creative too, not gonna lie."

                TRT "Thanks man."

                "{i}Across the other side of the room.{/i}"

                scene hs_classroom_left with Dissolve(1.0)

                HBI "And so, that's what he said."

                ABD "Dang that's great."
                ABD "Rumi-chan and I weren't sure what to do, so this really helps us out."
                ABD "Are you sure it'll be okay?"

                HBI "Yep."
                HBI "He said the criteria is the same for everybody, so it won't matter if some stuff is the same."
                HBI "I believe he also wanted you to keep it a secret from Rumi-chan."

                ABD "Poggers."

                scene hs_classroom_front with Dissolve(1.0)

                "The final day."

                "Classroom Morning"

                HUK "Okay class, I hope you're all ready to present your projects."
                HUK "Asuka and Chizuru, you two go to the front and start us off."

                AC "Yes, sensei."

                "{i}They presented their project with no issues.{/i}"

                HUK "Excellent, next is Minato and The Riot."

                "{i}Minato and The Riot present their brilliant project perfectly, bouncing off each other like the ideal married couple.{/i}"

                HUK "T-That was beautiful..."
                HUK "I never knew you two were such great partners!"

                TRT "What can I say except..."
                MH "You're welcome."

                "{i}The classroom roars with applause for the two boys.{/i}"

                HUK "That was a very tough act to follow, but no pressure."
                HUK "Next is TSBB and Bii-kun."

                "{i}TSBB presents the project by himself, while Bii acts as his cheerleader.{/i}"

                HUK "That will suffice, you two."
                HUK "Next, Atsushi-kun and Rumi-chan."

                "{i}Atsushi and Rumi walk up to the front.{/i}"
                "{i}They present their project, and it has the exact same content as TSBB and Bii's project.{/i}"
                "{i}TSBB raises his hand.{/i}"

                HUK "Yes, TSBB?"

                TSB "Have you noticed something strange, Hiro-sensei?"
                TSB "Atsushi is presenting the exact same project as my group."

                ABD "What are you saying, TSBB?"
                ABD "It's the same criteria, so there's bound to be a few similarities."

                TSB "But it's the exact same."

                HUK "I did think it was quite strange."
                HUK "The previous groups all had different ideas, but Atsushi, yours is the same as TSBB and Bii-kun's."

                RUT "I don't know why it's the same."
                RUT "Atsushi gave me an outline and I just followed what he said."

                ABD "That's–"

                HUK "Atsushi-kun, did you cheat off of them?"

                ABD "W-Well, I–"

                HUK "Was Rumi-chan in on it?"

                ABD "No."
                ABD "She–"

                TSB "Sounds like Atsushi did it all by himself."

                HUK "I can't believe I'm saying this, but I'm going to have to punish–"

                "{i}Atsushi gasps loudly for air and dramatically falls on the floor in a fetal position.{/i}"

                HUK "Atsushi-kun, what's wrong?"

                RUT "I think he's having a stroke."

                TRT "I'll handle it."

                "{i}The Riot leaps to the front of the class and lifts up Atsushi princess-style."
                "{i}The Riot carries Atsushi out of the class and takes him to the school nurse.{/i}"

                HUK "Well, that was something..."
                HUK "Let's just move to the last group."

                KH "Now that's what I call a tough act to follow."

                "{i}Keisuke and Eriko presents their project and the day ends without any more theatrics.{/i}"

            label Eleven_one:

                scene hs_classroom_front with Dissolve(1.0)

                DSN "My name is Donaldville-sensei." 
                DSN "I want you all to come up to the front and introduce yourselves."
                DSN "We'll go in alphabetical order." 
                DSN "First is Akane-san."

                ANA "Um, I'm not ready–"

                DSN "Don't talk back to me." 
                DSN "Respect your sensei."

                ANA "Yes, sensei..."

                "{i}Akane goes to the front and does an elaborate curtsy.{/i}"

                DSN "Alright, sit down Akane-san." 
                DSN "Next is Akiyuki-san."

                ANA "But I haven't–"

                DSN "What was that?"

                ANA "N-Nothing..."

                DSN "That's what I thought." 
                DSN "Now, Akiyuki-san, hurry up."

                AH "{i}What a bitch...{/i}"

                "{i}Akiyuki stands at the front.{/i}"

                AH "My name is Akiyuki. I look forward to–"

                DSN "Okay, next is Chiba-san. Hurry up now, we don't have all day for this."

                "{i}Akiyuki sits down and Chiba walks to the front.{/i}"

                "{i}Chiba nods his head and then immediately sits back down.{/i}"

                DSN "That's more like it. Next is Ei-san."

                DAB "Ackshually, I think I'm next, sensei."

                DSN "DID I SAY YOU WERE NEXT?"
                DSN "No, I didn't."
                DSN "Now, Ei-san, continue."

                HEI "Hello, fellow students. I'm Ei. I'm on the track team."

                DSN "That's wonderful. Next is Mishima-san."

                KH "She must only be introducing the NPC's."

                MH "Nah, don't say that about Akiyuki."

                DSN "{size=*1.5}MINATO! Stop talking!{/size}"
                DSN "Continue, Mishima-san."

                TET "As I was saying, don't forget to check out my Modifye. You can find me under \"Lil Tetsuo\"."

                DSN "That's enough of that. This has gone on long enough." 
                DSN "Tanaka-san is the last one."
                DSN "Just raise your hand."

                "{i}Tanaka raises his hand.{/i}"

                DSN "Finally."
                DSN "Now we can get to the matter at hand."
                DSN "First off, Ei and Rumi will be on class duty this week."

                "{i}Ei raises his hand.{/i}"

                DSN "What is it?"

                HEI "I was just wondering, since I've never been selected for this before, what exactly does this \"class duty\" entail?"

                DSN "..."
                DSN "Anyway, the faculty wants me to inform you that you'll be having a school trip in your third year."

                ANA "Why would you tell us that now though?"

                DSN "If you'd let me finish, you wouldn't have to ask such a stupid question."

                "{i}Ei raises his hand.{/i}"

                DSN "What is it now?"

                HEI "Our previous homeroom teacher told us that there were no stupid questions."
                HEI "So does that mean that he lied, and are there actually stupid questions?"

                DSN "Yes."

                HEI "Was that the answer to which question?"

                DSN "Both."

                HEI "Then could you please give an example of a stup–"

                DSN "That's enough of that."
                DSN "The reason I told you children about the trip is because we want you to donate some money to it."

                "{i}Ei raises his hand.{/i}"

                DSN "No."

                "{i}Chizuru raises her hand.{/i}"

                DSN "Fine, what is it?"

                CAT "Do we have to donate to it?"

                DSN "It's a donation. None of you have to."
                DSN "But the faculty would appreciate if you did it anyway."
                DSN "You have until tomorrow to donate as much money as you–"

                "{i}Bell rings.{/i}"

                DSN "But how is that possible? I've barely gotten anything done..."

                "{i}Ei raises his hand.{/i}"

                DSN "Oh."

                scene hs_classroom_left with Dissolve(1.0)

                "{i}The next day{i}"

                AH "How much are you guys donating?"

                MH "One thousand yen."

                KH "Nothing."

                AH "Really? Not even a hundred yen coin?"

                KH "She said it was optional."

                MH "Yeah, but you should give at least something."

                KH "No, I don't think I will."

                scene hs_classroom_front with Dissolve(1.0)

                "{i}Donaldville slammed a metal box on her desk to silence the class.{i}"

                DSN "Okay everyone, please drop your donations in this box."

                "{i}The entire class, except Keisuke, puts their donations in the box on the front desk.{/i}"

                DSN "Keisuke-san, did you forget to donate to the school trip?"

                KH "Nope."

                DSN "Oh, so you already put it in?"

                KH "Nope."

                DSN "Are you going to donate anything?"

                KH "Nope."

                DSN "I see. You aren't on the track team, are you?"

                KH "Nope."

                DSN "Of course not."
                DSN "{i}This is the worst class I've ever had.{/i}"
                DSN "Let's just get on with today's lesson."

                scene hs_hallway with Dissolve(1.0)

                "The next day"

                "{i}Keisuke walks through the empty hallway.{/i}"

                KH "{i}Can't believe I woke up early for once.{/i}"

                scene hs_classroom_morning with Dissolve(1.0)

                "{i}He opens the door and sits at his desk.{/i}"

                KH "{i}There isn't even anyone here.{/i}"
                KH "{i}Makes sense, considering I'm almost an hour early.{/i}"
                KH "{i}Guess I'll just sleep until class starts.{/i}"

                scene hs_classroom_front with Dissolve(2.0)

                DSN "WHAT IS THE MEANING OF THIS!?"

                "{i}Keisuke's beauty sleep was interrupted by the wailings of the siren.{/i}"

                RUT "I don't know. I swear it was there when Ei and I left..."

                EI "Yes, the donation box was definitely in this room when we left."

                RUT "I just said that."

                EI "Yeah yeah yeah yeah."

                DSN "Somebody must've stolen it."
                DSN "Who was the first person to go in the classroom?"

                ELI "It was Keisuke-kun."

                ANA "Yeah, we saw him at his desk when we walked in."

                MH "Hey, Keisuke, did you steal the money?"

                KH "What?"
                KH "Why would I do that?"

                DSN "Keisuke-san, admit taking the money and give it back right now."

                KH "Nope."

                DSN "Your punishment will only get worse the longer this goes on."

                KH "Why do you think it was me, anyway?"

                DSN "Because..."

                "{i}Donaldville stares at Keisuke for a while.{/i}"

                RUT "He was the first person to enter the classroom."

                DSN "Yes, that's precisely why!"
                DSN "So just hand it over and quit making a fool of yourself in front of the class!"

                CAT "Yeah, Keisuke-kun, I thought you were better than that."

                ELI "Really?"
                ELI "Doesn't surprise me."

                TET "I don't know the guy, but it wouldn't surprise me either."

                KH "Whatever happened to innocent until proven guilty?"

                DSN "All the proof points to you."

                KH "Proof?"
                KH "What proof?"
                KH "An eye-witness account barely counts as proof."

                DSN "What are you talking about? That's perfectly reasonable proof."

                KH "Not without sufficient logic and reasoning that is corroborated by hard evidence."
                KH "For example..."
                KH "The supposed eye-witnesses could potentially be the ones who actually perpetrated the crime."

                ANA "Are you saying we did it?"

                DSN "Accusing others only makes you look even worse."

                KH "I never accused anyone, unlike certain other people in this room."
                KH "I don't really care about figuring out who actually did what."
                KH "But I do care about defending myself."

                DSN "And how are you going to do that? The only option is you."

                AH "Why don't we have a class trial?"

                DSN "What? What's a class trial?"

                AH "It's like a courtroom trial, with a judge and everything, but in a classroom instead."

                KH "Wow, I'm surprised you actually came up with a good idea for once."

                AH "Hey, I'm trying to help you."

                DSN "No, that's ridiculous."

                KH "Are you scared that I'll be able to prove my innocence?"

                DSN "Okay, fine then."
                DSN "You better not complain when this gets you expelled."

                RUT "This is ridiculous. We already know it's him."

                AH "If you think it's so obvious, then you can be the prosecutor."

                RUT "Is that like a doctor or something?"

                AH "..."
                AH "Sure."

                HEI "What's Donaldville-Sensei gonna be?"

                KH "Wrong."

                DSN "I heard that. And I'm obviously the judge."

                AH "That's not fair though."
                AH "You're too involved. We should have someone else be the judge."

                DSN "Really? Like who?"
                DSN "There's no one else here that could do it except me."

                HEI "How about the principal?"

                DSN "What are you talking about? He'd never–"

                FAT "That sounds like a fun idea!"

                DSN "Principal?!"
                DSN "What are you doing here?"

                FAT "I've been here the whole time."
                FAT "I was originally here for a class evaluation..."
                FAT "But then all this racket started up."
                FAT "Anyway, where's my gavel? Let's get this trial started."

                AH "We have to gather the evidence first."

                KH "We don't need evidence."

                AH "Bruh"

                KH "Besides, we're the defense."
                KH "It's not our job to gather evidence anyway."
                KH "We just need to keep the prosecution in check."

                "{i}Principal walks behind Donadsonville's desk and sits down in the chair.{/i}"

                FAT "Order! Order!"
                FAT "Everyone, please be seated."

                "{i}Everyone takes their seats.{/i}"

                scene hs_classroom_left with Dissolve(0.5)

                "{i}Minato, Akiyuki, and Keisuke sit to the right, from the principal's perspective.{/i}"
                
                scene hs_classroom with Dissolve(0.5)
                
                "{i}Donaldville and Rumi sit to the left, from the principal's perspective.{/i}"

                RUT "I thought I was the prosecutor..."

                DSN "Nobody said that." 
                DSN "You'll be my assistant."
                DSN "We'll just call the witnesses to the front and get this over with."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Okay, everything seems to be in order."
                FAT "Donaldville, explain the case to the jury."

                scene hs_classroom with Dissolve(0.5)

                DSN "The case couldn't be any more simple."
                DSN "According to two witness reports, the defendant, Keisuke-san, was seen stealing the donation money."

                scene hs_classroom_left with Dissolve(0.5)

                "{i}Akiyuki slams his palms on his desk.{/i}"

                AH "OBJECTION!"

                scene hs_classroom with Dissolve(0.5)

                DSN "What?"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Order! Defense, please wait your turn."
                FAT "Since it's your first time, I'll let you off with a warning."

                scene hs_classroom_left with Dissolve(0.5)

                AH "Damn, I always wanted to do that too."

                KH "Chill out."
                KH "I'm innocent, so there's nothing to worry about."

                MH "Why am I with you guys?"

                AH "Bruh."
                AH "You're the assistant for the defense."

                MH "Why me?"

                AH "Keisuke can't defend himself."

                KH "I could, but they probably wouldn't let me."

                MH "Fine, what am I supposed to do?"

                AH "Just sit there for now."

                scene hs_classroom with Dissolve(0.5)

                DSN "And that's the prosecution's stance on the matter."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "I see."
                FAT "Defense, explain your stance."

                scene hs_classroom_left with Dissolve(0.5)

                AH "Obviously, my client is fully innocent."
                AH "And in the proceeding hours, I plan to prove it."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Good luck."
                FAT "Donaldville-sensei, please bring out your witness."

                scene hs_classroom with Dissolve(0.5)

                DSN "The prosecution calls Eriko-san and Akane-san to the stand."

                scene hs_classroom_front with Dissolve(0.5)

                "{i}Eriko and Akane stand up at the front of the classroom next to each other.{/i}"

                scene hs_classroom with Dissolve(0.5)
                
                DSN "Girls, explain what you saw when you were on your way to class."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Remember, any attempts at falsehood is perjury, and there will be true consequences."
                FAT "Oh my, I've always wanted to do something like this."

                ANA "So, we were walking down the hallway when–"

                AH "Hold it!"

                ANA "What?"

                scene hs_classroom_left with Dissolve(0.5)

                AH "I want you to–"

                KH "What are you doing?"
                KH "You can't cross-examine them yet."

                AH "Oh, really?"

                scene hs_classroom with Dissolve(0.5)

                DSN "You have to wait until they finish their full statement."

                scene hs_classroom_left with Dissolve(0.5)

                AH "..."
                AH "Well, since it's my first time, I think I should be left off with a warning."

                scene hs_classroom_front with Dissolve(0.5)

                "{i}The judge smh his head.{/i}"

                FAT "You've already exhausted all your warnings."

                scene hs_classroom_left with Dissolve(0.5)

                AH "Why do I feel like I just lost one of my five lives?"

                KH "Look, I'll tell you where to press their statements."
                KH "Just make sure you pay attention."

                AH "Don't worry, I know what I'm doing."

                KH "..."

                scene hs_classroom_front with Dissolve(0.5)

                ANA "Anyway, like I was saying, we were walking down the hallway–"

                ELI "When we walked in, we saw Keisuke-san sleeping alone in the classroom."

                ANA "We were the first ones there, so there's no one else who could've taken the donations."

                FAT "Sounds pretty cut and dry to me."
                FAT "Defense, you can start your cross-examination."

                scene hs_classroom_left with Dissolve(0.5)

                AH "..."
                AH "Uh, Keisuke–"

                "{i}Keisuke smh his head.{/i}"

                KH "Press the first statement."

                AH "Right, I knew that."

                scene hs_classroom_front with Dissolve(0.5)

                ANA "Anyway, like I was saying, we were walking down the hallway–"

                AH "Hold it!"

                ANA "Why do I keep getting interrupted by everyone?"

                scene hs_classroom_left with Dissolve(0.5)

                AH "I swear, it's just my job."
                AH "I'm gonna need you to explain that statement further."

                scene hs_classroom_front with Dissolve(0.5)

                ANA "How?"
                ANA "We were just walking to class. What else is there to say?"

                scene hs_classroom_left with Dissolve(0.5)

                AH "..."
                AH "Yeah, you're right."
                AH "Why was I supposed to press this statement, Keisuke?"

                KH "Sigh."
                KH "Ask her to extrapolate the details."

                AH "Ask who to what now?"

                KH "That wasn't even a complicated sentence."

                AH "Be more specific."

                KH "Ask her about the time."

                AH "Oh, I get it."

                AH "What time were you and Eriko-chan walking down the hallway?"

                scene hs_classroom_front with Dissolve(0.5)

                ANA "It was pretty early, so probably around–"

                ELI "It was 8:17 when we walked inside."
                ELI "I remember because I looked at the time when we first saw Keisuke-san in the class."

                scene hs_classroom_left with Dissolve(0.5)

                KH "I went to sleep at 7:41 by the way."

                AH "Aha!"
                AH "That means there was over thirty minutes of time in-between."
                AH "More than enough time for someone else to take the donations while Keisuke was asleep."

                DSN "Objection!"

                AH "Huh!?"

                scene hs_classroom with Dissolve(0.5)

                DSN "That line of reasoning would be true."
                DSN "If it wasn't based on pure assumptions."

                scene hs_classroom_left with Dissolve(0.5)
                
                AH "N-Nani?!"
                AH "Keisuke was asleep, so anyone could've snuck in and–"

                scene hs_classroom with Dissolve(0.5)

                DSN "And that is where your argument falls apart."
                DSN "There aren't any witnesses to corroborate the supposed fact he was just sleeping."
                DSN "If anything, the half hour gap just proves he had more than enough time to commit the crime himself..."
                DSN "And pretend to sleep as if nothing happened."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "I have to say, I agree with the prosecution's assertion."

                scene hs_classroom_left with Dissolve(0.5)
                
                AH "T-This can't be."
                AH "Nice going Keisuke, you just made things worse for yourself."

                KH "Establishing the facts early on is important."
                KH "I just wanted to know how big the gap in time was."

                MH "Well, looks like it's over for you guys."

                AH "No. There's gotta be something else we can do."

                KH "Yeah, like object the third statment."

                "{i}Akiyuki gave Keisuke a bombastic side-eye.{/i}"

                KH "Just trust me."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Defense, please continue your cross-examination."

                scene hs_classroom_left with Dissolve(0.5)

                AH "Yes, your honor."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Oh my, I've always wanted to be called that."

                ANA "Anyway, like I was saying, we were walking down the hallway–"

                ELI "When we walked in, we saw Keisuke-san sleeping alone in the classroom."

                ANA "We were the first ones there, so there's no one else who could've–"

                AH "Objection!"

                ANA "Really?"
                ANA "Me again?"
                ANA "What is it now?"

                scene hs_classroom_left with Dissolve(0.5)

                AH "Yeah, Keisuke, what is it now!?"

                KH "Are you serious?"
                KH "It's very obvious."

                AH "If it's so obvious, you should have no trouble explaining."

                KH "That's actually pretty fair."
                KH "They aren't the first ones to enter the classroom."

                AH "Oh wait, I see where you're going with–"

                scene hs_classroom with Dissolve(0.5)

                "{i}Donaldville slams her fist on her desk.{/i}"

                DSN "Objection!"
                DSN "The defendant was the first one there."
                DSN "He had half an hour to do as he pleased before anyone else entered the classroom."
                DSN "And a minute after the two witnesses entered, I joined them."
                DSN "It's just not plausible for anyone else to have taken it."

                scene hs_classroom_left with Dissolve(0.5)

                AH "Objection!"
                AH "That wasn't going to be our line of reasoning."

                scene hs_classroom with Dissolve(0.5)
                
                DSN "What other avenues could there possibly be?"

                scene hs_classroom_left with Dissolve(0.5)

                AH "Within that half hour gap, there could've been someone else who entered the classroom."
                AH "Keisuke went to sleep immediately, so he wouldn't have seen them."
                AH "It would have been ample time for them to take the donations and leave!"

                scene hs_classroom with Dissolve(0.5)

                DSN "Objection!"
                DSN "That's the best you could come up with?"
                DSN "A mysterious third party, that just so conveniently evaded the defendant and the witnesses?"
                
                scene hs_classroom with Dissolve(0.5)

                FAT "The prosecution is correct."
                FAT "Unless the defense can name this third party, I'm afraid I'm going to have to shut down this line of reasoning."

                scene hs_classroom_left with Dissolve(0.5)

                AH "Well, Keisuke?"

                KH "To be frank, I don't have a name."
                
                MH "Well, looks like it's over for you guys."

                AH "Whose side are you on?"

                MH "I'm just saying, if Keisuke was the first person to enter–"
                MH "Hey wait, how was Keisuke the first person to enter the class?"

                KH "Whaddaya mean?"

                MH "Whaddaya mean what do I mean?"

                KH "I just opened the door and sat down."

                MH "You don't think that's weird?"

                KH "Oh."
                KH "I'm surprised I didn't realize that sooner."

                AH "Realize what?"

                MH "Keisuke shouldn't have been able to get in, because the door should've been locked."

                AH "Of course!"
                AH "Wow guys, can't believe it took you so long to notice that."
                AH "I was just about to bring it up in my earlier objection too."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Defense, stop talking amongst yourselves!"
                FAT "It's obvious you don't have a reasonable answer to my prior inquiry."
                FAT "So I only have one last question for you."

                scene hs_classroom_left with Dissolve(0.5)
                
                AH "Wait, what does that mean?"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "If you can't answer properly, I'm going to have to give a verdict."

                scene hs_classroom_left with Dissolve(0.5)

                AH "That sounds bad."

                KH "It'll be fine." 
                KH "We already know what to point out."
                
                AH "Right."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Is there anything that these witnesses have said that alludes to the facts of this case being different?"

                scene hs_classroom_left with Dissolve(0.5)

                AH "Yes, your honor, there is."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Really?"
                FAT "Which one?"

                scene hs_classroom_left with Dissolve(0.5)

                AH "Akane-chan."

                scene hs_classroom_front with Dissolve(0.5)

                ANA "Why is it always me?"

                scene hs_classroom_left with Dissolve(0.5)

                AH "You stated in your official testimony that no one else could've done it, except my client."
                AH "But that statement, doesn't hold up with the evidence."

                scene hs_classroom_front with Dissolve(0.5)

                DSN "Objection!"
                DSN "We've already been through this."
                DSN "Keisuke was the first one there–"

                scene hs_classroom_left with Dissolve(0.5)

                AH "Objection!"
                AH "Keisuke couldn't have been the first person there."
                AH "And the evidence supports this."

                scene hs_classroom with Dissolve(0.5)

                DSN "What?"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "I can't turn a blind eye to that."
                FAT "What evidence supports the reasoning that Keisuke wasn't the first person in the classroom?"

                scene hs_classroom_left with Dissolve(0.5)

                AH "That evidence is..."
                AH "That Keisuke was in the classroom!"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "..."
                FAT "WHAT!?"

                "{i}Murmurs of how stupid that sounded ring throughout the classroom.{/i}"
                "{i}The judge slams his gavel on his desk.{/i}"

                FAT "Order! Order!"

                scene hs_classroom_left with Dissolve(0.5)

                MH "Where'd he even get that?"

                KH "No clue."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Akiyuki!"

                scene hs_classroom_left with Dissolve(0.5)

                AH "Yes, your honor?"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Please explain yourself in a way that makes sense to the court."

                scene hs_classroom_left with Dissolve(0.5)
                
                AH "Keisuke being in the classroom first..."
                AH "Is the very thing that proves he wasn't in the classroom first."

                scene hs_classroom with Dissolve(0.5)

                DSN "Wait, it can't be..."
                DSN "No!" 
                DSN "That's impossible!"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "I feel as though I'm missing something."

                scene hs_classroom_left with Dissolve(0.5)

                AH "It's elementary, my dear Honor."
                AH "At the end of every school day, all the classroom doors are locked."
                AH "And yet, Keisuke was able to enter the classroom before the Sensei."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Oh, I see!"
                FAT "That does seem like quite the conundrum."

                scene hs_classroom with Dissolve(0.5)

                RUT "He probably just stole the key too."

                scene hs_classroom_left with Dissolve(0.5)

                "{i}Akiyuki slams his fist on his desk.{/i}"

                AH "Objection!"
                AH "{i}I think I've got the hang of this now.{/i}"
                AH "Donaldville-Sensei herself can prove whether that's true."
                AH "Well?"

                scene hs_classroom with Dissolve(0.5)

                DSN "..."
                DSN "The key was in the office, where it was supposed to be."
                DSN "He couldn't have taken it without someone seeing him do it."

                scene hs_classroom_left with Dissolve(0.5)

                AH "And there you have it."
                AH "My client had no opportunity to commit the crime, so he has to be found not guilty."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "..."

                scene hs_classroom with Dissolve(0.5)

                DSN "Objection!"
                DSN "Just because the door wasn't locked, doesn't prove he didn't steal the donations."
                DSN "He clearly took advantage of the rare opportunity to commit his crime."

                scene hs_classroom_left with Dissolve(0.5)

                AH "What?"
                AH "O-Objection!"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Overruled."
                FAT "The prosecution makes an excellent point."
                FAT "The detail of the unlocked room feels troublesome..."
                FAT "But I don't see how it has any bearing on the case."

                scene hs_classroom_left with Dissolve(0.5)

                AH "You can't be serious..."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "If you can't provide any compelling reason why this reasoning should continue to be explored..."
                FAT "I'm going to have to end the cross-examination, and precede with my verdict."

                scene hs_classroom_left with Dissolve(0.5)

                AH "What am I gonna do?"

                KH "I think the reason everyone is so insistent on me is because there's no one else to point at."

                AH "Thanks, captain obvious."

                KH "I wanted to prove my evidence without incriminating anyone else."
                KH "But I care more about me than anyone else."
                KH "I think it's time to just point out who did it."

                AH "You know who did it?"

                KH "Well, I–"

                AH "Why'd you wait until now to tell me?"

                KH "I–"

                AH "Your Honor!"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Have you finished gathering your thoughts?"

                scene hs_classroom_left with Dissolve(0.5)

                AH "Yes."
                AH "The reason why my client, Keisuke, couldn't do it..."
                AH "Is because someone else did!"

                "{i}The courtroom was more silent than a graveyard at the reveal of this revelation.{/i}"

                AH "But wait, there's more!"
                AH "And he, I mean, I can point out who did it."

                scene hs_classroom with Dissolve(0.5)

                DSN "Oh really?"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "That's a bold statement, attorney for the defense."
                FAT "I'm going to have to press you on that one."
                FAT "This better be within reason, or else I'll have to end the trial immediately."

                scene hs_classroom_left with Dissolve(0.5)
                
                AH "No worries."
                AH "So Keisuke, who did it again?"

                KH "..."
                KH "I don't know."

                AH "What!?"
                AH "But you said you knew!"

                KH "I never said that."
                KH "But it doesn't matter." 
                KH "There's still a way we can turn things around in our favor."

                AH "You've gotta be kidding me."
                AH "How can that even be possible?" 
                AH "This situation is hopeless."

                KH "You'll have to call a witness to the stand."
                KH "Say that the cross-examination of the witness will bring out who did it."

                AH "What witness?"

                KH "Bii."

                AH "Who?"

                MH "He's that guy on the track team."

                AH "Oh, you mean Ei."

                MK "Who?"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Defense, it's time up."

                scene hs_classroom_left with Dissolve(0.5)

                AH "Yes, your Honor."
                AH "At this time, I cannot specifically point out the culprit."
                AH "But I can call out a witness who'll reveal their identity."

                scene hs_classroom with Dissolve(0.5)

                DSN "Objection!"
                DSN "What's the point of another testimony at this stage?"
                DSN "This charade has gone on long enough."

                scene hs_classroom_left with Dissolve(0.5)

                AH "{i}Oh well. Can't say I didn't try.{/i}"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "I hereby overrule that objection."

                ASN "What!?"

                FAT "If this witness can point out the true culprit..."
                FAT "Then I see no reason to end this trial until we hear their testimony."

                scene hs_classroom_left with Dissolve(0.5)

                AH "Yes!"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "But don't get too excited, defense."
                FAT "If the witness testimony proves to be unfruitful, then I'm declaring my verdict immediately."
                FAT "Don't expect that verdict to be in your favor either."
                FAT "Now then–"

                "{i}Bell rings.{/i}"

                FAT "Oh well then."
                FAT "Time for an intermission."

                scene hs_classroom with Dissolve(0.5)

                DSN "Why can't we just finish this now?"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Surely you aren't suggesting to deprive these kids of their midday meal, right Donaldville-sensei?"

                scene hs_classroom with Dissolve(0.5)

                DSN "O-Of course not, principal."

                scene hs_classroom_left with Dissolve(0.5)

                MH "We were just about to get to the good part too."

                AH "Whaddaya mean \"we\"?"
                AH "I was doing all the work."

                MH "Without me, you guys wouldn't have even gotten this far."

                AH "Whatever makes you feel better."
                AH "More importantly, why did you want to call Ei up there, Keisuke?"
                AH "What does he have to do with it?"

                KH "Honestly, I would've preferred to call Rumi."
                KH "But she's the prosecutor's assistant, so that probably wouldn't have worked."

                AH "But why those two?"

                MH "Oh, I get it now."
                MH "That actually does make a lot of sense."

                AH "You gonna answer any of my questions?"

                KH "Calling Bii up will reveal who the true culprit is."
                KH "I'm certain of that."

                AH "It's Ei."

                KH "Whatever."

                "{i}Tanaka and Chiba walk up to them.{/i}"

                THO "Akiyuki, you were on fire out there."
                THO "You may not need it, but we have something to tell you."

                AH "What's up?"

                XC "We saw who took the donation box."

                MAK "FOR REAL!?"

                THO "We were the last ones to leave class yesterday, and that's when we saw it."

                MH "If you saw it happen, why are you just now mentioning it?"

                XC "We were getting to that."

                THO "We didn't know what we actually saw at first."
                THO "We were in the hallway, and it was pretty dark since the lights were off."

                XC "But we saw someone mess with Donaldville-sensei's desk."

                AH "Who was it?"

                XC "It was definitely a guy."

                MH "You didn't think that was suspicious?" 
                MH "Why didn't you tell anyone when this started?"

                XC "For all we knew it could've just been Keisuke."

                THO "But now, after seeing Akiyuki's stunning defense, we're certain it wasn't him."

                XC "Plus, we wouldn't have seen anything if it was Keisuke, all things considered."

                AH "What does that mean?"

                KH "Obviously, they mean I wouldn't be dumb enough to get caught if I was gonna do it."

                XC "Let's go with that."

                KH "What time did you guys see that happen?"

                THO "It was around 17:30."
                THO "We stayed after to check out the clubs and stuff."

                XC "They were wastelands though." 
                XC "Everybody just joins the track team."
                XC "It didn't take long for us to get back and grab our stuff from the class."

                THO "Someone must've walked in behind us though, 'cause we only saw him from the hallway after we left."

                AH "That means it happened yesterday."
                AH "We know whoever did it went in the classroom after you guys left, around 17:30."

                MH "That means anyone could've done it."

                KH "Which is not good, cuz they're probably gonna blame me for it anyway."

                THO "Guess it really didn't help much, huh?"

                AH "Nah, thanks guys."
                AH "This means we have a backup plan now, just in case."

                KH "We won't need it though."
                KH "I'm certain Bii will tell us everything we need."

                AH "It's Ei."
                AH "And we'll see about that."

                "{i}Bell rings.{/i}"

                scene hs_classroom_front with Dissolve(0.5)

                "{i}The judge slammed his gavel on his desk.{/i}"

                FAT "Now, let's resume the trial."
                FAT "I believe the defense was about to call the next witness to the stand."
                FAT "Is the defense prepared to name this witness?"

                scene hs_classroom_left with Dissolve(0.5)

                AH "Yes, your Honor."
                AH "The witness we want to call up to the stand..."
                AH "Is Ei-san!"

                scene hs_classroom with Dissolve(0.5)

                DSN "Ei? Oh god, why him?"

                scene hs_classroom_front with Dissolve(0.5)

                "{i}Ei walks up to the front of the classroom.{i}"

                scene hs_classroom_left with Dissolve(0.5)

                AH "Please state your name and occupation for the court."

                scene hs_classroom_front with Dissolve(0.5)

                HEI "I'm Ei, and I'm on the track team."

                FAT "Hmm? A member of the esteemed track team?"
                FAT "What bearings could this young gentleman have on this case?"
                FAT "I shouldn't have to remind the defense of the consequences if this testimony turns out unrelated."

                scene hs_classroom_left with Dissolve(0.5)

                AH "Of course not."
                AH "The defense is certain that the testimony of Ei will bring out the truth."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "And what is the prosecution's stance?"

                scene hs_classroom with Dissolve(0.5)

                DSN "I believe that Keisuke stole the donations, and all the facts of the case point to this conclusion."

                RUT "Don't you mean we believe?"

                DSN "No."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "I understand both of your stances."
                FAT "So let's get the testimony started."

                scene hs_classroom_left with Dissolve(0.5)

                AH "Witness, please explain what you did after class yesterday."

                scene hs_classroom_front with Dissolve(0.5)

                HEI "Yeah yeah yeah yeah."
                HEI "I performed my class duties."
                HEI "And then I went home."

                scene hs_classroom_left with Dissolve(0.5)

                AH "..."

                scene hs_classroom with Dissolve(0.5)

                DSN "..."

                scene hs_classroom_front with Dissolve(0.5)

                E "..."

                FAT "..."
                FAT "Is that it?"

                HEI "Yeah yeah yeah yeah."

                FAT "I think I've heard enough."
                FAT "I'm ready to give my verdict."

                scene hs_classroom_left with Dissolve(0.5)

                AH "{i}Well, it was fun while it lasted.{/i}"

                KH "Objection."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Defendant? What's the meaning of that lukewarm objection?"

                scene hs_classroom_left with Dissolve(0.5)

                AH "Yeah, I'm supposed to do that."

                KH "You were too slow."
                KH "The judge can't give a verdict yet."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Why not?"

                KH "It's the defense's absolute right to be given the chance to cross-examine every witness testimony."
                KH "Akiyuki hasn't given his cross-examination yet, so you have to uphold that right."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Really? Is that how this works?"
                FAT "Now that I think about it, I heard something like that in a video game once."
                FAT "Defense, please proceed with the cross-examination."

                scene hs_classroom_left with Dissolve(0.5)

                AH "Nice save."
                AH "So, now what? You said Ei would tell us everything."

                KH "No, I said that about Bii."
                KH "I've never even heard of Ei."

                MH "I know how you feel, but his name is definitely Ei."

                AH "We're doomed."

                KH "Just ask him to elaborate on what he did during his class duties."
                KH "Tell him to be specific."

                AH "Got it."

                scene hs_classroom_front with Dissolve(0.5)

                HEI "Yeah yeah yeah yeah."
                HEI "I performed my class duties–"

                scene hs_classroom_left with Dissolve(0.5)

                AH "Hold it!"
                AH "Explain in detail what you did while you were on duty."
                AH "Be specific, don't leave anything out."

                scene hs_classroom_front with Dissolve(0.5)

                HEI "Yeah yeah yeah yeah."
                HEI "{i}I've been waiting for this!{/i}"
                HEI "So after the bell rang when class ended, I met up with Rumi."
                HEI "I reminded her about our duties, but she said she couldn't do them because she's on the track team."
                HEI "As you all know, I'm also on the track team."
                HEI "Even though we both had the same obligations, I was forced to cover for her."
                HEI "Once I was done I took the donations box out of Donaldville-sensei's desk."
                HEI "And I put it in the locker at the back of the room."
                HEI "That was at 17:42."
                HEI "I left the door unlocked and left the classroom."
                HEI "Finally, I walked home."

                scene hs_classroom_left with Dissolve(0.5)

                AH "..."

                scene hs_classroom with Dissolve(0.5)

                DSN "..."

                scene hs_classroom_front with Dissolve(0.5)

                E "..."

                FAT "..."
                FAT "D-Did this witness just confess to committing the crime?"

                scene hs_classroom with Dissolve(0.5)

                "{i}Donaldville slams both her fists on her desk.{/i}"

                DSN "OBJECTION!"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "What is the meaning of this outburst?"

                scene hs_classroom with Dissolve(0.5)
                
                DSN "This is ridiculous!"
                DSN "They must've forced him to give a false testimony!"

                scene hs_classroom_left with Dissolve(0.5)
                
                "{i}Akiyuki slams his fist on his desk.{/i}"

                AH "Objection!"
                AH "We did no such thing!"
                AH "He willingly admitted to doing it."

                scene hs_classroom_front with Dissolve(0.5)

                HEI "Yeah yeah yeah yeah."

                FAT "Someone, check the back locker now!"

                "{i}The closest student, Mishima, opens the locker and finds the donations box.{/i}"

                TET "It's in here." 
                TET "All the money's still there too."

                FAT "Goodness me!"

                HEI "Everything I said is true."

                scene hs_classroom with Dissolve(0.5)

                "{i}Rumi slams her palm on the desk and injures herself.{/i}"

                RUT "Ow!"
                RUT "I-I mean, objection!"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "What can it possibly be now?"

                scene hs_classroom with Dissolve(0.5)

                RUT "Ei is lying!"
                RUT "I never forced him to do the class duties by himself."
                RUT "I was there with him the whole time."

                DSN "And there you have it."
                DSN "They must've told him to concoct this story during the intermission."

                scene hs_classroom_left with Dissolve(0.5)

                AH "We–"

                KH "We know that's not true, Akiyuki."
                KH "And we can prove it, right?"

                AH "R-Right, that's what I was gonna say."
                AH "How can we prove it again?"

                MH "Tanaka and Chiba, right?"
                MH "They were with us, so they can vouch we never talked with Ei."

                scene hs_classroom_left with Dissolve(0.5)

                DSN "Don't even try to call any more witnesses."
                DSN "You probably coerced them for it as well."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Prosecution, I'm overruling your objection."

                scene hs_classroom with Dissolve(0.5)

                DSN "WHAT!?"
                DSN "Why?" 
                DSN "It makes perfect sense!"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "As long as there isn't anyone who can say for certain whether the defense tampered with this witness's testimony..."
                FAT "We have to accept it as the truth."

                scene hs_classroom_left with Dissolve(0.5)

                AH "{i}Yes!{/i}"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "However..."

                scene hs_classroom_left with Dissolve(0.5)

                AH "{i}No!{/i}"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "The prosecutor's assistant has brought up a new problem."
                FAT "Can anyone in the gallery confirm whether she went to track practice yesterday?"

                CAT "I know she wasn't there."

                ANA "I'm also on the team, and I didn't see her."

                scene hs_classroom with Dissolve(0.5)

                RUT "See? I'm not lying."

                scene hs_classroom_left with Dissolve(0.5)

                HEI "For the record, I didn't lie either."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "Sorry, but it looks like that's not the case."
                FAT "Unless there's anyone else that can corroborate your testimony, I'm going to have to disregard it."

                scene hs_classroom_left with Dissolve(0.5)
                
                AH "{i}This is it, isn't it...{/i}"

                KH "I think I know how to turn things around."
                KH "Akiyuki, it's time for that backup plan."

                AH "But Donaldville-sensei already shut it down."

                KH "Not completely."
                KH "We just have to point out the other possibility next."
                KH "Like I said at the beginning, logical reasoning is far more valuable than any witness testimony."

                AH "What's the other possibility?"

                KH "The possibility that both sides are telling the truth."
                KH "At least to an extent."

                AH "Whaddya mean?"

                KH "Ei isn't lying, and the members on the track team aren't lying."
                KH "They have no reason to."
                KH "The only person that gains anything from lying is Rumi."

                AH "But Akane-chan and Chizuru-chan agreed with her."

                KH "They said she wasn't at practice, which is probably true."
                KH "But that doesn't mean she was with Ei doing her class duties."

                AH "Oh, you're actually making sense for once."
                AH "Your Honor!"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "This better be good."

                scene hs_classroom_left with Dissolve(0.5)

                AH "The defense has multiple witness accounts that corroborate the fact that Ei-kun was working alone yesterday."

                scene hs_classroom with Dissolve(0.5)

                DSN "Objection!"
                DSN "And the prosecution has multiple witness accounts that state she was in fact doing her class duties with Ei-san."

                scene hs_classroom_left with Dissolve(0.5)

                AH "Objection!"
                AH "That's not what they say!"
                AH "They only said she wasn't at practice."
                AH "There isn't a single witness that has seen her with Ei, during the crucial time."

                scene hs_classroom with Dissolve(0.5)

                DSN "But that's ridiculous."
                DSN "If she wasn't at track, then she'd be doing her assigned class duties."
                DSN "Where else would she be?"

                scene hs_classroom_front with Dissolve(0.5)

                FAT "I have to say, I'm leaning towards the defense's side at the moment."
                FAT "Prosecution, if you can't produce a witness that has seen Rumi-chan with Ei-kun..."
                FAT "Then I'll have to end this trial with my verdict."
                FAT "The school day is almost over after all."

                scene hs_classroom with Dissolve(0.5)

                DSN "You can't be serious."
                DSN "There has to be someone who saw her."

                scene hs_classroom_front with Dissolve(0.5)

                TET "Uh, if I can say something, I did see Rumi-chan."

                FAT "And who are you?"

                TET "I'm Mishima, an aspiring music artist." 
                TET "You can find me on Modifye under the name \"Lil Tetsuo\"."

                FAT "No thank you."
                FAT "But you say you saw the prosecutor's assistant?"

                TET "Yeah, as I was walking outta class, I saw Rumi-chan leaving the building."
                TET "Must've been around 16:20. Point is, I saw her leaving school."
                TET "I thought she was goin' to practice, but the ladies said she wasn't there."
                TET "So I figure she was skippin', you feel me?"

                FAT "Oh my, heavens no."
                FAT "But if those events are true–"

                scene hs_classroom with Dissolve(0.5)

                DSN "Objection!"

                scene hs_classroom_front with Dissolve(0.5)

                "{i}The judge smh his head.{/i}"

                FAT "Overruled."
                FAT "I'm sure you'll say this testimony was fabricated as well?"
                FAT "The only testimony that disagrees with the facts is the one of the prosecutor's assistant."

                scene hs_classroom with Dissolve(0.5)

                RUT "But I–"

                DSN "Silence girl!"
                DSN "You'll be getting a severe punishment when this is over."
                DSN "Not only skipping your class duties, but also track practice?"
                DSN "You're in for a lot of trouble."

                RUT "Y-Yes Ma'am..."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "I believe this trial has reached its conclusion."
                FAT "I hereby sentence the defendant, Keisuke, not guilty."

                "{i}The judge slammed his gavel on his desk.{/i}"

                scene hs_classroom_left with Dissolve(0.5)

                AH "Does this mean we won?"

                MH "Yeah, I think so."

                KH "Of course we did, I was innocent the whole time."

                scene hs_classroom_front with Dissolve(0.5)

                FAT "There's just one last thing I don't quite understand."
                FAT "What made you do it, Ei-san?"
                FAT "You just moved the box, without taking any of the money."
                FAT "Surely there's an explanation?"

                HEI "Yeah yeah yeah yeah"
                HEI "Your Honor, I was offended."
                HEI "Offended that I had to perform the duties all in my lonesome, when it's supposed to be a duel effort."
                HEI "I wanted to get back at the girl who wronged me."
                HEI "So I moved the box, and left the door unlocked."
                HEI "I wanted her to realize what happens when you don't carry out your responsibilities as a dutiful student."

                FAT "You do realize, you're getting punished too, right?"

                HEI "I am?"

                scene hs_classroom with Dissolve(0.5)

                DSN "Of course you are."
                DSN "You hid the donation box, and left the door unlocked."
                DSN "But most egregiously, you wasted everyone's time with this nonsensical class trial."

                scene hs_classroom_front with Dissolve(0.5)

                HEI "Yeah yeah yeah yeah."

                "{i}Bell rings.{/i}"
                "{i}And so, the Great Class Trial of the Second Years ended.{/i}"
                "{i}Akiyuki became famous amongst the school as the laudable lawyer that defended that one black kid against all odds.{/i}"

            label Campaign_prologue:

                scene rooftop with Dissolve (1.0)

                "{i}After school.{/i}"

                MH "Did you guys hear?"

                KH "Yeah, I can hear."

                AH "Our old middle school is being closed down, right?"

                KH "Not really surprising."
                KH "It was a shit school. They barely had any new enrollments."

                MH "What are you talking about?"
                MH "You're telling me you're not gonna miss our old middle school?"
                MH "We made so many memories there."

                KH "So what?"
                KH "We don't exactly need our old middle school to remember it anyways."

                MH "You just don't get it."

                AH "I think we should hold a reunion with everyone from middle school."
                AH "What do y'all think?"

                MH "Yes! We should totally do that."
                MH "{i}I CANNOT wait to see Maruiko-chan after all these years again.{/i}"

                AH "Let's meet up with everyone at the GRAND CINEMA this weekend."

                scene theater_front with Dissolve(1.0)

                "{i}The weekend.{/i}"

                KH "Looks the exact same as last time."

                MH "Whaddaya mean? They clearly renamed themselves." 
                MH "It's not the GRAND CINEMA anymore. It's the SUPER STAR THEATRE now."

                KH "Akiyuki's late. Probably cuz no one's showing up."

                MH "What do you mean?"

                KH "If I was asked to go to a reunion with my middle school classmates..."
                KH "I'd say \"No.\"."

                AH "Sorry, I'm late."

                MH "What took you so long?"
                MH "And more importantly, who's coming?"
                MH "{i}Please tell me Maruiko-chan is coming.{/i}"
                MH "{i}Please tell me Maruiko-chan is coming.{/i}"
                MH "{i}Please tell me Maruiko-chan is coming.{/i}"

                AH "About that..."

                scene toilet with Dissolve (0.5)

                "{i}Two hours earlier...{/i}"

                AH "Yeah, that's why I called."
                AH "I was planning on doing a middle school reunion since the school's closing and all."
                AH "What do ya say? Do you think you can come?"

                BM "No."

                SHR "No."

                EI "Fo' sho? Fo' sho."

                BII "No."

                TY "No."

                CAM "No."

                SDK "No."

                GNG "Go nigga go."

                RIN "No."

                JEN "No."

                TIN "No."

                HN "No."

                RF "He can't come to the phone right now."
                RF "He's dead."

                LYN "Camouflage."
                LYN "So the robbers won't steal it."

                MI "No. And don't call me EVER again. Dumbass."

                JNE "I won't be able to go. I'm going out of town with my family."

                AH "Jeez, I didn't expect that."
                AH "Who should I ask instead?"
                AH "I don't like having an odd number going to the movies."
                AH "Especially since Minato wants to be in the middle."
                AH "He's always complaining about being left out of a conversation."
                AH "Hmmm..."
                AH "I could try asking her."
                AH "We haven't talked since that trial, but we're in the same class."

                scene theater_front with Dissolve (0.5)
                
                "{i}Back to the future.{/i}"

                AH "That's about it."

                MH "So, who'd you ask after?"

                ANA "Am I late?"

                AH "No, we all just got here."

                KH "Actually, we've been here for a while."

                AH "Shut up, Keisuke."
                AH "Guys this is Akane-chan. And that's Minato and Keisuke."

                MH "We know, she's in our class."

                KH "Really? I've never seen her before in my life."

                ANA "Anyway, I heard you guys were having a middle school reunion."
                ANA "Is it okay for me to join?"

                AH "Yeah, it's totally fine."
                AH "I called everyone from our old middle school and they couldn't come."
                AH "And one of them even died."

                ANA "Was I your last choice?"

                AH "Yes, but also the only choice."

                ANA "Such a charmer."

                AH "Everyone else I asked didn't want to come so..."

                ANA "Y'know, I've been here before. It was back whenever this theater was called..."

                MAK "The GRAND CINEMA."

                MH "Yeah. We're basically regulars here."

                scene theater with Dissolve (0.5)
                
                "{i}The group make it to The Place Where They Are Supposed to Turn Their Phones Off and Watch the Movie (Screening Room) and sit down in their seats."

                KH "By the way, what movie are we even watching?"

                AH "\"Start User One\"."

                ANA "I heard it's going to reference a lot of movies."

                MH "Yeah, like \"This\" and \"That\"."

                KH "Never heard of it."

                ANA "I love \"This\" and \"That\"!"
                ANA "I saw that a long time ago with my family."

                MH "Oh yeah? You remember the part where–"

                AH "So Akane-chan, I remember you mentioned you were on the track team."
                AH "How's it been during your second year?"

                ANA "Oh. Yeah, track..."

                AH "Something the matter?"

                ANA "I'm actually thinking of quitting the track team."

                AH "Waaaahhhhhh?"
                AH "That's crazy."
                AH "For what reason could you possibly ever wanna do that?"

                ANA "The atmosphere of that team gives me bad vibes."
                ANA "Everyone gossips about the people who haven't joined the team."
                ANA "They even laugh about bullying some of the students."

                MH "No way."

                ANA "YES way."
                ANA "Especially Bro. He's the biggest offender."
                ANA "He's been saying he's gonna completely segregate the students once he becomes president..."

                KH "Who?"

                ANA "You haven't heard of him?"

                AH "Yeah Keisuke, you haven't heard of \"Bro\"?"
                AH "Akane, he never touches grass. Please explain to him who \"Bro\" is."

                ANA "You don't know who he is either, do you?"

                AH "Ehe."

                MH "Just explain who he is for us."

                ANA "He's the new captain of the track team this year, and he's running for student council president."

                MH "What happened to The Riot? I thought he was still the captain."

                ANA "Bro was getting better times than him, so the coach made Bro captain instead."
                ANA "Ever since then, the position has definitely gotten to his head."

                AH "What do you mean?"

                ANA "He doesn't want to just stop at leading the team, he wants to run the whole school."

                KH "So what? It's not like it matters whether he gets elected or not."

                ANA "I'm actually really worried."
                ANA "He can really change the school for the worse if he gets elected."
                ANA "That's why I don't want to support him by staying on the track team."

                AH "Does the student council president really hold that much power?"

                ANA "In a normal school they wouldn't, but the principal pretty much let's the student council handle everything."
                ANA "Something about promoting leadership. And if they're on the track team, then they even have the approval of Fuka-sensei, the assistant principal."

                KH "How do you even know about all this?"

                ANA "I actually listen during speeches."

                KH "Touché"

                MH "Maybe I should run? I could stop Bro from taking over the school."
                MH "{i}Maybe Asuka-chan would look my way once again.{/i}"

                ANA "I think anyone would be better than him at this point."
                ANA "He's serious about bringing the school hierarchy to the way it was before Paruka-senpai."
                ANA "That's been his whole campaign plan."

                MH "Never fear, Minato is here!"
                MH "I'll take care of everything."

                "{i}The lights in the Screening Room turn back on.{/i}"

                AH "Oh, looks like the movie's over."

                KH "I didn't hear a single line."

                MGO "Honestly, I was more invested in what those kids behind us were talking about than the movie."

                MGT "I know right."

                scene rooftop with Dissolve(1.0)

                "{i}Four days until the campaign application deadline.{/i}"

                "{i}During lunch.{/i}"

                HEI "Are you really going to run for school president?"

                MH "Yeah."

                HEI "Why?"

                MH "I have my reasons."

                TET "You have my vote. Anything to stop Bro from keeping the girls all to himself."
                TET "I haven't been able to get a single date."

                XC "You sure it's not because you're ugly?"

                TET "They just can't appreciate my inner beauty..."
                TET "By the way, wanna listen to this new beat I made?"

                THO "But does anyone actually know you besides us?"
                THO "If we're talkin' connections, Akiyuki-kun's probably got the best shot."

                MH "I know a lot of people."
                MH "I even have experience with going up against the track team."

                KH "Yeah, experience losing against them."

                MH "It was close though."

                XC "Maybe if you squinted hard enough, from very far away."

                AH "Let's just see what happens. Minato could win."
                AH "He beat me whenever we ran against each other for student council back in middle school."

                MH "Exactly."
                MH "Trust me. I won't let y'all down."
                MH "It'll all go smoothly."

                scene hs_hallway with Dissolve(1.0)

                "{i}Three days until the campaign application deadline.{/i}"

                "{i}Mishima promotes Minato's campaign in the hallway.{/i}"

                TET "Minato-kun is running for the student council president position."
                TET "You guys should vote for him."
                TET "And don't forget to check out my beats. You can find me on Modifye under the name \"Lil Tetsuo\"."

                STU "No thanks, I don't even know who that is."

                TET "You haven't heard of him?"
                TET "He's... He's... uh, actually, I didn't even know him till this year either."

                STU "Exactly. You proved my point."
                STU "This is why you nerds need to be segregated from us."
                STU "Bro will bring this school back to its former glory."
                STU "No longer will we have to share the same space with those who aren't even on the track team."

                "{i}The student walked away from Mishima.{/i}"

                TET "And I thought Chiba-kun was crazy."

                scene hs_library with Dissolve(1.0)

                "{i}Two days until the campaign application deadline.{/i}"

                "{i}Minato mulls over poster ideas with Akiyuki, Keisuke, and Chiba.{/i}"

                MH "Like I was saying, I think the posters should be pirate themed."

                XC "What do pirates have to do with a student council election?"

                MH "Because it's like I'm stealing the election from right under Bro's nose."

                KH "Utterly risible."

                AH "What does that have to do with Rizz?"

                MH "Oh, I know all about Rizz!"

                KH "It should have a space theme."

                XC "That's an even dumber suggestion than what Minato had."

                AH "Why don't we make it a space pirate theme?"

                MH "That actually sounds pretty cool."

                XC "This is exactly why you're going to lose."

                MH "It's going to be fine. I told Mishima-kun to sing my praises to the students."

                KH "And how's that been going?"

                XC "Everyone probably still thinks Bro is the only student campaigning."

                AH "I'm not going to lie your chances of winning are looking pretty slim."

                MH "Where there's a will, there's a way."
                MH "Even if the chances are slim, there's still a–"

                "{i}The librarian makes her way to Minato.{/i}"

                DSN "{size=*1.5}MINATO! Stop talking!{/size}"
                DSN "I knew you were trouble ever since that opening ceremony."

                scene hs_hallway with Dissolve (1.0)

                "{i}One day until the campaign application deadline.{/i}"

                "{i}Minato walks out of his classroom and sees Asuka standing in the hallway.{/i}"

                MH "Asuka-chan? Were you perhaps waiting for me?"

                ALI "Yes, I was."
                ALI "We have something to talk about."

                MH "Oh, this is great."
                MH "I've been trying to find a way to talk to you again this whole year."

                ALI "Don't talk, just listen."
                ALI "I've heard that you're trying to run against Bro. I want you to stop campaigning RIGHT NOW."

                MH "Why?"

                ALI "Because I want him to win."
                ALI "You don't stand a chance against him anyway."
                ALI "Just stop before you embarrass yourself in front of the whole school again."
                ALI "That's all you'll get for going against the track team."

                "{i}Asuka walks away leaving Minato alone in the hallway."

                MH "{i}I have to quit before Asuka-chan starts hating me."

                scene rooftop with Dissolve(1.0)
                
                "{i}Day of the campaign application deadline."

                "{i}During lunch.{/i}"

                MH "And that's why I'm not gonna run for student council president anymore."

                KH "Is that really all it took? So the past week was all for nothing?"

                XC "I should've known this was gonna happen."
                XC "You weren't gonna win anyway. Saves everyone some time I guess."

                TET "I worked so hard to promote you though. You can still win, man."

                MH "It's not about me winning. I can't do this anymore because Asuka-chan asked me not to."
                MH "What kind of guy would I be if I let her down?"

                KH "A smart one."

                AH "I need to go to the restroom to clear my bladder."

                scene hs_hallway with Dissolve(0.5)
                
                "{i}Akiyuki leaves the rooftop and makes his way downstairs."

                "{i}As Akiyuki turns the corner, he falls to his knees."
                "{i}And before him was a bright light, the BRIGHTEST LIGHT he hasn't seen since his first opening ceremony.{/i}"

                AH "God?"

                TRE "This must be fate. You're the one that I've been looking for."
                TRE "The one that will bring about a great big change to this school."
                TRE "YOU will finish what I started."
                TRE "Hurry."
                TRE "There's not much time. We should make haste."

                AH "What are you talking about?"

                TRE "I want you to be the next student council president."

                AH "Sorry, I don't think I should."
                AH "I wouldn't win even if I tried."

                TRE "Whaddaya mean?"
                TRE "Don't you know what will happen to this school if no one puts a stop to the track team? It'll be–"

                AH "The track team makes up almost half of the student body. No one can win an electino against that."

                TRE "I did it."

                AH "Well, that's different. You're practically beaming with charisma."
                AH "I'm not like you."

                TRE "Very true."
                TRE "But that wasn't always the case."
                TRE "Back when I was a first year, I was just like you."
                TRE "No charisma, no friends, no girls, no money, no one on my side."
                TRE "You have no idea how much worse this school was before I succeeded."

                AH "I actually have friends though?"

                TRE "The school did not even allow students that weren't on the track team to run for student council."
                TRE "Even the assistant principal backed them in all their decisions that promoted discrimination."
                TRE "The only reason I was given a chance was because I begged the principal on my knees."

                AH "You did that?"

                TRE "I did what needed to be done."
                TRE "And it's thanks to my desperation that I was able to put a stop to the track team."
                TRE "I can see it in your eyes, the same look of desperation that I had, many years ago..."

                AH "Wasn't that, like, last year?"

                TRE "Please."
                TRE "If you don't do this, everything that I've worked for would be undone."

                AH "But what if I fail?"

                TRE "You won't fail."
                TRE "Like I said, you and I were cut from the same cloth. If I did it, you can too."
                TRE "Once you finish what I started, you can stop the track team from single-handedly usurping power ever again."

                AH "I guess I can at least try it."

                TRE "Do or do not, there is no try."

                AH "Isn't that copyrighted or something?"

                TRE "Now go!"
                TRE "Go and turn in your campaign application, before it's too late!"

                AH "Yes, Paruka-senpai!"

                "{i}Akiyuki runs to the office and turns in the application at the last second.{/i}"

            label Campaign:

                scene hs_track with Dissolve(1.0)
                
                "{i}After school.{/i}"

                RUT "I don't understand."
                RUT "Why does the school need to hold an election?"
                RUT "It's not like anyone else is running."

                CAT "Wasn't there someone else in our year planning to run? Wasn't it Minato-kun?"

                ALI "I wouldn't worry about him."
                ALI "I've spoken to him."
                ALI "There won't be any obstacles along the way."

                BRO "Aw man. I was hoping for there to be some trouble along the way."
                BRO "It's really no fun if they don't struggle."
                BRO "Well, I guess that just makes it all the more easier to further my plans."

                CAT "Is that really for the best?"

                BRO "Of course."
                BRO "Chizuru-chan, are you telling me you aren't disgusted by those low-lifes?"

                CAT "Well, I–"

                BRO "We're the ones earning recognition for this school."
                BRO "While they continue to go about their mundane lives, we're achieving our potential EVERY SINGLE DAY."
                BRO "We shouldn't even be in the same room, let alone the same school."

                CAT "Isn't that too–"

                BRO "Trust me."
                BRO "Why do you think the trash dissassociate with us themselves?"
                BRO "They'll thank me once I'm president."
                BRO "I'll be doing them a favor by forcefully transferring them out of this school."

                CAT "I guess you're right..."

                BRO "Of course I am."

                "{i}A few meters away...{/i}"

                TRT "Tsk..."
                TRT "I'll get him back for the humiliation that I went through."

                ANA "Minato-kun..."

                "{i}The next day.{/i}"

                scene hs_classroom_empty with Dissolve(1.0)

                "{i}Before class.{/i}"

                BRO "WHAT IS THE MEANING OF THIS?! Fuka-sensei, you told me I'd be the only one running."

                FBA "I did."

                BRO "SO WHY IS HE HERE?!"

                AH "And you are?"

                FBA "Because... he submitted his campaign application at the last second the other day."

                BRO "Why didn't you do everything as the assistant principal to make it impossible for him to run? "

                AH "I'm RIGHT HERE, bro."

                BRO "Don't you DARE utter my name out of your mouth!"

                AH "But I didn't."

                FBA "Settle down, Bro. Weren't you saying that it'd be more fun to run against someone for president?"
                FBA "Now's your chance."

                BRO "That's only because I was under the impression that no one would dare face off against ME."
                BRO "Even IF someone did, I'd rather it be someone who's AT LEAST on the track team, not part of the filth."

                AH "And who are you supposed to be?"

                BRO "Trust me. You'll learn who I am through my campaign."
                BRO "And by election day, you'll wish that you never ran against me."

                AH "I'm not on the track team, so I wouldn't run against you anyway."

                BRO "You think I don't know that? What are you, \"Literal-san\"?"

                FBA "Okay, that's enough."
                FBA "Allow me to explain some things about campaigning."
                FBA "You are allowed to campaign only on school grounds."
                FBA "You are NOT allowed to offer monetary incentives to potential voters."
                FBA "And... that's it. The principal wants this to be a great experience for you two and the rest of the students."
                FBA "Follow those two guidelines, and you'll be allowed to keep campaigning."

                BRO "As expected of the principal, he's far too lax."

                FBA "Indeed, it makes my job even harder."

                AH "I have a question."

                FBA "What are you still doing here?"
                FBA "You're free to leave now."

                AH "Sheesh."
                AH "Thanks for your hard work."

                "{i}Akiyuki leaves the classroom.{/i}"

                BRO "Aren't you going to help me win?"
                BRO "I thought you wanted this school to return to its former glory, before Paruka ruined it."

                FBA "Of course."
                FBA "I'll pull out all the stops to ruin Akiyuki's campaign."
                FBA "You have nothing to worry about. Leave him to me."
                FBA "You just focus on your own campaign."

                scene rooftop with Dissolve(1.0)
                
                "{i}After school.{/i}"

                XC "You're seriously running for president?"

                AH "Yep."

                TET "Well, I'll support you in any way I can."
                TET "Anything to stop Bro from winning."

                THO "Now this is what I'm talking about."
                THO "You're gonna win. I bet Bro was shitting his pants when he found out."

                HEI "Who's Bro again?"

                AH "The captain of the track team, apparently."
                AH "Didn't you join the team alongside Atsushi-kun?"
                AH "You should know that better than me."

                HEI "You're right. You're right."
                HEI "I am on the track team."

                MH "I think you should quit while it's still early."

                XC "What are you on about?"

                MH "I'm just saying."
                MH "Bro's very popular, and all the girls swarm him."
                KH "Keisuke can attest to it."

                KH "I guess."
                KH "I probably remember seeing something like that."

                AH "Some friends y'all are."

                TET "Don't worry about it, Akiyuki-kun."
                TET "You've got me to help you."
                TET "We're gonna go big or go home."

                XC "If you're gonna run, might as well go the full mile."

                THO "Nobody even likes Bro anyways."
                THO "We all love you, Akiyuki-kun."

                KH "Sounds gay as hell."

                HEI "What's wrong with that?"

                KH "..."
                KH "Back in my day–"

                MH "You can count me out."
                MH "I don't wanna fight a losing battle."

                XC "Then leave!"
                XC "Nobody's asking for you to stick around."
                XC "Fucking loser."
                XC "Still hung up on a bitch that you only texted."

                MH "You wouldn't understand how much she meant to me."
                MH "Fine, let's leave Keisuke."

                KH "Why do I need to go with you?"

                MH "You know, because..."

                KH "Whatever you say man."

                "{i}Minato and Keisuke leave the rooftop.{/i}"

                XC "I don't understand how you've lasted so long with them, Akiyuki."

                "{i}The door to the rooftop swings open.{/i}"

                ANA "IS IT TRUE AKIYUKI-KUN?!"
                ANA "You're running for president against Bro?"

                AH "Word sure travels fast."
                AH "Yeah, that's what's happening."

                ANA "Okay, let's do this."

                AH "Whaddaya mean?"

                ANA "I'm joining your campaign team."
                ANA "We're gonna put a stop to Bro and his plans."

                AH "I can't believe I'm actually running for student coucil president..."

                scene hs_frontgate with Dissolve(1.0)
                
                "{i}The next day."
                "{i}Akiyuki and his team begin campaigning throughout school before homeroom."
                "{i}Ei and Tanaka try to convince the incoming students to support Akiyuki.{/i}"

                HEI "Please, consider Akiyuki-kun for school president."

                THO "Please, consider Akiyuki-kun for school president."

                "{i}One of the students stops in front of them.{/i}"

                STU "What are you two nerds doing?"

                HEI "We're helping our good friend Akiyuki."

                THO "He's campaigning against Bro for student council president."

                STU "You guys should just quit while you still can."
                STU "You don't stand a chance against Bro anyway."
                STU "You'd be making it easier for everyone involved."

                THO "That's not true."
                THO "Akiyuki is the man who'll save our school."

                "{i}The student walks away, completely ignoring Tanaka"
                "{i}At lunch."
                "{i}Mishima goes up to the students waiting in line.{/i}"

                TET "Think about it, do you really wanna listen to Bro's voice EVERY day?"

                STU "That sounds good to me."

                TET "See?"
                TET "We're the same."
                TET "Wait, that's not what I–"

                STU "What are you even trying to say?"

                TET "Uh..."
                TET "Anyway, check out my official music debut, it's on Modifye."

                STU "No."

                scene rooftop with Dissolve(1.0)
                
                "{i}After school."
                "{i}The group of people who are campaigning for Akiyuki meet up at the rooftop.{/i}"

                AH "So, what's the haps?"

                THO "It hasn't been going so well."

                TET "Yeah, my monthly listeners haven't increased at all."

                XC "No one's even paynig attention to us."
                XC "We gotta do something to change their opinion of Bro."
                XC "They like him too much to accept anyone running against him."

                AH "How are we supposed to do that?"

                XC "Aren't you supposed to be the leader?"

                ANA "Calm down guys."
                ANA "It's only the first day."
                ANA "There's still plenty of time for us to turn things around."
                ANA "Let's just keep doing what we've been doing."
                ANA "I know we'll get through to them eventually."

                AH "Sounds good to me."

                XC "What if it doesn't work out?"
                XC "Then what?"

                AH "Then I don't know what I'm gonna do if it doesn't."

                "{i}The next day."
                "{i}Before class."
                "{i}Tanaka and Chiba wait at the front gate for the incoming students to promote Akiyuki in front of the gate to the incoming students.{/i}"

                THO "Please vote for ma boi, the one and only Akiyuki."

                XC "This is dumb, they're not even looking at us."

                THO "We can't give up hope."
                THO "If we keep trying, someone's bound to listen."

                "{i}During lunch.{/i}"

                AH "How'd it go at the front gate?"

                THO "Well–"

                XC "It went just as bad as yesterday."
                XC "Standing around and asking for votes won't do us any good."

                AH "What about posters?"

                HEI "What about posters?"

                AH "I was thinking we could use posters for the campaign."

                THO "That's a great idea, Akiyuki!"

                TET "Yeah, and we'll add a QR code that directly links to my Modifye page."

                XC "That's retarded."

                "{i}Akiyuki, Akane, and Chiba get the campaign posters ready.{/i}"

                ANA "These posters turned out pretty good."

                XC "At least they're better than Minato's."

                AH "That's a low bar."

                ANA "What are you guys talking about?"

                AH "Anyways, where should we post these posters?"

                XC "Around the school, where else?"

                AH "Fo' sho, Fo' sho!"

                "{i}The next day."
                "{i}After school.{/i}"

                "{i}Fuka-sensei goes around the school and removes the posted posters that Akiyuki's campaign group posted around the school.{/i}"

                FBA "That should be the last of them."

                BRO "Fuka-sensei, what's the haps?"

                FBA "Oh, nothing."
                FBA "I've just been taking out the trash."

                BRO "Here, take my empty water bottle while you're at it."

                FBA "What do you think you're doing?"
                FBA "I had to run around all day taking down these stupid posters while you've just been slacking."

                BRO "Why are you snapping at me?"
                BRO "I don't have to do anything to beat that monkey anyway."

                FBA "We can't give them any chances."
                FBA "Have you forgotten that Paruka won the election last year?"
                FBA "You still need to be cautious."

                BRO "Yes'm."

                "{i}The next day."
                "{i}During lunch."
                "{i}Akiyuki and his CC (Campaign Crew) gather on the rooftop.{/i}"

                TET "Didn't you guys hang up posters yesterday?"

                XC "Yeah, what about it?"

                HEI "Where'd you hang them up?"
                HEI "I wasn't able to witness any of them."

                XC "What?"

                AH "Yeah, what are you talking about?"
                AH "We hanged them up everywhere around the school."

                THO "I didn't see any either."

                "{i}Akane slams open the rooftop door to the rooftop.{/i}"

                ANA "Ermahgerd, I found all our posters in the dumpster behind the school."

                XC "What were you doing at the dumpster?"

                AH "That's not important."
                AH "What do you think the special for today's lunch is?"

                ANA "Uh, curry?"
                ANA "Anyway, the thing we need to focus on is who did this?"

                AH "It has to be someone that stays behind school and knew we were hanging up the posters..."

                XC "Literally anyone could have done it, dumbass."

                THO "It must've been Bro."
                THO "He's trying to sabotage our campaign."

                ANA "It couldn't have been Bro, because he has track practice."

                TET "He could've had someone else do it."

                ANA "But everyone who follows him is on the track team."
                ANA "I don't think Bro is that cunny."

                "TL Note: Cunny means conniving."

                XC "Why are you defending him so profusely?"

                ANA "I'm just–"

                AH "C'mon Chiba, cut her some slack."
                AH "We're all supposed to be in this together "

                HEI "So, what are we gonna do about this?"

                THO "I saw Bro out in the front gate this morning."
                THO "He was giving a speech to the incoming students ontop of a box."

                AH "What was the box for?"

                XC "That's not the important part, dumbass."
                XC "You're saying we should do that too, right?"

                TET "That's a great idea, Tanaka!"

                AH "Then let's do that after school."

                ANA "I don't know about that one."
                ANA "I think we should find out who took down the posters."

                XC "We don't have time to focus on that."
                XC "The longer we wait, the more advantage Bro will gain against us."

                HEI "Yeah yeah yeah yeah."

                "{i}After school."
                "{i}Akiyuki and the gang set up a box in front of the front gate."
                "{i}Akiyuki stands on the box and gives his speech to the students leaving the school.{/i}"

                AH "–and that's why you should vote for me, Akiyuki."

                TET "Bars."

                STU "Akiyuki?"
                STU "I feel like I've heard that name from somewehere..."

                STU "Isn't he the student who won against Donaldville-sensei?"

                STU "Oh yeah, I remmember him now."
                STU "If he's the one running for student council president, then I don't mind supporting him."

                THO "See, I knew you had a good chance."

                AH "Maybe you're right."
                AH "Let's see how it goes tomorrow, before homeroom."

                "{i}The next day."
                "{i}Before homeroom.{/i}"

                AH "Please allow me to take a moment of your time, and listen to what I have to say..."

                "{i}Akiyuki stands on a box and gives a speech to the incoming students."
                "{i}The rest of his campaign team stand behind him.{/i}"

                THO "He's so immaculate."
                THO "He's doing beautifully out there."

                XC "I'm surprised the students are actually stopping to listen to him."

                "{i}Mishima goes to the students and interrupts Akiyuki's speech."

                TET "If you're interested, please listen to my Modifye."
                TET "Oh yeah, and vote for Akiyuki too, I guess."

                XC "Stupid ass."
                XC "Ignore the first thing he said."
                XC "Just vote for Akiyuki."

                "{i}A small crowd forms in front of the front gate.{/i}"
                "{i}Fuka-sensei walks up and approaches Akiyuki from behind.{/i}"

                FBA "Akiyuki-kun, you're blocking the entrance."
                FBA "End this now and follow me."

                "{i}Akiyuki follows Fuka-sensei to an empty classroom.{/i}"

                AH "You asked for me, Fuka-sensei?"

                FBA "Yes."
                FBA "Take a seat."

                "{i}Akiyuki takes a seat at a desk nearby.{/i}"

                FBA "What do you think you're doing?"

                AH "What do you mean?"
                AH "I was just campaigning?"

                "{i}Fuka-sensei clenches a fist behind her back.{i}"

                FBA "The reason I called you here is because I want you to suspend your campaign."

                AH "WHAT?!"
                AH "Why would you do that?"

                FBA "I simply cannot allow Bro to lose to you."
                FBA "Not just you, but anyone not on the track team."
                FBA "You all leave a bad taste in my mouth that I can't even wash away with twenty-one bottles of sake."

                AH "Shouldn't you be dead?"
                AH "I'm pretty sure the maximum intake of sake is four cups."

                FBA "I AM PERFECTLY FINE!"
                FBA "Ahem."
                FBA "As I was saying, you will suspend your campaign."
                FBA "I will not allow you to campaign on my school grounds."
                FBA "If I find out that you do, I will immediately transfer you and your friends to another school in a different prefecture."
                FBA "Am I clear?"

                AH "(sighs) Yes, Fuka-sensei."

                "{i}In the hallway, The Riot walks by the empty classroom as Akiyuki and Fuka-sensei hold their conversation.{/i}"

                TRT "I can't believe Fuka-sensei would use such underhanded tactics."
                TRT "Sounds like a job for The Riot!"

                "{i}During lunch."
                "{i}Akane waits for The Riot on the rooftop."
                "{i}The Riot slams open the rooftop door and greets Akane.{/i}"

                TRT "Kept you waiting, didn't I?"
                TRT "Sorry, it's a habit of mine to make the damsels wait on me."

                ANA "Uh, sure."
                ANA "So, why'd you call me here alone?"
                ANA "It better be something important."

                TRT "It is very important, little lady."

                ANA "I'm taller than you."

                TRT "Anyway, it's about Akiyuki and his campaign."
                TRT "I overheard Fuka-sensei threatening Akiyuki to stop campaigning."

                ANA "No way."

                TRT "YES way."
                TRT "Personally, I can't stand Bro."
                TRT "He stole my position on the track team, and my future harem."
                TRT "I'd do anything to make sure he doesn't win."

                "{i}Ei walks up the stairs to the rooftop and sees Akane with The Riot."
                "{i}He hides behind the open door and eavesdrops on their conversation."

                TRT "With my connections to the track team, I'll get them to help us take him down."

                ANA "Wait a minute, maybe you're actually onto something..."

                TRT "Of course, I'm not just a pretty face."
                TRT "With my IQ of 530,000, I can come up with the greatest of plans in under a few hours."

                ANA "Anyway, if you can get the track team to support him instead, then we can table turn this whole debacle."

                TRT "Leave it to me."

                "{i}The Riot walks off rooftop, through the open door, down the stairs, and into the school building.{/i}"

                HEI "That was pretty amongst us of them."
                HEI "I better let the guys know."

                "{i}After school.{/i}"

                XC "You want us to stop campaigning?"

                TET "That doesn't make any sense."
                TET "Why now?"

                AH "It's what needs to be done."

                THO "Homie, if that's what you want, then I will respect your decision."

                XC "You're retarded!"

                "{i}Tanaka holds his hand up in front of Chiba.{/i}"

                XC "What the fuck are you doing?"

                THO "I dunno, that's what the narration said."

                "{i}Akiyuki ignores their outerversal antics.{/i}"

                AH "It's what I want."
                AH "I know this is surprising for you guys."

                "{i}Akiyuki lowers his head.{/i}"

                AH "I'll continue campaigning alone."

                XC "(sighs) Whatever man."
                XC "Do what you want."
                XC "I don't care anymore."

                AH "Chiba-kun..."

                XC "LEAVE!"

                "{i}Akiyuki leaves the rooftop.{/i}"

                XC "What's up with him?"
                XC "Why would he continue the campaign alone without us?"
                XC "And Tanaka, why'd you just let him go?"

                THO "Maybe he just wants prove he can do it alone."

                XC "That's retarded."
                XC "It's a little late to do that now."

                ANA "I have something to say."

                "{i}Ei enters the rooftop.{/i}"

                HEI "I bet you do have something to say, miss amongst us."

                TET "Who?"

                HEI "Akane is in cahoots with The Riot."

                TET "Who?"

                HEI "The former captain of the track team."
                HEI "I know because I am on the track team."

                ANA "That's right."
                ANA "I was discussing some tactics with him earlier."

                HEI "Well, well, well."
                HEI "So you finally admit it."
                HEI "You and The Riot were planning to betray us from the beginning."

                TET "That would explain why she told us to keep doing the failed practice of spittin' bars at the front gate."

                XC "So that's why she knew where the missing posters were."
                XC "She's the one who put them there from the start!"

                THO "I thought it was strange how she defended Bro earlier, but it all makes sense now."

                HEI "She was about to use the track team against us too, but thanks to my sleuthing, I have foiled her plans."

                ANA "That's not–"

                XC "Leave."

                ANA "But–"

                XC "LEAVE!"

                "{i}Akane leaves the rooftop.{/i}"

                THO "What are we going to do?"
                THO "Should we tell Akiyuki-sama about this?"

                XC "No, he'll just try to defend her."

                TET "Facts."

                "{i}The next week."
                "{i}Before class."
                "{i}Akiyuki walks down the halls.{/i}"

                STU "Hey."
                STU "Aren't you Akiyuki-san?"

                AH "Yes, I am."

                STU "I've heard about you."
                STU "You're running against Bro, for student council president, right?"

                AH "Yeah, I guess so."

                STU "Word of advice, quit while you still can."

                "{i}The student walks away from Akiyuki.{/i}"

                AH "Thank you...?"
                AH "What a jackass"

                "{i}A black, first year, gay student walks up to Akiyuki.{/i}"

                BGF "Ermahgerd, Akiyuki-senpai?"

                AH "Yes?"
                AH "And you are?"

                KAS "It's me, Kiyotaka."
                KAS "We went to the same middle school."
                KAS "I was a year below you."

                AH "Hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm."
                AH "Oh, I remember now."
                AH "I didn't know you enrolled in this school too."

                KAS "Yeah, it was close to my house."

                AH "Yeah, I know what you mean."

                KAS "Anyways, I've heard from my friends on the track team that you're running for student council president."

                AH "Something like that."
                AH "Wait, why'd the track team tell you about it?"

                KAS "I'm also on the team, and one of our senpai told us to support you in the election."

                AH "Who's that?"

                KAS "I think he called himself The Riot."

                AH "Oh really."
                AH "I think it's about time I have a chat with this, \"The Riot\"."

                KAS "I'll take you to him."

                "{i}Kiyotaka takes Akiyuki to the track field.{/i}"

                KAS "Hey, The Riot-senpai, I have the man of the hour himself with me."

                TRT "For real?"
                TRT "It's a good thing I'm the only one who trains before school."
                TRT "We can discuss everything without Bro intercepting us."

                AH "So, why are you trying to help me become student council president?"

                TRT "Our goals align with each other."
                TRT "You want to win the election, and I want Bro to lose the election."

                AH "But I thought everyone on the track team hated the students who didn't join."

                TRT "Times have changed."
                TRT "I've come to realize that even some of you nerds can contribute to our school."

                AH "Thank you?"

                TRT "Thanks to Akane-chan's help, I've been able to convince some of the track team to support you instead of Bro."

                AH "Akane-chan?"
                AH "Wait, Akane-chan has been helping you?"

                TRT "Of course."
                TRT "This plan couldn't have come to fruition without her."

                AH "Where is Akane?"
                AH "I want to discuss this with her too."

                TRT "I haven't seen her in a while."
                TRT "She'll probably meet with your campaign team after school as per usual."

                AH "I don't think so."

                TRT "Why not?"

                AH "I told them to disband."

                KAS "Why'd you do that?"

                AH "It's a long story."

                KAS "But if they're your friends, they would probably most liekly still try to help you anyway."
                KAS "'Cause that's what friends are for."

                AH "Friends, huh?"
                AH "I guess it wouldn't hurt to try."

                "{i}During lunch.{/i}"

                BRO "Great job on the thing you did earlier on."
                BRO "It's practically like I'm the only one campaigning again."

                FBA "That's because you are."

                BRO "But I still hear a few murmurs about that Akiyuki-kun."
                BRO "Isn't there anything else you can do?"

                FBA "It's nothing to worry about anyway."
                FBA "Any and all interest relating to him should go away soon."

                BRO "What should I do now?"

                FBA "How about..."

                "{i}On the other side of the school."
                "{i}As Akiyuki turns the corner, he falls to his knees."
                "{i}And before him was a bright light, the BRIGHTEST LIGHT.{/i}"

                AH "Paruka-senpai?"

                TRE "How's the campaign going?"

                AH "It's been rough."

                TRE "How come?"

                AH "I'm not even allowed to properly campaign."
                AH "I have to do the rest alone."

                TRE "Alone?"
                TRE "Didn't you say you had friends?"

                AH "I had to abandon them."

                TRE "You stupid?!"
                TRE "How could you abandon your friends?"

                AH "I didn't want to involve them in any trouble."

                TRE "Did you even ask how they feel about it?"
                TRE "You can't throw away the people who are willing to stick with you at your lowest."

                AH "You might be right..."

                TRE "I AM right."
                TRE "It was the same for me when I was campaigning."
                TRE "I couldn't do anything by myself, it was thanks to my friends I was able to find hope and break past the barrier of the track team's influence."

                AH "Paruka-senpai, I need to go."

                TRE "Goooooo."

                "{i}After school.{/i}"

                XC "So, why'd you call us up here?"
                XC "I thought you didn't need us."

                AH "I'm sorry."

                "{i}Akiyuki bows on his knees before everyone.{/i}"

                AH "I told you guys that I could do this campaign alone, but I cannot."
                AH "You all helped me begin this campaign."
                AH "It wouldn't be right to finish it without the people that stood by me, my friends."
                AH "Please help me become the student council president."

                "{i}Everyone stays silent and looks at Akiyuki.{/i}"

                XC "Dumbass."
                XC "There's no need for all the formalities."

                THO "Don't you remember?"
                THO "We want you to win."
                THO "That's why we'll stick with you until the end."

                HEI "Yeah yeah yeah yeah."

                TET "I cannot wait to take Bro down."

                AH "Wait, aren't we missing someone?"
                AH "Where's Akane?"

                HEI "We taught that bitch a lesson."

                AH "What?"

                XC "We found out she wasa sabotaging our campaign."

                THO "Yeah, she was using The Riot to turn the track team against us."

                AH "That doesn't even make any sense."
                AH "The track team was already against us to begin with."

                TET "Oh, we didn't think of that."

                AH "I've already talked with The Riot."
                AH "He and Akane were using the track team to support me, not sabotage me."

                THO "Really?"

                XC "I guess we owe her an apology."

                AH "Yeah, that's not cool you guys."
                AH "Accusing her of that without any evidence."
                AH "Didn't you guys learn anything from the start of the year?"

                "{i}They call Akane to the rooftop to apologize.{/i}"

                EEA "We're sorry."

                ANA "Don't worry about it guys."
                ANA "We have more pressing matters to attend to..."

                AH "I guess I should tell you guys the reason I started acting so stupid."

                "{i}Akiyuki tells them about Fuka's threat.{/i}"

                XC "You should've just told us earlier."
                XC "I wouldn't mind transferring anyway."
                XC "This is a shit school."

                ETM "Agreed."

                THO "Now that everything's cleared up, let's clue Akiyuki-kun in on what we've been doing."

                AH "What do you mean?"

                XC "We came up with the idea to campaign for you, indirectly."

                TET "Even though you told us to stop, we never did."
                TET "We went around and promoted you, and my Modifye, to everyone we saw."

                THO "We expected many people to ignore us."
                THO "But instead, they only ignored Mishima-kun."

                AH "That sounds good and all. But doesn't Bro still have a way larger audience than me?"

                ANA "We'll see how it goes."

                "{i}One month later."
                "{i}Before school.{/i}"

                BRO "Listen to me!"
                BRO "We need to restore this school back to its former glory!"
                BRO "I can do that!"
                BRO "I am the plan!"
                BRO "I am the answer!"
                BRO "I am the answer!"
                BRO "I am the plan!"
                BRO "Vote for me as the next student council president!"

                "{i}The crowd of students applaud Bro's speech.{/i}"

                RUT "What's with everyone?"
                RUT "Why aren't they more enthusiastic?"
                RUT "Don't they understand it's a privilege to see Bro when they arrive at school?"

                ALI "They were still clapping though."

                CAT "I don't know about that one."

                "{i}After school.{/i}"

                BRO "Your suggestions panned out wonderfully."
                BRO "The crowd this morning was absolutely elated to listen to my voice."

                FBA "Don't get too cocky."
                FBA "This still isn't enough to guarantee my victory."

                BRO "What are you talking about?"
                BRO "Didn't you see the crowd this morning?"
                BRO "I've got this in the bag."
                BRO "It's almost as if it was God's plan."

                FBA "Just because you got a few bitches on your dick doesn't guarantee that you'll be president."

                BRO "But what's that have to do with any–"

                FBA "Silence!"
                FBA "Do exactly as I say."
                FBA "Just like you always have."

                BRO "Y-Yes, Fuka-sensei..."

                FBA "You're in the final stretch, so you better make it count."
                FBA "This election will decide the fate of MY high school."

                "{i}Election day."
                "{i}All of the students are gathered in the auditorium for the two candidates to give their speeches.{/i}"

                FBA "After each candidate gives their speech, everyone will return to their classrooms to cast their votes."
                FBA "The votes will be counted, and the results will be announced tomorrow morning."

                "{i}Akiyuki and Bro are waiting backstage before being called out on stage.{/i}"

                BRO "Do you think you're better than me or something?"

                AH "What do you mean?"

                BRO "You didn't even print out your speech."

                AH "It's actually in my pock–"

                BRO "Well, it doesn't matter."
                BRO "You had a good run, but I was just faster."
                BRO "In fact, I don't think I've ever run against someone as pathetic as you."
                BRO "You're even worse than The Riot at running."

                AH "You know this is about the election, not track, right?"

                BRO "T-That's–"

                "{i}Out on stage.{/i}"

                FBA "\"Bro\"!"
                FBA "Please make your way to the stage."

                "{i}After Bro's speech, the student body roars in applause and cheers.{/i}"

                FBA "And the last candidate for the student council president..."
                FBA "Akiyuki-kun!"
                FBA "Make your way to the stage."

                AH "I guess it's time."

                "{i}Akiyuki comes onto the stage.{/i}"
                "{i}Akiyuki's friends cheer him on from a corner in the auditorium.{/i}"

                XC "AKIYUKI!"

                THO "YOU'VE GOT THIS!"

                ANA "WOO!"

                HEI "YEAH YEAH YEAH YEAH!"

                TET "GO BIG OR GO HOME!"
                TET "CHECK ME OUT ON MODIFYE!"

                "{i}Akiyuki sees his friends in the audience."
                "{i}Their cheers alone are louder than Bro's whole reception.{/i}"

            label Campaign_epilogue:

                "{i}The next day.{/i}"
                "{i}Akiyuki and his friends nervously await the results of the election in homeroom.{/i}"

                AH "I'm so nervous right now."

                THO "Don't be."
                THO "You did great yesterday."
                THO "Didn't you hear all the applause after your speech?"

                AH "What are you on about?"
                AH "All of the applause came from you guys."

                XC "Well, can you blame us?"
                XC "It was to make up for the fact that you spaced out in the middle of your speech."
                XC "You should be thanking us."

                ANA "Didn't you print out your speech?"

                AH "I did."
                AH "But by the time I got to the stage, I wanted to show off."

                TET "Hey, if you win, you should get people to check me out on Modifye."

                XC "SHUT YOUR DUMBASS UP!"

                HEI "Yeah yeah yeah yeah."

                "{i}The principal broadcasts his voice through the intercom.{/i}"

                FAT "As you know, the result of the votes collected yesterday would be announced today."
                FAT "After multiple recounts, as per the request of a certain faculty member, it's been decided by the student body who was elected."
                FAT "Congratulations to Akiyuki-kun for winning the election."
                FAT "That is all."
                FAT "You may continue on with the rest of your day."

                "{i}Akiyuki and the rest of the class remain silent.{/i}"

                AH "I won..."

                XC "You won..."

                ANA "He won..."

                HEI "Yeah yeah yeah yeah..."

                "{i}The rest of the class erupted in celebration.{/i}"

                THO "See."
                THO"What did I tell you, Akiyuki-kun?"

                TET "So about my compensation..."
                TET "You're going to have everyone check me out on Modifye, right?"

                "{i}Minato and Keisuke walk up to Akiyuki and the rest.{/i}"

                MH "Congratulations."
                MH "We never doubted you for a second."

                KH "I believed in you so much I even voted for Bro."
                KH "I knew you'd win anyway."

                AH "Fuck you."

            label Twelve_one:

                "{i}After school.{/i}"

                KH "There's two of them?"

                AH "They must be multiplying."

                MH "It all makes sense now."

                KH "What do you mean?"

                MH "Didn't you wonder why their names keep changing each year?"
                MH "And why one of them is larger than the other?"

                AH "That explains why he was always with us even when there was track practice."

                KH "Why didn't either of you say anything?"

                TBI "We wanted to see if you could tell us apart."
                TBI "I'm so disappointed in you guys."

                TEI "Yeah yeah yeah yeah."

                MH "Y'all are unfair."
                MH "I don't know what's so unfair, but I think it's unfair that I don't know what's unfair..."

                AH "It's like how that saying goes, \"If you make a mistake and do not correct it, this is called a mistake.\""

                KH "What the fuck did you guys just say?"

                MH "All in all."
                MH "That's crazy."

                AH "Yeah, how come no one else in this school caught on about the fact that y'all are twins."

                TBI "Ahem."
                TBI "Because..."

                TEI "I'm Ratman."

                "{i}The door to the rooftop opens.{/i}"

                BRO "President Akiyuki, I need you to go over some documents for the student council right now."

                AH "Okay."
                AH "I'll be right there."
                AH "I'll see y'all tomorrow then."

                AH "We've been walking for a while now."
                AH "I should try and break the ice."
                AH "How are you feeling about being a third year?"

                BRO "Feel about what?"

                AH "About–"

                BRO "Are you talking about the fact that I lost the election and became vice-president?"
                BRO "I'm feeling pretty swell."

                AH "..."
                AH "That's good."
                AH "Even after the election, there's still some division amongst track and non-track members."
                AH "I don't think I can do much about that."
                AH "However, I at least don't want the third years to hate each other."
                AH "If only there was something I could do to unite all the third years..."

                "{i}The next day."
                "{i}During lunch."
                "{i}Akiyuki goes around campus and invites all the third years to join his new Syschord server."
                "{i}Everyone except his friends say no.{/i}"

                DAB "I heard you made a Syschord server for the third years."

                AH "Yeah, but it looks like it'll just be me and my friends."

                DAB "I would like to join if you'll allow me."

                AH "Sure sure."

                "The day after the next day."

                "{i}Before homeroom."
                "{i}Fuka-sensei calls Akiyuki to her special empty classroom, her homeroom classroom, for a special chat.{/i}"

                FBA "I expected nothing less coming from you..."
                FBA "President Akiyuki."
                FBA "Would you mind explaining this?"

                AH "I don't know what you're talking about."

                "{i}Fuka whips out her phone and shows pictures of screenshots of text messages of a Syschord server.{/i}"

                FBA "Explain to me what this is."

                AH "It seems like she's at the beach."
                AH "No, I'm wrong."
                AH "That isn't the beach."
                AH "It's a bathtub."

                FBA "AKIYUKI-KUN."
                FBA "This isn't a joking matter."
                FBA "I need you to tell me the identity of the student who sent these messages."

                "{i}Akiyuki tells Fuka about the twins.{/i}"

                FBA "..."

                TEI "Yeah yeah yeah yeah."

                FBA "I must've drunk twenty-two too many sake bottles last night..."
                FBA "I'm seeing double."

                TBI "Who did you want to speak with?"

                FBA "Bii."

                TEI "Yeah yeah yeah yeah."

                FBA "So, you're Bii?"

                TBI "No, I'm Bii."

                FBA "Then, that's Ei, and you're Bii."

                TBI "No, I'm Bii."
                TBI "And that's Ei."

                TEI "Yeah yeah yeah yeah."

                FBA "That's what I said."
                FBA "You're Ei."
                FBA "And that's Bii."

                TBI "No."
                TBI "I'm Bii."
                TBI "And he's Ei."

                FBA "Why are you repeating what I'm saying and not just agreeing?"
                FBA "Let's get this straight."
                FBA "You are Ei."

                TEI "Yeah yeah yeah yeah."

                FBA "Then, that's Bii."

                TBI "No, I'm Bii."
                TBI "And that's Ei."

                "{i}This continues for another hour.{/i}"

                FBA "I think I'm gonna sit down."

                "{i}Fuka-sensei goes over to one of the desks, but she vomits and falls onto the floor.{/i}"

                TBI "I think we might've gone too far."

                TEI "Yeah yeah yeah yeah."

            label Twelve_two:

                "{i}After summer break."
                "{i}Monday.{/i}"

                FAT "And so, that's what happened."
                FAT "Sae-sensei will take over for Fuka-sensei until she gets well."

                SAE "Hello students, I'll be your substitute teacher for a while."

                FAT "Oh, and by the by, the third years will have a school trip."
                FAT "Sae-sensei will explain the details to you all."

                SAE "Wait–"

                "{i}Principal leaves the classroom.{/i}"

                SAE "And he's gone..."
                SAE "Well, as the principal said–"

                TEI "Sae-sensei, are you having hot sex with anyone concurrently?"

                SAE "Huh?"

                TEI "Have you ever experienced the carnal interaction of bukkake?"

                SAE "HUH!?"

                MH "Fellas, settle down."
                MH "You know those aren't the right questions to ask."

                TEB "Sorry, sir."

                SAE "Thank you, Minato-kun."

                MH "So, Sae-sensei..."
                MH "What are your thoughts on netorare?"
                MH "Mayhaps I can show you what it means."

                SAE "{size=*1.5}MINATO! Stop talking!{/size}"
                SAE "Anyway, as I was saying."
                SAE "We'll be visiting Aokigahara, also known as the Sea of Trees, a forest on the northwestern flank of Mount Fuji on the island of Honshu in Japan."

                ELI "Isn't that the forest where people seppuku all the time?"
                ELI "They be cosplaying as Sayori from DDLC."

                SAE "Yes, that is right."
                SAE "The school trip is in Aokigahara, also known as the Sea of Trees, a forest on the northwestern flank of Mount Fuji on the island of Honshu in Japan, because the faculty wants to teach the students the importance of appreciating life."

                DAB "That's so tacky."

                RUT "(disgusted face) You're so right girl."
                RUT "Like, that's so totally lame."

                CAT "Why are you talking like a gyaru?"

                RUT "Whaddya mean?"
                RUT "I've like, totally always talked this way, for realsies."

                CAT "I don't know about that..."

                SAE "Anyway, those are the details of the school trip."
                SAE "It'll be happening tomorrow."

                AH "Tomorrow?"
                AH "You just announced it today."

                KH "That only gives us about 80000 seconds to prepare."

                SAE "And that's plenty of time."
                SAE "Now, onto the next subject..."

                "{i}Tuesday."
                "{i}The students arrive at Aokigahara on Tuesday and stay until Friday.{/i}"

                MH "It's so hot out here."
                MH "I can't wait to get to the hotel."

                SAE "You won't have to wait for too long."
                SAE "The students will be put into groups of six."
                SAE "There'll be separate rooms for the girls and boys."

                MH "Too bad we can't spend time with Akiyuki."
                MH "Feels like we've been growing apart ever since high school started."

                KH "What are you on about?"
                KH "We don't need to talk to each other all the time to stay friends."

                MH "Still, we should do something together since it's the school trip."

                KH "I'm sure we'll get an opportunity eventually."

                "{i}Minato, Keisuke, Tanaka, Bii, and Ei share a room and get settled in the hotel.{/i}"

                THO "How come there's only five of us?"

                KH "There probably weren't enough guys to fill us out."

                TBI "Why are we always the last ones on the list?"

                TEI "Yeah yeah yeah yeah."

                MH "Thank god Randori transferred."
                MH "I would've joined the rest of the bodies in the forest if I had to share a room with him."

                THO "Don't say that man."

                KH "Who's Randori again?"

                TEI "Don't you remember?"
                TEI "He's the guy who transferred for only a week."

                KH "Ohya..."
                KH "Wait, how'd you know that?"

                TBI "Because I was in your class, don't act so silly."

                KH "Right, whatever you say."

                MH "What are we doing tomorrow?"

                THO "It's on the schedule they gave us. We'll be visiting the usual tourist spots."
                THO "And at the end of the day, we'll have a group camping activity where we set up tents and cook our own food."

                MH "I'm actually something of a chef myself."

                KH "Pretty sure the guys will be setting up all the tents and tables, while the girls do all the cooking."

                MH "What are we, some kinda sexism?"

                KH "What do you mean?"
                KH "That's the way it should be."

                TBI "I'm bored."
                TBI "Let's play a game."

                THO "What kind of game?"

                TBI "I don't know."

                TEI "Yeah yeah yeah yeah."

                KH "I have a deck of cards."
                KH "We can play tycoon."

                MH "I've never heard of that."

                THO "Oh, I know that one."
                THO "Isn't it played with four people?"

                KH "The twins can count as one person."
                KH "They might as well be since they look the same."

                MH "But I don't know how to play it."

                THO "I'll help you out."
                THO "Just show me your cards and I'll tell you which to use."

                MH "Thanks man, you're so nigga."

                KH "He's just gonna make you lose, stupid ass."

                MH "Nah, I trust him."

                "{i}They played seven matches of tycoon."
                "{i}Minato became the beggar every round and Keisuke was the tycoon every round."
                "{i}Wednesday."
                "{i}The male students finish setting up the tents while the females cook the food like all bitches should.{/i}"

                MH "I wonder what Asuka-chan is gonna make me for dinner."

                THO "She isn't the only girl cooking, you know."

                KH "And she's not cooking for you either."

                MH "What's wrong with you guys?"
                MH "Can't a man dream a little?"

                TEI "Yeah yeah yeah yeah."

                "{i}Chiba and Mishima walk over to Minato, Keisuke, Tanaka, Bii, and Ei.{/i}"

                XC "What are y'all doing?"

                MH "We were discussing about Asuka–"

                TET "I can't wait to get some quality cuisine from the girls."
                TET "I'm used to only eating ice sandwiches with a glass of ICE COLD milk at my house."

                XC "You're a dumbass."
                XC "They probably don't even know how to cook."
                XC "This school trip is so ass."

                THO "What do you mean?"

                XC "Whaddya mean, what do I mean?"
                XC "I'm stuck with Mishima and some goobers at the hotel, and now the only food I'll get is some garbage made by a bunch of hoes."

                TBI "Don't worry man, I heard they're making curry."
                TBI "No one can mess up curry."

                "{i}The girls finish and everyone gets their plates and sits back down.{/i}"

                TBI "See, it looks good."

                XC "Last time I checked, curry isn't supposed to be purple."

                THO "Maybe they used eggplant?"

                KH "I'm not eating any of this."

                MH "Why not?"

                KH "There's no salt."

                MH "Well, Asuka-chan helped, so it HAS to be good."

                "{i}Minato takes a bite and coughs violently onto the ground.{/i}"

                TBI "See? It must've tasted good."

                XC "I knew those hoes couldn't cook."

                TET "What do you mean?"
                TET "This is the best curry I've ever had, and I've NEVER eaten curry before."

                XC "It IS the only thing you've ever eaten that wasn't an ice cold sandwich."

                TET "Exactly."
                TET "All I need now is a glass of ice cold milk to wash all this down."

                XC "You're a dumbass."

                KH "I'm going back to the tent."

                XC "Me too."

                THO "You're not in our group, Chiba-kun."

                XC "I'm not about to stay in a tent with Mishima where he's just gonna play his shitty beats all night."

                TEI "Yeah yeah yeah yeah."

                "{i}They leave Minato on the floor and return to their tents for the night.{/i}"
                "{i}Thursday.{/i}"

                KH "Another day, another mindless droning around tourist spots doing absolutely nothing noteworthy."

                THO "C'mon, it's not that bad."

                MH "If you want some excitement, I have an idea."

                KH "Fine, I'm desperate."
                KH "What's your brilliant idea?"

                MH "You know how this hotel has a hot spring?"
                MH "We should peep on the girls when it's their turn."

                KH "Why?"

                MH "Whaddaya mean?"
                MH "This is our ONE AND ONLY chance to do this."

                TBI "I bet he just wants to see Asuka-chan naked."

                KH "I know."
                KH "And I don't see the point."
                KH "If he wants to see her naked, he can just look at the wall of this room."
                KH "There's practically no difference."

                MH "I've been telling you since first year."
                MH "She's HAWT AND has AN ASS like you wouldn't believe."

                THO "Are we going to only peep on Asuka-chan in the hot spring?"

                MH "NO!"
                MH "Well, yes."
                MH "But we're not only going to see her."
                MH "There'll be other girls there too."

                KH "They're all ugly and gross, so I'm not going."

                MH "Well, do y'all three wanna come?"

                TBI "I mean, it is our school trip."
                TBI "We should make as many memories as we can."

                TEI "Yeah yeah yeah yeah."

                THO "Me too."

                TSB "I'll come along, for it as well."

                TBI "Where'd you come from?"

                TSB "You nimrods."
                TSB "Did you not realize I was staying in the room next door?"
                TSB "And the door to your room was left wide open."
                TSB "Practically anyone passing by could come in."
                TSB "And so, let me go too."
                TSB "I would love to see Rumi-dono."

                TEI "Yeah yeah yeah yeah?"

                KH "And here I thought this was a hotel, not a circus."

                TBI "So what's our plan of attack, boss?"

                MH "The boy's turn for the hot springs is almost over."
                MH "Since the girls go after us, we'll just head inside and wait until they enter behind us."

                TES "Roger, Roger!"

                MH "Operation Peep on Asuka-chan is under way!"

                "{i}Asuka, Chizuru, Rumi, Eriko, and Akane enter the hot spring all naked.{/i}"

                CAT "This view sure is breathtaking."

                ELI "I know right."
                ELI "I thought the hot spring was going to be indoors."
                ELI "I didn't expect it to be outdoors with a view."

                ANA "It's hard to believe that we're so close to Aokigahara."

                RUT "We should've invited Sae-sensei."

                ALI "Shh, I hear something."

                "{i}The guys are hiding behind one of them big rocks.{/i}"

                TBI "I think they heard us."

                MH "Stay quiet! And move over, I can't see Asuka-chan."

                THO "If you guys keep talking, they're gonna find us."

                TEI "Yeah yeah yeah yeah."

                TSB "I can't see Rumi-dono, my glasses are all fogged up."
                TSB "I'm gonna move closer to get a better view."

                THO "No wait–"

                "{i}TSBB walks out in the open and trips into the water.{/i}"

                CAT "What was that?"

                ELI "Was it a racoon?"

                ANA "A trash panda?"

                RUT "It's probably a ghost or something."

                ALI "I'll check it out."

                "{i}Asuka swims over to find...{/i}"

                ALI "Nothing..."
                ALI "I don't see anything around here."
                ALI "It must've been a bird or something."

                RUT "Stupid ass Asuka-chan."
                RUT "If it's a ghost, you wouldn't be able to see it in the first place."

                CAT "Since when were you so rude, Rumi-chan?"

                RUT "Are you stupid?"
                RUT "I've always talked like this."

                "{i}TSB grabs Asuka by the hair and yanks her down into the water.{/i}"

                ALI "Ack!"

                ELI "What happened to her?"

                ANA "She must've died."

                RUT "See?"
                RUT "I told y'all it was a ghost."

                CAT "We gotta help her!"

                "{i}Meanwhile...{/i}"

                TEI "What's going on?"
                TEI "I can't see anything back here."

                THO "Akane's boobies are huge."

                MH "Who cares?"
                MH "Where'd Asuka-chan go?"

                TBI "I think she went scuba diving."

                MH "Huh?"

                "{i}The girls swim over and see the guys hiding.{/i}"

                RUT "Ewwwwwwwww, what are these nerds doing here?"
                RUT "Why couldn't it be Bro or The Riot?"

                CAT "They're peeping on us! Someone call the teachers!"

                MH "Wait a minute, this is all just a misunder–"

                TBI "Make a run for it!"

                "{i}Tanaka, Bii, Ei, and Minato bolt out of the hot spring, still completely naked.{/i}"

                ANA "I can't believe they've done this..."

                ELI "What happened to Asuka-chan?"

                RUT "It's too late for her."
                RUT "We need to go after them!"
                RUT "They might've taken mental sneak photography!"

                CAT "Huh?"

                "{i}Rumi rushes after the guys."
                "{i}Absolutely naked.{/i}"

                ELI "What a slut."
                ELI "She could've at least grabbed her towel."

                "{i}The guys split up while running away."
                "{i}Minato sees an open door and hides inside the room.{/i}"

                MH "Thank god that's over."

                "{i}Friday.{/i}"

                AH "On today's schedule, we're given free time since it's the last day of our trip."
                AH "So, whaddya wanna do?"

                MH "What is there to do in Aokigahara?"

                KH "Besides killing yourself, absolutely nothing."

                THO "What are you saying?"
                THO "There's plenty of things we can do."

                TEI "Yeah yeah yeah yeah."

                TBI "Wanna climb Fuji-san?"

                XC "You're a dumbass."

                AH "No, that's actually a good idea."
                AH "We can go on a hike and invite all the other guys."

                MH "What about the girls?"

                TET "Apparently they're cotting the boys, a boycott you could say."

                AH "It had something to do with what happened last night at the hot spring of the hotel."
                AH "There were some peepers peeping."
                AH "The teachers and the hotel staff are taking measures to find the culprits."
                AH "You guys wouldn't know anything about that would ya'?"

                TEI "Yeah yeah yeah yeah?"

                "{i}Tanaka, Minato, Twins Ei and Bii look at each other tentatively.{/i}"

                MH "Nope, never heard of it."

                XC "Why would we invite anybody else?"
                XC "We can just go by ourselves."

                AH "I want to strengthen the relationships between all of the third years."
                AH "We should get as many people as we can."

                KH "Sounds gay."

                TET "No, that's Kiyotaka-kun."
                TET "And you're right, we NEED to get some girls."

                MH "I'm not going unless Asuka-chan does too."

                TEI "Yeah yeah yeah yeah."

                XC "You guys are ridiculous."

                AH "Fine, I'll ask them if they can tag along, but no promises."

                "{i}Akiyuki leaves for the girls' rooms.{/i}"

                TBI "Since Akiyuki-kun mentioned it, what if we just played in our rooms."

                KH "What happened to hiking?"

                TBI "I'm over it."
                TBI "Let's do some party games instead."

                XC "Like what?"

                TET "Let's do the king's game."

                "TL Note: The king's game is a game."
                "{i}The king is chosen by random with labeled chopsticks pulled out by the group."
                "{i}The king gets to order any of the numbered players whatever he wants, but no one knows who has what number.{/i}"

                MH "Oh yeah, that's good."
                MH "If I become King, then I can make Asuka-chan do whatever I want..."

                TEI "Yeah yeah yeah yeah."

                "{i}The Riot, Bro, and Atsushi enter the room through the wide open door.{/i}"

                TRT "Did somebody say king?"
                TRT "Can't have a king game without a REAL king."

                BRO "I beg to differ."
                BRO "Didn't I beat you in a race to become captain of the track team?"

                TRT "That was last year."
                TRT "I'm the captain again."

                BRO "That's only because my hands are full with the student council."

                TRT "That's right..."
                TRT "You couldn't become president, so you had to settle being the vice-president."

                KH "Why are you guys even here?"
                KH "This isn't a field, this is a hotel room."

                MH "If The Riot and Bro are here, then Asuka-chan will have to come."
                MH "{i}Then I will come too.{/i}"

                "{i}Akiyuki walks into the room with Akane, Eriko, Chizuru, Rumi and Dabura.{/i}"

                AH "I brought some guests."

                CAT "President Akiyuki said that y'all want to hike up Fuji-san?"

                TRT "What?"
                TRT "I thought we were doing the king game."

                AH "Huh?"

                TBI "Yeah, I changed everyone's mind."

                TEI "Yeah yeah yeah yeah."

                RUT "King game?"
                RUT "That sounds way better than hiking anyway."
                RUT "This is my chance to finally have alone time with The Riot and Bro."

                AH "Guess we're doing the King game then."
                AH "Does anybody have chopsticks?"

                KH "I have thirty of them in my bag."

                AH "Why?"

                KH "They're already labeled too. I also have the cup."

                XC "This man collet's the utensils that you'd get from eating takeout."

                TET "Let's get this sho–"

                MH "Wait, where's Asuka-chan?"

                RUT "She's sick."

                "{i}Minato gasps and faints."
                "{i}The rest of them get ready to play the king game."
                "{i}They each pull a chopstick out of the cup in the center."
                "{i}The first king is Rumi.{/i}"

                RUT "Ermahgerd, YES!"
                RUT "I win!"

                THO "That's not how the game works..."

                RUT "I know that!"
                RUT "Number 7 and 12, I want you to lick my ass."

                AH "Huh?"

                RUT "Sorry, I meant give me a hug."

                "{i}Tanaka and Eriko raise their sticks at the same time.{/i}"

                THO "If I gotta, I guess I gotta..."

                RUT "(disgusted face) Ewwwwww, I don't want to do it with you guys."
                RUT "I wanna pass."

                ANA "I don't think you can do that..."

                RUT "I SAID I'LL PASS."

                "{i}They set up the next round."
                "{i}Minato wakes up and joins them."
                "{i}The king is...{/i}"

                MH "(sigh) I guess I'm the king..."

                XC "Say your orders already."

                MH "(sigh) Fine..."
                MH "There's no point if Asuka-chan isn't here anyway."
                MH "Numbers 6 and 9, go fuck yourselves."

                TRT "Who the fuck invited Debbie Downer over here?"

                MH "Fine."
                MH "Numbers 6 and 9 scream at the top of your lungs about how much you love Minato."

                AH "I LOVE MINATO!"

                TET "LISTEN TO MY BEATS ON MODIFYE, AND I GUESS I LOVE MINATO-KUN TOO OR SOMETHING."

                XC "This is a clown show."

                KH "Tell me about it."

                "{i}They reset the game."
                "{i}The new king...{/i}"

                TRT "ALRIGHT!"
                TRT "The king is finally the REAL king."
                TRT "I want numbers 11 and 16 to give me a kiss."

                "{i}Ei and Bii raise their hands.{/i}"

                TRT "Uh..."
                TRT "I changed my mind."
                TRT "I'll pass."

                TEI "No no no no."

                TBI "Exactly."
                TBI "That's not how the game works."
                TBI "We have to do what the king says."

                TRT "But Rumi-chan skipped her turn."

                BRO "That was an exception, not the rule."

                TBI "Get over here lover boy, let us give you phat one right on the lips."

                TRT "AAAAAAAAAAAAAAHHHHHHHHHHH!"

                "{i}The next king is...{/i}"

                ANA "Oh, I'm the king."

                CAT "Finally, somebody sensible."

                ANA "Number 8, tell us your biggest secret."

                DAB "My secret is last night, Minato-kun and I had sex."

                AH "Woah woah woah, what's this about?"

                MH "What?"
                MH "That never happened."

                DAB "I know you remember."
                DAB "How do you explain all the hickeys on your back?"

                KH "Isn't that just his back bubbles?"

                MH "No, it's acne on the back."
                MH "She's delusional."
                MH "I went into her room last night, but nothing else."

                "{i}Everyone in the room gasps after hearing about this new development.{/i}"

                TBI "Oh, so that's where you went."
                TBI "I was wondering why you didn't come back last night into this room of ours."

                RUT "I can't believe Minato-kun lost his virginity before me."

                CAT "And I thought he would be a wizard."

                MH "We didn't have sex."
                MH "Nobody's genitals went inside anybody else's."

                DAB "I gave you a blowjob."

                MH "With that much teeth?"
                MH "I would've been better off with a pencil sharpener."

                XC "So you did have sex."

                MH "I DID NOOOOOT."

                KH "Enough about Minato's sex life, let's continue the game now."

                MH "You sonuvabitch."

                "{i}The next king.{/i}"

                KH "I'm the king."

                XC "What are you, Kuro Hyou?"

                KH "Numbers 5 through 11, do a human centipede."

                "{i}Tanaka, Bii, Akane, Chizuru, Akiyuki, Mishima, and Bro stand up and get in a line.{/i}"

                KH "Stick your faces in their taint, it has to be believable."

                RUT "What's wrong with you?"

                KH "What do you mean?"

                BRO "Who votes for a coup d'etat?"

                TET "I'll do it if I get to be behind Akane-chan or Chizuru-chan."

                XC "This is a clown show."

                KH "Tell me about it."

                XC "You're the ringmaster of this circus, stupidass."

                "{i}They decide to end the game.{/i}"

                XC "Thank god that's finally over."

                ABD "Wait a minute, I didn't even get a single line."
                ABD "Let's do something else."

                AH "Like what?"

                ABD "Let's go to the forest and have a test of courage."

                ANA "Isn't that insensitive?"

                KH "Insensitive to who?"
                KH "They're all already dead."

                XC "Facts."

                TEI "Yeah yeah yeah yeah."

                AH "I guess we can do that."

                ANA "I don't want any part of this."
                ANA "Right girls?"

                ELI "Yeah yeah yeah–"

                CAT "Yeah, it's not nice."

                RUT "I'd rather just go to sleep."

                XC "Fine, leave then."
                XC "Buncha pussies."

                "{i}All the girls leave the room.{/i}"

                MH "I think I'm gonna sit this one out too."

                TRT "Nah man, you gotta come with us."

                MH "Huh?"
                MH "Why do you want me to be there?"
                MH "I thought you hated me again."

                TRT "That was before I knew you weren't a virgin."

                MH "I am a virgin."

                TRT "Potato, potato."
                TRT "Anyway, we're cool now."

                AH "So how are we gonna do this?"
                AH "We're just gonna raid the forest?"

                ABD "We'll split into pairs and each go in one at a time."

                "{i}The group went outside and gathered around the entrance to the forest.{/i}"

                ABD "So, we're here, right? And we've all talked about what we need to talk about. You know what you're doing. We know what we're doing. So we'll meet again tomorrow and we'll see where we go from there, okay? Sounds good."

                "{i}Akiyuki and Bro are the first to proceed through the forest.{/i}"
                "{i}They walk for a few meters in awkward silence.{/i}"

                AH "..."

                BRO "..."

                AH "..."

                BRO "..."

                AH "..."

                BRO "..."

                AH "..."

                BRO "..."

                AH "..."

                BRO "..."

                AH "..."

                BRO "..."

                AH "..."

                BRO "..."

                AH "..."

                AH "So, how about them baseball?"

                BRO "Huh?"
                BRO "I'm on the track team."

                AH "Yeah, I know..."
                AH "So, how about them baseball?"

                BRO "You don't have to force yourself."
                BRO "We can just get through this without talking."

                AH "I think we should at least iron out the wrinkles between us."

                BRO "There's no need."
                BRO "You won and I lost."
                BRO "There's nothing left to say."

                AH "I know that you didn't really believe all that nonsense about track."
                AH "Fuka-sensei put you up to it, right?"

                BRO "I don't know what you're talking about?"

                AH "C'mon now."
                AH "We both know that it's true."
                AH "What are you afraid of?"
                AH "Fuka-sensei is in a comatose state."

                BRO "I... I... I..."

                AH "It's just you and me."
                AH "Search your feelings, you know it to be true."

                BRO "You're right."
                BRO "I was Fuka-sensei's puppet the whole time."
                BRO "Her hand was so far up my ass I couldn't even tell."

                AH "It's okay man. I won, so everything's good."
                AH "And Fuka-sensei is basically dead, so there's nothing to worry about."
                AH "All's well that ends well."

                BRO "Huh?"
                BRO "How–"

                AH "Oh look, we made it back to the hotel."

                "{i}Saturday.{/i}"

                ABD "See guys?"
                ABD "Wasn't that a great idea?"
                ABD "You should be thanking me."

                XC "You're a dumbass."

                AH "C'mon guys."
                AH "We should hurry."

                BRO "Yeah everyone, listen to President Akiyuki."

                MH "I see that Asuka-chan seems better now."

                TBI "I wonder what happened to her?"

                TEI "Yeah yeah yeah yeah?"

                THO "Whaddaya mean, we were there when it happened?"

                TBI "Whaddaya mean what do I mean? Wink, wink."

                TET "Whatever happened to TSB?"
                TET "I haven't seen him since the beginning of the trip."
                TET "And he's not here either."

                KH "He's probably dead."

        label Syschord_epilogue:

            scene discord with Dissolve (1.0)

            MH "What actually happened to TSBB?"

            KH "Like I said, he's probably dead."

            AH "You know, it was really unclear."
            AH "The story seems kinda rushed."
            AH "It was almost as if the writers gave up."

            KH "Maybe."
            KH "It seems like they planned to finish within a week but instead it took them six months."

            MH "What are you guys even talking about?"

            AK "You wouldn't get it."

            MH "What were we talking about in the first place?"

            AH "I think we were talking about whether we would join tomorrow's Soom class."

            KH "It's today now."

            MH "Huh?"
            MH "We were talking for that long?"

            KH "Yeah, the Soom starts in two hours."

            AH "I'm going to sleep now."
            AH "You guys can join if you want."

            KH "Nah, I'm sleeping too."

            MH "What's wrong with you guys?"
            MH "You can't skip class."

            "{i}Akiyuki and Keisuke leave the call.{/i}"

            MH "Fine, I'll do it myself."

            "{i}Minato joins the Soom by himself.{/i}"

        return
    # This ends the game.

    return
