import re
import os

file_path = r"c:\Users\Admin\Downloads\project.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove intro screen
content = re.sub(r'<!-- ── INTRO SCREEN ── -->.*?<div class="intro-counter" id="intro-counter">000</div>\s*</div>', '', content, flags=re.DOTALL)

# 2. Change Nav
nav_search = r'<div class="nav-links">.*?</div>'
nav_replace = r'''<div class="nav-links">
          <a href="index.html" class="nav-close-trigger">← Back to Home</a>
        </div>'''
content = re.sub(nav_search, nav_replace, content, count=1, flags=re.DOTALL)

mobile_nav_search = r'<nav class="mobile-menu-links">.*?</nav>'
mobile_nav_replace = r'''<nav class="mobile-menu-links">
        <a href="index.html" id="mm-home">← Back to Home</a>
      </nav>'''
content = re.sub(mobile_nav_search, mobile_nav_replace, content, count=1, flags=re.DOTALL)

# Change Archive Title
content = content.replace("<span>Graphic Designer</span>", "<span>Archive</span>")

# 3. Replace body content from HERO to WORKS
body_search = r'<!-- ═══ HERO ═══ -->.*?<!-- ═══ GRAND FOOTER ═══ -->'
body_replace = r'''<!-- ═══ ARCHIVE HERO ═══ -->
    <section class="archive-hero" style="padding: 10rem 3rem 4rem; text-align: center;">
      <p class="section-label reveal">— Archive</p>
      <h1 class="section-title reveal reveal-delay-1" style="font-size: clamp(3rem, 8vw, 6rem); margin-bottom: 2rem;">Selected Works</h1>
      
      <div class="reveal reveal-delay-2" style="display: flex; justify-content: center; margin-top: 1.5rem;">
        <a href="index.html" class="btn-outline" style="text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="19" y1="12" x2="5" y2="12"></line>
            <polyline points="12 19 5 12 12 5"></polyline>
          </svg>
          Back to Home
        </a>
      </div>

      <div class="filter-bar reveal reveal-delay-3" id="filter-bar">
        <button class="filter-btn active" data-filter="all">All</button>
        <button class="filter-btn" data-filter="branding">Branding</button>
        <button class="filter-btn" data-filter="photography">Photography</button>
        <button class="filter-btn" data-filter="typography">Typography</button>
        <button class="filter-btn" data-filter="retouch">Retouch</button>
        <button class="filter-btn" data-filter="uxui">UX/UI</button>
      </div>
    </section>

    <!-- ═══ ARCHIVE GRID ═══ -->
    <section class="archive-grid-section" style="padding: 2rem 3rem 8rem;">
      <div class="archive-grid" style="max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fill, minmax(400px, 1fr)); gap: 3rem;">
        
        <div class="work-card-horizontal filter-item reveal" data-category="branding" style="height: 500px; width: 100%;">
          <div class="lando-label">Brand Identity, 2024</div>
          <div class="lando-img-wrap" style="border-radius: 12px;">
            <div class="work-bg" style="background: url('https://images.unsplash.com/photo-1600880292203-757bb62b4baf?q=80&w=1000&auto=format&fit=crop'); background-size: cover; background-position: center;"></div>
          </div>
        </div>
        
        <div class="work-card-horizontal filter-item reveal reveal-delay-1" data-category="photography" style="height: 600px; width: 100%;">
          <div class="lando-label">Photography, 2024</div>
          <div class="lando-img-wrap" style="border-radius: 12px;">
            <div class="work-bg" style="background: url('https://images.unsplash.com/photo-1516035069371-29a1b244cc32?q=80&w=1000&auto=format&fit=crop'); background-size: cover; background-position: center;"></div>
          </div>
        </div>

        <div class="work-card-horizontal filter-item reveal reveal-delay-2" data-category="retouch" style="height: 450px; width: 100%;">
          <div class="lando-label">Retouch, 2024</div>
          <div class="lando-img-wrap" style="border-radius: 12px;">
            <div class="work-bg" style="background: url('https://images.unsplash.com/photo-1542038784456-1ea8e935640e?q=80&w=1000&auto=format&fit=crop'); background-size: cover; background-position: center;"></div>
          </div>
        </div>

        <div class="work-card-horizontal filter-item reveal" data-category="typography" style="height: 650px; width: 100%;">
          <div class="lando-label">Typography, 2023</div>
          <div class="lando-img-wrap" style="border-radius: 12px;">
             <div class="work-bg" style="background: url('https://images.unsplash.com/photo-1523368743171-e7a9e334a179?q=80&w=1000&auto=format&fit=crop'); background-size: cover; background-position: center;"></div>
          </div>
        </div>

        <div class="work-card-horizontal filter-item reveal reveal-delay-1" data-category="uxui" style="height: 480px; width: 100%;">
          <div class="lando-label">UX/UI Design, 2023</div>
          <div class="lando-img-wrap" style="border-radius: 12px;">
             <div class="work-bg" style="background: url('https://images.unsplash.com/photo-1561070791-2526d30994b5?q=80&w=1000&auto=format&fit=crop'); background-size: cover; background-position: center;"></div>
          </div>
        </div>

        <div class="work-card-horizontal filter-item reveal reveal-delay-2" data-category="branding" style="height: 550px; width: 100%;">
          <div class="lando-label">Packaging Design, 2023</div>
          <div class="lando-img-wrap" style="border-radius: 12px;">
             <div class="work-bg" style="background: url('https://images.unsplash.com/photo-1607083206968-13611e3d76db?q=80&w=1000&auto=format&fit=crop'); background-size: cover; background-position: center;"></div>
          </div>
        </div>

        <div class="work-card-horizontal filter-item reveal" data-category="typography" style="height: 500px; width: 100%;">
          <div class="lando-label">Editorial, 2022</div>
          <div class="lando-img-wrap" style="border-radius: 12px;">
             <div class="work-bg" style="background: url('https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd?q=80&w=1000&auto=format&fit=crop'); background-size: cover; background-position: center;"></div>
          </div>
        </div>

        <div class="work-card-horizontal filter-item reveal reveal-delay-1" data-category="retouch" style="height: 600px; width: 100%;">
          <div class="lando-label">Photo Composite, 2022</div>
          <div class="lando-img-wrap" style="border-radius: 12px;">
             <div class="work-bg" style="background: url('https://images.unsplash.com/photo-1506744626753-1fa44df14d28?q=80&w=1000&auto=format&fit=crop'); background-size: cover; background-position: center;"></div>
          </div>
        </div>

      </div>
    </section>

    <!-- ═══ GRAND FOOTER ═══ -->'''
