#Mintal basic code idea
#mintal will be a search engine for symptoms of mental illness,
#it may provide more than one result according to the symptoms entered
usr_list = []

def main(): #main function

    symptoms = example_symptoms() #equates symptoms to example_symptoms function

    

    print('ASD symptoms:', symptoms["ASD_symptoms"])
    print()
    print('ADHD symptoms:', symptoms["ADHD_symptoms"])
    print()
    print('Schizophrenia symptoms:', symptoms["Schizophrenia_symptoms"])
    print()
    print('Bipolar symptoms:', symptoms["Bipolar_symptoms"])
    print()
    print('Major Depressive symptoms:', symptoms["Major_Depressive_symptoms"])
    print()
    print('Premenstrual Dysphoric symptoms:', symptoms["Premenstrual_Dysphoric_symptoms"])
    print()
    print('Specific Phobia symptoms:', symptoms["Specific_Phobia_symptoms"])
    print()
    print('Social Anxiety symptoms:', symptoms["Social_Anxiety_symptoms"])
    print()
    
    usr_input = input('what are some symptoms you are having ')
    
    if usr_input not in symptoms["ASD_symptoms"] and \
       usr_input not in symptoms["ADHD_symptoms"] and \
       usr_input not in symptoms["Schizophrenia_symptoms"] and \
       usr_input not in symptoms["Bipolar_symptoms"] and \
       usr_input not in symptoms["Major_Depressive_symptoms"]and \
       usr_input not in symptoms["Premenstrual_Dysphoric_symptoms"] and \
       usr_input not in symptoms["Specific_Phobia_symptoms"] and \
       usr_input not in symptoms["Social_Anxiety_symptoms"]:
        while True:
            if usr_input not in symptoms["ASD_symptoms"] and \
               usr_input not in symptoms["ADHD_symptoms"] and \
               usr_input not in symptoms["Schizophrenia_symptoms"] and \
               usr_input not in symptoms["Bipolar_symptoms"] and \
               usr_input not in symptoms["Major_Depressive_symptoms"] and \
               usr_input not in symptoms["Premenstrual_Dysphoric_symptoms"] and \
               usr_input not in symptoms["Specific_Phobia_symptoms"] and \
               usr_input not in symptoms["Social_Anxiety_symptoms"]:
                print(f'sorry the symptom {usr_input} is not in our database')
                usr_input = input('what are some symptoms you are having ')
            else:
                for symptom_list in symptoms:
                    if usr_input not in symptoms[str(symptom_list)]:
                        print(f'not found in list {symptom_list}')
                    elif usr_input in symptoms[str(symptom_list)]:
                        print(f'found in list {symptom_list}')
                        usr_list.append(usr_input)
                        continue
                        #break
                again = input('do you have another symptom?(Y/n) ')
                if again == 'y' or again == 'Y':
                    return main()
                else:
                    print(usr_list)
                    break
    else:
        for symptom_list in symptoms:
            if usr_input not in symptoms[str(symptom_list)]:
                print(f'not found in list {symptom_list}')
            elif usr_input in symptoms[str(symptom_list)]:
                print(f'found in list {symptom_list}')
                usr_list.append(usr_input)
                continue #the code will add the symptom to the list twice if it finds two diffrent lists it could be apart of
                #break
        again = input('do you have another symptom?(Y/n) ')
        if again == 'y' or again == 'Y':
            return main()
        else:
            print(usr_list)

