import random

import praw

reddit = praw.Reddit(client_id='rJ21tUD_z8pmZQ',
                     client_secret='IXYfxM2cWbmVUaMxv86Zl0CM4WU',
                     username='GaaliBoy',
                     password='(*&^%$#@!',
                     user_agent='gaaliboy by /u/code_god')

subreddit = reddit.subreddit('chodi')

gaalilist = ["यभ","पायु","वेश्यासुताः","अनेकजनक","क्लीब","धूर्त","पिशाची","पापात्मन्","मूर्ख","शिश्नमस्तक","हदतिमस्तक","विजात"]
Egaalilist = ["Yabha!","Payu","Veshyasutah","Anekajanaka","Kliba","Dhurta","Pishachi","Papatman","Murkha","Shishramastaka","Hadatimastaka","Vijata"]
meaning = ["F*ck off!","Arsehole","Son of a b*tch","Not with a single dad","Impotent","Evil","Demon","Sinner","Fool","Dickhead","Shithead","Bastard"]
vgaali = ["समिध्","उदारवेश्या","वामपंथी सर्दिगृदि","साम्यवादि सर्दिगृदि"]
Evgaali = ["Samidh","Udaraveshya","Vamapanthi sardigrdi","Samyavadi sardigrdi"]
vmeaning = ["Faggot","Liberandu","Leftist cunt","Commie cunt"]
keyphrase = ["!gaali","!vgaali"]

for comment in subreddit.stream.comments():
	for i in keyphrase:
		if i in comment.body:
			if(i == "!gaali"):
				try:
					j = random.choice(range(len(gaalilist)))
					reply = "**" + gaalilist[j] +"**"+ "\n\nTranslation: " + "*"+ Egaalilist[j] + "*" + "\n\nMeaning: " + meaning[j]
					comment.reply(reply)
					print('posted')

				except:
					print('To frequent')

			else:
				try:
					j = random.choice(range(len(vgaali)))
					reply = "**" + vgaali[j] + "**" + "\n\nTranslation: " + "*" + Evgaali[j] + "*" + "\n\nMeaning: " +vmeaning[j]
					comment.reply(reply)
					print('posted')

				except Exception as e:
					print(e)
					print('To frequent')
		

