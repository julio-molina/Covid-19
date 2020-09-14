#Julio Molina

#NOTICE: currently using temporary hard coded directories to download and run jupyter notebooks.
# ATM this script and it's use of additional programs currently implies that you are
#using a linux based system, with "jupyter lab" and anaconda installed which includes many
#data science oriented python libaries. Python 3.8

#TODO: ATM the script is able to run everything atleast once, and not countious as it will 
#be implemented later in its lifespan.
from time import strftime, localtime, sleep
import urllib.request
import subprocess

def gitDownloader():
    import urllib.request
    us_state_url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    us_url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
    us_liveurl ="https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us.csv"
    us_state_liveurl="https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv"
    print ("download start!")
    filename, headers = urllib.request.urlretrieve(us_state_url, filename="us-states.csv")
    print("us-states download complete")
    filename, headers = urllib.request.urlretrieve(us_url, filename="us.csv")
    print("us download complete")
    #filename, headers = urllib.request.urlretrieve(us_liveurl, filename="us-live.csv")
    #print("us live download complete")
    #filename, headers = urllib.request.urlretrieve(us-state_liveurl, filename="us-states-live.csv")
    #print("us-states live download complete")
    print ("download complete!")
    print ("download file location: ", filename)
    print ("download headers: ", headers)
    #sleep(82800)#23 hours
    sleep(60)

def runjupyter():
    subprocess.call("jupyter lab ~/projects/dir/models.ipynb", shell=True)

def main():
    subprocess.call("cd ~/projects/dir/", shell=True)
    refreshTime="06:04"
    currentTime=strftime( "%H:%M",localtime())
    while(True):
        if (True):
            print("worked, do something ")
            gitDownloader();
            runjupyter();
        else:
            print("Nothin")
            sleep(60)
            #main();

main();
