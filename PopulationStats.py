from PopulationGroup import PopulationGroup

class PopulationStats():

  def population_percentages(self):
    groups = ['Liberal', 'Capitalist', 'Conservative', 'Environmentalists', 'Poor', 'Elite', 'Motorists', 'Democrat', 'Republican']

    percentages = [20, 60, 20, 80, 30, 20, 10, 70, 40, 60]

    approvals = [5, 15, 2, 15, 10, 5, 8, 10, 10, 10]

    self.group_stats = [
        PopulationGroup(groups[i], percentages[i], approvals[i]) for i in range(len(groups)) 
    ]

    for i in 
    print(f"Population: {self.beliefs}")
