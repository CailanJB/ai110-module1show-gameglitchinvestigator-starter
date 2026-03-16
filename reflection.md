# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
. I expected the game to say I got a guess correct, and if guessed wrong the hints would be correct. However, when running the game my first guess was 7 and it said go lower but the correct answer was actaully 89. In addition when I ran the game for a second time the secret number kept changing after every guess. When the game finsihed, I tried to start a new game by clicking the new game button but nothing happened. 
- List at least two concrete bugs you noticed at the start  
  . I expected the hints to be accurate based on my guesses. After guessing the hints were saying go lower but the correct answer was a higher number than my guesses. 
  .After a game over, when trying to start a new game nothing occurs and no new game is started. 
  (for example: "the secret number kept changing" or "the hints were backwards").
  . At the start the attempts the diffculty gives does not match the attemps we have. For example easy difficulyt gives 6 attemps but when guessing we only get 5 attempts. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
. I used Copilot for this project specifcally the agent mode and ask mode. I used the ask mode to pinpoint bugs I could not find especialy with the secret number logic. Then used agent mode to add test or refactor code. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One example of an AI suggestion that was correct was for the hints logic. Specifically the "go higher" and "go lower: logic. The AI suggested swapping the results for each branch. the "go higher" would be under if g < secret and "go lower" should be prompted when the guess is higher than the secret number. I verfied this change by asking AI to make test and verifcying the test passed. I also went into the game UI myself and used differnt inputs to make sure the changes worked. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
An AI suggestion that was incorrect was when trying to fix the attempts bug. I wanted the to fix the bug where the attempts for a diffculty didnt match the amount of attempts the game actually gave. AI suggested that there wa sno error in the code but I still wasnt getting the correct amount of attempts when playing the game. I realzied the issue was the attempts at the start of the game was set to 1 instead of 0 when the game started so i changed it manually.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
. I asked copilot to make pytest testing my new changes then verifying these changes work. I also ran the game again and verified the new changes worked and the game runs as intended. 
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
- I ran a test to make sure the hints were working correctly. For example for the go higher hint I ran a test with secret number being 50 and a guess being 60 to make sure the output was too high for the user. I also ran a test making sure the user was attempting the correct number of times for each diffculty by manually going into the game using different inputs for each difficulty. 
- Did AI help you design or understand any tests? How?
. I asked AI to design my test for my bug fixes and asked to explain what exactly was being tested. For example for the secret number test I didn't understand states and streamlit so when it fixed the bug beofre asking what was fixed I asked for an overview on state space and streamlit. After that I then asked how the bug was fixed which helped my understanding. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
. The secret number kept changing because it was being reassigned a new value after every guess, instead of being initiaized to one value at the beggining of the game. 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
"Reruns" happen eveyr time a user interacts with the app and reruns the code from top to bottom. Session state is a feature that allows variables to keep their state accross all reruns. 
- What change did you make that finally gave the game a stable secret number?
Checking if the secret number wasnt in the session sate before assinging a random value. This ensured that the secret is set only once at the start of the game when the state was empty. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
. Getting used to making meanigful commit messages. In the past my commit messages werent really helpful but getting into the habit of commiting frequently allowed me to pinpoint previosu bugs. In addition, putting #FIX comments above code where there is a bug that got fixed and saying how it got fixed. 
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
One thing I would do differently next time working with AI is to have the AI make more test. Rather than testing the code myself my playing the game using AI to make better test can provide more assurance to the changes made. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project allowed me to see how AI is used as a teamate rather than doing all the work. I saw how AI made redundant task fatser but I was still in control with my thoughts and ideas while debugging. 
