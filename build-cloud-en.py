# -*- coding: utf-8 -*-
import re, io

SRC='/Users/yaronamor/Documents/yaronamor-vault/sol/O-output/website-sol-therapy/cloud.html'
OUT='/Users/yaronamor/Documents/yaronamor-vault/sol/O-output/website-sol-therapy/cloud-en.html'
h=io.open(SRC,encoding='utf-8').read()

# ---------- 1. WHOLESALE JS BLOCKS (regex) ----------
ART_EN='''var ART=[
 {dow:'Wed',date:'1.7',live:false,name:"Astral Projection",line:'A rare ambient set from the pioneers of psychedelic trance',slug:'astral',url:'https://www.eventer.co.il/ybtff'},
 {dow:'Thu',date:'2.7',live:true, name:'Yehezkel Raz',line:'Piano and ambient expanses, a minimalism of quiet',slug:'raz',url:'https://www.eventer.co.il/l6tff'},
 {dow:'Tue',date:'7.7',live:false,name:'Darwish',line:'A hypnotic trance journey, deep and tribal',slug:'darwish',url:'https://www.eventer.co.il/m6tff'},
 {dow:'Wed',date:'8.7',live:true, name:'Sefi Zisling',line:'Spiritual jazz on trumpet, warm and analogue',slug:'zisling',url:'https://www.eventer.co.il/q6tff'},
 {dow:'Thu',date:'9.7',live:false,name:'Karin Kimel',line:'An eclectic musical journey with a curator\\'s eye',slug:'kimel',url:'https://www.eventer.co.il/s6tff'},
 {dow:'Tue',date:'14.7',live:false,name:'Shuzin',line:'Multi-layered analogue sound worlds',slug:'shuzin',url:'https://www.eventer.co.il/t6tff'},
 {dow:'Wed',date:'15.7',live:true, name:'Eyal Talmudi',line:'Wind instruments, overtones and the resonance of the space',slug:'talmudi',url:'https://www.eventer.co.il/r6tff'},
 {dow:'Thu',date:'16.7',live:false,name:'Omri Smadar',line:'Meditative electronica, classics and roots',slug:'smadar',url:'https://www.eventer.co.il/f6tff'},
 {dow:'Tue',date:'21.7',live:false,name:'Assaf Amdursky',line:'A deep atmospheric expanse and active listening',slug:'amdursky',url:'https://www.eventer.co.il/76tff'},
 {dow:'Thu',date:'23.7',live:false,name:'Yossi Fine',line:'Low frequencies and deep bass textures',slug:'fine',url:'https://www.eventer.co.il/36tff'}, {dow:'Tue',date:'28.7',live:true, name:'Yonatan Daskal',line:'Synthesizer and keys, from quiet to intensity',slug:'daskal',url:'https://www.eventer.co.il/26tff'},
 {dow:'Wed',date:'29.7',live:false,name:'Anna Haleta',line:'Hypnotic techno, deep and uncompromising',slug:'haleta',url:'https://www.eventer.co.il/46tff'},
 {dow:'Thu',date:'30.7',live:true, name:'Shye Ben Tzur',line:'Qawwali and sacred song, a bridge to India',slug:'bentzur',url:'https://www.eventer.co.il/v6tff'}
];'''
h,n=re.subn(r'var ART=\[.*?\n\];', lambda m: ART_EN, h, count=1, flags=re.S)
assert n==1, 'ART not replaced'

