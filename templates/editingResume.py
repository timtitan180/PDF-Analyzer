# import pdfplumber
# import os
#
# targetFound = False
#
# with pdfplumber.open("C:/Users/timtu/Downloads/Web_Dev_Resume.pdf") as pdf:
#     first_page = pdf.pages[0]
#     pdf_paragraphs = first_page.extract_text()
#     if "SOFT SKILLS" in pdf_paragraphs:
#         targetFound = True
#         soft_skills_position = pdf_paragraphs.index("SOFT SKILLS")
#         pdf_paragraphs.replace(range(soft_skills_position), soft_skills_position + 10, "")
#         print(pdf_paragraphs.index("SOFT SKILLS"))
#         new_pdf = pdf_paragraphs.replace("SOFT SKILLS", "")
#         print(new_pdf)
