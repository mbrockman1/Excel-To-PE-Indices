def pesi_score(series):
    pesi = 0
    pesi += series['Age']
    if series['Sex'] == 'M':
        pesi += 10
    '''
    1 Malignancy, 2 COPD, 3 CHF
    '''
    if series['Cancer'] == 1:
        pesi += 30

    if series['CHF_COPD'] == 1:
        pesi += 10
        
    if series['CHF_COPD'] == 2:
        pesi += 20
        
    if series['HR'] > 109:
        pesi += 20
    
    if series['SBP'] < 100:
        pesi += 30
        
    if series['RR'] > 29:
        pesi += 20
        
    if series['Temp'] < 36:
        pesi += 20    
        
    if series['SpO2'] < 90:
        pesi += 20
        
    return(pesi)

def simple_pesi_score(series):
    pesi = 0
    if series['Age'] > 80:
        pesi += 1
    '''
    1 Malignancy, 2 COPD, 3 CHF
    '''
    if series['Cancer'] == 1:
        pesi += 1
    if series['CHF_COPD'] >= 1:
        pesi += 1
        
    if series['HR'] > 109:
        pesi += 1
    
    if series['SBP'] < 100:
        pesi += 1
         
    if series['SpO2'] < 90:
        pesi += 1
    if pesi > 0:
        return('High Risk')
    else:
        return('Low Risk')

def esc_score(series):
    trop_bool = False
    rv_bool = False
    pesi_bool = False    
    if str == type(series['TnI']):
        pass

    elif series['TnI'] >= .012:
        trop_bool = True   

    # RV abnormal 1: no, 2: yes
    if series['RV function'] == 2:
        rv_bool = True

    if pesi_score(series) > 85 or simple_pesi_score(series):
        pesi_bool = True

    if series['SBP'] < 90:
        return("High")

    if trop_bool == True and rv_bool == True and pesi_bool == True:
        return("Intermediate-high")
    
    elif (trop_bool == True and (rv_bool == True or pesi_bool == True)):
        return("Intermediate-low")

    else:
        return("Low")
    
def bova_score(series):
    # sbp < 90 cannot be done
    bova_score = 0
    if series['SBP'] < 101 and series['SBP'] > 89:
        bova_score += 2
    
    if str == type(series['TnI']):
        pass

    elif series['TnI'] >= .012:
        bova_score += 2 


    if series['RV function'] == 2:
        bova_score += 2
        
    if series['HR'] > 109:
        bova_score += 1
        
    return(bova_score)