# Spotify Streaming History Analysis

A deep dive into 11+ years of my personal Spotify listening history, using Python and pandas to explore listening habits, favorite artists and tracks, skip behavior, and how much of each song actually gets listened to.

## What's in this project

I looked at **149,860 individual song plays**, spanning **July 2013 to December 2024**, and worked through four main questions:

- **How has my listening changed over time?** (volume, time of day, day of week, seasons)
- **What are my most-played artists, tracks, and albums** — and does "most played" mean the same thing as "most total time listened"?
- **What makes me skip a song**, and can the data even be trusted to answer that?
- **How much of an average song do I actually listen to**, and does that differ by artist, year, or device?

Along the way, I also found and worked through a real data-quality problem in the dataset — the "skipped" flag turned out to be broken for four full years — and had to build my own estimate of song length, since the raw data doesn't include it.

## Key findings

- **Listening has become more deliberate over time.** Since 2017, I've played fewer songs overall, but each one runs longer, the mix of artists I play has gotten more varied, and the typical song now gets listened to almost all the way through — a median completion rate of just 13% in 2017 climbed to nearly 100% by 2023/2024.
- **"Ode To The Mets" by The Strokes is my single most-played song by every measure** — most plays, most total listening time, and one of the lowest skip rates of any song in the dataset.
- **The Beatles, The Killers, and John Mayer are my most consistent favorites**, topping both play-count and total-time rankings, and all getting skipped less than average.
- **Roughly half of everything I've ever played — both songs and artists — was played exactly once.** Alongside the steady favorites, there's been a lot of genuine one-off exploration.
- **The "skipped" label in the raw data is broken for 2017–2021** — it shows a literal 0% skip rate across tens of thousands of plays those years, which isn't realistic. I confirmed this using a separate, reliable signal (how often I hit "next"), which shows completely normal skipping behavior through that same period. This became one of the more important findings in the whole project.
- **A song's length changes what "skipped" and "% completed" even mean.** For long tracks (like Led Zeppelin's, which often run 8+ minutes), a completely normal, non-skip listen can still show up as a low completion percentage — the two measurements are answering genuinely different questions.

Full write-ups with the complete numbers and reasoning behind each finding are in [`docs/`](docs/):

- [`01-data-understanding.md`](docs/01-data-understanding.md) — dataset structure, data quality checks, and what the "skipped" column actually measures
- [`02-top-artists-tracks.md`](docs/02-top-artists-tracks.md) — top artists and tracks by play count vs. total time
- [`03-top-artists-tracks-extended.md`](docs/03-top-artists-tracks-extended.md) — top albums, listening diversity over time, favorite artist by year, one-play wonders
- [`04-skip-behavior.md`](docs/04-skip-behavior.md) — what predicts a skip, and the data-quality gap found in the `skipped` field
- [`05-completion-rate.md`](docs/05-completion-rate.md) — how much of each song gets listened to, and why it doesn't always agree with the skip data

## Tech stack

- **Python** with **pandas** for data cleaning and analysis
- **matplotlib** / **seaborn** for visualizations
- **Jupyter notebooks**, run through VS Code
- **uv** for dependency and environment management
- **Parquet** for the cleaned, processed dataset (keeps proper data types, unlike CSV)

## Project structure

```
spotify-analysis/
├── data/
│   ├── processed/
│   │   └── spotify_history_clean.parquet  # cleaned dataset with engineered columns (Parquet)
│   └── raw/
│       ├── spotify_data_dictionary.csv
│       └── spotify_history_csv            # original exported CSV, untouched
├── notebooks/
│   ├── 01_data_understanding.ipynb        # cleaning, data quality checks,
│   ├── 02_eda.ipynb                       # time trends, top artists/tracks,
│   ├── 03_eda_skip_behaviour.ipynb        # skip behavior analysis
│   └── 04_engagement.ipynb                # how much of each song gets listened to
├── src/
│   └── spotify_analysis/
│       ├── __pycache__/
│       ├── __init__.py
│       └── prep.py                       # shared data-cleaning function, used once by 01_data_understanding
├── docs/                                 # detailed write-ups for each analysis section
│   ├── 1.data_understanding.md
│   ├── 2_top_artists.md
│   ├── 3_top_artists_tracks_extended.md
│   ├── 4_eda_skip_behaviour.md
│   └── 5_engagement_completion_rate.md
├── pyproject.toml
├── README.md                            # main README file with project summary and analysis
└── uv.lock

```

The raw CSV is cleaned and feature-engineered exactly once, in `01_data_understanding.ipynb`, using the `clean_streaming_data()` function in `src/spotify_analysis/prep.py`. The result is saved to `data/processed/`, and every other notebook loads that processed file directly rather than repeating the cleaning steps.

## Running this yourself

1. Clone the repo and install [uv](https://docs.astral.sh/uv/) if you don't already have it.
2. From the project root, run:
   ```
   uv sync
   ```
3. Open the project in VS Code, open a notebook, and select the `.venv` kernel when prompted.
4. Run `01_data_understanding.ipynb` first — it generates the processed dataset the other notebooks depend on.
5. `02_eda.ipynb` and `03_skip_behaviour.ipynb` can then be run in any order.

## About the data

This is my own Spotify Extended Streaming History export, requested directly from Spotify. It includes every song I played from 2013 through 2024, with details like timestamp, platform, how long I played it, and how/why it started and ended. The raw CSV is included in this repo as-is, since it's just my own personal listening data.

## A note on data quality

Part of this project involved treating the dataset critically rather than accepting every column at face value — the `skipped` field turned out to be unreliable for a multi-year stretch, and the "% completed" metric had to be built from an estimate rather than true song lengths, with its own known limitations. Both issues are explained in detail in the relevant docs above, since flagging what a dataset _can't_ reliably tell you is as important as reporting what it can.
