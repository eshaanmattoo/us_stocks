# ==========================================
# 1. CONFIGURATION
# ==========================================

config = {
    "stock": {
        # Add one or multiple stock symbols to process
        "symbols":['MA', 'ABBV', 'ORCL', 'DELL', 'GS', 'GEV', 'CRM', 'BLK', 'UBER', 'TBB', 'COF', 'NOW', 'SNOW', 'NET', 'HCA', 'ICE', 'UPS', 'VRT', 'BX', 'RCL', 'HLT','KMI', 'CVNA', 'RSG', 'GM', 'HPE', 'URI', 'TRGP', 'LNG', 'DLR', 'MET', 'TDG', 'MPLX', 'BE', 'DVN', 'KEYS', 'VEEV', 'A', 'VYLR', 'XYZ', 'CIEN', 'SE', 'WAT', 'HEI', 'IQV', 'CARR', 'FIX', 'ARES', 'P', 'CMG', 'PRU', 'EL', 'VIK','CCL', 'MLM', 'VG', 'RKT', 'SUNB', 'TKO', 'ZTS', 'CQP', 'EXR', 'TWLO', 'IR', 'RBLX', 'FTS', 'SN', 'DG', 'OTIS', 'AWK', 'JBL', 'VLTO', 'VICI', 'CFG', 'CPNG', 'RBRK', 'DOW', 'IOT', 'Q', 'SYF', 'RL', 'LVS', 'PKG', 'MKL', 'USFD', 'HUBB', 'RS', 'PR', 'XYL', 'SOJC', 'DINO', 'AQNB', 'FTV', 'WES', 'DD', 'SNX', 'APG', 'FDXF', 'SOJD', 'CF', 'CRCL', 'TOST', 'PS', 'J', 'ITT', 'RDDT','IEX', 'CRL', 'ESS', 'H', 'WCC', 'DT', 'SOJE', 'U', 'OWL', 'DUKB', 'NVR', 'W', 'ALLE', 'YUMC', 'PFGC', 'CRBG', 'INVH', 'ULS', 'BURL', 'GDDY', 'EQH', 'TRU', 'RBC', 'IT', 'AIZ', 'APOS', 'OHI', 'ARMK', 'GKOS', 'SOLV', 'MAA', 'BJ', 'SUI', 'GWRE', 'KKRS', 'TME', 'AR', 'DKS', 'DTM', 'PEN', 'AHR', 'IONQ','GME', 'BMNR', 'PAYC', 'LII', 'RTO', 'SREA', 'HUBS', 'GNRC', 'FDS', 'MAIR', 'ALLY', 'WTS', 'FIG', 'ELAN', 'CR', 'AMH', 'RYAN', 'UHAL', 'EVR', 'PINS','DECK', 'AVTR', 'FNF', 'MOH', 'DOCN', 'BAH', 'GMED', 'RRX', 'AA', 'ESTC', 'WMS', 'AM', 'LTH', 'CPT', 'BXP', 'BIO', 'KNX', 'MUSA', 'HLI', 'PBF', 'OSCR', 'PCOR', 'HNGE', 'KNTK', 'JXN', 'SNAP', 'BRX', 'ALSN', 'VOYA', 'JAN', 'DAR', 'S', 'WLK', 'PRI', 'LEVI', 'CTRE', 'CHWY', 'EAI', 'EMP', 'CNM', 'WAL', 'ESI', 'ACM', 'REXR', 'NIO', 'FPS', 'ZETA', 'NE', 'CTVA', 'SARO', 'VSXY', 'ETSY', 'PACS', 'MSGK', 'MTDR', 'BROS', 'ANDG', 'LW', 'RAL', 'ZWS', 'VAL', 'AXTA', 'EPAM', 'FR', 'ADT', 'PATH', 'PRMB', 'PRH', 'TRNO', 'STAG', 'MGY', 'MP', 'BLDR', 'MAC', 'MSA', 'RNG', 'CAVA', 'COMP', 'PRS', 'MSM', 'ELF', 'INGM', 'OMF', 'HIMS', 'YOU', 'ACI', 'PJT', 'BOX', 'HOMB', 'CMSD', 'CMSC', 'EPRT', 'CVI', 'NIQ', 'DOCS', 'MANE', 'MTG', 'LOAR', 'DLB', 'ENS', 'GXO', 'KVYO', 'INSW', 'IBP', 'HGTY', 'CMSA', 'OUT', 'MBGL', 'HRI', 'ABCB', 'ORA', 'WH', 'HAE', 'SEI', 'CE', 'MTN', 'CNX', 'PSN', 'AMTM', 'PFH', 'KRMN', 'WHD', 'CWEN', 'ECG', 'MAIN', 'CON', 'BYD', 'AX', 'SNDR', 'OBDC', 'KRG', 'FCN', 'GOLF', 'FND', 'OGS', 'CRC', 'PL', 'KBR', 'JOBY', 'VNT', 'HASI', 'SITE', 'KGS','OKLO', 'CRGY', 'BETA', 'MC', 'WK', 'CNK', 'HCC', 'RXO', 'STWD', 'MIR', 'PIPR', 'DK', 'UCB', 'EPR', 'HCXY', 'NNI', 'APLE', 'ALH', 'OTF', 'TDW', 'ESAB', 'CNR', 'SLGN', 'ENVA', 'MRP', 'BMI', 'SKT', 'AQN', 'HESM', 'TPC', 'KRC','KFY', 'BILL', 'QTWO', 'PAY', 'VVV', 'ENO', 'COLD', 'KTB', 'NP', 'PLNT', 'EE', 'BOOT', 'SPHR', 'ELC', 'MSGE', 'NVST', 'ATMU', 'CNS', 'DTW', 'ASBA', 'POST', 'RNST', 'OGN', 'SMG', 'NIC', 'SLG', 'MWA', 'ABG', 'FIGS', 'CII', 'PDI', 'IRT', 'CURB', 'HIW', 'NATL', 'HAYW', 'UNMA', 'PK', 'MIAX', 'MMS', 'LMND', 'GNW', 'BNL', 'ACHR', 'PFSI', 'KNF', 'DKL', 'MHO', 'YETI', 'FOUR', 'BSM', 'HTGC', 'WT', 'KAI', 'CWK', 'GPI', 'DTG', 'DTB', 'BKU', 'FSK', 'TALO', 'WRBY', 'NAN', 'NOG', 'SHAK', 'KD', 'COTY', 'PFS', 'VIA', 'APAM', 'DNOW', 'GPOR', 'TNET', 'RWTN', 'HGV', 'KBH', 'REZI', 'AD', 'RWTO', 'FGN', 'RSI', 'KN', 'RH', 'FG', 'UNFI', 'KSS', 'LBRT', 'BCC', 'WTTR', 'AMC', 'BTU', 'FBK', 'BFAM', 'MSGR', 'GRBK', 'GRDN', 'ASAN', 'BGR', 'GDV', 'TTAM', 'NGVT', 'MFAO', 'MFAN', 'VVX', 'UE', 'BKD', 'FCPT', 'IVT', 'SMR', 'LCII', 'PEB', 'SHO', 'ROG', 'BHVN', 'LPG', 'PBH', 'CALX', 'RCUS', 'BKV', 'PHIN', 'STUB', 'NTST', 'PMTU', 'TIC', 'HLIO', 'CTRI', 'BOBS', 'DV', 'RDW', 'UA', 'WS', 'UTZ', 'NGL', 'LEU', 'CC', 'SMA', 'AMR', 'GLOB', 'KYN', 'INFQ', 'SAH', 'BTX', 'CIMN', 'INSP', 'VSTS', 'MTX', 'KRP', 'RLJ', 'AI', 'GRC', 'HMN', 'XHR', 'STDN', 'DBD', 'SFB', 'MIY', 'RVT', 'FLOC', 'GEL', 'BRSL', 'ATEN', 'MNR', 'BY', 'PDO','BFLY', 'MUJ', 'BDJ', 'ARDT', 'DEI', 'HUN', 'AFGD', 'NUVB', 'NBHC', 'RZC','AFGB', 'PRLB', 'VOYG', 'DFIN', 'MIN', 'MHD', 'GLP', 'GNL', 'RYZ', 'LOB', 'RVLV', 'ENR', 'CXM', 'ETV', 'MQY', 'CBL', 'ARLO', 'TDOC', 'AVEX', 'RQI', 'NRP', 'GAB', 'MUC', 'FRA', 'BCAT', 'CCS', 'UZD', 'MBC', 'ECCV', 'EFC', 'MUA', 'ECAT', 'KMPB', 'SVV', 'IIPR', 'AGL', 'AFGC', 'PRKS', 'NCV', 'TPB', 'AAT', 'UAN', 'PD', 'HAWK', 'ADIG', 'CNMD', 'SG', 'UZE', 'CDRE', 'UZF', 'UMH', 'ADNT', 'SLVM', 'USPH', 'AMPX', 'AFGE', 'BBAI', 'UTI', 'FOR', 'GBX', 'SPH','WD', 'MCB', 'HZO', 'WOLF', 'CRI', 'AMBQ', 'LADR', 'AESI', 'IBTA', 'BOW', 'MYE', 'DEC', 'ECVT', 'BV', 'AMRC', 'BRBR', 'NCZ', 'MMI', 'HRTG', 'HTFC', 'DEA', 'NMAX', 'YELP', 'BST', 'KFRC', 'BTZ', 'ETW', 'RPC', 'HQH', 'UTL', 'BCX', 'GSBD', 'DSL', 'FSCO', 'CMP', 'NABL', 'HIPO', 'FET', 'SXC', 'PUMP', 'PTA', 'RNP', 'ORC', 'INR', 'ACEL', 'COUR', 'BH', 'PLOW', 'TDAY', 'FMN', 'XIFR', 'ANRO', 'JBGS', 'DFH', 'MTUS', 'MAX', 'YSS', 'PXED', 'CAPL', 'ESRT', 'KBDC', 'CODI', 'FUBO', 'AIZN', 'LXU', 'GHM', 'SKYH', 'EIG', 'SAFE', 'KOP', 'TXO', 'PHR', 'VTS', 'INN', 'CTO', 'GRNT', 'WLKP', 'CNNE', 'MITN', 'BKSY', 'MITP', 'DNA', 'BFS', 'YEXT', 'GDOT', 'MNTN', 'BCSF', 'CIM', 'CLDT', 'PFLT', 'BALY', 'ANGX', 'FINV', 'NIE', 'NGVC', 'CUBB', 'PSTL', 'PMT', 'MG', 'BW', 'DLY', 'JBI', 'OFRM', 'NXP', 'SMC', 'WTI', 'BME', 'BTGO', 'BXC', 'VEL', 'FPH', 'FOF', 'CARS', 'BSTZ', 'MGRE', 'HOV', 'IVR', 'OIS', 'XFLT', 'AII', 'HPP', 'EVC', 'NRGV', 'NCDL', 'LUCK', 'OOMA', 'NPB', 'SD', 'MGR', 'SOC', 'ONT', 'SDHC', 'EVEX', 'RFI', 'CWH', 'TRTX', 'TYG', 'OLP', 'EVH', 'ETO', 'FTHY', 'OPFI', 'WNC', 'HQL', 'AVBC', 'NXRT', 'FBRT', 'HUYA', 'AHRT', 'FVR', 'RYAM','ETB', 'TRC', 'MGF', 'BNED', 'HBB', 'MGRB', 'GNE', 'BRSP', 'IPI', 'MAGN', 'ASPN', 'NGS', 'ASIX', 'BLW', 'CTEV', 'XRN', 'ABR', 'SAZ', 'SI', 'SAJ', 'SAY', 'EVN', 'RWT', 'SPCE', 'MGRD', 'BOC', 'MEC', 'CHCT', 'LEO', 'SPIR', 'RNGR', 'JILL', 'FPI', 'EBS', 'ZIP', 'CION', 'PMO', 'LAW', 'BBW', 'CYH', 'RM', 'OPTU', 'CBNA', 'COSO', 'PPT', 'KTF', 'EAF', 'HLLY', 'BRCC', 'PMM', 'EFT', 'KREF', 'ARI', 'PINE', 'SEG', 'MLP', 'GBAB', 'NREF', 'SES', 'PACK', 'ARDC','SMHI', 'BLND', 'XPER', 'CHPT', 'MMT', 'EOT', 'ACV', 'EVMN', 'CURV', 'ALTG', 'KLC', 'ALIT', 'BMEZ', 'AIV', 'MBI', 'NUS', 'XPOF', 'AMWL', 'MFM', 'FIRY', 'SCM', 'PNNT', 'DHX', 'LDI', 'NPWR', 'ACRE', 'TPVG', 'CIA', 'FOA', 'MPV', 'MITT', 'AMPY', 'RC', 'GPJA', 'AOMR', 'CMTG', 'SRI', 'ECC', 'PIM', 'SSTK', 'GNT', 'COOK', 'DOUG', 'LVWR', 'ONL', 'NLOP', 'EARN', 'TLYS', 'NXG', 'GHI', 'OWLT', 'JELD', 'GCTS', 'SRFM', 'SRG', 'ZVIA', 'BHR', 'EVF', 'RPT', 'NRDY', 'DTF', 'CRT', 'EIC', 'CHGG', 'BARK', 'SLQT', 'IH', 'PVL', 'RFL', 'TSQ','VOC', 'CLPR', 'ANVS', 'SKIL', 'AVD', 'CABO', 'SPRU', 'LOCL', 'STEM', 'GPMT', 'LFT', 'SST', 'PRT', 'AHT', 'AOMN', 'THQ', 'STK', 'ACP', 'WIW', 'WIA', 'WEA', 'WDI', 'TEI', 'THW', 'VLT', 'SOJF', 'AOD', 'UTF', 'VVR', 'AEFC', 'TWN', 'AGD', 'AFB', 'AOMD', 'ZTR', 'VGI', 'USA', 'MSD', 'SCD', 'IDE', 'BUI', 'HTD', 'HPS', 'HPI', 'HPF', 'BWG', 'HIX', 'HFRO', 'HEQ', 'CAF', 'GUG', 'GHY', 'GF', 'GDO', 'GDL', 'HYT', 'IGA', 'SBI', 'IGD', 'JRS', 'JRI', 'JQC', 'JOF', 'JLS', 'JGH', 'JFR', 'JCE', 'BSL', 'ISD', 'BTO', 'BTT', 'IIF', 'IGR', 'IGI', 'FSSL', 'FPF', 'FMY', 'FLC', 'EHI', 'EFR', 'EDF', 'EDD', 'ECCU', 'DUKU', 'DTK', 'DSU', 'DSM', 'DPG', 'DNP', 'DMO', 'DHF', 'DBL', 'CRBD', 'ELLA','EMF', 'EMO', 'EVT', 'FGSN', 'FFC', 'FFA', 'CICB', 'CICC', 'EXG', 'EVG', 'EOD', 'ETY', 'ETJ', 'ETG', 'CIMO', 'CIMP', 'EOI', 'KIO', 'KKRT', 'BOE', 'NVG', 'BBN', 'PHK', 'PGP', 'PFO', 'PFN', 'PFLA', 'PFL', 'PFD', 'PCQ', 'PCN', 'PCM', 'PAXS', 'BGB', 'OPP', 'BGH', 'PML', 'PMTV', 'PMTW', 'RIV', 'SAX', 'SAV', 'RWTS', 'RWTQ', 'RWTP', 'ASGI', 'RCS', 'PNI', 'RCD', 'AVK', 'AWF', 'RA', 'AWP', 'PTY', 'NZF', 'NUW', 'LDP', 'NUV', 'NBB', 'NAZ', 'NAD', 'NAC', 'MYN', 'BHV', 'MSDL', 'MPA', 'BIT', 'MMU', 'MMD', 'MHF', 'MEGI', 'MCN', 'LGI', 'NBXG', 'BHK', 'NEA', 'NNY', 'NRUC', 'NRK', 'NPV', 'NPFD', 'NPCT', 'BGT','NMZ', 'NFJ', 'NMS', 'NMI', 'NMAI', 'NKX', 'BGY', 'NIM', 'JPC'],
        "period": "max",
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
# 3. DOWNLOAD & SAVE STOCK DATA + CHART
# ==========================================

def process_company_data(symbol, config):
    data = yf.download(
        symbol,
        period=config["stock"]["period"],
        interval=config["stock"]["interval"],
        auto_adjust=True,
        progress=False
    )

    if data.empty:
        raise ValueError(f"No stock data downloaded for {symbol}.")

    # Create target directory: data/{symbol}/ only after successful download
    output_dir = os.path.join(config["data"]["base_dir"], symbol)
    os.makedirs(output_dir, exist_ok=True)

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.sort_index()

    # Calculate daily percentage returns
    data["Daily_Return"] = data["Close"].pct_change() * 100

    # Prepare CSV dataset
    df = data[[
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "Daily_Return"
    ]].copy()

    df.index.name = "Date"

    # Save CSV as data/{symbol}/{symbol}.csv
    csv_path = os.path.join(output_dir, f"{symbol}.csv")
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

    print(f"[{symbol}] Saved CSV: {csv_path}")
    print(f"[{symbol}] Saved Plot: {plot_path}")
    print(f"[{symbol}] Data points: {num_data_points} ({display_date_range})\n")

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

print(f"Finished! Successfully downloaded: {len(results)} | Failed/Skipped: {len(failed_symbols)}")