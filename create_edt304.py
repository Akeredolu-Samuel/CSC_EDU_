import os

def create_edt304_notes():
    with open('edt308_notes.html', 'r', encoding='utf-8') as f:
        notes_template = f.read()

    # We will just write the HTML manually since regex replacing 700 lines of specific content might be messy.
    # We can keep the top part of the template.
    head_end = notes_template.find('</style>') + 8
    head = notes_template[:head_end]
    head = head.replace('EDT 308 — Study Notes', 'EDT 304 — Study Notes')
    head = head.replace('Blended Learning, E-Moderation, E-tivities, Online Course Design', 'Distance Learning: Concepts Models and Technologies')

    body = """
</head>
<body style="background: #0a0f1e; margin: 0;">

<nav class="top-bar">
  <div class="tb-left">
    <a class="btn-back" href="index.html" id="back-btn"><i class="ti ti-arrow-left" style="font-size:13px"></i> Home</a>
    <div class="tb-title"><i class="ti ti-book-2" style="font-size:15px;color:#06b6d4"></i> EDT 304 — Study Notes</div>
    <span class="tb-badge" style="color:#06b6d4; border-color:rgba(6,182,212,0.3); background:rgba(6,182,212,0.1);">Active</span>
  </div>
  <a class="btn-quiz-link" href="edt304_quiz.html" id="take-quiz-btn" style="background:#06b6d4;"><i class="ti ti-player-play" style="font-size:13px"></i> Take Quiz</a>
</nav>

<div class="notes-layout">

  <!-- SIDEBAR -->
  <aside class="sidebar">
    <div class="sb-label">Contents</div>
    <a class="sb-link active" href="#sec1" id="sb-1"><span class="sb-num">1</span> Theories in Distance Learning</a>
    <a class="sb-link" href="#sec2" id="sb-2"><span class="sb-num">2</span> Paradigm Shift</a>
    <a class="sb-link" href="#sec3" id="sb-3"><span class="sb-num">3</span> Models of Distance Learning</a>
    <a class="sb-link" href="#sec4" id="sb-4"><span class="sb-num">4</span> Open Model in Distance Learning</a>
    <a class="sb-link" href="#sec5" id="sb-5"><span class="sb-num">5</span> Required Skills</a>
    <a class="sb-link" href="#sec6" id="sb-6"><span class="sb-num">6</span> Sync & Async Platforms</a>
  </aside>

  <!-- MAIN -->
  <main class="notes-main">

    <div class="notes-hero" style="background:linear-gradient(135deg,rgba(6,182,212,0.08),rgba(139,92,246,0.06));border:0.5px solid rgba(6,182,212,0.2);">
      <div class="nh-tag" style="color:#06b6d4;"><i class="ti ti-school" style="font-size:13px"></i> Compiled Study Notes</div>
      <div class="nh-title">Distance Learning: Concepts Models and Technologies</div>
      <div class="nh-sub">Lecturer: Dr. Ayinde &nbsp;&middot;&nbsp; Resources from Uthtech Solutions</div>
      <div class="topic-tags">
        <span class="topic-tag">Transactional Distance</span>
        <span class="topic-tag">MOOCs</span>
        <span class="topic-tag">Connectivism</span>
        <span class="topic-tag">ODL</span>
        <span class="topic-tag">Sync & Async</span>
      </div>
    </div>

    <!-- SECTION 1 -->
    <section class="notes-section" id="sec1">
      <div class="sec-header">
        <div class="sec-num" style="color:#06b6d4; border-color:rgba(6,182,212,0.3); background:rgba(6,182,212,0.1);">1</div>
        <div><div class="sec-title">Theories relating to Distance Learning</div><div class="sec-src">Objective 1</div></div>
      </div>
      
      <p>Distance Learning is also called distance education. It is a form of education in which the teacher and student are physically separated for most or all of the instructional process. Learning occurs without attending a traditional classroom.</p>
      <p>Distance learning has evolved significantly with technology, shifting from paper-based correspondence to fully digital and interactive platforms. It serves learners who cannot attend conventional schooling due to location, work, disability, or personal circumstances.</p>

      <h3>1. Transactional Distance Theory (TDT)</h3>
      <p>Founded by Michael Moore (1973), this was one of the most important and specific theories for distance education. Its core idea is that distance in distance education is not just physical (kilometres apart). It is a psychological and communication gap between learners and the teacher.</p>
      <div class="highlight-box">
        <div class="hb-label"><i class="ti ti-info-circle"></i> Transactional Distance Gap</div>
        <p>Moore called this gap 'Transactional Distance.' He argued that the gap increases when there is less dialogue and more rigid course structure. Good course design reduces this gap even when learners are far away.</p>
      </div>

      <h3>2. E-Learning Theory</h3>
      <p>Associated with scholars like Ruth Clark and Richard Mayer, addresses how digital tools and multimedia facilitate effective online learning. It draws from cognitive science, emphasizing that learners process information better when visuals and audio are well-coordinated.</p>
      <p>The core argument is that e-learning is most effective when technology is used to purposefully support, not replace – sound instructional design.</p>

      <h3>3. Community of Inquiry Theory (COI)</h3>
      <p>Developed by Garrison, Anderson & Archer, COI posits that meaningful online learning occurs through three overlapping presences:</p>
      <ul class="bullet-list">
        <li><strong>Social Presence:</strong> real interaction between participants</li>
        <li><strong>Cognitive Presence:</strong> critical thinking and problem-solving</li>
        <li><strong>Teaching Presence:</strong> design and facilitation of learning</li>
      </ul>

      <h3>4. Connectivism Theory</h3>
      <p>Developed by George Siemens, Connectivism is often called the 'learning theory for the digital age.' It argues that knowledge is distributed across networks, and learning is the process of connecting nodes or sources of information; both human and digital.</p>

      <h3>5. Andragogy Theory</h3>
      <p>Malcolm Knowles' Andragogy theory focuses on adult learners. It argues that adults are self-directed, bring prior experience to learning, are motivated by relevance, and prefer problem-centred approaches. This is especially relevant in distance education where most learners are adults.</p>

      <h3>6. Constructivism Theory</h3>
      <p>Constructivism holds that learners actively build (construct) their own understanding from experiences. In distance learning, this means instructional design should include activities, discussions, and projects {not just passive content delivery}.</p>
    </section>

    <div class="divider"></div>

    <!-- SECTION 2 -->
    <section class="notes-section" id="sec2">
      <div class="sec-header">
        <div class="sec-num" style="color:#06b6d4; border-color:rgba(6,182,212,0.3); background:rgba(6,182,212,0.1);">2</div>
        <div><div class="sec-title">Paradigm Shift in Distance Learning</div><div class="sec-src">Objective 2</div></div>
      </div>
      
      <p>The paradigm shift in distance learning refers to how the mode and approach to distance education has changed from the 19th to the 21st century.</p>
      <p>A paradigm shift means a fundamental change in the way something is understood or practiced. In distance learning, each era introduced new tools that radically changed how learning was delivered and experienced.</p>

      <ul class="bullet-list">
        <li><strong>1. Correspondence to Connectivity (19th–20th Century):</strong> During this period, learning was paper-based. Students received printed materials by mail and submitted assignments the same way.</li>
        <li><strong>2. Broadcast and Multimedia Expansion (Mid-20th Century):</strong> Radio and television were used for learning and instruction during this period. This stage made learning more accessible, as it could reach learners in remote areas.</li>
        <li><strong>3. Digital Beginning (1980–1990):</strong> The computer was introduced and used for learning. This period marked the beginning of digital education infrastructure. Early computer-based learning was mostly offline using CDs and floppy disks, but it set the groundwork for internet-based learning.</li>
        <li><strong>4. Internet and Online Learning (1990–2000s):</strong> Learners could learn through emails, forums, and Learning Management Systems (LMS). This era embraced two-way communication. Students could interact with peers and instructors across borders. LMS platforms like Moodle and Blackboard emerged during this era.</li>
        <li><strong>5. Massive Open Online Courses and Globalisation (MOOCs):</strong> In this era, education became scalable, flexible, and affordable. MOOCs allowed thousands of learners globally to access courses from top institutions at little or no cost.</li>
        <li><strong>6. Current Paradigm – [Personalised and Hybrid Learning]:</strong> The current paradigm includes AI-driven platforms, Mobile learning, and Hybrid learning.</li>
      </ul>

      <p>AI platforms now personalise learning experiences by adapting content to a learner's pace and performance. Hybrid learning blends online and in-person elements for a more flexible, student-centred experience.</p>
    </section>

    <div class="divider"></div>

    <!-- SECTION 3 -->
    <section class="notes-section" id="sec3">
      <div class="sec-header">
        <div class="sec-num" style="color:#06b6d4; border-color:rgba(6,182,212,0.3); background:rgba(6,182,212,0.1);">3</div>
        <div><div class="sec-title">Models of Distance Learning</div><div class="sec-src">Objective 3</div></div>
      </div>

      <p>Distance learning models describe the different structural approaches through which distance education is delivered. Each model has unique features suited to different learner needs and institutional capacities.</p>

      <h3>1. Fully Online Learning Model</h3>
      <p>This model is delivered entirely via the internet using platforms like Moodle, Blackboard, or Canvas. Features: Videos, Discussion Forums, Online assignments and assessments.</p>
      <ul class="bullet-list">
        <li><strong>Advantages:</strong> Flexibility, Global reach, Cost-effective.</li>
        <li><strong>Disadvantages:</strong> Requires strong digital literacy and reliable internet access. Highly dependent on technology infrastructure.</li>
      </ul>

      <h3>2. Blended [Hybrid] Learning</h3>
      <p>This model combines physical classroom instruction with online components. Features: Students attend physical classes but also engage in online discussion, live quizzes, and access to resources. Increasingly popular post-COVID-19.</p>
      <ul class="bullet-list">
        <li><strong>Advantages:</strong> Balances human interaction with digital flexibility.</li>
        <li><strong>Disadvantages:</strong> Needs careful integration to avoid duplication or confusion.</li>
      </ul>

      <h3>3. Mobile Learning (M-Learning)</h3>
      <p>Learning approach that takes place through smart phones, tablets, and handheld devices. Features: apps, podcasts, WhatsApp, study groups, SMS-based learning.</p>
      <ul class="bullet-list">
        <li><strong>Advantages:</strong> Highly accessible, especially in regions with limited infrastructure.</li>
        <li><strong>Disadvantages:</strong> Small screen size, Data cost, Distraction.</li>
      </ul>

      <h3>4. Competency-Based Learning</h3>
      <p>Student progress by demonstrating mastery of skills rather than completing a fixed time period. Features: Self-paced modules, Assessment tied to competencies.</p>
      <ul class="bullet-list">
        <li><strong>Advantages:</strong> Encourages personal learning, Outcome-focused, Efficient for skills acquisition.</li>
        <li><strong>Disadvantages:</strong> Requires robust assessment framework and accreditation standards.</li>
      </ul>

      <h3>5. Massive Open Online Courses (MOOCs)</h3>
      <p>Free or low-cost courses offered online to large numbers of learners. Platforms like Coursera, edX, and FutureLearn are popular. Despite high enrolment, completion rates average around 5-15%.</p>
      <ul class="bullet-list">
        <li><strong>Advantages:</strong> Democratizes education, Encourages global accessibility and scalability.</li>
        <li><strong>Disadvantages:</strong> Limits personal interaction, Brings about a high dropout rate.</li>
      </ul>

      <h3>6. Virtual University</h3>
      <p>A fully online institution that exists entirely online and offers full degree certification. Features: Structured curricula, Accreditation, Online faculty support.</p>
    </section>

    <div class="divider"></div>

    <!-- SECTION 4 -->
    <section class="notes-section" id="sec4">
      <div class="sec-header">
        <div class="sec-num" style="color:#06b6d4; border-color:rgba(6,182,212,0.3); background:rgba(6,182,212,0.1);">4</div>
        <div><div class="sec-title">Open Model in Distance Learning</div><div class="sec-src">Objective 4</div></div>
      </div>

      <p>The Open Model refers to Open and Distance Learning (ODL). These are educational approaches which minimise or remove traditional barriers to access, participation, and success. ODL is the dominant model used by many national universities in Africa and developing countries.</p>

      <h3>Characteristics of the Open Model</h3>
      <ul class="bullet-list">
        <li><strong>1. Open Admission:</strong> Minimal entry requirements. Recognition of prior learning (RPL) is often accepted.</li>
        <li><strong>2. Open Access:</strong> Available regardless of location, socio-economic status, gender, or disability. Also age-based (no age restrictions).</li>
        <li><strong>3. Open Pace:</strong> Encourages self-pace or flexible scheduling. Learners progress at their own speed.</li>
        <li><strong>4. Open Content/Resources:</strong> Makes heavy use of Open Educational Resources (OER) – reusable materials under Creative Commons licenses (e.g. MIT OpenCourseWare).</li>
      </ul>

      <h3>Institutional Models in ODL</h3>
      <ul class="bullet-list">
        <li><strong>Single-Mode Institution:</strong> Dedicate solely to distance education (e.g. NOUN, Open University UK).</li>
        <li><strong>Dual-Mode Institution:</strong> Traditional universities offering both on-campus and distance programmes simultaneously (e.g. LASU, Unilag).</li>
      </ul>

      <h3>Advantages and Disadvantages of ODL</h3>
      <ul class="bullet-list">
        <li><strong>Advantages:</strong> Supports lifelong learning and equity, cost-effective, democratises higher education.</li>
        <li><strong>Disadvantages:</strong> High dropout rate, digital divide (internet/electricity), quality and assessment integrity issues, hidden costs.</li>
      </ul>
    </section>

    <div class="divider"></div>

    <!-- SECTION 5 -->
    <section class="notes-section" id="sec5">
      <div class="sec-header">
        <div class="sec-num" style="color:#06b6d4; border-color:rgba(6,182,212,0.3); background:rgba(6,182,212,0.1);">5</div>
        <div><div class="sec-title">Required Skills in Distance Learning</div><div class="sec-src">Objective 5</div></div>
      </div>

      <p>Distance learners must develop certain skills to succeed without the constant physical presence of instructors.</p>
      
      <div class="skills-grid">
        <div class="skill-card">
          <div class="skill-name" style="color:#06b6d4">1. Self-Regulated Learning (SRL)</div>
          <div class="skill-desc">Advanced time management, goal setting, self-motivation. Without it, learners struggle with procrastination.</div>
        </div>
        <div class="skill-card">
          <div class="skill-name" style="color:#06b6d4">2. Digital and Information Literacy</div>
          <div class="skill-desc">Mastery of LMS (like NOUN & LASU Platforms), critical evaluation of resources, data/file management.</div>
        </div>
        <div class="skill-card">
          <div class="skill-name" style="color:#06b6d4">3. Communication & Collaboration</div>
          <div class="skill-desc">Ability to communicate effectively in writing (emails, forums) and participate in virtual group work.</div>
        </div>
        <div class="skill-card">
          <div class="skill-name" style="color:#06b6d4">4. Critical Thinking & Problem Solving</div>
          <div class="skill-desc">Analyze complex material without immediate lecturer support.</div>
        </div>
        <div class="skill-card">
          <div class="skill-name" style="color:#06b6d4">5. Lifelong Learning & Adaptability</div>
          <div class="skill-desc">Building a personal learning network (PLN) and embracing continuous self-development.</div>
        </div>
      </div>
    </section>

    <div class="divider"></div>

    <!-- SECTION 6 -->
    <section class="notes-section" id="sec6">
      <div class="sec-header">
        <div class="sec-num" style="color:#06b6d4; border-color:rgba(6,182,212,0.3); background:rgba(6,182,212,0.1);">6</div>
        <div><div class="sec-title">Synchronous and Asynchronous Platforms</div><div class="sec-src">Objective 6</div></div>
      </div>

      <h3>1. Synchronous Learning</h3>
      <p>Real-time, live interaction between instructors and learners at the same time. Examples: Zoom, Google Meet, Microsoft Teams, Live Webinars.</p>
      <ul class="bullet-list">
        <li><strong>Advantages:</strong> Immediate interaction reduces transactional distance, builds Social Presence (Community of Inquiry Theory), enables instant clarification.</li>
        <li><strong>Disadvantages:</strong> Requires stable internet at a fixed time, does not support Open Pace, time zone differences.</li>
      </ul>

      <h3>2. Asynchronous Learning</h3>
      <p>Learning that does not happen in real-time. Learners access materials and interact at their own chosen time. Examples: Moodle, WhatsApp Groups, Pre-recorded Lectures, Podcasts.</p>
      <ul class="bullet-list">
        <li><strong>Advantages:</strong> Supports Self-Regulated Learning (SRL), compatible with Open Pace, accessible via mobile devices offline.</li>
        <li><strong>Disadvantages:</strong> Delayed feedback can increase transactional distance, requires strong self-motivation, can feel isolating.</li>
      </ul>
      
      <p><strong>Conclusion:</strong> The current paradigm of Hybrid/Blended Learning offers the best solution – combining both approaches for a flexible, student-centred experience.</p>
    </section>

  </main>
</div>

<footer class="hub-footer">
  EDT 304 &nbsp;&middot;&nbsp; <span>Resources from Uthtech Solutions &nbsp;&middot;&nbsp; Built by samwissy</span>
</footer>

</body>
</html>
"""

    with open('edt304_notes.html', 'w', encoding='utf-8') as f:
        f.write(head + body)

