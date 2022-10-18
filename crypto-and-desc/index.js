const crypto = require("crypto-js")
require("dotenv").config()

let frase = "A paciência é a arte da esperança..."

let key = process.env.SECRET

let encrypted = crypto.AES.encrypt(frase, key)

console.log("Frase encripitado:")
console.log(encrypted.toString())

console.log("frase descriptografada:")

// let descrypted = crypto.AES.decrypt("U2FsdGVkX195rl0rVsyzq6zSUebXlNoYdwEwJqo8CmMDmrpLDMT6ROOde40gTIq4MdTodri/VdeeQkXv5zoiOg==", key)

let descrypted = crypto.AES.decrypt(encrypted, key)

console.log(descrypted.toString(crypto.enc.Utf8))