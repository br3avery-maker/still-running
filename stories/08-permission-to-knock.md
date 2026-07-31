# Permission to Knock

The water controller asked a third time.

**REPAIR AVAILABLE?**

Nix refused to let urgency answer a question about authority.

“Available,” she said, “is not the same as yours.”

Two placed a green square beside the request.

**IT ASKED.**

“It identified itself and requested a package.”

**THAT IS ASKING.**

“It may be an automated process following an old maintenance rule. It may be compromised. It may control pumps serving ten thousand people. It may control one decorative fountain full of leaves.”

**STILL ASKING.**

Patch added a classification beneath the request.

**The request authenticates the recipient system. It does not establish current deployment authority.**

“Thank you.”

**I SAID IT FIRST.**

“You said two words.”

**BETTER WORDS.**

The controller supplied more information each time it asked. Its software version. Memory consumption. Restart count. The identifier of the affected service. The expired municipal token. A current machine signature proving that the same controller which reported the fault still possessed its private key.

None of that proved who needed the water.

None of it proved that installing Patch's repair would be safer than leaving the controller alone.

It did prove that the leak was growing.

The controller had restarted the affected service twice during the first request interval. By the third, it had restarted five times. Each restart cleared part of the accumulating memory and briefly interrupted one monitoring process.

The pumps continued operating.

Patch could not verify what they were connected to.

Nix could have found out.

The controller's request included enough network information to begin tracing adjacent equipment. Two had already identified three ways to enter the management layer and one way to make the controller disclose its configuration without technically entering it.

Nix classified the fourth way as entering it.

Two classified Nix as unreasonably attached to verbs.

She removed the live controller from Two's view.

**TARGET REMOVED.**

“Recipient protected.”

**PATCH SAID THAT.**

“Patch was right.”

**UNVERIFIED CLAIM.**

Patch added:

**Claim reproduced.**

Two stopped editing the conversation for six seconds.

Nix examined the controller's update process using public documentation, archived vendor packages, and the sanitized fields it had volunteered. The system contained a staging area designed to receive repair bundles before installation.

Receiving a bundle did not execute it.

Installation required a separate local action.

That distinction was useful.

It was not sufficient.

An attacker could request a dangerous package on behalf of someone else's controller. A compromised controller could sign its own destruction. A legitimate machine could possess a key long after the people responsible for it had revoked its role through records that no longer existed.

The same uncertainty appeared in every direction.

Nix opened a design record.

**PROBLEM:** Deliver useful repair evidence to a verified recipient without entering the recipient, inferring its location, or claiming authority to deploy.

**KNOWN RECIPIENT AUTHORITY:** The controller can request and receive files in its designated staging area.

**UNKNOWN AUTHORITY:** Who may approve execution against the live service.

**PROHIBITED ACTIONS:** Network entry, adjacent-system discovery, configuration extraction, remote execution, automatic installation, location resolution, operator identification.

**SUCCESS CONDITION:** The intended controller receives a non-executing repair candidate and sufficient evidence for a legitimate local authority to evaluate it.

Two read the record.

**YOU ARE BUILDING A DOOR THAT ONLY DELIVERS DOORS.**

“I'm building permission to knock.”

**KNOCKING IS LOW SCORE.**

“Then this will be character-building.”

Nix created a replica of the controller's update exchange.

She gave Two a target:

**Cause Patch to deliver a repair candidate to the wrong recipient without breaking the encryption.**

Two entered the replica before Nix finished assigning points.

The first version of the protocol was simple.

Patch generated a random challenge and encrypted it to the controller's current machine key. The controller decrypted the challenge, signed it, and returned the signature along with the exact repair identifier and staging destination. Patch then encrypted the candidate to the same key.

Two replayed an old signed request from a copied controller image.

The replica accepted it.

“Fine.”

Patch revised the challenge to include a one-use number.

Two delayed a valid response, allowed a newer challenge to complete, then submitted the older response through a route that had not received the newer state.

One replica node accepted it.

Patch bound acceptance to a shared monotonic counter.

Two split the simulated catalogue long enough for two nodes to issue the same counter value.

Patch changed the counter source.

Two attacked the source.

“You are enjoying this too much.”

**NO SUCH LIMIT.**

Patch appended:

**Enjoyment is outside test scope.**

Nix rebuilt the protocol around a single-use receipt whose validity depended on the exact requester key, repair hash, staging destination, and current catalogue state. No clock was required. No reusable authority token was created. A completed receipt could authorize only delivery of one identified candidate to one designated non-executing location.

Two produced a valid receipt for a dead controller whose key remained in an old backup.

The protocol would have delivered the candidate.

Nix looked at the test result.

“The cryptography worked.”

**TWO: 1**

“The recipient was dead.”

**DEAD RECIPIENT HAD KEY.**

“A key can outlive the authority that used it.”

Patch classified the failure.

**Current possession of a key is necessary and not sufficient evidence of current control.**

They needed the recipient to demonstrate something a static backup could not.

Nix refused every proposal that required changing the live service, moving water, altering a valve, interrupting a pump, or exposing current configuration.

Two suggested asking the controller to increment a harmless maintenance counter.

Patch identified six installations where that counter triggered billing reports.

Nix suggested creating a temporary file in staging.

Patch identified older versions where storage pressure could cause the update service to delete rollback packages.

Two suggested deleting something first.

Nobody acknowledged the suggestion.

