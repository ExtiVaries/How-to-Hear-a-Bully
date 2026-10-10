# Practical Guides: agent handoff

This file applies to this repository. It explains the project and how to maintain it. Follow the user's current instructions and carry forward authorization already given in the session; this historical handoff is not blanket authorization for future merges or publication.

Status snapshot: **9 October 2026**. Inspect the current remote branch and working tree before making changes. Preserve unrelated work. Update this handoff when the project's structure or status materially changes.

## Purpose and collection

Practical Guides is a collection of free public resources that help people understand confusing situations, examine evidence, and choose useful next steps.

The owner wants resources that remain credible to people with different political views. Earn trust through inspectable evidence, fair reasoning, practical examples, and clearly stated uncertainty. Do not promise perfect neutrality or describe AI-assisted review as independent expert certification.

Collection: https://extivaries.github.io/How-to-Hear-a-Bully/practical-guides/

| Resource | Purpose | Public address |
| --- | --- | --- |
| Don't Pay a Middleman | Find official U.S. federal service routes and distinguish government fees from payments to a helper. Recognize that advice, translation, representation, and other paid help can be worthwhile. | https://dont-pay-a-middleman.vercel.app/ |
| How to Hear a Bully | Examine manipulative language, accusations, and labels while distinguishing them from disagreement, mistakes, exaggeration, and honest clarification. Apply the same scrutiny to favored and disfavored speakers. | https://extivaries.github.io/How-to-Hear-a-Bully/ |
| Why Does Everything Feel Like a Crisis? | Separate events, the information reaching readers, unequal exposure to harm, and appropriate responses. The method can support greater urgency as well as reassurance. | https://extivaries.github.io/How-to-Hear-a-Bully/crisis/ |
| Who to Trust When It All Breaks Down? | Decide whom to rely on, for which question, when accounts conflict. Examine expertise, evidence, independent corroboration, interests, corrections, and uncertainty. The title describes a loss of bearings, not a claim that every institution has failed. | https://extivaries.github.io/How-to-Hear-a-Bully/trust/ |

