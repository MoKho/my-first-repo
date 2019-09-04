import requests, bs4, json, random, pyrebase
config = {
  "apiKey": "AIzaSyBflxakAVKd8wLWKLj2qu3vJsvDdTeJn3Y",
  "authDomain": "cartgamefootbal.firebaseapp.com",
  "databaseURL": "https://cartgamefootbal.firebaseio.com/",
  "storageBucket": "cartgamefootbal.appspot.com"
}
firebase = pyrebase.initialize_app(config)

teamsoup = bs4.BeautifulSoup(requests.get("https://www.worldfootball.net/alltime_table/wm/").text, 'html.parser')
team_headers = ["Rank", "Team", "Matches", "Wins", "Draws", "Losses", "Goals", "Dif", "Points"]
team_elements = teamsoup.select("td")
list_of_params = []
final_result = []
temporary_list = []
for i, j in enumerate(team_elements):
    if i % 10 != 1:
        list_of_params.append(j.getText().replace("\n",""))

for i, j in enumerate(list_of_params):
    if i % 9 == 0:
        final_result.append(temporary_list)
        temporary_list = []
        temporary_list.append("id" + " : " + str(random.randrange(1234567890, 9876543210)))
        temporary_list.append(team_headers[i%9] + " : " + str(j))
    else :
        temporary_list.append(team_headers[i%9] + " : " + str(j))
final_result.pop(0)

#for i in final_result:
#    print("\n\n\n***************\n", i)

db = firebase.database()
db.child("cart2")
db.child("cart2").push(final_result)

#with open("Cards_data.json", 'w') as json_file:
#    json_file.write(json.dumps(final_result, sort_keys=True, indent=4))