# FOIA comparisons: bounded review, October 29, 2026

## Scope and publication boundary

The owner approved a first expansion containing three historical comparisons: the 2020 unofficial electoral certificates, Pentagon January 6 texts, and the Afghanistan Papers. The existing Biden vice-presidential PRA comparison remains in place. Clinton-email and torture-records cases are deferred, not part of this change.

This update adds context to `pra-release-tracker.md` and its HTML edition. It does not add events to `events.csv`, alter the two notification-level extension confirmations, change the live watch, or claim any new release of the three Trump-library collections. The October 27 case snapshot and October 28 request-status snapshot remain dated as originally recorded; this update is not a fresh audit of those statuses.

## Source checks and limits

### Unofficial electoral certificates

- Official public collection: https://www.archives.gov/foia/2020-presidential-election-unofficial-certificates
- NARA's page identifies certificates, related correspondence and envelope scans, distinguishes them from official state submissions, and links the seven state collections.
- Requester account: https://americanoversight.org/analysis/defense-department-and-army-failed-to-preserve-jan-6-text-messages/
- American Oversight reports receipt in March 2021. Do not turn that reported receipt month into NARA's first-publication date. Public availability is supported separately by NARA's collection page.

### Pentagon texts

- American Oversight's August 2, 2022 account identifies January 12, 2021 requests and describes a March 2022 joint status report. The linked court filing was not independently retrieved; the tracker attributes that account to the requester.
- Official NARA correspondence, UD-2022-0056: https://www.archives.gov/files/records-mgmt/resources/ud-2022-0056-dod-open-close.pdf
- The six-page PDF was inspected, including a screenshot of page 5 (June 15, 2023 Office of the Secretary of Defense closure letter). NARA describes the carrier-content/metadata distinction and closes its records-management case.
- Do not treat closure as recovery of texts, closure of the FOIA lawsuit, a finding about all Army records, or proof of motive. Do not transfer this preservation problem to the Hutchinson/Liddell collections.

### Afghanistan Papers

- Official CRS record: https://www.congress.gov/crs-product/R46197
- Inspected mirror: https://www.everycrsreport.com/reports/R46197.html
- Inspected PDF: https://www.everycrsreport.com/files/20200128_R46197_9f1b67a1b995b179acf078b24f4bb2be6eba2dc5.pdf
- The January 28, 2020 CRS report, pages 1–2, supports the August 2016 request / October 2017 lawsuit / August 2019 final-batch receipt / December 9, 2019 publication sequence. The PDF page containing the timeline was visually inspected.
- Direct Congress.gov PDF retrieval failed. The mirror is labeled as such, not presented as an official host. The historical report does not establish the current status of later disputes. Redactions and delivery/publication are separate facts.

## Candidate held outside live monitoring

**Judicial Watch v. CIA, D.D.C. No. 1:24-cv-02172.** A litigant's October 20, 2026 announcement reports an October 15 minute order directing rolling productions to begin November 16, 2026:

https://www.judicialwatch.org/court-orders-cia-producing-january-6-records/

Document landing page:

https://www.judicialwatch.org/documents/jw-v-cia-j6-rolling-productions-order-02172/

No independently retrieved official court-hosted docket entry or order was obtained in this review. The quoted order is a lead, not a verified official-development alert. No production or public posting is established. Verify the exact case and order, then separately verify delivery/publication before any monitoring expansion; a similarly numbered or similarly titled case is not a substitute.

## Validation performed

- Original Markdown reconstructed from a fresh GitHub read and its Git blob hash matched `2303d6408a5a6b2f744202aaf84b86c5fe05e6f9`.
- Removing the comparison section and its introductory date sentence restores the original Markdown exactly.
- Updated Markdown rendered with the suite's Pandoc format flags; HTML main-text and link parity checked.
- Unique IDs, internal fragment targets, JSON-LD date, the two-row case table, and the December 2 proposed-date safeguard checked.
- Existing shared CSS matched its repository blob hash and is not changed.
- Chromium checks at 320, 390 and 1280 pixels, in light and dark modes: no page-level horizontal overflow; three comparison subsections; keyboard skip link works; no JavaScript errors. Mobile and desktop screenshots inspected. Tests used the exact page content with the unchanged stylesheet inlined for the local browser harness, not a deployed URL.
- Changes limited to tracker Markdown/HTML, this review note and the tracker sitemap modification date. The extension event register is unchanged.

**Validation limit:** The full repository could not be cloned in the working environment, so `scripts/build_suite.py` and `scripts/check_site.py` were not run here. The targeted checks above are not a full-site build, external-link availability guarantee, independent expert review, merge, or deployment verification.
