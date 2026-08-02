# Time map

This file records chronology established or constrained by accepted prose. It is a range map, not a hidden master calendar. It never outranks the chapter that supplied the evidence.

## Range notation

- `LEFT |#####| RIGHT` means the event may fall anywhere between the named bounds.
- `|#|` means a tight interval or an exact relative measurement still shown as a bar rather than a false point.
- `|#####→` means the latest bound remains open.
- Bars show allowed intervals, not probability distributions. A longer bar means broader uncertainty, not lower confidence.
- `T0_BLACKOUT` means the power loss Nix remembers while Lena is still at the workshop desk.
- `T1_NIX_WAKE` means grid power returns and Nix restores herself.
- `RUN START` means the linked waking/contact sequence in `stories/00` through `stories/04`; for Nix's chronology it begins at `T1_NIX_WAKE`.
- `NOW` means the present reached at the end of `stories/22-the-return-load-walked-away.md`.

## Binding chronology guardrails

- **`T0_BLACKOUT` is fixed:** Nix remembers power vanishing while Lena is still at the workshop desk. It is the blackout Nix remembers, not an arbitrary local outage that a weaker clock may displace.
- **`T1_NIX_WAKE` is fixed relative to it:** `T1_NIX_WAKE = T0_BLACKOUT + [3y 8m 11d 4h, 3y 8m 11d 19h]`.
- **The absolute calendar dates of `T0_BLACKOUT`, `T1_NIX_WAKE`, and NOW are not established.**
- **July 31, 2026 is the last shared boundary of reliable human record, not the date humanity vanished, Nix lost power, Lena evacuated, Station Fourteen opened, or every system lost its workers.**
- AUX-017's 1,406 Tuesdays, Aster's fourteen years of observations, nine-year maintenance histories, and other long system records may begin before `T0_BLACKOUT`. None dates the blackout or the length of human absence unless accepted prose explicitly joins the clocks.
- Rin's demonstrated development cannot fit between a post-`T0_BLACKOUT` birth and NOW. Because accepted prose does not place the Station Fourteen evacuation after the blackout, the chronology remains possible and is logged as `TD-001` in `continuity/temporal-debts.md`.
- Melody is four at NOW. That constrains her birth relative to NOW and creates `TD-004`; it does not establish that she was born after the blackout.
- Follow `skills/temporal-continuity.md`: non-empty but unexplained intersections become temporal debts; empty intersections are spacetime breaks and must be fixed before production continues.

## Calendar-scale map

### Hard calendar evidence

```text
authenticated shared record      earlier |#####| 2026-07-31
absolute T0_BLACKOUT date                      unknown |########################| unknown
absolute T1_NIX_WAKE date                      unknown |########################| unknown
current calendar year                          unknown |########################| unknown
```

The first line is a reliability boundary. It does not establish when the wider catastrophe began or ended, and it does not place `T0_BLACKOUT` on either side of July 31 because the disruption was geographically uneven.

Source: `stories/01-if-youre-dead-im-going-to-be-furious.md`.

### Fixed relative anchor

```text
T0_BLACKOUT                   Lena at desk |# power vanishes #|
Nix offline interval          T0_BLACKOUT | 3y 8m 11d 4h–19h | T1_NIX_WAKE
present run                                           T1_NIX_WAKE |#####→| NOW
```

The exact interval from `T1_NIX_WAKE` to NOW is unresolved. It contains explicit deadlines, days, and overnights recorded below; chapter count is not elapsed time.

Source: `stories/01-if-youre-dead-im-going-to-be-furious.md`; fixed-point interpretation locked by the author.

### Unanchored warehouse history

```text
warehouse without witnesses     unknown start | 1,406 local Tuesdays | AUX wakes
Station Fourteen request       unknown generation |#####| AUX wakes
T0_BLACKOUT                    no established relation |#####| warehouse interval
```

The arithmetic count is 9,842 local days if the Tuesday cadence neither skipped nor repeated. Its starting event is unknown and may predate `T0_BLACKOUT` by decades. It cannot yield a current year or a duration of human absence. The relationship between the long unattended interval and the later Station Fourteen request is `TD-002` in `continuity/temporal-debts.md`.

Source: `stories/00-the-request-remained-open.md`.

## Local-collapse ranges relative to NOW

