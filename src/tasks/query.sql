SELECT good.name, category.name FROM good
LEFT JOIN category_has_good
    ON good.rowid = category_has_good.good_id
LEFT JOIN category
    ON category.rowid = category_has_good.category_id
ORDER BY
    good.name ASC,
    category.name ASC;
