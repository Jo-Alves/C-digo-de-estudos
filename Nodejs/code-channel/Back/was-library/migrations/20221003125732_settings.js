
exports.up = function (knex) {
    return knex.schema.createTable("settings", table => {
        table.increments("id").primary()
        table.integer("quatity_day")
        table.integer("quatity_book")
    })
};

exports.down = function (knex) {
    return knex.schema.dropTable("settings")
};
