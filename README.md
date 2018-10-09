#PoeFlipBot

main.py
-will manage threads and function calls within them (webscraping loop, etc), handles the listing/buying of currency. This file will make calls to all other files asking for information: image comparison, what is the best currency to trade (marketManager), who are we about to trade with, and will initiate the trades using this.

chat.py
-scans chat, looks for trades, controls functions for sending messages, logs username of pending trades, etc
inventory.py
-keeps track of all currency owned, contains functions for controls regarding item movement, etc

imageRecognition.py
-compares images to detect what kind of currency is in the slot asked, relays this info to inventory.py

webscraper.py
-scrapes currency.poe.trade for data between currencies, calculates profit margins, relays this information to marketManager.py

marketManager.py
-takes in the data from webscraper and will do the heavy lifting of mathematical comparisons, trend detection, etc. Relays which trades it needs to perform to main.py

general.py
-generic low-level set of functions for widespread use among many files

~ ~ ~ ~ ~ ~ ~
Current Tasks:


==Nathan==
webscraper.py & variables for marketManager- reference above. store all scraped information collected in webscraper as variables that can be manipulated later in marketManager

==Justin==
imageRecognition.py- reference above for information. We want it to do this: https://stackoverflow.com/questions/35205565/capture-screen-and-find-reference-image

~ ~ ~ ~ ~ ~ ~
NOTE:
building a higher level class like imageRecognition may require some ease-of-use low level functions to be made in the lower level classes like general.py or even chat.py (ex: the addition of leftClick() method) - be sure to note these function additions in the commit descriptions along with whatever edits you do to the bigger classes


-------------------
-POE CURRENCY ID's-
-------------------
1 alteration
2 fusing
3 alchemy
4 chaos
5 gemcutters
6 exalted
7 chroma
8 jewellers
9 chance
10 chisel
11 scour
12 blessed
13 regret
14 regal
15 divine
16 vaal
17 wisdom scroll
18 portal scroll
19 armourer's
20 whetstone
21 glassblowers
22 transmutes
23 augmentation
24 mirror
25 eternal
26 perandus coin
27 silver coin
//etc
