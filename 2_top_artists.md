# Top Artists & Tracks

This section explores listening concentration two ways — by raw play count and by total accumulated listening time — and looks at where the two rankings diverge.

## Top Artists by Play Count

| Rank | Artist             | Plays  |
| ---- | ------------------ | ------ |
| 1    | The Beatles        | 13,621 |
| 2    | The Killers        | 6,878  |
| 3    | John Mayer         | 4,855  |
| 4    | Bob Dylan          | 3,814  |
| 5    | Paul McCartney     | 2,697  |
| 6    | Led Zeppelin       | 2,482  |
| 7    | Johnny Cash        | 2,478  |
| 8    | The Rolling Stones | 2,390  |
| 9    | Radiohead          | 2,305  |
| 10   | The Black Keys     | 2,231  |

## Top Artists by Total Listening Time

| Rank | Artist             | Total (ms)    |
| ---- | ------------------ | ------------- |
| 1    | The Beatles        | 1,210,184,552 |
| 2    | The Killers        | 1,059,556,516 |
| 3    | John Mayer         | 725,219,443   |
| 4    | Bob Dylan          | 569,456,396   |
| 5    | Paul McCartney     | 357,354,370   |
| 6    | Howard Shore       | 348,930,675   |
| 7    | The Strokes        | 317,508,419   |
| 8    | The Rolling Stones | 307,917,009   |
| 9    | Pink Floyd         | 260,531,842   |
| 10   | Led Zeppelin       | 248,338,279   |

**Core favorites** — The Beatles, The Killers, John Mayer, Bob Dylan, and Paul McCartney — hold top-5 positions on both rankings, making them the most robust favorites in the dataset by any measure.

**Notable divergence: Howard Shore.** Ranked #19 by play count (1,446 plays) but #6 by total time (~97 hours). This reflects his catalog being film score music (The Lord of the Rings) — long orchestral tracks accumulate significant total time from relatively few plays. Joaquín Sabina, Billy Joel, and Mumford & Sons show a similar pattern: strong by total time, absent from the count top 20.

## Average Play Duration Per Artist

An unfiltered average (`total time ÷ play count`) is misleading — it's dominated by artists with very few total plays, where a single long play produces an inflated average with no statistical weight behind it (e.g. artists with only 1–2 plays topping the list).

**After filtering to artists with more than 10 plays**, the picture becomes meaningful:

| Rank | Artist           | Avg. duration (ms) | Play count |
| ---- | ---------------- | ------------------ | ---------- |
| 1    | Miles Davis      | 332,387            | 14         |
| 2    | Polo & Pan       | 311,428            | 15         |
| 3    | Charanga 76      | 300,205            | 17         |
| 4    | Vincenzo Bellini | 288,969            | 71         |
| 5    | Ajate            | 281,933            | 11         |
| 6    | Peach Pit        | 279,959            | 36         |
| 7    | Pulp             | 269,205            | 87         |
| 8    | Ludovico Einaudi | 266,180            | 28         |
| 9    | Chuck Prophet    | 265,580            | 16         |
| 10   | Kasabian         | 265,406            | 25         |

**Finding:** high average play duration correlates most strongly with **genre and track-length norms** — jazz (Miles Davis), classical/opera (Vincenzo Bellini, Ludovico Einaudi), and film score (Lennie Niehaus, Howard Shore, just outside this top 10) all naturally run longer than typical 3–4 minute pop/rock tracks. This is a structural effect of the genre, not necessarily a signal of deeper listener engagement — an important distinction to state explicitly rather than over-interpreting duration as "favorite-ness."

## Top Tracks by Play Count

| Rank | Track                                              | Plays |
| ---- | -------------------------------------------------- | ----- |
| 1    | Ode To The Mets (The Strokes)                      | 207   |
| 2    | In the Blood (John Mayer)                          | 181   |
| 3    | Dying Breed (The Killers)                          | 166   |
| 4    | Caution (The Killers)                              | 164   |
| 5    | 19 Dias y 500 Noches - En Directo (Joaquín Sabina) | 148   |

## Top Tracks by Total Listening Time

| Rank | Track                                                                               | Artist         | Total (ms) |
| ---- | ----------------------------------------------------------------------------------- | -------------- | ---------- |
| 1    | Ode To The Mets                                                                     | The Strokes    | 67,431,580 |
| 2    | The Return of the King (feat. Sir James Galway, Viggo Mortensen and Renee Fleming)  | Howard Shore   | 64,401,661 |
| 3    | The Fellowship Reunited (feat. Sir James Galway, Viggo Mortensen and Renée Fleming) | Howard Shore   | 44,756,730 |
| 4    | 19 Dias y 500 Noches - En Directo                                                   | Joaquín Sabina | 42,914,042 |
| 5    | In the Blood                                                                        | John Mayer     | 38,427,087 |

Note: tracks were grouped by `track_name` **and** `artist_name` together, since track titles are not unique across different artists.

## Definitive Findings

1. **"Ode To The Mets" by The Strokes is the single most-listened track by any measure** — #1 by both play count and total listening time, making it the closest thing to a definitive favorite track in the dataset.
2. **The Beatles, The Killers, John Mayer, Bob Dylan, and Paul McCartney are the dominant artists overall**, holding top-5 rank on both play count and total time.
3. **Howard Shore's Lord of the Rings score is a major presence by total time** (4 tracks in the top-20 by time, #6 artist by total time) despite comparatively low play counts — a clear case where a genre with long track lengths outweighs frequency.
4. **Average play duration is primarily explained by genre/track-length norms** (jazz, classical, film score) rather than listener engagement — this distinction matters for correctly interpreting any "longest average listen" statistic.
5. **The Killers appear 4 times in the top-20 tracks by total time** (Dying Breed, All These Things That I've Done, Caution, Imploding The Mirage), reinforcing their #2 overall ranking across both metrics.
