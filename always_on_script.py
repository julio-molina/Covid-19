from time import strftime, localtime, sleep
import urllib.request

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


def main():
    refreshTime="06:04"
    currentTime=strftime( "%H:%M",localtime())
    while(True):
        if (True):
            print("worked, do something ")
            gitDownloader();
        else:
            print("Nothin")
            sleep(60)
            #main();

main();
