const input = `...`

const strings = input.split(/\r?\n/);

const numbers = ['one','two','three','four','five','six','seven','eight','nine']

let a = 0;
for (let i=0; i < strings.length; i++) {
    strings[i] = strings[i].replaceAll("one","onee").replaceAll("two","twoo").replaceAll("three","threee").replaceAll("five","fivee").replaceAll("seven","sevenn").replaceAll("eight","eightt").replaceAll("nine","ninee");
    for (let j=0; j<numbers.length; j++) {
        strings[i] = strings[i].replaceAll(numbers[j],String(j+1));
    }
    a +=  Number(strings[i].match(/\d/) + strings[i].split("").reverse().join("").match(/\d/))
};
console.log(a);

