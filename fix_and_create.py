import re
import os

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

index_html = index_html.replace(
'''    <!-- EDT 304 -->
    <div class="course-card coming" style="--card-color:#06b6d4;--icon-bg:rgba(6,182,212,0.08);--icon-border:rgba(6,182,212,0.2)">
      <div class="card-top">
        <div class="card-icon"><i class="ti ti-cpu"></i></div>
        <span class="avail-badge soon">Coming Soon</span>
      </div>
      <div class="card-code">EDT 304</div>
      <div class="card-name">Instructional Design &amp; Media</div>
      <div class="card-dept"><i class="ti ti-building" style="font-size:10px"></i> Education Technology</div>
      <div class="card-actions">
        <a class="btn-card-quiz" id="edt304-quiz-btn"><i class="ti ti-player-play" style="font-size:13px"></i> Quiz</a>
        <a class="btn-card-notes" id="edt304-notes-btn"><i class="ti ti-book-2" style="font-size:13px"></i> Notes</a>
      </div>
      <div class="coming-overlay"><div class="coming-pill"><i class="ti ti-clock" style="font-size:11px"></i> Coming Soon</div></div>
    </div>''',
'''    <!-- EDT 304 — ACTIVE -->
    <div class="course-card available" style="--card-color:#06b6d4;--icon-bg:rgba(6,182,212,0.1);--icon-border:rgba(6,182,212,0.25)">
      <div class="card-top">
        <div class="card-icon"><i class="ti ti-cpu"></i></div>
        <span class="avail-badge active">&#x25CF; Active</span>
      </div>
      <div class="card-code">EDT 304</div>
      <div class="card-name">Distance Learning: Concepts Models and Technologies</div>
      <div class="card-dept"><i class="ti ti-building" style="font-size:10px"></i> Education Technology</div>
      <div class="card-actions">
        <a class="btn-card-quiz" href="edt304_quiz.html" id="edt304-quiz-btn"><i class="ti ti-player-play" style="font-size:13px"></i> Quiz</a>
        <a class="btn-card-notes" href="edt304_notes.html" id="edt304-notes-btn"><i class="ti ti-book-2" style="font-size:13px"></i> Notes</a>
      </div>
    </div>'''
)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# 2. Fix bug in bua312_quiz.html and edt308_cbt_quiz (1).html
def fix_cbt(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    # fix white space
    if 'body{background:var(--bg);' not in html:
        html = re.compile(r'body\s*\{\s*').sub(r'body { background: #0a0f1e; ', html, count=1)
    # fix bug
    if 'function selectOpt(idx, btn) {' in html:
        html = html.replace('function selectOpt(idx, btn) {', 'function selectOpt(idx, btn) {\n  if (answers[cur] !== undefined) return;')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

fix_cbt('bua312_quiz.html')

with open('edt308_cbt_quiz (1).html', 'r', encoding='utf-8') as f:
    edt308_cbt = f.read()
if 'body { background: #0a0f1e;' not in edt308_cbt:
    edt308_cbt = edt308_cbt.replace('<body>', '<body style="background: #0a0f1e; margin: 0;">')
with open('edt308_cbt_quiz (1).html', 'w', encoding='utf-8') as f:
    f.write(edt308_cbt)

print("Updates successful")
