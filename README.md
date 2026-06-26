# matthewcnisbet.github.io — build

Static site. No build step required to deploy: the seven HTML files plus
`assets/` are the live site. `generate.py` regenerates the HTML from the
markdown record files if any record changes.

## Files to deploy (repository root)
- index.html, about.html, cv.html, publications.html, talks.html, media.html, courses.html
- assets/css/style.css
- assets/img/headshot.png  (circular crop is applied by CSS)
- assets/pdf/Nisbet_CV.pdf  (add your CV PDF here; the C.V. page links to it)

## To rebuild after editing a record file
Place these alongside generate.py and run `python3 generate.py`:
- nisbet_cv_publications.md
- nisbet_cv_essays_columns_v2.md
- nisbet_cv_media_coverage.md
- nisbet_cv_talks.md
- nisbet_cv_appointments_record.md

## Navigation
Top and footer navigation are identical and defined once in generate.py (NAV):
About, C.V., Publications, Talks, Media, Courses, Substack.

## Notes
- Counts as built: publications 2 / 45 / 29 / 29, essays 124, talks 123, media 337.
- Education, Teaching/mentoring, and Service/leadership on the C.V. page are
  placeholders pending dedicated record sections; everything else pulls from
  nisbet_cv_appointments_record.md.
- Add assets/pdf/Nisbet_CV.pdf so the "PDF version" link resolves.
