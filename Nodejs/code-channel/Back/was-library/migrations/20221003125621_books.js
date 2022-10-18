
exports.up = function (knex) {
    return knex.schema.createTable("books", table => {
        table.increments("id").primary()
        table.integer("register").notNull()
        table.string("title", 150).notNull()
        table.string("gender", 50).notNull()
        table.string("date_register").notNull()
    })
};

exports.down = function (knex) {
    return knex.schema.dropTable("books")
};