content = re.sub(body_search, body_replace, content, count=1, flags=re.DOTALL)


# 4. Add CSS
css_search = r'    .mobile-menu-cta:hover { opacity: 0.85; }'
css_replace = r'''    .mobile-menu-cta:hover { opacity: 0.85; }

    /* ══════════════════════════════
       FILTER BAR
    ══════════════════════════════ */
    .filter-bar {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.75rem;
      margin-top: 3rem;
      margin-bottom: 1rem;
    }

    .filter-btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: rgba(255, 255, 255, 0.6);
      padding: 0.6rem 1.4rem;
      border-radius: 9999px;
      font-family: 'Inter', sans-serif;
      font-size: 0.85rem;
      font-weight: 500;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      cursor: none;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      backdrop-filter: blur(10px);
    }

    .filter-btn:hover {
      background: rgba(255, 255, 255, 0.1);
      color: #fff;
    }

    .filter-btn.active {
      background: #fff;
      color: #080808;
      border-color: #fff;
      box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
    }'''
content = content.replace(css_search, css_replace)

# 5. Intro JS removal
intro_js_search = r'''    // ════════════════════════════════════════
    // SCROLL LOCK INTRO
    // ════════════════════════════════════════
    \(function \(\) \{
      const intro = document\.getElementById\('intro'\);
      const counter = document\.getElementById\('intro-counter'\);
      document\.body\.classList\.add\('intro-active'\);.*?setTimeout\(\(\) => \{
          document\.body\.classList\.remove\('intro-active'\);
          intro\.style\.display = 'none';
          // Initialize all scroll effects AFTER intro finishes
          initScrollEffects\(\);
        \}, 950\);
      \}, duration \+ 200\);
    \}\)\(\);'''
intro_js_replace = r'''    // ════════════════════════════════════════
    // INITIALIZE SCROLL EFFECTS IMMEDIATELY
    // ════════════════════════════════════════
    initScrollEffects();'''
content = re.sub(intro_js_search, intro_js_replace, content, flags=re.DOTALL)

# 6. Filter JS addition
js_search = r'      menu.addEventListener\(\'click\', function\(e\) \{\n        if \(e.target === menu\) closeMenu\(\);\n      \}\);\n    \}\)\(\);\n  </script>'
js_replace = r'''      menu.addEventListener('click', function(e) {
        if (e.target === menu) closeMenu();
      });
    })();

    // ════════════════════════════════════════
    // FILTER LOGIC
    // ════════════════════════════════════════
    (function() {
      const filterBtns = document.querySelectorAll('.filter-btn');
      const items = document.querySelectorAll('.filter-item');
      
      filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          // Update active class
          filterBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          
          const filterValue = btn.getAttribute('data-filter');
          
          items.forEach(item => {
            const category = item.getAttribute('data-category');
            
            if (filterValue === 'all' || filterValue === category) {
              gsap.to(item, {
                scale: 1,
                opacity: 1,
                duration: 0.4,
                ease: 'power2.out',
                display: 'block'
              });
            } else {
              gsap.to(item, {
                scale: 0.8,
                opacity: 0,
                duration: 0.4,
                ease: 'power2.out',
                onComplete: () => {
                  item.style.display = 'none';
                }
              });
            }
          });
          
          // Refresh scroll trigger after animation completes
          setTimeout(() => ScrollTrigger.refresh(), 450);
        });
      });
    })();
  </script>'''
content = re.sub(js_search, js_replace, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done generating project.html!")
