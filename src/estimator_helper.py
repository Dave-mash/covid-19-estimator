estimate = {
	'data': {},
	'impact': {},
	'severeImpact': {}
}

def estimator_helper(data):
	estimate['impact']['currentlyInfected'] = data['reportedCases'] * 10
	estimate['impact']['infectionsByRequestedTime'] = int(estimate['impact']['currentlyInfected'] * (2 ** 9))
	estimate['severeImpact']['currentlyInfected'] = data['reportedCases'] * 50
	estimate['severeImpact']['infectionsByRequestedTime'] = int(estimate['severeImpact']['currentlyInfected'] * (2 ** 9))
	
	return estimate

