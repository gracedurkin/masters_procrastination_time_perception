# Temporal Bisection Task: Parameter Extraction

Python script that fits a sigmoid psychometric function to each participant's temporal bisection data and extracts the Bisection Point, thresholds (T1, T2), Differential Threshold and Weber Ratio. It also saves a plot of the fitted curve for each participant.

> **Attribution.** Based on the code from [m-v-arruda/Temporal-Bisection-Task](https://github.com/m-v-arruda/Temporal-Bisection-Task.git), used in:
>
> Valério de Arruda, M., Reyes, M. B., das Neves, S. F., Herrmann, F., Verzili, B., & Galduróz, R. F. (2024). Temporal bisection task as a predictor of cognitive deficits. *The European Journal of Neuroscience, 60*(9), 6330–6341. https://doi.org/10.1111/ejn.16554
>
> **Main differences:** the input was adapted to the format of my own data, and the analysis runs in batch (all participants in one run) instead of one participant at a time.

## Requirements

Python 3.8+ and:

```bash
pip install pandas numpy scipy matplotlib
```

For exact reproducibility, record your versions (`pip freeze | grep -E "pandas|numpy|scipy|matplotlib"`) in a `requirements.txt`.

## Input data

A CSV (default `Temporal_Bisection.csv`) with one row per participant and these columns. Proportions are between 0 and 1.

| Column | Description |
|---|---|
| `ID_REDCAP` | Participant ID (used in output file names) |
| `LONG_PROPORTION_500MS` | Proportion of "long" responses at 500 ms |
| `LONG_PROPORTION_630MS` | ... at 630 ms |
| `LONG_PROPORTION_793.5MS` | ... at 793.5 ms |
| `LONG_PROPORTION_1000MS` | ... at 1000 ms |
| `LONG_PROPORTION_1260MS` | ... at 1260 ms |
| `LONG_PROPORTION_1587MS` | ... at 1587 ms |
| `LONG_PROPORTION_2000MS` | ... at 2000 ms |

Example:

```csv
ID_REDCAP,LONG_PROPORTION_500MS,LONG_PROPORTION_630MS,LONG_PROPORTION_793.5MS,LONG_PROPORTION_1000MS,LONG_PROPORTION_1260MS,LONG_PROPORTION_1587MS,LONG_PROPORTION_2000MS
001,0.00,0.05,0.20,0.50,0.80,0.95,1.00
```

## How to run

The script uses Google Colab paths (`/content/`). On Colab, upload the CSV to `/content/` and run the script. To run locally, replace `/content/` in the script with your own folder and run:

```bash
python temporal_bisection_parameters.py
```

## Method

For each participant, the proportion of "long" responses is fitted against duration with:

```
P(long | t) = 1 / (1 + exp(-a * (t - b)))
```

using `scipy.optimize.curve_fit` with method `dogbox`, bounds `a` in [0, 0.8] and `b` in [300, 2300] ms, `maxfev=5000`, no weights and no explicit initial guess (SciPy starts at the middle of the bounds). The procedure is deterministic. Participants with missing values are skipped, and failed fits are reported in the console.

| Parameter | Formula | Meaning |
|---|---|---|
| Bisection Point | `b` | Duration at 50% "long" responses (ms) |
| T1 | `b − ln(3)/a` | Duration at 25% "long" (ms) |
| T2 | `b + ln(3)/a` | Duration at 75% "long" (ms) |
| Differential Threshold | `(T2 − T1) / 2` | Half the interquartile range (ms) |
| Weber Ratio | `(T2 − T1) / Bisection Point` | Relative sensitivity |

> **Note:** this Weber Ratio equals 2 × Differential Threshold / Bisection Point. Many papers use Differential Threshold / Bisection Point, so state the definition you use.

## Output

- `Final_Metrics_Results.csv`: one row per participant with `ID_REDCAP`, `Bisection_Point`, `Threshold_T1`, `Threshold_T2`, `Differential_Threshold` and `Weber_Ratio` (rounded to 4 decimals).
- `BISSEC_<ID_REDCAP>.png`: observed proportions, fitted curve and annotated Bisection Point, T1 and T2 (saved at 1000 dpi; lower `dpi` in `plt.savefig` for faster runs).

## Limitations

- Seven data points are used to fit two parameters, and no goodness-of-fit measure is saved.
- If a fit lands on a bound (slope at 0 or 0.8), the derived parameters are unreliable. Check those plots.
- Durations and column names are hard-coded.

## Citation

If you use this code, please cite the original paper (above), the original repository, and this repository:

- Original repository: https://github.com/m-v-arruda/Temporal-Bisection-Task
- This repository: Durkin, G. (2026). https://github.com/gracedurkin/masters_procrastination_time_perception
