import random

# Expanded lists of words (vocabulary)
nouns = [
    "pizza", "pasta", "cat", "dog", "car", "book", "movie", "music", 
    "restaurant", "beach", "idea", "friend", "journey", "house", "city", "universe", "phone", 
    "bicycle", "game", "television", "computer", "chair", "table", "window", "door", "school", "work",
    "airport", "mountain", "forest", "river", "sky", "sun", "moon", "earth", "space", "star", "tree",
    "cloud", "island", "desert", "plane", "train", "bus", "hotel", "hospital", "market", "store"
]

# Verbs (Common actions, states, and processes)
verbs = {
    "action": ["eat", "like", "play", "run", "work", "travel", "study", "cook", "help", "build", "drive"],
    "mental": ["think", "believe", "imagine", "understand", "learn", "talk"],
    "movement": ["walk", "run", "jump", "dance", "swim", "fly"],
    "communication": ["speak", "ask", "answer", "tell", "call", "listen"],
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
adverbs = {
    "action": ["quickly", "happily", "silently", "eagerly", "gracefully", "badly"],
    "communication": ["loudly", "quietly", "carefully", "easily"],
    "time": ["now", "soon", "always", "never", "sometimes", "today", "tonight"],
}

# Pronouns (Subject, Object, Possessive)
pronouns = ["I", "you", "he", "she", "it", "we", "they"]

# Time-related adverbs
time_adverbs = ["tomorrow", "next week", "soon", "already", "yet", "today", "tonight", "never", "always", "sometimes"]

# Word probabilities (Frequency or likelihood of a word being selected)
word_probabilities = {
    "nouns": { 
        "pizza": 0.1, "pasta": 0.08, "cat": 0.15, "dog": 0.2, "car": 0.12, "book": 0.07, 
        "movie": 0.05, "music": 0.1, "restaurant": 0.05, "beach": 0.08
    },
    "verbs": {
        "eat": 0.1, "like": 0.15, "play": 0.08, "run": 0.05, "work": 0.05, 
        "travel": 0.05, "study": 0.05, "cook": 0.05, "help": 0.05, "build": 0.05, 
        "drive": 0.05
    },
    "adjectives": {
        "delicious": 0.15, "funny": 0.08, "beautiful": 0.1, "fast": 0.08, 
        "spicy": 0.05, "interesting": 0.1, "huge": 0.08, "small": 0.1, 
        "amazing": 0.1, "horrible": 0.05
    },
    "adverbs": {
        "quickly": 0.12, "happily": 0.1, "loudly": 0.05, "carefully": 0.07, 
        "silently": 0.08, "eagerly": 0.05, "well": 0.1, "badly": 0.07
    },
    "pronouns": {
        "I": 0.1, "you": 0.1, "he": 0.1, "she": 0.1, "it": 0.1, "we": 0.1, "they": 0.1
    }
}

# Helper function to select a word based on its probability distribution
def weighted_random_choice(word_list, word_category_probs):
    probabilities = [word_category_probs.get(word, 0) for word in word_list]  # Safe get for missing words
    total = sum(probabilities)
    if total == 0:
        return random.choice(word_list)  # Fallback to random choice if no probabilities found
    normalized_probs = [p / total for p in probabilities]
    
    return random.choices(word_list, normalized_probs, k=1)[0]

# Helper function to generate a sentence with weighted selection
def generate_sentence(tense="present"):
    subject = weighted_random_choice(pronouns, word_probabilities["pronouns"])
    
    # Select verb based on context (e.g., only certain verbs with specific nouns)
    verb_category = "action"  # Assume a default category for simplicity (can expand logic here)
    verb = weighted_random_choice(verbs[verb_category], word_probabilities["verbs"])
    
    # Adjust verb selection for context (e.g., only suitable verbs for food like "eat" or "enjoy")
    obj = weighted_random_choice(nouns, word_probabilities["nouns"])
    
    # Ensure the sentence makes sense (e.g., "run" doesn't work with a "book" or "pasta")
    while (verb == "run" and obj not in ["dog", "cat", "bicycle"]) or \
          (verb == "eat" and obj not in ["pizza", "pasta", "food"]):
        obj = weighted_random_choice(nouns, word_probabilities["nouns"])
    
    # Select adjective
    adj = weighted_random_choice(adjectives, word_probabilities["adjectives"])
    
    # Select adverb based on context (e.g., "loudly" is not suitable for food items like "pasta")
    if obj in ["pizza", "pasta", "food"]:
        adv = weighted_random_choice(adverbs["action"], word_probabilities["adverbs"])
    else:
        adv = weighted_random_choice(adverbs["communication"], word_probabilities["adverbs"])
    
    # Time-related adverb
    time = weighted_random_choice(time_adverbs, word_probabilities["adverbs"])

    # Adjust verb tense based on subject
    verb = correct_verb_agreement(subject, verb, tense)
    
    # Construct sentence using a more natural structure
    sentence = f"{subject} {verb} {adj} {obj} {adv} {time}."
    return sentence

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
            # Add more verb agreements as needed
    return verb

# Start conversation and interact
def start_conversation():
    print("Hello! Ask me anything.")
    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break
        response = generate_sentence()
        print(f"Model: {response}")

if __name__ == "__main__":
    start_conversation()
