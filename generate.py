#!/usr/bin/env python3
"""
Generate the Matthew C. Nisbet static site.

Reads the canonical CV record markdown files (authoritative as of the June 2026
redesign) and emits the redesigned pages: typographic green-dot mark, circular
headshot, seven-item top nav mirrored in the footer, CV-page grouped sidebar,
publications-page anchor sidebar, no divider lines, no italics.

Record files expected alongside this script:
  nisbet_cv_publications.md
  nisbet_cv_essays_columns_v2.md
  nisbet_cv_media_coverage.md
  nisbet_cv_talks.md
  nisbet_cv_appointments_record.md

Emits: index.html, about.html, cv.html, publications.html, talks.html,
media.html, courses.html, plus assets/css/style.css (written by build_css()).
"""
import re, html, os

FAVICON = ("data:image/svg+xml,"
  "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
  "%3Ccircle cx='16' cy='16' r='9' fill='%2300693E'/%3E%3C/svg%3E")

# Top navigation, fixed order. The footer parallels this exactly.
NAV = [
    ("About",        "about.html"),
    ("C.V.",         "cv.html"),
    ("Publications", "publications.html"),
    ("Talks",        "talks.html"),
    ("Media",        "media.html"),
    ("Courses",      "courses.html"),
    ("Substack",     "https://mattnisbet.substack.com"),
]

HEADSHOT = "assets/img/headshot.png"

def nav_html(active, cls):
    out = ""
    for label, href in NAV:
        a = ' class="active"' if label == active else ""
        out += f'<a href="{href}"{a}>{html.escape(label)}</a>'
    return f'<nav class="{cls}">{out}</nav>'

def head(title, active):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;600;700&display=swap">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<header class="masthead"><div class="wrap">
  <a class="brand" href="index.html"><span class="bar"></span><span class="name">Matthew C. Nisbet</span></a>
  {nav_html(active, "main")}
</div></header>
<main class="wrap">
"""

def footer():
    return f"""</main>
<footer><div class="wrap">
  <span class="dot"></span>
  {nav_html(None, "foot")}
  <span class="copy">&copy; Matthew C. Nisbet</span>
</div></footer>
</body></html>"""

def md_links_to_html(text):
    out, pos = [], 0
    for m in re.finditer(r'\[([^\]]+)\]\((https?://[^)]+)\)', text):
        out.append(html.escape(text[pos:m.start()]))
        out.append(f'<a href="{html.escape(m.group(2))}">{html.escape(m.group(1))}</a>')
        pos = m.end()
    out.append(html.escape(text[pos:]))
    return "".join(out)

def read_record(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    sections, ch, cc, ce = [], None, None, []
    for ln in lines:
        s = ln.rstrip()
        hm = re.match(r'^#{1,4}\s+(.*)$', s)
        if hm:
            if ch is not None:
                sections.append((ch, cc, ce))
            raw = hm.group(1)
            m = re.search(r'\[(\d+)\]', raw)
            cc = m.group(1) if m else None
            ch = re.sub(r'\s*\[[^\]]*\]', '', raw).strip()
            ce = []
        elif s.strip() == "---" or not s.strip():
            continue
        else:
            ce.append(s.strip())
    if ch is not None:
        sections.append((ch, cc, ce))
    return sections

def entry_html(raw):
    return f'<div class="entry"><div class="cite">{md_links_to_html(raw)}</div></div>'

# ---------------- landing ----------------
def build_index():
    h = head("Matthew C. Nisbet", "About")
    h += f"""
<section class="hero">
  <img class="avatar" src="{HEADSHOT}" alt="Matthew C. Nisbet">
  <div class="herotext">
    <div class="title">Professor of communication, public policy, and urban affairs</div>
    <div class="subtitle">Northeastern University-Boston MA</div>
    <p>I study how media and intellectuals shape public debate over science, technology, and the environment. My research spans climate change, the politics of expertise, and the place of contemplative practice in public life.</p>
    <p>I write <a href="https://mattnisbet.substack.com">Counterpoints</a>, a Substack for readers across policy, journalism, and the academy. Much of it grows out of <a href="publications.html#peerreviewed">peer-reviewed research</a> and <a href="publications.html#reports">policy reports</a> archived here.</p>
    <p>See my <a href="about.html">full biography</a>, <a href="talks.html">talks</a>, or <a href="media.html">news coverage</a>.</p>
  </div>
</section>
"""
    return h + footer()

# ---------------- about ----------------
def build_about():
    h = head("About — Matthew C. Nisbet", "About")
    h += f"""
