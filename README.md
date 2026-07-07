# matthewcnisbet.github.io — website files

Flat static site for GitHub Pages. Every file sits at the repository root; there is no
assets/ folder. Green accent (#00693E), all-sans typography, version-2 landing hero.

## What to upload to the repo root
Site (required to render):
- index.html, about.html, cv.html, publications.html, talks.html, media.html, courses.html
- style.css
- headshot.png
- CNAME  (contains "www.matthewnisbet.com" — see HTTPS note below)

Add separately (not in this package):
- Nisbet_CV.pdf  (the C.V. page links to it; upload your updated PDF to the repo root)

For future rebuilds (optional, not served):
- generate.py and the five record files:
  nisbet_cv_media_coverage.md, nisbet_cv_publications.md,
  nisbet_cv_essays_columns_v2.md, nisbet_cv_talks.md, nisbet_cv_appointments_record.md
  Rebuild with: python3 generate.py

## Delete these stale files from the repo if present
alldata.json, talks.json, media.json, parse_cv.py, bio.html

## Fixing the Chrome "not secure" warning (HTTPS)
1. The CNAME file in this package must stay at the repo root on every deploy; it tells
   GitHub Pages the custom domain is www.matthewnisbet.com and prevents the setting from
   being wiped on push.
2. In the repo: Settings > Pages > "Enforce HTTPS". Tick it. If it is grayed out, the
   Let's Encrypt certificate is still provisioning; wait up to 24-48 hours, then tick it.
3. If it stays grayed out past 48 hours, remove and re-enter the custom domain in
   Settings > Pages to restart certificate provisioning, then enforce HTTPS.
4. Confirm at GoDaddy the only @ records are the four GitHub IPs and the only www record
   is the CNAME to matthewcnisbet.github.io; remove any parked A record or default CNAME.

## Note
After uploading, hard-refresh (Cmd/Ctrl-Shift-R) to clear cached CSS.
