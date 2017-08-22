def Levenshtein(m1,m2):
    d=np.zeros((len(m1)+1,len(m2)+1))
    for i in range(len(m1)+1):
        d[i][0]=i
    for j in range(len(m2)+1):
        d[0][j]=j
    for i in range(1,len(m1)+1):
        for j in range(1,len(m2)+1):
            if m1[i-1]==m2[j-1]:
                cs=0
            else:
                cs=1
            d[i][j]=min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+cs)
    return(d[len(m1)][len(m2)])

def detect_language(sentence):
    try:
        return(detect_langs(sentence)[0].lang)
    except:
        return('unsure')

def find_nearest_word_with_accent(mots_accent,word):
    mini=999
    for x in list(mots_accent):
        d=Levenshtein(str(x),word)
        if d<mini:
            mini=d
            m=x
    return(m)

def del_small_char(string,l):
    string=string.split(' ')
    for i in range(len(string)-1,-1,-1):
        if len(string[i])<l:
            del string[i]
    return(' '.join(string))



def normalize(string,spec,stopwords,dico_mot_accent,sigle=False): #pas très optimisé, mais le temps d'execution est plus que correct
    if string!=None:
        string=string.lower()
        if sigle==False:
            string=del_stopwords(string,stopwords)
            string=deal_accents(string,dico_mot_accent)
        for x in spec:
            string=string.replace(x,'')
        if (sigle==True) & (len(string)>3):
            return(string)
        if (sigle==True) & (len(string)<=3):
            return('')
        return(string.replace(' ',''))
    return('')

def deal_accents(string,dico_mot_accent):
    string=string.split(' ')
    for i,x in enumerate(string):
        if x in dico_mot_accent:
            string[i]=dico_mot_accent[x]
    return(' '.join(string))

def del_stopwords(string,stopwords):
    string=string.split(' ')
    for i in range(len(string)-1,-1,-1):
        if string[i] in stopwords:
            del string[i]
    return(' '.join(string))