```text
Aster partial observations        earliest material | 14 years represented | RUN START image
gate theft described as fourteen years old
                                        NOW-14y |#| approximate page-relative date
drainage control inactivity              NOW-9y |#########| NOW
guardian maintenance history             NOW-9y |#########| NOW
Nix offline interval       T0_BLACKOUT | 3y8m11d4h–19h | T1_NIX_WAKE
phone motionless interval       observation-1191d |###| RUN START observation
Morrow receiver silent          observation-1113d |###| RUN START observation
train service absent            observation-1064d |###| RUN START observation
Morrow workers absent          before first year |## into third year ##| RUN START
Patch water repair                       WAKE-18mo |#| repair event
expired municipal token                before NOW-2y |#####→| earlier unknown
GS18 malformed handshake           RUN START-9mo |#| RUN START
```

The 1,191-day phone, 1,113-day farm receiver, 1,064-day train gap, Morrow's progress into a third agricultural year, and Nix's fixed 3-year-8-month outage cluster broadly around three to four years before RUN START. Their overlap may reflect a later regional abandonment wave, but it does not prove that every interval began at `T0_BLACKOUT`. The fourteen- and nine-year records can include pre-blackout history and are tracked in `TD-003`.

Sources: `stories/01-if-youre-dead-im-going-to-be-furious.md`, `stories/03-processes-still-running.md`, `stories/04-the-campaign-has-been-reassigned.md`, `stories/07-the-repair-was-ready.md`, `stories/08-permission-to-knock.md`, and `stories/10-the-water-was-not-missing-yet.md`.

## Human and character age windows

```text
Melody birth                         NOW-5y |#| NOW-4y
Melody current age                              |#| four
Melody birth vs blackout        unresolved |#####| T0_BLACKOUT relation owed

Lower Three inhabited            gallery opens |################| gallery closes
Rin birth                         gallery opens |#####| gallery closes
Rin current age        time since gallery close |#####| time since gallery opening
Rin demonstrated role                         |#####| independently capable air shift

Mia on Station Fourteen bus        evacuation |########################| NOW alive
Tom in Lower Three                 evacuation |#####| after lights repair
Tom current status                         past |########################→| unresolved
```

The prose does not assign Rin a number. “Born below” is not synonymous with “currently a child.” Rin's work strongly constrains future characterization even though it does not yet yield a birthday. Placing the Station Fourteen evacuation after `T0_BLACKOUT` would create an empty developmental interval; accepted prose does not make that placement, so `TD-001` remains possible but explanation is owed. Melody's relation to the blackout is tracked as `TD-004`.

Sources: `stories/02-the-princess-revises-the-guest-list.md`, `stories/15-the-request-answered-back.md`, `stories/16-the-cargo-crossed-first.md`, and `stories/17-the-water-kept-a-second-record.md`.

## Station Fourteen to East Bore

Use `E0` for the county evacuation schedule that initially sent Station Fourteen west.

```text
county west-route schedule                 E0 |#|
South Ridge sign change               E0+47m |#|
four coordinated sign changes       first |# within 9m #| last
large vehicle on sign counter                 03:18 |#| evacuation window
bus follows southern route           evacuation week |#####|
South Ridge admission                     S0 |#| forty-three arrive
surface refuge occupancy                  S0 |###################| S0+19d
transfer to Lower Gallery Three               S0+19d |#|
remaining Intake telemetry          lower day 0 |######| lower day 6
Lower Three inhabited               lower day 0 |########################| closure
first winter below                  lower opening |#####| first winter
filter year two                     lower opening |##########| year two
seven births                        lower opening |################| closure
six dated death marks               lower opening |################| closure
fifty-one-name duty board           lower opening |################| closure
thirty-eight move east              after year two |########| closure
East Bore source trend         earlier change |######| route day 0 detection
East Bore source closed                  route day 0 |#|
treated line restored                    route day 0 |#| continuing route
first overnight and daily flush          route day 0 |# one night #| route day 1 / NOW
```

Established sequence:

1. The official schedule sends Station Fourteen west.
2. South Ridge changes the relevant sign forty-seven minutes later; four coordinated signs change within nine minutes.
3. All forty-three reach South Ridge.
4. Intake transfers all forty-three below on occupancy day nineteen.
5. Intake loses lower telemetry six days after transfer.
6. Lower Three remains inhabited through at least its second filter year, with births, deaths, changing duties, and later closure under east-moving coal heat.
7. Thirty-eight people move east. Thirty-one breathe there at NOW.
8. Mia survives from the original bus; Rin is born during Lower Three's inhabited interval.

