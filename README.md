# matthewcnisbet.github.io — build (June 2026, revised)

Static site. The seven HTML files plus assets/ are the live site.
generate.py regenerates the HTML from the markdown record files.

## Deploy (must replace ALL of these, not just the HTML)
- index.html, about.html, cv.html, publications.html, talks.html, media.html, courses.html
- assets/css/style.css   <-- REPLACE THIS; the layout depends on it
- assets/img/headshot.png
- assets/pdf/Nisbet_CV.pdf  (add your CV PDF; the C.V. page links to it)

If the site looks unstyled (sidebar stacked, footer links merged, square headshot),
the old assets/css/style.css is still being served. Overwrite it with the new file
and hard-refresh (Cmd-Shift-R / Ctrl-Shift-R).

## Rebuild after editing a record file
Place these next to generate.py and run `python3 generate.py`:
nisbet_cv_publications.md, nisbet_cv_essays_columns_v2.md,
nisbet_cv_media_coverage.md, nisbet_cv_talks.md, nisbet_cv_appointments_record.md

## Notes
- Top navigation only; no footer navigation.
- Talks and Media group entries under bold year subheaders.
- Citations are flush left; list spacing is dense.
- Bracketed counts are not bold.
