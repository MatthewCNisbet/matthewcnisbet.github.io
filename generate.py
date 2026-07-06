#!/usr/bin/env python3
"""Generate the static site from alldata.json + CV/WoS-derived content."""
import json, re, html

data = json.load(open('alldata.json'))

# ---------- shared chrome ----------
# green-dot favicon as inline SVG data URI
FAVICON = ("data:image/svg+xml,"
  "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
  "%3Ccircle cx='16' cy='16' r='9' fill='%2300693E'/%3E%3C/svg%3E")

NAVITEMS = [("Bio/C.V.","bio.html"),("Publications","publications.html"),
            ("Talks","talks.html"),("Media","media.html"),("Substack","https://mattnisbet.substack.com")]

def head(title, active, depth_css="assets/css/style.css"):
    nav=""
    for label,href in NAVITEMS:
        cls=' class="active"' if label==active else ''
        nav+=f'<a href="{href}"{cls}>{html.escape(label)}</a>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,wght@0,400;0,600;0,700;1,400&display=swap">
<link rel="stylesheet" href="{depth_css}">
</head>
<body>
<header class="masthead"><div class="wrap">
  <a class="brand" href="index.html"><span class="bar"></span><span class="name">Matthew C. Nisbet</span></a>
  <nav class="main">{nav}</nav>
</div></header>
<main class="wrap">
"""

FOOTER = """</main>
<footer><div class="wrap">
  <span class="dot"></span>
  <a href="bio.html">Bio</a>
  <a href="talks.html">Talks &amp; lectures</a>
  <a href="media.html">News coverage</a>
  <a href="https://mattnisbet.substack.com">Counterpoints</a>
  <span>&copy; Matthew C. Nisbet</span>
</div></footer>
</body></html>"""

# ---------- citation rendering ----------
def italicize_venue(venue):
    # No italics anywhere per house style; render venue plain.
    return html.escape(venue)

def render_entry(it):
    title=it.get('title') or it.get('raw')
    authors=html.escape(it.get('authors',''))
    year=it.get('year','')
    venue=it.get('venue','')
    # title hyperlinked to DOI if present
    link=None
    if it.get('doi'):
        link=f'https://doi.org/{it["doi"]}'
    elif it.get('url'):
        link=it['url']
    if link:
        title_html=f'<a href="{html.escape(link)}">{html.escape(title)}</a>'
    else:
        title_html=html.escape(title)
    cite=f'{authors} ({year}). {title_html}. {italicize_venue(venue)}' if venue else f'{authors} ({year}). {title_html}.'
    return f'<div class="entry"><div class="cite">{cite}</div></div>'

# ---------- publications page ----------
SECTIONS=[('peerreviewed','Peer-reviewed studies/articles'),
          ('chapters','Book chapters'),
          ('reports','Reports/white papers'),
          ('essays','Essays/commentary'),
          ('edited','Edited volumes')]

def build_publications():
    h=head("Publications — Matthew C. Nisbet","Publications")
    h+='<h1 class="page">Publications</h1>'
    # jump index
    h+='<div class="jump">'
    for key,label in SECTIONS:
        h+=f'<a href="#{key}">{html.escape(label)}</a>'
    h+='</div>'
    for key,label in SECTIONS:
        h+=f'<h2 class="section" id="{key}">{html.escape(label)}</h2>'
        for it in data[key]:
            h+=render_entry(it)
    h+=FOOTER
    return h

with open('publications.html','w') as f:
    f.write(build_publications())

print("publications.html written")
print("peer-reviewed entries:", len(data['peerreviewed']))
print("with abstract panels:", sum(1 for i in data['peerreviewed'] if i.get('abstract')))
print("with DOI title links:", sum(1 for i in data['peerreviewed'] if i.get('doi')))

# ============================================================
#  Remaining pages
# ============================================================

# ---------- landing ----------
def build_index():
    h=head("Matthew C. Nisbet","")  # no active nav item on home
    h+="""
<section class="intro">
  <div class="text">
    <div class="title-1">Professor of communication, public policy, and urban affairs</div>
    <div class="title-2">Northeastern University-Boston MA</div>
    <p>I study how media and intellectuals shape public debate over science, technology, and the environment. My research spans climate change, the politics of expertise, and the place of contemplative practice in public life.</p>
    <p>I write <a href="https://mattnisbet.substack.com">Counterpoints</a>, a Substack on moderation, deep work, and the life of the mind for readers across policy, journalism, and the academy. Much of it grows out of <a href="publications.html#peerreviewed">peer-reviewed research</a> and <a href="publications.html#reports">policy reports</a> archived here.</p>
    <p>See my <a href="bio.html">full biography</a>, <a href="talks.html">talks</a>, or <a href="media.html">news coverage</a>.</p>
  </div>
  <div class="photo"><img src="assets/img/headshot.jpg" alt="Matthew C. Nisbet"></div>
</section>

