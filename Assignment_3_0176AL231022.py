import os 
import json 
import random 
import datetime 
import time 




BASE_DIR =os .path .dirname (os .path .abspath (__file__ ))
USERS_FILE =os .path .join (BASE_DIR ,'users.json')
SCORES_FILE =os .path .join (BASE_DIR ,'scores.json')
QUESTIONS_FILE =os .path .join (BASE_DIR ,'questions.json')


def ensure_file_exists (path ,default ):
    if not os .path .exists (path ):
        with open (path ,'w',encoding ='utf-8')as f :
            json .dump (default ,f ,indent =4 )


def load_json (path ):
    ensure_file_exists (path ,{})
    with open (path ,'r',encoding ='utf-8')as f :
        try :
            return json .load (f )
        except json .JSONDecodeError :
            return {}


def save_json (path ,data ):
    with open (path ,'w',encoding ='utf-8')as f :
        json .dump (data ,f ,indent =4 )


def safe_input (prompt ,*,default =None ):
    try :
        val =input (prompt )
    except (EOFError ,KeyboardInterrupt ):
        print ('\nInput cancelled. Exiting.')
        raise SystemExit 
    if val ==''and default is not None :
        return default 
    return val 


def safe_int (prompt ,min_val =None ,max_val =None ):
    while True :
        val =safe_input (prompt )
        try :
            i =int (val )
        except ValueError :
            print ('Please enter a valid integer.')
            continue 
        if min_val is not None and i <min_val :
            print (f'Please enter a number >= {min_val }.')
            continue 
        if max_val is not None and i >max_val :
            print (f'Please enter a number <= {max_val }.')
            continue 
        return i 



def setup_sample_questions ():

    data ={
    "PYTHON":[
    {"question":"What will print(type([])) display in Python?",
    "options":["A. <class 'tuple'>","B. <class 'dict'>","C. <class 'list'>","D. <class 'set'>"],
    "answer":"C"},
    {"question":"Which keyword is used to define a function in Python?",
    "options":["A. fun","B. def","C. function","D. define"],
    "answer":"B"},
    {"question":"Which of the following is used to start a comment in Python?",
    "options":["A. //","B. <!--","C. #","D. /*"],
    "answer":"C"},
    {"question":"Which method converts a string to lowercase in Python?",
    "options":["A. lower()","B. toLower()","C. downcase()","D. low()"],
    "answer":"A"},
    {"question":"What is the output of print(2 ** 3) in Python?",
    "options":["A. 6","B. 8","C. 9","D. 5"],
    "answer":"B"}
    ],
    "DBMS":[
    {"question":"DBMS stands for?",
    "options":["A. Database Management System","B. Data Manage System","C. Database Monitor","D. None"],
    "answer":"A"}
    ],
    "DSA":[
    {"question":"Stack follows which order?",
    "options":["A. FIFO","B. FIFO (Queue)","C. LILO","D. LIFO"],
    "answer":"D"}
    ]
    }
    save_json (QUESTIONS_FILE ,data )


def ensure_data_files ():
    ensure_file_exists (USERS_FILE ,{})
    ensure_file_exists (SCORES_FILE ,{})

    if not os .path .exists (QUESTIONS_FILE ):
        setup_sample_questions ()
    else :

        q =load_json (QUESTIONS_FILE )
        if not q :
            setup_sample_questions ()


def register ():
    users =load_json (USERS_FILE )
    enroll =safe_input ('Enter enrollment/username: ').strip ()
    if not enroll :
        print ('Enrollment cannot be empty.')
        return 
    if enroll in users :
        print ('User already exists! Try logging in.')
        return 
    password =safe_input ('Enter password: ').strip ()
    name =safe_input ('Enter name: ').strip ()
    email =safe_input ('Enter email: ').strip ()
    branch =safe_input ('Enter branch: ').strip ()
    year =safe_input ('Enter year: ').strip ()
    contact =safe_input ('Enter contact number: ').strip ()

    users [enroll ]={
    'password':password ,
    'name':name ,
    'email':email ,
    'branch':branch ,
    'year':year ,
    'contact':contact ,
    'role':'user'
    }
    save_json (USERS_FILE ,users )
    print ('Registration successful!')


def login ():
    users =load_json (USERS_FILE )
    enroll =safe_input ('Enter enrollment/username: ').strip ()
    password =safe_input ('Enter password: ').strip ()
    if enroll in users and users [enroll ].get ('password')==password :
        print (f"Welcome, {users [enroll ].get ('name',enroll )}!")
        return enroll 
    print ('Invalid credentials.')
    return None 



