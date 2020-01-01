
from policies import policies_enacted

print("Welcome to Goverment.You have been elected by the populus to lead the nation of Seytin.You may now begin your first year.")

def country_stats():
  unemployment = 40
  gdp = 4000
  deficit = 300
  health = 70
  education = 80
  print(f"GDP: {gdp}, Deficit: {deficit}, Health: {health}, Education: {education}, Unemployment {unemployment}")

country_stats()
current_population = Population()
current_population.population_percentages()
current_policies = policies_enacted()
current_policies.check_policies()