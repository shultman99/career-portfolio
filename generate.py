"""Portfolio generator for my career portfolio."""

import shutil
from pathlib import Path

import yaml


def load_content() -> dict:
    """Load content from content.yaml file."""
    with open('data/content.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def generate_html(data: dict) -> str:
    """Generate HTML for the portfolio site.

    Args:
        data: Dictionary containing all portfolio content from YAML.

    Returns:
        Complete HTML document as a string.
    """
    profile = data['profile']
    contact = data['contact']
    skills = data['skills']
    experience = data['experience']
    projects = data['projects']
    education = data['education']
    featured_projects = [p for p in projects if p.get('featured', False)]
    photo_filename = Path(profile['photo']).name
    site_url = "https://arbowl.github.io/career-portfolio"
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{profile['tagline']}">
    <title>{profile['name']} - {profile['title']}</title>
    <meta property="og:title" content="{profile['name']} - {profile['title']}">
    <meta property="og:description" content="{profile['tagline']}">
    <meta property="og:image" content="{site_url}/images/og-default.png">
    <meta property="og:url" content="{site_url}">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{profile['name']} - {profile['title']}">
    <meta name="twitter:description" content="{profile['tagline']}">
    <meta name="twitter:image" content="{site_url}/images/og-default.png">
    <link rel="apple-touch-icon" sizes="57x57" href="images/apple-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="images/apple-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="images/apple-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="images/apple-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="images/apple-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="images/apple-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="images/apple-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="images/apple-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="images/apple-icon-180x180.png">
    <link rel="icon" type="image/png" sizes="192x192" href="images/android-icon-192x192.png">
    <link rel="icon" type="image/png" sizes="32x32" href="images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="96x96" href="images/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="16x16" href="images/favicon-16x16.png">
    <link rel="manifest" href="images/manifest.json">
    <meta name="msapplication-TileColor" content="#A17941">
    <meta name="msapplication-TileImage" content="images/ms-icon-144x144.png">
    <meta name="theme-color" content="#A17941">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav id="nav">
        <div class="nav-content">
            <a href="#top" class="nav-brand">{profile['name']}</a>
            <div class="nav-links">
                <a href="#about">About</a>
                <a href="#skills">Projects</a>
                <a href="#experience">Experience</a>
                <a href="#projects">Projects</a>
                <a href="#contact">Contact</a>
            </div>
        </div>
    </nav>

    <section id="top" class="hero">
        <div class="hero-content">
            <div class="hero-image">
                <img src="images/{photo_filename}" alt="{profile['name']}">
            </div>
            <h1>{profile['name']}</h1>
            <h2>{profile['title']}</h2>
            <p class="tagline">{profile['tagline']}</p>
            <div class="hero-links">
                <a href="mailto:{contact['email']}" class="btn">Email</a>
                <a href="{profile.get('resume', '#')}" class="btn btn-secondary" download>Resume</a>
                <a href="https://github.com/{contact['github']}" class="btn btn-secondary" target="_blank">GitHub</a>
                <a href="https://linkedin.com/{contact['linkedin']}" class="btn btn-secondary" target="_blank">LinkedIn</a>
            </div>
            <a href="#about" class="scroll-indicator">↓</a>
        </div>
    </section>

    <section id="about" class="section">
        <div class="container">
            <h2 class="section-title">About</h2>
            <div class="about-content">
                <p class="bio">{profile['bio']}</p>
                <div class="about-meta">
                    <div class="meta-item">
                        <span class="meta-label">Location</span>
                        <span class="meta-value">{profile['location']}</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Email</span>
                        <span class="meta-value">{contact['email']}</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Phone</span>
                        <span class="meta-value">{contact['phone']}</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="skills" class="section section-alt">
        <div class="container">
            <h2 class="section-title">Skills</h2>
            <div class="skills-grid">'''
    for skill_cat in skills:
        html += f'''
                <div class="skill-card">
                    <h3>{skill_cat['category']}</h3>
                    <ul class="skill-list">'''
        for item in skill_cat['items']:
            html += f'''
                        <li>{item}</li>'''
        html += '''
                    </ul>
                </div>'''
    html += '''
            </div>
        </div>
    </section>

    <section id="experience" class="section">
        <div class="container">
            <h2 class="section-title">Experience</h2>
            <div class="experience-timeline">'''
    for exp in experience:
        html += f'''
                <div class="experience-card">
                    <div class="experience-header">
                        <div>
                            <h3>{exp['title']}</h3>
                            <p class="company">{exp['company']} - {exp['location']}</p>
                        </div>
                        <span class="period">{exp['period']}</span>
                    </div>
                    <ul class="highlights">'''
        for highlight in exp['highlights']:
            html += f'''
                        <li>{highlight}</li>'''
        html += '''
                    </ul>
                </div>'''
    html += '''
            </div>
        </div>
    </section>

    <section id="contact" class="section">
        <div class="container">
            <h2 class="section-title">Get In Touch</h2>
            <div class="contact-content">
                <p>I'm always interested in discussing opportunities, questions, and projects.</p>
                <div class="contact-links">
                    <a href="mailto:{contact['email']}" class="contact-link">
                        <span class="contact-label">Email</span>
                        <span class="contact-value">{contact['email']}</span>
                    </a>
                    <a href="https://github.com/{contact['github']}" class="contact-link" target="_blank">
                        <span class="contact-label">GitHub</span>
                        <span class="contact-value">github.com/{contact['github']}</span>
                    </a>
                    <a href="https://linkedin.com/{contact['linkedin']}" class="contact-link" target="_blank">
                        <span class="contact-label">LinkedIn</span>
                        <span class="contact-value">linkedin.com/{contact['linkedin']}</span>
                    </a>
                    <a href="https://{contact['website']}" class="contact-link" target="_blank">
                        <span class="contact-label">Website</span>
                        <span class="contact-value">{contact['website']}</span>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2025 {profile['name']}. Built with Python, YAML, and minimal dependencies.</p>
            <p class="footer-education">{education['degree']} - {education['institution']} ({education['year']})</p>
        </div>
    </footer>

    <button id="back-to-top" class="back-to-top" aria-label="Back to top">↑</button>

    <script src="script.js"></script>
</body>
</html>'''
    return html


def generate_css() -> str:
    """Generate CSS for the portfolio site.

    Returns:
        Complete CSS stylesheet as a string.
    """
    return '''* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --navy: #E27628;
    --navy-light: #c49a5a;
    --navy-dark: #7a5c30;
    --gold: #fffde4;
    --gold-light: #fffff5;
    --off-white: #fafafa;
    --white: #ffffff;
    --text-dark: #2c3e50;
    --text-medium: #5a6c7d;
    --text-light: #8b9cad;
    --border: #e1e8ed;
    --shadow: rgba(26, 58, 82, 0.1);
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
    line-height: 1.6;
    color: var(--text-dark);
    background: var(--off-white);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

nav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: var(--white);
    box-shadow: 0 2px 10px var(--shadow);
    z-index: 1000;
}

