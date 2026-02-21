from pathlib import Path

def create_sample_handbook():
    """Create a sample handbook for testing"""
    
    sample_content = """LAS General Education Requirements

All students in the College of LAS must complete the following General Education requirements:

1. Composition I (3-4 hours)
   - Fulfilled by RHET 105 or equivalent

2. Advanced Composition (3 hours)
   - Must be taken after Composition I
   - Can be fulfilled by many 200+ level courses in various departments

3. Humanities & the Arts (6 hours)
   - At least 3 hours in Humanities
   - At least 3 hours in Arts
   - Courses must come from approved list

4. Natural Sciences & Technology (6 hours)
   - At least 3 hours in Physical Sciences
   - At least 3 hours in Life Sciences
   - One course must include a lab component

5. Social & Behavioral Sciences (6 hours)
   - Courses must come from approved list
   - Can include Economics, Psychology, Sociology, etc.

6. Cultural Studies (9 hours)
   - US Minority Cultures (3 hours)
   - Non-Western Cultures (3 hours)
   - Western/Comparative Cultures (3 hours)

Pass/Fail Policy:
- Students may take up to 12 hours Pass/Fail
- Cannot be used for courses in major
- Cannot be used to fulfill General Education requirements
- Deadline: End of 8th week of semester

Declaration of Major:
- Must be declared by 60 credit hours
- Requires minimum 2.0 GPA in major courses
- Some majors have additional requirements

Transfer Credit:
- Must be approved by relevant department
- Grade of C or better required
- Maximum 60 hours from community colleges

Sociology Major Requirements:
- SOC 100: Introduction to Sociology
- SOC 200: Social Statistics
- SOC 280: Sociological Research Methods
- SOC 380: Sociological Theory
- 5 additional 300/400 level SOC courses
- Minimum 2.0 GPA in major courses
"""
    
    handbook_path = Path("data/handbooks/sociology_handbook.txt")
    handbook_path.write_text(sample_content)
    print(f"✅ Created sample handbook at {handbook_path}")

if __name__ == "__main__":
    create_sample_handbook()
