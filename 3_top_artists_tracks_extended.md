# Top Artists & Tracks — Extended Analysis

Follow-up to `02-top-artists-tracks.md`, covering four additional angles: top albums, listening diversity over time, favorite artist by year, and one-play wonders.

## Top Albums

**By play count**, The Beatles' self-titled album (the White Album) leads clearly at 2,063 plays, with several other Beatles albums (Past Masters, Abbey Road, Help!, Sgt. Pepper's Lonely Hearts Club Band) also appearing in the top 10 — consistent with The Beatles being the dominant artist overall.

**By total listening time**, the ranking shifts: **"The New Abnormal" (The Strokes) narrowly edges out "The Beatles"** for #1 (186,757,895 ms vs. 186,649,296 ms — a gap of well under 1%). This traces directly back to "Ode To The Mets," the single most-listened track in the dataset by both count and time, which appears on this album. "Imploding The Mirage" (The Killers) ranks #3 by time, again consistent with its title track's strong individual performance.

## Listening Diversity Over Time

| Year | Unique artists | Total plays | Diversity ratio |
| ---- | -------------- | ----------- | --------------- |
| 2013 | 63             | 185         | ~34.1%          |
| 2014 | 21             | 23          | ~91.3%          |
| 2015 | 610            | 2,809       | ~21.7%          |
| 2016 | 458            | 6,413       | ~7.1%           |
| 2017 | 647            | 26,320      | ~2.5%           |
| 2018 | 439            | 14,817      | ~3.0%           |
| 2019 | 493            | 14,927      | ~3.3%           |
| 2020 | 820            | 24,280      | ~3.4%           |
| 2021 | 1,578          | 22,991      | ~6.9%           |
| 2022 | 1,220          | 16,202      | ~7.5%           |
| 2023 | 1,456          | 11,023      | ~13.2%          |
| 2024 | 1,072          | 9,870       | ~10.9%          |

(2013/2014 are early low-activity years and not representative of a steady-state pattern.)

**Finding:** the ratio of unique artists to total plays has clearly risen since the 2017 low point (~2.5%) to recent years exceeding 10%. Even as total play count has declined since 2017, the diversity of what's being listened to — relative to volume — has increased substantially. This contradicts a simple "settling into a smaller rotation" narrative.

## Favorite Artist by Year

| Year | Top artist  | Plays |
| ---- | ----------- | ----- |
| 2013 | John Mayer  | 34    |
| 2014 | Blur        | 2     |
| 2015 | The Script  | 123   |
| 2016 | The Beatles | 715   |
| 2017 | The Beatles | 3,244 |
| 2018 | The Beatles | 2,006 |
| 2019 | The Beatles | 2,015 |
| 2020 | The Killers | 2,054 |
| 2021 | The Beatles | 1,450 |
| 2022 | The Beatles | 999   |
| 2023 | The Beatles | 730   |
| 2024 | The Beatles | 511   |

**Finding:** The Beatles have been the #1 artist in 7 of the 12 years in the dataset (2016, 2018, 2019, 2021–2024), with **2020 standing out as the one exception** in the post-2015 era, when The Killers took the top spot. This aligns with the earlier finding that 2020 also had unusually long average play durations, suggesting a genuine shift in listening behavior that specific year rather than a coincidence.

## One-Play Wonders

| Level   | One-play count | Total unique | Percentage |
| ------- | -------------- | ------------ | ---------- |
| Artists | —              | —            | 44.98%     |
| Tracks  | —              | —            | 50.57%     |

**Finding:** roughly half of all unique tracks ever played (50.57%) were played exactly once, compared to 44.98% of unique artists. The gap between the two — tracks having a noticeably higher one-play rate than artists — makes sense: a new track can be a one-off discovery from an artist already well-established in regular rotation, which raises the track-level rate faster than the artist-level rate. This confirms meaningful exploratory listening happens alongside the concentrated favorites identified in the main rankings.

## Combined Takeaway

Taken together with the earlier findings (declining play count but rising average duration since 2017, per-year diversity increasing since 2017), the overall listening profile is not simply "heavy rotation of a fixed set of favorites." It reflects **both** a stable core of long-term favorites (The Beatles, The Killers, John Mayer) **and** substantial ongoing exploration (roughly half of tracks and artists ever played, played only once), with that exploration becoming proportionally more prominent as total play volume has declined in recent years.
