const {readFileSync, promises: fsPromises} = require('fs');

function syncReadFile(filename: string) {
    const contents = readFileSync(filename, 'utf-8');
    const arr = contents.split(/\r?\n/) as string[];
    return arr;
  }
  
  const input = syncReadFile("./input.txt");

  let curr = 0;
  let topThree = [] as number[] 
  input.forEach((value, i) => {
    if(value.length <= 0 || (input.length - 1) === i) {
        if (topThree.length < 3) topThree.push(curr) 
        else {
            topThree = topThree.sort((a,b) => b - a)
            if(topThree[2] < curr)
                topThree[2] = curr  
        }
        curr = 0
    }
    else {
        curr += Number(value) 
    }
  })
console.log(topThree.reduce((partialSum, a) => partialSum + a, 0))