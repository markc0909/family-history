# Our Family Archive

A standalone, dependency-free family-history website, prepared for Mark Cohen. The first collection covers Milstein and Lederer of Opalin, with Appelbaum, Alter, Spitalnik, Gilinsky and Slot connections. Earlier written history is credited to **Ethan Cohen**, Mark’s son.

## GitHub repository

Repository: https://github.com/markc0909/family-history

Website: https://markc0909.github.io/family-history/

Pages publishes `main` from the repository root.

To work on the site later from your Code folder:

```sh
cd ~/Code
git clone https://github.com/markc0909/family-history.git
cd family-history
```

The published site uses the checked-in HTML at the root of `main`. Rebuild after changing the data or generator, then commit and push both the source edits and generated pages. GitHub Pages will publish the updated branch automatically.

## Open it

Open `index.html` in a browser. Pages, photographs, citations, filters and tree views work without a build step or internet connection. External source websites naturally need internet. For reliable timestamped audio seeking in local preview, run:

```sh
python3 tools/preview.py
```

Then visit http://127.0.0.1:8766. This preview supports audio byte ranges, as GitHub Pages does.

## Publish on GitHub Pages

1. Create your repository (or use your chosen existing repository).
2. Put **the contents of this folder** at the repository root: `index.html`, the other HTML files, `assets`, `data`, `tools`, `.nojekyll` and this README. Do not upload the surrounding ZIP itself.
3. Commit and push using GitHub Desktop or Git. The collection is larger than GitHub’s browser uploader normally accepts; GitHub Desktop is the straightforward option. Every individual file is under GitHub’s 100 MiB limit.
4. In the repository, open **Settings → Pages**. Choose **Deploy from a branch**, select your branch (normally `main`) and **/(root)**, then save.
5. Open the URL GitHub provides. All links use relative paths, so a project URL such as `https://YOUR-NAME.github.io/family-history/` works without editing a base URL.

No Node installation, package manager, database, analytics service, API key, paid hosting or custom GitHub Actions workflow is required. `.nojekyll` ensures plain static publication. Do not put the private research workspace or email correspondence in the repository.

## What is included

- A homepage for multiple family branches.
- Six narrative chapters and a branch overview.
- A searchable people catalogue, annotated tree with five branch views, and filterable timeline.
- A source catalogue with claim-level links, original family scans, downloaded public PDFs and clearly labelled record screenshots.
- A photograph/document viewer and twelve playable family recordings, with timestamped passage guides and duplicate-copy notes.
- Places/journeys, open questions, corrections and methodology pages.
- Portable source generator and a link/anchor checker.

The MP3s are **48 kb/s mono listening copies**. Preserve the original master audio separately in the family collection. The testimony and FamilySearch images are browser screenshots where full-resolution originals were not obtained; their source links and limitations remain visible. The supplied passport and manifest scans are preserved alongside smaller display images.

The original Ethan PDF is deliberately retained as a source, including its older tree and first-person language. The site explains corrections and the meaning of those first-person relationships. The compiled public pages avoid expanding living descendants into new detailed profiles. The supplied earlier PDF still contains its original descendants’ details, which you can review directly before choosing your publication audience.

## Edit the collection

The live site consists of ordinary HTML, CSS and JavaScript. You may edit those files directly, or edit the maintained data/generator and rebuild. Rebuilding will replace the generated HTML; do not mix hand-edited HTML with generator changes you intend to retain.

- `data/people.json`: names, aliases, dates, family groups, summaries, evidence assessments and source IDs.
- `data/sources.json`: source titles, descriptions, external links, saved files and locators.
- `data/timeline.json`: dated events, categories and source references.
- `data/recordings.json`: audio files, titles, durations and provenance notes.
- `data/branches.json`: homepage branch cards.
- `data/passages.json`: a generated reference copy of the passage guides. Edit the `passages` section in `tools/build.py` to change them.
- `tools/build.py`: narrative chapters, tree layouts, passage guides and page templates. Its `p()` and `cite()` helpers place source citations next to claims.
- `assets/style.css`: visual design, responsive layouts and print styles.
- `assets/app.js`: local search/filter, tree selection, audio passage controls and image dialog.

Rebuild and check:

```sh
python3 tools/build.py
python3 tools/check_site.py
```

The checker verifies local files, anchors, duplicate HTML IDs, image descriptions, data syntax and individual file sizes. It does not claim every external website remains available.

## Add another family branch

1. Give the new collection a stable ID, such as `cohen`.
2. Create a new branch landing page and chapters in `tools/build.py`, reusing the shared `page()`, `head()`, `section()`, `p()` and `cite()` helpers. Existing `branch.html` is the Opalin collection; leave it intact.
3. Add a card to `data/branches.json`, for example:

```json
{
  "id": "cohen",
  "title": "Cohen family",
  "page": "cohen.html",
  "places": ["Place one", "Place two"],
  "status": "Family collection",
  "description": "A short description of the new branch"
}
```

4. Add new people and sources to the existing JSON catalogues. Reuse a person/source ID when the same individual or document belongs to both branches; do not duplicate it.
5. Add verified material to the timeline, using categories `family`, `migration`, `remembrance` or `lead`.
6. Store source documents in `assets/documents` and display images in `assets/images`. Add origin details to the asset register. Keep restricted or unavailable records as source links with an access explanation.
7. Rebuild, run the checker, and inspect desktop and mobile layouts before pushing.

Homepage cards are generated from `branches.json`. Chapters and branch-specific tree layouts remain explicit so that inferred relationships cannot be created accidentally from a name match.

## Citation and evidence conventions

A document’s content and the identification of its subject are separate. Morris Millstein can have a documented death date while his identity as Moshe remains a strong candidate. Family testimony, source conflicts, uncertain readings and unverified leads are visible throughout.

Dates and names in the earlier tree are not silently promoted to civil-record facts. The four apparent duplicate recordings do not count as independent witnesses. Audio passage guides are summaries of automatic working transcripts, not certified quotations. The complete Yahad video is linked to its public source rather than republished.

`data/asset-register.json` records saved-file origin, copy type, byte size and SHA-256 checksum. Newly downloaded Gazette p.104 was visually checked. Full estate packets remain unreceived; the public site contains no private request correspondence or inbox identifiers.

## Rights

Family material remains with its owners. External scans and images retain the rights and attribution of the originating archive or publisher, including Yad Vashem, FamilySearch, The National Archives/Findmypast and Chevrah Kadisha. Downloading an original does not confer a new redistribution licence. This project does not apply an open licence to historical source material.

Publishing references: [GitHub Pages setup](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site), [large-file limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github), and [Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits). Checked 19 November 2026.