<section class="news">
  <h2>News</h2>
  <div class="item"><div class="date">Jun 2026</div><div class="body">[Placeholder] New essay at Counterpoints: <a href="https://mattnisbet.substack.com">title</a>.</div></div>
  <div class="item"><div class="date">May 2026</div><div class="body">[Placeholder] New report released, with a <a href="https://mattnisbet.substack.com">summary</a> at Substack.</div></div>
  <div class="item"><div class="date">Apr 2026</div><div class="body">[Placeholder] Recent interview or talk.</div></div>
</section>
"""
    h+=FOOTER
    return h

# ---------- bio ----------
def build_bio():
    h=head("Bio & C.V. — Matthew C. Nisbet","Bio/C.V.")
    h+="""
<div class="bio-head">
  <div class="photo"><img src="assets/img/headshot.jpg" alt="Matthew C. Nisbet"></div>
  <div style="flex:1;">
    <div class="cvline"><a href="assets/pdf/Nisbet_CV.pdf">Curriculum Vitae</a></div>
    <div class="bio-body">
      <!-- BIO PLACEHOLDER: replace with your own third-person biography.
           Draft below is assembled from CV facts only. -->
      <p>Matthew C. Nisbet is Professor of Communication, Public Policy, and Urban Affairs at Northeastern University, where he studies the role of communication, media, and intellectuals in public debates over science, technology, and the environment.</p>
      <p>His research examines climate change and energy politics, the politics of expertise and knowledge-based journalism, public opinion about emerging science, and the cultural politics of wellness and contemplative practice. He is the editor of <em>The Oxford Encyclopedia of Climate Change Communication</em> and a co-author of the U.S. National Academies report <em>Communicating Science Effectively: A Research Agenda</em>. His <a href="publications.html#peerreviewed">peer-reviewed work</a> has been widely cited, and several papers rank among the most-cited in the field.</p>
      <p>He has held visiting positions and fellowships at Dartmouth College and Goucher College, and earned his Ph.D. and M.S. in Communication from Cornell University and his B.A. in Government from Dartmouth College.</p>
      <p>He writes <a href="https://mattnisbet.substack.com">Counterpoints</a>, a Substack for readers across policy, journalism, and the academy. His <a href="publications.html">publications</a>, <a href="talks.html">talks and lectures</a>, and <a href="media.html">news coverage and interviews</a> are collected on this site.</p>
    </div>
  </div>
</div>
"""
    h+=FOOTER
    return h

# ---------- courses ----------
COURSES = {
 "Northeastern University":[
   "Political Communication","Environmental Issues, Communication and Media",
   "Strategic Communication Capstone","Health Communication",
   "Climate Change Communication, Energy Politics and Journalism",
   "Media Advocacy and Communication Research"],
 "American University":[
   "Political Communication","Communication, Culture and Environment",
   "Public Communication Theory","Strategic Communication","Advanced Media Theory",
   "Ethical Persuasion","Public Communication Research Methods",
   "Communication and Society","Understanding Media"],
 "The Ohio State University":[
   "Mass Communication and Social Systems","Quantitative Reasoning for Journalism and Communication",
   "Communication Research Methods","Science Communication (Honors)","Mass Communication and Society"],
}
def build_courses():
    h=head("Courses — Matthew C. Nisbet","Courses")
    h+='<h1 class="page">Courses</h1>'
    h+='<div class="subnote">Selected courses taught. Syllabi and reading lists available on request.</div>'
    h+='<div class="content">'
    for inst,cs in COURSES.items():
        h+=f'<h2 class="section">{html.escape(inst)}</h2>'
        for c in cs:
            h+=f'<div class="course"><span class="ct">{html.escape(c)}</span></div>'
    h+='</div>'
    h+=FOOTER
    return h

# ---------- talks (placeholder structure) ----------
def build_talks():
    talks=json.load(open('talks.json'))
    h=head("Talks — Matthew C. Nisbet","Talks")
    h+='<h1 class="page">Talks</h1>'
    for t in talks:
        h+=f'<div class="entry"><div class="cite">{html.escape(t["raw"])}</div></div>'
    h+=FOOTER
    return h

# ---------- media (placeholder structure) ----------
def build_media():
    media=json.load(open('media.json'))
    h=head("Media — Matthew C. Nisbet","Media")
    h+='<h1 class="page">Media</h1>'
    for m in media:
        raw=m.get("raw","")
        url=m.get("url")
        if url:
            # link the article title: title is the sentence after the first ").  "
            mt=re.match(r'^(.*?\)\.\s*)(.+?)(\.\s.*)$', raw)
            if mt:
                cite=html.escape(mt.group(1))+f'<a href="{html.escape(url)}">'+html.escape(mt.group(2))+'</a>'+html.escape(mt.group(3))
            else:
                cite=html.escape(raw)
        else:
            cite=html.escape(raw)
        h+=f'<div class="entry"><div class="cite">{cite}</div></div>'
    h+=FOOTER
    return h

for fn,builder in [("index.html",build_index),("bio.html",build_bio),
                   ("talks.html",build_talks),("media.html",build_media)]:
    open(fn,'w').write(builder())
    print("wrote", fn)
