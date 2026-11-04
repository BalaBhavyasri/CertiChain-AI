import re

# =========================================
# ORGANIZATIONS
# =========================================

organizations = [

    "Eduskills",
    "AICTE",
    "Google",
    "Microsoft",
    "AWS",
    "Amazon",
    "Cisco",
    "Oracle",
    "Infosys",
    "Coursera",
    "Udemy",
    "NPTEL",
    "Internshala",
    "Salesforce",
    "IBM",
    "Meta",
    "OpenAI"
]

# =========================================
# PROGRAM KEYWORDS
# =========================================

program_keywords = {

    # =====================================
    # INTERNSHIP PROGRAMS (SPECIFIC FIRST)
    # =====================================

    "AI Virtual Internship": [
        "ai virtual internship",
        "artificial intelligence virtual internship",
        "ai internship",
        "artificial intelligence internship"
    ],

    "AI & ML Virtual Internship": [
        "ai & ml virtual internship",
        "ai and ml virtual internship",
        "ai ml virtual internship"
    ],

    "Machine Learning Internship": [
        "machine learning internship",
        "ml internship",
        "machine learning intern"
    ],

    "Deep Learning Internship": [
        "deep learning internship",
        "deep learning intern"
    ],

    "Generative AI Internship": [
        "generative ai internship",
        "generative ai intern",
        "generative artificial intelligence internship"
    ],

    "NLP Internship": [
        "nlp internship",
        "natural language processing internship",
        "text processing internship"
    ],

    "Computer Vision Internship": [
        "computer vision internship",
        "vision internship",
        "image processing internship"
    ],

    "Data Science Internship": [
        "data science internship",
        "data science intern"
    ],

    "Data Analyst Internship": [
        "data analyst internship",
        "data analyst intern"
    ],

    "Business Analytics Internship": [
        "business analytics internship",
        "business analytics intern"
    ],

    "Big Data Internship": [
        "big data internship",
        "big data intern",
        "hadoop internship",
        "spark internship"
    ],

    "Frontend Development Internship": [
        "frontend development internship",
        "frontend internship",
        "ui ux internship"
    ],

    "Backend Development Internship": [
        "backend development internship",
        "backend internship",
        "server side internship"
    ],

    "Full Stack Development Internship": [
        "full stack development internship",
        "full stack internship",
        "fullstack internship"
    ],

    "MERN Stack Internship": [
        "mern stack internship",
        "mern internship"
    ],

    "MEAN Stack Internship": [
        "mean stack internship",
        "mean internship"
    ],

    "React Internship": [
        "react internship",
        "reactjs internship",
        "react developer internship"
    ],

    "Angular Internship": [
        "angular internship",
        "angularjs internship"
    ],

    "Node.js Internship": [
        "node.js internship",
        "nodejs internship",
        "node internship"
    ],

    "Django Internship": [
        "django internship"
    ],

    "Flask Internship": [
        "flask internship"
    ],

    "PHP Development Internship": [
        "php development internship",
        "php internship"
    ],

    "Java Programming Internship": [
        "java programming internship",
        "java internship"
    ],

    "Java Full Stack Internship": [
        "java full stack internship",
        "java fullstack internship",
        "java full-stack internship"
    ],

    "Spring Boot Internship": [
        "spring boot internship",
        "springboot internship"
    ],

    "JDBC Internship": [
        "jdbc internship",
        "jdbc intern"
    ],

    "Hibernate Internship": [
        "hibernate internship"
    ],

    "Python Programming Internship": [
        "python programming internship",
        "python internship"
    ],

    "Python Full Stack Internship": [
        "python full stack internship",
        "python fullstack internship",
        "python full-stack internship"
    ],

    "Cloud Computing Internship": [
        "cloud computing internship",
        "cloud internship"
    ],

    "AWS Internship": [
        "aws internship",
        "amazon web services internship"
    ],

    "Azure Internship": [
        "azure internship"
    ],

    "Google Cloud Internship": [
        "google cloud internship",
        "gcp internship"
    ],

    "DevOps Internship": [
        "devops internship",
        "dev ops internship"
    ],

    "Docker Internship": [
        "docker internship"
    ],

    "Kubernetes Internship": [
        "kubernetes internship",
        "k8s internship"
    ],

    "Cyber Security Internship": [
        "cyber security internship",
        "cybersecurity internship"
    ],

    "Ethical Hacking Internship": [
        "ethical hacking internship",
        "penetration testing internship"
    ],

    "SOC Analyst Internship": [
        "soc analyst internship",
        "security operations center internship"
    ],

    "Information Security Internship": [
        "information security internship",
        "security compliance internship"
    ],

    "Network Security Internship": [
        "network security internship",
        "firewalls internship"
    ],

    "Blockchain Internship": [
        "blockchain internship",
        "blockchain intern"
    ],

    "Solidity Internship": [
        "solidity internship"
    ],

    "Ethereum Internship": [
        "ethereum internship"
    ],

    "Web3 Internship": [
        "web3 internship",
        "web 3 internship"
    ],

    "Smart Contract Internship": [
        "smart contract internship",
        "smart contracts internship"
    ],

    "Android Development Internship": [
        "android development internship",
        "android internship"
    ],

    "Kotlin Internship": [
        "kotlin internship"
    ],

    "Flutter Internship": [
        "flutter internship",
        "dart internship"
    ],

    "React Native Internship": [
        "react native internship"
    ],

    "Firebase Internship": [
        "firebase internship"
    ],

    "AR Internship": [
        "ar internship",
        "augmented reality internship"
    ],

    "VR Internship": [
        "vr internship",
        "virtual reality internship"
    ],

    "AR/VR Internship": [
        "ar/vr internship",
        "ar vr internship",
        "xr internship"
    ],

    "Unity Internship": [
        "unity internship"
    ],

    "Unreal Engine Internship": [
        "unreal engine internship",
        "unreal internship"
    ],

    "Game Development Internship": [
        "game development internship"
    ],

    "Metaverse Internship": [
        "metaverse internship"
    ],

    "IoT Internship": [
        "iot internship",
        "internet of things internship"
    ],

    "Embedded Systems Internship": [
        "embedded systems internship",
        "embedded internship"
    ],

    "Robotics Internship": [
        "robotics internship"
    ],

    "Edge AI Internship": [
        "edge ai internship",
        "tinyml internship"
    ],

    "Networking Internship": [
        "networking internship",
        "routing internship"
    ],

    "CCNA Internship": [
        "ccna internship",
        "cisco certification internship"
    ],

    "Graphic Design Internship": [
        "graphic design internship",
        "photoshop internship"
    ],

    "UI/UX Internship": [
        "ui/ux internship",
        "ux internship",
        "ui internship"
    ],

    "Motion Graphics Internship": [
        "motion graphics internship",
        "animation internship"
    ],

    "Canva Design Internship": [
        "canva design internship",
        "canva internship"
    ],

    "Software Testing Internship": [
        "software testing internship",
        "qa internship"
    ],

    "Automation Testing Internship": [
        "automation testing internship"
    ],

    "Selenium Internship": [
        "selenium internship"
    ],

    "Agile Internship": [
        "agile internship",
        "scrum internship",
        "sprint planning internship"
    ],

    "Software Engineering Internship": [
        "software engineering internship",
        "sdlc internship"
    ],

    "Digital Marketing Internship": [
        "digital marketing internship",
        "seo internship",
        "sem internship"
    ],

    "Product Management Internship": [
        "product management internship"
    ],

    "ERP Internship": [
        "erp internship",
        "sap internship"
    ],

    "CRM Internship": [
        "crm internship",
        "customer relationship management internship"
    ],

    "FinTech Internship": [
        "fintech internship",
        "financial technology internship"
    ],

    # =====================================
    # GENERAL PROGRAMS
    # =====================================

    "Java Full Stack": [
        "java full stack",
        "full stack java",
        "java fullstack",
        "java full-stack",
        "java stack",
        "java full stack development",
        "full stack java development",
        "java web development",
        "java application development",
        "java enterprise development"
    ],

    "Python Full Stack": [
        "python full stack",
        "full stack python",
        "python fullstack",
        "python full-stack",
        "python stack"
    ],

    "Frontend Development": [
        "frontend",
        "front end",
        "frontend development",
        "front-end",
        "front-end development",
        "ui ux",
        "ui/ux",
        "web design"
    ],

    "Backend Development": [
        "backend",
        "back end",
        "backend development",
        "server side",
        "server-side",
        "api development"
    ],

    "Full Stack Development": [
        "full stack",
        "fullstack",
        "web development",
        "web dev",
        "mern stack",
        "mean stack",
        "full stack development",
        "full-stack development"
    ],

    "AI & ML": [
        "ai ml",
        "artificial intelligence",
        "machine learning",
        "ai/ml",
        "artificial intelligence and machine learning",
        "ai and ml",
        "ml ai",
        "machine learning ai",
        "deep learning",
        "neural networks",
        "computer vision",
        "natural language processing",
        "nlp",
        "computer vision",
        "cv",
        "tensorflow",
        "pytorch",
        "scikit-learn",
        "pandas",
        "numpy"
    ],

    "Data Science": [
        "data science",
        "data scientist",
        "data analysis",
        "data analytics",
        "big data",
        "business intelligence",
        "bi",
        "data visualization",
        "statistics",
        "predictive analytics"
    ],

    "AI Virtual Internship": [
        "ai virtual internship",
        "artificial intelligence virtual internship",
        "ai internship",
        "artificial intelligence internship"
    ],

    "AI & ML Virtual Internship": [
        "ai & ml virtual internship",
        "ai and ml virtual internship",
        "ai ml virtual internship"
    ],

    "Machine Learning Internship": [
        "machine learning internship",
        "ml internship",
        "machine learning intern"
    ],

    "Deep Learning Internship": [
        "deep learning internship",
        "deep learning intern"
    ],

    "Generative AI Internship": [
        "generative ai internship",
        "generative ai intern",
        "generative artificial intelligence internship"
    ],

    "NLP Internship": [
        "nlp internship",
        "natural language processing internship",
        "text processing internship"
    ],

    "Computer Vision Internship": [
        "computer vision internship",
        "vision internship",
        "image processing internship"
    ],

    "Data Science Internship": [
        "data science internship",
        "data science intern"
    ],

    "Data Analyst Internship": [
        "data analyst internship",
        "data analyst intern"
    ],

    "Business Analytics Internship": [
        "business analytics internship",
        "business analytics intern"
    ],

    "Big Data Internship": [
        "big data internship",
        "big data intern",
        "hadoop internship",
        "spark internship"
    ],

    "Frontend Development Internship": [
        "frontend development internship",
        "frontend internship",
        "ui ux internship"
    ],

    "Backend Development Internship": [
        "backend development internship",
        "backend internship",
        "server side internship"
    ],

    "Full Stack Development Internship": [
        "full stack development internship",
        "full stack internship",
        "fullstack internship"
    ],

    "MERN Stack Internship": [
        "mern stack internship",
        "mern internship"
    ],

    "MEAN Stack Internship": [
        "mean stack internship",
        "mean internship"
    ],

    "React Internship": [
        "react internship",
        "reactjs internship",
        "react developer internship"
    ],

    "Angular Internship": [
        "angular internship",
        "angularjs internship"
    ],

    "Node.js Internship": [
        "node.js internship",
        "nodejs internship",
        "node internship"
    ],

    "Django Internship": [
        "django internship"
    ],

    "Flask Internship": [
        "flask internship"
    ],

    "PHP Development Internship": [
        "php development internship",
        "php internship"
    ],

    "Java Programming Internship": [
        "java programming internship",
        "java internship"
    ],

    "Java Full Stack Internship": [
        "java full stack internship",
        "java fullstack internship",
        "java full-stack internship"
    ],

    "Spring Boot Internship": [
        "spring boot internship",
        "springboot internship"
    ],

    "JDBC Internship": [
        "jdbc internship",
        "jdbc intern"
    ],

    "Hibernate Internship": [
        "hibernate internship"
    ],

    "Python Programming Internship": [
        "python programming internship",
        "python internship"
    ],

    "Python Full Stack Internship": [
        "python full stack internship",
        "python fullstack internship",
        "python full-stack internship"
    ],

    "Cloud Computing Internship": [
        "cloud computing internship",
        "cloud internship"
    ],

    "AWS Internship": [
        "aws internship",
        "amazon web services internship"
    ],

    "Azure Internship": [
        "azure internship"
    ],

    "Google Cloud Internship": [
        "google cloud internship",
        "gcp internship"
    ],

    "DevOps Internship": [
        "devops internship",
        "dev ops internship"
    ],

    "Docker Internship": [
        "docker internship"
    ],

    "Kubernetes Internship": [
        "kubernetes internship",
        "k8s internship"
    ],

    "Cyber Security Internship": [
        "cyber security internship",
        "cybersecurity internship"
    ],

    "Ethical Hacking Internship": [
        "ethical hacking internship",
        "penetration testing internship"
    ],

    "SOC Analyst Internship": [
        "soc analyst internship",
        "security operations center internship"
    ],

    "Information Security Internship": [
        "information security internship",
        "security compliance internship"
    ],

    "Network Security Internship": [
        "network security internship",
        "firewalls internship"
    ],

    "Blockchain Internship": [
        "blockchain internship",
        "blockchain intern"
    ],

    "Solidity Internship": [
        "solidity internship"
    ],

    "Ethereum Internship": [
        "ethereum internship"
    ],

    "Web3 Internship": [
        "web3 internship",
        "web 3 internship"
    ],

    "Smart Contract Internship": [
        "smart contract internship",
        "smart contracts internship"
    ],

    "Android Development Internship": [
        "android development internship",
        "android internship"
    ],

    "Kotlin Internship": [
        "kotlin internship"
    ],

    "Flutter Internship": [
        "flutter internship",
        "dart internship"
    ],

    "React Native Internship": [
        "react native internship"
    ],

    "Firebase Internship": [
        "firebase internship"
    ],

    "AR Internship": [
        "ar internship",
        "augmented reality internship"
    ],

    "VR Internship": [
        "vr internship",
        "virtual reality internship"
    ],

    "AR/VR Internship": [
        "ar/vr internship",
        "ar vr internship",
        "xr internship"
    ],

    "Unity Internship": [
        "unity internship"
    ],

    "Unreal Engine Internship": [
        "unreal engine internship",
        "unreal internship"
    ],

    "Game Development Internship": [
        "game development internship"
    ],

    "Metaverse Internship": [
        "metaverse internship"
    ],

    "IoT Internship": [
        "iot internship",
        "internet of things internship"
    ],

    "Embedded Systems Internship": [
        "embedded systems internship",
        "embedded internship"
    ],

    "Robotics Internship": [
        "robotics internship"
    ],

    "Edge AI Internship": [
        "edge ai internship",
        "tinyml internship"
    ],

    "Networking Internship": [
        "networking internship",
        "routing internship"
    ],

    "CCNA Internship": [
        "ccna internship",
        "cisco certification internship"
    ],

    "Graphic Design Internship": [
        "graphic design internship",
        "photoshop internship"
    ],

    "UI/UX Internship": [
        "ui/ux internship",
        "ux internship",
        "ui internship"
    ],

    "Motion Graphics Internship": [
        "motion graphics internship",
        "animation internship"
    ],

    "Canva Design Internship": [
        "canva design internship",
        "canva internship"
    ],

    "Software Testing Internship": [
        "software testing internship",
        "qa internship"
    ],

    "Automation Testing Internship": [
        "automation testing internship"
    ],

    "Selenium Internship": [
        "selenium internship"
    ],

    "Agile Internship": [
        "agile internship",
        "scrum internship",
        "sprint planning internship"
    ],

    "Software Engineering Internship": [
        "software engineering internship",
        "sdlc internship"
    ],

    "Digital Marketing Internship": [
        "digital marketing internship",
        "seo internship",
        "sem internship"
    ],

    "Product Management Internship": [
        "product management internship"
    ],

    "ERP Internship": [
        "erp internship",
        "sap internship"
    ],

    "CRM Internship": [
        "crm internship",
        "customer relationship management internship"
    ],

    "FinTech Internship": [
        "fintech internship",
        "financial technology internship"
    ],

    "Data Science": [
        "data science",
        "data scientist",
        "data analysis",
        "data analytics",
        "big data",
        "business intelligence",
        "bi",
        "data visualization",
        "statistics",
        "predictive analytics"
    ],

    "Blockchain": [
        "blockchain",
        "solidity",
        "ethereum",
        "web3",
        "smart contracts",
        "cryptocurrency",
        "bitcoin",
        "defi",
        "decentralized finance"
    ],

    "Cloud Computing": [
        "cloud",
        "aws",
        "azure",
        "google cloud",
        "gcp",
        "cloud computing",
        "cloud architecture",
        "devops",
        "docker",
        "kubernetes",
        "microservices"
    ],

    "Cyber Security": [
        "cyber security",
        "ethical hacking",
        "penetration testing",
        "network security",
        "information security",
        "cybersecurity",
        "hacking",
        "security",
        "vulnerability assessment"
    ],

    "AR/VR": [
        "ar vr",
        "augmented reality",
        "virtual reality",
        "mixed reality",
        "mr",
        "unity",
        "unreal engine",
        "3d modeling",
        "game development"
    ],

    "Android Development": [
        "android",
        "kotlin",
        "mobile development",
        "android studio",
        "java android",
        "firebase"
    ],

    "iOS Development": [
        "ios",
        "swift",
        "objective-c",
        "xcode",
        "apple development"
    ],

    "DevOps": [
        "devops",
        "ci/cd",
        "continuous integration",
        "continuous deployment",
        "jenkins",
        "docker",
        "kubernetes",
        "infrastructure as code"
    ],

    "Database Administration": [
        "database",
        "dba",
        "sql",
        "mysql",
        "postgresql",
        "mongodb",
        "oracle",
        "database administration"
    ]
}

