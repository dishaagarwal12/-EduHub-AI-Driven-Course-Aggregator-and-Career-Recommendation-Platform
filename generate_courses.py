import re

html_file = "d:/PROJECT/ux_sample.html"

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

new_jee_courses = [
    {
        "exam": "jee_main", "badge": "JEE Main & Adv", "title": "Lakshya JEE (Class 12)", "instructor": "Rajwant Sir", "price": 4500, "rating": 4.8, "lang": "hindi", "lang_label": "Hindi", "link": "https://pw.live", "img": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&w=400&q=80",
        "stars": ['fill','fill','fill','fill','half']
    },
    {
        "exam": "jee_main", "badge": "JEE Dropper", "title": "Prayas JEE 2025", "instructor": "Sachin Sir", "price": 4800, "rating": 4.9, "lang": "hindi", "lang_label": "Hindi", "link": "https://pw.live", "img": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&w=400&q=80",
        "stars": ['fill','fill','fill','fill','fill']
    },
    {
        "exam": "jee_main", "badge": "JEE Dropper", "title": "Excel Batch", "instructor": "Brijesh J.", "price": 12000, "rating": 4.6, "lang": "english", "lang_label": "English", "link": "https://unacademy.com", "img": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=400&q=80",
        "stars": ['fill','fill','fill','fill','half']
    },
    {
        "exam": "jee_main", "badge": "JEE Class 11", "title": "Emerge Batch", "instructor": "Vineet L.", "price": 15000, "rating": 4.7, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://unacademy.com", "img": "https://images.unsplash.com/photo-1563804369792-71c1efeb5086?auto=format&fit=crop&w=400&q=80",
        "stars": ['fill','fill','fill','fill','half']
    },
    {
        "exam": "jee_main", "badge": "JEE Advanced", "title": "Eklavya JEE", "instructor": "Anand P.", "price": 0, "rating": 4.9, "lang": "english", "lang_label": "English", "link": "https://vedantu.com", "img": "https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&w=400&q=80",
        "stars": ['fill','fill','fill','fill','fill']
    },
    {
        "exam": "jee_main", "badge": "JEE Class 11", "title": "Nurture Batch", "instructor": "Allen Expert", "price": 10000, "rating": 4.8, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://allen.ac.in", "img": "https://images.unsplash.com/photo-1620025964894-323a7bb7d5d2?auto=format&fit=crop&w=400&q=80",
        "stars": ['fill','fill','fill','fill','half']
    },
    {
        "exam": "jee_main", "badge": "JEE Dropper", "title": "Leader Batch", "instructor": "Allen Expert", "price": 10000, "rating": 4.7, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://allen.ac.in", "img": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=400&q=80",
        "stars": ['fill','fill','fill','fill','half']
    },
    {
        "exam": "jee_main", "badge": "JEE Dropper", "title": "Aakash Repeater", "instructor": "Aakash Faculty", "price": 10000, "rating": 4.5, "lang": "english", "lang_label": "English", "link": "https://aakash.ac.in", "img": "https://images.unsplash.com/photo-1517420704952-d9f39741e815?auto=format&fit=crop&w=400&q=80",
        "stars": ['fill','fill','fill','fill','half']
    },
    {
        "exam": "jee_main", "badge": "JEE Advanced", "title": "FIITJEE Pinnacle", "instructor": "FIITJEE Team", "price": 10000, "rating": 4.6, "lang": "english", "lang_label": "English", "link": "https://fiitjee.com", "img": "https://images.unsplash.com/photo-1504164996022-09080787b6b3?auto=format&fit=crop&w=400&q=80",
        "stars": ['fill','fill','fill','fill','half']
    }
]

html_cards = ""
for c in new_jee_courses:
    star_html = ""
    for s in c['stars']:
        if s == 'fill':
            star_html += '<i class="bi bi-star-fill"></i>\\n'
        elif s == 'half':
            star_html += '<i class="bi bi-star-half"></i>\\n'
        else:
            star_html += '<i class="bi bi-star"></i>\\n'
            
    price_str = f"₹{c['price']:,}" if c['price'] > 0 else "Free"

    card = f'''
                    <div class="col-xl-4 col-lg-6 col-md-6 course-element" data-exam="{c['exam']}" data-price="{c['price']}" data-rating="{c['rating']}" data-language="{c['lang']}">
                        <a href="{c['link']}" target="_blank" style="text-decoration: none; color: inherit;">
                            <div class="course-card-3d tilt-card">
                                <div class="reflection"></div>
                                <div class="course-card-inner">
                                    <img src="{c['img']}" alt="{c['title']}" style="width: 100%; height: 160px; object-fit: cover; border-radius: 14px; margin-bottom: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.3); transform: translateZ(30px);">
                                    <span class="exam-badge" style="color: #ff9f43;">{c['badge']}</span>
                                    <h3 class="course-h3">{c['title']}</h3>
                                    
                                    <div class="course-details">
                                        <span><i class="bi bi-translate me-1"></i> {c['lang_label']}</span>
                                        <span class="text-warning ms-auto" style="font-size: 0.85rem;">
                                            {star_html}
                                            <span class="text-white ms-1">{c['rating']}</span>
                                        </span>
                                    </div>
                                    <div class="course-details" style="margin-bottom: 20px;">
                                        <span><i class="bi bi-person me-1"></i> {c['instructor']}</span>
                                    </div>
                                    <div class="course-footer">
                                        <span class="course-price">{price_str}</span>
                                        <button class="buy-btn">View</button>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </div>
'''
    html_cards += card

# Insert right before the closing div of #course-container
match = re.search(r'(<div class="row g-4" id="course-container">.*?)(                </div>\s*</div>)', html, flags=re.DOTALL)
if match:
    new_html = html[:match.end(1)] + html_cards + html[match.end(1):]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("JEE Courses appended successfully!")
else:
    print("Could not find the end of #course-container")
