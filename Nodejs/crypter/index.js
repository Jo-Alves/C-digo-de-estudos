const Cryptr = require("cryptr");

cryptr = new Cryptr("ansadjkasdasd")

let encrypted = cryptr.encrypt("Minha esposa Valdirene é muito linda e muitíssima gostosa")

console.log(encrypted)

let decrypted = cryptr.decrypt(encrypted)

console.log(decrypted)