.nav-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-brand {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--navy);
    text-decoration: none;
}

.nav-links {
    display: flex;
    gap: 2rem;
}

.nav-links a {
    color: var(--text-medium);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s;
}

.nav-links a:hover {
    color: var(--navy);
}

.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 6rem 2rem 4rem;
    background: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%);
    color: var(--white);
}

.hero-content {
    max-width: 800px;
}

.hero-image {
    margin-bottom: 2rem;
}

.hero-image img {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid var(--gold);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
    font-weight: 700;
}

.hero h2 {
    font-size: 1.5rem;
    font-weight: 400;
    color: var(--gold-light);
    margin-bottom: 1.5rem;
}

.tagline {
    font-size: 1.25rem;
    line-height: 1.8;
    margin-bottom: 2rem;
    color: rgba(255, 255, 255, 0.9);
}

.hero-links {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 3rem;
}

.btn {
    display: inline-block;
    padding: 0.75rem 2rem;
    background: var(--gold);
    color: var(--navy-dark);
    text-decoration: none;
    border-radius: 4px;
    font-weight: 600;
    transition: all 0.3s;
}

.btn:hover {
    background: var(--gold-light);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(244, 196, 48, 0.4);
}

.btn-secondary {
    background: transparent;
    border: 2px solid var(--white);
    color: var(--white);
}

.btn-secondary:hover {
    background: var(--white);
    color: var(--navy);
}

.scroll-indicator {
    display: inline-block;
    font-size: 2rem;
    color: var(--gold);
    text-decoration: none;
    animation: bounce 2s infinite;
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
    }
    40% {
        transform: translateY(-10px);
    }
    60% {
        transform: translateY(-5px);
    }
}

