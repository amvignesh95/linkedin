import urllib2
import json
from datetime import date

class UserProfile:
    user_info = ""
    def __init__(self,token):
        self.user_info = token
    def get_firstname(self):
        return self.user_info['firstName']
    def get_lastname(self):
        return self.user_info['lastName']
    def get_email(self):
        return self.user_info['emailAddress']
    def get_education(self):
        for education in token['educations']['values']:
            print "\nDegree: "+education['degree'].encode('ascii',errors='ignore')
            print "Field of Study: "+education['fieldOfStudy']
            print "College: "+ education['schoolName']
            print "Start Date: "+str(education['startDate']['year'])
            print "End Date: "+str(education['endDate']['year'])
    def get_skills(self):
        print "\nSkills"
        for skills in token['skills']['values']:
            print "\t"+skills['skill']['name']
    def get_languages(self):
        print "\nLanguages Known"
        for language in token['languages']['values']:
            print "\n\tLanguage: "+language['language']['name']
            print "\tProficiency Level: "+language['proficiency']['level']

    def get_experience(self):
        
        for experience in token['positions']['values']:
            print "\nCompany Name: "+experience['company']['name']
            print "\nPosition: "+experience['title']
            joining_month = experience['startDate']['month']
            joining_year = experience['startDate']['year']
            end_month = experience['endDate']['month']
            end_year = experience['endDate']['year']
            joining_date = date(joining_year,joining_month,1)
            end_date = date(end_year,end_month,28)
            experience_in_days = end_date - joining_date
            experience_year = experience_in_days.days/365
            experience_month = (experience_in_days.days%365)/30                
            print "\nExperience"
            print "\t"+str(experience_year)+" Years"
            print "\t"+str(experience_month)+" Months"
            
api_link = "https://api.linkedin.com/v1/people/~:(firstName,lastName,email-address,skills:(id,skill:(name)),educations:(id,school-name,field-of-study,start-date,end-date,degree,activities,notes),languages:(id,language:(name),proficiency:(level,name)),positions:(id,title,summary,start-date,end-date,is-current,company:(id,name,type,size,industry,ticker)))?oauth2_access_token="
url = api_link+"AQXu4mAx9-rQgh8v_8_sv5lJsk5BcxKls-t1SDWVipl2DpihEroWavJCi0qG8gdEAoE9Md5M9zHVUQgJR7lzEEnfxejPiHmn48w1EW6kjii0X2YTblViDrSAzkWe7DigJ0xiOJLh3r8kMKgEv2u4d2cIue98R2wB41x4_R0cUEAsKY7Y470&format=json"
request = urllib2.Request(url)
response = urllib2.urlopen(request)
token = json.loads(response.read())

obj = UserProfile(token)
print "First Name: "+obj.get_firstname()
print "Last Name: "+obj.get_lastname()
print "Email Id: "+obj.get_email()
obj.get_education()
obj.get_skills()
obj.get_languages()
obj.get_experience()
