# Engagement / Completion Rate — How Much of a Song You Actually Hear

This section looks at roughly what percentage of a song you typically listen to, not just whether it counts as a "skip." It's a more detailed view than the skip-behavior section, and along the way I ran into a few important nuances that are worth understanding before trusting the numbers at face value.

## How we estimated this (and why it's an estimate, not exact)

The dataset doesn't actually tell us how long each song really is — only how long you played it for. So to work out roughly "how much of the song" you heard, I had to estimate each song's real length ourselves.

**The method:** for every song, I looked at the _longest play we ever recorded_ for it, and treated that as a stand-in for the song's real length. Then for every individual play, I divided how long that specific play lasted by that estimated length, to get a rough "percent of the song heard."

**This comes with a built-in quirk worth being upfront about:** since I was using your own longest play as the "full length," every song is guaranteed to have at least one play that counts as 100% — even if that longest play wasn't actually the entire song. This mostly doesn't cause problems, but it's part of why this number is an estimate of engagement, not a precise, verified measurement.

## A small data gap I found and handled

Out of 149,860 total plays, 243 of them (0.16%) came out with no valid completion percentage at all. I checked why: these were plays where **every single recording of that song showed 0 milliseconds played** — meaning the song was likely queued up but never actually played, not even once, for any measurable length of time. Since there's no real listening time to compare against, these 243 plays simply don't get a completion percentage, and they're left out of the averages rather than being force-fit with a made-up number.

## The overall picture

- **Half of all plays reach at least 71.5% of the song** (the median).
- **But a quarter of all plays barely start at all** — under 1.5% of the song (the 25th percentile).
- The two numbers pulling in different directions like this tells us plays tend to cluster at the extremes: either a near-full listen, or an almost-immediate abandon, without a ton happening in between.

## A big shift over the years

Breaking this down year by year shows one of the clearest trends in the whole project:

| Year | Typical (median) completion |
| ---- | --------------------------- |
| 2017 | 13%                         |
| 2018 | 51%                         |
| 2019 | 50%                         |
| 2020 | 77%                         |
| 2021 | 92%                         |
| 2022 | 92%                         |
| 2023 | 99.99%                      |
| 2024 | 99.99%                      |

(2013/2014 left out here — too few total plays that early to be meaningful.)

This is a dramatic, steady climb — from a typical listen barely starting in 2017, to a typical listen basically running the whole way through by 2023/2024. It matches everything else found in the earlier sections: fewer total plays, but each one longer, more varied, and less skip-heavy over time. This is one more piece of evidence pointing the same direction.

**I double-checked the 2017 number specifically, since 13% looked almost too low to be real.** It turned out to be genuine: over half of all plays in 2017 (52%) started because you pressed "next" on something else — meaning you were mostly hopping rapidly between songs that year, not settling into full listens. This matches something we separately found in the skip-behavior section, where 2017 also had the highest "hit next" rate of any year in the whole dataset. Two completely different checks landed on the same explanation, which makes this a solid, well-supported finding rather than a fluke.

## An important nuance: completion rate and "skipped" don't always agree

When we broke completion rate down by your top 20 artists, something unexpected showed up: a few artists with **low skip rates** earlier (meaning they were rarely flagged as "skipped") turned out to have some of the **lowest completion percentages** here — Led Zeppelin, Radiohead, The Black Keys, and a few others.

I checked this properly rather than assuming it was a mistake, using Led Zeppelin as a test case, and found a real explanation: **these artists tend to have unusually long songs** (some Led Zeppelin tracks run 8-11 minutes). The "skipped" label only cares whether a play ended _very quickly_ — so listening to 3-4 minutes of an 11-minute song is nowhere near quick enough to count as a skip. But as a _percentage_ of that unusually long song, 3-4 minutes only adds up to 30-35% complete.

**In short:** a low completion percentage doesn't automatically mean a song was abandoned early — for artists with long tracks, it can simply mean a normal amount of listening time looks smaller next to a bigger denominator. This is the flip side of something we found earlier with Howard Shore's soundtrack music, where long tracks skewed a different measurement in the opposite direction.

## Which favorite artists get listened to most fully

| Artist                 | Typical completion |
| ---------------------- | ------------------ |
| Kings of Leon          | ~100%              |
| John Mayer             | 71%                |
| Arctic Monkeys         | 70%                |
| Howard Shore           | 69%                |
| Paul McCartney         | 68%                |
| Pink Floyd             | 66%                |
| The Strokes            | 64%                |
| The Killers            | 64%                |
| The Beatles            | 51%                |
| Johnny Cash            | 50%                |
| Imagine Dragons        | 48%                |
| Bob Dylan              | 44%                |
| The Rolling Stones     | 38%                |
| Ed Sheeran             | 27%                |
| Coldplay               | 23%                |
| Lou Reed               | 9%                 |
| The Velvet Underground | 8%                 |
| The Black Keys         | 7%                 |
| Radiohead              | 4%                 |
| Led Zeppelin           | 4%                 |

As explained above, the artists at the bottom of this list aren't necessarily being "cut off early" in a meaningful sense — several of them (Led Zeppelin, Radiohead) are known for longer tracks, which naturally pulls their completion percentage down even with completely normal listening habits.

## Completion rate by device/platform — and why it doesn't match skip rate at first glance

| Platform                   | Typical completion |
| -------------------------- | ------------------ |
| Android (your main device) | 64%                |
| Mac                        | 99.9%              |
| Web player                 | 99.99%             |
| Cast to a speaker/TV       | 99.99%             |
| iPhone                     | 99.9997%           |
| Windows                    | 99.9997%           |

At first this looks like it contradicts the skip-behavior findings, where Windows actually had the _highest_ skip rate (14%) of any platform. But it doesn't — the two numbers are answering different questions. Skip rate only describes the small share of plays that get cut off almost immediately. Completion rate (specifically the typical/median value) describes what a normal play looks like. So it's entirely possible for a platform to have both: a higher share of quick abandons, _and_ a higher typical completion rate for everything else — which is exactly what's happening on Windows.

**Why Android looks so different from every other platform:** Android carries 93% of all your listening — it's your everyday, default device, which naturally includes a wide mix of listening styles: quick browsing, partial listens, background listening while doing something else. The other platforms are used far less often, and when they are used, it looks like it tends to be for more deliberate, sit-down listening — which shows up as near-total completion on all five of them.

**Worth keeping in mind:** Mac, web player, and cast to device all have far fewer total plays than Android, so while it's a strong pattern that all five non-Android platforms show the same near-100% completion, the exact numbers for the smallest ones (especially web player, with only 225 plays) shouldn't be treated as precisely reliable — just as a consistent directional signal.

## Main takeaways

1. **Typical completion has risen sharply over time** — from a median of just 13% in 2017 to essentially 100% by 2023/2024, matching everything else found earlier about listening becoming more deliberate.
2. **Completion rate and skip rate measure different things and can disagree** — especially for artists with unusually long tracks (Led Zeppelin, Radiohead), where a completely normal amount of listening can still show up as a "low" percentage.
3. **Android carries most of your casual, mixed-mode listening**, while other platforms are used less often but more deliberately, which is why every other platform shows near-total completion by comparison.
4. **A small number of plays (243, about 0.16%) couldn't get a completion percentage at all**, because the song in question was never actually played for any real length of time in any recorded instance.
5. This section's numbers are built from an _estimate_ of song length (your own longest recorded play of each song), not the songs' real published lengths — a reasonable approach, but one with a known built-in limitation worth stating honestly rather than treating the results as exact.