<section class="bio">
  <img class="avatar" src="{HEADSHOT}" alt="Matthew C. Nisbet">
  <div class="biotext">
    <p>Matthew C. Nisbet is Professor of Communication, Public Policy, and Urban Affairs at Northeastern University, where he studies the role of communication, media, and intellectuals in public debates over science, technology, and the environment.</p>
    <p>His research examines climate change and energy politics, the politics of expertise and knowledge-based journalism, public opinion about emerging science, and the cultural politics of wellness and contemplative practice. He is the editor of The Oxford Encyclopedia of Climate Change Communication and a co-author of the U.S. National Academies report Communicating Science Effectively: A Research Agenda. His <a href="publications.html#peerreviewed">peer-reviewed work</a> has been widely cited, and several papers rank among the most-cited in the field.</p>
    <p>He has held visiting positions and fellowships at Dartmouth College and Goucher College, and earned his Ph.D. and M.S. in Communication from Cornell University and his B.A. in Government from Dartmouth College.</p>
    <p>He writes <a href="https://mattnisbet.substack.com">Counterpoints</a>, a Substack for readers across policy, journalism, and the academy. His <a href="publications.html">publications</a>, <a href="talks.html">talks and lectures</a>, and <a href="media.html">news coverage and interviews</a> are collected on this site.</p>
  </div>
