# matthewcnisbet.github.io — upload set (June 2026)

Flat site: every file sits at the repository root. No assets/ folder.

## Upload all of these to the repo root
index.html, about.html, cv.html, publications.html, talks.html, media.html,
courses.html, style.css, headshot.png, generate.py

## Add yourself
Nisbet_CV.pdf at the root (the C.V. page links to it).

## Delete from the repo (obsolete, unused)
alldata.json, bio.html, talks.json, media.json, parse_cv.py

## After uploading
Hard-refresh (Cmd-Shift-R / Ctrl-Shift-R) so the browser loads the new style.css.

## Rebuild later (optional)
generate.py reads the five record markdown files directly. To regenerate the HTML,
keep those records next to generate.py and run: python3 generate.py
