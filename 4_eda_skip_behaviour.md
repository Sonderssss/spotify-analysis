# Skip Behavior Deep-Dive

This section explores what correlates with `skipped == True`, building on the finding from `01-data-understanding.md` that `skipped` reflects short play duration rather than simply "ended via the forward button."

## Note on Sample Size

Several categorical breakdowns below include categories with very few plays (e.g. certain `reason_start` values, some platforms). Skip rates calculated from small samples (roughly under 100 plays) are shown for completeness but are **not treated as statistically meaningful** — a single anomalous play can swing a small group's rate dramatically. Findings are only stated as conclusions where sample size supports them.

## Stage 1 — Skip Rate by Platform

| Platform       | Skip rate |
| -------------- | --------- |
| windows        | 14.07%    |
| iOS            | 10.27%    |
| mac            | 6.12%     |
| android        | 5.18%     |
| cast to device | 0.00%     |
| web player     | 0.00%     |

Android (139,821 plays) and, to a lesser extent, iOS/windows/mac carry enough volume to trust their rates. **Cast to device (3,898 plays) and web player (225 plays) both show a literal 0% skip rate** — plausible as a real pattern (e.g. casting to a speaker may not lend itself to active skipping), but the web player sample in particular is small enough to treat this cautiously rather than as a firm conclusion.

## Stage 2 — Skip Rate by Shuffle Mode

- **74.5%** of all plays occur in shuffle mode.
- Shuffle usage varies sharply by platform: near-universal on android/iOS/windows, but **cast to device is almost exclusively non-shuffle** (3,893 of 3,898 plays).
- Skip rate is modestly higher for shuffled plays: **5.57%** (shuffle=True) vs. **4.32%** (shuffle=False) — consistent with shuffled listening being less deliberately chosen.

## Stage 3 — Skip Rate by `reason_start`

| reason_start | Count  | Skip rate |
| ------------ | ------ | --------- |
| trackdone    | 76,655 | 2.26%     |
| fwdbtn       | 53,793 | 7.85%     |
| clickrow     | 11,228 | 9.00%     |
| appload      | 3,729  | 15.07%    |
| backbtn      | 2,205  | 7.07%     |
| playbtn      | 1,458  | 5.01%     |
| remote       | 477    | 5.24%     |

(Categories under ~100 plays — trackerror, unknown/Unknown, nextbtn, popup, endplay, autoplay — omitted from conclusions per the sample-size note above.)

**Findings:**

- Plays starting from `trackdone` (i.e. the previous track finished naturally) have the lowest skip rate — a natural continuation is rarely abandoned.
- Plays starting from `appload` (track auto-resumes when the app opens) have the highest reliable skip rate — suggesting these plays are often not what the listener was ready for at that moment.
- `clickrow` (deliberately selecting a track) has a slightly _higher_ skip rate than `fwdbtn` (landing on a track via forward-skipping) — a mild inversion of intuition, possibly because deliberate clicks are more exploratory ("let me check this out") while forward-skip landings during shuffle are more passively accepted either way.

## Stage 4 — Skip Rate by Top 20 Artists (by play count)

| Artist                 | Skip rate |
| ---------------------- | --------- |
| Ed Sheeran             | 6.79%     |
| Imagine Dragons        | 5.48%     |
| The Rolling Stones     | 5.23%     |
| Led Zeppelin           | 5.16%     |
| The Velvet Underground | 4.84%     |
| Radiohead              | 4.43%     |
| Bob Dylan              | 4.27%     |
| The Black Keys         | 4.26%     |
| Coldplay               | 4.23%     |
| Paul McCartney         | 3.97%     |
| Arctic Monkeys         | 3.69%     |
| Lou Reed               | 3.47%     |
| Howard Shore           | 3.39%     |
| John Mayer             | 3.15%     |
| The Killers            | 2.86%     |
| The Beatles            | 2.85%     |
| Johnny Cash            | 2.78%     |
| Pink Floyd             | 2.57%     |
| Kings of Leon          | 2.46%     |
| The Strokes            | 1.60%     |

**Findings:**

- **The Strokes have the lowest skip rate of the group (1.6%)** — notable given "Ode To The Mets" (a Strokes track) is the single most-played, most-total-time track in the dataset; it is rarely abandoned as well as frequently played.
- **The Beatles, The Killers, and John Mayer — the three dominant all-time favorites by both count and total time — all sit below the dataset-wide average skip rate of 5.25%** (2.85%, 2.86%, 3.15% respectively), reinforcing that heaviest rotation correlates with lowest abandonment.
- **Ed Sheeran is a clear outlier at the top of this list (6.79%)**, the only top-20 artist skipped more often than the dataset average — a genuine anomaly worth noting rather than a small-sample artifact, since this list is restricted to high-play-count artists by construction.
- All differences within this group are modest in absolute terms (1.6%–6.8%) — best framed as "consistently low-skip favorites with small relative variation," not as any artist being frequently skipped in an absolute sense.

## Stage 5 — Skip Rate Over Time — Data Quality Finding

Grouping `skipped` by year initially suggested a dramatic, implausible pattern: **2018–2021 show a literal 0% skip rate across tens of thousands of plays each year**, with 2017 nearly as low (0.05%), while 2015 shows an implausibly high 78.7%.

**This was investigated and confirmed to be a data tracking issue, not real behavior.** Checking the `fwdbtn` rate (percentage of plays ending via forward button) per year shows people were still pressing forward at substantial, consistent rates throughout 2018–2021 (45.0%, 40.6%, 33.3%, 30.4%) — meaning skip-like behavior clearly continued as normal. The `skipped` field itself was not being populated correctly during this window, most likely due to changes in Spotify's export format over time.

**Conclusion:** the `skipped` column is only reliable for roughly **2016 and 2022–2024** in this dataset. Any year-over-year skip-rate analysis should exclude 2013–2015 (too small a sample) and 2017–2021 (field not populated) explicitly, rather than treating the raw yearly averages at face value.

**A more reliable long-term proxy — `reason_end == 'fwdbtn'` rate — is tracked consistently across the entire dataset** and shows a clear declining trend:

| Year | fwdbtn rate |
| ---- | ----------- |
| 2017 | 52.36%      |
| 2018 | 45.01%      |
| 2019 | 40.56%      |
| 2020 | 33.33%      |
| 2021 | 30.36%      |
| 2022 | 30.32%      |
| 2023 | 20.04%      |
| 2024 | 17.72%      |

This decline lines up with other findings from the time-trends section: fewer total plays, longer average play duration, and greater artist diversity per play — together painting a consistent picture of listening becoming more deliberate and less skip-heavy over time, even though the `skipped` field itself can't confirm this directly across the full period.

## Definitive Findings

1. **`skipped` reflects play duration, not button choice** — established in the data understanding phase and reconfirmed throughout this section.
2. **Shuffle mode is used in ~74.5% of plays and correlates with a modestly higher skip rate** (5.57% vs. 4.32%).
3. **`appload`-started plays have the highest reliable skip rate (15.07%)**; naturally-continued (`trackdone`-started) plays have the lowest (2.26%).
4. **Favorite artists (by play count) are skipped less than the dataset average**, with The Strokes lowest overall and Ed Sheeran a notable outlier on the high side.
5. **The `skipped` field is unreliable for 2017–2021 due to a data tracking gap** — a genuine data-quality limitation identified during analysis. The `fwdbtn` rate serves as a reliable substitute across the full time range and shows a clear declining trend since 2017, consistent with the broader "fewer, longer, more deliberate plays over time" narrative established in earlier sections.
