import urllib2
import json
from linkedin import UserProfile
import pymongo
from pymongo import MongoClient

token = "Null"
try:
    api_link = "https://api.linkedin.com/v1/people/~:(id,firstName,lastName,email-address,skills:(id,skill:(name)),educations:(id,school-name,field-of-study,start-date,end-date,degree,activities,notes),languages:(id,language:(name),proficiency:(level,name)),positions:(id,title,summary,start-date,end-date,is-current,company:(id,name,type,size,industry,ticker)))?oauth2_access_token="
    url = api_link+"AQUkwrBNKJY6QAuxxX4Sem6JkO12kwchhCwxp8-cwsaOcL_0NSAkaZ6hwgNEwWh2XPQ-LN4k-bHHRy2rb5l2QhpJ4dmOli3Z-i_LzUWCW-vNx_CERd9rzDeFnFa-bft6jWEGtSQKCHrsYCq2RKTkr6WvvGavEwkxX2eqaOIfEKPituJvPsI&format=json"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    token = json.loads(response.read())
except urllib2.URLError:
    print "Check Your Internet Connection"

if(token!="Null"):
    obj = UserProfile(token)

    profile_id = obj.get_id()
    first_name = obj.get_firstname()
    last_name = obj.get_lastname()
    email_id = obj.get_email()

    degree = obj.get_degree()
    major_sub = obj.get_major()
    college = obj.get_college()
    joining_date = obj.get_joining_date()
    end_date = obj.get_end_date()

    skill = obj.get_skills()


    language = obj.get_languages()
    proficiency_level = obj.get_proficiency()

    company_name = obj.get_company()
    position = obj.get_position()
    month = obj.get_experience_month()
    year = obj.get_experience_year()


    try:
        client = MongoClient()
        db = client.linkedInDb
        result = db.profile.insert_one(
            {
                "_id" : profile_id,
                "firstName" : first_name,
                "lastName" : last_name,
                "emailId" : email_id,
                "education" :
                {
                    "degree" : degree,
                    "fieldOfStudy" : major_sub,
                    "college" : college,
                    "startDate" : joining_date,
                    "endDate" : end_date
                },
                "skill" : skill,
                "languages" :
                {
                    "language" : language,
                    "proficiency" : proficiency_level,
                },
                "position" :
                {
                    "companyName" : company_name,
                    "title" : position,
                    "experience " :
                    {
                        "month" : month,
                        "year" : year
                    }
                }
            })    
        print "Inserted"
    except pymongo.errors.ServerSelectionTimeoutError:
        print "No Server Found yet"
    except pymongo.errors.DuplicateKeyError:
        result = db.profile.save(
            {
                "_id" : profile_id,
                "firstName" : first_name,
                "lastName" : last_name,
                "emailId" : email_id,
                "education" :
                {
                    "degree" : degree,
                    "fieldOfStudy" : major_sub,
                    "college" : college,
                    "startDate" : joining_date,
                    "endDate" : end_date
                },
                "skill" : skill,
                "languages" :
                {
                    "language" : language,
                    "proficiency" : proficiency_level,
                },
                "position" :
                {
                    "companyName" : company_name,
                    "title" : position,
                    "experience " :
                    {
                        "month" : month,
                        "year" : year
                    }
                }
            })
        print "Updated"
