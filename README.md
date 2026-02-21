# LAS Academic Advising Assistant

An AI-powered academic advising assistant designed to help students navigate degree requirements, course selections, and academic policies across multiple departments at the University of Illinois Urbana-Champaign.

This tool was developed as part of my internship with the **Applied Technologies for Learning in the Arts & Sciences (ATLAS)** at the University of Illinois Urbana-Champaign.

**Author:** Beichen Hu  
**Role:** AI Research Intern, ATLAS  
**Date:** February 2026

---

## Overview

The College of Liberal Arts & Sciences has 70+ majors, each with complex degree requirements, course offerings, and academic policies. Students often struggle to find accurate information about their programs, and advisors face repetitive questions that could be automated.

The LAS Academic Advising Assistant solves that.

It takes a plain-language question from a student and returns:

- Accurate information about degree requirements
- Course descriptions and prerequisites
- Program options (majors, minors, certificates)
- Department contact information when needed
- Validated responses based on official handbooks

This gives students 24/7 access to advising information and allows advisors to focus on more complex developmental advising.

---

## Features

### 1. Multi-Department Knowledge Base
The system currently supports:

#### **Sociology Department**
- Sociology Major (32 hours)
- Sociology Minor (18 hours)
- CLS Minor (18 hours)
- Sociology + CLS Combination (41 hours)
- Complete course catalog (SOC 100-599)

#### **Statistics Department**
- Statistics Major (42-45 hours)
- Statistics & Computer Science Major (68-72 hours)
- Statistics Minor
- Data Science Minor (21 hours)
- Certificate in Data Science

*More departments coming soon: Economics, Psychology, and others.*

### 2. Free-form Query Intake
Students can describe their question however they want. The system understands natural language and retrieves relevant information.

Example queries:
- "What are the requirements for Sociology major?"
- "Can I take STAT 100 instead of SOC 280?"
- "Tell me about the Data Science minor"
- "What's the difference between SOC 450 and SOC 495?"

### 3. AI-Powered Responses
Powered by OpenAI's GPT models, the system:
- Understands context and follow-up questions
- Provides accurate, detailed answers
- Cites sources from official handbooks
- Offers department contact information when needed

### 4. Structured Knowledge Base
All program information is stored in organized text files:
data/knowledge_base/
├── sociology/
│   ├── sociology_major_requirements.txt
│   ├── sociology_minor_requirements.txt
│   ├── cls_minor_requirements.txt
│   ├── sociology_cls_combination.txt
│   ├── sociology_course_catalog.txt
│   └── sociology_programs_overview.txt
└── statistics/
    ├── statistics_major_requirements.txt
    ├── stat_cs_major_requirements.txt
    ├── statistics_minor_requirements.txt
    ├── data_science_minor_requirements.txt
    ├── data_science_certificate.txt
    └── statistics_programs_overview.txt

### 5. Extensible Architecture
The system is designed to easily add new departments:
- Add files to data/knowledge_base/[department]/
- Update contact information in the configuration
- Add sample questions to the UI

---

## Setup Instructions

### 1. Clone the repository
git clone [your-repository-url]
cd las_advising_assistant

### 2. Install dependencies
pip install -r requirements.txt

### 3. Configure your environment
Create a .env file in the root directory:
OPENAI_API_KEY=your_openai_api_key_here

### 4. Run the application
streamlit run app.py

The app will open in your browser at http://localhost:8501.

---

## How It Works

### 1. User Query
The system accepts a natural language question from the student.

### 2. Knowledge Base Loading
All handbook files are loaded from the organized folder structure.

### 3. AI Processing
The query is sent to the LLM along with relevant handbook context.

### 4. Response Generation
The AI generates a helpful, accurate response based on official documents.

### 5. Contact Information
When information is unavailable, the system provides appropriate department contact details.

---

## Project Structure

las_advising_assistant/
├── app.py                    # Main Streamlit application
├── llm_client_openai.py      # OpenAI API client
├── config.py                 # Configuration settings
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (API keys)
├── data/
│   └── knowledge_base/       # Organized handbook files
│       ├── sociology/        # Sociology department documents
│       └── statistics/       # Statistics department documents
└── README.md                 # This file

---

## Future Directions

- **Expand to More Departments**: Add Economics, Psychology, Political Science, and other LAS departments
- **Course Schedule Integration**: Connect with Course Explorer API for real-time offering information
- **Personalized Advising**: Incorporate student records for personalized degree audits
- **Multi-Language Support**: Add support for international students
- **Mobile App**: Develop a mobile-friendly version for on-the-go access

---

## Acknowledgments

This project was developed during my internship with **Applied Technologies for Learning in the Arts & Sciences (ATLAS)** at the University of Illinois Urbana-Champaign.

Special thanks to:
- The ATLAS team for their guidance and support
- Sociology Department for providing detailed handbook information
- Statistics Department for comprehensive program documentation
- LAS Academic Advising offices for their valuable input

---

## Contact

**Beichen Hu**  
AI Research Intern, ATLAS  
University of Illinois Urbana-Champaign

For questions about the project, please contact the ATLAS team at atlas@illinois.edu.

---

## License

This project is developed for educational and research purposes at the University of Illinois Urbana-Champaign.

© 2026 Beichen Hu, ATLAS, University of Illinois Urbana-Champaign
