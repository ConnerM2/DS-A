var romanToInt = function(s) {
    // Objects that holds the integer that corrisponds with each roman numeral
    let romanNum = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
    }

    let total = 0
        // loops through the array
        for (let i = 0; i < s.length; i++){
            // stores current and next roman numeral as INTEGERS. romanNum[s[i]]
            let currentRom = romanNum[s[i]]
            let nextRom = romanNum[s[i+1]]
        // 
        if (nextRom > currentRom) {
            total -= currentRom
        } else {
            total += currentRom
        }
    }   
return total 
};


//video solution
var romanToInt = function(s) {
    let roman = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    }
    let total = 0
    let n = s.length
    i = 0
    
    while (i < n){
        if (i < n-1 && roman[s[i]] < roman[s[i + 1]]) {
            total += roman[s[i + 1]] - roman[s[i]]
            i += 2
        } else {
            total += roman[s[i]]
            i ++
        }
    }
    return total
};