
exports.up = function (knex) {
    return knex.schema.createTable("devolutions", table => {
        table.increments("id").primary()
        table.timestamp("date_devolution").defaultTo(knex.fn.now());
        table.integer("lending_id").unsigned().notNull()
        table.foreign("lending_id").references("lendings.id").onDelete("CASCADE")
    })
};

exports.down = function (knex) {
    return knex.schema.dropTable("devolutions")
};
