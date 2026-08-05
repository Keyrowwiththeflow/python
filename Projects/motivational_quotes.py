# This script provides a collection of motivational quotes that can be used to inspire and uplift the user.
# The quotes are stored in a list and can be accessed randomly to provide motivation whenever needed.
# There will be multiple classes of quotes: Resilience/Persistence, Change/Growth, Life, Connection, Optimism, Gratitude, Mindfulness. Maybe more in the future.
import random 

resilience_and_persistence_quotes = [
    "\"Persistence and resilience only come from having been given the chance to work through difficult problems\" - \033[3mGever Tulley\033[0m",
    "\"It does not matter how slowly you go as long as you do not stop.\" - \033[3mConfucius\033[0m",
    "\"Success is not final, failure is not fatal: It is the courage to continue that counts.\" - \033[3mWinston Churchill\033[0m",
    "\"The greatest glory in living lies not in never falling, but in rising every time we fall.\" - \033[3mNelson Mandela\033[0m",
    "\"Fall seven times and stand up eight.\" - Japanese Proverb",
    "\"Our greatest glory is not in never failing, but in rising every time we fail.\" - \033[3mConfucius\033[0m",
    "\"It always seems impossible until it's done.\" - \033[3mNelson Mandela\033[0m",
    "\"Perseverance is not a long race; it is many short races one after the other.\" - \033[3mWalter Elliot\033[0m",
    "\"The only way to achieve the impossible is to believe it is possible.\" - \033[3mCharles Kingsleigh\033[0m",
    "\"Do not judge me by my success, judge me by how many times I fell and got back up again.\" - \033[3mNelson Mandela\033[0m",
    "\"The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack in will.\" - \033[3mVince Lombardi\033[0m",
    "\"Be yourself; everyone else is already taken.\" - \033[3mOscar Wilde\033[0m",
    "\"In the middle of every difficulty lies opportunity.\" - \033[3mAlbert Einstein\033[0m",
    "\"Watch your thoughts; they become words. Watch your words; they become actions. Watch your actions; they become habits. Watch your habits; they become character. Watch your character; it becomes your destiny.\" - \033[3mLao Tzu\033[0m",
    "\"Do not wait to strike till the iron is hot; but make it hot by striking.\" - \033[3mWilliam Butler Yeats\033[0m",
    "\"All dreams are within reach. All you have to do is keeping moving towards them.\" - \033[3mViola Davis\033[0m",
    "\"The best way to predict the future is to create it.\" - \033[3mPeter Drucker\033[0m",
    "\"Do what you can, with what you have, where you are.\" - \033[3mTheodore Roosevelt\033[0m",
    "\"The only limit to our realization of tomorrow will be our doubts of today.\" - \033[3mFranklin D. Roosevelt\033[0m",
    "\"The future belongs to those who believe in the beauty of their dreams.\" - \033[3mEleanor Roosevelt\033[0m",
    "\"Do not go where the path may lead, go instead where there is no path and leave a trail.\" - \033[3mRalph Waldo Emerson\033[0m"
]

change_and_growth_quotes = [
    "\"The only way to make sense out of change is to plunge into it, move with it, and join the dance.\" - \033[3mAlan Watts\033[0m",
    "\"Change is the law of life. And those who look only to the past or present are certain to miss the future.\" - \033[3mJohn F. Kennedy\033[0m",
    "\"Growth is the only evidence of life.\" - \033[3mJohn Henry Newman\033[0m",
    "\"The measure of intelligence is the ability to change.\" - \033[3mAlbert Einstein\033[0m",
    "\"Progress is impossible without change, and those who cannot change their minds cannot change anything.\" - \033[3mGeorge Bernard Shaw\033[0m",
    "\"Change is inevitable. Growth is optional.\" - \033[3mJohn C. Maxwell\033[0m",
    "\"Embrace change, for it is the only constant in life.\" - \033[3mHeraclitus\033[0m",
    "\"The secret of change is to focus all of your energy, not on fighting the old, but on building the new.\" - \033[3mSocrates\033[0m",
    "\"Change the way you look at things and the things you look at change.\" - \033[3mWayne Dyer\033[0m",
    "\"If you want to change attitudes, start with a change in behavior.\" - \033[3mWilliam Glasser\033[0m",
    "\"Not everything that is faced can be changed, but nothing can be changed until it is faced.\" - \033[3mJames Baldwin\033[0m",
    "\"Life is about how much you can take and keep fighting, how much you can suffer and keep moving forward.\" - \033[3mAnderson Silva\033[0m",
    "\"In any given moment, we have two options: to step forward into growth or to step back into safety.\" - \033[3mAbraham Maslow\033[0m",
    "\"Whatever makes you uncomfortable is your biggest opportunity for growth.\" - \033[3mBryang McGill\033[0m",
    "\"The only way to grow is to step out of your comfort zone.\" - \033[3mRoy T. Bennett\033[0m",
    "\"Life begins at the end of your comfort zone.\" - \033[3mNeale Donald Walsch\033[0m",
    "\"Change is the end result of all true learning.\" - \033[3mLeo Buscaglia\033[0m",
    "\"Transformation is not a future event. It is a present activity.\" - \033[3mJillian Michaels\033[0m",
    "\"It is not the strongest of the species that survive, nor the most intelligent, but the one most responsive to change.\" - \033[3mCharles Darwin\033[0m",
    "\"Incredible change happens in your life when you decide to take control of what you do have power over instead of craving control over what you don't.\" - \033[3mSteve Maraboli\033[0m"
]

print("What types of quotes would you like to see?")
print("""Type one of the following words: 
resilience/persistence 
change/growth
""")
user_input = input().lower()
if user_input == "resilience" or user_input == "persistence":
    print(random.choice(resilience_and_persistence_quotes))
elif user_input == "change" or user_input == "growth":
    print(random.choice(change_and_growth_quotes))
else:
   print("Invalid input. Please type one of the given words!")