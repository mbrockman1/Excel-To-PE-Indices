# Excel To PE Indices
Functions for calculating PESI, sPESI, ESC, BOVA

Input is an excel spreadsheet with the following columns:

• MRN(int)\
• Age(int)\
• Sex(M or F)\
• Cancer(0 for No, 1 for Yes)\
• CHF_COPD(0 for Neither, 1 for COPD or CHF history, 2 for history of both)\
• Age(int)\
• SBP(int)\
• RR(int)\
• Temp(int)\
• SpO2(int)\
• TnI(float)\
• RV function(1 for no abnormalities, 2 for abnormalities) # will change to 0/1 compliance

Exports an excel sheet called "updated_data.xlsx" with results in following column

### TODO to start

Pandas is the only requirement
You need to change the INPUT_FILE line to satisfy your requirement.
