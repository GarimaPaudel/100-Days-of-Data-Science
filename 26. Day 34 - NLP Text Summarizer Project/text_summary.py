import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """As we journey deeper into space, it is essential to remember that our planet, the Earth,
 is a unique and precious oasis in the vast cosmos.
 Space exploration not only expands our understanding of the universe but also reminds us of the fragility of our own home.
 The insights we gain from space exploration can inform our efforts to protect and preserve the Earth for future generations.

In conclusion, space exploration is an endeavor that unites humanity in the pursuit of knowledge,
 adventure, and the quest to reach the stars. From the early days of the space race to the collaborative
   efforts of the International Space Station and the pioneering spirit of private space companies,
 our journey into space continues to inspire and push the boundaries of what is possible.
 The universe is vast, and our potential is limitless; it's a journey that promises to be as breathtaking 
 as the stars themselves."""

# Function to summarize text
def summarizer(rawdocs):
    
    # Create a list of stopwords 
    stopwords = list(STOP_WORDS)
    #print(stopwords)

    # Load spaCy and English language model
    nlp = spacy.load('en_core_web_sm')

    # Tokenize the input text
    doc = nlp(text)
    #print(doc)

    tokens = [token.text for token in doc]
    #print(tokens)

 # Calculate word frequency
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] +=1

    #print(word_freq)

 # Find the maximum word frequency
    max_freq = max(word_freq.values())
    #print(max_freq)

    #calculation of normalized frequency of each word
    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq

    #print(word_freq)

  # Tokenize the text into sentences
    sent_tokens = [sent for sent in doc.sents]
    #print(sent_tokens)


    # Calculate sentence scores based on word frequency
    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]
    #print(sent_scores)

    #30 percent length
    select_len = int(len(sent_tokens)*0.3)
    #print(select_len)

    summary = nlargest(select_len, sent_scores, key = sent_scores.get)
    #print(summary)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    #print(text)
    #print(summary)
    #print("Length of original text ", len(text.split(' ')))
    print("Length of summary text ", len(summary.split(' ')))

    return summary, doc, len(rawdocs.split(' ')), len(summary.split(' '))