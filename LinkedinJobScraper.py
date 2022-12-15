import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, RemoteFilters
import json

def on_data(data: EventData):
    # print('[ON_DATA]'
    #       '\nJob ID: {0}'.format(data.job_id),
    #       '\nJob Title: {0}'.format(data.title),
    #       '\nCompany Name: {0}'.format(data.company),
    #       '\nEmployment Type: {0}'.format(data.employment_type),
    #       '\nIndustries: {0}'.format(data.industries),
    #       '\nDate: {0}'.format(data.date),
    #       '\nLocation: {0},{1}'.format(data.location,data.place),
    #       '\nJob Description: {0}'.format(data.description),
    #       '\nJob Link: {0}'.format(data.link),
    #       '\nApply Link: {0}'.format(data.apply_link),
    #       '\nJob Function: {0}'.format(data.job_function))

    # Serializing json
    JobData = {
        "Job_ID": data.job_id,
        "Job_Title:": data.title,
        "Company_Name:": data.company,
        "Employment_Type": data.employment_type,
        "Industries":data.industries,
        "Date":data.date,
        "Location":data.location+","+data.place,
        "Job_Description":data.description,
        "Job_Link":data.link,
        "Apply_Link":data.apply_link,
    }
    json_object = json.dumps(JobData, indent=4)


    # Writing to sample.json
    with open("/Users/cchen/Desktop/university/computerScience/631/ScrapedData/JobID:{0}.json".format(data.job_id), "w") as outfile:
        outfile.write(json_object)

def on_error(error):
    print('[ON_ERROR]', error)


def on_end():
    print('[ON_END]')


scraper = LinkedinScraper(
    chrome_executable_path="/usr/local/bin/chromedriver", # Custom Chrome executable path (e.g. /foo/bar/bin/chromedriver)
    chrome_options=None,  # Custom Chrome options here
    headless=True,  # Overrides headless mode only if chrome_options is None
    max_workers=1,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
    slow_mo=3,  # Slow down the scraper to avoid 'Too many requests (429)' errors. Suggest a value of at least 1.3 in anonymous mode and 0.4 in authenticated mode.
)

# Add event listeners
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

option=QueryOptions(
            locations=['United States'],
            optimize=False,
            filters=QueryFilters(
                #company_jobs_url='https://www.linkedin.com/jobs/search/?f_C=1441%2C17876832%2C791962%2C2374003%2C18950635%2C16140%2C10440912&geoId=92000000',  # Filter by companies
                relevance=RelevanceFilters.RELEVANT,
                type=None,
                experience=None
            )
        )
queries = [
    Query(
        query='software engineer',
        options=option
    ),
    Query(
        query='software developer',
        options=option
    ),
    Query(
        query='software',
        options=option
    ),
    Query(
        query='machine learning',
        options=option
    ),
    Query(
        query='data science',
        options=option
    ),
    Query(
        query='developer',
        options=option
    )

]

scraper.run(queries)

