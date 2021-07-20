function mergeArray(Array, lo, hi){
    if(lo == hi) return Array;
    var m = (lo + hi) >> 1;
    var i = lo;
    var j = m + 1;
    var B = [];

    while( i <= m && j <= hi){
        if(Array[i] < Array[j]){
            B.push(Array[i]);
            ++i;
        }
        else{
            B.push(Array[j]);
            ++j;
        }
    }
    for(var k = i; k <= m; ++k) B.push(Array[k]);
    for(var k = j; k <= hi; ++k) B.push(Array[k]);
    for(var k = lo; k <= hi; ++k) Array[k] = B[k - lo];
}


function mergeSort(arrayA, lo, hi){
    if(lo >= hi) return 0;
    var m = (lo + hi) >> 1;
    var i = lo;
    var j = m + 1;
    mergeSort(arrayA, i, m);
    mergeSort(arrayA, j, hi);
    mergeArray(arrayA, lo, hi);
}


function set(Array){
    let res = [];
    var i;
    for(i = 0; i < Array.length - 1; ++i){
        if(Array[i] != Array[i + 1]) res.push(Array[i]);
    }
    res.push(Array[i]); // 마지막 인자는 무조건 담는다.
    return res;
}


function sum(base, other){
    var result = [];
    var i = 0;
    var j = 0;
    while( i < base.length && j < other.length){
        if(base[i] < other[j]){ // 세 줄 넘었는데 함수로 빼는 법 ??
            result.push(base[i]);
            ++i;
            
        }
        else{
            result.push(other[j]);
            ++j;
            }
    }
    
    for(var k = i; k < base.length; ++k) result.push(base[k]);
    for(var k = j; k < other.length; ++k) result.push(other[k]);
    return set(result);
}


function complement(base, other){
    var i = 0;
    var j = 0;
    var res = [];
    while(i < base.length && j < other.length){
        if(base[i] < other[j]){
            res.push(base[i]);
            ++i;
        }
        else if (base[i] == other[j]) {++i; ++j;}
        else ++j;
    }
    for(var k = i; k < base.length; ++k) res.push(base[k]); // ++i 실수

    return res;
}


function intersect(base, other){
    var i = 0;
    var j = 0;
    var res = [];
    while(i < base.length && j < other.length){
        if(base[i] < other[j]) ++i;
        else if (base[i] > other[j]) {++j;}
        else{
            res.push(base[i]);
            ++i;
            ++j;
        }
    }
    return res;
}

function f(a, b){
    return a - b;
}

function solution(arrayA, arrayB){
    //var answer = [];
    var answer = new Array(5);
    for(var i = 0; i < 5; ++i){
        answer[i] = [];
    }
    mergeSort(arrayA, 0, arrayA.length - 1);
    //arrayB.sort(f);
    if(isNaN(arrayB)) arrayB.sort(); // 문자열이면 기존 sort
    else arrayB.sort(f);

    arrayA = set(arrayA);
    answer[0] = arrayA;
    arrayB = set(arrayB);
    answer[1] = arrayB;

    //answer.push( sum(arrayA, arrayB) );
    answer[2] = sum(arrayA, arrayB) ;
    answer[3] = complement(arrayA, arrayB) ;
    answer[4] = intersect(arrayA, arrayB) ;
    return answer;
}


function print(Array, dimension){
    if(dimension == 1){
        var i;
        process.stdout.write('[');
        if(!Array.length){
            process.stdout.write(']');
            return;
        }
        for(i = 0; i < Array.length - 1; ++i){
            process.stdout.write(Array[i] + ',');
        }
        process.stdout.write(Array[i] + ']');
    }

    else if(dimension == 2){
        for(var i = 0; i < finalResult.length; ++i){
            print(finalResult[i], 1); 
            if(i != finalResult.length - 1)
                process.stdout.write(',');
        }
    }
}


function newline(){
    console.log('\n');
}


function printOutput(info, array){
    for(var i = 0; i < info.length; ++i){
        process.stdout.write(info[i]+' = ');
        print(array[i], 1);
        newline();  
    }  
}


function printLastOutput(finalResult){
    process.stdout.write('리턴값 [');
    print(finalResult, 2);
    process.stdout.write(']');
    //var finalComment = "A로 만든 집합 원소 개수는 {0}개, B로 만든 집합 원소 개수는 {1}개, 합집합 원소 개수는 {2}, 차집합 원소 개수는 {3}, 공통 원소 개수는 {4}".format( 
    //finalResult[0].length, finalResult[1].length, finalResult[2].length, finalResult[3].length, finalResult[4].length);
    //console.log(finalComment);
    
    // ! 포맷팅 다른 게 안됨
    console.log(` //A로 만든 집합 원소 개수는 ${finalResult[0].length}개, B로 만든 집합 원소 개수는 ${finalResult[1].length}개, 합집합 원소 개수는 ${finalResult[2].length}, 차집합 원소 개수는 ${finalResult[3].length}, 공통 원소 개수는 ${finalResult[4].length}`);
}








let arrayA = [2, 3, 4, 3, 5]
arrayA = [11, 2, 3, 2]
//arrayA = ['app', 'a', 'Apple', 'app', '111', '2']
let arrayB = new Array(1, 6, 7)
arrayB = [1,3]
//arrayB = ['b', '111', 'apple']

//var formula = 'return'
// js는 내장형 객체로서 function 객체를 준비하고 있다. 함수는 이 function의 객체의 생성자를 이용하여 정의할 수 있다.
//var solution = new Function('a', 'b', 'return a + b;');
//console.log('test: ' + solution(1, 2));

let print1 = ['매개변수 A', '매개변수 B']
let print2 = ['A 집합', 'B 집합', '합집합sum', '차집합complement', '교집합intersect']

printOutput(print1, [arrayA, arrayB]);

let finalResult = solution(arrayA, arrayB);
printOutput(print2, finalResult);

printLastOutput(finalResult);