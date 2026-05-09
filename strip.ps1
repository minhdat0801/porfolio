$path = "c:\Users\Admin\Downloads\project.html"
$utf8 = New-Object System.Text.UTF8Encoding($false)
$content = [System.IO.File]::ReadAllText($path, $utf8)

# Strip out Marquee 1 down to Works
$search = '(?s)    <hr class="divider" />\s*<!-- ═══ MARQUEE 1 ═══ -->.*?<!-- ═══ GRAND FOOTER ═══ -->'
$replace = '<!-- ═══ GRAND FOOTER ═══ -->'
$content = [regex]::Replace($content, $search, $replace, 1)

# Remove intro
$introSearch = '(?s)  <!-- ── INTRO SCREEN ── -->.*?<div class="intro-counter" id="intro-counter">000</div>\s*</div>'
$content = [regex]::Replace($content, $introSearch, '', 1)

# Update nav
$content = $content.Replace('<span>Graphic Designer</span>', '<span>Archive</span>')

$deskNavSearch = '(?s)<div class="nav-links">.*?</div>'
$deskNavReplace = '<div class="nav-links">
          <a href="index.html" class="nav-close-trigger">← Back to Home</a>
        </div>'
$content = [regex]::Replace($content, $deskNavSearch, $deskNavReplace, 1)

$mobileNavSearch = '(?s)<nav class="mobile-menu-links">.*?</nav>'
$mobileNavReplace = '<nav class="mobile-menu-links">
        <a href="index.html" id="mm-home">← Back to Home</a>
      </nav>'
$content = [regex]::Replace($content, $mobileNavSearch, $mobileNavReplace, 1)

# Add CSS
$cssSearch = '    .mobile-menu-cta:hover { opacity: 0.85; }'
$cssReplace = '    .mobile-menu-cta:hover { opacity: 0.85; }

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
      font-family: ''Inter'', sans-serif;
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
    }'
if (-not $content.Contains('.filter-bar {')) {
    $content = $content.Replace($cssSearch, $cssReplace)
}

# Replace Intro JS with direct init
$introJsSearch = '(?s)    // ════════════════════════════════════════
    // SCROLL LOCK INTRO
    // ════════════════════════════════════════
    \(function \(\) \{
      const intro = document\.getElementById\(''intro''\);
      const counter = document\.getElementById\(''intro-counter''\);.*?setTimeout\(\(\) => \{.*?initScrollEffects\(\);.*?\}, 950\);
      \}, duration \+ 200\);
    \}\)\(\);'
$introJsReplace = '    // ════════════════════════════════════════
    // INITIALIZE SCROLL EFFECTS IMMEDIATELY
    // ════════════════════════════════════════
    initScrollEffects();'
$content = [regex]::Replace($content, $introJsSearch, $introJsReplace, 1)

# Add Filter JS logic
$jsSearch = "(?s)      // Close on backdrop click
      menu\.addEventListener\('click', function\(e\) \{
        if \(e\.target === menu\) closeMenu\(\);
      \}\);
    \}\)\(\);\n  </script>"
$jsReplace = "      // Close on backdrop click
      menu.addEventListener('click', function(e) {
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
  </script>"
if (-not $content.Contains('FILTER LOGIC')) {
    $content = [regex]::Replace($content, $jsSearch, $jsReplace, 1)
}

[System.IO.File]::WriteAllText($path, $content, $utf8)
Write-Output "Fixed."
