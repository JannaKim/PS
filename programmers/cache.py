
def solution(cacheSize, cities):
    link= {}
    link['start']=None
    top='start'
    filled=0
    stock={}
    ans=0
    if not cacheSize:
        return 5*len(cities)
    elif cacheSize==1:
        for a, b in zip(cities, cities[1:]):
            a=a.lower()
            b=b.lower()
            if a==b:
                ans+=1
            else:
                ans+=5
        return ans+5
         
    for city in cities:
        city=city.lower()
        if city not in stock or stock[city]==False:
            if filled<cacheSize:
                filled+=1
            else:
                stock[link['start']]=False
                link['start']= link[link['start']]
            link[top]=city
            top=city
            ans+=5
            stock[city]=True
            link[city]=None
            
        else:
            ans+=1
            ths='start'
            while link[ths]!=city:
                ths=link[ths]
            link[ths]= link[link[ths]]
            link[top]=city
            top=city
        print(ans)

    return ans
            
            
#print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
#print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(1, ["Jeju", "Jeju", "Jeju", "Pangyo"]))