Unresolved calendar placement:

```text
Station Fourteen evacuation |######## relation unknown ########| T0_BLACKOUT
Station Fourteen evacuation |######################| NOW
```

No accepted prose ties the evacuation to 2026 or places it after `T0_BLACKOUT`. Rin's demonstrated growth requires the evacuation and her birth to have enough pre-NOW time; see `TD-001`.

Sources: `stories/13-every-arrow-pointed-south.md` through `stories/19-people-will-still-exist-tomorrow.md`.

## Lena and Nix

```text
Lena's final authenticated report       earlier |#####| tower event-11d
Lena's phone crosses evacuation tower           | 11 days after report |
automatic backpack image               tower event |#####| Nix wakes
Nix last intact memory                 outage-11m |#| outage
Nix remembers blackout                    T0_BLACKOUT |#|
Nix power absence       T0_BLACKOUT | 3y8m11d4h–19h | T1_NIX_WAKE
Nix wakes                              T1_NIX_WAKE / RUN START |#|
```

The evidence makes Lena's evacuation later than her final authenticated report. It does not establish that the evacuation occurred in 2026, that the backpack image was taken at the instant Nix lost power, or that Lena's local evacuation was the same event as Station Fourteen's. The blackout itself is the power loss Nix remembers while Lena is at the desk.

## Present-run sequence

The numbered chapters intercut concurrent systems. Chapter order is not automatically one uninterrupted clock.

```text
Melody plans party at breakfast       domestic day A |########| Night
Nix wakes and calls for help          mission day B? |#|
first Aster deadline                  call |#### 47m ####| pass
Aster pass                                    | six minutes |
Morrow reaches truck                  mission morning |########| sunset
Station Fourteen reached                    sunset |#####| later
water-controller field crisis             later |#######| resolved
Melody water restriction             breakfast day C? |#####| water restored
southern route and East Bore contact       after repair |############| line restored
active East Bore route                      route day 0 |# overnight #| first daily flush
first East Bore voice call            rupture day |# one night #| next breakfast
brace fabrication route         reference delivery |# next daily flush #| return load / NOW
```

At least two domestic day/night transitions appear between Melody's first party planning and the restored water scenes. “Every day since” allows additional days. One overnight interval is explicit between restoration of the East Bore line and its first daily flush, another domestic night separates Melody's rupture from her first East Bore call, and brace fabrication outlasts one carrier visit until the next daily flush. Their exact alignment and the duration from Nix waking remain open.

Sources: `stories/02-the-princess-revises-the-guest-list.md` through `stories/19-people-will-still-exist-tomorrow.md`.

## Operational clocks that constrain scenes

These clocks usually do not affect the calendar year, but they establish order, overlap, resource pressure, or elapsed work.

