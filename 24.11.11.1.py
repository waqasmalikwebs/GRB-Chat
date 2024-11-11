import random

# Expanded lists of words (vocabulary)

# Nouns (Objects, people, places, things)
nouns = [
    "pizza", "pasta", "cat", "dog", "car", "book", "movie", "music", 
    "restaurant", "beach", "idea", "friend", "journey", "house", "city", "universe", "phone", 
    "bicycle", "game", "television", "computer", "chair", "table", "window", "door", "school", "work",
    "airport", "mountain", "forest", "river", "sky", "sun", "moon", "earth", "space", "star", "tree",
    "cloud", "beach", "island", "desert", "plane", "train", "bus", "hotel", "hospital", "market", "store"
]

# Verbs (Common actions, states, and processes)
verbs = [
    "eat", "like", "play", "watch", "read", "run", "love", "enjoy", 
    "believe", "think", "study", "travel", "write", "cook", "imagine", "explore", "dance", "sleep",
    "work", "live", "talk", "walk", "see", "hear", "feel", "understand", "believe", "want", "need",
    "buy", "sell", "help", "study", "teach", "give", "take", "call", "answer", "open", "close", "ask",
    "listen", "speak", "wait", "find", "lose", "create", "build", "jump", "run", "drive", "sing", "speak",
    "look", "smile", "laugh", "cry", "shine", "change", "write", "hear", "think", "belong", "believe"
]

# Phrasal verbs (Verb + Particle Combinations)
phrasal_verbs = {
    "look": ["look up", "look after", "look into", "look forward to", "look out for", "look down on"],
    "turn": ["turn on", "turn off", "turn up", "turn down", "turn around", "turn back"],
    "get": ["get up", "get out", "get in", "get off", "get back", "get over", "get along"],
    "give": ["give up", "give in", "give out", "give away", "give off", "give back"],
    "run": ["run into", "run out of", "run over", "run away", "run after", "run down"],
    "take": ["take off", "take in", "take up", "take over", "take after", "take back"],
    "bring": ["bring up", "bring about", "bring in", "bring back", "bring on", "bring together"],
    "put": ["put off", "put up with", "put away", "put on", "put out", "put down"],
    "break": ["break down", "break up", "break into", "break out", "break through", "break away"]
}

# Adjectives (Descriptive words)
adjectives = [
    "delicious", "funny", "beautiful", "fast", "spicy", "interesting", 
    "huge", "small", "old", "new", "amazing", "horrible", "dark", "bright", "colorful", "fantastic", 
    "good", "bad", "nice", "terrible", "soft", "hard", "sweet", "bitter", "hot", "cold", "warm", "dry",
    "wet", "loud", "quiet", "bright", "sharp", "smooth", "rough", "rich", "poor", "strong", "weak",
    "happy", "sad", "exciting", "boring", "dangerous", "safe", "gentle", "rough", "young", "old"
]

# Adverbs (Words that modify verbs, adjectives, or other adverbs)
adverbs = [
    "quickly", "happily", "loudly", "carefully", "silently", "eagerly", 
    "gracefully", "well", "badly", "usually", "never", "sometimes", "almost", "constantly", "too", 
    "really", "extremely", "quite", "probably", "definitely", "absolutely", "just", "almost", "only"
]

# Pronouns (Subject, Object, Possessive)
pronouns = ["I", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them", "my", "your", 
            "his", "her", "its", "our", "their"]

# Prepositions (Words that show relationships between objects)
prepositions = ["in", "on", "at", "with", "by", "under", "over", "between", "around", "through", "along", 
                "beside", "below", "above", "near", "behind", "in front of", "out of", "into", "during", "before"]

# Conjunctions (Words that connect clauses or sentences)
conjunctions = ["and", "but", "or", "because", "so", "although", "yet", "if", "unless", "while", "when", "until"]

# Determiners (Words that modify nouns)
determiners = ["a", "an", "the", "this", "that", "these", "those", "some", "any", "many", "few", "most", "all", 
               "both", "each", "either", "neither", "every", "much", "more", "less"]

# Interjections (Words used to express emotions or reactions)
interjections = ["wow", "ouch", "hey", "uh", "oh", "ah", "hmm", "oops", "wow", "hey", "oops", "yay", "phew"]

# Question Words
question_words = ["What", "How", "Why", "Where", "Who", "When", "Which", "Whose", "How much", "How many"]

# Time-related adverbs
time_adverbs = ["tomorrow", "next week", "soon", "already", "yet", "today", "tonight", "never", "always", "sometimes"]

# Helper function to ensure subject-verb agreement
def correct_verb_agreement(subject, verb, tense="present"):
    if tense == "present":
        if subject in ["I", "you", "we", "they"]:
            return verb
        elif subject in ["he", "she", "it"]:
            if verb == "eat":
                return "eats"
            elif verb == "play":
                return "plays"
            elif verb == "run":
                return "runs"
            else:
                return verb + "s"
    elif tense == "past":
        if verb == "eat":
            return "ate"
        elif verb == "run":
            return "ran"
        else:
            return verb + "ed"  # Assume regular verbs
    elif tense == "future":
        return "will " + verb  # Future tense

    return verb

# Helper functions for sentence construction

def generate_subject():
    return random.choice(pronouns)

def generate_verb():
    return random.choice(verbs)

def generate_phrasal_verb():
    verb = random.choice(list(phrasal_verbs.keys()))
    phrasal_verb = random.choice(phrasal_verbs[verb])
    return phrasal_verb

def generate_object():
    return random.choice(nouns)

def generate_adjective():
    return random.choice(adjectives)

def generate_adverb():
    return random.choice(adverbs)

def generate_preposition():
    return random.choice(prepositions)

def generate_conjunction():
    return random.choice(conjunctions)

def generate_question_word():
    return random.choice(question_words)

def generate_time_adverb():
    return random.choice(time_adverbs)

# Generate a complex sentence with modifiers, adjectives, and adverbs
def generate_complex_sentence(tense="present"):
    subject = generate_subject()
    verb = generate_verb()
    obj = generate_object()
    adj = generate_adjective()
    adv = generate_adverb()
    time = generate_time_adverb()

    verb = correct_verb_agreement(subject, verb, tense)
    sentence = f"{subject} {verb} {adj} {obj} {adv} {time}."
    return sentence

# Generate a sentence using a phrasal verb
def generate_phrasal_verb_sentence(tense="present"):
    subject = generate_subject()
    verb = generate_phrasal_verb()
    obj = generate_object()
    adj = generate_adjective()
    adv = generate_adverb()
    time = generate_time_adverb()

    sentence = f"{subject} {verb} {adj} {obj} {adv} {time}."
    return sentence

# Generate a question using phrasal verbs
def generate_phrasal_verb_question():
    question_word = generate_question_word()
    verb = generate_phrasal_verb()
    obj = generate_object()
    return f"{question_word} did you {verb} {obj}?"

# Start conversation and interact
def start_conversation():
    print("Hello! Ask me anything.")
    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break
        tone = "casual"  # Default tone, can be adjusted based on user preference
        if "please" in question or "kindly" in question:
            tone = "formal"
        response = generate_phrasal_verb_sentence()
        print(f"Model: {response}")

if __name__ == "__main__":
    start_conversation()
