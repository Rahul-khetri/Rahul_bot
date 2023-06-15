import random

from telethon import TelegramClient, events

from .. import bot

# Jokes list

jokes = [

    "Why don't scientists trust atoms? Because they make up everything!",

    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",

    "I'm reading a book about anti-gravity. It's impossible to put down!",

    "Why don't skeletons fight each other? They don't have the guts!",

    "I used to play piano by ear, but now I use my hands.",

    "Why don't eggs tell jokes? Because they might crack up!",

    "Why did the scarecrow win an award? Because he was outstanding in his field!",

    "What do you call a bear with no teeth? A gummy bear!",

    "I asked the librarian if they had any books on paranoia. She whispered, They're right behind you!",

    "Why did the scarecrow win an award? Because he was outstanding in his field!",

    "How do you organize a space party? You planet!",

    "Whats brown and sticky? A stick!",

    "What do you call a snowman with a six-pack? An abdominal snowman!",

    "How do you make a tissue dance? You put a little boogie in it!",

    "Why don't eggs tell jokes? Because they might crack up!",

   

    "Why don't eggs tell jokes?Because they might crack up!",

    "What do you call a fake noodle?An impasta!",

    "How do you catch a squirrel?Climb a tree and act like a nut!",

    "Why did the tomato turn red?Because it saw the salad dressing!",

    "Why did the scarecrow win an award?Because he was outstanding in his field!",

    "What did one hat say to the other hat?You stay here, I'll go on ahead!",

    "Why don't scientists trust stairs?Because they're always up to something!",

    "What do you get if you cross a snowman and a vampire?Frostbite!",

    "Why did the golfer bring two pairs of pants?In case he got a hole in one!",

    "Why did the bicycle fall over?It was two-tired!",

    "Why don't ants get sick?Because they have little anty-bodies!",

    "How does a penguin build its house?Igloos it together!",

    "Why did the tomato turn red?Because it saw the salad dressing!",

    "Why did the scarecrow win an award?Because he was outstanding in his field!",

    "What did the grape say when it got stepped on?Nothing, it just let out a little wine!",

    "Why did the math book look sad?Because it had too many problems!",

    "What did the ocean say to the shore?Nothing, it just waved!",

    "Why did the chicken go to the seance?To talk to the other side!",

    "What do you call a bear with no teeth?A gummy bear"

    "Why did the couple go to therapy?Because they had too many loose ends in their relationship!",

    "What do you call two birds in love?Tweet-hearts!",

    "Why did the banana go out with the prune?Because it couldn't find a date!",

    "What did the grape say to the raisin? You raisin me up!",

    "Why do scientists say that love is like a chemical reaction?Because if you have the right elements, it's explosive!",

    "How did the telephone propose to its girlfriend?It gave her a ring!",

    "Why did the two birds break up?Because they had fowl play!",

    "What did one light bulb say to the other light bulb?I love you a watt!",

    "Why did the tomato turn red?Because it saw the salad dressing!",

    "How did the computer propose to its partner?It said, You're the apple of my i!",

    "Why did the calendar date the clock?Because they had great chemistry and always had good times together!",

    "What did the French chef give to his wife on Valentine's Day ? A moulin rouge bouquet!",

    "What did one magnet say to the other magnet?I'm attracted to you!",

    "How did the octopus express its love?With a big hug!",

    "Why did the girl bring a ladder to the bar?She heard the drinks were on the house!",

    "What did the paper clip say to the magnet?You're so attractive!",

    "Why did the bicycle fall in love with the motorcycle?It was wheel-y attracted to it!",

    "What did the flower say to its beloved bee?I bee-long with you!",

    "Why did the mathematician fall in love with the graph?Because they had perfect curves!",

  

    "तेरे प्यार में बहुत मजबूत हूँ।वाह, तेरी नस-नस में मेरे लिए क्या प्यार है!",

    "तुम्हारी आवाज़ सुनते ही मेरे दिल की धड़कन बढ़ जाती है।आच्छा, तो क्या मैं अब खामखा उल्टे दिल को धड़का दे रहा हूँ?",

    "तेरी हंसी मेरे दिल को बहुत प्यारी है।वाह, तो मैं ख़ास करके कमेडी शो में गया करूँ?",

  

    "जबसे तू मेरी जिंदगी में आई है, सब कुछ बदल गया है।हाँ, मैंने ब्रश करनी और नहाना छोड़ दिया है!",

    "तुम्हारे प्यार में मैं पागल हो गया हूँ।ओह, अच्छा! तो क्या अब तू मेरे खेत में चरमारे बै",

    "Why did the two lovers go to school together?Because they wanted to be in the same class!",

    "What did the ocean say to the beach?You shore are beautiful!",

    "Why did the tomato turn red?Because it saw the salad dressing!",

    "How do you make your girlfriend smile?Tell her a joke-lery!",

    "What did one light bulb say to the other light bulb?I love you a watt!",

    "How do you make a tissue dance?You put a little boogie in it!",

    "Why don't some couples go to the gym?Because some relationships don't work out!",

    "Why did the bicycle fall over?It was two-tired!",

    "Why don't oysters donate to charity?Because they are shellfish!",

  

    "जब जितना काम करना हो उतना काम करो, क्योंकि बाद में तुम्हें बड़ी सफलता मिलेगी और चुटकुले सुनाने का समय भी होगा!",

    "सपने देखने वाले लोगों को ही तो इंस्पिरेशन कहते हैं, और अन्य लोगों को वक्तपास कहते हैं",

    "दुनिया में सबसे सस्ता इंजीनियरिंग कैसे मिलता है?जब कोई इंजीनियर अपनी गर्लफ्रेंड के साथ रहता है, तब!",

    "जब तुम चलो तो सबका मुँह बंद हो जाए, क्योंकि तुम उनके लिए बिलकुल अजीब लगते हो!",

    "जिंदगी एक रेस नहीं है, जो खत्म हो जाएगी। यह एक यात्रा है, जो खुशियों से भरी होनी चाहिए।",

    "जब लोग तुम्हें नकारते हैं, तो समझो कि तुम दूसरों से आगे चल रहे हो। उन्हें बस पिछले डबरी में बचा रहना है!",

    "जब तक तुम खुद को नकारात्मक विचारों के जंजीरों में बंधे रखोगे, तुम कभी आगे नहीं बढ़ पाओगे। उठो और आगे बढ़ो!",

    "अगर तुम उठकर बहार देखोगे, तो तुम जानोगे कि सूरज ने आज भी जब नास्ता किया होगा तब जगमगाता है!",

    "जब तुम लोगों को जलाकर रखते हो, तो जानो कि तुम रोशनी का कारण बन चुके हो!"

    ]

# Command handler

@bot.on(events.NewMessage(pattern='/joke'))

async def handle_joke(event):

    chat = await event.get_chat()

    # Select a random joke

    joke = random.choice(jokes)

    # Send the joke as a message

    await event.reply(joke)
