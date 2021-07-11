#Problem 2 (Challenge): Score of best 75% days
#The same question as previously, however, we only take your best 75% days to account for sick
#days. No one is ever healthy every day. That means that even if #they didn’t get every question
#correct, as long as they got 75% of the questions correct, they will get 100%. See the example
#outputs below.
#Write a function that produces your final score as a percentage given:
#● total: the number of quizzes
#● correct: the number of quizzes you correctly answered
#● wrong: the number of quizzes you answered incorrectly.

def score75(total, correct, wrong):
  newTotal = total * 2 * 0.75
  correctPoint = correct * 2
  wrongPoint = min(total * 0.75 - correct, wrong)
  finalPoint = correctPoint + wrongPoint
  return min(finalPoint / newTotal, 1) * 100

print(score75(20,15,0))
print(score75(20,15,5))
print(score75(20,10,5))
print(score75(20,0,20))