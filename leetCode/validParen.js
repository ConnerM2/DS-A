// My attempt
var isValid = function(s) {
    let pare = {
        '(': ')',
        '{': '}',
        '[': ']',
        ')': ')',
        '}': '}',
        ']': ']'
    }

    for (let i = 0; i < s.length; i++){
        let current = pare[s[i]]
        for (let j = 0; j < s.length; j++) {
            let next = pare[s[j+1]]
            if (current === next) {
                return true
            } else {
                return false
            }
        }
    }
}

console.log(isValid('([])'))


// correct version
var isValid = function(s) {
    let pare = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    let stack = []; 

    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        
        if (pare[char]) {
            stack.push(char);
        } else {
            let last = stack.pop();
            if (pare[last] !== char) {
                return false;
            }
        }
    }
    return stack.length === 0;
}