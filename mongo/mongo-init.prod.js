db.createUser(
    {
        user: "flaskuser",
        pwd: "flaskuserpassword",
        roles: [
            { role: "readWrite", db: "flaskdb_prod" }
        ]
    }
)