def example_symptoms(): #example_symptoms function
    
    possible_symptoms = {"ASD_symptoms": ['failure of back-and-forth conversation', 'reduced sharing of intrests',
                                          'reduced sharing of emotions', 'failure to initiate or respond to socail interactions',
                                          'poorly intergrated verbal and nonverbal communication', 'failure to make eye contact',
                                          'misunderstanding of gestures', 'lack of facial expressions and nonverbal communication',
                                          'deficits in developing relationships', 'deficits in mantaining relationships',
                                          'deficits in understanding relationships', 'difficulties adjusting behavior to socail contexs',
                                          'difficulties in sharing imaginative play', 'difficulties making friends', 'absence of interests in peers',
                                          'restricted patterns of behavior', 'restricted interest', 'restricted activites', 'repetitve motor movements',
                                          'repetitve use of objects', 'repetitve speech', 'insistence on sameness', 'inflexible adherence to routines',
                                          'ritualized patterns', 'extreme distress at small changes', 'difficulties with transitions',
                                          'rigid thinking patterns', 'fixated interests with abnormal intensity', 'hyper- or hyporeactivity to sensory input',
                                          'unusual interest in sensory aspects of the environment'],
                         
                         "ADHD_symptoms": ['fails to give close attention to details', 'makes careless mistakes in work of some kind', 'difficulty sustaining attention in tasks',
                                           'does not  listen when spoken to directly', 'does not follow through on instructions',
                                           'fails to finish tasks', 'difficulty organizing tasks', 'teluctant to engage in tasks that require sustained mental effort',
                                           'loses things necessary for tasks', 'easily distracted by extraneous stimuli', 'forgetful in daily activities',
                                           'often fidgets', 'often leaves leat in seated situations', 'runds about or climbs in situations where inappropriate',
                                           'unable to play or engage in leisure activites quietly', 'often on the go', 'talks excessively', 'blurts out answer before a question is completed',
                                           'difficutlty waiting their turn', 'interrupts or intrudes on others'],
                         
                         "Schizophrenia_symptoms": ['delusions', 'hallucinations', 'disoganized speech', 'grossly disorganized or catatonic behavior', 'diminished emotional expression', 'avolition'],
                         
                         "Bipolar_symptoms": ['inflated self-esteem', 'grandiosity', 'decreased need for sleep', 'more talkative than usual', 'pressure to keep talking', 'flight of ideas', 'racing thoughts',
                                              'distractibility', 'increase in goal-directed activity', 'excessive involvement in activities that have a high potential for painful consequences',
                                              'depressed mood most of the day', 'markedly diminished intrest in most or all activities', 'dminished pleasure in most or all activites', 'significant weight loss',
                                              'insomnia', 'hypersomnia', 'psychomotor agitation', 'psychomotor retardation', 'fatigue', 'loss of energy', 'feelings of worthlessness', 'excessive guilt',
                                              'inappropriate guilt', 'diminished ability to think', 'diminished ability to concentrate', 'indecisiveness', 'recurrent thoughts of death',
                                              'recurrent suicidal ideation', 'suicide attempt'],
                         
                         "Major_Depressive_symptoms": ['depressed mood most of the day', 'markedly diminished intrest in most or all activities', 'dminished pleasure in most or all activites', 'significant weight loss',
                                                       'insomnia', 'hypersomnia', 'psychomotor agitation', 'psychomotor retardation', 'fatigue', 'loss of energy', 'feelings of worthlessness', 'excessive guilt',
                                                       'inappropriate guilt', 'diminished ability to think', 'diminished ability to concentrate', 'indecisiveness', 'recurrent thoughts of death',
                                                       'recurrent suicidal ideation', 'suicide attempt'],
                         
                         "Premenstrual_Dysphoric_symptoms": ['marked affective lability', 'marked irritability', 'marked anger', 'increased interperonal conflicts', 'marked depressed mood', 'feelings of hopelessness',
                                                             'self-deprecating thoughts', 'marked anxiety', 'marked tension', 'feelings of being on edge', 'decreased interest in usual activities', 'subjective difficulty in concentration',
                                                             'lethargy', 'easy fatigability', 'marked lack of energy', 'marked change in appetite', 'overeating', 'specific food cravings', 'hypersomnia', 'insomnia', 'a sense of being overwhelmed',
                                                             'a sense of being out of control', 'breast tenderness', 'breast swelling', 'joint pain', 'mucsle pain', 'sensation of bloating', 'sensation of weight gain'],
                         
                         "Specific_Phobia_symptoms": ['phobic object almost always provokes immediate fear', 'phobic situation almost always provokes immediate fear', 'phobic object almost always provokes immediate anxiety',
                                                      'phobic situation almost always provokes immediate anxiety', 'phobic object is actively avoided', 'phobic situation is actively avoided', 'phobic situation is endured with intense fear',
                                                      'phobic situation is endured with intense anxiety', 'phobic object is endured with intense fear', 'phobic object is endured with intense anxiety',
                                                      'fear is out of proportion to the actual danger posed by the object', 'anxiety is out of proportion to the actual danger posed by the specific object',
                                                      'fear is out of propotion to the actual danger posed by the specific situation', 'anxiety is out of proportion to the actual danger posed by the specific situation', 'fear is persistent',
                                                      'anxiety is persistent', 'avoidance is persistent', 'fear causes clinically significant distress', 'anxiety causes clinically significant distress', 'avoidance causes clinically significant distress'],
                         
                         "Social_Anxiety_symptoms": []}

    return possible_symptoms

main() #end of main fuction




































'''symptom_list = ['sadness', 'nervous', 'distressing memories'] #lists several symptoms
usr_list = []

while True: #while loop to keep search going
    usr_input = input('what is a symptom you are having? ') #asks the user what kind of symptom they are having

    if usr_input in symptom_list: #the if statement makes sure the symptom is recognized
        usr_list.append(usr_input)
        add_symptom_prompt = input('Would you like to add another symptom?(Y/n) ')

        
    else: #if the user enters an unknown symptom
        print('sorry we have not heard of that symptom before') #then it gives an error message
        retry_search = input('would you like to try agian (Y/n) ') #ask user if they wish to continue
        if retry_search == 'y' or retry_search == 'Y': #if the user enters y
            continue #then it continues the loop
        else: #if the user enters anything else
            break #it breaks the loop '''









"""     if usr_input == 'sadness': #if user enters sadness
            print('you may have depression') #then the user may have depression
        elif usr_input == 'nervous': #if the user enters nervous
            print('you may have anxiety') #then the user may have anxiety
        elif usr_input == 'distressing memories': #if the user enters distressing memories
            print('you may have PTSD') #then the user may have ptsd """
