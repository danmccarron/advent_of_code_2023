const lines = document.getElementsByTagName("pre")[0].innerHTML.split(/\r?\n/)


//Part 1
let answer = 0
for (let i = 0; i < lines.length; i++) {
    let game = i+1
    let sets = lines[i].split(":")[1].split(";")
    for (let j = 0; j < sets.length; j++) {
        console.log(sets[j].split(", "))
        let set = sets[j].split(", ")
        for (let k = 0; k < set.length; k++) {
            let number = set[k].replace(/\D/g,'').replaceAll(" ","");
            let colour = set[k].replace(/[0-9]/g, '').replaceAll(" ","");
            if (colour == 'red' && number > 12 || colour == 'green' && number > 13 || colour == 'blue' && number > 14) {
                game = 0
            }
        }
    }
    console.log(game)
    answer += game
    console.log(answer)
}

//Part 2


let answer = 0
for (let i = 0; i < lines.length; i++) {
    let game = i+1
    let red = 0
    let green = 0
    let blue = 0
    let sets = lines[i].split(":")[1].split(";")
    for (let j = 0; j < sets.length; j++) {
        console.log(sets[j].split(", "))
        let set = sets[j].split(", ")
        for (let k = 0; k < set.length; k++) {
            let number = Number(set[k].replace(/\D/g,'').replaceAll(" ",""));
            let colour = set[k].replace(/[0-9]/g, '').replaceAll(" ","");
            if (colour == 'red' && number > red ) {
                red = number
            }
            if (colour == 'green' && number > green ) {
                green = number
            }
            if (colour == 'blue' && number > blue ) {
                blue = number
            }            
        }
    }
    console.log("red: "+red)
    console.log("green: "+green)
    console.log("blue: "+blue)
    console.log("product = " + red*green*blue)
    answer += red*green*blue
    console.log("running total = " + answer)
    }
