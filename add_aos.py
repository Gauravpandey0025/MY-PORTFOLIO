import os

file_path = r"c:\Users\rocka\OneDrive\Desktop\projects\portfolio\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add AOS CSS to Head
target_head = '    <link rel="stylesheet" href="style.css">'
replacement_head = '    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">\n    <link rel="stylesheet" href="style.css">'
content = content.replace(target_head, replacement_head)

# 2. Add AOS JS and Init to Body End
target_body_end = '</body>'
replacement_body_end = '''    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({
            duration: 800,
            once: true,
            offset: 100,
        });
    </script>
</body>'''
content = content.replace(target_body_end, replacement_body_end)

# 3. Add data-aos to elements
replacements = {
    '<div class="hero-content">': '<div class="hero-content" data-aos="fade-up" data-aos-duration="1000">',
    '<div class="section-title">': '<div class="section-title" data-aos="fade-in">',
    '<div class="about-img">': '<div class="about-img" data-aos="fade-right">',
    '<div class="about-text">': '<div class="about-text" data-aos="fade-left">',
    '<div class="skill-card">': '<div class="skill-card" data-aos="zoom-in" data-aos-delay="100">',
    '<div class="project-card">': '<div class="project-card" data-aos="fade-up" data-aos-delay="100">',
    '<div class="timeline-item left">': '<div class="timeline-item left" data-aos="fade-right">',
    '<div class="timeline-item right">': '<div class="timeline-item right" data-aos="fade-left">',
    '<div class="certificate-card">': '<div class="certificate-card" data-aos="zoom-in" data-aos-delay="100">',
    '<div class="contact-info">': '<div class="contact-info" data-aos="fade-right">',
    '<div class="contact-form">': '<div class="contact-form" data-aos="fade-left">',
}

for target, replacement in replacements.items():
    content = content.replace(target, replacement)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("AOS additions successful.")
