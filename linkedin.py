import urllib2
import json
from datetime import date

class linkedin_info:
    info = ""
    def __init__(self,token):
        self.info = token
    def firstname(self):
        return self.info['firstName']
    def lastname(self):
        return self.info['lastName']
    def email(self):
        return self.info['emailAddress']
    def education(self):
        for edu in token['educations']['values']:
            print "\nDegree: "+edu['degree'].encode('ascii',errors='ignore')
            print "Field of Study: "+edu['fieldOfStudy']
            print "College: "+ edu['schoolName']
            print "Start Date: "+str(edu['startDate']['year'])
            print "End Date: "+str(edu['endDate']['year'])
    def skills(self):
        for ski in token['skills']['values']:
            print "\t"+ski['skill']['name']
    def lang(self):
        for lang in token['languages']['values']:
            print "\n\tLanguage: "+lang['language']['name']
            print "\tProficiency Level: "+lang['proficiency']['level']

    def exp(self):
        
        for exp in token['positions']['values']:
            print "\nCompany Name: "+exp['company']['name']
            print "\nPosition: "+exp['title']
            month1 = exp['startDate']['month']
            year1 = exp['startDate']['year']
            month2 = exp['endDate']['month']
            year2 = exp['endDate']['year']
            d0 = date(year1,month1,1)
            d1 = date(year2,month2,28)
            days = d1 - d0
            exp_year = days.days/365
            exp_month = (days.days%365)/30                
            print "\nExperience"
            print "\t"+str(exp_year)+" Years"
            print "\t"+str(exp_month)+" Months"
            
api = "https://api.linkedin.com/v1/people/~:(firstName,lastName,email-address,skills:(id,skill:(name)),educations:(id,school-name,field-of-study,start-date,end-date,degree,activities,notes),languages:(id,language:(name),proficiency:(level,name)),positions:(id,title,summary,start-date,end-date,is-current,company:(id,name,type,size,industry,ticker)))?oauth2_access_token="
url = api+"AQXu4mAx9-rQgh8v_8_sv5lJsk5BcxKls-t1SDWVipl2DpihEroWavJCi0qG8gdEAoE9Md5M9zHVUQgJR7lzEEnfxejPiHmn48w1EW6kjii0X2YTblViDrSAzkWe7DigJ0xiOJLh3r8kMKgEv2u4d2cIue98R2wB41x4_R0cUEAsKY7Y470&format=json"
req = urllib2.Request(url)
response = urllib2.urlopen(req)
token = json.loads(response.read())

obj = linkedin_info(token)
print "First Name: "+obj.firstname()
print "Last Name: "+obj.lastname()
print "Email Id: "+obj.email()
obj.education()
print "\nSkills"
obj.skills()
print "\nLanguages Known"
obj.lang()
obj.exp()
