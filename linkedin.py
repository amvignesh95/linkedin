import urllib2
import json
from datetime import date
from pymongo import MongoClient

class UserProfile:
    user_info = ""
    try:
        def __init__(self,token):
            self.user_info = token
    except urlli2.URLError as er:
        print er.message
        
    def get_firstname(self):
        return self.user_info['firstName']
    
    def get_lastname(self):
        return self.user_info['lastName']
    
    def get_email(self):
        return self.user_info['emailAddress']
    
    def get_degree(self):
        degree_name = []
        for degree in token['educations']['values']:
            degree_name.append(degree['degree'].encode('ascii',errors='ignore'))
        return degree_name    

    def get_major(self):
        major_sub = []
        for major in token['educations']['values']:
            major_sub.append(major['fieldOfStudy'])
        return major_sub
            
    def get_college(self):
        college_name = []
        for college in token['educations']['values']:
            college_name.append(college['schoolName'])
        return college_name
    
    def get_joining_date(self):        
        joining_year = []
        for year in token['educations']['values']:
            joining_year.append(str(year['startDate']['year']))
        return joining_year
    
    def get_end_date(self):
        end_year = []
        for year in token['educations']['values']:            
            end_year.append(str(year['endDate']['year']))
        return end_year
            
    def get_skills(self):
        skill = []
        for skills in token['skills']['values']:
            skill.append(skills['skill']['name'])
        return skill
    
    def get_languages(self):
        language_name = []
        for language in token['languages']['values']:
            language_name.append(language['language']['name'])
        return language_name
    
    def get_proficiency(self):
        proficiency_level = []
        for proficiency in token['languages']['values']:
            proficiency_level.append(proficiency['proficiency']['level'])
        return proficiency_level

    def get_company(self):
        company_name = []
        for company in token['positions']['values']:
            company_name.append(company['company']['name'])
        return company_name

    def get_position(self):
        pos = []
        for position in token['positions']['values']:
            pos.append(position['title'])
        return pos
    
    def get_experience_year(self):
        experience_year = []
        index = 0
        for experience in token['positions']['values']:                       
            joining_month = experience['startDate']['month']
            joining_year = experience['startDate']['year']
            end_month = experience['endDate']['month']
            end_year = experience['endDate']['year']
            joining_date = date(joining_year,joining_month,1)
            end_date = date(end_year,end_month,28)
            experience_in_days = end_date - joining_date            
            experience_year.insert(index,(experience_in_days.days/365))
            index +=1
        return experience_year            

    def get_experience_month(self):
        experience_month = []
        index = 0
        for experience in token['positions']['values']:                        
            joining_month = experience['startDate']['month']
            joining_year = experience['startDate']['year']
            end_month = experience['endDate']['month']
            end_year = experience['endDate']['year']
            joining_date = date(joining_year,joining_month,1)
            end_date = date(end_year,end_month,28)
            experience_in_days = end_date - joining_date            
            experience_month.insert(index,(experience_in_days.days%365)/30)               
        return experience_month
            
    
            
api_link = "https://api.linkedin.com/v1/people/~:(firstName,lastName,email-address,skills:(id,skill:(name)),educations:(id,school-name,field-of-study,start-date,end-date,degree,activities,notes),languages:(id,language:(name),proficiency:(level,name)),positions:(id,title,summary,start-date,end-date,is-current,company:(id,name,type,size,industry,ticker)))?oauth2_access_token="
url = api_link+"AQXu4mAx9-rQgh8v_8_sv5lJsk5BcxKls-t1SDWVipl2DpihEroWavJCi0qG8gdEAoE9Md5M9zHVUQgJR7lzEEnfxejPiHmn48w1EW6kjii0X2YTblViDrSAzkWe7DigJ0xiOJLh3r8kMKgEv2u4d2cIue98R2wB41x4_R0cUEAsKY7Y470&format=json"

request = urllib2.Request(url)
response = urllib2.urlopen(request)
token = json.loads(response.read())
obj = UserProfile(token)
first_name = obj.get_firstname()
last_name = obj.get_lastname()
email_id = obj.get_email()

print "First Name: "+first_name
print "Last Name: "+last_name
print "Email Id: "+email_id

degree = obj.get_degree()
major_sub = obj.get_major()
college = obj.get_college()
joining_date = obj.get_joining_date()
end_date = obj.get_end_date()

for education in range(len(degree)):
    print "\nDegree: "+degree[education]
    print "Field of Study: "+major_sub[education]
    print "College Name: "+college[education]
    print "Start Date: "+joining_date[education]
    print "End Date: "+end_date[education]

print "\nSkills"
skill = obj.get_skills()
for skills in skill:
    print "\t"+skills

print "\nLanguages Known"
language = obj.get_languages()
proficiency_level = obj.get_proficiency()
for j in range(len(language)):
    print "\n\tLanguage:\t"+language[j]
    print "\tProficiency Level:\t"+proficiency_level[j]

company_name = obj.get_company()
position = obj.get_position()
month = obj.get_experience_month()
year = obj.get_experience_year()


for k in range(len(company_name)):
    print "\nCompany Name: "+company_name[k]
    print "Position: "+position[k]
    print "Experience: "+str(year[k])+" Years "+str(month[k])+" Months "

client = MongoClient()
db = client.LinkedInDB
result = db.profile.insert_one(
            {
                
                "FirstName" : first_name,
                "LastName" : last_name,
                "EmailId" : email_id,
                "education" :
                {
                    "Degree" : degree,
                    "FieldOfStudy" : major_sub,
                    "College" : college,
                    "StartDate" : joining_date,
                    "endDate" : end_date
                },
                "Skill" : skill,
                "Language" : language,
                "Proficiency" : proficiency_level,
                "CompanyName" : company_name,
                "Position" : position,
                "Experience " :
                {
                    "Month" : month,
                    "Year" : year
                }
            })
            
    
    

