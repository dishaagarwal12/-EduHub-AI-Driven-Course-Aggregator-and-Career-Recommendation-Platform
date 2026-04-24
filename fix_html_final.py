import sys

def fix_html():
    filepath = "d:\\PROJECT\\ux_sample.html"
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    start_marker = '<div class="row g-4" id="course-container">'
    chatbot_marker = '<!-- Floating Chatbot Button -->'
    
    start_idx = text.find(start_marker)
    chatbot_idx = text.find(chatbot_marker)
    
    if start_idx == -1 or chatbot_idx == -1:
        print("Markers not found.")
        sys.exit(1)
        
    end_idx = text.rfind('</section>', 0, chatbot_idx)
    
    if end_idx == -1 or end_idx < start_idx:
        print("End section marker not found correctly.")
        sys.exit(1)

    replacement = """<div class="row g-4" id="course-container">
                    <!-- Courses empty as requested -->
                </div>
            </div>
    </section>
"""
    
    new_text = text[:start_idx] + replacement + text[end_idx + len('</section>'):]
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_text)
        
    print("Cleaned successfully.")

if __name__ == "__main__":
    fix_html()
