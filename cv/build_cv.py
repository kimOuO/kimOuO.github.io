# -*- coding: utf-8 -*-
"""由 cv_data.py 產生中英文 CV 的 HTML，並以 WeasyPrint 輸出 PDF。

    python3 build_cv.py

輸出：
    cv/cv-zh.html, cv/cv-en.html          可在瀏覽器預覽
    ../黃耀慶_中文CV.pdf                   網站「下載中文 CV」指向的檔案
    ../Yao-Ching_Huang_EN_CV.pdf          網站「Download CV (EN)」指向的檔案
"""
import os
from cv_data import ZH, EN, SKILLS, CONTACT

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

CSS = """
@page { size: A4; margin: 10mm 13mm 9mm 13mm; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Noto Sans CJK TC', 'Noto Sans TC', Arial, sans-serif;
       font-size: 8.4pt; line-height: 1.44; color: #22262e; }
a { color: #2E50CA; text-decoration: none; }

.head { display: flex; gap: 11px; align-items: flex-start; margin-bottom: 9px; }
.head img { width: 20mm; border-radius: 2px; }
.head-txt { flex: 1; }
.name { font-size: 20pt; font-weight: 700; letter-spacing: -0.01em; line-height: 1.1; }
.name small { font-size: 10.5pt; font-weight: 500; color: #5b6475; margin-left: 7px; letter-spacing: 0; }
.affil { font-size: 8pt; color: #5b6475; margin-top: 2px; }
.contact { font-size: 8pt; color: #2E50CA; margin-top: 2px; }
.contact span { color: #b9c0cd; margin: 0 9px; }

.skills { border-left: 2.5px solid #2E50CA; padding-left: 9px; margin: 9px 0 4px; }
.skills table { width: 100%; border-collapse: collapse; }
.skills td { padding: 0.7px 0; vertical-align: top; }
.sk-k { width: 46mm; font-weight: 700; font-size: 8pt; color: #1f2740; }
.sk-s { width: 5mm; color: #c7cedb; }
.sk-v { font-size: 8pt; color: #3a4150; }

h2 { font-size: 10.5pt; font-weight: 700; color: #2E50CA; margin: 9px 0 1px;
     padding-bottom: 2px; border-bottom: 1px solid #d8e0f0; }

.entry { margin-top: 5.5px; }
.entry.tight { margin-top: 4px; }
.e-head { display: flex; align-items: baseline; gap: 8px; }
.e-title { flex: 1; font-size: 8.8pt; font-weight: 700; color: #1b2030; }
.e-date { font-size: 7.6pt; color: #868f9e; white-space: nowrap; }
.e-sub { font-size: 8pt; color: #4a5160; margin-top: 1px; }
ul { list-style: none; margin-top: 1.5px; }
li { position: relative; padding-left: 10px; margin-bottom: 1.2px; }
li::before { content: '\\2022'; position: absolute; left: 1px; color: #9aa3b4; }
b { font-weight: 700; color: #11151d; }
.awards li { margin-bottom: 3.5px; }
"""

PAGE = """<!DOCTYPE html>
<html lang="{lang}">
<head><meta charset="UTF-8"><title>{title}</title><style>{css}</style></head>
<body>
{head}
<div class="skills"><table>{skills}</table></div>
{body}
</body></html>
"""


def render(d, out_html):
    photo = ('<img src="photo.jpg" alt="">' if d['photo'] else '')
    nm = d['name'] + (f" <small>{d['name_en']}</small>" if d['name_en'] else '')
    head = f"""<div class="head">{photo}<div class="head-txt">
  <div class="name">{nm}</div>
  <div class="affil">{d['affil']}</div>
  <div class="contact">{CONTACT['email']}<span>|</span>{CONTACT['github']}<span>|</span>{CONTACT['phone']}</div>
</div></div>"""

    skills = ''.join(
        f'<tr><td class="sk-k">{k}</td><td class="sk-s">|</td><td class="sk-v">{v}</td></tr>'
        for k, v in SKILLS)

    body = []
    for heading, kind, entries in d['sections']:
        body.append(f'<h2>{heading}</h2>')
        if kind == 'list':
            items = ''.join(f'<li>{i}</li>' for i in entries[0]['items'])
            body.append(f'<ul class="awards">{items}</ul>')
            continue
        for e in entries:
            cls = 'entry tight' if kind in ('edu', 'proj') else 'entry'
            parts = [f'<div class="{cls}">']
            if e['title']:
                parts.append('<div class="e-head">'
                             f'<div class="e-title">{e["title"]}</div>'
                             + (f'<div class="e-date">{e["date"]}</div>' if e['date'] else '')
                             + '</div>')
            if e['sub']:
                parts.append(f'<div class="e-sub">{e["sub"]}</div>')
            if e['items']:
                parts.append('<ul>' + ''.join(f'<li>{i}</li>' for i in e['items']) + '</ul>')
            parts.append('</div>')
            body.append(''.join(parts))

    html = PAGE.format(lang=d['lang'], title=d['name'], css=CSS + d.get('css', ''),
                       head=head, skills=skills, body='\n'.join(body))
    with open(out_html, 'w', encoding='utf-8') as f:
        f.write(html)
    return out_html


def main():
    from weasyprint import HTML
    jobs = [(ZH, 'cv-zh.html', '黃耀慶_中文CV.pdf'),
            (EN, 'cv-en.html', 'Yao-Ching_Huang_EN_CV.pdf')]
    for d, html_name, pdf_name in jobs:
        p = render(d, os.path.join(HERE, html_name))
        pdf = os.path.join(ROOT, pdf_name)
        HTML(filename=p).write_pdf(pdf)
        print('wrote', html_name, '->', pdf_name)


if __name__ == '__main__':
    main()
