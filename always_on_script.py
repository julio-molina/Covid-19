#Julio Molina

#NOTICE: currently using temporary hard coded directories to download and run jupyter notebooks.
# ATM this script and it's use of additional programs currently implies that you are
#using a linux based system, with "jupyter lab" and anaconda installed which includes many
#data science oriented python libaries. Python 3.8

#TODO: ATM the script is able to run everything atleast once, and not countious as it will
#be implemented later in its lifespan.
from time import strftime, sleep, gmtime#UTC time +4EST
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
    sleep(6)

def runjupyter():
    #process=subprocess.call("jupyter lab ~/projects/dir/models.ipynb", shell=True)
    #command = ['perl', '-e', "'alarm shift @ARGV; exec @ARGV'", "200"]
    exec_proc = subprocess.call("perl -e 'alarm shift @ARGV; exec @ARGV' 21600 jupyter lab ~/projects/dir/models.ipynb", shell=True)# 6 hours


def getFilestats():
    print("set to do nothing:")


def main():
    subprocess.call("cd ~/projects/dir/", shell=True)
    currentTime=strftime( "%H:%M",gmtime())#UTC time +4 EST
    while(True):
        if (True):#("10:00"):#utctime +4 EST
            print("worked, do something ")
            gitDownloader();
            runjupyter();
        else:
            print("Nothin")
            sleep(60)
            #main();

main();
