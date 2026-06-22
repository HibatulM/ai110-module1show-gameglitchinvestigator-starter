# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1. The game gave incorrect hints when the user guessed a number. Even when the user gussed the highest number in the range the hint was to enter a higher number. 
2. It showed the incorrect score to the user. The user score was 0 but the game showed that the user's score was 5 
3. The new game doesn't reset everything and new inputs are not registered. 
4. The new game doesn't do anything even after winning the game, as in hints don't appear and the winning or losing message doesn't go away after the game ends, though the new game feature works if the user has not won 
5. Gives Negative score when guessed correctly 
6. Difficulty not accurately represented with the number of attempts 



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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?: For this project I used Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). : The AI correctly identified the logic error that was causing the score error and fixed it. I verified this manually by playing the game and checking the score 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result): The new game button did not work as expected and the AI's suggestion was the just change the st.session_state.status = playing but this was misleading because we need to verify if the user has clicked on new game to reset the state 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?: I tested features manually and tested some functions for intended outputs using pytests.
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.: I tested check_guess by using AI to write tests that tested a variety of inputs by users. It showed when the tests were failing that I needed to fix the buggy code
- Did AI help you design or understand any tests? How?: I used AI to help write the automatated tests for functions that dealed with data that passed through functions. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit runs the new code everytime there is a file change and the session states change according to the user so we can start a clean slate whenever the user wants and we don't have to do anything manually

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I want to keep the habit of opening different instances for different parts of the code so the AI is not confused
- What is one thing you would do differently next time you work with AI on a coding task?
  I would start a new chat session for minor changes and for commiting to github instead of doing it manually 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  I used to think AI could only be used to fix minor issues but now I can use AI to diagnose and even explain the code to me so I can reduce the time it takes to comb through the code to understand the logic and fix it
