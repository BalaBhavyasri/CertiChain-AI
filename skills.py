import re
from difflib import SequenceMatcher

# =========================================
# DOMAIN SKILLS DATABASE
# =========================================

skill_database = {

    # =====================================
    # PROGRAMMING LANGUAGES
    # =====================================

    "Python": [
        "python",
        "python3",
        "python 3",
        "py",
        "python language",
        "python programming"
    ],

    "Java": [
        "java",
        "java language",
        "java programming",
        "j2ee",
        "j2se",
        "enterprise java"
    ],

    "C": [
        "c",
        " c "
    ],

    "C++": [
        "c++",
        "c plus plus"
    ],

    "C#": [
        "c#",
        "c sharp"
    ],

    "JavaScript": [
        "javascript",
        "js",
        "ecmascript",
        "java script",
        "javascript programming"
    ],

    # =====================================
    # WEB DEVELOPMENT
    # =====================================

    "HTML": [
        "html"
    ],

    "CSS": [
        "css"
    ],

    "React": [
        "react",
        "reactjs",
        "react.js",
        "react js",
        "react library",
        "react native"
    ],

    "Angular": [
        "angular",
        "angularjs",
        "angular.js"
    ],

    "Vue.js": [
        "vue",
        "vuejs",
        "vue.js"
    ],

    "TypeScript": [
        "typescript",
        "type script",
        "ts"
    ],

    "Node.js": [
        "nodejs",
        "node js",
        "node.js",
        "node",
        "node.js framework",
        "nodejs framework",
        "express",
        "express js",
        "express.js"
    ],

    "Django": [
        "django",
        "django framework"
    ],

    "Flask": [
        "flask",
        "flask framework"
    ],

    "FastAPI": [
        "fastapi",
        "fast api"
    ],

    "Spring Boot": [
        "spring boot",
        "springboot"
    ],

    "Spring": [
        "spring framework",
        "spring boot",
        "spring"
    ],

    "Bootstrap": [
        "bootstrap",
        "bootstrap css"
    ],

    "Tailwind CSS": [
        "tailwind",
        "tailwind css"
    ],

    "Sass": [
        "sass",
        "scss"
    ],

    "jQuery": [
        "jquery"
    ],

    "GraphQL": [
        "graphql"
    ],

    "Frontend": [
        "frontend",
        "front end",
        "frontend development",
        "web design",
        "ui development",
        "ui/ux",
        "user interface"
    ],

    "REST API": [
        "rest api",
        "restful",
        "rest api development",
        "restful api",
        "api development",
        "api integration"
    ],

    "Backend": [
        "backend",
        "back end",
        "backend development",
        "server side",
        "server-side",
        "server side development"
    ],

    "Full Stack": [
        "full stack",
        "fullstack",
        "full stack development",
        "java full stack",
        "python full stack",
        "mern stack",
        "mean stack"
    ],

    # =====================================
    # AI / ML
    # =====================================

    "Machine Learning": [
        "machine learning",
        "machinelearning",
        "ml",
        "machine learn",
        "supervised learning",
        "unsupervised learning",
        "learning algorithms"
    ],

    "Deep Learning": [
        "deep learning",
        "deeplearning",
        "deep learn",
        "neural networks",
        "neural network",
        "cnn",
        "convolutional neural network",
        "rnn",
        "lstm",
        "recurrent"
    ],

    "Artificial Intelligence": [
        "artificial intelligence",
        "artificialintelligence",
        "ai",
        "intelligent systems"
    ],

    "AI & ML": [
        "ai ml",
        "aiml",
        "ai/ml",
        "artificial intelligence and machine learning",
        "artificial intelligence machine learning"
    ],

    "Data Science": [
        "data science",
        "datascience",
        "data analysis",
        "data scientist",
        "analytics"
    ],

    "TensorFlow": [
        "tensorflow",
        "tensor flow"
    ],

    "PyTorch": [
        "pytorch",
        "py torch"
    ],

    "Keras": [
        "keras"
    ],

    "Prompt Engineering": [
        "prompt engineering",
        "prompt design"
    ],

    "LLM": [
        "llm",
        "large language model",
        "large language models"
    ],

    "Transformers": [
        "transformers",
        "transformer models"
    ],

    "NLP": [
        "nlp",
        "natural language processing",
        "text processing",
        "sentiment analysis"
    ],

    "Text Processing": [
        "text processing",
        "text analytics"
    ],

    "Sentiment Analysis": [
        "sentiment analysis"
    ],

    "Feature Engineering": [
        "feature engineering"
    ],

    "Model Training": [
        "model training"
    ],

    "GPU Computing": [
        "gpu computing",
        "gpu"
    ],

    "Hadoop": [
        "hadoop"
    ],

    "Spark": [
        "spark",
        "apache spark"
    ],

    "Big Data": [
        "big data",
        "data engineering"
    ],

    "Power BI": [
        "power bi"
    ],

    "Tableau": [
        "tableau"
    ],

    "Excel": [
        "excel"
    ],

    "Business Intelligence": [
        "business intelligence",
        "bi"
    ],

    "Docker": [
        "docker",
        "containers"
    ],

    "Kubernetes": [
        "kubernetes",
        "k8s"
    ],

    "CI/CD": [
        "ci/cd",
        "continuous integration",
        "continuous deployment"
    ],

    "Linux": [
        "linux",
        "ubuntu",
        "centos",
        "redhat"
    ],

    "Jenkins": [
        "jenkins",
        "jenkins ci"
    ],

    "Firebase": [
        "firebase",
        "realtime db",
        "firebase authentication"
    ],

    "Dart": [
        "dart"
    ],

    "Flutter": [
        "flutter"
    ],

    "React Native": [
        "react native"
    ],

    "Unity": [
        "unity",
        "unity3d"
    ],

    "Unreal Engine": [
        "unreal engine",
        "unreal"
    ],

    "3D Modeling": [
        "3d modeling",
        "blender",
        "maya"
    ],

    "Photoshop": [
        "photoshop"
    ],

    "Illustrator": [
        "illustrator"
    ],

    "Figma": [
        "figma"
    ],

    "After Effects": [
        "after effects"
    ],

    "Canva": [
        "canva"
    ],

    "Selenium": [
        "selenium"
    ],

    "Agile": [
        "agile",
        "scrum",
        "sprint planning"
    ],

    "SAP": [
        "sap"
    ],

    "ERP": [
        "erp"
    ],

    "CRM": [
        "crm"
    ],

    "IoT": [
        "iot",
        "internet of things"
    ],

    "ESP32": [
        "esp32"
    ],

    "Arduino": [
        "arduino"
    ],

    "Microcontrollers": [
        "microcontrollers",
        "microcontroller"
    ],

    "Smart Contracts": [
        "smart contracts",
        "smart contract"
    ],

    "Web3": [
        "web3",
        "meta mask",
        "metamask"
    ],

    "Blockchain": [
        "blockchain",
        "solidity",
        "ethereum",
        "web3"
    ],

    "OpenCV": [
        "opencv",
        "open cv"
    ],

    "Pandas": [
        "pandas",
        "pd"
    ],

    "NumPy": [
        "numpy",
        "np"
    ],

    "Scikit-Learn": [
        "scikit-learn",
        "scikit learn",
        "sklearn"
    ],

    "Matplotlib": [
        "matplotlib"
    ],

    "Seaborn": [
        "seaborn"
    ],

    # =====================================
    # DATABASE
    # =====================================

    "SQL": [
        "sql",
        "mysql",
        "postgresql",
        "database",
        "structured query language",
        "relational database"
    ],

    "MySQL": [
        "mysql",
        "my sql"
    ],

    "PostgreSQL": [
        "postgresql",
        "postgres"
    ],

    "MongoDB": [
        "mongodb",
        "mongo db",
        "nosql"
    ],

    # =====================================
    # BLOCKCHAIN
    # =====================================

    "Blockchain": [
        "blockchain",
        "distributed ledger"
    ],

    "Solidity": [
        "solidity"
    ],

    "Ethereum": [
        "ethereum",
        "ethereum development"
    ],

    "Web3": [
        "web3",
        "web 3",
        "decentralized"
    ],

    "Smart Contracts": [
        "smart contracts",
        "smart contract"
    ],

    # =====================================
    # CLOUD
    # =====================================

    "AWS": [
        "aws",
        "amazon web services",
        "ec2",
        "s3"
    ],

    "Azure": [
        "azure",
        "microsoft azure"
    ],

    "GCP": [
        "gcp",
        "google cloud",
        "cloud platform"
    ],

    "Docker": [
        "docker",
        "containerization"
    ],

    "Kubernetes": [
        "kubernetes",
        "k8s"
    ],

    "DevOps": [
        "devops",
        "dev ops",
        "ci/cd",
        "continuous integration"
    ],

    "Jenkins": [
        "jenkins",
        "jenkins ci"
    ],

    "Cloud Computing": [
        "cloud computing",
        "cloud",
        "aws",
        "azure",
        "gcp",
        "google cloud",
        "amazon web services"
    ],

    "MongoDB": [
        "mongodb",
        "mongo db",
        "nosql"
    ],

    # =====================================
    # CYBER SECURITY
    # =====================================

    "Cyber Security": [
        "cyber security",
        "cybersecurity"
    ],

    "Ethical Hacking": [
        "ethical hacking"
    ],

    "Network Security": [
        "network security"
    ],

    "Linux": [
        "linux",
        "ubuntu",
        "centos",
        "redhat"
    ],

    "Bash": [
        "bash",
        "shell scripting",
        "bash scripting"
    ],

    # =====================================
    # MOBILE DEVELOPMENT
    # =====================================

    "Android": [
        "android"
    ],

    "Kotlin": [
        "kotlin"
    ],

    "Firebase": [
        "firebase"
    ],

    # =====================================
    # AR / VR
    # =====================================

    "AR/VR": [
        "ar vr",
        "augmented reality",
        "virtual reality"
    ],

    "Unity": [
        "unity",
        "unity3d",
        "unity engine"
    ],

    "Unreal Engine": [
        "unreal engine",
        "unreal",
        "ue4",
        "ue5"
    ],

    "3D Modeling": [
        "3d modeling",
        "3d model",
        "blender",
        "maya",
        "3ds max"
    ],

    "Game Development": [
        "game development",
        "game dev",
        "gaming"
    ]
}