</section>
"""
    return h + footer()

# ---------------- C.V. ----------------
CV_SIDEBAR = [
    ("Biography", "about.html"),
    ("Education", "#education"),
    ("__GROUP__", "Experience"),
    ("Academic", "#academic"),
    ("Editorial", "#editorial"),
    ("Fellowships", "#fellowships"),
    ("Expert advice", "#expert"),
    ("Consulting", "#consulting"),
    ("Professional", "#professional"),
    ("__GAP__", ""),
    ("Funding/grants", "#funding"),
    ("Honors/awards", "#honors"),
    ("Impact/recognition", "#impact"),
    ("Teaching/mentoring", "#teaching"),
    ("Service/leadership", "#service"),
]

def cv_sidebar_html():
    out = ['<aside class="side">',
           f'<img class="avatar" src="{HEADSHOT}" alt="Matthew C. Nisbet">',
           '<nav class="sidenav">']
    for label, target in CV_SIDEBAR:
        if label == "__GROUP__":
            out.append(f'<div class="glabel">{html.escape(target)}</div>')
        elif label == "__GAP__":
            out.append('<div class="gap"></div>')
        else:
            out.append(f'<a href="{target}">{html.escape(label)}</a>')
    out.append('</nav></aside>')
    return "".join(out)

def build_cv():
    appt = read_record("nisbet_cv_appointments_record.md")
    by = {h: (c, e) for h, c, e in appt}

    def section(anchor, label, key, show_count=True):
        if key not in by:
            return ""
        count, entries = by[key]
        cnt = f' <span class="ct">[{count}]</span>' if (count and show_count) else ""
        block = [f'<h2 class="section" id="{anchor}">{html.escape(label)}{cnt}</h2>']
        for e in entries:
            block.append(entry_html(e))
        return "".join(block)

    h = head("C.V. — Matthew C. Nisbet", "C.V.")
    h += '<div class="cols">' + cv_sidebar_html() + '<div class="maincol cvpage">'
    h += '<div class="cvtitle">Curriculum vitae</div>'
    h += ('<div class="cvmeta">'
          '<a href="assets/pdf/Nisbet_CV.pdf">PDF version</a> '
          '<a href="publications.html">Publications</a></div>')
    h += '<h2 class="section" id="education">Education</h2>'
    for e in ["Nisbet, M.C. (2003). Ph.D., Communication, Cornell University.",
              "Nisbet, M.C. (1999). M.S., Communication, Cornell University.",
              "Nisbet, M.C. (1994). B.A., Government, Dartmouth College."]:
        h += entry_html(e)
    h += section("academic", "Academic appointments", "Academic appointments")
    h += '<h2 class="section" id="editorial">Editorial appointments</h2>'
    for sub in ("Editor-in-chief/associate editor", "Editorial board"):
        if sub in by:
            c, e = by[sub]
            cnt = f' <span class="ct">[{c}]</span>' if c else ""
            h += f'<h3 class="subsection">{html.escape(sub)}{cnt}</h3>'
            for x in e:
                h += entry_html(x)
    h += section("fellowships", "Fellowships", "Visiting positions/fellowships")
    h += '<h2 class="section" id="expert">Expert advisory committees'
    if "Expert advisory committees" in by and by["Expert advisory committees"][0]:
        h += f' <span class="ct">[{by["Expert advisory committees"][0]}]</span>'
    h += '</h2>'
    for sub in ("U.S. National Academies of Sciences, Engineering, and Medicine",
                "U.S. National Science Foundation, National Science Board"):
        if sub in by:
            c, e = by[sub]
            h += f'<h3 class="subsection">{html.escape(sub)}</h3>'
            for x in e:
                h += entry_html(x)
    h += section("consulting", "Consulting/advisory positions", "Consulting/advisory positions")
    h += section("professional", "Professional positions", "Professional positions")
    h += section("funding", "Funded research projects", "Funded research projects")
    h += section("honors", "Honors and awards", "Honors and awards")
    h += section("impact", "Impact/recognition", "Impact/recognition", show_count=False)
    h += '<h2 class="section" id="teaching">Teaching and mentoring</h2>'
    h += '<div class="entry"><div class="cite">See <a href="courses.html">Courses</a> for current and past teaching.</div></div>'
    h += '<h2 class="section" id="service">Service and leadership</h2>'
    h += '<div class="entry"><div class="cite">Departmental, university, and professional service available in the PDF C.V.</div></div>'
    h += '</div></div>'
    return h + footer()

# ---------------- Publications ----------------
PUB_SECTIONS = [
    ("edited",       "Edited volumes",                  "Edited volumes"),
    ("peerreviewed", "Peer-reviewed studies / articles","Peer-reviewed articles"),
    ("chapters",     "Book chapters",                   "Book chapters"),
    ("reports",      "Reports",                         "Reports/white papers"),
    ("essays",       "Essays/columns",                  "Essays and columns"),
]

def pub_sidebar_html():
    out = ['<aside class="side">',
           f'<img class="avatar" src="{HEADSHOT}" alt="Matthew C. Nisbet">',
           '<nav class="sidenav">']
    for anchor, label, _ in PUB_SECTIONS:
        disp = 'Peer-reviewed<br>studies / articles' if anchor == "peerreviewed" else html.escape(label)
        out.append(f'<a href="#{anchor}">{disp}</a>')
    out.append('</nav></aside>')
    return "".join(out)

def build_publications():
    lookup = {h: (c, e) for h, c, e in read_record("nisbet_cv_publications.md")}
    for h, c, e in read_record("nisbet_cv_essays_columns_v2.md"):
        lookup[h] = (c, e)
    out = head("Publications — Matthew C. Nisbet", "Publications")
    out += '<div class="cols">' + pub_sidebar_html() + '<div class="maincol pubpage">'
    out += '<div class="cvtitle">Publications</div>'
    out += '<div class="cvmeta"><a href="https://mattnisbet.substack.com">Counterpoints on Substack</a></div>'
    for anchor, label, key in PUB_SECTIONS:
        if key not in lookup:
            continue
        count, entries = lookup[key]
        cnt = f' <span class="ct">[{count}]</span>' if count else ""
        out += f'<h2 class="section" id="{anchor}">{html.escape(label)}{cnt}</h2>'
        for e in entries:
            out += entry_html(e)
    out += '</div></div>'
    return out + footer()

# ---------------- Talks / Media ----------------
def build_list_page(record_file, page_title, active, heading):
    secs = read_record(record_file)
    _, count, entries = secs[0]
    h = head(f"{page_title} — Matthew C. Nisbet", active)
    cnt = f' <span class="ct">[{count}]</span>' if count else ""
    h += f'<h1 class="page">{html.escape(heading)}{cnt}</h1>'
    h += '<div class="listcol">'
    for e in entries:
        h += entry_html(e)
    h += '</div>'
    return h + footer()

def build_talks():
    return build_list_page("nisbet_cv_talks.md", "Talks and lectures", "Talks", "Talks and lectures")

def build_media():
    return build_list_page("nisbet_cv_media_coverage.md", "News coverage and interviews", "Media", "News coverage and interviews")

# ---------------- Courses ----------------
COURSES = {
    "Northeastern University": [
        "Political Communication", "Environmental Issues, Communication and Media",
        "Strategic Communication Capstone", "Health Communication",
        "Climate Change Communication, Energy Politics and Journalism",
        "Media Advocacy and Communication Research"],
    "American University": [
        "Political Communication", "Communication, Culture and Environment",
        "Public Communication Theory", "Strategic Communication", "Advanced Media Theory",
        "Ethical Persuasion", "Public Communication Research Methods",
        "Communication and Society", "Understanding Media"],
    "The Ohio State University": [
        "Mass Communication and Social Systems",
        "Quantitative Reasoning for Journalism and Communication",
        "Communication Research Methods", "Science Communication (Honors)",
        "Mass Communication and Society"],
}

def build_courses():
    h = head("Courses — Matthew C. Nisbet", "Courses")
    h += '<h1 class="page">Courses</h1>'
    h += '<div class="listcol">'
    for inst, cs in COURSES.items():
        h += f'<h2 class="section">{html.escape(inst)}</h2>'
        for c in cs:
            h += f'<div class="entry"><div class="cite">{html.escape(c)}</div></div>'
    h += '</div>'
    return h + footer()

PAGES = [
    ("index.html", build_index), ("about.html", build_about),
    ("cv.html", build_cv), ("publications.html", build_publications),
    ("talks.html", build_talks), ("media.html", build_media),
    ("courses.html", build_courses),
]

if __name__ == "__main__":
    for fn, b in PAGES:
        open(fn, "w", encoding="utf-8").write(b())
        print("wrote", fn)
