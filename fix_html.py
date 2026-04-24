import sys

with open("d:\\PROJECT\\ux_sample.html", "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '<div class="row g-4" id="course-container">'
end_marker = '</section>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found!")
    sys.exit(1)

new_html_content = """
                    <!-- UPSC CSE Card -->
                    <div class="col-xl-4 col-lg-6 col-md-6 course-element" data-exam="upsc_cse" data-price="4999" data-rating="4.8" data-language="english">
                        <a href="https://unacademy.com/goal/upsc-civil-services-examination-ias-preparation/KSCGY" target="_blank" style="text-decoration: none; color: inherit;">
                            <div class="course-card-3d tilt-card">
                                <div class="reflection"></div>
                                <div class="course-card-inner">
                                    <img src="https://images.unsplash.com/photo-1596484552834-8a58f9fc2fec?auto=format&fit=crop&w=400&q=80" alt="Sankalp Batch 2024" style="width: 100%; height: 160px; object-fit: cover; border-radius: 14px; margin-bottom: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.3); transform: translateZ(30px);">
                                    <span class="exam-badge">UPSC CSE</span>
                                    <h3 class="course-h3">Sankalp Batch 2024</h3>
                                    
                                    <div class="course-details">
                                        <span><i class="bi bi-translate me-1"></i> English</span>
                                        <span class="text-warning ms-auto" style="font-size: 0.85rem;">
                                            <i class="bi bi-star-fill"></i>
                                            <i class="bi bi-star-fill"></i>
                                            <i class="bi bi-star-fill"></i>
                                            <i class="bi bi-star-fill"></i>
                                            <i class="bi bi-star-half"></i>
                                            <span class="text-white ms-1">4.8</span>
                                        </span>
                                    </div>
                                    <div class="course-details" style="margin-bottom: 20px;">
                                        <span><i class="bi bi-person me-1"></i> Mrunal P.</span>
                                    </div>
                                    <div class="course-footer">
                                        <span class="course-price">₹4,999</span>
                                        <button class="buy-btn">View</button>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </div>

                    <!-- JEE Main Card -->
                    <div class="col-xl-4 col-lg-6 col-md-6 course-element" data-exam="jee_main" data-price="4500" data-rating="4.8" data-language="hindi">
                        <a href="https://pw.live/batches/jee/lakshya-jee-2025" target="_blank" style="text-decoration: none; color: inherit;">
                            <div class="course-card-3d tilt-card">
                                <div class="reflection"></div>
                                <div class="course-card-inner">
                                    <img src="https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&w=400&q=80" alt="Lakshya JEE (Class 12)" style="width: 100%; height: 160px; object-fit: cover; border-radius: 14px; margin-bottom: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.3); transform: translateZ(30px);">
                                    <span class="exam-badge" style="color: #ff9f43;">JEE Main & Adv</span>
                                    <h3 class="course-h3">Lakshya JEE (Class 12)</h3>
                                    
                                    <div class="course-details">
                                        <span><i class="bi bi-translate me-1"></i> Hindi</span>
                                        <span class="text-warning ms-auto" style="font-size: 0.85rem;">
                                            <i class="bi bi-star-fill"></i>
                                            <i class="bi bi-star-fill"></i>
                                            <i class="bi bi-star-fill"></i>
                                            <i class="bi bi-star-fill"></i>
                                            <i class="bi bi-star-half"></i>
                                            <span class="text-white ms-1">4.8</span>
                                        </span>
                                    </div>
                                    <div class="course-details" style="margin-bottom: 20px;">
                                        <span><i class="bi bi-person me-1"></i> Rajwant Sir</span>
                                    </div>
                                    <div class="course-footer">
                                        <span class="course-price">₹4,500</span>
                                        <button class="buy-btn">View</button>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </div>

                    <!-- Banking Card -->
                    <div class="col-xl-4 col-lg-6 col-md-6 course-element" data-exam="ibps_po" data-price="1299" data-rating="5.0" data-language="bilingual">
                        <a href="https://unacademy.com/goal/bank-exams/RTPSX" target="_blank" style="text-decoration: none; color: inherit;">
                            <div class="course-card-3d tilt-card">
                                <div class="reflection"></div>
                                <div class="course-card-inner">
                                    <img src="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=400&q=80" alt="IBPS PO Pro Selection" style="width: 100%; height: 160px; object-fit: cover; border-radius: 14px; margin-bottom: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.3); transform: translateZ(30px);">
                                    <span class="exam-badge">Banking</span>
                                    <h3 class="course-h3">IBPS PO Pro Selection</h3>
                                    
                                    <div class="course-details">
                                        <span><i class="bi bi-translate me-1"></i> Bilingual</span>
                                        <span class="text-warning ms-auto" style="font-size: 0.85rem;">
                                            <i class="bi bi-star-fill"></i>
                                            <i class="bi bi-star-fill"></i>
                                            <i class="bi bi-star-fill"></i>
                                            <i class="bi bi-star-fill"></i>
                                            <i class="bi bi-star-fill"></i>
                                            <span class="text-white ms-1">5.0</span>
                                        </span>
                                    </div>
                                    <div class="course-details" style="margin-bottom: 20px;">
                                        <span><i class="bi bi-person me-1"></i> Puneet S.</span>
                                    </div>
                                    <div class="course-footer">
                                        <span class="course-price">₹1,299</span>
                                        <button class="buy-btn">View</button>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
    """

new_content = content[:start_idx + len(start_marker)] + "\n" + new_html_content + "\n    " + content[end_idx:]

with open("d:\\PROJECT\\ux_sample.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("HTML fixed successfully!")
