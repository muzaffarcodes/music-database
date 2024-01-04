import sqlite3
import time

contact = sqlite3.connect("/home/muzaffar/Desktop/seleniumPython/music_player.db")

index = contact.cursor()

def enter_table():
	index.execute("CREATE TABLE IF NOT EXISTS music_player (Musician Text,Music Text, Duration Text,Size Text,Album Text) ")
	contact.commit()
enter_table()

def add_info(musician,music,duration,size,album):
	index.execute("INSERT INTO music_player VALUES(?,?,?,?,?)",(musician,music,duration,size,album))	
	contact.commit()

def get_all():
	index.execute("SELECT * FROM music_player")
	info = index.fetchall()
	print("Loading...")
	time.sleep(2)
	for i in info:
		print(*i)	

def data_getOne():
    try:
        index.execute("SELECT * FROM music_player WHERE Musician = ?",(input("Which musician do you want to see: "),))
        info = index.fetchall()
        print("Sabr...")
        time.sleep(2)
        for i in info:
            print(*i)
    except:
        print("Please enter correct!")        

def update_music():
	index.execute("UPDATE music_player SET Music WHERE Musician=?",(input("Which Music: "),input("Which Musician:"),))
	contact.commit()

def update_duration():
	index.execute("UPDATE music_player SET Duration WHERE Musician=?",(input("How many Duration: "),input("Which Musician:"),))
	contact.commit()

def update_size():
	index.execute("UPDATE music_player SET Size WHERE Musician=?",(input("How many Size: "),input("Which Musician:"),))
	contact.commit()

def update_album():
	index.execute("UPDATE music_player SET Album WHERE Musician=?",(input("Which Album: "),input("Which Musician:"),))
	contact.commit()

def data_deleteOne():
    index.execute("DELETE FROM music_player WHERE Musician=?",(input("Which Musician Do you want to delete: "),))
    contact.commit()
    
def data_deleteAll():
    index.execute("DELETE FROM data_base")
    contact.commit()

while True:

	choice = int(input("""
		~Spotify.com~	
1. Add Musician;
2. Get Info About Musicians;
3. Get Info About One;
4. Update Informations;
5. Delete All Musicians;
6. Delete Only Selected Musician.
0. Exit/Goodbye
Choose: """))
	if choice == 1:
		musician = input("Musician: ")
		music = input("Music: ")
		duration = input(f"Duration of {music}[min]: ")
		size = input("Size[mb]: ")
		album = input("Album: ")
		print("Added Successfully!")
		add_info(musician,music,duration,size,album)
	elif choice == 2:
		get_all()
	elif choice == 3:
		data_getOne()
	elif choice == 4:
		tanlov = int(input("""1. Update Music;
2. Update Duration Time;
3. Update Size;
4. Update Album.
Chooose: """))
		if tanlov == 1:
			print("Music has been Updated!")
		elif tanlov == 2:
			update_duration()
			print("Duration Time has been Updated!")
		elif tanlov == 3:
			update_size()
			print("Size has been Updated!")
		elif tanlov == 4:
			update_album() 
			print("Album has been Updated!")
	elif choice == 5:
		data_deleteAll()
	elif choice == 6:
		data_deleteOne()
	elif choice == 0:
		print("See you soon!")
		break
contact.close()





