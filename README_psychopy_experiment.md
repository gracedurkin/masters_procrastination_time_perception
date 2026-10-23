# Pure Procrastination Scale, 27-item Monetary Choice Questionnaire and Temporal Bisection Task (PsychoPy)

A PsychoPy experiment that combines three tasks in a single session:

Pure Procrastination Scale (PPS): a 12-item self-report questionnaire (1-5 Likert scale). The original scale is described in Steel (2010), and the Portuguese items used here follow the Brazilian version by Rocha et al. (2021).

Monetary Choice Questionnaire (MCQ-27): 27 hypothetical choices between a smaller immediate reward and a larger delayed reward, based on Kirby et al. (1999).

Temporal Bisection (TB) task: participants learn a short (500 ms) and a long (2000 ms) tone, are trained to classify them, and then classify intermediate durations. The task is based on the protocol by Valério De Arruda et al. (2024).

Instrument references

- PPS (original): Steel, P. (2010). Arousal, avoidant and decisional procrastinators: Do they exist? Personality and Individual Differences, 48(8), 926-934.

- PPS (Brazilian version): Rocha, R. Z., Almeida, C. R. S., & Dias, A. C. G. (2021). Pure Procrastination Scale e Irrational Procrastination Scale: validation of a Brazilian version. Psico-USF, 26(3), 507-518. https://doi.org/10.1590/1413-82712021260309
  
- MCQ: Kirby, K. N., Petry, N. M., & Bickel, W. K. (1999). Heroin addicts have higher discount rates for delayed rewards than non-drug-using controls. Journal of Experimental Psychology: General, 128(1), 78-87.
  
- Temporal bisection task: Valério De Arruda, M., Reyes, M. B., Das Neves, S. F., Herrmann, F., Verzili, B., & Galduróz, R. F. (2024). Temporal bisection task as a predictor of cognitive deficits. European Journal of Neuroscience, 60(9), 6330-6341. https://doi.org/10.1111/ejn.16554

