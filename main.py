from jenkinsapi.jenkins import Jenkins
import sqlite3
import datetime

conn = sqlite3.connect('casestudy1.db') #Connect to dtabase
c = conn.cursor() # get cursor


def get_server_instance():
    jenkins_url = 'http://jenkins_host:8080' #jenkins host
    server = Jenkins(jenkins_url, username = 'foouser', password = 'foopassword') 
    return server

if __name__ == '__main__':
    print (get_server_instance().version)

def get_job_details():
    server = get_server_instance()
    for j in server.get_jobs():
        job_instance = server.get_job(j[0]) #get job instance
        now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') #get now variable
        insertValues = [(job_instance.name,job_instance.is_running(),now)] # array with values to insert
        c.executemany("INSERT INTO job VALUES (?,?,?)", insertValues) #insert in db
        conn.commit()
    exit()





