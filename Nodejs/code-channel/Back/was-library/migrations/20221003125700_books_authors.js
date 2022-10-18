
exports.up = function (knex) {
    return knex.schema.createTable("books_authors", table => {
        table.integer("book_id").unsigned().notNull()
        table.integer("author_id").unsigned().notNull()
        table.foreign("book_id").references("books.id").onDelete("CASCADE")
        table.foreign("author_id").references("authors.id").onDelete("CASCADE")
    })
};

exports.down = function (knex) {
    return knex.schema.dropTable("books_authors")
};