.section {
    padding: 5rem 0;
}

.section-alt {
    background: var(--white);
}

.section-title {
    font-size: 2.5rem;
    color: var(--navy);
    margin-bottom: 3rem;
    text-align: center;
    position: relative;
}

.section-title::after {
    content: '';
    display: block;
    width: 60px;
    height: 4px;
    background: var(--gold);
    margin: 1rem auto 0;
}

.about-content {
    max-width: 900px;
    margin: 0 auto;
}

.bio {
    font-size: 1.125rem;
    line-height: 1.8;
    margin-bottom: 2rem;
    text-align: center;
}

.about-meta {
    display: flex;
    justify-content: center;
    gap: 3rem;
    flex-wrap: wrap;
}

.meta-item {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.meta-label {
    font-size: 0.875rem;
    color: var(--text-light);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.25rem;
}

.meta-value {
    font-weight: 600;
    color: var(--navy);
}

.skills-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
}

.skill-card {
    background: var(--off-white);
    padding: 2rem;
    border-radius: 8px;
    border-left: 4px solid var(--navy);
    transition: all 0.3s;
}

.skill-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px var(--shadow);
}

.skill-card h3 {
    color: var(--navy);
    margin-bottom: 1rem;
    font-size: 1.25rem;
}

.skill-list {
    list-style: none;
}

.skill-list li {
    padding: 0.5rem 0;
    color: var(--text-dark);
    border-bottom: 1px solid var(--border);
}

.skill-list li:last-child {
    border-bottom: none;
}

.experience-timeline {
    max-width: 900px;
    margin: 0 auto;
}

.experience-card {
    background: var(--white);
    padding: 2rem;
    border-radius: 8px;
    margin-bottom: 2rem;
    border-left: 4px solid var(--gold);
    box-shadow: 0 2px 10px var(--shadow);
}

.experience-header {
    display: flex;
    justify-content: space-between;
    align-items: start;
    margin-bottom: 1rem;
    flex-wrap: wrap;
    gap: 1rem;
}

.experience-card h3 {
    color: var(--navy);
    font-size: 1.5rem;
    margin-bottom: 0.25rem;
}

.company {
    color: var(--text-medium);
    font-size: 1rem;
}

.period {
    color: var(--text-light);
    font-size: 0.875rem;
    font-weight: 600;
    background: var(--off-white);
    padding: 0.25rem 0.75rem;
    border-radius: 4px;
}

.highlights {
    list-style: none;
    padding-left: 0;
}

.highlights li {
    padding: 0.5rem 0 0.5rem 1.5rem;
    position: relative;
    line-height: 1.6;
}

.highlights li::before {
    content: '▸';
    position: absolute;
    left: 0;
    color: var(--gold);
    font-weight: bold;
}

.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
}

.project-card {
    background: var(--off-white);
    padding: 2rem;
    border-radius: 8px;
    border-top: 4px solid var(--navy);
    transition: all 0.3s;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

.project-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px var(--shadow);
}

.project-image {
    margin: -2rem -2rem 1.5rem -2rem;
    width: calc(100% + 4rem);
    overflow: hidden;
}

.project-image img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    object-position: top;
    display: block;
}

.project-header {
    display: flex;
    justify-content: space-between;
    align-items: start;
    margin-bottom: 1rem;
    gap: 1rem;
}

.project-card h3 {
    color: var(--navy);
    font-size: 1.5rem;
}

.project-description {
    color: var(--text-dark);
    line-height: 1.6;
    margin-bottom: 1rem;
    flex-grow: 1;
}

.project-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
}

.tag {
    background: var(--navy);
    color: var(--white);
    padding: 0.25rem 0.75rem;
    border-radius: 4px;
    font-size: 0.875rem;
}

.project-link {
    color: var(--navy);
    text-decoration: none;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    transition: color 0.3s;
}

.project-link:hover {
    color: var(--gold);
}

.contact-content {
    max-width: 700px;
    margin: 0 auto;
    text-align: center;
}

.contact-content > p {
    font-size: 1.125rem;
    margin-bottom: 2rem;
    color: var(--text-medium);
}

.contact-links {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
}

