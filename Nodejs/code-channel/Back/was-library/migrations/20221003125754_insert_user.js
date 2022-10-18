
exports.up = function (knex) {
    return knex("users").insert({
        name: "BIBLIOTECA MANEIRA",
        email: "biblioteca@waslibrary.com",
        password: "$2b$10$NwVbkS3bp1Y2.ciHFFaFSeUUT0YV7C4YkNS9Enf/c4WiuyWcqOUwy",
        role: "admim"
    })
};

exports.down = function (knex) {
return knex("users").delete().where({email: "biblioteca@waslibrary.com"})
};
