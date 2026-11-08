# ==========================================
# 1. CONFIGURATION
# ==========================================

config = {
    "stock": {
        # Add one or multiple stock symbols to process
        "symbols":['AAPL', 'NVDA', 'MSFT', 'GOOGL', 'GOOG', 'AMZN', 'SPCX', 'TSLA', 'META', 'AVGO', 'CSCO', 'AMAT', 'LRCX', 'CRWD', 'NFLX', 'AMGN', 'GILD', 'KLAC', 'QCOM', 'MRVL', 'ISRG', 'VRTX', 'SBUX', 'CME', 'EQIX', 'FTNT', 'ABNB', 'ADBE','REGN', 'INTU', 'SNPS', 'MRNA', 'CTAS', 'DDOG', 'HOOD', 'APP', 'ROST', 'ORLY', 'NTRA', 'FAST', 'MPWR', 'FANG', 'MSTR', 'EBAY', 'ROP', 'ALAB', 'IDXX','BTSGU', 'MDLN', 'MCHP', 'RVMD', 'PAYX', 'NTAP', 'ZS', 'RPRX', 'OKTA', 'ODFL', 'STLD', 'ILMN', 'TTWO', 'IBKR', 'AXON', 'RKLB', 'DXCM', 'CRWV', 'CTSH', 'TW', 'MDB', 'CRDO', 'CPRT', 'ZM', 'VRSN', 'ULTA', 'FISV', 'CBRS', 'UTHR', 'VRSK', 'CASY', 'DLTR', 'AFRM', 'GH', 'PFG', 'ENTG', 'GFS', 'ROKU', 'SYM', 'TROW', 'ALNY', 'LPLA', 'ARXS', 'SMCI', 'SBAC', 'CDW', 'FFIV', 'SSNC', 'FSLR', 'PAA', 'NTNX', 'MEDP', 'MTSI', 'RIVN', 'TSCO', 'TPG', 'VNOM', 'ZBRA','EXEL', 'WMG', 'LAMR', 'ASTS', 'DOCU', 'TRMB', 'NBIX', 'BBIO', 'CHRW', 'MANH', 'CG', 'COKE', 'ARCC', 'MKSI', 'REG', 'LOGI', 'SITM', 'CART', 'AKAM', 'FIVE', 'BTSG', 'TEM', 'SMMT', 'BSY', 'SEIC', 'CSGP', 'NXT', 'SAIL', 'TXRH','FROG', 'BMRN', 'JKHY', 'AGNC', 'KYMR', 'GSAT', 'ALGN', 'VSAT', 'ENSG', 'CHYM', 'PODD', 'DKNG', 'DPZ', 'TWST', 'SYRE', 'RGEN', 'MDGL', 'NTSK', 'TTEK', 'KRYS', 'AMKR', 'PCVX', 'CAI', 'HSIC', 'CGNX', 'PTGX', 'TXG', 'RMBS', 'GTLB', 'QNT', 'PCTY', 'AEIS', 'SANM', 'AUR', 'IBRX', 'CORT', 'CYTK', 'TTMI', 'COLB', 'HQY', 'MORN', 'LINE', 'DBX', 'TTAN', 'PRAX', 'FCFS', 'URBN', 'QLYS', 'WYNN', 'AXSM', 'APPF', 'SLAB', 'POOL', 'KNSA', 'SFD', 'ZG', 'CROX', 'FORM', 'VCTR', 'NAVN', 'CVLT', 'LNTH', 'ACT', 'AVAV', 'RYTM', 'EXLS', 'KOD', 'BLTE', 'DUOL', 'MXL', 'LYFT', 'IMVT', 'CWST', 'AAOI', 'MKTX', 'TTD', 'CGON', 'ALGM', 'VRNS', 'CAKE', 'TENB', 'PEGA', 'PI', 'MIRM', 'CRUS', 'APLD', 'COGT', 'WAY', 'XMTR', 'OLLI', 'BLLN', 'SRRK', 'NXST', 'STEP', 'BRZE', 'SHC','RRR', 'ROAD', 'MMED', 'HTFL', 'LFST', 'EBC', 'RELY', 'PTEN', 'NSIT', 'ERAS', 'PTCT', 'PECO', 'REYN', 'LSTR', 'MRCY', 'CACC', 'MWH', 'LKQ', 'SYNA', 'HLNE', 'DNTH', 'TFSL', 'CDNA', 'SFM', 'CHEF', 'UFPI', 'LAUR', 'BWIN', 'XE','MYRG', 'CLMT', 'EQPT', 'ADPT', 'EWTX', 'LEGN', 'ITRI', 'LGN', 'ICUI', 'IRTC', 'WING', 'LQDA', 'ARQT', 'RLAY', 'VCYT', 'LOPE', 'FRSH', 'TNGX', 'PLSE', 'FA', 'BANF', 'PLMR', 'TARS', 'ASO', 'LIF', 'AMLX', 'AVPT', 'AXTI', 'USAR', 'FIBK', 'ACAD', 'APPN', 'VKTX', 'COLM', 'PBLS', 'ARLP', 'ACCV', 'ENPH', 'CELC', 'COCO', 'CENX', 'WSC', 'CIFR', 'GBDC', 'SLDE', 'FRPT', 'ELVN', 'INTA', 'MCHB', 'NMIH', 'SKYW', 'ALRM', 'SHOO', 'ACMR', 'OSIS', 'PENG', 'DYN', 'ATRC', 'CSQ', 'HURN', 'ACLS', 'IPGP', 'IDYA', 'FHB', 'SGRY', 'DNLI', 'FLY', 'CLBK', 'CALM', 'EXTR', 'WDFC', 'PTRN', 'SPSC', 'NRIX', 'DRH', 'MGRC', 'AVAH', 'CARG', 'CENT', 'ASST', 'LIFE', 'BEAM', 'VRDN', 'NTCT', 'AMBA', 'DGII', 'PRVA', 'PRCH', 'FIVN', 'MBX', 'RUM', 'FBNC', 'SKWD', 'NEOG', 'LFTO', 'VERX', 'LIND', 'POWI', 'LUNR', 'SUPN', 'FRVO', 'PLUS', 'BLKB', 'RXRX', 'NCNO', 'FLYW', 'MBIN', 'UCTT', 'VECO', 'ADEA', 'EEFT', 'ADUS', 'TMDX', 'PTON', 'HRMY', 'UPST', 'PGNY', 'VERA', 'NWBI', 'XNCR', 'UFPT', 'BCRX', 'IMNM', 'LASR', 'PENN', 'ALMR', 'NMRK', 'GCT', 'WGS', 'SEPN', 'DRVN', 'SDGR', 'MRVI', 'NEXT', 'MCRI', 'BL', 'XERS', 'ALGT', 'BRVE', 'COAG', 'VIR', 'TRVI', 'SONO', 'ABSI', 'PLUG', 'TBBK', 'XRAY', 'MQ', 'GENB', 'LMAT', 'ZBIO', 'PRGS', 'AGIO', 'ADRX', 'RUN', 'AEHR', 'ATEX', 'RBCAA', 'KMTS', 'ARHS', 'BLBD', 'MAZE', 'NTLA', 'PDFS', 'EZPW', 'ICFI', 'STOK', 'GSHD', 'PSNL', 'CERT', 'FRMI', 'OMCL', 'REPL', 'KLRA', 'WERN', 'HCSG', 'HUBG', 'PLAB', 'STRA', 'EVCM', 'MLYS', 'WLTH', 'IMKTA', 'JJSF', 'RARE', 'PAHC', 'CBRL', 'YSWY', 'CASH', 'GPCR', 'DJT', 'INVA', 'BAND', 'OCUL', 'HYMC', 'SAFT', 'ALHC', 'HLMN', 'LIME', 'ESQ', 'VISN', 'INOD', 'AMAL', 'REAL', 'ETON', 'ULCC', 'TWFG', 'ICHR', 'PCRX', 'TYRA', 'PWP', 'ANAB', 'ATLC', 'LQDT', 'LYCA', 'TRS', 'CRSR', 'TH', 'TSHA', 'OMER', 'TNDM', 'HBT', 'ALKT', 'KARD', 'EYE', 'AMSC', 'GIII', 'GO', 'LBRX', 'CRCT', 'GTM', 'INNV', 'CRAI', 'SNDX', 'SHLS', 'WBTN', 'RAPP', 'GDRX', 'ROCK', 'VSTM', 'AMPH', 'VOR', 'LZ', 'OMDA', 'UPWK', 'AVLN', 'CSTL', 'JCAP', 'MNKD', 'WLDN', 'BVS', 'OXLC', 'RPD', 'HLIT', 'FSBC', 'PRCT', 'LMRI', 'ATEC', 'GDYN', 'SGP', 'KRT', 'JBLU', 'JANX', 'FLNC', 'SPTX', 'CTY', 'MBWM', 'MCBS', 'LGIH', 'HSTM', 'CBLL', 'AVO', 'MLTX', 'QNST', 'IRMD', 'OIG', 'NBBK', 'CGEM', 'RIGL', 'ORIC', 'MRTN', 'SIBN', 'WLFC', 'NWPX', 'ODTX', 'DGICB', 'SBGI', 'LTGO', 'AIP', 'FRBT', 'GLUE', 'DJTWW', 'MGTX', 'BBNX', 'DAKT', 'BLMN', 'RJET', 'ASTE', 'JBIO', 'ACDC', 'AKTS', 'KPLT', 'GSBC', 'ALMS', 'NXDR', 'SWIM', 'PSEC', 'PRME', 'MFIC', 'DSP', 'EVLV', 'CRVS', 'HMH', 'SPFI', 'EVER', 'ALRS', 'PACB', 'KIDS', 'ROOT', 'CTKB', 'AHCO', 'BMBL', 'HTLD', 'BBSI', 'FWRG', 'FISI', 'COLL', 'SANA', 'ANNX', 'BBTX', 'WRLD', 'TASK', 'ARDX', 'WOOF', 'LYTS', 'BWMN', 'OABI', 'APEI', 'CGBD', 'ITG', 'CDNL', 'PRAA', 'AVBP', 'FDUS', 'SPT', 'PUBM', 'SCHL', 'NRDS', 'ELMT', 'KOPN', 'SGMT', 'LEGH', 'ATTO', 'ENVX', 'APMD', 'MSBI', 'RRBI', 'CBNK', 'FOXF', 'DSGN', 'RXT', 'STLN', 'SLDB', 'CCB', 'FDMT', 'LINC', 'TBLD', 'SABR', 'PRTH', 'GRPN', 'CADL', 'AURA', 'IMMX', 'IAM', 'SLRC', 'JBSS', 'RSVR', 'NNE', 'AVR', 'NTGR', 'OLMA','PZZA', 'MYGN', 'TRON', 'BCAX', 'GAIN', 'NVCT', 'MATW', 'ULH', 'KRNY', 'SSYS', 'CLYM', 'ACRS', 'IRWD', 'GERN', 'DNUT', 'BWFG', 'LPTH', 'FLGT', 'BWB','TITN', 'BSVN', 'STTK', 'GOOD', 'PDLB', 'SBC', 'ADTN', 'NANO', 'ARRY', 'TCMD', 'PANL', 'BRCB', 'MCFT', 'BBCP', 'ARVN', 'SGHT', 'CTMX', 'ETRA', 'GYRE', 'ANGO', 'CBIO', 'DMAC', 'OVID', 'MPLT', 'AQST', 'FRBA', 'EOLS', 'ABTC', 'FTH', 'FAC', 'HBCP', 'RGNX', 'MNPR', 'BLZE', 'WYFI', 'MBUU', 'PHAT', 'LOCO', 'MASS', 'IIIV', 'RMNI', 'CERS', 'ILPT', 'OPRT', 'TKNO', 'CBK', 'METC', 'PBFS', 'HNST', 'SLDP', 'BLSM', 'ASPE', 'RBB', 'CMCO', 'GLAD', 'VRRM', 'KRUS', 'NPCE', 'RUMBW', 'CCCC', 'RPAY', 'SUJA', 'PCB', 'EDIT', 'ASMB', 'CARL', 'ALLO', 'TLS', 'CTRN', 'HCMA', 'ALTI', 'NECB', 'VALU', 'SRTA', 'FOSL', 'PROK', 'ADV', 'AMSF', 'TECX', 'AVTX', 'TACO', 'GFUZ', 'ISTR', 'TRXB', 'GEMI', 'MNRO', 'TLRY', 'VITL', 'PTLO', 'RCKY', 'NNBR', 'USCB', 'FRST', 'CV', 'JAKK', 'SFIX', 'IRLA', 'FNKO', 'ERII', 'OBIO', 'CTNM', 'MOBI', 'WSBF', 'TCPC', 'KYTX', 'NAUT', 'CUB', 'FSBW', 'IMSR', 'SPRY', 'BCML', 'XFOR', 'MRAM', 'AVIR', 'ALEC', 'TMS', 'GOGO', 'LAND', 'QSI', 'CLNE', 'MNTK', 'ENTA', 'ASPI', 'PRLD', 'PPHC', 'GEVO', 'AGEN', 'NODK', 'BNTC', 'SABS', 'MYFW', 'VOGX', 'RELL', 'SCTX', 'BTBT', 'TMCI', 'EIKN', 'PUSA', 'FULC', 'LTRX', 'IMXI', 'RWAY', 'TDUP', 'HRZN', 'PLAY', 'CMRC', 'BCBP', 'LYEL', 'BIOA', 'GLOO', 'RCKT', 'OPAL', 'FBLA', 'IPSC', 'RMBI', 'QTTB', 'MTRX', 'ULBI', 'LXEO', 'LRMR', 'CABA', 'GLSI', 'OPTX', 'FATE', 'CAMP', 'CPZ', 'BDSX', 'IMRX', 'LAB', 'IMMR', 'OCGN', 'SVIA', 'LOVE', 'ZUMZ', 'GWRS', 'ASLE', 'VNDA', 'TLSI', 'REFI', 'CZWI', 'OPBK', 'ELDN', 'MRBK', 'CPSS', 'KLTR', 'MVST', 'KROS', 'RICK', 'PYXS', 'IKT', 'EXFY', 'RR', 'KRRO', 'MOVE', 'BBOT', 'FORR', 'LIEN', 'XGN', 'SVCO', 'SND', 'ARTV', 'RXST', 'RBKB', 'ATER', 'RNAC', 'AKBA', 'DTIL', 'LCUT', 'GPRO', 'AIRJ', 'ZSQR', 'VRA', 'APC', 'UPB', 'ECBK', 'ZNTL', 'BVFL', 'YARW', 'FLWS', 'CHCI', 'FINW', 'INGN', 'PAAC', 'TRDA', 'SION', 'RRGB', 'IVVD', 'STIM', 'ANTX', 'EBMT', 'NXH', 'DLTH', 'DIBS', 'HNVR', 'MXCT', 'PEPG', 'AIRO', 'DH', 'ONEW', 'QUIK', 'BRLT', 'SWMR', 'FISN', 'NSLR', 'AUC', 'CNTN', 'CURI','TUSK', 'MGNX', 'ALXO', 'HYNE', 'GSIT', 'CUE', 'NCMI', 'PDSB', 'STRO', 'EGAN', 'SRBK', 'HUCK', 'LSBK', 'TARA', 'DERM', 'MGYR', 'PLBY', 'QTRX', 'RAIL', 'ONEN', 'KVHI', 'SOUNW', 'SPRB', 'AMRO', 'SAMG', 'ATOM', 'CDXS', 'LUNG', 'OSS', 'SKYA', 'CVGI', 'CHRS', 'HCAT', 'AIRS', 'WSBK', 'FHTX', 'BYND', 'BSBK', 'HUMA', 'OTLK', 'NKTX', 'NERV', 'SIDU', 'SSTI', 'DFDV', 'SKYX', 'NAKA','EQ', 'OKUR', 'VYGR', 'UNCY', 'SHIM', 'IMUX', 'ILLU', 'BDTX', 'PARK', 'VTVT', 'JYNT', 'OXSQ', 'PMVP', 'ORGO', 'CBUS', 'VANI', 'NRXP', 'FNWB', 'RDZN','LENZ', 'MRLN', 'GNLX', 'INSE', 'ICCC', 'SEER', 'TVGN', 'FDSB', 'RENT', 'NDLS', 'RTSN', 'LAKE', 'CPBI', 'COYA', 'OESX', 'TNYA', 'RLYB', 'ETS', 'LUCD', 'RANI', 'BZFD', 'HFFG', 'SERA', 'ATRA', 'NFE', 'HOVR', 'EMPD', 'FACWW', 'VERI', 'TTEC', 'CSPI', 'ISPR', 'MMLP', 'SSBI', 'HYPR', 'OM', 'JRSH', 'BLUW', 'CCLD', 'RGS', 'BCIC', 'PAL', 'USGO', 'CING', 'FATN', 'AISP', 'GFUZW', 'ACRV', 'CPIX', 'CLST', 'HFBL', 'NMRA', 'TELO', 'DVLT', 'AFCG', 'BXBL', 'ECOR', 'TYGO', 'ROC', 'LNZA', 'UPXI', 'IMSRW', 'CGTX', 'SPAI', 'SKIN', 'MCHX', 'GOSS', 'UEIC', 'GRML', 'SPRO', 'RNXT', 'OABIW', 'RNTX', 'VRCA', 'XBIT', 'BOLD', 'OPTXW', 'DTI', 'TACT', 'TMSWW', 'PRTS', 'HOUR', 'AIRG', 'MYPS', 'INKT', 'TLPH', 'PLRX', 'XLO', 'ESYN', 'GENK', 'CTOR', 'COCH', 'SCOR', 'WATT', 'HYPD', 'AMCI', 'TCBS', 'GANX', 'MDAI', 'LASE', 'KLRS', 'IDN', 'HOWL', 'HDRN', 'LONA', 'IMA', 'BMEA', 'NXXT', 'LIDR', 'TIL', 'FRMM', 'ELTX', 'SRTS', 'CRBU', 'VGAS', 'INMB', 'SBCWW', 'DWTX', 'IPWR', 'KFFB', 'MNTS', 'AIRJW', 'SPWH', 'MVIS', 'HBIO', 'XTIA', 'MAMO', 'XOS', 'EXOZ', 'HIT', 'CVRX', 'SCYX','XBP', 'MWYN', 'ELUT', 'RPID', 'GAIA', 'MIND', 'TELA', 'STI', 'RYM', 'GRDX', 'RMCO', 'CIRC', 'LITS', 'ALDX', 'BOF', 'SVIAW', 'LVLU', 'ATHR', 'ACET', 'MLGO', 'BNAI', 'BEAT', 'PXLW', 'AERT', 'ALGS', 'AARD', 'MGX', 'FLD', 'HCMAW', 'PIII', 'ELWT', 'NXTC', 'JVA', 'TEAD', 'RMTI', 'BZAI', 'ESLA', 'RNAZ', 'AIFA', 'BYSI', 'PRHI', 'CELU', 'HOLO', 'FTCI', 'SHPH', 'DAIO', 'DCGO', 'SWAG', 'KTCC', 'MIRA', 'BIRD', 'FFR', 'FGC', 'SMXT', 'SDOT', 'ATOS', 'SNAL', 'MSGM', 'AEI', 'SKYQ', 'AWRE', 'MDRR', 'KYNB', 'ACTU', 'EXYN', 'OCCI', 'MCRB', 'CNTX', 'JSPR', 'ARAY', 'NEUP', 'ZEO', 'AISPW', 'HOVRW', 'BNGO', 'HSCS', 'EHTH', 'CLIR', 'SCLX', 'PAVM', 'FGI', 'LHAI', 'ABOS', 'KPTI', 'VEEA', 'SLE', 'MDAIW', 'QNME', 'DFNS', 'DARE', 'REBN', 'MOBX', 'PRPL', 'BBGI', 'BFRI', 'GUTS', 'SINT', 'BOLT', 'SMSI', 'JAGX', 'HIND', 'IRIX', 'ATYR', 'KTTA', 'RKTO', 'ICU', 'UPLD', 'FEMY', 'BTBD', 'ASBP', 'PASG', 'INTS', 'TCRX', 'KSCP', 'TVRD', 'AUROW', 'CDLX', 'ICMB', 'AZR', 'CALC', 'LTRN', 'XHLD', 'PLCE','MEDS', 'INHD', 'MDBH', 'BTLN', 'BFRG', 'INAB', 'BNKK', 'BLIN', 'MBRX', 'CURX', 'CYCU', 'MTVA', 'CNSP', 'LUCY', 'MSAI', 'NDRA', 'MYSE', 'EEIQ', 'SNTI', 'BTOC', 'FTHM', 'APRE', 'SNES', 'ALZN', 'INBS', 'ACXP', 'HDRNW', 'NWTG','ACON', 'TNON', 'RDZNW', 'VEEE', 'LGVN', 'CYN', 'GDC', 'SNOA', 'MGRX', 'PULM', 'FFAI', 'CDIO', 'GXAI', 'AQMS', 'NVNO', 'AUUD', 'HCTI', 'TRAW', 'SEGG', 'CWD', 'GRMLW', 'SONM', 'DRMA', 'VVOS', 'BIAF', 'AMST', 'XPON', 'HODO', 'QCLS', 'DFLI', 'AMIX', 'CVKD', 'CXAI', 'HYFM', 'GRI', 'ONCO', 'SXTP', 'YHC', 'CODX', 'KALA', 'EXYNW', 'CTNT', 'JTAI', 'FLYE', 'SGLY', 'FLDDW', 'POLA','JUNS', 'TGL', 'IPST', 'STLNW', 'DCOY', 'TRNR', 'BJDX', 'HCWB', 'CJMB', 'REVB', 'SLDPW', 'WORX', 'BFRGW', 'ELAB', 'ISPC', 'BOXL', 'NXL', 'GNPX', 'FRGT', 'KITT', 'ZEOWW', 'NXGL', 'PWCM', 'BLUWW', 'MOBXW', 'SHFS', 'WHLR', 'RMCOW', 'SGRX', 'EDBL', 'SKYAW', 'TVGNW', 'OLOX', 'UK', 'IPDN', 'VBIO', 'SQFT', 'ONFO', 'GNLN', 'TRUG', 'MSS', 'IPW', 'BEATW', 'DBGI', 'BZFDW', 'CDT', 'VGASW', 'LUCYW', 'RKDA', 'HSCSW', 'SCLXW', 'SHFSW', 'BIAFW', 'DFNSW', 'SRTM', 'COCHW', 'BTBDW', 'CYCUW', 'LNZAW', 'SXTPW', 'VEEAW', 'PIIIW', 'CXAIW', 'ACONW', 'ICUCW', 'SWAGW', 'EDBLW', 'DFLIW', 'ONFOW', 'CDIOW', 'ASBPW', 'KITTW', 'NXGLW', 'PARAW', 'SVIVW', 'SVIVU', 'TLNC', 'TLACU', 'TLNCU', 'SVIV', 'TDACU', 'TLNCW', 'CXII', 'CXIIU', 'CXIIW', 'SVCCW', 'CEPF', 'SVCC', 'SVAQU', 'SVAQ', 'DAAQ', 'DAAQW', 'CCXIW', 'CCXIU', 'CEPO', 'CEPV', 'SZZL', 'SZZLR', 'CRAN', 'CHI', 'CHPG', 'TBCV', 'CHPGR', 'TBCVU', 'TBCVW', 'CHPGU', 'TMTSU', 'TCGX', 'CHW', 'TDWD', 'CHY', 'TCXB', 'TDAC', 'TAVIR', 'CHAR', 'TAVI','CTAA', 'TLAC', 'TACH', 'CEPS', 'TDACW', 'CGCF', 'TACHW', 'THEO', 'CRANR','TACOW', 'CRAQR', 'CRAQ', 'CRANU', 'CGCFU', 'CGO', 'TMTS', 'OCLTW', 'CCXI', 'CCIIW', 'ALFUW', 'ALIS', 'ALISR', 'ALISU', 'ALOV', 'ALOVU', 'ALPX', 'ALPXU', 'AMAN', 'WLIIU', 'WLII', 'APAC', 'APMC', 'APMCR', 'WENN', 'APUR', 'APXT', 'APXTU', 'APXTW', 'ARCI', 'ARCIW', 'ARCL', 'ARCLU', 'ARTC', 'ATLQ', 'BACC', 'BACCR', 'XCBE', 'XCBEU', 'ALF', 'YICCU', 'AACOU', 'AACP', 'AACPR', 'AACPU', 'ZKPW', 'ZKPU', 'ZKP', 'AACPW', 'ACAA', 'ACAAU', 'ACAAW', 'ACGC', 'YICC', 'ALDFW', 'XTER', 'XSLLU', 'XSLL', 'ADAC', 'AESP', 'AESPR', 'AFJK', 'XIIIW', 'XIIIU', 'XIII', 'AFJKR', 'ALDF', 'VNMEW', 'VNME', 'VLOSW', 'CAII', 'TWLV', 'BRKHW', 'TVIVW', 'TVIVU', 'TVIV', 'BRTM', 'TVAIR', 'TVAI', 'TVACW', 'TVACU', 'TVA', 'CAES', 'CAPN', 'BRKH', 'CAPNU', 'CAQ', 'CAQUU', 'CATL', 'CATLR', 'CATLU', 'CCAQ', 'TRGSU', 'TRGS', 'CCAQU', 'CCCT', 'CCII', 'TWLVU', 'BREZR', 'VLOS', 'UYSCR', 'BCCQ', 'BCCQU', 'BCCQW', 'BDCI', 'VHCPW', 'VHCP', 'BEAG', 'BEAGR', 'BEAGU', 'BHAIU', 'BHAV', 'UYSCU', 'UYSC', 'BREZ', 'BHAVR', 'BID', 'BIXI', 'BIXIW', 'BKHA', 'BKHAR', 'BKHAU', 'BLRK', 'BLZR', 'BLZRU', 'BLZRW', 'BPAC', 'BRKHU', 'FDMMW', 'DBCA', 'DMAA', 'LATAU', 'LCCC', 'LEDRU', 'LFAC', 'LKSP', 'LKSPR', 'LKSPU', 'LPAA', 'LPAAU', 'LPBB', 'LPBBW','LPCV', 'LTGR', 'LTGRW', 'POLEW', 'POLE', 'PMTRW', 'PMTRU', 'PMTR', 'LWAC', 'LWACU', 'LWACW', 'MACI', 'PLMKW', 'PLMK', 'PLCIR', 'PLCI', 'MACIW', 'MBVI', 'LATA', 'PTAC', 'KRAQW', 'QSEA', 'ITHAW', 'JATT', 'JONE', 'RANGU', 'RANGR', 'RANG', 'RACD', 'RACC', 'QUMSU', 'QUMS', 'JTTT', 'KBON', 'QSEAR', 'KBONU', 'KRAQ', 'KCHV', 'KCHVR', 'KEYY', 'QADRU', 'QADR', 'KFII', 'KFIIR', 'KFIIU', 'KOYN', 'KOYNW', 'PTORU', 'PTOR', 'AACO', 'MCAH', 'MCAHU', 'MCGA', 'NPAC', 'MYXXU', 'NCO', 'OTGAW', 'OTGAU', 'OTGA', 'NHIV', 'OSPRU', 'OSPR', 'NHIVW', 'NMP', 'NMPAR', 'NOEM', 'NOEMU', 'NPACU', 'OYSE', 'NSAI', 'NSAIU', 'NSAIW', 'NTWO', 'ONCHW', 'ONCHU', 'ONCH', 'NTWOW', 'OACC', 'OCLT', 'OIMAU','OIM', 'OCLTU', 'MYX', 'OYSER', 'MCGAU', 'MKLY', 'PGACU', 'PGAC', 'MCGAW','MESH', 'MESHW', 'PECEW', 'PECEU', 'PECER', 'PECE', 'MEVO', 'MEVOU', 'MEVOW', 'MIAC', 'MKLYU', 'OYSEU', 'PCAPU', 'PCAP', 'MLAA', 'PAXGU', 'PAXG', 'MRCO', 'PALO', 'MTAK', 'PACHW', 'PACH', 'MUZE', 'PAACW', 'MUZEW', 'ITHA', 'ISNRW', 'ISNR', 'FMACR', 'OHAC', 'FGII', 'FGIIU', 'FIGX', 'FIGXU', 'SIMA', 'FJDI', 'FJDIR', 'FJDIU', 'SHOTU', 'SHOT', 'FLSC', 'FMAC', 'FMACU', 'FACTW', 'FSHP', 'FSHPR', 'FVAV', 'FWAC', 'FWACW', 'FXAC', 'GCGR', 'SDHIU', 'SDHI', 'GHXI', 'GHXIU', 'GIW', 'SCQCU', 'FDMM', 'FACT', 'GIWWU', 'SPEGU', 'SSEA', 'DMAAR', 'SSACU', 'SSAC', 'DMII', 'DMIIR', 'DNMX', 'DNMXU', 'DNMXW', 'DRDB', 'DRDBW', 'DTSQ', 'DYOR', 'SPEG', 'EWAVU', 'EGHA', 'EGHAR', 'SORN', 'SOCAU', 'SOCA', 'EMIS', 'EMISR', 'EURK', 'EURKR', 'EVOX', 'EVOXU', 'EVOXW', 'EWAV', 'SCPQ', 'GIX', 'RDAG', 'IEAG', 'HVMCW', 'IACO', 'IACOU', 'IACOW', 'IACQ', 'IACQW', 'IBAC', 'IBACR', 'RNGT', 'RNAQU', 'RNAQ', 'IDAC', 'IDACU', 'IGAC', 'HLXC', 'ILLUU', 'INAC', 'INACU', 'IPFX', 'IPFXU', 'IPHX', 'IPHXW', 'IPVV', 'IPXG', 'IPXGU', 'IRHO', 'IRHOR', 'RDAGW', 'HVMC', 'RREV', 'SCII', 'SAAQU', 'GIXXU', 'SCATW', 'SCATR', 'SCAT', 'GPAC', 'GPACU', 'GPAT', 'GPATW', 'GSHR', 'GSRF', 'GSRFR', 'GSRFU', 'SAAQW', 'SAAQ', 'RREVW', 'GSRV', 'GSRVR', 'GSRVU', 'GTEN', 'GTENW', 'GUAC', 'GUACW', 'HACQ', 'HCIC', 'RTACW', 'RTACU', 'RTAC', 'HCMAU', 'AACI'],
        "start_date": "2026-11-03",  # Download from Nov 3, 2026 onwards
        "append_to_existing": True,  # Set True to append to existing CSV, False to overwrite with only post-Nov 3 data
        "interval": "1d"
    },

    "data": {
        "window_size": 20,
        "train_split_size": 0.80,
        "base_dir": "data",
    },

    "plots": {
        "xticks_interval": 90,
        "dpi": 300,  # High-resolution output
        "color_actual": "#001f3f",
        "color_train": "#3D9970",
        "color_val": "#0074D9",
        "color_pred_train": "#3D9970",
        "color_pred_val": "#0074D9",
        "color_pred_test": "#FF4136",
    },

    "model": {
        "input_size": 1,
        "num_lstm_layers": 2,
        "lstm_size": 32,
        "dropout": 0.2,
    },

    "training": {
        "device": "cpu",
        "batch_size": 64,
        "num_epoch": 100,
        "learning_rate": 0.01,
        "scheduler_step_size": 40,
    }
}


