import re
head=open('src/head.html').read()
body=open('src/body.html').read()
data=open('src/data.json').read().strip()
STP='https://www.youtube.com/results?search_query=Straight+Talk+Pharmacist'
VC='https://www.youtube.com/@VitalCode6811'
BOOK=''  # Amazon link goes here when the book is live
meta='''<title>Straight Talk Pharmacist | Free Traffic Light Medicine Checker</title>
<meta name="description" content="Can you take turmeric with a blood thinner, or ibuprofen with blood pressure tablets? Check 1,100 common medicine mixes in seconds with pharmacist Leon Van Vuuren's free traffic-light checker.">
<link rel="canonical" href="https://straighttalkpharmacist.com/">
<meta property="og:title" content="Can I take this with my medicines? Free Traffic Light Checker">
<meta property="og:description" content="Check 1,100 common medicine mixes as RED, AMBER or GREEN. By pharmacist Leon Van Vuuren.">
<meta property="og:image" content="https://straighttalkpharmacist.com/share.jpg">
<meta property="og:url" content="https://straighttalkpharmacist.com/">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect x='9' y='1' width='14' height='30' rx='5' fill='%231f2326'/%3E%3Ccircle cx='16' cy='8' r='4' fill='%23d7261e'/%3E%3Ccircle cx='16' cy='16' r='4' fill='%23f0a500'/%3E%3Ccircle cx='16' cy='24' r='4' fill='%231f9d55'/%3E%3C/svg%3E">'''
head=re.sub(r'<title>.*?</title>',meta,head,flags=re.S)
css='''
nav.site{display:flex;gap:6px 18px;flex-wrap:wrap}
nav.site a{color:var(--ink);text-decoration:none;font-weight:700;font-size:16px;padding:6px 2px;border-bottom:2px solid transparent}
nav.site a:hover{border-color:var(--grn)}
.sec{border-top:1px solid var(--line)}
.sec h2{font-size:clamp(28px,3.4vw,40px);font-weight:800;margin-bottom:12px}
.lead{color:var(--soft);max-width:64ch;margin:0 0 18px}
.book{display:grid;grid-template-columns:minmax(0,260px) minmax(0,1fr);gap:clamp(20px,4vw,48px);align-items:center}
.book img{width:100%;height:auto;border-radius:6px;box-shadow:0 14px 34px rgba(0,0,0,.22)}
.book ul{padding-left:20px;margin:10px 0 18px}
.book li{margin:4px 0}
.cta{display:inline-block;background:var(--grn);color:#fff;font-weight:700;text-decoration:none;padding:12px 20px;border-radius:10px}
.cta.soon{background:var(--house)}
.cta.sample{background:transparent;color:var(--ink);border:2px solid var(--grn);margin-left:8px}
.cta.sample:hover{background:var(--grnt)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px}
.card h3{font-size:22px;margin-bottom:6px}
.card p{color:var(--soft);margin:0 0 14px}
.card a{font-weight:700;color:var(--grn)}
.about{max-width:70ch}
@media (max-width:700px){.book{grid-template-columns:1fr}.book img{max-width:220px}}
'''
head=head.replace('family=Atkinson+Hyperlegible:','family=Fira+Sans:wght@700;800;900&family=Atkinson+Hyperlegible:')
head=head.replace('</style>',css+open('src/theme.css').read()+'</style>')
body=body.replace('<header class="band"><div class="wrap brand"><b>Straight Talk Pharmacist</b><span>Free medicine mix checker</span></div></header>',
'<header class="band"><div class="wrap brand"><b>Straight Talk Pharmacist</b><nav class="site" aria-label="Main"><a href="#checker">Checker</a><a href="#book">The book</a><a href="#videos">Videos</a><a href="#about">About</a></nav></div></header>')
hero='''<main><section class="hero"><div class="wrap">
<div>
<div class="lamps" aria-hidden="true"><i></i><i></i><i></i></div>
<p class="kicker">From the pharmacy counter</p>
<h1><span class="w">Can</span> <span class="w">I</span> <span class="w">take</span> <span class="w">this</span> <span class="w">with</span> <span class="w">my</span> <span class="w">medicines?</span></h1>
<p class="lead">Check 1,100 everyday medicine mixes in seconds. Pharmacist Leon Van Vuuren rates each one GREEN, AMBER or RED, in plain language.</p>
<div class="actions"><a class="cta" href="#checker">Check my medicines</a><a class="cta ghost" href="sample.pdf" target="_blank" rel="noopener">Read a free sample</a></div>
</div>
<div class="shelfbox"><img src="shelf.jpg" width="1100" height="843" alt="A wooden medicine shelf glowing red, amber and green"><div class="glow r"></div><div class="glow a"></div><div class="glow g"></div><div class="shine"></div></div>
</div></section>'''
body=body.replace('<main class="band"><div class="wrap">',hero+'<section class="band sec" id="checker"><div class="wrap">',1)
body=body.replace('<h1>Can I take this with my medicines?</h1>','<h2>The free Traffic Light Checker</h2>',1)
extra=f'''</div></section>
<section class="band sec" id="book"><div class="wrap book">
<img class="reveal" src="book-cover.jpg" width="600" height="960" alt="Cover of The Traffic Light Medicine Cabinet by Leon Van Vuuren" loading="lazy">
<div>
<h2>The Traffic Light Medicine Cabinet</h2>
<p class="lead">A pharmacist's plain-language guide to safely mixing supplements, herbs and over-the-counter medicines with your prescriptions.</p>
<ul>
<li>1,100 common combinations rated RED, AMBER or GREEN</li>
<li>20 prescription medicine groups and 55 everyday products</li>
<li>A 30-minute medicine cabinet check, with worksheets</li>
<li>What to say to your doctor and pharmacist</li>
</ul>
<div class="actions">{{BOOKBTN}}</div>
</div>
</div></section>
<section class="band sec" id="videos"><div class="wrap">
<h2>Watch on YouTube</h2>
<p class="lead">Short, plain-English videos from a working pharmacist.</p>
<div class="cards reveal">
<div class="card"><h3>Straight Talk Pharmacist</h3><p>Medicine mixes, side effects and the questions people ask at the pharmacy counter.</p><a href="{STP}">Visit the channel →</a></div>
<div class="card"><h3>Vital Code</h3><p>Health explained simply: how your body and your medicines work.</p><a href="{VC}">Visit the channel →</a></div>
</div>
</div></section>
<section class="band sec" id="about"><div class="wrap"><div class="about reveal">
<h2>About Leon</h2>
<p>Leon Van Vuuren is a South African pharmacist. For years, the question he heard most across the counter was "Can I take this with my tablets?" This checker and his books give you clear, calm answers, so you can talk to your own doctor and pharmacist with confidence.</p>
<p class="hint">Privacy: this site uses no tracking and no sign-up. Your ticked medicines are saved only in your own browser.</p>
</div></div></section>
</main>'''
BOOKBTN=(f'<a class="cta" href="{BOOK}" target="_blank" rel="noopener">Get it on Amazon</a>' if BOOK else '<span class="cta soon">Coming soon on Amazon</span>')
extra=extra.replace('{BOOKBTN}',BOOKBTN+' <a class="cta sample" href="sample.pdf" target="_blank" rel="noopener">Read a free sample</a>')
if BOOK:
    body=body.replace('<span class="btn">Book coming soon on Amazon</span>',f'<a class="btn" href="{BOOK}" target="_blank" rel="noopener">Get the book on Amazon</a>')
body=body.replace('</div></main>',extra,1)
body=body.replace(STP.replace('&','&amp;'),STP)
import re as _re
body=_re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', body)
body=body.replace('<section class="top">','<section class="top reveal">',1).replace('<div class="grid">','<div class="grid reveal">',1)
js='''<script>
document.querySelectorAll('.hero h1 .w').forEach((w,i)=>w.style.animationDelay=(0.08*i+0.1)+'s');
const io=('IntersectionObserver' in window)?new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12}):null;
document.querySelectorAll('.reveal').forEach(el=>io?io.observe(el):el.classList.add('in'));
const hd=document.querySelector('header.band');addEventListener('scroll',()=>hd.classList.toggle('scrolled',scrollY>8),{passive:true});
</script>'''
body=body.replace('</body>',js+'</body>')
html=head+body.replace('__DATA__',data)
open('index.html','w').write(html)
print(len(html))
