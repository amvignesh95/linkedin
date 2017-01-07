from datetime import date
import pymongo
from pymongo import MongoClient

class UserProfile:
    user_info = ""    
    def __init__(self,token):
        self.user_info = token

    def get_id(self):
        return self.user_info['id']
    
    def get_firstname(self):
        return self.user_info['firstName']
    
    def get_lastname(self):
        return self.user_info['lastName']
    
    def get_email(self):
        return self.user_info['emailAddress']
    
    def get_degree(self):
        degree_name = []
        try:
            for degree in self.user_info['educations']['values']:
                degree_name.append(degree['degree'].encode('ascii',errors='ignore'))
        except KeyError:
            degree_name.append('-')
        return degree_name    

    def get_major(self):
        major_sub = []
        try:
            for major in self.user_info['educations']['values']:
                major_sub.append(major['fieldOfStudy'])
        except KeyError:
            major_sub.append('-')
        return major_sub
            
    def get_college(self):
        college_name = []
        try:
            for college in self.user_info['educations']['values']:
                college_name.append(college['schoolName'])
        except KeyError:
            college_name.append('-')
        return college_name
    
    def get_joining_date(self):        
        joining_year = []
        try:
            for year in self.user_info['educations']['values']:
                joining_year.append(str(year['startDate']['year']))
        except KeyError:
            joining_year.append('-')
        return joining_year
    
    def get_end_date(self):
        end_year = []
        try:
            for year in self.user_info['educations']['values']:            
                end_year.append(str(year['endDate']['year']))
        except KeyError:
            end_yeadr.append('-')
        return end_year

            
    def get_skills(self):
        skill = []
        try:
            for skills in self.user_info['skills']['values']:
                skill.append(skills['skill']['name'])            
        except KeyError:
            skill.append('-')
        return skill
    
    def get_languages(self):
        language_name = []
        try:
            for language in self.user_info['languages']['values']:
                language_name.append(language['language']['name'])
        except KeyError:
            language_name.append('-')
        return language_name
        
                
    def get_proficiency(self):
        proficiency_level = []
        try:            
            for proficiency in self.user_info['languages']['values']:
                proficiency_level.append(proficiency['proficiency']['level'])
        except KeyError:
            proficiency_level.append('-')
        return proficiency_level

    def get_company(self):
        company_name = []
        try:
            for company in self.user_info['positions']['values']:
                company_name.append(company['company']['name'])
        except KeyError:
            company_name.append('-')
        return company_name

    def get_position(self):
        pos = []
        try:
            for position in self.user_info['positions']['values']:
                pos.append(position['title'])
        except KeyError:
            pos.append('-')
        return pos
    
    def get_experience_year(self):
        experience_year = []
        index = 0
        try:
            for experience in self.user_info['positions']['values']:                       
                joining_month = experience['startDate']['month']
                joining_year = experience['startDate']['year']
                end_month = experience['endDate']['month']
                end_year = experience['endDate']['year']
                joining_date = date(joining_year,joining_month,1)
                end_date = date(end_year,end_month,28)
                experience_in_days = end_date - joining_date            
                experience_year.insert(index,(experience_in_days.days/365))
                index +=1
        except KeyError:
            experience_year.append('-')
        return experience_year            

    def get_experience_month(self):
        experience_month = []
        index = 0
        try:
            for experience in self.user_info['positions']['values']:                        
                joining_month = experience['startDate']['month']
                joining_year = experience['startDate']['year']
                end_month = experience['endDate']['month']
                end_year = experience['endDate']['year']
                joining_date = date(joining_year,joining_month,1)
                end_date = date(end_year,end_month,28)
                experience_in_days = end_date - joining_date            
                experience_month.insert(index,(experience_in_days.days%365)/30)
        except KeyError:
            experience_month.append('-')
        return experience_month

    def insert_details(self,basic_profile,education,skill,language,proficiency_level,position):
        try:
            client = MongoClient()
            db = client.linkedInDb
            result = db.profile.save(
            {
                "_id" : basic_profile['profile_id'],
                "firstName" : basic_profile['first_name'],
                "lastName" : basic_profile['last_name'],
                "emailId" : basic_profile['email_id'],
                "education" :
                {
                    "degree" : education['degree'],
                    "fieldOfStudy" : education['major_sub'],
                    "college" : education['college'],
                    "startDate" : education['joining_date'],
                    "endDate" : education['end_date']
                },
                "skill" : skill,
                "languages" :
                {
                    "language" : language,
                    "proficiency" : proficiency_level,
                },
                "position" :
                {
                    "companyName" : position['company_name'],
                    "title" : position['title'],
                    "experience " :
                    {
                        "month" : position['month'],
                        "year" : position['year']
                    }
                }
            })    
            print "Inserted"
        except pymongo.errors.ServerSelectionTimeoutError:
            print "No Server Found yet"

