def checkAgainstRules(update, rules):
    # check each rule against the update
    applicableRules = [x for x in rules if set(x).issubset(update)]
    allRulesCorrect = True
    incorrectRules = []

    for rule in applicableRules:
        # first number must come before second
        rulesCorrect = (update.index(rule[0]) < update.index(rule[1]))

        if not rulesCorrect:
            incorrectRules.append(rule)
            allRulesCorrect = False
    
    return allRulesCorrect, incorrectRules



f = open("input/5.txt", "r")

rules = []
correctUpdateTotal = 0
fixedUpdateTotal = 0

# parse the file
for line in f:
    if '|' in line:
        rule = [int(x) for x in line.strip().split('|') if x.isdigit()]
        rules.append(rule)

    elif ',' in line:
       # it's an update
        update = [int(x) for x in line.strip().split(',') if x.isdigit()]
        
        # check each rule against the update
        isCorrect, incorrectRules = checkAgainstRules(update, rules)
        
        if isCorrect:
            # get the middle number and add it to the total
            correctUpdateTotal += update[len(update) // 2]
        else:
            # we can fix it!
            isFixed = False
            while not isFixed:
                # swap things around until it works??
                # take first rule and then run again
                i1 = update.index(incorrectRules[0][0])
                i2 = update.index(incorrectRules[0][1])

                # multiple assignment feels gross and weird
                update[i1], update[i2] = update[i2], update[i1]

                isFixed, incorrectRules = checkAgainstRules(update, rules)
            
            # should be fixed here?
            fixedUpdateTotal += update[len(update) // 2]
            print(update)
                

print(correctUpdateTotal)
print(fixedUpdateTotal)

