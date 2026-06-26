# matthewcnisbet.github.io — flat build (June 2026)

All files live at the repository root. No assets/ folder.
The seven HTML files plus style.css and headshot.png are the live site.

## Files to upload (all at root)
index.html, about.html, cv.html, publications.html, talks.html, media.html,
courses.html, style.css, headshot.png

Add Nisbet_CV.pdf at the root too; the C.V. page links to "Nisbet_CV.pdf".

## Delete from the repo (old, unused)
alldata.json, bio.html  (replaced by about.html; not referenced anywhere)
Also any old talks.json, media.json, parse_cv.py if present.

## Rebuild after editing a record file
Keep these next to generate.py and run `python3 generate.py`:
nisbet_cv_publications.md, nisbet_cv_essays_columns_v2.md,
nisbet_cv_media_coverage.md, nisbet_cv_talks.md, nisbet_cv_appointments_record.md

## Notes
- Top navigation only; no footer navigation.
- Talks and Media group entries under bold year subheaders.
- Citations are flush left; list spacing is dense; bracketed counts are not bold.
- If the site still looks unstyled after upload, hard-refresh (Cmd-Shift-R / Ctrl-Shift-R).
