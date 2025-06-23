# Problem
# - A disease affets 1% of a population
# - A test is 95% accurate for diseased individuals & 90% accurate for non-diseased individuals
# - Find the probability of having the disease given a positive test result

def bayes_theorem(pior, sensitivity, specificity):
  evidence = (sensitivity * prior) + ((1-specificity) * (1-prior))
  posterior = (sensitivity * prior) / evidence
  return posterior


#
prior = 0.01 # 1% prevalence
sensitivity = 0.95 # True positive rate
specificity = 0.90 # True negative rate

posterior = bayes_theorem(prior, sensitivity, specificity)
print("Probability of Disease Given Positive Results: ", posterior)
