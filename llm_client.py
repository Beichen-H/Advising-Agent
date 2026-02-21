class UIUCChatClient:
    def __init__(self):
        print("⚠️  Running in offline mode with official handbook data")
    
    def generate_response(self, messages, temperature=0.7, max_tokens=1000):
        """Return responses based on official Sociology handbook"""
        user_message = ""
        for msg in reversed(messages):
            if msg["role"] == "user":
                user_message = msg["content"]
                break
        
        # Sociology Major Requirements (from official handbook)
        if "sociology" in user_message.lower() or "soc" in user_message.lower():
            if "declare" in user_message.lower():
                return """**📋 Declaring Sociology Major**

**Requirements to Declare:**
• Complete at least one sociology course (SOC 100 or equivalent)
• 2.00 GPA or higher for sociology courses
• Current UIUC students: Complete the declaration form online
• Once approved, you'll receive an email confirmation

**Contact:** soc-advising@illinois.edu for advising appointments

**Prospective Transfer Students:**
• Check Office of Undergraduate Admissions Transfer Handbook (Sociology listed on page 69)
• Recommended: Complete course that transfers as SOC 100
• Email soc-advising@illinois.edu for more information"""
            
            elif "requirement" in user_message.lower() or "overview" in user_message.lower() or "major" in user_message.lower():
                return """**📊 Sociology Major Requirements (32 total hours)**

**Required Courses (5 classes):**

1. **Introductory Sociology** (3-4 hrs)
   - SOC 100: Introduction to Sociology
   - Prerequisite for most 200-level courses

2. **Introductory Statistics** (3-4 hrs)
   - SOC 200: Social Statistics
   - Topics: statistical measures, central tendency, correlation, inference
   - Prerequisite for SOC 380

3. **Introduction to Sociological Theory** (3 hrs)
   - SOC 380: Sociological Theory
   - Topics: social order, conflict, capitalism, bureaucracy
   - Prerequisite: Sophomore standing

4. **Social Science Research Methods** (4 hrs)
   - SOC 280: Research Methods
   - Topics: research design, measurement, sampling, surveys, data analysis

5. **Capstone Experience** (3 hrs) - Choose one:
   - SOC 400: Internships (requires approved internship)
   - SOC 490: Senior Research Seminar
   - SOC 495: Senior Honors Seminar (3.5 GPA in SOC courses, instructor consent)

**Note:** If using transfer credit for SOC 100, some schools grant only 3 credits."""
            
            elif "statistics" in user_message.lower() or "stat" in user_message.lower():
                return """**📊 Statistics Requirement**

**SOC 200: Social Statistics** (4 hrs)
• Introduction to statistical measures for social sciences
• Topics: measures of central tendency, dispersion, correlation, statistical inference
• Includes computer-based data analysis
• Prerequisite for SOC 380

**Alternative courses that meet requirement:**
• STAT 100
• PSYCH 235
• ECON 202
• MATH 161
• UP 116
• Parkland College: MATH 108, MATH 160

**Note:** Alternative courses count for statistics requirement but NOT toward sociology hours."""
            
            elif "theory" in user_message.lower():
                return """**📚 Sociological Theory (SOC 380)**

**Course Description:**
Introduction to foundations of sociological theory.

**Topics include:**
• Problem of social order
• Nature of social conflict
• Capitalism and bureaucracy
• Social structure and politics
• Evolution of modern societies

**Prerequisite:** Sophomore standing
**Credit:** 3 hours"""
            
            elif "research" in user_message.lower() or "methods" in user_message.lower():
                return """**🔬 Social Science Research Methods (SOC 280)**

**Course Description:**
Introduction to foundations of social research and major research methods.

**Topics covered:**
• Research design
• Finding and using sociology literature
• Measurement and sampling
• Survey research and field methods
• Quantitative data analysis
• Computer resources for research

**Credit:** 4 hours
**Includes:** Computer use in sociology"""
            
            elif "capstone" in user_message.lower():
                return """**🎓 Capstone Experience Options (3 hrs)**

Choose ONE of the following:

**1. SOC 400: Internships**
• Requires approved on/off-campus internship
• Apply before 1st class day of term
• Must meet Guidelines for Internships
• Can be repeated up to 6 hours
• Prerequisite: Sophomore+ standing, SOC 100, SOC 200, +3 additional SOC hours
• Seats limited, reserved for primary majors

**2. SOC 490: Senior Research Seminar**
• Conceive and execute original sociological research
• Use knowledge from substantive courses
• Apply skills from methods courses
• Professional development activities included

**3. SOC 495: Senior Honors Seminar**
• For students graduating with distinction
• Critical reading, essays, research proposals
• Prerequisite: 3.5 GPA in SOC courses, instructor consent
• May be repeated up to 6 hours"""
            
            elif "supporting coursework" in user_message.lower() or "supporting" in user_message.lower():
                return """**📚 Supporting Coursework Requirement**

**Requirement:** 12 hours of supporting coursework
• 4 courses logically grouped around a theme
• Reflects interests outside Sociology
• Courses can be from different departments

**Common ways to fulfill:**
• Complete a certificate
• Complete a minor (e.g., Criminology, Law & Society)
• Complete a double major

**Sociology + Criminology, Law & Society Combination:**
• Reduced hours: 41 credit hours total
• Contact soc-advising@illinois.edu for assistance

**Planning:** Start planning by sophomore year!"""
            
            elif "criminology" in user_message.lower() or "cls" in user_message.lower():
                return """**⚖️ Sociology + Criminology, Law & Society Combined**

**Combined Program Benefits:**
• Reduced total hours: 41 credit hours
• Complete both Sociology major and CLS minor
• Contact soc-advising@illinois.edu for planning assistance

**Requirements:**
• Sociology major requirements (32 hours)
• Criminology, Law & Society minor requirements (overlap reduces total)

**To Declare CLS Minor:**
• Contact CLS advising or use declaration form"""
            
            elif "transfer" in user_message.lower():
                return """**🔄 Transfer Student Information**

**Admission Requirements:**
• Check Office of Undergraduate Admissions Transfer Handbook
• Sociology is listed on page 69
• Email soc-advising@illinois.edu for details

**Recommended Preparation:**
• Complete a 3-hour course that transfers as SOC 100
• Contact Office of Undergraduate Admissions for:
  - Admission details
  - Campus visits
  - Application process

**Note:** Transfer credit for SOC 100 may be 3 credits instead of 4"""
            
            elif "internship" in user_message.lower():
                return """**💼 SOC 400 Internships**

**Requirements:**
• Must have approved on or off-campus internship
• Apply before 1st class day of the term
• Internship must meet Guidelines for Internships
• Seats are limited
• Reserved for primary majors

**Prerequisites:**
• Sophomore, Junior, or Senior standing
• SOC 100 (or SOC 101/163)
• SOC 200
• 3 additional hours in Sociology

**Credit:** 3 hours, may be repeated up to 6 hours"""
            
            elif "honors" in user_message.lower() or "495" in user_message.lower():
                return """**🏆 SOC 495 Senior Honors Seminar**

**Description:**
• One of two options for graduating with departmental distinction
• Critical reading and discussion
• Essays and research proposals
• Topic varies yearly

**Requirements:**
• Sociology majors only
• 3.5 GPA in sociology courses
• Consent of instructor

**Credit:** 3 undergraduate hours, may be repeated up to 6 hours

**Example Project:**
Junior Dale Robbennolt (Civil Engineering + Sociology) researched "Faculty Perceptions of Gender in Engineering Education and Group Work" - presented at UIUC Undergraduate Research Symposium Spring 2021"""
            
            elif "advisor" in user_message.lower() or "advising" in user_message.lower():
                return """**👥 Sociology Academic Advising**

**Contact Information:**
• Email: soc-advising@illinois.edu
• Department: sociology@illinois.edu
• Phone: (217) 333-1950
• Office: 3120 Lincoln Hall, 702 S. Wright St., Urbana, IL 61801

**Services:**
• Schedule advising appointments
• Questions about major/minor requirements
• Transfer student inquiries
• Course planning assistance

**Resources:**
• Sociology Major Course Planning Form
• Supporting Coursework PowerPoint guide
• Sociology + CLS Combination planning form"""
            
            else:
                return """**🎓 Sociology Major at UIUC**

The Department of Sociology offers:
• **Major in Sociology** (32 hours)
• **Minors** in various sociology topics
• **Combined program** with Criminology, Law & Society (41 hours)

**Key Requirements:**
• 5 core courses: SOC 100, SOC 200, SOC 280, SOC 380, plus Capstone
• 12 hours supporting coursework (can use minor/certificate)
• Declare by completing one SOC course with 2.0+ GPA

**Contact:** soc-advising@illinois.edu for advising
**Location:** 3120 Lincoln Hall

What would you like to know more about?
• Declaration requirements
• Course requirements
• Statistics alternatives
• Capstone options
• Supporting coursework
• Transfer information
• Advising contact"""
        
        # Default response for non-sociology questions
        else:
            return """I specialize in Sociology major information at UIUC. 

**I can help you with:**
• 📋 Declaring Sociology major
• 📚 Required courses (SOC 100, 200, 280, 380, Capstone)
• 📊 Statistics requirements and alternatives
• 🎓 Capstone options (Internship, Research, Honors)
• 📝 Supporting coursework
• 🔄 Transfer student information
• 👥 Advising contact information

**Try asking:**
• "What are the Sociology major requirements?"
• "How do I declare Sociology?"
• "What statistics courses count for Sociology?"
• "Tell me about SOC 400 internships"
• "What is supporting coursework?"
• "How do I contact Sociology advising?"

For questions about other majors or general LAS policies, please consult the LAS Academic Handbook or your college advisor."""
    
    def get_embeddings(self, text):
        """Return mock embeddings"""
        return [0.1] * 1536
