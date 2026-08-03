# Capability continuity skill

Use this repository skill whenever prose assigns an action, perception, movement, tool use, access path, or physical result to a character or system.

Its purpose is to stop narrative shorthand from silently giving a remote intelligence a body, giving a fixed installation mobile reach, or letting an actuator use tools and senses it has never established.

## The provenance question

For every consequential verb, ask:

1. **Who decides?** The intelligence that selects, models, authorizes, rejects, or evaluates the action.
2. **Who communicates?** The system carrying instructions, telemetry, or results.
3. **Who senses?** The camera, sensor, person, or machine that can actually observe the relevant evidence.
4. **Who actuates?** The body, arm, wheel, tool, valve, winch, or other mechanism that physically changes the world.
5. **Is every link present in this scene?** A capability established elsewhere does not teleport into the current location.

Decision credit and physical grammar are separate. A remote intelligence may design the operation and remain its intellectual author, but the sentence must name the actuator that wraps, cuts, lifts, aligns, tightens, carries, or installs.

## Capability classifications

- **Remote intelligence:** may compute, communicate, design, direct, prioritize, simulate, evaluate telemetry, and change software through established routes. It cannot perform an unmediated physical verb.
- **Embodied mobile system:** may perform only actions supported by its established body, tools, load limits, sensors, location, and current damage state.
- **Fixed installation:** may act only through its installed sensors and actuators. It cannot follow a convoy or observe beyond its telemetry.
- **Distributed intelligence:** must name which local instance, machine, or established actuator performs a physical action.
- **Person:** physical presence still requires scene placement, access, tools, and feasible reach.

The current capability registry is `continuity/capability-map.json`.

## Required check

Before accepting a chapter:

1. Extract every physical, sensory, access, and movement claim, including implied actions hidden inside shorthand such as “Patch installed the plate.”
2. Resolve the grammatical subject and any pronoun carrying that subject into the next sentence.
3. Trace the action through the capability registry and the bodies actually present in the scene.
4. Classify the result:
   - **PROVEN:** the subject has the required body, tool, sense, location, and current capacity.
   - **MEDIATED:** a remote or fixed intelligence directs the action and the sentence names the capable actuator.
   - **CAPABILITY BREAK:** no established provenance path can perform the verb as written.

## Minimum repair

When a capability break appears:

1. Preserve the decision-maker's agency and the established physical cast.
2. Reassign only the physical verb to the actuator already present.
3. Name remote direction or telemetry only where needed for clarity.
4. Do not invent a body, drone, manipulator, local copy, vehicle, sensor, or travel event merely to preserve shorthand.
5. Repair downstream canon and continuity summaries that repeat the false embodiment.

Example pattern:

```text
CAPABILITY BREAK:  Patch aligned the plate.
MEDIATED REPAIR:   Under Patch's direction, the healthy crawler aligned the plate.
```

## Automation boundary

`scripts/capability-check.py` is a conservative regression guard. It loads remote-only actors from `continuity/capability-map.json`, flags direct physical predicates, and follows simple pronoun carryover. Its self-tests prove that it distinguishes mediated action from unmediated embodiment.

The script cannot understand every literary verb. The authoring agent must perform the semantic provenance pass above; the script prevents already-known embodiment leaks from returning.