All on-screen text is in **Brazilian Portuguese** (see [Stimulus language](#stimulus-language) for English reference translations).

- **Experiment name (internal):** `procrastination_timeperception`
- **Built with:** PsychoPy Builder, version **2026.1.3**
- **Estimated duration:** about 20 minutes (estimate; depends on participant response speed)

---

## Table of contents

1. [Contents of the ZIP file](#contents-of-the-zip-file)
2. [Requirements](#requirements)
3. [How to run in PsychoPy](#how-to-run-in-psychopy)
4. [Experiment flow](#experiment-flow)
5. [Output data](#output-data)
6. [Converting the CSV output to XLSX (recommended)](#converting-the-csv-output-to-xlsx-recommended)
7. [Customizing the experiment](#customizing-the-experiment)
8. [Known issues and notes](#known-issues-and-notes)
9. [Stimulus language](#stimulus-language)
10. [Citation and license](#citation-and-license)

---

## Contents of the ZIP file

This repository provides the whole experiment as a single archive, **`procrastination_timeperception.zip`**. Download it and **extract it completely** before running anything (see [How to run in PsychoPy](#how-to-run-in-psychopy)). Inside the ZIP you will find:

```
procrastination_timeperception.zip
├── experimento_completo_grace.psyexp                  # PsychoPy Builder file (editable experiment)
├── experimento_completo_grace_lastrun.py              # Auto-generated Python script (runnable)
├── perguntas copy.csv                                 # PPS items (column: pergunta)
├── Kirby_Conditions copy.csv                          # MCQ trials (valor_imediato, valor_adiado, dias_atraso)
├── Condicoes_tempo_updated.csv                        # TB phase 2 conditions (stimulus, correct_response, duration)
├── condicoes_fasefinal_temporal_updated .csv          # TB phase 3 conditions (stimulus, duration)  <- note the space before ".csv"
├── pps_scale.png                                      # Image of the 1-5 response scale shown with each PPS item
├── 500ms2.wav, 630ms2.wav, 793ms2.wav,
│   1000ms2.wav, 1260ms2.wav, 1587ms2.wav,
│   2000ms2.wav                                        # Tone stimuli (must be in the same folder)
└── data/                                              # Output folder (one set of files per participant)
```

> **Important:** the script uses relative paths and changes its working directory to its own folder. After extracting the ZIP, all CSV, image and audio files listed above must sit in the **same folder** as the `.psyexp` / `.py` file, with exactly these names. Do **not** run the experiment from inside the ZIP file (e.g., by double-clicking the script in the compressed-folder preview), because the stimulus files will not be found. Keep the extracted folder structure intact.

### Input files

| File | Columns | Rows | Used in |
|---|---|---|---|
| `perguntas copy.csv` | `pergunta` | 12 | PPS loop (`trials_pps`), presented sequentially |
| `Kirby_Conditions copy.csv` | `valor_imediato`, `valor_adiado`, `dias_atraso` | 27 | MCQ loop (`trials_mcq`), presented sequentially |
| `Condicoes_tempo_updated.csv` | `stimulus`, `correct_response`, `duration` | 2 | TB phase 2 loop (`trials_TBphase2`) |
| `condicoes_fasefinal_temporal_updated .csv` | `stimulus`, `duration` | 70 | TB phase 3 loop (`trials_phase3`) |

---

## Requirements

- **PsychoPy 2026.1.3** (Builder/Runner, or the standalone installation). Using the same version is recommended for exact reproducibility; other versions may work but are untested.
- **Python:** the version bundled with that PsychoPy release (no extra packages are needed to run the experiment).
- **Operating system:** developed and run on Windows; PsychoPy is also supported on macOS and Linux.
- **Audio:** stereo headphones or speakers. The audio library is **PTB** (`Audio lib = ptb`), so a working PsychoPy-compatible sound device is required.
- **Keyboard:** a standard QWERTY layout. The task uses the keys `1`-`5`, `Q`, `P`, `Space` and `Esc`.
- **Display:** the experiment runs **full-screen** at 1536 x 864 px (`units = height`) on screen 1 (Builder setting; `screen=0` in the generated script). Adjust in *Experiment settings* if your monitor differs.
- *(Optional, for the data conversion step)* Python with `pandas` and `openpyxl`, or Microsoft Excel / LibreOffice.

---

## How to run in PsychoPy

### Option A: PsychoPy Builder / Runner (recommended)

1. Install PsychoPy 2026.1.3.
2. Download `procrastination_timeperception.zip` and **extract (unzip) all of its contents** into a folder of your choice, keeping all files together.
3. Open `experimento_completo_grace.psyexp` (from the extracted folder) in PsychoPy Builder.
4. Click **Run** (green play button). To test without full-screen and with a "pilot" participant ID, click **Pilot** instead.

### Startup dialog

A dialog asks for:

- `participant`: pre-filled with a random 6-digit ID; overwrite it with your own ID.
- `session`: defaults to `001`.

### Quitting

Press **Esc** at any time to abort the experiment. Data collected up to that point is saved by PsychoPy's data handler.

---

## Experiment flow

| # | Routine(s) | What happens | Keys |
|---|---|---|---|
| 1 | `Start` | Welcome and instructions for the questionnaire | `Space` |
| 2 | `PPS` (loop `trials_pps`, 12 trials) | One procrastination statement is shown with the 1-5 response scale image (`pps_scale.png`). Timeout: 120 s. | `1`-`5` |
| 3 | `MCQ_Instructions`, `MCQ_Instructions2` | Instructions for the monetary choice task (rewards are **hypothetical**) | `Space` |
| 4 | `MCQ` + `spacer_mcq` (loop `trials_mcq`, 27 trials) | Choice between "R$ X today" (left) and "R$ Y in N days" (right). Timeout: 30 s. 0.5 s blank between trials. | `Q` = immediate, `P` = delayed |
| 5 | `TB_Instructions`, `TB_Inst_phase1` | Instructions for the time-perception task | `Space` |
| 6 | `TB_phase1` (loop `trials_TBphase1`, 5 reps) | **Learning phase.** Each repetition: fixation (2 s) -> label "CURTO (TECLA Q)" -> 500 ms tone -> fixation -> label "LONGO (TECLA P)" -> 2000 ms tone. No response required. | none |
| 7 | `TB_Inst_phase2` | Instructions for the classification phase | `Space` |
| 8 | `spacer_phase2`, `trial_phase2`, `response_phase2` (loop `trials_TBphase2`, up to 40 reps x 2 conditions, random order) | **Training phase.** Fixation (2 s) -> tone (500 ms or 2000 ms) -> "Curto(Q) ou Longo(P)?" (max 10 s). The phase ends once the participant reaches **10 correct responses**. | `Q` = short, `P` = long |
| 9 | `TB_Inst_phase3` | Instructions for the test phase (intermediate durations) | `Space` |
| 10 | `spacer_phase3`, `trial_phase3`, `response_phase3` (loop `trials_phase3`, 70 trials, random order) | **Test phase.** Fixation (2 s) -> tone -> "Curto (Q) ou Longo(P)?" (max 10 s). 7 durations x 10 repetitions. | `Q` = short, `P` = long |
| 11 | `End` | Thank-you screen | `Space` |

### Tone durations used in the test phase

| Stimulus file | Duration (ms) | Repetitions |
|---|---|---|
| `500ms2.wav` | 500 (short anchor) | 10 |
| `630ms2.wav` | 630 | 10 |
| `793ms2.wav` | 793 | 10 |
| `1000ms2.wav` | 1000 | 10 |
| `1260ms2.wav` | 1260 | 10 |
| `1587ms2.wav` | 1587 | 10 |
| `2000ms2.wav` | 2000 (long anchor) | 10 |

The durations are logarithmically spaced between the short and long anchors.

### Key mapping summary

| Task | Key | Meaning |
|---|---|---|
| PPS | `1` ... `5` | 1 = very rarely / does not represent me ... 5 = very frequently / always represents me |
| MCQ | `Q` | Choose the immediate reward ("Agora") |
| MCQ | `P` | Choose the delayed reward ("Depois") |
| Time bisection | `Q` | Short |
| Time bisection | `P` | Long |

---

## Output data

For each run PsychoPy writes the following files to the `data/` folder, named
`<participant>_procrastination_timeperception_<date>`:

| Extension | Content |
|---|---|
| `.csv` | **Wide-format** trial data (the file you will analyze) |
| `.psydat` / `.pkl` | PsychoPy binary data (can be re-loaded with PsychoPy's `fromFile`) |
| `.log` | Detailed event log (`info` level) |

### Main columns in the `.csv`

Each row corresponds to one trial of one of the loops, so many columns are empty for rows that belong to other tasks.

**PPS**

| Column | Description |
|---|---|
| `pergunta` | Statement shown (Portuguese) |
| `key_resp_pps.keys` | Key pressed (`1`-`5`); empty if timed out |
| `key_resp_pps.rt` | Response time (s) |

**MCQ (delay discounting)**

| Column | Description |
|---|---|
| `valor_imediato`, `valor_adiado`, `dias_atraso` | Immediate amount (R$), delayed amount (R$), delay (days) |
| `key_resp_MCQ.keys`, `key_resp_MCQ.rt` | Raw key (`q`/`p`) and response time |
| `Resposta` | `q`, `p`, or `no_response` |
| `Valor_Imediato`, `Valor_Adiado`, `Dias_Atraso` | Copies of the trial parameters |
| `Resposta_Binaria` | `0` = immediate (Q), `1` = delayed (P) |

**Time bisection - phase 2 (training)**

| Column | Description |
|---|---|
| `stimulus`, `duration`, `correct_response` | Tone file, duration (s) and correct key |
| `key_resp_phase2.keys`, `key_resp_phase2.rt` | Participant's key and response time |

**Time bisection - phase 3 (test)**

| Column | Description |
|---|---|
| `stimulus`, `duration` | Tone file and duration |
| `key_resp_phase3.keys`, `key_resp_phase3.rt` | Participant's key (`q` = short, `p` = long) and response time |

**General**

`participant`, `session`, `date`, `expName`, `psychopyVersion`, `frameRate`, `thisRow.t` (timestamp), and `*.started` / `*.stopped` timestamps for each routine and component.

## Converting the CSV output to XLSX (recommended)

**For the best visualization of the output, we recommend converting the `.csv` file to an `.xlsx` workbook.** The wide-format file has many columns (including timestamps) and several empty cells, and it is much easier to read, filter and freeze panes in a spreadsheet. It also avoids delimiter and encoding problems when double-clicking a CSV in Excel.

## Citation and license

If you use this experiment, please cite this repository and PsychoPy:

Grace Durkin, 2026. https://github.com/gracedurkin/masters_procrastination_time_perception

> Peirce J, Gray JR, Simpson S, MacAskill M, Hochenberger R, Sogo H, Kastman E, Lindelov JK. (2019). PsychoPy2: Experiments in behavior made easy. *Behavior Research Methods*, 51, 195-203. https://doi.org/10.3758/s13428-018-01193-y

Please also cite the original sources of the instruments you use (the Pure Procrastination Scale and the Kirby Monetary Choice Questionnaire, as well as the Portuguese adaptations, if applicable)
