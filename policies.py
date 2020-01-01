class policies_enacted:

  def check_policies(self):
    print("What policies would you like to check on?")
    policies_check = str(input())
    if policies_check == "Jail":
      print("Jail polices: Medium guard weapons, Security cams and Tvs, Medium treatment of prisoners.")
      print("Would you like to change any of them?")
      change_policies = str(input())
      if change_policies == "Yes":
        print("Which one?")
        jail_change = str(input())
        if jail_change == "Medium guard weapons":
          print("Change to low or high?")
          weapon_jail = str(input())
          if weapon_jail == "High":
