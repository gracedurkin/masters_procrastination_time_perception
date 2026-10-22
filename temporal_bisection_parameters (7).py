import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def sigmoid(x, a, b):
    return 1.0 / (1.0 + np.exp(-a * (x - b)))

file_path = '/content/Temporal_Bisection.csv'
df = pd.read_csv(file_path)

time_stm = np.array([500.0, 630.0, 793.5, 1000.0, 1260.0, 1587.0, 2000.0])

proportion_columns = [
    'LONG_PROPORTION_500MS', 'LONG_PROPORTION_630MS', 'LONG_PROPORTION_793.5MS',
    'LONG_PROPORTION_1000MS', 'LONG_PROPORTION_1260MS', 'LONG_PROPORTION_1587MS',
    'LONG_PROPORTION_2000MS'
]

metrics_results = []

for index, row in df.iterrows():
    subj_id = row['ID_REDCAP']

    if pd.isna(row[proportion_columns]).any():
        print(f"Skipping ID {subj_id}: missing data.")
        continue

    perc_long = row[proportion_columns].values.astype(float)

    try:
        popt, pcov = curve_fit(
            sigmoid, time_stm, perc_long, 
            method='dogbox', bounds=([0., 300.], [0.8, 2300.]), maxfev=5000
        )

        pnt_bisec = round(popt[1], 4)
        T1_ = popt[1] - (np.log(3) / popt[0])
        T2_ = popt[1] + (np.log(3) / popt[0])
        lim_dif = (T2_ - T1_) / 2
        WR = (T2_ - T1_) / pnt_bisec

        metrics_results.append({
            'ID_REDCAP': subj_id,
            'Bisection_Point': pnt_bisec,
            'Threshold_T1': round(T1_, 4),
            'Threshold_T2': round(T2_, 4),
            'Differential_Threshold': round(lim_dif, 4),
            'Weber_Ratio': round(WR, 4)
        })

        rng = np.arange(time_stm[0], time_stm[-1], 0.1)
        
        plt.figure(figsize=(15, 10))
        plt.plot(time_stm, perc_long, color='green', marker='o', linestyle='', ms=7)
        plt.plot(rng, sigmoid(rng, *popt), label="Ajusted Curve [Sigmoid]", linestyle=':', lw=3)
        plt.ylabel('Proportion "Long" Responses', fontsize=14)
        plt.xlabel('Temporal Duration (ms)', fontsize=14)
        plt.xticks(time_stm, time_stm, fontsize=12)
        plt.yticks(np.arange(0, 1.1, step=0.1), fontsize=12)
        plt.legend(loc='upper left', fontsize=14)
        
        plt.annotate(pnt_bisec, xy=(popt[1], 0.5), xycoords='data',
                    xytext=(popt[1]-47, 0.), textcoords=("data", "axes fraction"),
                    arrowprops=dict(arrowstyle="<-", connectionstyle="arc3"),
                    bbox=dict(boxstyle="round", fc="w"), fontsize=12)
        
        plt.annotate(round(T1_, 4), xy=(T1_, 0.25), xycoords='data',
                    xytext=(T1_-200, 0.265), textcoords=("data", "axes fraction"),
                    arrowprops=dict(arrowstyle="<-", connectionstyle="arc3"),
                    bbox=dict(boxstyle="round", fc="w"), fontsize=12)
        
        plt.annotate(round(T2_, 4), xy=(T2_, 0.75), xycoords='data',
                    xytext=(T2_+100, 0.72), textcoords=("data", "axes fraction"),
                    arrowprops=dict(arrowstyle="<-", connectionstyle="arc3"),
                    bbox=dict(boxstyle="round", fc="w"), fontsize=12)

        plt.title('Ajusted Curve for the Temporal Bisection Task', fontsize=18)
        plt.grid()

        plt.savefig(f'/content/BISSEC_{subj_id}.png', dpi=1000, transparent=True, bbox_inches='tight')
        plt.close()

    except Exception as e:
        print(f"Error for ID {subj_id}: {e}")

df_results = pd.DataFrame(metrics_results)
df_results.to_csv('/content/Final_Metrics_Results.csv', index=False)
print("Batch processing and plotting complete!")