BIO_SESSIONS_EN=r'''var BIO={"darwish-b":["One of the central and most influential DJs and producers in Israel's trance scene. Over decades, Darwish has developed a singular musical language that fuses psychedelic and progressive trance with rooted elements of world music and organic rhythms.","He approaches listening spaces as places of mental release and energetic union, leading a hypnotic, deep and tribal sound journey that connects the listener to the most fundamental beat of the heart."],"astral":["For the opening event we host the legendary psychedelic trance act Astral Projection, among the pioneers of Israeli electronic sound who went on to conquer the world. Avi Nissim and Lior Perlmutter, working together since the days of the SFX project in 1989, are key figures behind some of the eternal anthems of the Goa and psy-trance genres, sounds that shaped generations of listeners and creators across the globe.","Their music is a multi-layered cosmic journey, weaving hypnotic melodies, sweeping rhythms and rich sonic textures. With an extensive discography that keeps growing to this day, Astral Projection lead vast crowds at festivals and events around the world, consistently exploring the power of sound to create immersive experiences in space.","They will play a rare, specially composed ambient set."],"raz":["A musician, pianist and producer whose work has earned sweeping international recognition, with tens of millions of streams and millions of monthly listeners across the streaming platforms.","Raz has developed a minimalist, distinctive musical language that blends piano, soundscapes and atmospheric electronic spaces.","He leads deep audio-visual pieces, and his work rests on intricate ambient layers that create a reflection of inner quiet and deep listening at the heart of the urban space."],"darwish":["One of the central and most influential DJs and producers in Israel's trance scene. Over decades, Darwish has developed a singular musical language that fuses psychedelic and progressive trance with rooted elements of world music and organic rhythms.","He approaches listening spaces as places of mental release and energetic union, leading a hypnotic, deep and tribal sound journey that connects the listener to the most fundamental beat of the heart."],"zisling":["We host Sefi Zisling, one of the most respected and influential trumpeters, composers and creators in Israel's jazz, Afrobeat and contemporary Black music scene.","Zisling, who released his debut album on the leading musical collective Raw Tapes and is now signed to the acclaimed British label Tru Thoughts, is known for a particularly warm, analogue and spiritual sound signature. His trumpet playing is a conduit for raw emotion, air and breath.","In the meditative space, Zisling builds rich layers of spiritual jazz, threading nostalgic melodies with free improvisation and inviting the audience into a deep dive."],"kimel":["We host Karin Kimel, a respected DJ, selector and artist who plays regularly at leading lineups and festivals.","Karin plays across a wide range of genres and creates a connection between a distinct visual vision and the building of atmospheric spaces and eclectic musical journeys, inviting those in the space to switch off the background noise and dive into a total, imagination-stirring listening experience."],"shuzin":["Shuzin (Yonatan Levin) is a multidisciplinary artist, music producer, multi-instrumentalist and sound engineer, one of the most original and prolific creators in the Israeli indie and electronic scene.","Shuzin is the founder of the independent Haifa label Ghost Town Records, and works under a range of identities - he is a member of the acts Geshem and 3421, and is regarded as a wizard of synthesizers and studio production. His work moves between experimental electronica, dub, futuristic beats and ambient.","To the space, Shuzin brings his ability to weave multi-layered, hypnotic sonic worlds, threading analogue gear with atmospheric expanses."],"talmudi":["A virtuoso musician, saxophonist, clarinettist, composer and mesmerising producer, behind countless seminal projects in Israeli and international music, from the band Malox to membership in the leading acts Balkan Beat Box and Oy Division, alongside iconic collaborations with giants such as Berry Sakharof, Shalom Hanoch, Knesiyat HaSechel, Mosh Ben Ari and Avraham Tal.","Talmudi, known for his raw and uncompromising energy, brings a deep understanding of the wind instrument as a direct extension of the mind and spirit. He comes to us to lead his fascinating project: Sonologed.","The project began in 2018 as a sound laboratory and musical research effort, born of a deep wish to create an alternative to the fast, demanding pace of daily life. Over the years it grew into an acclaimed album trilogy on the RAW TAPES label, and into a phenomenon of live shows built entirely on the singular concept of \"music for people lying down\".","In this intimate session, Talmudi sheds the fast rhythms and dives into the study of overtones, the resonance of the space and bare air, creating a total, hypnotic listening experience. He leads the project into realms of organic ambient and meditative frequencies, where the wind instruments (saxophone, clarinet, bagpipes and flutes) and overtone singing meet a looper and an array of effects."],"smadar":["We host Omri Smadar, a DJ, producer and musician with a broad background in classical music and jazz, and one of the most successful and in-demand electronic creators in Israel.","Smadar has cracked a distinctive formula, fusing iconic classics and musical roots with contemporary electronic production. He leads long, meditative and hypnotic electronic journeys, unfolding layers of sound in which every small tone, note and movement carries deliberate meaning.","Omri, one of Sol Therapy's resident artists, comes to us straight from his first international tour."],"smadar-b":["We host Omri Smadar, a DJ, producer and musician with a broad background in classical music and jazz, and one of the most successful and in-demand electronic creators in Israel.","Smadar has cracked a distinctive formula, fusing iconic classics and musical roots with contemporary electronic production. He leads long, meditative and hypnotic electronic journeys, unfolding layers of sound in which every small tone, note and movement carries deliberate meaning.","Omri, one of Sol Therapy's resident artists, comes to us straight from his first international tour."],"amdursky":["We host Assaf Amdursky, one of the central, most established and most respected creators in Israeli music and electronic work.","Since the early nineties, Amdursky has consistently broken new ground and explored the boundaries of sound, blending worlds of rock, pop and inventive electronica. His albums became cultural landmarks thanks to their sophisticated production, meticulous studio work and their singular, mesmerising atmosphere.","He is known for his ability to create whole musical worlds built from rich textures, and moves into the meditative space to create an experience grounded in active listening, a deep atmospheric expanse and full mental release."],"amdursky-b":["We host Assaf Amdursky, one of the central, most established and most respected creators in Israeli music and electronic work.","Since the early nineties, Amdursky has consistently broken new ground and explored the boundaries of sound, blending worlds of rock, pop and inventive electronica. His albums became cultural landmarks thanks to their sophisticated production, meticulous studio work and their singular, mesmerising atmosphere.","He is known for his ability to create whole musical worlds built from rich textures, and moves into the meditative space to create an experience grounded in active listening, a deep atmospheric expanse and full mental release."],"fine":["We host Yossi Fine, one of the most influential and respected bassists and music producers in Israel and worldwide.","Fine's extensive international career, which earned him a Grammy nomination, includes close work with rock legends such as David Bowie and Lou Reed, and jazz greats such as Gil Evans and Stanley Jordan, alongside the production of seminal albums on the local scene such as the band Hadag Nahash. Fine is an artist who understands sound, frequency and rhythm at their physical and studio depths.","He comes to us to share his accumulated knowledge and his singular feel, and to lead a meditative journey through low frequencies and deep bass textures."],"daskal":["We host Yonatan Daskal, a singular synthesizer artist, pianist, composer and producer, regarded as one of the busiest keyboardists and producers in Israel, working among other things in the project THE MOON and in collaboration with the Raw Tapes label.","Daskal leads sound journeys and keyboard sessions that move along the axis between total quiet and complex harmonic intensities.","His performance creates a space that envelops the audience in dynamic ambient electronica, exploring the perception of time from within, and inviting a clear mental dive free of distraction."],"haleta":["We host Anna Haleta, one of the central and most respected figures in Israel's techno and underground scene, and a co-founder of the Pacotek collective.","With more than two decades behind the decks at the most acclaimed clubs and festivals in Israel and abroad, Anna leads a singular musical line, deep and uncompromising.","Her sets are sweeping journeys into realms of quality, hypnotic techno, in which she skilfully weaves sounds and frequencies that challenge the mind and invite full surrender, clearing away the background noise of the psyche."],"bentzur":["We host Shye Ben Tzur, an exceptional international musician, composer and producer, who builds a rare musical and spiritual bridge between traditional Sufi music (Qawwali), sacred poetry in Hebrew and classical traditions from India.","Ben Tzur, who lived and worked in India for years, won wall-to-wall acclaim and worldwide recognition, in part for his masterful album \"Junun\" - a border-crossing collaboration with Radiohead guitarist Jonny Greenwood and the Rajasthan Express ensemble. Ben Tzur's music is a mesmerising journey into the depths of the soul, threading rich melodies, hypnotic rhythms and frequencies of love and spiritual connection.","In the live session at the CLOUD space, Ben Tzur will smooth away the cultural and musical distances and build a session tailored for deep release, in which those lying in the space can surrender to the organic sounds, find a clear breathing space and dive into a total, uplifting listening experience."]};'''
h,n=re.subn(r'(artist bio\) ----\s*\n\s*)var BIO=\{.*?\};', lambda m: m.group(1)+BIO_SESSIONS_EN, h, count=1, flags=re.S)
assert n==1, 'sessions BIO not replaced'

WS_EN='''var WS=[{slug:"rachel",dow:"Sat night",date:"11.7",time:"19:45",name:"Rachel Sander",url:"https://www.eventer.co.il/6n6ff"},{slug:"bonsai",dow:"Sun",date:"12.7",time:"18:00",name:"Bonsai Workshop",url:"https://www.eventer.co.il/3qgff"},{slug:"darwish-ed",dow:"Fri",date:"17.7",time:"12:00",name:"Darwish Ecstatic Dance",url:"https://web.vibez.io/events/darwish-ecstatic-dance?c=12658"},{slug:"deep-state",dow:"Mon",date:"27.7",time:"19:00",name:"Deep State",url:"https://www.eventer.co.il/fpvff"}];'''
h,n=re.subn(r'var WS=\[.*?\];', lambda m: WS_EN, h, count=1, flags=re.S)
assert n==1, 'WS not replaced'

