
exports.up = function (knex) {
    return knex.schema.createTable("items_lendings", table => {
        table.increments("id").primary()
        table.integer("book_id").unsigned().notNull()
        table.foreign("book_id").references("books.id").onDelete("CASCADE")
    })
};

exports.down = function (knex) {
    return knex.schema.dropTable("items_lendings")
};
