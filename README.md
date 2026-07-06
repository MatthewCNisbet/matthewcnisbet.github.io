# matthewnisbet.com — personal site

A minimalist, low-maintenance academic hub. Static HTML/CSS/JS, no build step,
deploys free on GitHub Pages. Complements the Counterpoints Substack; every
publication can link out to a backdated Substack summary, a republished essay,
and media coverage.

## Files

```
index.html            Landing page (short bio, headshot, news)
bio.html              Extended biography + Curriculum Vitae link
publications.html     All publications, 5 sections, APA format, newest first
courses.html          Courses taught, by institution
talks.html            Talks & lectures (placeholder, populate from CV)
media.html            News coverage & interviews (placeholder, populate from CV)
assets/css/style.css  The whole design system
assets/js/site.js     Abstract/Media expand-collapse
assets/img/headshot.jpg
assets/pdf/Nisbet_CV.pdf
generate.py           Rebuilds the HTML from alldata.json (optional)
alldata.json          Parsed publications data (source of truth for the build)
```

## Design system (locked)

- One accent: green `#00693E` — used ONLY for the masthead bar, the active-nav
  underline, the panel border, and the favicon dot. Never on links.
- Links: black, underlined.
- White background, black text.
- Wordmark/headings: Source Serif 4 (free stand-in for Utopia Std).
- Body: system sans, tight/condensed density.
- Favicon: solid green dot (inline SVG, no file needed).

### Swapping in Utopia Std later
The wordmark is live text in `.brand .name`. Either (a) license Utopia Std as a
webfont and change `--serif` in `style.css`, or (b) replace the `<span class="name">`
in each page's masthead with an inline SVG of the wordmark drawn in Utopia.

## Deploying to GitHub Pages

1. Create a public repo, e.g. `matthewnisbet.github.io` (or any repo + Pages enabled).
2. Commit all files at the repo root.
3. Settings → Pages → Build from branch → `main` / root.
4. Optional custom domain `matthewnisbet.com`: add a `CNAME` file containing the
   domain, and point DNS at GitHub Pages.

## Updating content

### The CV
Replace `assets/pdf/Nisbet_CV.pdf`. Keep the filename so the link never breaks.

### Publications (titles, abstracts, links)
Edit `alldata.json`, then run `python3 generate.py` to rebuild `publications.html`.
Each entry supports these fields:

```json
{
  "authors": "Nisbet, M.C.",
  "year": "2018",
  "title": "Strategic philanthropy ...",
  "venue": "Wiley Interdisciplinary Reviews: Climate Change, 9(4), e524.",
  "doi": "10.1002/wcc.524",          // title links here; omit if none
  "abstract": "...",                  // shows the Abstract button; omit if none
  "pdf": "assets/pdf/foo.pdf",        // (to add) shows the PDF button
  "summary": "https://mattnisbet.substack.com/p/...",  // (to add) Summary button
  "essay": {"cite": "...", "url": "..."},              // (to add) leads Media panel
  "media": [ {"cite": "...", "url": "..."} ]            // (to add) Media panel list
}
```

Icons render conditionally: an entry with only an abstract shows just **Abstract**;
an entry with nothing shows no buttons. Add `pdf`, `summary`, `essay`, `media`
fields per entry as you collect them, then re-run `generate.py`. (The PDF/Summary/
Media rendering hooks are stubbed in `generate.py` — wire them on when you start
populating, following the Abstract pattern already there.)

### Bio prose
`bio.html` and the landing intro contain a CV-derived DRAFT biography marked with
an HTML comment. Replace with your own voice.

### News (landing page)
Three placeholder items in `index.html`. Edit directly.

## Data provenance

- Citations and section order: the long-form CV (master record).
- DOIs and abstracts: Web of Science export, matched to CV citations by title.
  28 of 45 journal articles matched a DOI; 26 carried abstracts. Unmatched
  entries simply show fewer controls — nothing was fabricated.
