
exports.up = function (knex) {
    return knex.schema.createTable("authors", table => {
        table.increments("id").primary()
        table.string("name", 100).notNull()
    })
};

exports.down = function (knex) {
    return knex.schema.dropTable("authors")
};