# =========================================
# CLEAN TEXT
# =========================================

def normalize_text(text):

    text = text.replace("\n", " ")

    text = re.sub(
        r'[^a-zA-Z0-9/ ]',
        ' ',
        text
    )

    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text.strip()

# =========================================
# EXTRACT INFO
# =========================================

def extract_certificate_info(text):

    clean_text = normalize_text(text)

    lower_text = clean_text.lower()

    info = {

        "organization": "Not Detected",

        "name": "Not Detected",

        "program": "Not Detected",

        "date": "Not Detected"
    }

    # =====================================
    # ORGANIZATION DETECTION
    # =====================================

    for org in organizations:

        if org.lower() in lower_text:

            info["organization"] = org

            break

    # =====================================
    # PROGRAM DETECTION
    # =====================================

    detected_programs = []

    for program, keywords in program_keywords.items():

        for keyword in keywords:

            if keyword.lower() in lower_text:

                detected_programs.append(program)

                break

    # Priority handling - More specific programs first

    if "Java Full Stack" in detected_programs:
        info["program"] = "Java Full Stack"

    elif "Python Full Stack" in detected_programs:
        info["program"] = "Python Full Stack"

    elif "AI & ML" in detected_programs:
        info["program"] = "AI & ML"

    elif "Data Science" in detected_programs:
        info["program"] = "Data Science"

    elif "Full Stack Development" in detected_programs:
        info["program"] = "Full Stack Development"

    elif "Frontend Development" in detected_programs:
        info["program"] = "Frontend Development"

    elif "Backend Development" in detected_programs:
        info["program"] = "Backend Development"

    elif "Blockchain" in detected_programs:
        info["program"] = "Blockchain"

    elif "Cloud Computing" in detected_programs:
        info["program"] = "Cloud Computing"

    elif "Cyber Security" in detected_programs:
        info["program"] = "Cyber Security"

    elif "Android Development" in detected_programs:
        info["program"] = "Android Development"

    elif "AR/VR" in detected_programs:
        info["program"] = "AR/VR"

    elif "DevOps" in detected_programs:
        info["program"] = "DevOps"

    elif "iOS Development" in detected_programs:
        info["program"] = "iOS Development"

    elif "Database Administration" in detected_programs:
        info["program"] = "Database Administration"

    elif len(detected_programs) > 0:
        info["program"] = detected_programs[0]

    # =====================================
    # CROSS-PROGRAM INFERENCE
    # =====================================

    # If Java and Full Stack terms detected separately
    if info["program"] == "Not Detected":

        if ("java" in lower_text and
            ("full stack" in lower_text or "fullstack" in lower_text or
             "web development" in lower_text or "application development" in lower_text)):

            info["program"] = "Java Full Stack"

        elif ("python" in lower_text and
              ("full stack" in lower_text or "fullstack" in lower_text or
               "web development" in lower_text)):

            info["program"] = "Python Full Stack"

    # =====================================
    # PROGRAM INFERENCE FROM CERTIFICATE CONTEXT
    # =====================================

    if info["program"] == "Not Detected":

        if "full stack" in lower_text or "fullstack" in lower_text or "mern stack" in lower_text or "mean stack" in lower_text:
            info["program"] = "Full Stack Development"

        elif "web development" in lower_text or "web dev" in lower_text:
            info["program"] = "Full Stack Development"

        elif "frontend" in lower_text and "backend" in lower_text:
            info["program"] = "Full Stack Development"

        elif "frontend" in lower_text:
            info["program"] = "Frontend Development"

        elif "backend" in lower_text or "server side" in lower_text or "api development" in lower_text:
            info["program"] = "Backend Development"

    # =====================================
    # PROGRAM INFERENCE FROM TECH TERMS
    # =====================================

    if info["program"] == "Not Detected":

        if any(term in lower_text for term in ["django", "flask", "fastapi", "rest api", "react", "angular", "vue", "node.js", "nodejs"]):
            if "python" in lower_text or "django" in lower_text or "flask" in lower_text:
                info["program"] = "Python Full Stack"
            elif "java" in lower_text or "spring" in lower_text or "spring boot" in lower_text:
                info["program"] = "Java Full Stack"
            else:
                info["program"] = "Full Stack Development"

        elif any(term in lower_text for term in ["machine learning", "artificial intelligence", "ai", "data science"]):
            info["program"] = "AI & ML"

        elif any(term in lower_text for term in ["blockchain", "solidity", "ethereum", "web3"]):
            info["program"] = "Blockchain"

        elif any(term in lower_text for term in ["cloud", "aws", "azure", "gcp"]):
            info["program"] = "Cloud Computing"

        elif any(term in lower_text for term in ["cyber security", "ethical hacking"]):
            info["program"] = "Cyber Security"

        elif any(term in lower_text for term in ["augmented reality", "virtual reality", "ar vr"]):
            info["program"] = "AR/VR"

        elif any(term in lower_text for term in ["android", "kotlin"]):
            info["program"] = "Android Development"

    # =====================================
    # DATE DETECTION
    # =====================================

    date_patterns = [

        r'\b\d{2}/\d{2}/\d{4}\b',

        r'\b\d{2}-\d{2}-\d{4}\b',

        r'\b\d{4}\b'
    ]

    for pattern in date_patterns:

        match = re.search(pattern, clean_text)

        if match:

            info["date"] = match.group()

            break

    # =====================================
    # NAME DETECTION
    # =====================================

    lines = text.split('\n')

    ignore_words = [

        "certificate",
        "completion",
        "internship",
        "program",
        "course",
        "training",
        "issued",
        "verify",
        "learning",
        "student",
        "award",
        "organization",
        "date",
        "skills"
    ]

    possible_names = []

    for line in lines:

        line = line.strip()

        if len(line) < 3:
            continue

        lower_line = line.lower()

        # Ignore lines with numbers
        if any(char.isdigit() for char in line):
            continue

        # Ignore unwanted words
        if any(word in lower_line for word in ignore_words):
            continue

        words = line.split()

        # Candidate names usually 2-4 words
        if 2 <= len(words) <= 4:

            # Mostly alphabets
            if line.replace(" ", "").isalpha():

                possible_names.append(
                    line.title()
                )

    if len(possible_names) > 0:

        # Choose longest likely name
        info["name"] = max(
            possible_names,
            key=len
        )

    return info