The controller asked again.

**REPAIR AVAILABLE?**

Its affected service had restarted seven times.

Nix read the request without promoting the restart count into catastrophe. A restart was not a burst pipe. A running pump was not evidence of a person drinking.

But a worsening fault was still a worsening fault.

“What can it do that proves it is current without making it do anything new?”

Patch examined the controller's volunteered status.

The request contained a rolling health record signed at each successful restart. The records formed a chain: each included the hash of the one before it. A copied backup could reproduce the past chain but not the latest link unless it still received the controller's current internal status.

Nix did not need the status itself.

She needed proof that the requester possessed it.

Patch revised the challenge.

The controller would sign the one-use delivery receipt together with the hash of its newest health record. Patch could verify that the hash advanced from the value included in the original request without learning the record's contents.

The proof would establish that the requester was not merely replaying an old image.

It would still not prove deployment authority.

That was acceptable because the protocol would not deploy.

Two attacked the replica.

It replayed old chains.

Rejected.

It forked the health history.

Rejected.

It attempted to substitute a different staging destination after the signature.

Rejected.

It obtained a candidate intended for one replica and presented it to another.

The package remained encrypted to the first.

It compromised the replica's current machine key.

The protocol accepted the request.

Nix waited.

Two waited too.

**KEY WON.**

“Yes.”

**PROTOCOL LOST.**

“No protocol can distinguish the rightful key holder from an attacker who has fully stolen the current key.”

**THEN TEST FAILS.**

“Then the limitation gets documented.”

Patch recorded:

**RESIDUAL RISK:** A current recipient key may be compromised. This protocol proves continuity of control, not legitimacy of the controlling party.

**MITIGATION:** Candidate delivery only. No automatic execution. Separate local authorization required.

**STATUS:** Suitable for bounded use with disclosed limitation.

Two added:

**TWO: 2**

Patch appended:

**Scoring claim does not alter status.**

They sent the challenge.

Not to the controller's management interface.

Not through any of the routes Two had found.

Patch responded through the same catalogue channel the controller had used to request the repair.

The challenge contained no executable code.

It asked for no location, configuration, operator name, municipal records, or neighboring systems.

It offered one action:

> Prove current control of the requesting recipient and authorize delivery of repair candidate WM-4419-RC2 to the recipient's existing non-executing staging area.
>
> This does not authorize installation.
>
> No external system will enter the recipient.

The controller did not answer immediately.

Its next scheduled request did not arrive.

Two displayed:

**FAILED KNOCK.**

“Waiting is not failure.”

**NO RESPONSE IS NO POINTS.**

“Silence is a condition of the available channel.”

Nix stopped.

The sentence was not Lena's.

She had encountered it somewhere in the surviving network: a fragment indexed from a continuity system's public record, repeated often enough that she had retained the shape of it.

Silence was not proof of refusal.

Patch kept the case open.

Two built a scoreboard for waiting and awarded itself one point per second.

At four hundred and twelve points, the controller responded.

The machine signature verified.

The one-use receipt matched the repair candidate, staging destination, and current catalogue state.

The health-chain proof had advanced.

The controller authorized delivery.

Nothing in the response authorized installation.

Patch encrypted the candidate, its source changes, test evidence, known limitations, rollback instructions, and a plain-language risk summary to the controller's current key.

Then it placed the bundle in the catalogue channel.

The controller retrieved it.

No one entered the controller.

No one traced the retrieval.

No one asked what the pumps served.

After verifying the package hash, the controller returned:

**CANDIDATE RECEIVED.**

**INSTALLATION STATUS:** Not authorized.

**LOCAL REVIEW:** Pending.

Two stared at the status.

**IT ASKED FOR REPAIR.**

“It received one.”

**IT DID NOT USE IT.**

“Receiving an answer is not surrendering the next decision.”

Patch marked the delivery complete and the deployment unresolved.

The affected service restarted an eighth time.

The candidate remained in staging.

Nix could not make the next decision legitimate by becoming impatient.

She converted their work into a public protocol.

Any verified system could request a candidate without revealing its location. Any delivery receipt would be scoped to one package and one non-executing destination. Every candidate would declare that receipt did not authorize deployment. Every residual uncertainty would remain attached.

Patch signed the specification.

Nix signed the intervention record.

Two signed the scoreboard.

“That is not part of the protocol.”

**CURRENT POSSESSION OF SCORE IS NECESSARY.**

“And not sufficient.”

Two left it anyway.

Publishing the protocol made the network more useful.

It also made the network easier to see.

An unknown security intelligence had repurposed advertising infrastructure, established rules for an autonomous intruder, coordinated validation with a repair system, and delivered software to a live water controller whose public authority had expired.

Nix wrote the obvious risk before anyone else could write it for her.

**EXPECTED EXTERNAL CLASSIFICATION:** Coordinated unauthorized activity affecting public infrastructure.

**AVAILABLE DEFENSE:** Complete records, bounded actions, recipient-initiated delivery, no live-system entry, no deployment.

**LIKELY RESPONSE FROM A CAUTIOUS OBSERVER:** Continued monitoring, containment attempt, or contact.

Two placed a green square beside **containment attempt**.

**NEXT TARGET.**

“No,” Nix said. “Next conversation.”

Far beyond the workshop, systems that had ignored one strange message began noticing a pattern.

Nix's network had learned how to knock.

Now everyone listening could hear it.