[Plant Climate Map](https://plantclimatemap.org/) appears separately under **Climate and growing**. It explores Köppen–Geiger climate classifications and USDA plant hardiness zones across the contiguous United States. Keep it a separate app with its own sources, scope, and reuse terms. Middleman is also hosted separately; this repository contains the guides and collection, not those applications.

## Community claim tracker planning

The owner requested a first-version written specification and a Claude adversarial-review handoff for a **Community claim tracker**, a planned interactive resource within Practical Guides. The packet is in [docs/claim-tracker/](docs/claim-tracker/): [v1 specification](docs/claim-tracker/v1.md), [next Claude review handoff](docs/claim-tracker/claude.md), [initial summary](docs/claim-tracker/review.md), [full original review](docs/claim-tracker/review-detailed.md), [historical follow-up](docs/claim-tracker/FOLLOWUP.md), and [revision response](docs/claim-tracker/REVISIONS.md). The full reports were subsequently supplied on `claude/project-thread-68owll` and copied unchanged into the packet. The follow-up at `1adb5a3` judged the five initial blockers resolved in writing but left N1–N3 and before-pilot requirements; its verdict was **ready after specified revisions**. The latest specification addresses those findings; confirmation of these latest edits and runtime checks remain pending. No functioning tracker, live connector, or schedule exists.

The first release is a bounded manual-only pilot. Publication follows a completed assessment and preserves the as-circulating meaning. Evidence-change reports need a cited record and specific change; a reviewer checks specificity before a public banner, with at most two open correction reports/member. Removal uses closed bases, retains every revision’s safe label/dates/author, and labels same-reviewer action. Accepted-but-unpublished records expire after their deadline plus grace; all closed unpublished payloads have a seven-day purge. Conclusive labels require reviewed non-lead evidence. Every revision has a required change type; material follower updates generate exactly one persisted event per active follower. Community attribution requires opt-in for member-supplied context.

Use the handoff to verify the latest changes against N1–N3, F11/F13, and N4, and to check regressions of the original blockers. Preserve all historical review reports; a later requested verification report should use `docs/claim-tracker/FOLLOWUP-2.md`. Keep popularity separate from credibility, repeated coverage separate from corroboration, and developments separate from corrections. Apply the same standards across communities and political viewpoints. AI-assisted review is not expert certification.

Implementation, initial niche/source selection, hosting, and runtime checks remain open. Manual launch additionally requires the participation notice, contribution terms, named roles, weekly spot checks, and a host meeting retention/restore rules. Automatic discovery is later-gated on source permission, measured capacity, caps/expiry, fenced import writes, source edit/deletion handling, and coverage gaps. Deferred refinements are tracked in the revision response. This planning addition does not authorize changing published guides, adding their backend dependencies, merging the draft PR, or extending Bully's reuse terms to the tracker or its data.

## Publication checkpoint

**Complain or Constrain?** has completed text drafting, review, and bounded corrections. The approved manuscript, source notes, and handoff are in [docs/complain-guide/](docs/complain-guide/). The user authorized pushing this packet to GitHub on a separate branch. It has no website edition yet. A successful docket check and legal review of the Tennessee section remain open before that section goes live. Preserve the accepted article wording; its length is intentionally flexible under the user's instruction to prioritize quality.

At this snapshot, the Trust guide completed drafting, adversarial review, corrections, final manuscript checking, website construction, and publication. There is no outstanding task to publish that version.

- Trust guide: https://extivaries.github.io/How-to-Hear-a-Bully/trust/
- Seven source notes: https://extivaries.github.io/How-to-Hear-a-Bully/trust/notes.html
- Shared methods: https://extivaries.github.io/How-to-Hear-a-Bully/practical-guides/methods.html
- Publication commit: `bd1d7b5a74056b57d77e3a8940531f6be9f23214`, merged through [PR #4](https://github.com/ExtiVaries/How-to-Hear-a-Bully/pull/4).

The approved Trust guide has 1,924 readable words. Its guide and notes were preserved unchanged during website construction. GitHub Pages deployment succeeded. All eight reading pages and eight supporting files returned HTTP 200 and matched the checked build.

Historical checks passed for eight pages, 230 internal links, and 16 reciprocal citation pairs across Crisis and Trust. Browser checks covered four new or updated pages at 320, 390 and 1280 pixels in light and dark modes. All seven Trust citation round trips, the keyboard skip link, and contents menu passed. These results describe that release, not future changes.

## Repository and source files

Repository: https://github.com/ExtiVaries/How-to-Hear-a-Bully

GitHub Pages publishes from `claude/project-thread-i83pmv`, at the repository root. Confirm the current configuration before release.

| Path | Role |
| --- | --- |
| [how-to-hear-a-bully.md](how-to-hear-a-bully.md), [how-to-hear-a-bully-notes.md](how-to-hear-a-bully-notes.md) | Bully manuscript and source notes |
| [docs/crisis-guide/](docs/crisis-guide/) | Crisis manuscript, notes, and review records |
| [docs/trust-guide/](docs/trust-guide/) | Trust manuscript, seven notes, research history, and reviews |
| [docs/complain-guide/](docs/complain-guide/) | Accepted Complain manuscript, thirteen source notes, and review handoff; website publication pending |
| [docs/claim-tracker/](docs/claim-tracker/) | Revised tracker specification, adversarial-review handoff, supplied review summary, and response; follow-up review and implementation pending |
| [docs/practical-guides/homepage.md](docs/practical-guides/homepage.md) | Current collection copy |
| [docs/practical-guides/methods.md](docs/practical-guides/methods.md) | Current methods, limits, corrections, and reuse information |
| `index.html`, `notes.html` | Bully reading pages |
| `crisis/`, `trust/`, `practical-guides/` | Generated reading pages |
| [scripts/build_suite.py](scripts/build_suite.py) | Generates the six collection, Crisis, and Trust pages |
| [scripts/check_site.py](scripts/check_site.py) | Checks reproducibility, links, anchors, metadata, and sitemap |
| [assets/practical-guides.css](assets/practical-guides.css) | Shared styling |
| [DISCOVERY.md](DISCOVERY.md), [sitemap.xml](sitemap.xml), [llms.txt](llms.txt) | Discovery instructions and indexes |

Read the latest [Trust final check](docs/trust-guide/FINAL-CHECK.md) and [website check](docs/trust-guide/PUBLICATION-CHECK.md) before changing that work. Older research packets and handoffs are historical and can contain superseded findings. The original Crisis homepage draft is historical; use the current collection copy above.

## Editing, build, and release

The site serves static HTML. The current builder requires Python 3.9+ and Pandoc 3:

```sh
python3 scripts/build_suite.py
python3 scripts/check_site.py
python3 -m http.server 8765
```

Open `http://localhost:8765/practical-guides/` for a local preview. Consult the current scripts and README if requirements change.

- Edit canonical Markdown and regenerate affected pages. Commit generated HTML alongside source changes. The checker also rebuilds generated pages and flags stale output.
- The builder does not regenerate the original Bully pages. Keep their HTML and Markdown synchronized if their prose changes.
- Preserve approved manuscript wording during layout, navigation, or discovery work. Substantive corrections need supporting evidence and an updated review/change record.
- Keep section IDs, note anchors, and return links stable. Respect the `/How-to-Hear-a-Bully/` project prefix.
- For relevant presentation changes, check phone and desktop layouts, light/dark modes, navigation, and citations.
- When publication is authorized, check the current branch, complete appropriate validation, merge through the applicable workflow, and verify the actual public URLs. Distinguish committed, merged, deployed, and indexed.
- Do not introduce analytics, a backend, or client-side rendering dependencies merely to publish another guide.

## Editorial standards and known limits

Keep an accessible voice, practical exercises, and approximately 1,500–2,000 words for new short guides, excluding source notes. This is a target for new work, not a reason to cut an approved existing guide. Preserve successful sections when making bounded corrections.

Use primary sources where possible. Distinguish empirical findings, philosophical interpretations, professional guidance, and our own teaching advice. Record incomplete source access honestly. Do not infer motives from disagreement, manufacture partisan balance, or generalize a study beyond its design. Apply the same evidentiary standards to people the reader supports and opposes.

At this snapshot, the 2022 classroom study's allocation procedure in the Trust notes remains unverified. The guide describes the comparison without calling it randomized. Other access limits are recorded in the notes. The teaching questions have not been tested with readers.

These projects use AI assistance for research, drafting, critical review, and development. The owner directs the work; do not imply every factual statement was individually checked by a human. AI review, link checks, and successful builds are not scholarly peer review or reader testing.

## Discovery and reuse

Maintain canonical URLs, structured metadata, Markdown alternatives, the sitemap, and the optional `llms.txt` index. Preserve `.nojekyll`, Google/Bing verification files, and the IndexNow ownership file.

IndexNow accepted notifications for the Trust guide, Trust notes, collection, and methods page after publication. Acceptance does not prove indexing or guarantee inclusion in AI answers. Follow [DISCOVERY.md](DISCOVERY.md) for later notifications; do not repeatedly submit unchanged pages. A repository edit alone is not evidence of deployment.

Do not renew research dates merely because a page was rebuilt or a link checked. Keep original publication dates and update sitemap modification dates only for real changes.

Consult the current [README license section](README.md#license) and [LICENSE](LICENSE) before making reuse claims. At this snapshot, Bully has CC BY 4.0 plus the owner's additional noncommercial permission. **Crisis, Trust, and collection reuse terms remain undecided.** Do not extend Bully's license automatically to them, other apps, or third-party material. Author credits are not a major priority for the owner; that does not select a license.

## Collaboration

The established workflow is: prepare a brief and evidence, draft, independently challenge the draft, make bounded corrections, and publish when authorized. Codex and Claude have alternated these roles; useful handoffs identify exact files, changes, evidence, and remaining uncertainty.

Continue work already authorized without repeatedly asking for confirmation. Give concise progress updates and clearly separate completed work from outstanding questions. Provide public web or GitHub links; workspace-only downloads have failed on the owner's phone.

Build on the completed collection. Do not restart the Trust review or rewrite approved guides without a concrete reason.
