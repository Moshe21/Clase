function SecondLargestNumber(numbers){
    let first = numbers[0]

    let second = 0;


    for (let i=0;i<numbers.length;i++){

        if(numbers[i]> first){
            second = first;
            first=numbers[i]
        }
        if(numbers[i]> second && numbers[i]< first){
            second= numbers[i];

        }
    }
    return second
}

let nums=[8,4,6,12,34,10]
console.log (SecondLargestNumber(nums))