# ==========================================
# 2. IMPORT LIBRARIES
# ==========================================
import os
import warnings
import numpy as np
import pandas as pd
import yfinance as yf

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from torch.utils.data import Dataset, DataLoader

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# Silence Pandas deprecation warnings from yfinance
warnings.filterwarnings("ignore", message=".*inplace keyword.*")

print("All libraries loaded")


# ==========================================
# 3. DOWNLOAD & UPDATE STOCK DATA + CHART
# ==========================================

def process_company_data(symbol, config):
    output_dir = os.path.join(config["data"]["base_dir"], symbol)
    csv_path = os.path.join(output_dir, f"{symbol}.csv")

    # Download data starting from 2026-11-03 onwards
    new_data = yf.download(
        symbol,
        start=config["stock"]["start_date"],
        interval=config["stock"]["interval"],
        auto_adjust=True,
        progress=False
    )

    if new_data.empty:
        raise ValueError(f"No new stock data downloaded for {symbol} since {config['stock']['start_date']}.")

    os.makedirs(output_dir, exist_ok=True)

    if isinstance(new_data.columns, pd.MultiIndex):
        new_data.columns = new_data.columns.get_level_values(0)

    new_data.index = pd.to_datetime(new_data.index).tz_localize(None)
    new_data = new_data.sort_index()

    # If appending to existing CSV downloaded up to Nov 3, 2026
    if config["stock"].get("append_to_existing", True) and os.path.exists(csv_path):
        existing_df = pd.read_csv(csv_path, index_col="Date", parse_dates=True)
        existing_df.index = pd.to_datetime(existing_df.index).tz_localize(None)

        # Combine old and new data, keeping the newest records for overlapping dates (like 2026-11-03)
        combined = pd.concat([existing_df[["Open", "High", "Low", "Close", "Volume"]], new_data[["Open", "High", "Low", "Close", "Volume"]]])
        combined = combined[~combined.index.duplicated(keep="last")].sort_index()
        data = combined
    else:
        data = new_data[["Open", "High", "Low", "Close", "Volume"]].copy()

    # Recalculate daily percentage returns cleanly across the seam
    data["Daily_Return"] = data["Close"].pct_change() * 100

    df = data[[
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "Daily_Return"
    ]].copy()

    df.index.name = "Date"

    # Save updated CSV as data/{symbol}/{symbol}.csv
    df.to_csv(csv_path)

    data_date = df.index.strftime("%Y-%m-%d").tolist()
    data_close_price = df["Close"].to_numpy(dtype=float)
    num_data_points = len(df)
    display_date_range = f"from {data_date[0]} to {data_date[-1]}"

    # Generate High-Quality Plot
    fig = figure(figsize=(25, 5), dpi=config["plots"]["dpi"])

    plt.plot(
        data_date,
        data_close_price,
        color=config["plots"]["color_actual"],
        linewidth=1.2
    )

    xticks = [
        data_date[i]
        if (
            (i % config["plots"]["xticks_interval"] == 0
             and (num_data_points - i) > config["plots"]["xticks_interval"])
            or i == num_data_points - 1
        )
        else ""
        for i in range(num_data_points)
    ]

    x = np.arange(len(xticks))
    plt.xticks(x, xticks, rotation="vertical")

    plt.title(f"Daily close price for {symbol}, {display_date_range}")
    plt.grid(True, axis="y", linestyle="--", alpha=0.7)
    plt.xlabel("Date")
    plt.ylabel("Adjusted closing price")
    plt.tight_layout()

    # Save high-resolution chart in data/{symbol}/{symbol}_chart.png
    plot_path = os.path.join(output_dir, f"{symbol}_chart.png")
    plt.savefig(plot_path, dpi=config["plots"]["dpi"], bbox_inches="tight")
    plt.close(fig)

    print(f"[{symbol}] Updated CSV: {csv_path}")
    print(f"[{symbol}] Updated Plot: {plot_path}")
    print(f"[{symbol}] Total data points: {num_data_points} ({display_date_range})\n")

    return data_date, data_close_price, num_data_points, display_date_range, df


# ==========================================
# 4. RUN FOR ALL SYMBOLS (WITH TRY-EXCEPT)
# ==========================================

results = {}
failed_symbols = []

for sym in config["stock"]["symbols"]:
    try:
        results[sym] = process_company_data(sym, config)
    except Exception as e:
        print(f"[{sym}] Skipped due to error: {e}\n")
        failed_symbols.append(sym)

print(f"Finished! Successfully updated: {len(results)} | Failed/Skipped: {len(failed_symbols)}")