# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1. The game gave incorrect hints when the user guessed a number. Even when the user gussed the highest number in the range the hint was to enter a higher number. *fix it*
2. It showed the incorrect score to the user. The user score was 0 but the game showed that the user's score was 5 *fix it*
3. The new game doesn't reset everything and new inputs are not registered. *fix it*
4. The input bar says to enter to submit the guess but pressing enter doesn't do anything.
5. The new game doesn't do anything even after winning the game, as in hints don't appear and the winning or losing message doesn't go away after the game ends, though the new game feature works if the user has not won 
6. Gives Negative score when guessed correctly 
7. Difficulty not accurately represented 


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 50 | Hint Shows to guess lower| Hint Shows to guess igher| No Console Output |
| 20 | Hint shows to guess higher| Hint Shows to guess lower | No Consoloe Output| 
| New Game + New Guess  |  Hint appears, win message goes away| Win Message still there, input not recorded | No Console Output|
| Toggle the Show Hint | Hint hides when the show hint is toggled off and hint shows the the show hint is toggled on | Hint hides after show toggled is off but toggle it on doesn't make the hint show up again| No Console Output| 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
