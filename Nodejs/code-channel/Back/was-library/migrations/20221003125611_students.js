
exports.up = function (knex) {
    return knex.schema.createTable("students", table => {
        table.increments("id").primary()
        table.string("name", 100).notNull()
        table.string("gong", 10).notNull()
        table.string("level", 50).notNull()
        table.string("year").notNull()
        table.string("telephone").notNull()
        table.string("living_room").notNull()
    })
};

exports.down = function (knex) {
    return knex.schema.dropTable("students")
};