BIO_WORKSHOPS_EN=r'''var BIO={"rachel":["A meditative journey that connects us to deep channels of self-healing. A musical journey of about three hours that moves between the poles within us - between free dance and ecstatic movement and quiet sitting, vocal expression and deep release, accompanied by live sound.","All of it with eyes closed, no cameras and no talking. A personal journey we take together. Every layer - body, mind and spirit - receives its attention.","Three hours of release, pure wellbeing and expansion of consciousness."],"bonsai":["An experiential creative workshop of about two hours, led by bonsai artist Sagi Baron. We will get to know the principles of the art of bonsai; Sagi will demonstrate the shaping technique, and then each participant will shape a bonsai tree of their own and pot it in a dedicated bonsai container. Each participant takes home the shaped and potted tree to continue nurturing it.","Sagi Baron, a bonsai artist and expert in the design and building of Japanese gardens, with more than 20 years of experience in the field. Founder of the Israeli Bonsai Academy, and chair of the Israeli Bonsai Association since its founding.","As an autodidact, he taught himself the field over many years, and later travelled as far as Japan to train and deepen his knowledge. From 2009 to today he continues his specialization under the guidance of master artist Marc Noelanders of Belgium."],"darwish-ed":["Darwish comes for a long, deep ecstatic dance set.","A space of free dance, movement, music and connection. Everyone in their own rhythm, their own way, their own moment.","For years Darwish has led dance spaces in Israel and abroad, bringing with him a musical journey that moves between tribal beats, groove, world music and electronic sounds.","Music that connects people, opens the heart and invites us to be more present in the body, in movement and in the moment.","The event takes place at CLOUD SPACE, Sol Therapy's new urban breathing space in Kiryat HaMelacha, Tel Aviv."],"deep-state":["A deep, lying-down meditative journey into the recesses of the subconscious, the place where healing and connection to what lies beyond become possible. Through presence, guided breath, live music and release beyond words, a meeting emerges with emotion, fresh insight and a wider perspective.","Led by Tal Eden, a meditation and mindfulness teacher, and Ofir Manki, a teacher of Eastern philosophies and lead singer of ANNARF."]};'''
h,n=re.subn(r'(WSBY\[a\.slug\]=a;\}\);\s*\n)var BIO=\{.*?\};', lambda m: m.group(1)+BIO_WORKSHOPS_EN, h, count=1, flags=re.S)
assert n==1, 'workshops BIO not replaced'

# ---------- 2. EXACT LONG STRINGS (head, sections, JS text) ----------
R=[]
def add(a,b): R.append((a,b))

# html tag
add('<html lang="he" dir="rtl">','<html lang="en" dir="ltr">')
# title
add('<title>קלאוד ספייס CLOUD SPACE - מדיטציית סאונד תל אביב | סול תרפי</title>','<title>CLOUD SPACE - Sound Meditation in Tel Aviv | Sol Therapy</title>')
# meta description
add('content="קלאוד ספייס (CLOUD SPACE) - פופ אפ מדיטציית סאונד עמוקה וסדנאות חווייתיות מבית סול תרפי. המרץ 6, קרית המלאכה, תל אביב. יולי-ספטמבר 2026: 13 מפגשי מדיטציה עם מיטב האמנים, וסדנת בונסאי עם שגיא ברון. כרטיסים באתר."',
    'content="CLOUD SPACE - a pop-up urban breathing space by Sol Therapy. Deep sound meditation sessions with live ambient sets from Israel\'s leading musicians, plus experiential workshops. HaMeretz 6, Kiryat HaMelacha, Tel Aviv. July to September 2026. Tickets on site."')
# canonical + hreflang: consume the source's full canonical+alternates block (cloud.html carries hreflang now) to avoid duplication
add('<link rel="canonical" href="https://sol-therapy.com/cloud">\n    <link rel="alternate" hreflang="he" href="https://sol-therapy.com/cloud">\n    <link rel="alternate" hreflang="en" href="https://sol-therapy.com/cloud-en">\n    <link rel="alternate" hreflang="x-default" href="https://sol-therapy.com/cloud">',
    '<link rel="canonical" href="https://sol-therapy.com/cloud-en">\n    <link rel="alternate" hreflang="he" href="https://sol-therapy.com/cloud">\n    <link rel="alternate" hreflang="en" href="https://sol-therapy.com/cloud-en">\n    <link rel="alternate" hreflang="x-default" href="https://sol-therapy.com/cloud">')
# OG
add('content="קלאוד ספייס CLOUD SPACE - מרחב נשימה אורבני מבית סול תרפי"','content="CLOUD SPACE - An Urban Breathing Space by Sol Therapy"')
add('content="פופ אפ מדיטציית סאונד עמוקה וסדנאות מבית סול תרפי. המרץ 6, תל אביב. יולי-ספטמבר 2026."','content="A pop-up for deep sound meditation and live ambient by Sol Therapy. HaMeretz 6, Tel Aviv. July to September 2026."')
add('<meta property="og:url" content="https://sol-therapy.com/cloud">','<meta property="og:url" content="https://sol-therapy.com/cloud-en">')
add('<meta property="og:locale" content="he_IL">','<meta property="og:locale" content="en_IL">')
add('content="קלאוד ספייס CLOUD SPACE - מרחב נשימה אורבני | סול תרפי"','content="CLOUD SPACE - An Urban Breathing Space | Sol Therapy"')
add('content="פופ אפ מדיטציית סאונד וסדנאות מבית סול תרפי. המרץ 6, תל אביב. יולי-ספטמבר 2026."','content="A pop-up for deep sound meditation and live ambient by Sol Therapy. HaMeretz 6, Tel Aviv. July to September 2026."')
# Event schema name+desc
add('"name": "CLOUD SPACE - מרחב נשימה אורבני מבית סול תרפי"','"name": "CLOUD SPACE - An Urban Breathing Space by Sol Therapy"')
add('"description": "פופ אפ מדיטציית סאונד עמוקה מבית סול תרפי. 13 מפגשים עם מיטב האמנים בישראל, יולי-ספטמבר 2026."','"description": "A pop-up for deep sound meditation by Sol Therapy. Thirteen sessions with some of Israel\'s finest musicians, July to September 2026."')
# LocalBusiness schema
add('"name":"CLOUD SPACE קלאוד ספייס"','"name":"CLOUD SPACE"')
add('"alternateName":"קלאוד ספייס - מדיטציית סאונד"','"alternateName":"CLOUD SPACE - Sound Meditation"')
add('"description":"מרחב נשימה אורבני מבית סול תרפי - פופ אפ מדיטציית סאונד עמוקה בקריית המלאכה, תל אביב. יולי-ספטמבר 2026."','"description":"An urban breathing space by Sol Therapy - a pop-up for deep sound meditation in Kiryat HaMelacha, Tel Aviv. July to September 2026."')
# schema urls -> the english page (Event offers.url + LocalBusiness url)
add('"url": "https://sol-therapy.com/cloud", "validFrom"','"url": "https://sol-therapy.com/cloud-en", "validFrom"')
add('"url":"https://sol-therapy.com/cloud","image"','"url":"https://sol-therapy.com/cloud-en","image"')
# Breadcrumb
add('"position": 1, "name": "בית"','"position": 1, "name": "Home"')
add('"position": 2, "name": "CLOUD SPACE", "item": "https://sol-therapy.com/cloud"','"position": 2, "name": "CLOUD SPACE", "item": "https://sol-therapy.com/cloud-en"')
# FAQ schema (Q names + A texts)
add('"name": "מה זה סול תרפי?"','"name": "What is Sol Therapy?"')
add('"text": "מיזם סול תרפי נשען על פרקטיקת הסאונד הילינג (Sound Healing) - שימוש בצלילים ומוזיקה ככלי להרחבת תודעה וצלילה למצבים מדיטטיביים עמוקים. באירועי סול תרפי אנו מזמינים אמני סאונד, מוזיקאים, דיג\'ייז ויוצרים אלקטרוניים מובילים להוביל מפגשים של מדיטציית סאונד בשכיבה, עם הנחיה הנשענת על עקרונות הזן-בודהיזם. הפעילות נשענת על בסיס רוחני ומדעי, ומלווה על ידי נזירים בודהיסטים ולצד מדענים וחוקרי מוח מהמובילים בעולם."',
    '"text": "The Sol Therapy project rests on the practice of Sound Healing - the use of sound and music as a tool for expanding consciousness and diving into deep meditative states. At Sol Therapy events we invite leading sound artists, musicians, DJs and electronic creators to lead lying-down sound meditation sessions, with guidance grounded in the principles of Zen Buddhism. The work rests on a spiritual and scientific foundation, accompanied by Buddhist monks alongside some of the world\'s leading scientists and brain researchers."')
