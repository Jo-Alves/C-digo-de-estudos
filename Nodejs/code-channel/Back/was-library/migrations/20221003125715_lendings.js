
exports.up = function (knex) {
    return knex.schema.createTable("lendings", table => {
        table.increments("id").primary()
        table.timestamp("date_lending").defaultTo(knex.fn.now());
        table.integer("student_id").unsigned().notNull()
        table.integer("user_id").unsigned().notNull()
        table.foreign("student_id").references("students.id").onDelete("CASCADE")
        table.foreign("user_id").references("users.id").onDelete("CASCADE")
    })
};

exports.down = function (knex) {
    return knex.schema.dropTable("lendings")
};
