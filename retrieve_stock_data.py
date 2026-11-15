# ==========================================
# 1. CONFIGURATION
# ==========================================

config = {
    "stock": {
        # Separate symbol lists mapped directly to the "nasdaq/" and "nyse/" folders
        "exchanges": {
            "nasdaq": [
                'AAPL', 'NVDA', 'MSFT', 'GOOGL', 'GOOG', 'AMZN', 'SPCX', 'TSLA', 'META', 'AVGO', 'CSCO', 'AMAT', 'LRCX', 'CRWD', 'NFLX', 'AMGN', 'GILD', 'KLAC', 'QCOM', 'MRVL', 'ISRG', 'VRTX', 'SBUX', 'CME', 'EQIX', 'FTNT', 'ABNB', 'ADBE','REGN', 'INTU', 'SNPS', 'MRNA', 'CTAS', 'DDOG', 'HOOD', 'APP', 'ROST', 'ORLY', 'NTRA', 'FAST', 'MPWR', 'FANG', 'MSTR', 'EBAY', 'ROP', 'ALAB', 'IDXX','BTSGU', 'MDLN', 'MCHP', 'RVMD', 'PAYX', 'NTAP', 'ZS', 'RPRX', 'OKTA', 'ODFL', 'STLD', 'ILMN', 'TTWO', 'IBKR', 'AXON', 'RKLB', 'DXCM', 'CRWV', 'CTSH', 'TW', 'MDB', 'CRDO', 'CPRT', 'ZM', 'VRSN', 'ULTA', 'FISV', 'CBRS', 'UTHR', 'VRSK', 'CASY', 'DLTR', 'AFRM', 'GH', 'PFG', 'ENTG', 'GFS', 'ROKU', 'SYM', 'TROW', 'ALNY', 'LPLA', 'ARXS', 'SMCI', 'SBAC', 'CDW', 'FFIV', 'SSNC', 'FSLR', 'PAA', 'NTNX', 'MEDP', 'MTSI', 'RIVN', 'TSCO', 'TPG', 'VNOM', 'ZBRA','EXEL', 'WMG', 'LAMR', 'ASTS', 'DOCU', 'TRMB', 'NBIX', 'BBIO', 'CHRW', 'MANH', 'CG', 'COKE', 'ARCC', 'MKSI', 'REG', 'LOGI', 'SITM', 'CART', 'AKAM', 'FIVE', 'BTSG', 'TEM', 'SMMT', 'BSY', 'SEIC', 'CSGP', 'NXT', 'SAIL', 'TXRH','FROG', 'BMRN', 'JKHY', 'AGNC', 'KYMR', 'GSAT', 'ALGN', 'VSAT', 'ENSG', 'CHYM', 'PODD', 'DKNG', 'DPZ', 'TWST', 'SYRE', 'RGEN', 'MDGL', 'NTSK', 'TTEK', 'KRYS', 'AMKR', 'PCVX', 'CAI', 'HSIC', 'CGNX', 'PTGX', 'TXG', 'RMBS', 'GTLB', 'QNT', 'PCTY', 'AEIS', 'SANM', 'AUR', 'IBRX', 'CORT', 'CYTK', 'TTMI', 'COLB', 'HQY', 'MORN', 'LINE', 'DBX', 'TTAN', 'PRAX', 'FCFS', 'URBN', 'QLYS', 'WYNN', 'AXSM', 'APPF', 'SLAB', 'POOL', 'KNSA', 'SFD', 'ZG', 'CROX', 'FORM', 'VCTR', 'NAVN', 'CVLT', 'LNTH', 'ACT', 'AVAV', 'RYTM', 'EXLS', 'KOD', 'BLTE', 'DUOL', 'MXL', 'LYFT', 'IMVT', 'CWST', 'AAOI', 'MKTX', 'TTD', 'CGON', 'ALGM', 'VRNS', 'CAKE', 'TENB', 'PEGA', 'PI', 'MIRM', 'CRUS', 'APLD', 'COGT', 'WAY', 'XMTR', 'OLLI', 'BLLN', 'SRRK', 'NXST', 'STEP', 'BRZE', 'SHC','RRR', 'ROAD', 'MMED', 'HTFL', 'LFST', 'EBC', 'RELY', 'PTEN', 'NSIT', 'ERAS', 'PTCT', 'PECO', 'REYN', 'LSTR', 'MRCY', 'CACC', 'MWH', 'LKQ', 'SYNA', 'HLNE', 'DNTH', 'TFSL', 'CDNA', 'SFM', 'CHEF', 'UFPI', 'LAUR', 'BWIN', 'XE','MYRG', 'CLMT', 'EQPT', 'ADPT', 'EWTX', 'LEGN', 'ITRI', 'LGN', 'ICUI', 'IRTC', 'WING', 'LQDA', 'ARQT', 'RLAY', 'VCYT', 'LOPE', 'FRSH', 'TNGX', 'PLSE', 'FA', 'BANF', 'PLMR', 'TARS', 'ASO', 'LIF', 'AMLX', 'AVPT', 'AXTI', 'USAR', 'FIBK', 'ACAD', 'APPN', 'VKTX', 'COLM', 'PBLS', 'ARLP', 'ACCV', 'ENPH', 'CELC', 'COCO', 'CENX', 'WSC', 'CIFR', 'GBDC', 'SLDE', 'FRPT', 'ELVN', 'INTA', 'MCHB', 'NMIH', 'SKYW', 'ALRM', 'SHOO', 'ACMR', 'OSIS', 'PENG', 'DYN', 'ATRC', 'CSQ', 'HURN', 'ACLS', 'IPGP', 'IDYA', 'FHB', 'SGRY', 'DNLI', 'FLY', 'CLBK', 'CALM', 'EXTR', 'WDFC', 'PTRN', 'SPSC', 'NRIX', 'DRH', 'MGRC', 'AVAH', 'CARG', 'CENT', 'ASST', 'LIFE', 'BEAM', 'VRDN', 'NTCT', 'AMBA', 'DGII', 'PRVA', 'PRCH', 'FIVN', 'MBX', 'RUM', 'FBNC', 'SKWD', 'NEOG', 'LFTO', 'VERX', 'LIND', 'POWI', 'LUNR', 'SUPN', 'FRVO', 'PLUS', 'BLKB', 'RXRX', 'NCNO', 'FLYW', 'MBIN', 'UCTT', 'VECO', 'ADEA', 'EEFT', 'ADUS', 'TMDX', 'PTON', 'HRMY', 'UPST', 'PGNY', 'VERA', 'NWBI', 'XNCR', 'UFPT', 'BCRX', 'IMNM', 'LASR', 'PENN', 'ALMR', 'NMRK', 'GCT', 'WGS', 'SEPN', 'DRVN', 'SDGR', 'MRVI', 'NEXT', 'MCRI', 'BL', 'XERS', 'ALGT', 'BRVE', 'COAG', 'VIR', 'TRVI', 'SONO', 'ABSI', 'PLUG', 'TBBK', 'XRAY', 'MQ', 'GENB', 'LMAT', 'ZBIO', 'PRGS', 'AGIO', 'ADRX', 'RUN', 'AEHR', 'ATEX', 'RBCAA', 'KMTS', 'ARHS', 'BLBD', 'MAZE', 'NTLA', 'PDFS', 'EZPW', 'ICFI', 'STOK', 'GSHD', 'PSNL', 'CERT', 'FRMI', 'OMCL', 'REPL', 'KLRA', 'WERN', 'HCSG', 'HUBG', 'PLAB', 'STRA', 'EVCM', 'MLYS', 'WLTH', 'IMKTA', 'JJSF', 'RARE', 'PAHC', 'CBRL', 'YSWY', 'CASH', 'GPCR', 'DJT', 'INVA', 'BAND', 'OCUL', 'HYMC', 'SAFT', 'ALHC', 'HLMN', 'LIME', 'ESQ', 'VISN', 'INOD', 'AMAL', 'REAL', 'ETON', 'ULCC', 'TWFG', 'ICHR', 'PCRX', 'TYRA', 'PWP', 'ANAB', 'ATLC', 'LQDT', 'LYCA', 'TRS', 'CRSR', 'TH', 'TSHA', 'OMER', 'TNDM', 'HBT', 'ALKT', 'KARD', 'EYE', 'AMSC', 'GIII', 'GO', 'LBRX', 'CRCT', 'GTM', 'INNV', 'CRAI', 'SNDX', 'SHLS', 'WBTN', 'RAPP', 'GDRX', 'ROCK', 'VSTM', 'AMPH', 'VOR', 'LZ', 'OMDA', 'UPWK', 'AVLN', 'CSTL', 'JCAP', 'MNKD', 'WLDN', 'BVS', 'OXLC', 'RPD', 'HLIT', 'FSBC', 'PRCT', 'LMRI', 'ATEC', 'GDYN', 'SGP', 'KRT', 'JBLU', 'JANX', 'FLNC', 'SPTX', 'CTY', 'MBWM', 'MCBS', 'LGIH', 'HSTM', 'CBLL', 'AVO', 'MLTX', 'QNST', 'IRMD', 'OIG', 'NBBK', 'CGEM', 'RIGL', 'ORIC', 'MRTN', 'SIBN', 'WLFC', 'NWPX', 'ODTX', 'DGICB', 'SBGI', 'LTGO', 'AIP', 'FRBT', 'GLUE', 'DJTWW', 'MGTX', 'BBNX', 'DAKT', 'BLMN', 'RJET', 'ASTE', 'JBIO', 'ACDC', 'AKTS', 'KPLT', 'GSBC', 'ALMS', 'NXDR', 'SWIM', 'PSEC', 'PRME', 'MFIC', 'DSP', 'EVLV', 'CRVS', 'HMH', 'SPFI', 'EVER', 'ALRS', 'PACB', 'KIDS', 'ROOT', 'CTKB', 'AHCO', 'BMBL', 'HTLD', 'BBSI', 'FWRG', 'FISI', 'COLL', 'SANA', 'ANNX', 'BBTX', 'WRLD', 'TASK', 'ARDX', 'WOOF', 'LYTS', 'BWMN', 'OABI', 'APEI', 'CGBD', 'ITG', 'CDNL', 'PRAA', 'AVBP', 'FDUS', 'SPT', 'PUBM', 'SCHL', 'NRDS', 'ELMT', 'KOPN', 'SGMT', 'LEGH', 'ATTO', 'ENVX', 'APMD', 'MSBI', 'RRBI', 'CBNK', 'FOXF', 'DSGN', 'RXT', 'STLN', 'SLDB', 'CCB', 'FDMT', 'LINC', 'TBLD', 'SABR', 'PRTH', 'GRPN', 'CADL', 'AURA', 'IMMX', 'IAM', 'SLRC', 'JBSS', 'RSVR', 'NNE', 'AVR', 'NTGR', 'OLMA','PZZA', 'MYGN', 'TRON', 'BCAX', 'GAIN', 'NVCT', 'MATW', 'ULH', 'KRNY', 'SSYS', 'CLYM', 'ACRS', 'IRWD', 'GERN', 'DNUT', 'BWFG', 'LPTH', 'FLGT', 'BWB','TITN', 'BSVN', 'STTK', 'GOOD', 'PDLB', 'SBC', 'ADTN', 'NANO', 'ARRY', 'TCMD', 'PANL', 'BRCB', 'MCFT', 'BBCP', 'ARVN', 'SGHT', 'CTMX', 'ETRA', 'GYRE', 'ANGO', 'CBIO', 'DMAC', 'OVID', 'MPLT', 'AQST', 'FRBA', 'EOLS', 'ABTC', 'FTH', 'FAC', 'HBCP', 'RGNX', 'MNPR', 'BLZE', 'WYFI', 'MBUU', 'PHAT', 'LOCO', 'MASS', 'IIIV', 'RMNI', 'CERS', 'ILPT', 'OPRT', 'TKNO', 'CBK', 'METC', 'PBFS', 'HNST', 'SLDP', 'BLSM', 'ASPE', 'RBB', 'CMCO', 'GLAD', 'VRRM', 'KRUS', 'NPCE', 'RUMBW', 'CCCC', 'RPAY', 'SUJA', 'PCB', 'EDIT', 'ASMB', 'CARL', 'ALLO', 'TLS', 'CTRN', 'HCMA', 'ALTI', 'NECB', 'VALU', 'SRTA', 'FOSL', 'PROK', 'ADV', 'AMSF', 'TECX', 'AVTX', 'TACO', 'GFUZ', 'ISTR', 'TRXB', 'GEMI', 'MNRO', 'TLRY', 'VITL', 'PTLO', 'RCKY', 'NNBR', 'USCB', 'FRST', 'CV', 'JAKK', 'SFIX', 'IRLA', 'FNKO', 'ERII', 'OBIO', 'CTNM', 'MOBI', 'WSBF', 'TCPC', 'KYTX', 'NAUT', 'CUB', 'FSBW', 'IMSR', 'SPRY', 'BCML', 'XFOR', 'MRAM', 'AVIR', 'ALEC', 'TMS', 'GOGO', 'LAND', 'QSI', 'CLNE', 'MNTK', 'ENTA', 'ASPI', 'PRLD', 'PPHC', 'GEVO', 'AGEN', 'NODK', 'BNTC', 'SABS', 'MYFW', 'VOGX', 'RELL', 'SCTX', 'BTBT', 'TMCI', 'EIKN', 'PUSA', 'FULC', 'LTRX', 'IMXI', 'RWAY', 'TDUP', 'HRZN', 'PLAY', 'CMRC', 'BCBP', 'LYEL', 'BIOA', 'GLOO', 'RCKT', 'OPAL', 'FBLA', 'IPSC', 'RMBI', 'QTTB', 'MTRX', 'ULBI', 'LXEO', 'LRMR', 'CABA', 'GLSI', 'OPTX', 'FATE', 'CAMP', 'CPZ', 'BDSX', 'IMRX', 'LAB', 'IMMR', 'OCGN', 'SVIA', 'LOVE', 'ZUMZ', 'GWRS', 'ASLE', 'VNDA', 'TLSI', 'REFI', 'CZWI', 'OPBK', 'ELDN', 'MRBK', 'CPSS', 'KLTR', 'MVST', 'KROS', 'RICK', 'PYXS', 'IKT', 'EXFY', 'RR', 'KRRO', 'MOVE', 'BBOT', 'FORR', 'LIEN', 'XGN', 'SVCO', 'SND', 'ARTV', 'RXST', 'RBKB', 'ATER', 'RNAC', 'AKBA', 'DTIL', 'LCUT', 'GPRO', 'AIRJ', 'ZSQR', 'VRA', 'APC', 'UPB', 'ECBK', 'ZNTL', 'BVFL', 'YARW', 'FLWS', 'CHCI', 'FINW', 'INGN', 'PAAC', 'TRDA', 'SION', 'RRGB', 'IVVD', 'STIM', 'ANTX', 'EBMT', 'NXH', 'DLTH', 'DIBS', 'HNVR', 'MXCT', 'PEPG', 'AIRO', 'DH', 'ONEW', 'QUIK', 'BRLT', 'SWMR', 'FISN', 'NSLR', 'AUC', 'CNTN', 'CURI','TUSK', 'MGNX', 'ALXO', 'HYNE', 'GSIT', 'CUE', 'NCMI', 'PDSB', 'STRO', 'EGAN', 'SRBK', 'HUCK', 'LSBK', 'TARA', 'DERM', 'MGYR', 'PLBY', 'QTRX', 'RAIL', 'ONEN', 'KVHI', 'SOUNW', 'SPRB', 'AMRO', 'SAMG', 'ATOM', 'CDXS', 'LUNG', 'OSS', 'SKYA', 'CVGI', 'CHRS', 'HCAT', 'AIRS', 'WSBK', 'FHTX', 'BYND', 'BSBK', 'HUMA', 'OTLK', 'NKTX', 'NERV', 'SIDU', 'SSTI', 'DFDV', 'SKYX', 'NAKA','EQ', 'OKUR', 'VYGR', 'UNCY', 'SHIM', 'IMUX', 'ILLU', 'BDTX', 'PARK', 'VTVT', 'JYNT', 'OXSQ', 'PMVP', 'ORGO', 'CBUS', 'VANI', 'NRXP', 'FNWB', 'RDZN','LENZ', 'MRLN', 'GNLX', 'INSE', 'ICCC', 'SEER', 'TVGN', 'FDSB', 'RENT', 'NDLS', 'RTSN', 'LAKE', 'CPBI', 'COYA', 'OESX', 'TNYA', 'RLYB', 'ETS', 'LUCD', 'RANI', 'BZFD', 'HFFG', 'SERA', 'ATRA', 'NFE', 'HOVR', 'EMPD', 'FACWW', 'VERI', 'TTEC', 'CSPI', 'ISPR', 'MMLP', 'SSBI', 'HYPR', 'OM', 'JRSH', 'BLUW', 'CCLD', 'RGS', 'BCIC', 'PAL', 'USGO', 'CING', 'FATN', 'AISP', 'GFUZW', 'ACRV', 'CPIX', 'CLST', 'HFBL', 'NMRA', 'TELO', 'DVLT', 'AFCG', 'BXBL', 'ECOR', 'TYGO', 'ROC', 'LNZA', 'UPXI', 'IMSRW', 'CGTX', 'SPAI', 'SKIN', 'MCHX', 'GOSS', 'UEIC', 'GRML', 'SPRO', 'RNXT', 'OABIW', 'RNTX', 'VRCA', 'XBIT', 'BOLD', 'OPTXW', 'DTI', 'TACT', 'TMSWW', 'PRTS', 'HOUR', 'AIRG', 'MYPS', 'INKT', 'TLPH', 'PLRX', 'XLO', 'ESYN', 'GENK', 'CTOR', 'COCH', 'SCOR', 'WATT', 'HYPD', 'AMCI', 'TCBS', 'GANX', 'MDAI', 'LASE', 'KLRS', 'IDN', 'HOWL', 'HDRN', 'LONA', 'IMA', 'BMEA', 'NXXT', 'LIDR', 'TIL', 'FRMM', 'ELTX', 'SRTS', 'CRBU', 'VGAS', 'INMB', 'SBCWW', 'DWTX', 'IPWR', 'KFFB', 'MNTS', 'AIRJW', 'SPWH', 'MVIS', 'HBIO', 'XTIA', 'MAMO', 'XOS', 'EXOZ', 'HIT', 'CVRX', 'SCYX','XBP', 'MWYN', 'ELUT', 'RPID', 'GAIA', 'MIND', 'TELA', 'STI', 'RYM', 'GRDX', 'RMCO', 'CIRC', 'LITS', 'ALDX', 'BOF', 'SVIAW', 'LVLU', 'ATHR', 'ACET', 'MLGO', 'BNAI', 'BEAT', 'PXLW', 'AERT', 'ALGS', 'AARD', 'MGX', 'FLD', 'HCMAW', 'PIII', 'ELWT', 'NXTC', 'JVA', 'TEAD', 'RMTI', 'BZAI', 'ESLA', 'RNAZ', 'AIFA', 'BYSI', 'PRHI', 'CELU', 'HOLO', 'FTCI', 'SHPH', 'DAIO', 'DCGO', 'SWAG', 'KTCC', 'MIRA', 'BIRD', 'FFR', 'FGC', 'SMXT', 'SDOT', 'ATOS', 'SNAL', 'MSGM', 'AEI', 'SKYQ', 'AWRE', 'MDRR', 'KYNB', 'ACTU', 'EXYN', 'OCCI', 'MCRB', 'CNTX', 'JSPR', 'ARAY', 'NEUP', 'ZEO', 'AISPW', 'HOVRW', 'BNGO', 'HSCS', 'EHTH', 'CLIR', 'SCLX', 'PAVM', 'FGI', 'LHAI', 'ABOS', 'KPTI', 'VEEA', 'SLE', 'MDAIW', 'QNME', 'DFNS', 'DARE', 'REBN', 'MOBX', 'PRPL', 'BBGI', 'BFRI', 'GUTS', 'SINT', 'BOLT', 'SMSI', 'JAGX', 'HIND', 'IRIX', 'ATYR', 'KTTA', 'RKTO', 'ICU', 'UPLD', 'FEMY', 'BTBD', 'ASBP', 'PASG', 'INTS', 'TCRX', 'KSCP', 'TVRD', 'AUROW', 'CDLX', 'ICMB', 'AZR', 'CALC', 'LTRN', 'XHLD', 'PLCE','MEDS', 'INHD', 'MDBH', 'BTLN', 'BFRG', 'INAB', 'BNKK', 'BLIN', 'MBRX', 'CURX', 'CYCU', 'MTVA', 'CNSP', 'LUCY', 'MSAI', 'NDRA', 'MYSE', 'EEIQ', 'SNTI', 'BTOC', 'FTHM', 'APRE', 'SNES', 'ALZN', 'INBS', 'ACXP', 'HDRNW', 'NWTG','ACON', 'TNON', 'RDZNW', 'VEEE', 'LGVN', 'CYN', 'GDC', 'SNOA', 'MGRX', 'PULM', 'FFAI', 'CDIO', 'GXAI', 'AQMS', 'NVNO', 'AUUD', 'HCTI', 'TRAW', 'SEGG', 'CWD', 'GRMLW', 'SONM', 'DRMA', 'VVOS', 'BIAF', 'AMST', 'XPON', 'HODO', 'QCLS', 'DFLI', 'AMIX', 'CVKD', 'CXAI', 'HYFM', 'GRI', 'ONCO', 'SXTP', 'YHC', 'CODX', 'KALA', 'EXYNW', 'CTNT', 'JTAI', 'FLYE', 'SGLY', 'FLDDW', 'POLA','JUNS', 'TGL', 'IPST', 'STLNW', 'DCOY', 'TRNR', 'BJDX', 'HCWB', 'CJMB', 'REVB', 'SLDPW', 'WORX', 'BFRGW', 'ELAB', 'ISPC', 'BOXL', 'NXL', 'GNPX', 'FRGT', 'KITT', 'ZEOWW', 'NXGL', 'PWCM', 'BLUWW', 'MOBXW', 'SHFS', 'WHLR', 'RMCOW', 'SGRX', 'EDBL', 'SKYAW', 'TVGNW', 'OLOX', 'UK', 'IPDN', 'VBIO', 'SQFT', 'ONFO', 'GNLN', 'TRUG', 'MSS', 'IPW', 'BEATW', 'DBGI', 'BZFDW', 'CDT', 'VGASW', 'LUCYW', 'RKDA', 'HSCSW', 'SCLXW', 'SHFSW', 'BIAFW', 'DFNSW', 'SRTM', 'COCHW', 'BTBDW', 'CYCUW', 'LNZAW', 'SXTPW', 'VEEAW', 'PIIIW', 'CXAIW', 'ACONW', 'ICUCW', 'SWAGW', 'EDBLW', 'DFLIW', 'ONFOW', 'CDIOW', 'ASBPW', 'KITTW', 'NXGLW', 'PARAW', 'SVIVW', 'SVIVU', 'TLNC', 'TLACU', 'TLNCU', 'SVIV', 'TDACU', 'TLNCW', 'CXII', 'CXIIU', 'CXIIW', 'SVCCW', 'CEPF', 'SVCC', 'SVAQU', 'SVAQ', 'DAAQ', 'DAAQW', 'CCXIW', 'CCXIU', 'CEPO', 'CEPV', 'SZZL', 'SZZLR', 'CRAN', 'CHI', 'CHPG', 'TBCV', 'CHPGR', 'TBCVU', 'TBCVW', 'CHPGU', 'TMTSU', 'TCGX', 'CHW', 'TDWD', 'CHY', 'TCXB', 'TDAC', 'TAVIR', 'CHAR', 'TAVI','CTAA', 'TLAC', 'TACH', 'CEPS', 'TDACW', 'CGCF', 'TACHW', 'THEO', 'CRANR','TACOW', 'CRAQR', 'CRAQ', 'CRANU', 'CGCFU', 'CGO', 'TMTS', 'OCLTW', 'CCXI', 'CCIIW', 'ALFUW', 'ALIS', 'ALISR', 'ALISU', 'ALOV', 'ALOVU', 'ALPX', 'ALPXU', 'AMAN', 'WLIIU', 'WLII', 'APAC', 'APMC', 'APMCR', 'WENN', 'APUR', 'APXT', 'APXTU', 'APXTW', 'ARCI', 'ARCIW', 'ARCL', 'ARCLU', 'ARTC', 'ATLQ', 'BACC', 'BACCR', 'XCBE', 'XCBEU', 'ALF', 'YICCU', 'AACOU', 'AACP', 'AACPR', 'AACPU', 'ZKPW', 'ZKPU', 'ZKP', 'AACPW', 'ACAA', 'ACAAU', 'ACAAW', 'ACGC', 'YICC', 'ALDFW', 'XTER', 'XSLLU', 'XSLL', 'ADAC', 'AESP', 'AESPR', 'AFJK', 'XIIIW', 'XIIIU', 'XIII', 'AFJKR', 'ALDF', 'VNMEW', 'VNME', 'VLOSW', 'CAII', 'TWLV', 'BRKHW', 'TVIVW', 'TVIVU', 'TVIV', 'BRTM', 'TVAIR', 'TVAI', 'TVACW', 'TVACU', 'TVA', 'CAES', 'CAPN', 'BRKH', 'CAPNU', 'CAQ', 'CAQUU', 'CATL', 'CATLR', 'CATLU', 'CCAQ', 'TRGSU', 'TRGS', 'CCAQU', 'CCCT', 'CCII', 'TWLVU', 'BREZR', 'VLOS', 'UYSCR', 'BCCQ', 'BCCQU', 'BCCQW', 'BDCI', 'VHCPW', 'VHCP', 'BEAG', 'BEAGR', 'BEAGU', 'BHAIU', 'BHAV', 'UYSCU', 'UYSC', 'BREZ', 'BHAVR', 'BID', 'BIXI', 'BIXIW', 'BKHA', 'BKHAR', 'BKHAU', 'BLRK', 'BLZR', 'BLZRU', 'BLZRW', 'BPAC', 'BRKHU', 'FDMMW', 'DBCA', 'DMAA', 'LATAU', 'LCCC', 'LEDRU', 'LFAC', 'LKSP', 'LKSPR', 'LKSPU', 'LPAA', 'LPAAU', 'LPBB', 'LPBBW','LPCV', 'LTGR', 'LTGRW', 'POLEW', 'POLE', 'PMTRW', 'PMTRU', 'PMTR', 'LWAC', 'LWACU', 'LWACW', 'MACI', 'PLMKW', 'PLMK', 'PLCIR', 'PLCI', 'MACIW', 'MBVI', 'LATA', 'PTAC', 'KRAQW', 'QSEA', 'ITHAW', 'JATT', 'JONE', 'RANGU', 'RANGR', 'RANG', 'RACD', 'RACC', 'QUMSU', 'QUMS', 'JTTT', 'KBON', 'QSEAR', 'KBONU', 'KRAQ', 'KCHV', 'KCHVR', 'KEYY', 'QADRU', 'QADR', 'KFII', 'KFIIR', 'KFIIU', 'KOYN', 'KOYNW', 'PTORU', 'PTOR', 'AACO', 'MCAH', 'MCAHU', 'MCGA', 'NPAC', 'MYXXU', 'NCO', 'OTGAW', 'OTGAU', 'OTGA', 'NHIV', 'OSPRU', 'OSPR', 'NHIVW', 'NMP', 'NMPAR', 'NOEM', 'NOEMU', 'NPACU', 'OYSE', 'NSAI', 'NSAIU', 'NSAIW', 'NTWO', 'ONCHW', 'ONCHU', 'ONCH', 'NTWOW', 'OACC', 'OCLT', 'OIMAU','OIM', 'OCLTU', 'MYX', 'OYSER', 'MCGAU', 'MKLY', 'PGACU', 'PGAC', 'MCGAW','MESH', 'MESHW', 'PECEW', 'PECEU', 'PECER', 'PECE', 'MEVO', 'MEVOU', 'MEVOW', 'MIAC', 'MKLYU', 'OYSEU', 'PCAPU', 'PCAP', 'MLAA', 'PAXGU', 'PAXG', 'MRCO', 'PALO', 'MTAK', 'PACHW', 'PACH', 'MUZE', 'PAACW', 'MUZEW', 'ITHA', 'ISNRW', 'ISNR', 'FMACR', 'OHAC', 'FGII', 'FGIIU', 'FIGX', 'FIGXU', 'SIMA', 'FJDI', 'FJDIR', 'FJDIU', 'SHOTU', 'SHOT', 'FLSC', 'FMAC', 'FMACU', 'FACTW', 'FSHP', 'FSHPR', 'FVAV', 'FWAC', 'FWACW', 'FXAC', 'GCGR', 'SDHIU', 'SDHI', 'GHXI', 'GHXIU', 'GIW', 'SCQCU', 'FDMM', 'FACT', 'GIWWU', 'SPEGU', 'SSEA', 'DMAAR', 'SSACU', 'SSAC', 'DMII', 'DMIIR', 'DNMX', 'DNMXU', 'DNMXW', 'DRDB', 'DRDBW', 'DTSQ', 'DYOR', 'SPEG', 'EWAVU', 'EGHA', 'EGHAR', 'SORN', 'SOCAU', 'SOCA', 'EMIS', 'EMISR', 'EURK', 'EURKR', 'EVOX', 'EVOXU', 'EVOXW', 'EWAV', 'SCPQ', 'GIX', 'RDAG', 'IEAG', 'HVMCW', 'IACO', 'IACOU', 'IACOW', 'IACQ', 'IACQW', 'IBAC', 'IBACR', 'RNGT', 'RNAQU', 'RNAQ', 'IDAC', 'IDACU', 'IGAC', 'HLXC', 'ILLUU', 'INAC', 'INACU', 'IPFX', 'IPFXU', 'IPHX', 'IPHXW', 'IPVV', 'IPXG', 'IPXGU', 'IRHO', 'IRHOR', 'RDAGW', 'HVMC', 'RREV', 'SCII', 'SAAQU', 'GIXXU', 'SCATW', 'SCATR', 'SCAT', 'GPAC', 'GPACU', 'GPAT', 'GPATW', 'GSHR', 'GSRF', 'GSRFR', 'GSRFU', 'SAAQW', 'SAAQ', 'RREVW', 'GSRV', 'GSRVR', 'GSRVU', 'GTEN', 'GTENW', 'GUAC', 'GUACW', 'HACQ', 'HCIC', 'RTACW', 'RTACU', 'RTAC', 'HCMAU', 'AACI'
            ],
            "nyse": [
                'MA', 'ABBV', 'ORCL', 'DELL', 'GS', 'GEV', 'CRM', 'BLK', 'UBER', 'TBB', 'COF', 'NOW', 'SNOW', 'NET', 'HCA', 'ICE', 'UPS', 'VRT', 'BX', 'RCL', 'HLT','KMI', 'CVNA', 'RSG', 'GM', 'HPE', 'URI', 'TRGP', 'LNG', 'DLR', 'MET', 'TDG', 'MPLX', 'BE', 'DVN', 'KEYS', 'VEEV', 'A', 'VYLR', 'XYZ', 'CIEN', 'SE', 'WAT', 'HEI', 'IQV', 'CARR', 'FIX', 'ARES', 'P', 'CMG', 'PRU', 'EL', 'VIK','CCL', 'MLM', 'VG', 'RKT', 'SUNB', 'TKO', 'ZTS', 'CQP', 'EXR', 'TWLO', 'IR', 'RBLX', 'FTS', 'SN', 'DG', 'OTIS', 'AWK', 'JBL', 'VLTO', 'VICI', 'CFG', 'CPNG', 'RBRK', 'DOW', 'IOT', 'Q', 'SYF', 'RL', 'LVS', 'PKG', 'MKL', 'USFD', 'HUBB', 'RS', 'PR', 'XYL', 'SOJC', 'DINO', 'AQNB', 'FTV', 'WES', 'DD', 'SNX', 'APG', 'FDXF', 'SOJD', 'CF', 'CRCL', 'TOST', 'PS', 'J', 'ITT', 'RDDT','IEX', 'CRL', 'ESS', 'H', 'WCC', 'DT', 'SOJE', 'U', 'OWL', 'DUKB', 'NVR', 'W', 'ALLE', 'YUMC', 'PFGC', 'CRBG', 'INVH', 'ULS', 'BURL', 'GDDY', 'EQH', 'TRU', 'RBC', 'IT', 'AIZ', 'APOS', 'OHI', 'ARMK', 'GKOS', 'SOLV', 'MAA', 'BJ', 'SUI', 'GWRE', 'KKRS', 'TME', 'AR', 'DKS', 'DTM', 'PEN', 'AHR', 'IONQ','GME', 'BMNR', 'PAYC', 'LII', 'RTO', 'SREA', 'HUBS', 'GNRC', 'FDS', 'MAIR', 'ALLY', 'WTS', 'FIG', 'ELAN', 'CR', 'AMH', 'RYAN', 'UHAL', 'EVR', 'PINS','DECK', 'AVTR', 'FNF', 'MOH', 'DOCN', 'BAH', 'GMED', 'RRX', 'AA', 'ESTC', 'WMS', 'AM', 'LTH', 'CPT', 'BXP', 'BIO', 'KNX', 'MUSA', 'HLI', 'PBF', 'OSCR', 'PCOR', 'HNGE', 'KNTK', 'JXN', 'SNAP', 'BRX', 'ALSN', 'VOYA', 'JAN', 'DAR', 'S', 'WLK', 'PRI', 'LEVI', 'CTRE', 'CHWY', 'EAI', 'EMP', 'CNM', 'WAL', 'ESI', 'ACM', 'REXR', 'NIO', 'FPS', 'ZETA', 'NE', 'CTVA', 'SARO', 'VSXY', 'ETSY', 'PACS', 'MSGK', 'MTDR', 'BROS', 'ANDG', 'LW', 'RAL', 'ZWS', 'VAL', 'AXTA', 'EPAM', 'FR', 'ADT', 'PATH', 'PRMB', 'PRH', 'TRNO', 'STAG', 'MGY', 'MP', 'BLDR', 'MAC', 'MSA', 'RNG', 'CAVA', 'COMP', 'PRS', 'MSM', 'ELF', 'INGM', 'OMF', 'HIMS', 'YOU', 'ACI', 'PJT', 'BOX', 'HOMB', 'CMSD', 'CMSC', 'EPRT', 'CVI', 'NIQ', 'DOCS', 'MANE', 'MTG', 'LOAR', 'DLB', 'ENS', 'GXO', 'KVYO', 'INSW', 'IBP', 'HGTY', 'CMSA', 'OUT', 'MBGL', 'HRI', 'ABCB', 'ORA', 'WH', 'HAE', 'SEI', 'CE', 'MTN', 'CNX', 'PSN', 'AMTM', 'PFH', 'KRMN', 'WHD', 'CWEN', 'ECG', 'MAIN', 'CON', 'BYD', 'AX', 'SNDR', 'OBDC', 'KRG', 'FCN', 'GOLF', 'FND', 'OGS', 'CRC', 'PL', 'KBR', 'JOBY', 'VNT', 'HASI', 'SITE', 'KGS','OKLO', 'CRGY', 'BETA', 'MC', 'WK', 'CNK', 'HCC', 'RXO', 'STWD', 'MIR', 'PIPR', 'DK', 'UCB', 'EPR', 'HCXY', 'NNI', 'APLE', 'ALH', 'OTF', 'TDW', 'ESAB', 'CNR', 'SLGN', 'ENVA', 'MRP', 'BMI', 'SKT', 'AQN', 'HESM', 'TPC', 'KRC','KFY', 'BILL', 'QTWO', 'PAY', 'VVV', 'ENO', 'COLD', 'KTB', 'NP', 'PLNT', 'EE', 'BOOT', 'SPHR', 'ELC', 'MSGE', 'NVST', 'ATMU', 'CNS', 'DTW', 'ASBA', 'POST', 'RNST', 'OGN', 'SMG', 'NIC', 'SLG', 'MWA', 'ABG', 'FIGS', 'CII', 'PDI', 'IRT', 'CURB', 'HIW', 'NATL', 'HAYW', 'UNMA', 'PK', 'MIAX', 'MMS', 'LMND', 'GNW', 'BNL', 'ACHR', 'PFSI', 'KNF', 'DKL', 'MHO', 'YETI', 'FOUR', 'BSM', 'HTGC', 'WT', 'KAI', 'CWK', 'GPI', 'DTG', 'DTB', 'BKU', 'FSK', 'TALO', 'WRBY', 'NAN', 'NOG', 'SHAK', 'KD', 'COTY', 'PFS', 'VIA', 'APAM', 'DNOW', 'GPOR', 'TNET', 'RWTN', 'HGV', 'KBH', 'REZI', 'AD', 'RWTO', 'FGN', 'RSI', 'KN', 'RH', 'FG', 'UNFI', 'KSS', 'LBRT', 'BCC', 'WTTR', 'AMC', 'BTU', 'FBK', 'BFAM', 'MSGR', 'GRBK', 'GRDN', 'ASAN', 'BGR', 'GDV', 'TTAM', 'NGVT', 'MFAO', 'MFAN', 'VVX', 'UE', 'BKD', 'FCPT', 'IVT', 'SMR', 'LCII', 'PEB', 'SHO', 'ROG', 'BHVN', 'LPG', 'PBH', 'CALX', 'RCUS', 'BKV', 'PHIN', 'STUB', 'NTST', 'PMTU', 'TIC', 'HLIO', 'CTRI', 'BOBS', 'DV', 'RDW', 'UA', 'WS', 'UTZ', 'NGL', 'LEU', 'CC', 'SMA', 'AMR', 'GLOB', 'KYN', 'INFQ', 'SAH', 'BTX', 'CIMN', 'INSP', 'VSTS', 'MTX', 'KRP', 'RLJ', 'AI', 'GRC', 'HMN', 'XHR', 'STDN', 'DBD', 'SFB', 'MIY', 'RVT', 'FLOC', 'GEL', 'BRSL', 'ATEN', 'MNR', 'BY', 'PDO','BFLY', 'MUJ', 'BDJ', 'ARDT', 'DEI', 'HUN', 'AFGD', 'NUVB', 'NBHC', 'RZC','AFGB', 'PRLB', 'VOYG', 'DFIN', 'MIN', 'MHD', 'GLP', 'GNL', 'RYZ', 'LOB', 'RVLV', 'ENR', 'CXM', 'ETV', 'MQY', 'CBL', 'ARLO', 'TDOC', 'AVEX', 'RQI', 'NRP', 'GAB', 'MUC', 'FRA', 'BCAT', 'CCS', 'UZD', 'MBC', 'ECCV', 'EFC', 'MUA', 'ECAT', 'KMPB', 'SVV', 'IIPR', 'AGL', 'AFGC', 'PRKS', 'NCV', 'TPB', 'AAT', 'UAN', 'PD', 'HAWK', 'ADIG', 'CNMD', 'SG', 'UZE', 'CDRE', 'UZF', 'UMH', 'ADNT', 'SLVM', 'USPH', 'AMPX', 'AFGE', 'BBAI', 'UTI', 'FOR', 'GBX', 'SPH','WD', 'MCB', 'HZO', 'WOLF', 'CRI', 'AMBQ', 'LADR', 'AESI', 'IBTA', 'BOW', 'MYE', 'DEC', 'ECVT', 'BV', 'AMRC', 'BRBR', 'NCZ', 'MMI', 'HRTG', 'HTFC', 'DEA', 'NMAX', 'YELP', 'BST', 'KFRC', 'BTZ', 'ETW', 'RPC', 'HQH', 'UTL', 'BCX', 'GSBD', 'DSL', 'FSCO', 'CMP', 'NABL', 'HIPO', 'FET', 'SXC', 'PUMP', 'PTA', 'RNP', 'ORC', 'INR', 'ACEL', 'COUR', 'BH', 'PLOW', 'TDAY', 'FMN', 'XIFR', 'ANRO', 'JBGS', 'DFH', 'MTUS', 'MAX', 'YSS', 'PXED', 'CAPL', 'ESRT', 'KBDC', 'CODI', 'FUBO', 'AIZN', 'LXU', 'GHM', 'SKYH', 'EIG', 'SAFE', 'KOP', 'TXO', 'PHR', 'VTS', 'INN', 'CTO', 'GRNT', 'WLKP', 'CNNE', 'MITN', 'BKSY', 'MITP', 'DNA', 'BFS', 'YEXT', 'GDOT', 'MNTN', 'BCSF', 'CIM', 'CLDT', 'PFLT', 'BALY', 'ANGX', 'FINV', 'NIE', 'NGVC', 'CUBB', 'PSTL', 'PMT', 'MG', 'BW', 'DLY', 'JBI', 'OFRM', 'NXP', 'SMC', 'WTI', 'BME', 'BTGO', 'BXC', 'VEL', 'FPH', 'FOF', 'CARS', 'BSTZ', 'MGRE', 'HOV', 'IVR', 'OIS', 'XFLT', 'AII', 'HPP', 'EVC', 'NRGV', 'NCDL', 'LUCK', 'OOMA', 'NPB', 'SD', 'MGR', 'SOC', 'ONT', 'SDHC', 'EVEX', 'RFI', 'CWH', 'TRTX', 'TYG', 'OLP', 'EVH', 'ETO', 'FTHY', 'OPFI', 'WNC', 'HQL', 'AVBC', 'NXRT', 'FBRT', 'HUYA', 'AHRT', 'FVR', 'RYAM','ETB', 'TRC', 'MGF', 'BNED', 'HBB', 'MGRB', 'GNE', 'BRSP', 'IPI', 'MAGN', 'ASPN', 'NGS', 'ASIX', 'BLW', 'CTEV', 'XRN', 'ABR', 'SAZ', 'SI', 'SAJ', 'SAY', 'EVN', 'RWT', 'SPCE', 'MGRD', 'BOC', 'MEC', 'CHCT', 'LEO', 'SPIR', 'RNGR', 'JILL', 'FPI', 'EBS', 'ZIP', 'CION', 'PMO', 'LAW', 'BBW', 'CYH', 'RM', 'OPTU', 'CBNA', 'COSO', 'PPT', 'KTF', 'EAF', 'HLLY', 'BRCC', 'PMM', 'EFT', 'KREF', 'ARI', 'PINE', 'SEG', 'MLP', 'GBAB', 'NREF', 'SES', 'PACK', 'ARDC','SMHI', 'BLND', 'XPER', 'CHPT', 'MMT', 'EOT', 'ACV', 'EVMN', 'CURV', 'ALTG', 'KLC', 'ALIT', 'BMEZ', 'AIV', 'MBI', 'NUS', 'XPOF', 'AMWL', 'MFM', 'FIRY', 'SCM', 'PNNT', 'DHX', 'LDI', 'NPWR', 'ACRE', 'TPVG', 'CIA', 'FOA', 'MPV', 'MITT', 'AMPY', 'RC', 'GPJA', 'AOMR', 'CMTG', 'SRI', 'ECC', 'PIM', 'SSTK', 'GNT', 'COOK', 'DOUG', 'LVWR', 'ONL', 'NLOP', 'EARN', 'TLYS', 'NXG', 'GHI', 'OWLT', 'JELD', 'GCTS', 'SRFM', 'SRG', 'ZVIA', 'BHR', 'EVF', 'RPT', 'NRDY', 'DTF', 'CRT', 'EIC', 'CHGG', 'BARK', 'SLQT', 'IH', 'PVL', 'RFL', 'TSQ','VOC', 'CLPR', 'ANVS', 'SKIL', 'AVD', 'CABO', 'SPRU', 'LOCL', 'STEM', 'GPMT', 'LFT', 'SST', 'PRT', 'AHT', 'AOMN', 'THQ', 'STK', 'ACP', 'WIW', 'WIA', 'WEA', 'WDI', 'TEI', 'THW', 'VLT', 'SOJF', 'AOD', 'UTF', 'VVR', 'AEFC', 'TWN', 'AGD', 'AFB', 'AOMD', 'ZTR', 'VGI', 'USA', 'MSD', 'SCD', 'IDE', 'BUI', 'HTD', 'HPS', 'HPI', 'HPF', 'BWG', 'HIX', 'HFRO', 'HEQ', 'CAF', 'GUG', 'GHY', 'GF', 'GDO', 'GDL', 'HYT', 'IGA', 'SBI', 'IGD', 'JRS', 'JRI', 'JQC', 'JOF', 'JLS', 'JGH', 'JFR', 'JCE', 'BSL', 'ISD', 'BTO', 'BTT', 'IIF', 'IGR', 'IGI', 'FSSL', 'FPF', 'FMY', 'FLC', 'EHI', 'EFR', 'EDF', 'EDD', 'ECCU', 'DUKU', 'DTK', 'DSU', 'DSM', 'DPG', 'DNP', 'DMO', 'DHF', 'DBL', 'CRBD', 'ELLA','EMF', 'EMO', 'EVT', 'FGSN', 'FFC', 'FFA', 'CICB', 'CICC', 'EXG', 'EVG', 'EOD', 'ETY', 'ETJ', 'ETG', 'CIMO', 'CIMP', 'EOI', 'KIO', 'KKRT', 'BOE', 'NVG', 'BBN', 'PHK', 'PGP', 'PFO', 'PFN', 'PFLA', 'PFL', 'PFD', 'PCQ', 'PCN', 'PCM', 'PAXS', 'BGB', 'OPP', 'BGH', 'PML', 'PMTV', 'PMTW', 'RIV', 'SAX', 'SAV', 'RWTS', 'RWTQ', 'RWTP', 'ASGI', 'RCS', 'PNI', 'RCD', 'AVK', 'AWF', 'RA', 'AWP', 'PTY', 'NZF', 'NUW', 'LDP', 'NUV', 'NBB', 'NAZ', 'NAD', 'NAC', 'MYN', 'BHV', 'MSDL', 'MPA', 'BIT', 'MMU', 'MMD', 'MHF', 'MEGI', 'MCN', 'LGI', 'NBXG', 'BHK', 'NEA', 'NNY', 'NRUC', 'NRK', 'NPV', 'NPFD', 'NPCT', 'BGT','NMZ', 'NFJ', 'NMS', 'NMI', 'NMAI', 'NKX', 'BGY', 'NIM', 'JPC'
            ]
        },
        "default_period": "max",  # Used only if a stock's CSV doesn't exist yet
        "interval": "1d"
    },

    "plots": {
        "xticks_interval": 90,
        "dpi": 300,
        "color_actual": "#001f3f",
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
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# Silence Pandas deprecation warnings from yfinance
warnings.filterwarnings("ignore", message=".*inplace keyword.*")

print("All libraries loaded")


# ==========================================
# 3. CHECK LAST FETCHED DATE & APPEND DATA
# ==========================================

def process_company_data(symbol, exchange_dir, config):
    # Target path matches your folder layout: nasdaq/{symbol}/ or nyse/{symbol}/
    output_dir = os.path.join(exchange_dir, symbol)
    csv_path = os.path.join(output_dir, f"{symbol}.csv")

    if os.path.exists(csv_path):
        # 1. Read existing CSV and find the last fetched date
        existing_df = pd.read_csv(csv_path, index_col="Date", parse_dates=True)
        existing_df.index = pd.to_datetime(existing_df.index).tz_localize(None)
        existing_df = existing_df.sort_index()

        if existing_df.empty:
            raise ValueError(f"Existing CSV for {symbol} is empty.")

        last_fetched_date = existing_df.index.max().strftime("%Y-%m-%d")

        # 2. Download from last_fetched_date onwards
        new_data = yf.download(
            symbol,
            start=last_fetched_date,
            interval=config["stock"]["interval"],
            auto_adjust=True,
            progress=False
        )

        if new_data.empty:
            raise ValueError(f"No new stock data for {symbol} since {last_fetched_date}.")

        if isinstance(new_data.columns, pd.MultiIndex):
            new_data.columns = new_data.columns.get_level_values(0)

        new_data.index = pd.to_datetime(new_data.index).tz_localize(None)
        new_data = new_data.sort_index()

        # 3. Combine existing data with newly downloaded rows and deduplicate
        cols = ["Open", "High", "Low", "Close", "Volume"]
        combined = pd.concat([existing_df[cols], new_data[cols]])
        data = combined[~combined.index.duplicated(keep="last")].sort_index()
        action_status = f"Appended from {last_fetched_date}"

    else:
        # Fallback if a stock does not have a folder/CSV in nasdaq/ or nyse/ yet
        new_data = yf.download(
            symbol,
            period=config["stock"]["default_period"],
            interval=config["stock"]["interval"],
            auto_adjust=True,
            progress=False
        )

        if new_data.empty:
            raise ValueError(f"No stock data downloaded for new symbol {symbol}.")

        os.makedirs(output_dir, exist_ok=True)

        if isinstance(new_data.columns, pd.MultiIndex):
            new_data.columns = new_data.columns.get_level_values(0)

        new_data.index = pd.to_datetime(new_data.index).tz_localize(None)
        data = new_data[["Open", "High", "Low", "Close", "Volume"]].sort_index().copy()
        action_status = "Created full history"

    # Recalculate daily percentage returns cleanly across the full dataset
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

    # Save updated CSV in {exchange_dir}/{symbol}/{symbol}.csv
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

    plt.title(f"Daily close price for {symbol} ({exchange_dir.upper()}), {display_date_range}")
    plt.grid(True, axis="y", linestyle="--", alpha=0.7)
    plt.xlabel("Date")
    plt.ylabel("Adjusted closing price")
    plt.tight_layout()

    # Save high-resolution chart in {exchange_dir}/{symbol}/{symbol}_chart.png
    plot_path = os.path.join(output_dir, f"{symbol}_chart.png")
    plt.savefig(plot_path, dpi=config["plots"]["dpi"], bbox_inches="tight")
    plt.close(fig)

    print(f"[{exchange_dir.upper()} - {symbol}] {action_status} -> {csv_path}")
    print(f"[{exchange_dir.upper()} - {symbol}] Total data points: {num_data_points} ({display_date_range})\n")

    return data_date, data_close_price, num_data_points, display_date_range, df


# ==========================================
# 4. RUN FOR BOTH NASDAQ AND NYSE LISTS
# ==========================================

results = {"nasdaq": {}, "nyse": {}}
failed_symbols = {"nasdaq": [], "nyse": []}

for exchange_folder, symbol_list in config["stock"]["exchanges"].items():
    print(f"\n==========================================")
    print(f"Processing {exchange_folder.upper()} ({len(symbol_list)} symbols)...")
    print(f"==========================================\n")

    for sym in symbol_list:
        try:
            results[exchange_folder][sym] = process_company_data(sym, exchange_folder, config)
        except Exception as e:
            print(f"[{exchange_folder.upper()} - {sym}] Skipped due to error: {e}\n")
            failed_symbols[exchange_folder].append(sym)

print("\n==========================================")
print("UPDATE SUMMARY")
print("==========================================")
for exchange_folder in config["stock"]["exchanges"]:
    print(
        f"{exchange_folder.upper()}: "
        f"Updated {len(results[exchange_folder])} | "
        f"Failed/Skipped {len(failed_symbols[exchange_folder])}"
    )