# Quizzer

Quizzer is Python app that helps you to memorize foreign language words easier (or any arbitrary key value pair)
It supports unicode characters and so it can be used to learn asian languages

## Usage

First you need to install Python 3
Then you need to install dependencies
`pip install -r requirements.txt`
and you can finally run the app
`python quizzer.py dictionary.txt`
where `dictionary.txt` is your dictionary you want to learn

When you run Quizzer it will give you random questions from dictionary
If you answer incorrectly it will show you correct answer
After each question Quizzer will show you scores (score of current question, max and sum of all scores)
Score lowers when you answer correctly and increases when you made a mistake
Random question selection uses weighted random and will prioritize words that have higher score
Scores are saved between runs of the program (when you exit with Ctrl+C) in folder called `saved` next to your dictionary file

## Creating dictionary

To create your dictionary put your words in following format:
```
word1 - translation1
word2 - translation2
word3 - translation3
...
```
e.g.
```
にほん - Japan
たべもの - Food
ねこ - Cat
```
Note that all lines must have exactly one hyphen `-` or be empty