add('"name": "צריך ניסיון קודם?"','"name": "Do I need prior experience?"')
add('"text": "לא. הסשנים מתאימים גם למי שזו ההתנסות הראשונה שלו וכוללים שיחת פתיחה עם הדרכה מלאה."','"text": "No. The sessions suit first-timers too, and include an opening talk with full guidance."')
add('"name": "מה צריך להביא?"','"name": "What should I bring?"')
add('"text": "בגדים נוחים ונכונות להגיע כמו שאתם. אם יש הנחיות מיוחדות, הן יופיעו בדף הכרטיסים של האירוע."','"text": "Comfortable clothes and a willingness to arrive just as you are. If there are any special instructions, they will appear on the event\'s ticket page."')
add('"name": "זו הופעה או מדיטציה?"','"name": "Is this a performance or a meditation?"')
add('"text": "זו מדיטציה עמוקה - חוויה חיה של סאונד, קשב ונוכחות. לא הופעה על במה ולא שיעור מדיטציה רגיל."','"text": "It is a deep meditation - a live experience of sound, attention and presence. Not a performance on a stage, and not a regular meditation class."')
add('"name": "אפשר להגיע לבד?"','"name": "Can I come on my own?"')
add('"text": "כן. הרבה מגיעים לבד."','"text": "Yes. Many people come on their own."')
add('"name": "כמה זמן נמשך הסשן?"','"name": "How long does a session last?"')
add('"text": "בין שעה לשעה וחצי, תלוי באירוע. הזמן המדויק מופיע בדף הכרטיסים."','"text": "Between one hour and an hour and a half, depending on the event. The exact time appears on the ticket page."')
add('"name": "צריך לשכב? מה אם יש לי מגבלה פיזית?"','"name": "Do I have to lie down? What if I have a physical limitation?"')
add('"text": "רוב האנשים שוכבים, אבל אפשר גם לשבת. המרחב מאפשר כל עמדה שנוחה לך."','"text": "Most people lie down, but you can also sit. The space allows any position that is comfortable for you."')
add('"name": "אפשר לאחר?"','"name": "Can I arrive late?"')
add('"text": "חשוב להגיע בזמן - הכניסה אחרי שהסשן התחיל מפריעה לשקט שנוצר. אם אתם יודעים מראש שתאחרו, כדאי לפנות אלינו."','"text": "It matters to arrive on time - entering after a session has begun disturbs the quiet that has formed. If you know in advance that you will be late, it is best to get in touch with us."')
add('"name": "האם יש חניה באזור?"','"name": "Is there parking nearby?"')
add('"text": "אזור קריית המלאכה מוקף במקומות חניה (כחול-לבן) בנוסף לכמה חניונים באזור."','"text": "The Kiryat HaMelacha area is surrounded by street parking (blue-and-white) as well as a few parking lots nearby."')
# bonsai + rainbow event schema descriptions
add('"name": "סדנת בונסאי בהנחיית שגיא ברון | CLOUD SPACE תל אביב"','"name": "Bonsai Workshop led by Sagi Baron | CLOUD SPACE Tel Aviv"')
add('"description": "סדנת יצירה חווייתית בהנחיית אמן הבונסאי שגיא ברון. כל משתתף יעצב וישתול עץ בונסאי וייקח אותו לביתו. CLOUD SPACE, המרץ 6, תל אביב."','"description": "An experiential creative workshop led by bonsai artist Sagi Baron. Each participant shapes and pots a bonsai tree to take home. CLOUD SPACE, HaMeretz 6, Tel Aviv."')
add('"name": "Rainbow Dance & Sound Meditation - רחלי סנדר | CLOUD SPACE"','"name": "Rainbow Dance & Sound Meditation - Rachel Sander | CLOUD SPACE"')
add('"description": "מסע מדיטטיבי של ריקוד, תנועה וצליל בהנחיית רחלי סנדר. CLOUD SPACE, המרץ 6, תל אביב."','"description": "A meditative journey of dance, movement and sound led by Rachel Sander. CLOUD SPACE, HaMeretz 6, Tel Aviv."')
# fonts link
add('<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=Inter:wght@300;400;600&family=Heebo:wght@400&display=swap" rel="stylesheet">')

# strip the EN toggle that the Hebrew source now carries (English page only needs the עברית toggle)
add('        <a href="/cloud-en" class="lang-toggle" hreflang="en" lang="en" aria-label="Switch to English">EN</a>\n','')
# back link
add('<a href="/" class="event-page__back">&rarr; חזרה לדף הבית</a>',
    '<a href="/cloud" class="lang-toggle" hreflang="he" lang="he" aria-label="Switch to Hebrew">עברית</a>\n        <a href="/" class="event-page__back">&larr; Back to home</a>')
# h1
add('<h1 class="event-page__title">קלאוד ספייס - מרחב נשימה אורבני<br>מבית סול ת\'רפי</h1>',
    '<h1 class="event-page__title">CLOUD SPACE - An Urban Breathing Space<br>by Sol Therapy</h1>')
# hero alt
add('alt="פוסטר CLOUD SPACE - מרחב נשימה אורבני מבית סול תרפי, אמן ויזואל רן סלוין"',
    'alt="CLOUD SPACE poster - an urban breathing space by Sol Therapy, visual art by Ran Slavin"')
