t = int(input())
for _ in range(t):
    n = int(input())
    L = [int(i) for i in input().split()]
    mx =0
    for i in L:
        M=0
        for j in L:
            if j>=i:
                M+=1

        #M = [1 for j in L if j>=i]
        mx=max(mx, M*i)

    print(mx)

'''
6
3
1 1 1
3
4 1 1
3
2 4 2
8
1 2 3 4 5 6 7 8
1
1000000000000
3
1000000000000 999999999999 1
'''
'''
# 코틀린
fun main() {
    var t = readLine()!!.toInt()
    for(k in 0..t-1){
        var n = readLine()!!.toInt()
        var L = readLine()!!.split(" ").map { it.toDouble() }
 
    	var mx: Double =0.0
        for(i in 0..n-1){
            var M: Double = 0.0
            for (j in 0..n-1){
                if (L[j]>L[i]-1){
                    M =M+1
                }
            if (M*L[i]>mx){
                mx = M*L[i]
            } 
            }
        }
        println(String.format("%.0f", mx))
    }  
}

이게 답이 아니야..
fun main() {
    var t = readLine()!!.toInt()

    for(i in 1..t){
        var n = readLine()!!.toInt()
        var L = readLine()!!.split(" ").map{it.toDouble()}
        var mx: Double=0.0

        for(j in 0..n-1){
            var customer: Double = 0.0

            for(k in 0..n-1){
                if(L[j]>=L[k]){
                customer=customer+1
                }
            }
            if(mx< customer*L[j]){
                    mx=customer*L[j]
            }
        }
        println(String.format("%.0f",mx))
    }
}

'''