.contact-link {
    display: flex;
    flex-direction: column;
    padding: 1.5rem;
    background: var(--white);
    border-radius: 8px;
    text-decoration: none;
    border: 2px solid var(--border);
    transition: all 0.3s;
}

.contact-link:hover {
    border-color: var(--navy);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px var(--shadow);
}

.contact-label {
    font-size: 0.875rem;
    color: var(--text-light);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.5rem;
}

.contact-value {
    color: var(--navy);
    font-weight: 600;
}

footer {
    background: var(--navy-dark);
    color: var(--white);
    padding: 3rem 0;
    text-align: center;
}

footer p {
    margin: 0.5rem 0;
}

.footer-education {
    color: var(--gold-light);
    font-size: 0.875rem;
}

.back-to-top {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    width: 50px;
    height: 50px;
    background: var(--navy);
    color: var(--white);
    border: none;
    border-radius: 50%;
    font-size: 1.5rem;
    cursor: pointer;
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s;
    box-shadow: 0 4px 12px var(--shadow);
}

.back-to-top.visible {
    opacity: 1;
    visibility: visible;
}

.back-to-top:hover {
    background: var(--gold);
    color: var(--navy-dark);
    transform: translateY(-4px);
}

@media (max-width: 768px) {
    .nav-links {
        gap: 1rem;
        font-size: 0.875rem;
    }

    .hero h1 {
        font-size: 2rem;
    }

    .hero h2 {
        font-size: 1.25rem;
    }

    .tagline {
        font-size: 1rem;
    }

    .section-title {
        font-size: 2rem;
    }

    .skills-grid,
    .projects-grid {
        grid-template-columns: 1fr;
    }

    .about-meta {
        gap: 1.5rem;
    }

    .experience-header {
        flex-direction: column;
    }
}

@media (max-width: 480px) {
    .container {
        padding: 0 1rem;
    }

    .nav-content {
        padding: 1rem;
    }

    .nav-links {
        display: none;
    }

    .hero-image img {
        width: 150px;
        height: 150px;
    }

    .hero h1 {
        font-size: 1.75rem;
    }
}'''


def generate_js() -> str:
    """Generate JavaScript for the portfolio site.

    Returns:
        Complete JavaScript code as a string.
    """
    return '''document.addEventListener('DOMContentLoaded', function() {
    const backToTopButton = document.getElementById('back-to-top');
    const nav = document.getElementById('nav');

    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopButton.classList.add('visible');
        } else {
            backToTopButton.classList.remove('visible');
        }
    });

    backToTopButton.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    const navLinks = document.querySelectorAll('.nav-links a, .hero-links a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href.startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
});'''


def main() -> None:
    """Main function to generate the portfolio site."""
    print('Loading content from data/content.yaml...')
    data = load_content()
    print('Creating docs directory...')
    docs_dir = Path('docs')
    docs_dir.mkdir(exist_ok=True)
    docs_images_dir = docs_dir / 'images'
    docs_images_dir.mkdir(exist_ok=True)
    print('Generating HTML...')
    html = generate_html(data)
    with open(docs_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Generating CSS...')
    css = generate_css()
    with open(docs_dir / 'style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print('Generating JavaScript...')
    js = generate_js()
    with open(docs_dir / 'script.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print('Copying images...')
    data_images_dir = Path('data/images')
    if data_images_dir.exists():
        for image_file in data_images_dir.iterdir():
            if image_file.is_file():
                shutil.copy(image_file, docs_images_dir / image_file.name)
                print(f'  Copied {image_file.name}')
    else:
        print('  Warning: data/images directory not found')
    if 'resume' in data['profile']:
        resume_path = Path('data') / data['profile']['resume']
        if resume_path.exists():
            shutil.copy(resume_path, docs_dir / resume_path.name)
            print(f'Copied resume: {resume_path.name}')
        else:
            print(f'Warning: Resume not found at {resume_path}')
    print('\nPortfolio generated successfully!')
    print(f'Output location: {docs_dir.absolute()}')
    print('\nTo preview locally, open docs/index.html in your browser')
    print('To deploy to GitHub Pages:')
    print('  1. Commit and push all files')
    print('  2. Go to repository Settings > Pages')
    print('  3. Set source to "Deploy from a branch"')
    print('  4. Select "main" branch and "/docs" folder')
    print('  5. Save and wait for deployment')


if __name__ == '__main__':
    main()