# description paragraphs
add('<p>סול ת\'רפי מציגים את הפופ-אפ "קלאוד ספייס" - מרחב נשימה אורבני חדש ויחיד במינו בארץ, בקריית המלאכה שבתל אביב, שיפעל בחודשים יולי, אוגוסט וספטמבר. בתוך החיים הסואנים שבהם אנו חיים, הבנו את הצורך במרחב שונה, מיוחד, מאזן ומרגיע.</p>',
    '<p>Sol Therapy presents the CLOUD SPACE pop-up - a new urban breathing space, one of a kind in Israel, in Kiryat HaMelacha, Tel Aviv, open through July, August and September. Inside the noise of the lives we lead, we understood the need for a different space - a considered one, quieting and restorative.</p>')
add('<p>החיים היומיומיים בצל יוקר המחיה, המצב הביטחוני הרעוע, הרעש העירוני הבלתי פוסק ועוד שלל הסחות דעת, גורמים לרמות סטרס גבוהות שאנו צוברים בגוף ובנפש בקצב הולך וגובר בשנים האחרונות.</p>',
    '<p>Daily life under the weight of the cost of living, an unsettled security situation, the ceaseless urban noise and countless other distractions leaves us carrying rising levels of stress in body and mind, faster than ever in recent years.</p>')
add('<p>מתוך תובנה זו, ולאחר עשרות סדנאות וריטריטים של מדיטציית סאונד במרחבים משתנים כגון מרכז סוזן דלל, מוזיאון תל אביב, הספרייה הלאומית בירושלים, MOA ועוד, הסקנו שזהו התזמון הנכון לפתוח פופ-אפ מוקפד שהוא מרחב לנשימה, הרפיה ותנועה.</p>',
    '<p>Out of that understanding, and after dozens of sound meditation workshops and retreats in changing spaces such as the Suzanne Dellal Centre, the Tel Aviv Museum of Art, the National Library in Jerusalem, MOA and more, we felt this was the right moment to open a carefully considered pop-up: a space for breath, release and movement.</p>')
add('<p>בחודשים הקרובים נארח את האמנים המובילים בישראל לסשנים של מדיטציות סאונד עמוקות, המשלבות את כוחה המרפא של המוזיקה עם עקרונות הזן-בודהיזם כדי לאפשר חלל להרפיה עמוקה, המעניק הזדמנות נדירה להיחשף לזרמים התת-קרקעיים ביצירתם של אמנים אהובים. אנו נרגשים להציג לכם את תוכנית יולי עם נבחרת אמנים מובילים בתחומם שבחרנו בקפידה. <strong>שימו לב כי מספר המקומות בסדנאות מוגבל, ואנו ממליצים לשריין מקומות מראש.</strong></p>',
    '<p>Over the coming months we will host Israel\'s leading artists for deep sound meditation sessions that pair the healing power of music with the principles of Zen Buddhism, opening a space for deep release and a rare chance to meet the undercurrents in the work of beloved artists. We are glad to present the July programme, a lineup of leading artists we chose with care. <strong>Please note that places in the sessions are limited, and we recommend reserving in advance.</strong></p>')
# page share
add('aria-label="להעביר הלאה - שיתוף הדף"','aria-label="Pass it on - share this page"')
add('<span>להעביר הלאה</span>','<span>Pass it on</span>')
# tickets label
add('<p class="cloud-tickets__label">מדיטציות סאונד עמוקות<span class="yr">יולי 2026</span></p>',
    '<p class="cloud-tickets__label">Deep Sound Meditations<span class="yr">July 2026</span></p>')
# session section
add('<section class="cloud-session" aria-label="מה מחכה לכם בסשן">','<section class="cloud-session" aria-label="What happens in a session">')
add('<h2 class="cloud-session__title">מה מחכה לכם בסשן?</h2>','<h2 class="cloud-session__title">What Happens in a Session?</h2>')
add('<p class="cloud-session__text">במפגש נקיים מדיטציית שכיבה חצי מודרכת במשך 60 דקות.<br>אנו מדייקים את הסט והסטטינג בחלל עם סאונד מוקפד ומזרנים נוחים - אין צורך להביא ציוד כלשהו ואין צורך בניסיון קודם במדיטציה.<br>כמו כן, במפגש תתקיים שיחה פתוחה עם האמן והזדמנות לשאול שאלות.</p>',
    '<p class="cloud-session__text">Each session is a semi-guided lying-down meditation of 60 minutes.<br>We tune the set and the setting in the space with considered sound and comfortable mattresses - no equipment to bring, and no prior meditation experience needed.<br>Each session also includes an open conversation with the artist and a chance to ask questions.</p>')
# workshops
add('<section class="cloud-workshops" aria-label="סדנאות">','<section class="cloud-workshops" aria-label="Workshops">')
add('<h2 class="cloud-tickets__label">סדנאות<span class="yr">יולי 2026</span></h2>','<h2 class="cloud-tickets__label">Workshops<span class="yr">July 2026</span></h2>')
add('<p class="lp-card__sub">מדיטציה בתנועה</p>','<p class="lp-card__sub">Meditation in Motion</p>')
add('<p class="lp-card__sub">טל עדן ואופיר מאנקי</p>','<p class="lp-card__sub">Tal Eden and Ofir Manki</p>')
# video
add('<section class="cloud-video" aria-label="וידאו"','<section class="cloud-video" aria-label="Video"')
add('aria-label="נגן וידאו - סול תרפי"','aria-label="Play video - Sol Therapy"')
add('alt="סול תרפי - מדיטציות סאונד"','alt="Sol Therapy - sound meditations"')
add("ifr.title='סול תרפי - מדיטציות סאונד';","ifr.title='Sol Therapy - sound meditations';")
# space
add('<section class="cloud-space" aria-label="הדמיית המרחב">','<section class="cloud-space" aria-label="Space rendering">')
add('alt="הדמיית מרחב CLOUD - אולם מדיטציית סאונד עם מזרנים, צמחייה ומערכת סאונד מרכזית"',
    'alt="CLOUD space rendering - a sound meditation hall with mattresses, greenery and a central sound system"')