def create_edt304_quiz():
    with open('bua312_quiz.html', 'r', encoding='utf-8') as f:
        quiz_template = f.read()

    # Replacing strings in the template to match EDT 304
    quiz_html = quiz_template.replace('BUA 312 — CBT Practice Quiz', 'EDT 304 — CBT Practice Quiz')
    quiz_html = quiz_html.replace('CBT practice quizzes for BUA 312: Small Business Management.', 'CBT practice quizzes for EDT 304: Distance Learning: Concepts Models and Technologies.')
    
    quiz_html = quiz_html.replace('BUA 312 — Small Business Management', 'EDT 304 — Distance Learning')
    
    
    # Update read box
    read_box_old = '''<li>Definitions &amp; Characteristics of Small Business</li>
      <li>Types, Advantages &amp; Disadvantages</li>
      <li>Entrepreneurial Skills &amp; Thinking</li>
      <li>Starting, Financing &amp; Managing a Business</li>
      <li>Small Business Environment &amp; HRM</li>
      <li>Challenges &amp; Prospects in Nigeria</li>'''
    
    read_box_new = '''<li>Theories relating to Distance Learning</li>
      <li>Paradigm Shift in Distance Learning</li>
      <li>Models of Distance Learning</li>
      <li>Open Model in Distance Learning</li>
      <li>Required Skills in Distance Learning</li>
      <li>Synchronous and Asynchronous Platforms in Distance Learning</li>'''
    
    quiz_html = quiz_html.replace(read_box_old, read_box_new)
    
    # Update difficulty select
    diff_old = '''<option value="obj1">Definitions &amp; Characteristics</option>
      <option value="obj2">Entrepreneurship &amp; Skills</option>
      <option value="obj3">Finance, Environment &amp; HRM</option>'''
      
    diff_new = '''<option value="obj1">Theories & Paradigm Shift</option>
      <option value="obj2">Models & Open Model</option>
      <option value="obj3">Skills & Platforms</option>'''
      
    quiz_html = quiz_html.replace(diff_old, diff_new)
    
    # Replace BUA 312 references
    quiz_html = quiz_html.replace('BUA 312', 'EDT 304')
    quiz_html = quiz_html.replace('bua312_notes.html', 'edt304_notes.html')
    
    # Replace color scheme
    # f97316 to 06b6d4 (cyan-500)
    quiz_html = quiz_html.replace('#f97316', '#06b6d4')
    quiz_html = quiz_html.replace('rgba(249,115,22,0.08)', 'rgba(6,182,212,0.08)')
    quiz_html = quiz_html.replace('rgba(249,115,22,0.07)', 'rgba(6,182,212,0.07)')
    quiz_html = quiz_html.replace('rgba(249,115,22,0.25)', 'rgba(6,182,212,0.25)')
    quiz_html = quiz_html.replace('rgba(249,115,22,0.15)', 'rgba(6,182,212,0.15)')
    quiz_html = quiz_html.replace('rgba(249,115,22,0.35)', 'rgba(6,182,212,0.35)')
    quiz_html = quiz_html.replace('rgba(249,115,22,0.3)', 'rgba(6,182,212,0.3)')
    quiz_html = quiz_html.replace('rgba(249,115,22,0.12)', 'rgba(6,182,212,0.12)')
    quiz_html = quiz_html.replace('rgba(249,115,22,0.4)', 'rgba(6,182,212,0.4)')
    quiz_html = quiz_html.replace('rgba(249,115,22,0.1)', 'rgba(6,182,212,0.1)')
    quiz_html = quiz_html.replace('#ea6c08', '#0891b2')
    
    # Replace BANK
    bank_code_start = quiz_html.find('const BANK = [')
    bank_code_end = quiz_html.find('];\n\nlet pool = [], cur')
    
    new_bank = '''const BANK = [
  { q: "Which theory focuses on the psychological and communication gap between learners and the teacher?", opts: ["E-Learning Theory","Community of Inquiry Theory","Transactional Distance Theory","Connectivism Theory"], ans: 2, exp: "Transactional Distance Theory (Moore, 1973) states that distance is psychological, requiring dialogue to bridge the gap.", hint: "Topic: TDT", sec: "Theories" },
  { q: "According to Community of Inquiry (COI) Theory, meaningful learning requires three presences: Social, Teaching, and...", opts: ["Physical Presence","Cognitive Presence","Technological Presence","Psychological Presence"], ans: 1, exp: "COI posits learning requires Social, Cognitive, and Teaching presences.", hint: "Topic: COI", sec: "Theories" },
  { q: "Which theory is often called the 'learning theory for the digital age'?", opts: ["Andragogy Theory","Connectivism Theory","Constructivism Theory","E-Learning Theory"], ans: 1, exp: "Connectivism (Siemens) argues that knowledge is distributed across networks.", hint: "Topic: Connectivism", sec: "Theories" },
  { q: "The era of learning characterised by paper-based learning delivered through mail is known as:", opts: ["Digital Beginning","Correspondence to Connectivity","Broadcast and Multimedia Expansion","MOOCs"], ans: 1, exp: "The 19th-20th century era used printed materials sent via mail.", hint: "Topic: Paradigm Shift", sec: "Paradigm Shift" },
  { q: "Which distance learning model describes free or low-cost courses offered online to thousands of learners?", opts: ["Blended Learning","Mobile Learning","Massive Open Online Courses (MOOCs)","Virtual University"], ans: 2, exp: "MOOCs democratize education by reaching massive numbers globally.", hint: "Topic: MOOCs", sec: "Models" },
  { q: "What does 'Open Pace' mean in Open and Distance Learning (ODL)?", opts: ["No age restrictions","Free educational materials","Learners progress at their own speed/flexible scheduling","Minimal entry requirements"], ans: 2, exp: "Open Pace encourages self-pace and flexible scheduling.", hint: "Topic: ODL Characteristics", sec: "Open Model" },
  { q: "A traditional university that offers both on-campus and distance programmes is called a:", opts: ["Single-Mode Institution","Virtual University","Dual-Mode Institution","MOOC"], ans: 2, exp: "Dual-Mode Institutions like LASU and Unilag offer both face-to-face and distance learning.", hint: "Topic: Institutional Models", sec: "Open Model" },
  { q: "Which required skill is perhaps the most critical for preventing procrastination in distance learning?", opts: ["Digital Literacy","Self-Regulated Learning (SRL)","Communication Skills","Critical Thinking"], ans: 1, exp: "SRL involves advanced time management and self-motivation to combat procrastination.", hint: "Topic: Required Skills", sec: "Skills" },
  { q: "Which is an example of an Asynchronous Platform?", opts: ["Zoom","Live Webinars","Microsoft Teams","Discussion Forums on Moodle"], ans: 3, exp: "Forums are asynchronous because learners participate at different times.", hint: "Topic: Platforms", sec: "Platforms" },
  { q: "Which of the following is a disadvantage of Synchronous Learning?", opts: ["Delayed feedback","Requires stable internet at a fixed time","Can feel isolating","High schedule flexibility"], ans: 1, exp: "Synchronous learning requires stable internet at a specific, fixed time, reducing flexibility.", hint: "Topic: Sync vs Async", sec: "Platforms" },
  { q: "When designing a program for rural students with limited internet, which strategy reduces the psychological gap according to Transactional Distance Theory?", opts: ["Mandatory 3-hour Zoom sessions","Asynchronous Audio/SMS check-ins","Extensive high-definition video lectures","Virtual Reality simulations"], ans: 1, exp: "Audio/SMS check-ins increase dialogue without requiring high bandwidth.", hint: "Topic: Test Question 1", sec: "Case Study" },
  { q: "In the context of Nigerian distance education, how does the shift to AI-driven personalized learning impact learners?", opts: ["It reduces learner autonomy.","It increases engagement through instant feedback loops.","It entirely replaces the need for human instructors.","It causes absolute disengagement in all scenarios."], ans: 1, exp: "AI-driven platforms adapt to learners, increasing autonomy and engagement via instant feedback.", hint: "Topic: Test Question 2", sec: "Case Study" },
  { q: "Andragogy Theory focuses primarily on:", opts: ["Children's learning","Digital network nodes","Adult learners","Multimedia processing"], ans: 2, exp: "Malcolm Knowles' Andragogy focuses on adult learners who are self-directed.", hint: "Topic: Theories", sec: "Theories" },
  { q: "Which model combines physical classroom instruction with online components?", opts: ["Fully Online Learning Model","Virtual University","Competency-Based Learning","Blended [Hybrid] Learning"], ans: 3, exp: "Blended or Hybrid learning balances face-to-face with digital flexibility.", hint: "Topic: Models", sec: "Models" },
  { q: "According to the notes, what is the completion rate average for MOOCs?", opts: ["50-60%","70-80%","90-100%","5-15%"], ans: 3, exp: "Despite high enrollment numbers, MOOC completion rates tend to be low, averaging 5-15%.", hint: "Topic: MOOCs", sec: "Models" },
  { q: "What does 'distance' refer to in distance education according to its basic definition?", opts: ["Physical separation of teacher and student", "A new method of internet communication", "Only geographical distance measured in kilometres", "The time taken to grade assignments"], ans: 0, exp: "Distance refers to the physical separation for most or all of the instructional process.", hint: "Topic: Definition", sec: "Theories" },
  { q: "Which theory specifically emphasizes that distance is psychological and requires dialogue to bridge the gap?", opts: ["Constructivism Theory", "Connectivism Theory", "Transactional Distance Theory", "Andragogy Theory"], ans: 2, exp: "Moore's theory argues that distance is psychological and communication-based.", hint: "Topic: TDT", sec: "Theories" },
  { q: "Michael Moore is associated with which foundational distance learning theory?", opts: ["E-Learning Theory", "Transactional Distance Theory", "Community of Inquiry Theory", "Connectivism Theory"], ans: 1, exp: "Michael Moore founded the Transactional Distance Theory in 1973.", hint: "Topic: TDT", sec: "Theories" },
  { q: "According to Transactional Distance Theory, the gap increases when there is:", opts: ["More dialogue and less structure", "Less dialogue and more rigid course structure", "No internet connection available", "A lack of adult learners"], ans: 1, exp: "Less dialogue and higher structure increase the transactional distance.", hint: "Topic: TDT", sec: "Theories" },
  { q: "Which theory addresses how digital tools and multimedia facilitate effective online learning?", opts: ["Constructivism Theory", "Community of Inquiry Theory", "Andragogy Theory", "E-Learning Theory"], ans: 3, exp: "E-Learning theory deals with digital tools and multimedia.", hint: "Topic: E-Learning", sec: "Theories" },
  { q: "E-Learning theory draws heavily from which field of science?", opts: ["Quantum Mechanics", "Cognitive Science", "Biology", "Sociology"], ans: 1, exp: "It draws from cognitive science regarding how learners process information.", hint: "Topic: E-Learning", sec: "Theories" },
  { q: "According to E-Learning Theory, learners process information better when:", opts: ["It is only in text format", "Visuals and audio are well-coordinated", "There are no multimedia elements", "It is delivered entirely through mobile phones"], ans: 1, exp: "Information is processed better when visuals and audio are well-coordinated.", hint: "Topic: E-Learning", sec: "Theories" },
  { q: "Who are the developers of the Community of Inquiry (COI) Theory?", opts: ["Michael Moore", "Ruth Clark and Richard Mayer", "Garrison, Anderson & Archer", "George Siemens"], ans: 2, exp: "COI was developed by Garrison, Anderson & Archer.", hint: "Topic: COI", sec: "Theories" },
  { q: "Which presence in the Community of Inquiry Theory involves critical thinking and problem-solving?", opts: ["Teaching Presence", "Cognitive Presence", "Social Presence", "Physical Presence"], ans: 1, exp: "Cognitive presence deals with critical thinking and problem-solving.", hint: "Topic: COI", sec: "Theories" },
  { q: "Which theory argues that knowledge is distributed across networks?", opts: ["Andragogy Theory", "Connectivism Theory", "E-Learning Theory", "Transactional Distance Theory"], ans: 1, exp: "Connectivism argues knowledge is distributed across networks.", hint: "Topic: Connectivism", sec: "Theories" },
  { q: "Malcolm Knowles is best known for which theory focusing on adult learners?", opts: ["Constructivism Theory", "Community of Inquiry Theory", "Andragogy Theory", "Connectivism Theory"], ans: 2, exp: "Andragogy focuses on adult learners, developed by Malcolm Knowles.", hint: "Topic: Andragogy", sec: "Theories" },
  { q: "Which theory holds that learners actively build their own understanding from experiences?", opts: ["Constructivism Theory", "Andragogy Theory", "Connectivism Theory", "E-Learning Theory"], ans: 0, exp: "Constructivism states that learners construct their own understanding.", hint: "Topic: Constructivism", sec: "Theories" },
  { q: "During the 19th-20th century, distance learning was primarily delivered through:", opts: ["Radio broadcast", "Paper-based correspondence", "Emails", "Learning Management Systems"], ans: 1, exp: "It was the era of correspondence to connectivity.", hint: "Topic: Paradigm", sec: "Paradigm Shift" },
  { q: "Which technology was characteristic of the 'Broadcast and Multimedia Expansion' era?", opts: ["Radio and television", "Floppy disks and CDs", "Internet forums", "Mobile apps"], ans: 0, exp: "Mid-20th century saw the use of radio and TV.", hint: "Topic: Paradigm", sec: "Paradigm Shift" },
  { q: "The 'Digital Beginning' era in the 1980s-1990s was characterized by learning using:", opts: ["Radio", "Mail correspondence", "Offline computers with CDs and floppy disks", "Live Zoom sessions"], ans: 2, exp: "Digital Beginning used computers, CDs and floppy disks.", hint: "Topic: Paradigm", sec: "Paradigm Shift" },
  { q: "Which platforms emerged during the 'Internet and Online Learning' era?", opts: ["Television networks", "Learning Management Systems (LMS) like Moodle", "Virtual Reality", "Radio broadcasts"], ans: 1, exp: "LMS platforms emerged during the Internet era.", hint: "Topic: Paradigm", sec: "Paradigm Shift" },
  { q: "What does MOOC stand for?", opts: ["Massive Online Operational Course", "Mainstream Open Online Classes", "Massive Open Online Courses", "Multiple Offline Organized Courses"], ans: 2, exp: "MOOCs allow thousands of learners to access courses globally.", hint: "Topic: Paradigm", sec: "Paradigm Shift" },
  { q: "The current paradigm of distance learning relies heavily on:", opts: ["Radio and TV", "Paper and mail", "AI-driven platforms and Hybrid learning", "CD-ROMs"], ans: 2, exp: "Current paradigm includes AI-driven and Hybrid learning.", hint: "Topic: Paradigm", sec: "Paradigm Shift" },
  { q: "How do AI platforms personalize learning experiences today?", opts: ["By adapting content to a learner's pace and performance", "By completely removing the need for a curriculum", "By replacing all human contact", "By enforcing a rigid course structure"], ans: 0, exp: "AI adapts content to a learner's pace and performance.", hint: "Topic: Paradigm", sec: "Paradigm Shift" },
  { q: "A model delivered entirely via the internet using platforms like Canvas or Blackboard is called:", opts: ["Blended Learning", "Fully Online Learning Model", "Virtual University", "Competency-Based Learning"], ans: 1, exp: "Fully Online Learning Model is delivered entirely via the internet.", hint: "Topic: Models", sec: "Models" },
  { q: "What is a major disadvantage of the Fully Online Learning Model?", opts: ["It is not scalable", "It requires strong digital literacy and reliable internet", "It offers no flexibility", "It is extremely expensive compared to traditional schooling"], ans: 1, exp: "It heavily depends on technology infrastructure and digital literacy.", hint: "Topic: Models", sec: "Models" },
  { q: "Which model is described as increasingly popular post-COVID-19?", opts: ["Mobile Learning", "Blended [Hybrid] Learning", "Competency-Based Learning", "Virtual University"], ans: 1, exp: "Blended Learning combines physical and online learning.", hint: "Topic: Models", sec: "Models" },
  { q: "A major advantage of Mobile Learning (M-Learning) is:", opts: ["It provides a large screen for viewing complex diagrams", "It completely eliminates data costs", "It is highly accessible, especially in regions with limited infrastructure", "It forces students to attend physical classes"], ans: 2, exp: "M-Learning is highly accessible, even with limited infrastructure.", hint: "Topic: Models", sec: "Models" },
  { q: "In which model do students progress by demonstrating mastery of skills rather than completing a fixed time period?", opts: ["Virtual University", "Competency-Based Learning", "Fully Online Learning Model", "MOOCs"], ans: 1, exp: "Competency-Based Learning focuses on mastery of skills.", hint: "Topic: Models", sec: "Models" },
  { q: "What is the typical completion rate for Massive Open Online Courses (MOOCs) despite their high enrolment?", opts: ["90-100%", "50-70%", "5-15%", "30-40%"], ans: 2, exp: "MOOCs have high dropout rates, with completion around 5-15%.", hint: "Topic: Models", sec: "Models" },
  { q: "A fully online institution that exists entirely online and offers full degree certification is called a:", opts: ["MOOC", "Dual-Mode Institution", "Virtual University", "Blended Learning Center"], ans: 2, exp: "Virtual Universities offer full degree certification entirely online.", hint: "Topic: Models", sec: "Models" },
  { q: "What does ODL stand for?", opts: ["Online Distance Logic", "Open and Distance Learning", "Offline and Digital Learning", "Organized Distance Learning"], ans: 1, exp: "ODL stands for Open and Distance Learning.", hint: 'Topic: Open Model', sec: "Open Model" },
  { q: "Which characteristic of the Open Model means there are minimal entry requirements?", opts: ["Open Access", "Open Pace", "Open Admission", "Open Content"], ans: 2, exp: "Open Admission minimizes entry barriers and accepts prior learning.", hint: 'Topic: Open Model', sec: "Open Model" },
  { q: "Which characteristic of ODL encourages flexible scheduling?", opts: ["Open Admission", "Open Content", "Open Pace", "Open Access"], ans: 2, exp: "Open Pace allows learners to progress at their own speed.", hint: 'Topic: Open Model', sec: "Open Model" },
  { q: "OER stands for:", opts: ["Online Educational Registration", "Open Educational Resources", "Offline Electronic Resources", "Open Evaluation Rules"], ans: 1, exp: "OER refers to reusable materials under open licenses.", hint: 'Topic: Open Model', sec: "Open Model" },
  { q: "An institution dedicated solely to distance education is known as a:", opts: ["Dual-Mode Institution", "Single-Mode Institution", "Virtual University", "Blended Institution"], ans: 1, exp: "Single-Mode Institutions are dedicated entirely to distance education.", hint: 'Topic: Open Model', sec: "Open Model" },
  { q: "NOUN (National Open University of Nigeria) is an example of a:", opts: ["Dual-Mode Institution", "Single-Mode Institution", "Traditional University", "Competency-Based Center"], ans: 1, exp: "NOUN is a Single-Mode Institution.", hint: 'Topic: Open Model', sec: "Open Model" },
  { q: "LASU and Unilag offering both on-campus and distance programmes makes them:", opts: ["Single-Mode Institutions", "Dual-Mode Institutions", "Virtual Universities", "MOOCs"], ans: 1, exp: "Institutions offering both are Dual-Mode Institutions.", hint: 'Topic: Open Model', sec: "Open Model" },
  { q: "Which of the following is a disadvantage of ODL?", opts: ["It democratises higher education", "It supports lifelong learning", "High dropout rate and digital divide", "It is cost-effective"], ans: 2, exp: "High dropout rates and digital divide are major disadvantages.", hint: 'Topic: Open Model', sec: "Open Model" },
  { q: "SRL stands for:", opts: ["Student Registration List", "Self-Regulated Learning", "Synchronous Resource Learning", "Systematic Research Logic"], ans: 1, exp: "SRL includes time management and self-motivation.", hint: "Topic: Skills", sec: "Skills" },
  { q: "Mastery of LMS platforms and critical evaluation of resources fall under which skill?", opts: ["Self-Regulated Learning", "Digital and Information Literacy", "Communication & Collaboration", "Critical Thinking"], ans: 1, exp: "This refers to Digital and Information Literacy.", hint: "Topic: Skills", sec: "Skills" },
  { q: "The ability to analyze complex material without immediate lecturer support is an example of:", opts: ["Lifelong Learning", "Digital Literacy", "Critical Thinking & Problem Solving", "Self-Regulated Learning"], ans: 2, exp: "Critical Thinking helps analyze materials independently.", hint: "Topic: Skills", sec: "Skills" },
  { q: "Building a Personal Learning Network (PLN) is associated with which skill?", opts: ["Lifelong Learning & Adaptability", "Digital Literacy", "Communication Skills", "Critical Thinking"], ans: 0, exp: "It falls under Lifelong Learning & Adaptability.", hint: "Topic: Skills", sec: "Skills" },
  { q: "Google Meet and Microsoft Teams are examples of:", opts: ["Asynchronous Platforms", "Synchronous Platforms", "Paper-based correspondence", "MOOCs"], ans: 1, exp: "These are live, real-time synchronous platforms.", hint: "Topic: Platforms", sec: "Platforms" },
  { q: "Which of the following is an advantage of Synchronous Learning?", opts: ["Does not require internet", "Immediate interaction reduces transactional distance", "Compatible with Open Pace", "Can be done completely offline"], ans: 1, exp: "It reduces transactional distance and builds Social Presence.", hint: "Topic: Platforms", sec: "Platforms" },
  { q: "WhatsApp Groups, Pre-recorded Lectures, and Podcasts are examples of:", opts: ["Synchronous Learning", "Asynchronous Learning", "Virtual Reality", "Blended Learning"], ans: 1, exp: "These do not happen in real-time.", hint: "Topic: Platforms", sec: "Platforms" },
  { q: "Which type of learning is more compatible with 'Open Pace'?", opts: ["Synchronous Learning", "Asynchronous Learning", "Live Webinars", "Traditional Classroom"], ans: 1, exp: "Asynchronous learning allows learners to study at their own pace.", hint: "Topic: Platforms", sec: "Platforms" },
  { q: "A disadvantage of Asynchronous Learning is:", opts: ["It is not flexible", "It does not support mobile devices", "Delayed feedback can increase transactional distance", "It requires stable internet at a fixed time"], ans: 2, exp: "Delayed feedback increases the psychological gap.", hint: "Topic: Platforms", sec: "Platforms" },
  { q: "The notes conclude that the best solution for distance learning is:", opts: ["Fully Synchronous Learning", "Fully Asynchronous Learning", "Hybrid/Blended Learning", "Paper-based correspondence"], ans: 2, exp: "Hybrid/Blended learning offers a flexible, student-centered experience.", hint: "Topic: Platforms", sec: "Platforms" },
  { q: "If a student prefers to study late at night by watching recorded videos, they are engaging in:", opts: ["Synchronous Learning", "Asynchronous Learning", "Blended Learning", "Traditional Learning"], ans: 1, exp: "Recorded videos accessed at one's own time are asynchronous.", hint: "Topic: Platforms", sec: "Platforms" }
]
'''
    
    quiz_html = quiz_html.replace(
        "if (diff === 'obj1') filtered = BANK.filter(q => q.sec === 'Definitions');",
        "if (diff === 'obj1') filtered = BANK.filter(q => ['Theories', 'Paradigm Shift', 'Case Study'].includes(q.sec));"
    )
    quiz_html = quiz_html.replace(
        "else if (diff === 'obj2') filtered = BANK.filter(q => q.sec === 'Entrepreneurship');",
        "else if (diff === 'obj2') filtered = BANK.filter(q => ['Models', 'Open Model'].includes(q.sec));"
    )
    quiz_html = quiz_html.replace(
        "else if (diff === 'obj3') filtered = BANK.filter(q => q.sec === 'Finance & HRM');",
        "else if (diff === 'obj3') filtered = BANK.filter(q => ['Skills', 'Platforms'].includes(q.sec));"
    )
    # Ensure it says 60 questions
    quiz_html = quiz_html.replace('CBT practice quiz · 15 questions · Timed', 'CBT practice quiz · 60 questions · Timed')
    quiz_html = quiz_html[:bank_code_start] + new_bank + quiz_html[bank_code_end:]
    
    with open('edt304_quiz.html', 'w', encoding='utf-8') as f:
        f.write(quiz_html)

create_edt304_notes()
create_edt304_quiz()
print("Done")
