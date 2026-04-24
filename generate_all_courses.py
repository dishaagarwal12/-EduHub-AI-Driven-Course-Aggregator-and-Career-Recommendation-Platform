import re

html_file = "d:/PROJECT/ux_sample.html"

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Comprehensive Dataset covering all 41 exam categories with at least 2 courses each
course_data = [
    # 👷‍♂️ ENGINEERING EXAMS
    {"exam": "jee_main", "badge": "JEE Main 2025", "title": "Arjuna JEE Batch", "instructor": "Alakh Pandey", "price": 4500, "rating": 4.9, "lang": "hindi", "lang_label": "Hindi", "link": "https://pw.live", "img": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&w=400&q=80"},
    {"exam": "jee_main", "badge": "JEE Main Prep", "title": "Physics Galaxy Concept", "instructor": "Ashish Arora", "price": 0, "rating": 5.0, "lang": "english", "lang_label": "English", "link": "https://physicsgalaxy.com", "img": "https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=400&q=80"},
    {"exam": "jee_advanced", "badge": "JEE Advanced", "title": "FIITJEE Rankers Study", "instructor": "FIITJEE Faculty", "price": 15000, "rating": 4.8, "lang": "english", "lang_label": "English", "link": "https://fiitjee.com", "img": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&w=400&q=80"},
    {"exam": "jee_advanced", "badge": "JEE Advanced", "title": "Varun Advanced Batch", "instructor": "PW Team", "price": 3500, "rating": 4.7, "lang": "hindi", "lang_label": "Hindi", "link": "https://pw.live", "img": "https://images.unsplash.com/photo-1579373903781-fd5c0c30c4cd?auto=format&fit=crop&w=400&q=80"},
    {"exam": "bitsat", "badge": "BITSAT 2025", "title": "Mathongo BITSAT Course", "instructor": "Anup Sir", "price": 3200, "rating": 4.9, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://mathongo.com", "img": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=400&q=80"},
    {"exam": "bitsat", "badge": "BITSAT Prep", "title": "Embibe BITSAT Mock", "instructor": "Embibe Team", "price": 0, "rating": 4.5, "lang": "english", "lang_label": "English", "link": "https://embibe.com", "img": "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&w=400&q=80"},
    {"exam": "viteee", "badge": "VITEEE 2025", "title": "VIT Master Course", "instructor": "Vidyakul", "price": 1200, "rating": 4.3, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://vidyakul.com", "img": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=400&q=80"},
    {"exam": "viteee", "badge": "VITEEE Special", "title": "Gradeup VIT Batch", "instructor": "BYJU'S Prep", "price": 899, "rating": 4.1, "lang": "hindi", "lang_label": "Hindi", "link": "https://byjusexamprep.com", "img": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=400&q=80"},

    # 🧠 MEDICAL EXAMS
    {"exam": "neet_ug", "badge": "NEET UG 2025", "title": "Yakeen NEET Dropper", "instructor": "Alakh Pandey", "price": 4200, "rating": 4.9, "lang": "hindi", "lang_label": "Hindi", "link": "https://pw.live", "img": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=400&q=80"},
    {"exam": "neet_ug", "badge": "NEET Biology", "title": "BeWise NEET Biology", "instructor": "Sunil Nain", "price": 0, "rating": 4.8, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://bewiseclasses.com", "img": "https://images.unsplash.com/photo-1530210124550-912dc1381cb8?auto=format&fit=crop&w=400&q=80"},
    {"exam": "neet_pg", "badge": "NEET PG Prep", "title": "Marrow Edition 8", "instructor": "Marrow Faculty", "price": 12500, "rating": 4.9, "lang": "english", "lang_label": "English", "link": "https://marrow.com", "img": "https://images.unsplash.com/photo-1581056771107-24ca5f033842?auto=format&fit=crop&w=400&q=80"},
    {"exam": "neet_pg", "badge": "NEET PG 2025", "title": "PrepLadder Rapid", "instructor": "Dr. Deepshikha", "price": 9500, "rating": 4.7, "lang": "english", "lang_label": "English", "link": "https://prepladder.com", "img": "https://images.unsplash.com/photo-1505751172876-fa1923c5c528?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ini_cet", "badge": "INI-CET 2025", "title": "DAMS INI-CET Pro", "instructor": "Dr. Sumer Sethi", "price": 11000, "rating": 4.8, "lang": "english", "lang_label": "English", "link": "https://damsdelhi.com", "img": "https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ini_cet", "badge": "INI-CET Special", "title": "Cerebellum Special", "instructor": "Dr. Zainab Vora", "price": 8000, "rating": 4.9, "lang": "english", "lang_label": "English", "link": "https://cerebellumacademy.com", "img": "https://images.unsplash.com/photo-1551076805-e1869033e561?auto=format&fit=crop&w=400&q=80"},

    # 🏛️ UPSC & CIVIL SERVICES
    {"exam": "upsc_cse", "badge": "UPSC IAS 2025", "title": "Foundation Batch - GS", "instructor": "Khan Sir", "price": 0, "rating": 5.0, "lang": "hindi", "lang_label": "Hindi", "link": "https://youtube.com", "img": "https://images.unsplash.com/photo-1455390582262-044cdead2708?auto=format&fit=crop&w=400&q=80"},
    {"exam": "upsc_cse", "badge": "UPSC Mains", "title": "Answer Writing Mastery", "instructor": "Drishti IAS", "price": 4500, "rating": 4.8, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://drishtiias.com", "img": "https://images.unsplash.com/photo-1544928147-79a2dbc1f389?auto=format&fit=crop&w=400&q=80"},
    {"exam": "state_psc", "badge": "UPPSC & BPSC", "title": "State Services Pro", "instructor": "StudyIQ", "price": 8500, "rating": 4.5, "lang": "english", "lang_label": "English", "link": "https://studyiq.com", "img": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?auto=format&fit=crop&w=400&q=80"},
    {"exam": "state_psc", "badge": "State PCS", "title": "Drishti PCS Batch", "instructor": "Vikas Divyakirti", "price": 12000, "rating": 4.9, "lang": "hindi", "lang_label": "Hindi", "link": "https://drishtiias.com", "img": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=400&q=80"},
    {"exam": "upsc_epfo", "badge": "UPSC EPFO 2025", "title": "EPFO AO/EO Batch", "instructor": "EduTap", "price": 4000, "rating": 4.6, "lang": "english", "lang_label": "English", "link": "https://edutap.co.in", "img": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=400&q=80"},
    {"exam": "upsc_epfo", "badge": "EPFO Prep", "title": "Adda247 EPFO Special", "instructor": "Adda247 Team", "price": 2500, "rating": 4.4, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://adda247.com", "img": "https://images.unsplash.com/photo-1553484771-047a44eee27f?auto=format&fit=crop&w=400&q=80"},

    # 🏦 BANKING EXAMS
    {"exam": "sbi_po", "badge": "SBI PO Prelims", "title": "Banker's Way", "instructor": "Adda247 Team", "price": 1200, "rating": 4.4, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://adda247.com", "img": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?auto=format&fit=crop&w=400&q=80"},
    {"exam": "sbi_po", "badge": "SBI PO 2025", "title": "Unacademy Plus Bank", "instructor": "Ankush Lamba", "price": 5000, "rating": 4.9, "lang": "hindi", "lang_label": "Hindi", "link": "https://unacademy.com", "img": "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&w=400&q=80"},
    {"exam": "sbi_clerk", "badge": "SBI Clerk Prep", "title": "Testbook Smart Pass", "instructor": "Testbook Team", "price": 499, "rating": 4.3, "lang": "english", "lang_label": "English", "link": "https://testbook.com", "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=400&q=80"},
    {"exam": "sbi_clerk", "badge": "SBI Clerk 2025", "title": "Oliveboard Special", "instructor": "Oliveboard", "price": 1500, "rating": 4.6, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://oliveboard.in", "img": "https://images.unsplash.com/photo-1556740758-90eb3af51c2d?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ibps_po", "badge": "IBPS PO Pro", "title": "Bank Wallah PO", "instructor": "Saurabh Sir", "price": 2500, "rating": 4.7, "lang": "hindi", "lang_label": "Hindi", "link": "https://pw.live", "img": "https://images.unsplash.com/photo-1550565118-3d1428df73e0?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ibps_po", "badge": "IBPS PO Prep", "title": "Career Power Batch", "instructor": "Adda247", "price": 3200, "rating": 4.5, "lang": "english", "lang_label": "English", "link": "https://adda247.com", "img": "https://images.unsplash.com/photo-1565514020179-026b92b84bb6?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ibps_clerk", "badge": "IBPS Clerk 2025", "title": "Exampur Selection", "instructor": "Vivek Sir", "price": 999, "rating": 4.4, "lang": "hindi", "lang_label": "Hindi", "link": "https://exampur.com", "img": "https://images.unsplash.com/photo-1554224155-16974fa0f2c5?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ibps_clerk", "badge": "IBPS Clerk Mega", "title": "Guidely Smart Course", "instructor": "Guidely Team", "price": 799, "rating": 4.2, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://guidely.in", "img": "https://images.unsplash.com/photo-1508672019048-805c876b67e2?auto=format&fit=crop&w=400&q=80"},
    {"exam": "rbi_grade_b", "badge": "RBI Grade B Pro", "title": "Edutap RBI Master", "instructor": "Edutap Faculty", "price": 8500, "rating": 4.8, "lang": "english", "lang_label": "English", "link": "https://edutap.co.in", "img": "https://images.unsplash.com/photo-1628156113473-b7834a6abc42?auto=format&fit=crop&w=400&q=80"},
    {"exam": "rbi_grade_b", "badge": "RBI Grade B Special", "title": "Anuj Jindal RBI", "instructor": "Anuj Jindal", "price": 12000, "rating": 4.9, "lang": "english", "lang_label": "English", "link": "https://anujjindal.in", "img": "https://images.unsplash.com/photo-1579621970795-87f127f32997?auto=format&fit=crop&w=400&q=80"},

    # 🚆 SSC & GOVERNMENT JOBS
    {"exam": "ssc_cgl", "badge": "SSC CGL 2025", "title": "Abhinay Maths Advanced", "instructor": "Abhinay Sir", "price": 999, "rating": 4.6, "lang": "hindi", "lang_label": "Hindi", "link": "https://abhinaymaths.com", "img": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ssc_cgl", "badge": "SSC CGL Mains", "title": "Gagan Pratap Maths", "instructor": "Gagan Sir", "price": 1200, "rating": 4.8, "lang": "hindi", "lang_label": "Hindi", "link": "https://careerwill.com", "img": "https://images.unsplash.com/photo-1543269865-cbf427effbad?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ssc_chsl", "badge": "SSC CHSL Basic", "title": "Testbook CHSL Course", "instructor": "Testbook Team", "price": 499, "rating": 4.1, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://testbook.com", "img": "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ssc_chsl", "badge": "SSC CHSL Special", "title": "Rankers Gurukul", "instructor": "Aditya Ranjan", "price": 699, "rating": 4.7, "lang": "hindi", "lang_label": "Hindi", "link": "https://rankersgurukul.com", "img": "https://images.unsplash.com/photo-1606326608996-af157bb1593c?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ssc_je", "badge": "SSC JE 2025", "title": "Engineers Academy JE", "instructor": "EA Team", "price": 3500, "rating": 4.5, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://engineersacademy.org", "img": "https://images.unsplash.com/photo-1581094794329-c8112a89af12?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ssc_je", "badge": "SSC JE Technical", "title": "Unacademy SSC JE", "instructor": "Rahul Sir", "price": 4000, "rating": 4.2, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://unacademy.com", "img": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=400&q=80"},
    {"exam": "rrb_ntpc", "badge": "Railway NTPC", "title": "WifiStudy Crash Course", "instructor": "Sahil Sir", "price": 0, "rating": 4.3, "lang": "hindi", "lang_label": "Hindi", "link": "https://youtube.com", "img": "https://images.unsplash.com/photo-1474487548417-781cb71495f3?auto=format&fit=crop&w=400&q=80"},
    {"exam": "rrb_ntpc", "badge": "RRB NTPC 2025", "title": "Toprankers Railway", "instructor": "TR Team", "price": 899, "rating": 4.0, "lang": "hindi", "lang_label": "Hindi", "link": "https://toprankers.com", "img": "https://images.unsplash.com/photo-1532102235608-620023a78065?auto=format&fit=crop&w=400&q=80"},
    {"exam": "rrb_alp", "badge": "RRB ALP Prep", "title": "Exampur ALP Batch", "instructor": "Abhishek Sir", "price": 1200, "rating": 4.4, "lang": "hindi", "lang_label": "Hindi", "link": "https://exampur.com", "img": "https://images.unsplash.com/photo-1510519133417-2ad0b387c9b9?auto=format&fit=crop&w=400&q=80"},
    {"exam": "rrb_alp", "badge": "Railway ALP Tech", "title": "Platform Coaching", "instructor": "Rukmini Team", "price": 599, "rating": 4.1, "lang": "hindi", "lang_label": "Hindi", "link": "https://platform.com", "img": "https://images.unsplash.com/photo-1447433588726-ad7308d770c3?auto=format&fit=crop&w=400&q=80"},

    # ⚖️ LAW EXAMS
    {"exam": "clat", "badge": "CLAT 2025", "title": "Legal Edge Clat Course", "instructor": "Toprankers", "price": 8500, "rating": 4.5, "lang": "english", "lang_label": "English", "link": "https://toprankers.com", "img": "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&w=400&q=80"},
    {"exam": "clat", "badge": "CLAT Prep", "title": "Unacademy Law Plus", "instructor": "Keshav Sir", "price": 12000, "rating": 4.7, "lang": "english", "lang_label": "English", "link": "https://unacademy.com", "img": "https://images.unsplash.com/photo-1505664159811-2eb2d4c09d57?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ailet", "badge": "AILET 2025", "title": "LawSikho AILET Pro", "instructor": "Abhyuday Sir", "price": 15000, "rating": 4.8, "lang": "english", "lang_label": "English", "link": "https://lawsikho.com", "img": "https://images.unsplash.com/photo-1589923188900-85dae523342b?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ailet", "badge": "AILET Prep", "title": "Career Launcher Law", "instructor": "CL Team", "price": 18000, "rating": 4.6, "lang": "english", "lang_label": "English", "link": "https://careerlauncher.com", "img": "https://images.unsplash.com/photo-1582213782179-e0d53f98f2ca?auto=format&fit=crop&w=400&q=80"},
    {"exam": "judiciary", "badge": "Judiciary Basic", "title": "Law Sikho Foundation", "instructor": "Ramanuj M.", "price": 15000, "rating": 4.8, "lang": "english", "lang_label": "English", "link": "https://lawsikho.com", "img": "https://images.unsplash.com/photo-1453919102434-601962366b1a?auto=format&fit=crop&w=400&q=80"},
    {"exam": "judiciary", "badge": "JS Special", "title": "Finology Legal JS", "instructor": "Priya Jain", "price": 5000, "rating": 4.9, "lang": "hindi", "lang_label": "Hindi", "link": "https://finology.in", "img": "https://images.unsplash.com/photo-1423592707957-3b212afa6733?auto=format&fit=crop&w=400&q=80"},

    # 💼 MANAGEMENT EXAMS (MBA)
    {"exam": "cat", "badge": "CAT 99 Percentile", "title": "IQuanta CAT Course", "instructor": "Indrajeet Sir", "price": 12000, "rating": 5.0, "lang": "english", "lang_label": "English", "link": "https://iquanta.in", "img": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=400&q=80"},
    {"exam": "cat", "badge": "CAT Quants", "title": "Elites Grid QA Course", "instructor": "Hunny Sir", "price": 7500, "rating": 4.9, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://elitesgrid.com", "img": "https://images.unsplash.com/photo-1596495578065-6e0763fa1178?auto=format&fit=crop&w=400&q=80"},
    {"exam": "xat", "badge": "XAT Decision Making", "title": "Cracku Daily Target", "instructor": "Maruti Sir", "price": 0, "rating": 4.7, "lang": "english", "lang_label": "English", "link": "https://cracku.in", "img": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=400&q=80"},
    {"exam": "xat", "badge": "XAT Prep", "title": "XAT Online Workshop", "instructor": "Hitesh Sir", "price": 3500, "rating": 4.5, "lang": "english", "lang_label": "English", "link": "https://careerlauncher.com", "img": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=400&q=80"},
    {"exam": "snap", "badge": "SNAP 2025", "title": "SNAP Buster Course", "instructor": "MBA Pathshala", "price": 2500, "rating": 4.8, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://mbapathshala.com", "img": "https://images.unsplash.com/photo-1513258496099-48168024aec0?auto=format&fit=crop&w=400&q=80"},
    {"exam": "snap", "badge": "SNAP Special", "title": "SNAP Quick Prep", "instructor": "Hitbullseye", "price": 1200, "rating": 4.2, "lang": "english", "lang_label": "English", "link": "https://hitbullseye.com", "img": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=400&q=80"},
    {"exam": "nmat", "badge": "NMAT Pro", "title": "IMS NMAT Prep", "instructor": "IMS Faculty", "price": 4500, "rating": 4.6, "lang": "english", "lang_label": "English", "link": "https://imsindia.com", "img": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=400&q=80"},
    {"exam": "nmat", "badge": "NMAT Prep", "title": "NMAT Strategy Course", "instructor": "C2C Mentors", "price": 0, "rating": 4.5, "lang": "english", "lang_label": "English", "link": "https://c2cmentors.com", "img": "https://images.unsplash.com/photo-1515378960530-7c0da6231fb1?auto=format&fit=crop&w=400&q=80"},

    # 💻 ENGINEERING PG / TECH EXAMS
    {"exam": "gate", "badge": "GATE CS & IT", "title": "Made Easy Next", "instructor": "Made Easy Team", "price": 10000, "rating": 4.9, "lang": "english", "lang_label": "English", "link": "https://madeeasy.in", "img": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=400&q=80"},
    {"exam": "gate", "badge": "GATE Mechanical", "title": "Unacademy Plus", "instructor": "Negi Sir", "price": 8000, "rating": 4.5, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://unacademy.com", "img": "https://images.unsplash.com/photo-1537462715879-360eeb61a0ad?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ese", "badge": "ESE (IES) 2025", "title": "ACE Academy ESE", "instructor": "ACE Team", "price": 15000, "rating": 4.7, "lang": "english", "lang_label": "English", "link": "https://aceenggacademy.com", "img": "https://images.unsplash.com/photo-1513530534585-c7b1394c6d51?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ese", "badge": "ESE Special", "title": "Made Easy GS Batch", "instructor": "JS Gill", "price": 5000, "rating": 4.9, "lang": "hindi", "lang_label": "Hindi", "link": "https://madeeasy.in", "img": "https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=400&q=80"},
    {"exam": "isro", "badge": "ISRO Scientist", "title": "BYJU'S ISRO Course", "instructor": "BYJU'S Team", "price": 2500, "rating": 4.2, "lang": "english", "lang_label": "English", "link": "https://byjusexamprep.com", "img": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?auto=format&fit=crop&w=400&q=80"},
    {"exam": "isro", "badge": "ISRO Prep", "title": "Kreatryx ISRO Batch", "instructor": "Kreatryx", "price": 0, "rating": 4.5, "lang": "english", "lang_label": "English", "link": "https://kreatryx.com", "img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=400&q=80"},
    {"exam": "barc", "badge": "BARC OCES/DGFS", "title": "Gate Academy BARC", "instructor": "Umesh Dhande", "price": 3200, "rating": 4.6, "lang": "hindi", "lang_label": "Hindi", "link": "https://gateacademy.co.in", "img": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&w=400&q=80"},
    {"exam": "barc", "badge": "BARC Prep", "title": "Testbook BARC Series", "instructor": "Testbook", "price": 0, "rating": 4.0, "lang": "english", "lang_label": "English", "link": "https://testbook.com", "img": "https://images.unsplash.com/photo-1621640165181-34442144ba44?auto=format&fit=crop&w=400&q=80"},

    # 🎓 UNIVERSITY ENTRANCE EXAMS
    {"exam": "cuet_ug", "badge": "CUET UG 2025", "title": "CUET Wallah Domain", "instructor": "PW Team", "price": 2500, "rating": 4.8, "lang": "hindi", "lang_label": "Hindi", "link": "https://pw.live", "img": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=400&q=80"},
    {"exam": "cuet_ug", "badge": "CUET Domain", "title": "CUET Adda247 Batch", "instructor": "Adda247 Team", "price": 2000, "rating": 4.2, "lang": "hindi", "lang_label": "Hindi", "link": "https://adda247.com/cuet", "img": "https://images.unsplash.com/photo-1541339907198-e08759df9a73?auto=format&fit=crop&w=400&q=80"},
    {"exam": "cuet_pg", "badge": "CUET PG 2025", "title": "Unacademy CUET PG", "instructor": "Unacademy Team", "price": 4500, "rating": 4.6, "lang": "english", "lang_label": "English", "link": "https://unacademy.com", "img": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=400&q=80"},
    {"exam": "cuet_pg", "badge": "CUET PG Spec", "title": "EduNext CUET PG", "instructor": "EduNext", "price": 1500, "rating": 4.1, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://edunext.in", "img": "https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=400&q=80"},

    # 🪖 DEFENCE EXAMS
    {"exam": "nda", "badge": "NDA Target 2025", "title": "SSB Crack NDA", "instructor": "SSB Expert", "price": 3200, "rating": 4.7, "lang": "english", "lang_label": "English", "link": "https://ssbcrackexams.com", "img": "https://images.unsplash.com/photo-1529686342540-1b43aec0df75?auto=format&fit=crop&w=400&q=80"},
    {"exam": "nda", "badge": "NDA 2025", "title": "Rakshak NDA Batch", "instructor": "PW Defence", "price": 1500, "rating": 4.6, "lang": "hindi", "lang_label": "Hindi", "link": "https://pw.live", "img": "https://images.unsplash.com/photo-1526662092594-e98c1e356d6a?auto=format&fit=crop&w=400&q=80"},
    {"exam": "cds", "badge": "CDS I & II 2025", "title": "CDS Master Course", "instructor": "StudyIQ", "price": 4500, "rating": 4.8, "lang": "english", "lang_label": "English", "link": "https://studyiq.com", "img": "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=400&q=80"},
    {"exam": "cds", "badge": "CDS Special", "title": "Exampur CDS Batch", "instructor": "Exampur", "price": 999, "rating": 4.3, "lang": "hindi", "lang_label": "Hindi", "link": "https://exampur.com", "img": "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&w=400&q=80"},
    {"exam": "afcat", "badge": "AFCAT 2025", "title": "AFCAT Flying Batch", "instructor": "Testbook Team", "price": 899, "rating": 4.4, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://testbook.com", "img": "https://images.unsplash.com/photo-1568229915220-f7cbb7ff2cf2?auto=format&fit=crop&w=400&q=80"},
    {"exam": "afcat", "badge": "AFCAT Special", "title": "Defence Adda AFCAT", "instructor": "Adda247", "price": 1200, "rating": 4.2, "lang": "english", "lang_label": "English", "link": "https://adda247.com", "img": "https://images.unsplash.com/photo-1512412023212-f05456b15090?auto=format&fit=crop&w=400&q=80"},
    {"exam": "capf", "badge": "CAPF AC 2025", "title": "CAPF Paper I & II", "instructor": "Abhijit Sir", "price": 5500, "rating": 4.7, "lang": "english", "lang_label": "English", "link": "https://byjusexamprep.com", "img": "https://images.unsplash.com/photo-1531206715517-5c0ba140b2b8?auto=format&fit=crop&w=400&q=80"},
    {"exam": "capf", "badge": "CAPF Spec", "title": "Civilsdaily CAPF", "instructor": "Sajal Sir", "price": 0, "rating": 4.9, "lang": "english", "lang_label": "English", "link": "https://civilsdaily.com", "img": "https://images.unsplash.com/photo-1427501741910-09c3943394ee?auto=format&fit=crop&w=400&q=80"},

    # 👨‍🏫 TEACHING EXAMS
    {"exam": "ctet", "badge": "CTET Master", "title": "Let's Learn CDP Master", "instructor": "Himanshi Singh", "price": 0, "rating": 4.9, "lang": "hindi", "lang_label": "Hindi", "link": "https://youtube.com/letslearn", "img": "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ctet", "badge": "CTET Selection", "title": "Target CTET 2025", "instructor": "Vidyakul Team", "price": 599, "rating": 4.1, "lang": "hindi", "lang_label": "Hindi", "link": "https://vidyakul.com", "img": "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ugc_net", "badge": "UGC NET Paper 1", "title": "Byju's Exam Prep", "instructor": "Byju's Team", "price": 5500, "rating": 4.1, "lang": "bilingual", "lang_label": "Bilingual", "link": "https://byjusexamprep.com", "img": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&w=400&q=80"},
    {"exam": "ugc_net", "badge": "UGC NET Spec", "title": "Arpita Karwa NET", "instructor": "Arpita Karwa", "price": 9500, "rating": 4.8, "lang": "english", "lang_label": "English", "link": "https://arpitakarwa.com", "img": "https://images.unsplash.com/photo-1546410531-bb4caa6b424d?auto=format&fit=crop&w=400&q=80"},
    {"exam": "state_tet", "badge": "State TET 2025", "title": "SuperTET Success", "instructor": "Teachers Adda", "price": 899, "rating": 4.4, "lang": "hindi", "lang_label": "Hindi", "link": "https://adda247.com/tet", "img": "https://images.unsplash.com/photo-1514369118554-e20d93546b30?auto=format&fit=crop&w=400&q=80"},
    {"exam": "state_tet", "badge": "TET Special", "title": "MahaTET Pro Course", "instructor": "Unacademy Team", "price": 0, "rating": 4.0, "lang": "hindi", "lang_label": "Hindi", "link": "https://unacademy.com", "img": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=400&q=80"},
    {"exam": "kvs", "badge": "KVS PRT/TGT/PGT", "title": "KVS Master Class", "instructor": "Himanshi Singh", "price": 1200, "rating": 4.9, "lang": "hindi", "lang_label": "Hindi", "link": "https://youtube.com/letslearn", "img": "https://images.unsplash.com/photo-1491841315574-8848416809c9?auto=format&fit=crop&w=400&q=80"},
    {"exam": "kvs", "badge": "KVS Selection", "title": "Exampur KVS Batch", "instructor": "Vivek Sir", "price": 1500, "rating": 4.4, "lang": "hindi", "lang_label": "Hindi", "link": "https://exampur.com", "img": "https://images.unsplash.com/photo-1510531704581-5b2870972060?auto=format&fit=crop&w=400&q=80"}
]

def get_stars(rating):
    stars = []
    full_stars = int(rating)
    half_star = 1 if rating - full_stars >= 0.3 and rating - full_stars <= 0.7 else 0
    if rating - full_stars > 0.7:
        full_stars += 1
        half_star = 0
    
    for i in range(5):
        if i < full_stars:
            stars.append('fill')
        elif i == full_stars and half_star == 1:
            stars.append('half')
        else:
            stars.append('empty')
    return stars

html_cards = ""
for c in course_data:
    stars = get_stars(c['rating'])
    star_html = ""
    for s in stars:
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
                                    <h3 class="course-h3" style="font-size: 1.3rem;">{c['title']}</h3>
                                    
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
                                        <button class="buy-btn">{"Enroll Now" if c['price'] > 0 else "Start Free"}</button>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </div>
'''
    html_cards += card

# We clear `<div class="row g-4" id="course-container">` first
match = re.search(r'(<div class="row g-4" id="course-container">\s*)(.*?)\s*(</div>\s*</div>\s*</section>)', html, flags=re.DOTALL)
if match:
    new_html = html[:match.start(2)] + html_cards + html[match.end(2):]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("All Courses populated successfully!")
else:
    print("Could not find the end of #course-container")
