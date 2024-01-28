import math

#zadání
a = 0
point_1 = []
point_2 = []

#kontola velikosti krychle
def check_room_size(input_1):
    try:
        a = int(input_1)
        
        #je délka strany kladná?    
        if a <= 0:
            exit()
            
        return(a)
    except:
        print("Invalid input")
        exit()

#konrola souřadnic bodu 1
def check_point_1(input_2):
    try:
        #formátování inputu
        point_1 = input_2.split()
        point_1 = [int(x) for x in point_1]
        #jsou zadané 3 souřadnice?
        temp = point_1[2]

        #jsou souřadnice bodů nezáporné?  (není v zadání, ale vyplývá z logiky)
        temp_1 = False
        for i in range(3):
            if point_1[i] < 0:
                exit()

            #nejsou body moc blízko k hraně?
            if point_1[i] != 0 and point_1[i] != a:
                if point_1[i] < 20 or point_1[i] > (a - 20):
                    exit()
            
        
            if point_1[i] == 0 or point_1[i] == a:

                if temp_1 == True:
                    exit()
                temp_1 = True

        if temp_1 == False:
            exit()

        return(point_1)
    
    except:
        print("Invalid input")
        exit()

#konrola souřadnic bodu 2
def check_point_2(input_3):
    try:
        #formátování inputu
        point_2 = input_3.split()
        point_2 = [int(x) for x in point_2]
        #jsou zadané 3 souřadnice?
        temp = point_2[2]

        #jsou souřadnice bodů nezáporné?  (není v zadání, ale vyplývá z logiky)
        temp_2 = False
        for i in range(3):
            if point_2[i] < 0:
                exit()

            #nejsou body moc blízko k hraně?
            if point_2[i] != 0 and point_2[i] != a:
                if point_2[i] < 20 or point_2[i] > (a - 20):
                    exit()
            
        
            if point_2[i] == 0 or point_2[i] == a:

                if temp_2 == True:
                    exit()
                temp_2 = True

        if temp_2 == False:
            exit()

        return(point_2)

    except:
        print("Invalid input")
        exit()

#input hrany krychle a souřadnic bodů 
input_1 = input("Napiště délku hrany krychle: " )
a = check_room_size(input_1)
input_2 = input("Napiště souřadnice prvního bodu ve formátu 'XXX XXX XXX': ")
point_1 = check_point_1(input_2)
input_3 = input("Napiště souřadnice druhého bodu ve formátu 'XXX XXX XXX': ")
point_2 = check_point_2(input_3)

#vzdálenost k hraně (body na protější straně)
def edge_distances(point_1, point_2):
    distances_1 = [point_1[0]]
    distances_1.append(point_1[1])
    distances_1.append(a - point_1[0])
    distances_1.append(a - point_1[1])

    distances_2 = [point_2[0]]
    distances_2.append(point_2[1])
    distances_2.append(a - point_2[0])
    distances_2.append(a - point_2[1])

    return(distances_1, distances_2)


#výpočet trubky a hadice u bodů na stejné straně
def stejna_strana(i):
    pipe = 0
    distances = []

    for j in range(3):
        if j != i:
            temp = abs(point_1[j] - point_2[j])
            pipe = pipe + temp
            distances.append(temp)
            
    hose = math.sqrt((math.pow(distances[0], 2) + math.pow(distances[1], 2)))  

    return(pipe, hose)
    
#výpočet trubky a hadice u bodů na protějších stranách
def protejsi_strany(point_1, point_2):   
    #vytvoření 2d prostoru
    point_1 = [i for i in point_1 if (i != 0 and i != a)]
    point_2 = [i for i in point_2 if (i != 0 and i != a)]

    distances_1, distances_2 = edge_distances(point_1, point_2)

    total_distances = []
    hose_distances = []
    #určení vzdálenosti u všech 4 směrů
    for i in range(4):
        distance_between_points = 0
        if i % 2 == 0:
            distance_between_points = abs(point_1[1] - point_2[1])
        else: 
            distance_between_points = abs(point_1[0] - point_2[0])
       
        total_distances.append(distances_1[i] + distances_2[i] + a + distance_between_points)
        hose_distances.append(((distances_1[i] + distances_2[i] + a) ** 2 + distance_between_points ** 2 ) ** 0.5)
 
    #určení nejkratší cesty
    total_distances.sort()
    hose_distances.sort()

    return(total_distances[0], hose_distances[0])
    
# výpočet trubky a hadice u bodů na soudedících stranách
def sousedni_strany():
    a_side = 0
    b_side = 0

    for j in range(3):
        #výpočet strany "b" pro pythagorovu větu
        if (point_1[j] != 0 and point_1[j] != a) and (point_2[j] != 0 and point_2[j] != a):
            b_side = abs(point_1[j] - point_2[j])
        
        #výpočet strany "a" pro pythagorovu větu
        else:
            a_side = a_side + abs(point_1[j] - point_2[j])

    #pyth. věta
    hose = (a_side ** 2 + b_side ** 2) ** 0.5
    
    
    #součet stran trojúholníku = trubky
    pipe = a_side + b_side
    
    return(pipe, hose)

#určení stran, na kterých body leží
pipe = 0
hose = 0
neighboring_sides = True
for i in range(3):
    diff = point_1[i] - point_2[i]
    #stejné strany
    if (diff == 0) and (point_1[i] == a or point_1[i] == 0):
        pipe, hose = stejna_strana(i)
        neighboring_sides = False
    #protější strany
    elif (abs(diff) == a):
        pipe, hose = protejsi_strany(point_1, point_2)
        neighboring_sides = False

#sousední strany
if (neighboring_sides == True):
    pipe, hose = sousedni_strany()


#vypsat výsledek
print("Delka potrubi: " + str(pipe))
print("Delka hadice: " + str(hose))