add('<p class="cloud-space__cap">הדמיית המרחב · קלאוד ספייס, המרץ 6</p>','<p class="cloud-space__cap">Space rendering · CLOUD SPACE, HaMeretz 6</p>')
# FAQ body
add('<section class="cloud-faq" aria-label="שאלות נפוצות">','<section class="cloud-faq" aria-label="Frequently asked questions">')
add('<h2 class="cloud-faq__title">שאלות נפוצות</h2>','<h2 class="cloud-faq__title">Frequently Asked Questions</h2>')
add('<summary class="cloud-faq__q">מה זה סול תרפי?</summary><div class="cloud-faq__a">מיזם "סול תרפי" נשען על פרקטיקת הסאונד הילינג (Sound Healing) - שימוש בצלילים ומוזיקה ככלי להרחבת תודעה, וצלילה למצבים מדיטטיביים עמוקים. במשך אלפי שנים רתמו בני האדם את הטכנולוגיה המתקדמת ביותר ברשותם כדי לייצר כלים, פעימות ופרקטיקות שמעמיקות את החיבור בין נפש, תודעה ומוזיקה.<br><br>במסגרת אירועי סול תרפי אנו מזמינים אמני סאונד, מוזיקאים, דיג\'ייז ויוצרים אלקטרוניים מובילים - אנשים שהקדישו את חייהם לחקר התדר והצליל - להוביל מפגשים של מדיטציית סאונד בשכיבה, עם הנחיה מוקפדת הנשענת על עקרונות הזן-בודהיזם. אלו מסעות טרנספורמטיביים אל תוך התודעה, לעיתים בעלי אופי רוחני, הנערכים באמצעות מוזיקה המתעלה מעל גבולות של שפה ותרבות - ומאפשרת חיבור ישיר אל הגוף והנפש.<br><br>מסגרת הפעילות שלנו נשענת על בסיס רוחני ומדעי עמוק, ומלווה על ידי נזירים בודהיסטים המחזיקים בידע בן 2,500 שנה על התודעה האנושית - לצד מדענים וחוקרי מוח מהמובילים בעולם, הלוקחים חלק באירועים ובריטריטים שלנו. תוכלו למצוא המון מידע נוסף ב<a href="/" style="color:#209CB4">אתר הבית שלנו</a>.</div>',
    '<summary class="cloud-faq__q">What is Sol Therapy?</summary><div class="cloud-faq__a">The Sol Therapy project rests on the practice of Sound Healing - the use of sound and music as a tool for expanding consciousness and diving into deep meditative states. For thousands of years, people have harnessed the most advanced technology available to them to create instruments, pulses and practices that deepen the connection between mind, consciousness and music.<br><br>At Sol Therapy events we invite leading sound artists, musicians, DJs and electronic creators - people who have devoted their lives to the study of frequency and sound - to lead lying-down sound meditation sessions, with careful guidance grounded in the principles of Zen Buddhism. These are transformative journeys into consciousness, at times spiritual in nature, held through music that rises above the boundaries of language and culture, and allows a direct connection to body and mind.<br><br>Our work rests on a deep spiritual and scientific foundation, accompanied by Buddhist monks who hold 2,500 years of knowledge of the human mind, alongside some of the world\'s leading scientists and brain researchers who take part in our events and retreats. You can find much more on our <a href="/" style="color:#209CB4">home site</a>.</div>')
add('<summary class="cloud-faq__q">צריך ניסיון קודם?</summary><div class="cloud-faq__a">לא. הסשנים מתאימים גם למי שזו ההתנסות הראשונה שלו וכוללים שיחת פתיחה עם הדרכה מלאה.</div>',
    '<summary class="cloud-faq__q">Do I need prior experience?</summary><div class="cloud-faq__a">No. The sessions suit first-timers too, and include an opening talk with full guidance.</div>')
add('<summary class="cloud-faq__q">מה צריך להביא?</summary><div class="cloud-faq__a">בגדים נוחים ונכונות להגיע כמו שאתם. אם יש הנחיות מיוחדות, הן יופיעו בדף הכרטיסים של האירוע.</div>',
    '<summary class="cloud-faq__q">What should I bring?</summary><div class="cloud-faq__a">Comfortable clothes and a willingness to arrive just as you are. If there are any special instructions, they will appear on the event\'s ticket page.</div>')
add('<summary class="cloud-faq__q">זו הופעה או מדיטציה?</summary><div class="cloud-faq__a">זו מדיטציה עמוקה - חוויה חיה של סאונד, קשב ונוכחות. לא הופעה על במה ולא שיעור מדיטציה רגיל.</div>',
    '<summary class="cloud-faq__q">Is this a performance or a meditation?</summary><div class="cloud-faq__a">It is a deep meditation - a live experience of sound, attention and presence. Not a performance on a stage, and not a regular meditation class.</div>')
add('<summary class="cloud-faq__q">אפשר להגיע לבד?</summary><div class="cloud-faq__a">כן. הרבה מגיעים לבד.</div>',
    '<summary class="cloud-faq__q">Can I come on my own?</summary><div class="cloud-faq__a">Yes. Many people come on their own.</div>')
add('<summary class="cloud-faq__q">כמה זמן נמשך הסשן?</summary><div class="cloud-faq__a">בין שעה לשעה וחצי, תלוי באירוע. הזמן המדויק מופיע בדף הכרטיסים.</div>',
    '<summary class="cloud-faq__q">How long does a session last?</summary><div class="cloud-faq__a">Between one hour and an hour and a half, depending on the event. The exact time appears on the ticket page.</div>')
add('<summary class="cloud-faq__q">צריך לשכב? מה אם יש לי מגבלה פיזית?</summary><div class="cloud-faq__a">רוב האנשים שוכבים, אבל אפשר גם לשבת. המרחב מאפשר כל עמדה שנוחה לך.</div>',
    '<summary class="cloud-faq__q">Do I have to lie down? What if I have a physical limitation?</summary><div class="cloud-faq__a">Most people lie down, but you can also sit. The space allows any position that is comfortable for you.</div>')
add('<summary class="cloud-faq__q">אפשר לאחר?</summary><div class="cloud-faq__a">חשוב להגיע בזמן - הכניסה אחרי שהסשן התחיל מפריעה לשקט שנוצר. אם אתם יודעים מראש שתאחרו, כדאי לפנות אלינו.</div>',
    '<summary class="cloud-faq__q">Can I arrive late?</summary><div class="cloud-faq__a">It matters to arrive on time - entering after a session has begun disturbs the quiet that has formed. If you know in advance that you will be late, it is best to get in touch with us.</div>')
add('<summary class="cloud-faq__q">האם יש חניה באזור?</summary><div class="cloud-faq__a">אזור קריית המלאכה מוקף במקומות חניה (כחול-לבן) בנוסף לכמה חניונים באזור.</div>',
    '<summary class="cloud-faq__q">Is there parking nearby?</summary><div class="cloud-faq__a">The Kiryat HaMelacha area is surrounded by street parking (blue-and-white) as well as a few parking lots nearby.</div>')
# contact
add('<section class="cloud-contact" id="contact" aria-label="יצירת קשר">','<section class="cloud-contact" id="contact" aria-label="Contact">')
add('<h2 class="cloud-contact__title">יש לכם שאלות?</h2>','<h2 class="cloud-contact__title">Have Questions?</h2>')
add('<p class="cloud-contact__sub">דברו איתנו, נשמח לעזור</p>','<p class="cloud-contact__sub">Talk to us, we are happy to help</p>')
add('?text=%D7%94%D7%99%D7%99%2C%20%D7%99%D7%A9%20%D7%9C%D7%99%20%D7%A9%D7%90%D7%9C%D7%94%20%D7%9C%D7%92%D7%91%D7%99%20%D7%90%D7%99%D7%A8%D7%95%D7%A2%D7%99%20CLOUD"',
    '?text=Hi%2C%20I%20have%20a%20question%20about%20the%20CLOUD%20events"')