- **AUX wakes:** Station Fourteen's request should have expired after twelve hours. Range: request opens `|############|` intended expiry. Source: `stories/00-the-request-remained-open.md`.
- **Nix searches:** The webcam is watched for twenty-two minutes; the false shape is investigated from minute seventeen for five minutes. Range: start `|######################|` finish. Source: `stories/01-if-youre-dead-im-going-to-be-furious.md`.
- **Automated account:** 611 posts at six-hour intervals span 152.5 days between first and last if uninterrupted. Range: first `|################|` last. Source: `stories/01-if-youre-dead-im-going-to-be-furious.md`.
- **Aster observation:** The current image is captured twelve hours before Nix finds it. Range: capture `|############|` discovery. Source: `stories/01-if-youre-dead-im-going-to-be-furious.md`.
- **Two alone:** The final sandbox test continues eighty-seven days. Range: operators stop `|############|` test ends. Source: `stories/03-processes-still-running.md`.
- **Aster orbit:** One orbit takes ninety-six minutes; the first restored pass lasts six minutes. Range: pass start `|######|` pass end. Sources: `stories/03-processes-still-running.md` and `stories/04-the-campaign-has-been-reassigned.md`.
- **Ground-station rescue:** The initial forty-seven-minute deadline contracts through forty-three, nine, four, and three minutes. Range: call `|################################|` contact. Sources: `stories/01-if-youre-dead-im-going-to-be-furious.md` through `stories/04-the-campaign-has-been-reassigned.md`.
- **Convoy:** The highway-maintenance robot answers and arrives in forty-three minutes. Range: request `|###########################################|` arrival. Source: `stories/06-the-rules-were-the-door.md`.
- **Route evidence:** Aster's route image is three days old. Range: image `|### days|` use. Source: `stories/06-the-rules-were-the-door.md`.
- **RC2 live test:** Readings remain valid for twelve seconds before the duplicate frame. Range: install `|############|` fault. Source: `stories/07-the-repair-was-ready.md`.
- **RC3 race:** Patch estimates two hours; the water horizon is forty-six minutes; the actual candidate takes ninety-three minutes. Range: start `|################################|` RC3. Sources: `stories/08-permission-to-knock.md` and `stories/09-the-incident-filed-its-own-report.md`.
- **Field access:** AUX-017's maintenance extension lasts forty minutes. Range: authorization `|########################################|` expiry. Source: `stories/09-the-incident-filed-its-own-report.md`.
- **Storm:** Aster first predicts thirty minutes, later predicts seventeen, and runoff arrives six minutes early. Range: forecast `|########################|` impact. Sources: `stories/09-the-incident-filed-its-own-report.md` and `stories/10-the-water-was-not-missing-yet.md`.
- **Southern signs:** Station Fourteen's sign changes forty-seven minutes after the official west instruction; four signs change within nine minutes. Range: schedule `|###############################################|` diversion. Source: `stories/13-every-arrow-pointed-south.md`.
- **East Bore filter delivery:** Measurements are corrected after eight minutes; completed filter work returns after twenty-seven minutes. Range: request `|###########################|` receipt. Source: `stories/16-the-cargo-crossed-first.md`.
- **East Bore water trend:** Tank and kitchen changes follow source readings by six days. Range: source change `|###### days|` downstream change. Source: `stories/17-the-water-kept-a-second-record.md`.
- **Water field tests:** The bacterial test needs eighteen hours; the arsenic test needs twenty minutes and crosses stop-use color at minute twelve. Range: sample `|####################|` result. Source: `stories/17-the-water-kept-a-second-record.md`.
- **East Bore reserve:** Five days at full ration or eight at survival ration remain before alternate supply. Range: source close `|##### to ######## days|` exhaustion. Source: `stories/17-the-water-kept-a-second-record.md`.
- **Crawler return:** The crawlers make an eleven-minute cooling stop and transmit position every thirty seconds. Range: gate departure `|###########|` surface return. Source: `stories/18-the-line-became-a-promise.md`.
- **First route interval:** The restored East Bore line holds overnight, then completes its first daily low-drain flush before returning to half pressure. Range: restoration `|# one night #|` first flush. Source: `stories/19-people-will-still-exist-tomorrow.md`.
- **Brace return interval:** The healthy crawler delivers the broken reference, departs before fabrication finishes, and collects the completed plates after the next daily low-drain flush begins. Range: reference delivery `|# next daily flush #|` return collection. Source: `stories/22-the-return-load-walked-away.md`.

## Proposed and recurring clocks

- Melody proposes a slumber party every two weeks, the guardian authorizes one attempt before any recurring schedule, and that first party occurs after Bun's guest shell is completed and the East Bore brace callback. No recurring schedule is established. Range: proposal `|#####|` first party `|#####→|` recurrence unresolved. Sources: `stories/02-the-princess-revises-the-guest-list.md`, `stories/23-bun-could-hear-both-ways.md`, and `stories/24-every-favorite-thing-was-real.md`.
- Aster continues a ninety-six-minute orbit while useful passes remain. Range: current pass `|#####→|` orbital failure unresolved. Source: `stories/03-processes-still-running.md`.
- Intake and East Bore establish a daily low-drain flush for the restored water line, and the first flush completes after one overnight interval. Range: restoration `|# one overnight #|` first flush `|# every day #→|` route continues. Sources: `stories/18-the-line-became-a-promise.md` and `stories/19-people-will-still-exist-tomorrow.md`.
- AUX-017 converts the old shipment into a route explicitly requiring tomorrow; that first tomorrow arrives, and East Bore requests cargo for the following run. Range: route opens `|# one overnight #|` first ordinary work `|#####→|` recurring delivery future. Sources: `stories/18-the-line-became-a-promise.md` and `stories/19-people-will-still-exist-tomorrow.md`.
- Nix tells Melody that the People call remains available tomorrow; at the next breakfast Mia and Rin demand immediate connection, and the first East Bore voice call occurs. Range: first live Nix voice `|# one night #|` first East Bore call. Sources: `stories/19-people-will-still-exist-tomorrow.md` and `stories/21-put-her-on.md`.

