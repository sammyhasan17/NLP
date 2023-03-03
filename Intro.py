#Sammy Hasan-Silva
# dependencies are below:

# !pip install gtts
# !pip install pyttsx3
# !pip install pyobjc # for macOS users only


from gtts import gTTS
import os

# Define the text to be spoken
text = "Hello, how are you doing today?"

# Initialize the gTTS object
tts = gTTS(text=text, lang='de')

# Save the audio file
tts.save("hello.mp3")

# Play the audio file
os.system("afplay hello.mp3")


# Language	Code	Voices

# Afrikaans	af	male, female
# Albanian	sq	male, female
# Amharic	am	male
# Arabic	ar	male, female
# Armenian	hy	male, female
# Azerbaijani	az	male
# Basque	eu	male
# Belarusian	be	male
# Bengali	bn	male, female
# Bosnian	bs	male
# Bulgarian	bg	male
# Burmese	my	male
# Catalan	ca	male
# Cebuano	ceb	male
# Chinese (Mandarin)	zh-cn	male, female
# Chinese (Cantonese)	zh-yue	male
# Croatian	hr	male
# Czech	cs	male
# Danish	da	male
# Dutch	nl	male, female
# English	en	male, female
# Esperanto	eo	male
# Estonian	et	male
# Filipino	tl	male
# Finnish	fi	male
# French	fr	male, female
# Galician	gl	male
# Georgian	ka	male
# German	de	male, female
# Greek	el	male
# Gujarati	gu	male
# Haitian Creole	ht	male
# Hausa	ha	male
# Hebrew	he	male
# Hindi	hi	male, female
# Hmong	hmn	male
# Hungarian	hu	male
# Icelandic	is	male
# Igbo	ig	male
# Indonesian	id	male
# Irish	ga	male
# Italian	it	male, female
# Japanese	ja	male, female
# Javanese	jw	male
# Kannada	kn	male
# Kazakh	kk	male
# Khmer	km	male
# Kinyarwanda	rw	male
# Korean	ko	male, female
# Kurdish	ku	male
# Kyrgyz	ky	male
# Lao	lo	male
# Latin	la	male
# Latvian	lv	male
# Lithuanian	lt	male
# Luxembourgish	lb	male
# Macedonian	mk	male
# Malagasy	mg	male
# Malay	ms	male
# Malayalam	ml	male
# Maltese	mt	male
# Maori	mi	male
# Marathi	mr	male
# Mongolian	mn	male
# Nepali	ne	male
# Norwegian	no	male
# Nyanja (Chichewa)	ny	male
# Odia (Oriya)	or	male
# Pashto	ps	male
# Persian	fa	male, female
# Polish	pl	male, female
# Portuguese	pt	male, female
# Punjabi	pa	male
# Romanian	ro	male
# Russian	ru	male, female
# Samoan	sm	male
# Scots Gaelic	gd	male
# Serbian	sr	male
# Sesotho	st	male
# Shona	sn	male
# Sindhi	sd	male
# Sinhala (Sinhalese)	si	male
# Slovak	sk	male
# Slovenian	sl	male
# Somali	so
# Spanish es