add('aria-label="פנייה בוואטסאפ">','aria-label="Contact us on WhatsApp">')
add('                    וואטסאפ\n','                    WhatsApp\n')
add('aria-label="פנייה במייל">','aria-label="Contact us by email">')
add('                    מייל\n','                    Email\n')
add('aria-label="עקבו אחרינו באינסטגרם של CLOUD SPACE">','aria-label="Follow CLOUD SPACE on Instagram">')
add('                    אינסטגרם\n','                    Instagram\n')
# friends
add('<section class="cloud-friends" aria-label="חברים שעוזרים לנו להגשים חלומות">','<section class="cloud-friends" aria-label="Friends who help us make it happen">')
add('<h2 class="cloud-friends__title">חברים שעוזרים לנו להגשים חלומות</h2>','<h2 class="cloud-friends__title">Friends Who Help Us Make It Happen</h2>')
add('aria-label="SOOS - מעבר לאתר"','aria-label="SOOS - visit the site"')
add('<p class="cf-note">סטודיו בוטיק לעיצוב סאונד, היוצר אובייקטים קוליים פיסוליים ונדירים, ואחראי על מערכת הסאונד בקלאוד ספייס.</p>',
    '<p class="cf-note">A boutique sound-design studio, creating rare sculptural sound objects, and responsible for the sound system at CLOUD SPACE.</p>')
add('aria-label="המשתלה היפנית - מעבר לאתר"','aria-label="The Japanese Nursery - visit the site"')
add('alt="המשתלה היפנית - BONSAI SHOP"','alt="The Japanese Nursery - BONSAI SHOP"')
add('<p class="cf-note">אמנות הבונסאי והגן היפני.</p>','<p class="cf-note">The art of bonsai and the Japanese garden.</p>')
# sticky
add('<button type="button" id="cloudStickyBtn">לרכישת כרטיסים</button>','<button type="button" id="cloudStickyBtn">Get Tickets</button>')
# JS share popover
add("pop.setAttribute('dir','rtl');","pop.setAttribute('dir','ltr');")
add('aria-label="וואטסאפ" title="וואטסאפ">','aria-label="WhatsApp" title="WhatsApp">')
add('data-ig aria-label="אינסטגרם" title="אינסטגרם">','data-ig aria-label="Instagram" title="Instagram">')
add('aria-label="פייסבוק" title="פייסבוק">','aria-label="Facebook" title="Facebook">')
add('data-copy aria-label="העתקת קישור" title="העתקת קישור">','data-copy aria-label="Copy link" title="Copy link">')
add("window.prompt('העתיקו את הקישור:', url);","window.prompt('Copy the link:', url);")
add("var text='CLOUD SPACE - מדיטציית סאונד בהשתתפות '+name+' | '+when+' | 20:30';","var text='CLOUD SPACE - a sound meditation with '+name+' | '+when+' | 20:30';")
add("var text='CLOUD SPACE - מרחב נשימה אורבני מבית סול ת\\'רפי | מדיטציות סאונד עמוקות, יולי 2026';","var text='CLOUD SPACE - an urban breathing space by Sol Therapy | deep sound meditations, July 2026';")
# detail modal labels (both scripts share identical substrings)
add('<button type="button" class="lp-detail__x" aria-label="סגירה">×</button>','<button type="button" class="lp-detail__x" aria-label="Close">×</button>')
add('<a class="lp-detail__btn" target="_blank" rel="noopener">כרטיסים</a>','<a class="lp-detail__btn" target="_blank" rel="noopener">TICKETS</a>')
# css comment
add('/* card actions + "על האמן" link */','/* card actions + "about the artist" link */')

# recorded sessions archive
add('<section class="cloud-archive" aria-label="סשנים מוקלטים">','<section class="cloud-archive" aria-label="Recorded Sessions">')
add('<h2 class="cloud-archive__title">סשנים מוקלטים</h2>','<h2 class="cloud-archive__title">Recorded Sessions</h2>')
add('כל סשן בקלאוד מוקלט במלואו ועולה לערוץ היוטיוב שלנו','Every CLOUD session is recorded in full and uploaded to our YouTube channel')
add("aria-label=\"נגן: אסטרל פרוג'קשן - הסשן המלא\"",'aria-label="Play: Astral Projection - the full session"')
add('aria-label="נגן: יחזקאל רז - הסשן המלא"','aria-label="Play: Yehezkel Raz - the full session"')
add(' - סשן מוקלט בקלאוד"',' - recorded session at CLOUD"')
add('<span class="arc-card__label">הסשן המלא</span>','<span class="arc-card__label">Full session</span>')
add('aria-label="לכל הסשנים בערוץ היוטיוב של סול תרפי"','aria-label="All sessions on the Sol Therapy YouTube channel"')
add('\n                    לכל הסשנים בערוץ\n                </a>','\n                    All Sessions on the Channel\n                </a>')
add('aria-label="ערוץ היוטיוב של סול תרפי"','aria-label="Sol Therapy on YouTube"')
add('\n                    יוטיוב\n                </a>','\n                    YouTube\n                </a>')

# ---------- 3. GLOBAL TOKENS (names, address, labels, days, buttons) ----------
G=[]
def g_(a,b): G.append((a,b))
# artist / people / place names (longer first)
for a,b in [
 ("אסטרל פרוג'קשן","Astral Projection"),("יחזקאל רז","Yehezkel Raz"),("ספי ציזלינג","Sefi Zisling"),
 ("קארין קימל","Karin Kimel"),("אייל תלמודי","Eyal Talmudi"),("עמרי סמדר","Omri Smadar"),
 ("אסף אמדורסקי","Assaf Amdursky"),("יוסי פיין","Yossi Fine"),("יונתן דסקל","Yonatan Daskal"),
 ("אנה הלטה","Anna Haleta"),("שי בן צור","Shye Ben Tzur"),("רחלי סנדר","Rachel Sander"),
 ("סדנת בונסאי","Bonsai Workshop"),("שגיא ברון","Sagi Baron"),("דרוויש","Darwish"),("שוזין","Shuzin"),
]:
    g_(a,b)
# address / brand tokens
for a,b in [
 ("המרץ 6, קרית המלאכה","HaMeretz 6, Kiryat HaMelacha"),("קריית המלאכה","Kiryat HaMelacha"),
 ("קרית המלאכה","Kiryat HaMelacha"),("תל אביב","Tel Aviv"),("סול ת'רפי","Sol Therapy"),("סול תרפי","Sol Therapy"),
]:
    g_(a,b)
