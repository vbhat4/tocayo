import pandas as pd

evidenceList = ["strong", "moderate"]
classificationList = ["P/LP", "B/LB"]
classificationList_v2 = ["plp", "blb"]

for evidence in evidenceList:

	for i in range(len(classificationList)):

		clas = classificationList[i]
		clas_v2 = classificationList_v2[i]
		
		cvDf = pd.read_csv(f"/net/data/aasubs/dbnsfp_catalog/{evidence}_cv_potential_entries.csv")
		dbDf = pd.read_csv(f"/net/data/aasubs/dbnsfp_catalog/{evidence}_cv_potential_entries.csv")
		
		dbDf["aa_sub_name"] = cvDf["aa_sub_name"]
		
		

		df = pd.read_csv(f"/net/data/aasubs/dbnsfp_catalog/filtered/{evidence}_filtered_potential_entries_full.csv")

		df = df[df["cv_simple_annot"] == clas]

		df.to_csv(f"/net/data/aasubs/dbnsfp_catalog/classified/dbnsfp_{evidence}_{clas_v2}_analysis.csv")