# =========================================
# FUZZY MATCHING
# =========================================

def fuzzy_match(text, keyword, threshold=0.75):
    """
    Fuzzy matching for skill detection with threshold
    """
    ratio = SequenceMatcher(None, text, keyword).ratio()
    return ratio >= threshold

# =========================================
# EXTRACT SKILLS
# =========================================

def extract_skills(text, program=None):

    detected_skills = []

    # =====================================
    # CLEAN TEXT
    # =====================================

    text = text.lower()

    cleaned_text = re.sub(

        r'[^a-zA-Z0-9+#/. ]',

        ' ',

        text
    )

    cleaned_text = re.sub(

        r'\s+',

        ' ',

        cleaned_text
    )

    cleaned_text = f" {cleaned_text} "

    # =====================================
    # MATCH SKILLS - EXACT MATCH FIRST
    # =====================================

    for skill, keywords in skill_database.items():

        for keyword in keywords:

            keyword = keyword.lower()

            # =================================
            # STRICT MATCH FOR SHORT WORDS
            # =================================

            if len(keyword) <= 3:

                pattern = (
                    r'\b' +
                    re.escape(keyword) +
                    r'\b'
                )

                if re.search(

                    pattern,

                    cleaned_text

                ):

                    detected_skills.append(skill)

                    break

            # =================================
            # NORMAL MATCH FOR LONG WORDS
            # =================================

            else:

                if keyword in cleaned_text:

                    detected_skills.append(skill)

                    break
    
    # =====================================
    # FUZZY MATCHING FOR MISSED SKILLS
    # =====================================
    
    words = cleaned_text.split()
    
    for skill, keywords in skill_database.items():
        
        if skill in detected_skills:
            continue
        
        for keyword in keywords:
            
            keyword = keyword.lower()
            
            for word in words:
                
                if len(word) > 3 and fuzzy_match(word, keyword, 0.8):
                    
                    detected_skills.append(skill)
                    break
            
            if skill in detected_skills:
                break

    # =====================================
    # SMART LOGIC
    # =====================================

    # Java-only certificates
    if (
        "Java" in detected_skills
        and
        "Full Stack" not in detected_skills
    ):

        if "Frontend" in detected_skills:

            detected_skills.remove(

                "Frontend"
            )

    # Python-only certificates
    if (
        "Python" in detected_skills
        and
        "Full Stack" not in detected_skills
    ):

        if "Frontend" in detected_skills:

            detected_skills.remove(

                "Frontend"
            )

    # AI/ML smart expansion
    if "AI & ML" in detected_skills:

        if (
            "Machine Learning"

            not in detected_skills
        ):

            detected_skills.append(

                "Machine Learning"
            )

        if (
            "Artificial Intelligence"

            not in detected_skills
        ):

            detected_skills.append(

                "Artificial Intelligence"
            )
        
        # If AI/ML is detected and Python is present, ensure data science skills
        if "Python" in detected_skills:
            
            if "Data Science" not in detected_skills:
                detected_skills.append("Data Science")

    # Full Stack smart expansion
    if "Full Stack" in detected_skills:

        if "Frontend" not in detected_skills:

            detected_skills.append(

                "Frontend"
            )

        if "Backend" not in detected_skills:

            detected_skills.append(

                "Backend"
            )

    # If Backend is detected, ensure REST API is included
    if "Backend" in detected_skills:

        if "REST API" not in detected_skills:

            detected_skills.append(

                "REST API"
            )

    # If Frontend is detected without specific framework
    if "Frontend" in detected_skills:

        if (
            "React" not in detected_skills
            and "Angular" not in detected_skills
            and "Vue.js" not in detected_skills
        ):

            if "HTML" not in detected_skills:

                detected_skills.append(

                    "HTML"
                )

            if "CSS" not in detected_skills:

                detected_skills.append(

                    "CSS"
                )

    # Remove Frontend from Python/Java backend certificates
    if (
        "Backend" in detected_skills
        and "Full Stack" not in detected_skills
    ):

        if (
            "Python" in detected_skills
            or "Java" in detected_skills
        ):

            if "Frontend" in detected_skills:

                detected_skills.remove(

                    "Frontend"
                )

    # If Database is mentioned with Python, ensure Data Science
    if (
        "SQL" in detected_skills
        and "Python" in detected_skills
    ):

        if "Data Science" not in detected_skills:

            detected_skills.append(

                "Data Science"
            )

    # =====================================
    # LIMIT SKILLS BASED ON PROGRAM
    # =====================================

    if program:

        program_lower = program.lower()

        if "java" in program_lower:
            # For Java programs, limit to max 6-8 relevant skills
            if len(detected_skills) > 8:
                priority_skills = [
                    "Java", "Spring Boot", "Spring", "REST API", "SQL",
                    "MySQL", "PostgreSQL", "MongoDB", "HTML", "CSS",
                    "JavaScript", "Full Stack", "Frontend", "Backend"
                ]
                filtered = []
                for skill in priority_skills:
                    if skill in detected_skills:
                        filtered.append(skill)
                        if len(filtered) >= 6:
                            break
                if filtered:
                    detected_skills = filtered

        elif "python" in program_lower:
            # For Python programs, limit to max 7-8 skills
            if len(detected_skills) > 8:
                priority_skills = [
                    "Python", "Django", "Flask", "FastAPI", "REST API",
                    "SQL", "MySQL", "PostgreSQL", "MongoDB", "HTML", "CSS",
                    "JavaScript", "Full Stack", "Frontend", "Backend",
                    "Data Science", "Machine Learning"
                ]
                filtered = []
                for skill in priority_skills:
                    if skill in detected_skills:
                        filtered.append(skill)
                        if len(filtered) >= 7:
                            break
                if filtered:
                    detected_skills = filtered

        elif "ai" in program_lower or "ml" in program_lower:
            # For AI/ML programs, limit to max 8 skills
            if len(detected_skills) > 8:
                priority_skills = [
                    "Python", "Machine Learning", "Deep Learning",
                    "Artificial Intelligence", "Data Science", "TensorFlow",
                    "Pandas", "NumPy", "Scikit-Learn"
                ]
                filtered = []
                for skill in priority_skills:
                    if skill in detected_skills:
                        filtered.append(skill)
                        if len(filtered) >= 8:
                            break
                if filtered:
                    detected_skills = filtered

        elif "data science" in program_lower:
            # For Data Science programs, limit to max 7 skills
            if len(detected_skills) > 7:
                priority_skills = [
                    "Python", "Data Science", "Machine Learning", "SQL",
                    "Pandas", "NumPy", "TensorFlow"
                ]
                filtered = []
                for skill in priority_skills:
                    if skill in detected_skills:
                        filtered.append(skill)
                        if len(filtered) >= 7:
                            break
                if filtered:
                    detected_skills = filtered

        # General limit for other programs
        elif len(detected_skills) > 10:
            detected_skills = detected_skills[:8]

    if program:

        program_lower = program.lower()

        filtered_skills = []

        # Java Full Stack - focus on Java ecosystem
        if "java full stack" in program_lower:

            java_relevant = [
                "Java", "Spring Boot", "Spring", "REST API", "SQL",
                "MySQL", "PostgreSQL", "MongoDB", "HTML", "CSS",
                "JavaScript", "React", "Angular", "Node.js", "Full Stack",
                "Frontend", "Backend"
            ]

            for skill in detected_skills:

                if skill in java_relevant:

                    filtered_skills.append(skill)

            detected_skills = filtered_skills

        # Python Full Stack - focus on Python ecosystem
        elif "python full stack" in program_lower:

            python_relevant = [
                "Python", "Django", "Flask", "FastAPI", "REST API",
                "SQL", "MySQL", "PostgreSQL", "MongoDB", "HTML", "CSS",
                "JavaScript", "React", "Angular", "Node.js", "Full Stack",
                "Frontend", "Backend", "Data Science", "Machine Learning"
            ]

            for skill in detected_skills:

                if skill in python_relevant:

                    filtered_skills.append(skill)

            detected_skills = filtered_skills

        # AI/ML - focus on AI/ML skills
        elif "ai" in program_lower or "ml" in program_lower:

            ai_relevant = [
                "Python", "Machine Learning", "Deep Learning",
                "Artificial Intelligence", "AI & ML", "Data Science",
                "TensorFlow", "OpenCV", "Pandas", "NumPy",
                "Scikit-Learn", "Matplotlib", "Seaborn", "SQL"
            ]

            for skill in detected_skills:
                if skill in ai_relevant:
                    filtered_skills.append(skill)

            detected_skills = filtered_skills

        # Data Science - focus on data skills
        elif "data science" in program_lower:

            data_relevant = [
                "Python", "Data Science", "Machine Learning", "SQL",
                "Pandas", "NumPy", "Matplotlib", "Seaborn",
                "TensorFlow", "Scikit-Learn", "Statistics"
            ]

            filtered_skills = []
            for skill in detected_skills:
                if skill in data_relevant:
                    filtered_skills.append(skill)

            detected_skills = filtered_skills

        # Blockchain - focus on blockchain skills
        elif "blockchain" in program_lower:

            blockchain_relevant = [
                "Blockchain", "Solidity", "Ethereum", "Web3",
                "Smart Contracts", "JavaScript", "React"
            ]

            filtered_skills = []
            for skill in detected_skills:
                if skill in blockchain_relevant:
                    filtered_skills.append(skill)

            detected_skills = filtered_skills

        # Cloud Computing - focus on cloud skills
        elif "cloud" in program_lower:

            cloud_relevant = [
                "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes",
                "DevOps", "Python", "Java", "CI/CD"
            ]

            filtered_skills = []
            for skill in detected_skills:
                if skill in cloud_relevant:
                    filtered_skills.append(skill)

            detected_skills = filtered_skills

        # Cyber Security - focus on security skills
        elif "cyber" in program_lower:

            security_relevant = [
                "Cyber Security", "Ethical Hacking", "Network Security",
                "Penetration Testing", "Python", "Linux"
            ]

            filtered_skills = []
            for skill in detected_skills:
                if skill in security_relevant:
                    filtered_skills.append(skill)

            detected_skills = filtered_skills

        # AR/VR - focus on AR/VR skills
        elif "ar" in program_lower or "vr" in program_lower:

            arvr_relevant = [
                "AR/VR", "Unity", "Unreal Engine", "C#", "C++",
                "3D Modeling", "Game Development"
            ]

            filtered_skills = []
            for skill in detected_skills:
                if skill in arvr_relevant:
                    filtered_skills.append(skill)

            detected_skills = filtered_skills

        # Android Development - focus on Android skills
        elif "android" in program_lower:

            android_relevant = [
                "Android", "Kotlin", "Java", "Mobile Development",
                "Firebase", "REST API", "SQLite"
            ]

            filtered_skills = []
            for skill in detected_skills:
                if skill in android_relevant:
                    filtered_skills.append(skill)

            detected_skills = filtered_skills

    # Remove duplicates
    detected_skills = list(set(detected_skills))

    return detected_skills