# round inline + subs
g_('>סבב מוקדם</span>','>EARLY ROUND</span>')
g_('>סולו מדיטציה</span>','>Solo Meditation</span>')
# labels (chips)
g_('>אזלו הכרטיסים<','>SOLD OUT<')
g_('>כרטיסים אחרונים<','>LAST TICKETS<')
g_('>כרטיס אחרון<','>LAST TICKET<')
# buttons + aria patterns
g_('>אזל</a>','>SOLD OUT</a>')
g_('aria-label="אזל: ','aria-label="Sold out: ')
g_('>כרטיסים</a>','>TICKETS</a>')
g_('aria-label="כרטיסים: ','aria-label="Tickets: ')
g_('על האמן<span class="chev"','<span class="lp-more-lg">ABOUT THE ARTIST</span><span class="lp-more-sm">ABOUT</span><span class="chev"')
g_('aria-label="על האמן: ','aria-label="About the artist: ')
g_('פרטים<span class="chev"','DETAILS<span class="chev"')
g_('פרטים<span class="cf-chev"','DETAILS<span class="cf-chev"')
g_('aria-label="פרטים: ','aria-label="Details: ')
g_('aria-label="שיתוף: ','aria-label="Share: ')
g_(' סבב מוקדם"',' early round"')   # remaining aria occurrences after name is english
g_('על האמן','about the artist')   # catch-all for any remaining "about the artist" in JS builder
# image alt-text patterns (longer first)
g_('מדיטציית סאונד ב-CLOUD SPACE','sound meditation at CLOUD SPACE')
g_('ב-CLOUD SPACE','at CLOUD SPACE')
g_('סבב מוקדם','early round')
# days (anchored: w-dow span + data-when)
for a,b in [("רביעי","Wed"),("חמישי","Thu"),("שלישי","Tue"),("ראשון","Sun"),("שני","Mon"),("שישי","Fri"),("מוצ״ש","Sat night")]:
    g_('>'+a+'</span>','>'+b+'</span>')
    g_('data-when="'+a+' ','data-when="'+b+' ')
# workshops: give the two subtitle-less cards an empty reserved sub so all four align (runs after names are English)
g_('<h3 class="lp-card__name">Bonsai Workshop</h3><div class="lp-card__when">','<h3 class="lp-card__name">Bonsai Workshop</h3><p class="lp-card__sub" aria-hidden="true">&nbsp;</p><div class="lp-card__when">')
g_('<h3 class="lp-card__name">Darwish Ecstatic Dance</h3><div class="lp-card__when">','<h3 class="lp-card__name">Darwish Ecstatic Dance</h3><p class="lp-card__sub" aria-hidden="true">&nbsp;</p><div class="lp-card__when">')

# ---------- APPLY ----------
for a,b in R:
    if a not in h:
        print('MISS exact:', a[:60])
    h=h.replace(a,b)
for a,b in G:
    h=h.replace(a,b)

# ---------- 4. APPEND OVERRIDE STYLE (fonts, LTR, toggle) before </head> ----------
override='''<style>
/* ===== English (LTR) mirror overrides ===== */
:root{--font-display:'Newsreader',Georgia,'Times New Roman',serif;--font-body:'Inter',system-ui,sans-serif;--font-english:'Inter',system-ui,sans-serif;}
.event-page{position:relative;}
/* type tuning for Newsreader (calmer than Fraunces) */
.event-page__title{font-weight:500;letter-spacing:-.005em;font-optical-sizing:auto;}
.lp-card__name{font-weight:500;letter-spacing:.002em;}
.lp-detail__name{font-weight:500;}
.faq-section__title{font-weight:600;}
.lp-soldout,.lp-lastseats{letter-spacing:.04em;}
/* LTR fixes */
.event-page__note{border-right:0;border-inline-start:3px solid var(--color-green);}
.lp-detail__inner{text-align:left;direction:ltr;}
.lp-card__body{text-align:left;}
.lp-detail__x{left:auto;inset-inline-end:.7rem;}
@media (min-width:980px){.cloud-logo{text-align:left;}.event-page__title{text-align:left;}}
@media (max-width:600px){.cloud-ticket__bio-in{text-align:left;}}
/* button system v2: outlined teal, muted sold-out, quiet about-link */
.lp-card__btn{font-family:var(--font-english);font-weight:500;font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;white-space:nowrap;color:#209CB4;background:transparent;border:1px solid rgba(32,156,180,.55);border-radius:4px;padding:.5rem 1.15rem;min-height:38px;transition:background .25s ease,color .25s ease,border-color .25s ease;}
.lp-card__btn:hover{background:#209CB4;border-color:#209CB4;color:#0f1413;}
.lp-card__btn--sold{color:#C0392B;background:transparent;border:1px solid rgba(192,57,43,.6);letter-spacing:.06em;pointer-events:none;cursor:default;}
.lp-card__btn--sold:hover{background:transparent;border-color:rgba(192,57,43,.6);color:#C0392B;}
.lp-card__more{font-family:var(--font-english);font-weight:400;font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:var(--color-muted);text-decoration:none;white-space:nowrap;}
.lp-card__more:hover{color:var(--color-washi);text-decoration:none;}
.lp-card__more .chev{font-size:.62em;opacity:.8;}
.lp-more-sm{display:none;}
@media(max-width:560px){.lp-more-lg{display:none;}.lp-more-sm{display:inline;}}
.lp-card__actions{gap:.85rem;}
@media(max-width:560px){.lp-card__actions{gap:.55rem;}.lp-card__btn{padding:.45rem .95rem;font-size:.74rem;}.lp-card__more{font-size:.64rem;letter-spacing:.1em;}}
/* workshops: reserve consistent sub-title space so dates/buttons align across the row */
.lp-grid--workshops .lp-card__sub{min-height:1.05em;}
.lp-detail__btn{font-family:var(--font-english);font-weight:500;font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:#209CB4;background:transparent;border:1px solid rgba(32,156,180,.55);border-radius:4px;padding:.55rem 1.4rem;min-height:40px;transition:background .25s ease,color .25s ease,border-color .25s ease;}
.lp-detail__btn:hover{background:#209CB4;border-color:#209CB4;color:#0f1413;}
.lang-toggle{position:absolute;top:1.15rem;inset-inline-end:1.25rem;z-index:70;display:inline-flex;align-items:center;min-height:44px;padding:.3rem .1rem;font-family:var(--font-english);font-size:.72rem;font-weight:400;letter-spacing:.18em;text-transform:uppercase;color:var(--color-muted);text-decoration:none;transition:color .3s ease;-webkit-tap-highlight-color:transparent;}
.lang-toggle:hover,.lang-toggle:focus-visible{color:var(--color-washi);}
.lang-toggle[lang="he"]{text-transform:none;letter-spacing:.02em;font-family:'Heebo','Inter',sans-serif;font-size:.82rem;}
@media (max-width:600px){.lang-toggle{top:1rem;inset-inline-end:1rem;}}
</style>
</head>'''
h=h.replace('</head>',override,1)

io.open(OUT,'w',encoding='utf-8').write(h)
print('WROTE', OUT, len(h),'chars')
