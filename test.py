from textblob import TextBlob
feed1="She is a good girl."
feed2="She is a very good girl."
blob1=TextBlob(feed1)
blob2=TextBlob(feed2)
print(blob1.sentiment)
print(blob2.sentiment)
