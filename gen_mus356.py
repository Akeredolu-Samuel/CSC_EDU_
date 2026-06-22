import re

with open('c:\\Users\\HomePC\\Desktop\\cscedu\\edt308_cbt_quiz (1).html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Titles
content = content.replace('EDT 308 Quiz', 'MUS 356 Quiz')
content = content.replace('EDT 308 &nbsp;|&nbsp; CBT Practice', 'MUS 356 &nbsp;|&nbsp; CBT Practice')
content = content.replace('Blended Learning &middot; E-Moderation &middot; Online Course Design', 'Music Education &middot; Technology &middot; Performance')
content = content.replace('<span class="qh-logo"><i class="ti ti-school" aria-hidden="true"></i> EDT 308</span>', '<span class="qh-logo"><i class="ti ti-school" aria-hidden="true"></i> MUS 356</span>')
content = content.replace('EDT 308', 'MUS 356')

# Replace Coverage Area
coverage_area = '''
      <ul>
        <li>Objective 1: The Staff and Clefs</li>
        <li>Objective 2: Lines and Spaces</li>
        <li>Objective 3: Solfa Notes & Technical Names</li>
        <li>Objective 4: Genres of Music</li>
        <li>Objective 5: Stage Performance Types</li>
        <li>Objective 6: Performance Tips</li>
        <li>Objective 7: Music Licensing in Nigeria</li>
        <li>Objective 8: Copyright Organizations (COSON, MCSN)</li>
        <li>Objective 9: Western Orchestra Instruments</li>
        <li>Objective 10: History of the Piano</li>
      </ul>
'''
content = re.sub(r'<div class="read-box-title">.*?</ul>', '<div class="read-box-title"><i class="ti ti-book-2" aria-hidden="true" style="font-size:14px"></i> Quiz Coverage Areas</div>' + coverage_area, content, flags=re.DOTALL)

# Bank
bank_data = '''const BANK = [
  { q: "What does a musical staff (or stave) consist of?", opts: ["4 lines and 5 spaces", "5 lines and 4 spaces", "6 lines and 3 spaces", "5 lines and 5 spaces"], ans: 1, exp: "A staff consists of 5 lines and 4 spaces.", hint: "", sec: "Music Fundamentals" },
  { q: "Which clef is used for notating music for high-pitched singers or instruments?", opts: ["Bass Clef", "F Clef", "Treble / G Clef", "Alto Clef"], ans: 2, exp: "The Treble or G Clef is used for high pitch.", hint: "", sec: "Music Fundamentals" },
  { q: "What are the letter names for the lines of a Treble Staff from bottom to top?", opts: ["F, A, C, E", "G, B, D, F, A", "E, G, B, D, F", "A, C, E, G"], ans: 2, exp: "The lines are E, G, B, D, F (Every Good Boy Deserves Food).", hint: "", sec: "Music Fundamentals" },
  { q: "What are the letter names for the spaces of a Treble Staff from bottom to top?", opts: ["F, A, C, E", "E, G, B, D, F", "A, C, E, G", "G, B, D, F, A"], ans: 0, exp: "The spaces are F, A, C, E (Face).", hint: "", sec: "Music Fundamentals" },
  { q: "What is the technical name for the Solfa note 'Doh'?", opts: ["Supertonic", "Tonic", "Mediant", "Dominant"], ans: 1, exp: "Doh is the Tonic.", hint: "", sec: "Music Fundamentals" },
  { q: "What is the technical name for the Solfa note 'Soh'?", opts: ["Subdominant", "Leading Note", "Dominant", "Submediant"], ans: 2, exp: "Soh is the Dominant.", hint: "", sec: "Music Fundamentals" },
  { q: "Which genre of music is known as 'serious music' and consists of western text and lyrics?", opts: ["R&B", "Jazz", "Reggae", "Classical or Western Chorus"], ans: 3, exp: "Classical music is known as serious music with rules.", hint: "", sec: "Genres of Music" },
  { q: "Which Nigerian music genre originated from highlife and involves the use of 2 or more string instruments?", opts: ["Fuji", "Juju", "Afrobeat", "Apala"], ans: 1, exp: "Juju originated from highlife and uses multiple string instruments.", hint: "", sec: "Genres of Music" },
  { q: "What type of stage is completely surrounded by audience seating on all sides?", opts: ["Proscenium Stage", "Thrust Stage", "Arena Stage", "Platform Stage"], ans: 2, exp: "An Arena Stage (theater-in-the-round) is surrounded by seating on all sides.", hint: "", sec: "Stage Performance" },
  { q: "Which type of music license grants the right to synchronize sound with visual media like movies or TV?", opts: ["Master License", "Performance License", "Synchronization License", "Print License"], ans: 2, exp: "Synchronization license allows syncing music with visual media.", hint: "", sec: "Music Licensing" },
  { q: "Which organization acts as the sole collective management organization (CMO) approved by the Nigerian Copyright Commission?", opts: ["MCSN", "COSON", "PMAN", "NCC"], ans: 1, exp: "COSON is the sole CMO approved by the NCC.", hint: "", sec: "Music Licensing" },
  { q: "Which of the following is a Woodwind instrument?", opts: ["Violin", "Clarinet", "Trumpet", "Conga"], ans: 1, exp: "The clarinet is a woodwind instrument.", hint: "", sec: "Instruments" },
  { q: "Who invented the piano around 1720?", opts: ["Claudio Monteverdi", "J.G Handel", "Bartholomeo Cristofori", "Arnold Schoenberg"], ans: 2, exp: "Bartholomeo Cristofori, an Italian carpenter, invented the piano.", hint: "", sec: "Instruments" },
  { q: "What was the original full name for the piano?", opts: ["Pianoforte", "Harpsichord", "Clavichord", "Synthesizer"], ans: 0, exp: "The full name is Pianoforte because it could play soft (piano) and loud (forte).", hint: "", sec: "Instruments" },
  { q: "In what year was Claudio Monteverdi's opera 'Orfeo' produced?", opts: ["1500", "1607", "1720", "1800"], ans: 1, exp: "His opera Orfeo was produced in 1607.", hint: "", sec: "Orchestra" },
  { q: "Which of the following is a Brass instrument?", opts: ["Flute", "Trombone", "Cello", "Marimba"], ans: 1, exp: "The Trombone is a brass instrument.", hint: "", sec: "Instruments" },
  { q: "What type of stage has a framed opening at the front, known as the arch?", opts: ["Proscenium Stage", "Thrust Stage", "Outdoor Stage", "Arena Stage"], ans: 0, exp: "Proscenium stage has a proscenium arch at the front.", hint: "", sec: "Stage Performance" },
  { q: "Which music license is required to play a sound recording in public via radio, TV, or concerts?", opts: ["Print License", "Synchronization License", "Mechanical License", "Broadcast or Performance License"], ans: 3, exp: "Performance licenses cover public streaming and playing.", hint: "", sec: "Music Licensing" },
  { q: "The Bass Clef is also known as what?", opts: ["G Clef", "C Clef", "F Clef", "D Clef"], ans: 2, exp: "The Bass Clef is known as the F Clef.", hint: "", sec: "Music Fundamentals" },
  { q: "Which genre of music originated from Jamaica and is known for its strong rhythmic baseline?", opts: ["Highlife", "Hip-Hop", "Reggae", "Juju"], ans: 2, exp: "Reggae originated from Jamaica.", hint: "", sec: "Genres of Music" }
];'''

content = re.sub(r'const BANK = \[.*?\];', bank_data, content, flags=re.DOTALL)

with open('c:\\Users\\HomePC\\Desktop\\cscedu\\mus356_quiz.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Created mus356_quiz.html")
