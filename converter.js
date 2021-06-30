const fs = require("fs");

let str = fs.readFileSync("/dev/stdin").toString();

let csv = str.trim().split("\n\n").map(a=>{
    return a.split("\n")[1].slice(1,-1);
}).join("\n").trim();

console.log("\"lon\",\"lat\"");
console.log(csv);