def record_score (enroll ,category ,score ,total ,time_seconds =None ):
    scores =load_json (SCORES_FILE )
    if enroll not in scores :
        scores [enroll ]=[]
    entry ={
    'category':category ,
    'score':score ,
    'total':total ,
    'datetime':str (datetime .datetime .now ())
    }
    if time_seconds is not None :

        entry ['time_seconds']=round (time_seconds ,2 )
    scores [enroll ].append (entry )
    save_json (SCORES_FILE ,scores )


def attempt_quiz (enroll ):
    questions =load_json (QUESTIONS_FILE )
    categories =list (questions .keys ())
    if not categories :
        print ('No quiz categories available.')
        return 

    print ('\nAvailable Categories:')
    for i ,cat in enumerate (categories ,1 ):
        print (f"{i }. {cat }")
    choice =safe_int ('Choose category number: ',min_val =1 ,max_val =len (categories ))
    category =categories [choice -1 ]

    selected_questions =questions .get (category ,[])[:]
    if not selected_questions :
        print ('No questions in this category.')
        return 

    random .shuffle (selected_questions )

    if len (selected_questions )>=5 :
        selected_questions =selected_questions [:5 ]
    else :

        needed =5 -len (selected_questions )
        selected_questions .extend (random .choices (selected_questions ,k =needed ))
    score =0 
    total =len (selected_questions )

    start_time =time .time ()
    for idx ,q in enumerate (selected_questions ,1 ):
        print (f"\nQ{idx }: {q .get ('question')}")
        for opt in q .get ('options',[]):
            print (opt )

        while True :

            ans =safe_input ('Your answer (A/B/C/D): ').strip ()
            if not ans :
                print ('Invalid try again')
                continue 

            if ans in ('A','B','C','D'):
                chosen =ans 
                break 

            if ans in ('1','2','3','4'):
                mapping ={'1':'A','2':'B','3':'C','4':'D'}
                chosen =mapping [ans ]
                break 
            print ('Invalid try again')

        correct =q .get ('answer','').strip ().upper ()
        if chosen ==correct :
            print ('Correct!')
            score +=1 
        else :
            print (f"Wrong. Correct answer: {correct }")

    end_time =time .time ()
    elapsed =end_time -start_time 
    print (f"\nYour Score: {score }/{total }")
    print (f"Time taken: {elapsed :.2f} seconds")
    record_score (enroll ,category ,score ,total ,time_seconds =elapsed )


def view_profile (enroll ):
    users =load_json (USERS_FILE )
    user =users .get (enroll )
    if not user :
        print ('User not found.')
        return 
    print ('\n--- PROFILE ---')
    for k ,v in user .items ():
        if k !='password':
            print (f"{k .capitalize ()}: {v }")


def update_profile (enroll ):
    users =load_json (USERS_FILE )
    user =users .get (enroll )
    if not user :
        print ('User not found.')
        return 
    print ('\nLeave blank to keep current value.')
    for field in ['name','email','branch','year','contact']:
        current =user .get (field ,'')
        new_val =safe_input (f"{field .capitalize ()} ({current }): ").strip ()
        if new_val :
            user [field ]=new_val 
    users [enroll ]=user 
    save_json (USERS_FILE ,users )
    print ('Profile updated successfully!')



def user_menu (enroll ):
    while True :
        print ('\n--- USER MENU ---')
        print ('1. Attempt Quiz')
        print ('2. View Profile')
        print ('3. Update Profile')
        print ('4. Logout')
        choice =safe_input ('Enter choice: ').strip ()
        if choice =='1':
            attempt_quiz (enroll )
        elif choice =='2':
            view_profile (enroll )
        elif choice =='3':
            update_profile (enroll )
        elif choice =='4':
            print ('Logged out.')
            break 
        else :
            print ('Invalid try again')

def main ():
    ensure_data_files ()
    print ('Welcome to the Standalone Quiz Application!')
    while True :
        print ('\nMain Menu:')
        print ('1. Register')
        print ('2. Login')
        print ('3. Exit')
        choice =safe_input ('Enter choice: ').strip ()
        if choice =='1':
            register ()
        elif choice =='2':
            user =login ()
            if user :
                user_menu (user )
        elif choice =='3':
            print ('Goodbye!')
            break 
        else :
            print ('Invalid try again')

if __name__ =='__main__':
    main ()