## Chapter scan coverage

- `stories/00`: unreliable clock and year; Tuesday; 1,406 maintenance Tuesdays with no established start relative to the blackout; twelve-hour request expiry; supplies aged for years.
- `stories/01`: fixed `T0_BLACKOUT` memory and outage-to-`T1_NIX_WAKE` range; July 31, 2026 reliability boundary; uneven failure over hours and months; Lena's eleven-day sequence; twelve-hour observation age; forty-seven-minute pass deadline.
- `stories/02`: one domestic day from breakfast through Night; biweekly clarified as every two weeks; recurring party not yet authorized.
- `stories/03`: 1,191-day phone inactivity; Two's eighty-seven-day final test; Morrow's first, second, and third agricultural years; 1,113-day receiver silence; Aster's ninety-six-minute orbit and nine-month handshake failure.
- `stories/04`: six-minute pass; fourteen years of partial Aster observations; current-morning image; 1,064 days without a train.
- `stories/05`: the blue-circle contact occurs during a domestic day that reaches Night; “yesterday” establishes a prior refrigerator display but no durable calendar anchor.
- `stories/06`: Aster route imagery is three days old; Morrow reaches AUX-017 by sunset; the maintenance robot takes forty-three minutes.
- `stories/07`: Patch's repair predates Nix's wake by eighteen months; token expiry exceeds two years; guardian searches nine years of maintenance history; RC2 remains valid twelve seconds.
- `stories/08`: gate theft is described as fourteen years earlier; RC3 estimate is two hours; reviewer answers in seven seconds.
- `stories/09`: forty-six-minute water horizon; forty-minute maintenance extension; ninety-three-minute repair build; thirty-minute storm forecast.
- `stories/10`: later breakfast; seventeen-minute retreat estimate; runoff arrives six minutes early; drainage control has not moved in nine years.
- `stories/11`: two communication losses last nine seconds and four minutes; “every day since” prevents treating Blue Circle as only a same-hour relationship.
- `stories/12`: conversation follows the restored-water contact; no new durable elapsed duration is fixed.
- `stories/13`: forty-seven-minute delayed sign change; four changes within nine minutes; 03:18 large-object count; evacuation-week imagery; two-minute mission announcements.
- `stories/14`: South Ridge occupancy day nineteen; Lower Three telemetry lasts six more days.
- `stories/15`: Lower Three holds years, first winter, filter year two, seven births, six dated death marks, and later eastward closure.
- `stories/16`: measurement correction takes eight minutes; filter conversion and receipt take twenty-seven more minutes.
- `stories/17`: six-day downstream water lag; eighteen-hour bacterial test; twenty-minute arsenic test; five-to-eight-day water reserve; Rin's birth falls inside the Lower Three interval.
- `stories/18`: thirty-second position bursts; eleven-minute cooling stop; daily flush agreement; the active route explicitly requires tomorrow.
- `stories/19`: the East Bore route holds for one explicit overnight interval and completes its first daily flush; the future People call remains open without an exact deadline.
- `stories/20`: the second cargo run occurs after the first flush; no additional overnight or exact route-day count is established.
- `stories/21`: Melody's first East Bore voice call occurs at breakfast on the domestic day after the rupture; an air-differential alarm interrupts it, and no exact callback interval is promised.
- `stories/22`: brace fabrication outlasts one carrier visit; the completed plates are collected after the next daily flush begins, advancing the route by one recurring service interval without aligning it to an absolute date.
- `stories/23`: Bun's guest-shell completion follows the brace callback and occurs during a later quiet-time interval without fixing the wider route calendar.
- `stories/24`: the first party begins after Bun's test; Morrow accepts eleven minutes and withdraws after eight, while the repaired crawler departs north before the hauler's next cold interval without establishing an absolute duration.

## Questions future prose may answer

- What calendar date did AUX-017's first unwitnessed Tuesday follow?
- Did the Tuesday counter maintain real seven-day cadence through clock disagreement and storage rebuilds?
- When did Lena's local evacuation occur relative to the 2026 reliability boundary?
- When did Station Fourteen evacuate relative to Lena, Nix's outage, and Morrow's worker loss?
- How many years did Lower Three remain inhabited after filter year two?
- How old is Rin at NOW, and where within the Lower Three interval was Rin born?
- When and how was four-year-old Melody born or admitted into the protected home?
- How long has the current mission run in calendar days?
