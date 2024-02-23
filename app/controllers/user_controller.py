from ..database.db_session import get_db
from ..models.user import User, UpdateUser
from passlib.context import CryptContext

# Global variables
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

db = get_db()

SELECT_USER_QUERY = """
    SELECT
        u.user_id,
        u.username,
        u.email,
        u.password,
        u.disabled,
        array_agg(r.role_name) AS roles
    FROM
        users u
    JOIN
        user_roles ur ON u.user_id = ur.user_id
    JOIN
        roles r ON ur.role_id = r.role_id
    WHERE
        FILTER
    GROUP BY
        u.user_id, u.username, u.email;
    """
    
USERNAME_FILTER = """
        u.username = $1
    """
    
EMAIL_FILTER = """
        u.email = $1
    """
    
USER_ID_FILTER = """
        u.user_id = $1
    """
    
SEARCH_FILTER = """
        u.username ILIKE $1
    """
    
NO_FILTER = """
        1 = 1
    """

# Difference between these two queries is 
# one is to be used with a filter and the other without
ORDER_BY_AND_LIMIT_NO_FILTER = """
    ORDER BY
        u.user_id
    LIMIT $1 OFFSET $2;
    """

ORDER_BY_AND_LIMIT_FILTER = """
    ORDER BY
        u.user_id
    LIMIT $2 OFFSET $3;
    """


# Function to create a new user in the database
async def create_user(user: User):
    query = """
    INSERT INTO users (username, email, password)
    VALUES ($1, $2, $3)
    RETURNING user_id;
    """
    user_id = await db.fetch_val(query, user.username, user.email, user.password)
    query = """
    INSERT INTO user_roles (user_id, role_id)
    VALUES ($1, $2);
    """
    role_ids = await get_role_ids(user.roles)
    for role in role_ids:
        await db.execute(query, user_id, role)
    return { "message": "User successfully created" }


# Function to get the user from the database using the username
async def find_user_by_username(username: str):
    query = SELECT_USER_QUERY
    query = query.replace("FILTER", USERNAME_FILTER)
    result = await db.fetch_row(query, username)
    if result is None:
        return None
    user_dict = dict(result)
    user = User(**user_dict)
    return user

# Function to get the user from the database using the email
async def find_user_by_email(email: str):
    query = SELECT_USER_QUERY
    query = query.replace("FILTER", EMAIL_FILTER)
    result = await db.fetch_row(query, email)
    if result is None:
        return None
    user_dict = dict(result)
    return user_dict

# Function to get the user from the database using the user_id
async def find_user_by_user_id(user_id: int):
    query = SELECT_USER_QUERY
    query = query.replace("FILTER", USER_ID_FILTER)
    result = await db.fetch_row(query, user_id)
    if result is None:
        return None
    user_dict = dict(result)
    # Remove password from the user_dict
    user_dict["password"] = ""
    return user_dict


# Function that returns the role ids of the roles passed in parameter
async def get_role_ids(roles: list[str]) -> list[int]:
    roles = "(" + ", ".join([f"'{role}'" for role in roles]) + ")"
    query = f"""
    SELECT
        ARRAY_AGG(role_id) as role_ids
    FROM
        roles
    WHERE
        role_name IN {roles};
    """
    role_ids = await db.fetch_val(query)
    return role_ids
    
    
# Ban user by user_id
async def ban_user_by_user_id(user_id: int):
    query = """
    UPDATE users SET disabled = true WHERE user_id = $1;
    """
    await db.execute(query, user_id)
    return { "message": "User successfully banned" }


# Get all users with pagination
async def get_all_users(page: int, limit: int):
    query = SELECT_USER_QUERY
    query = query.replace("FILTER", NO_FILTER)
    # Replace the ;
    query = query.replace(";", "")
    query += ORDER_BY_AND_LIMIT_NO_FILTER
    offset = (page - 1) * limit
    result = await db.fetch_rows(query, limit, offset)
    users = []
    for row in result:
        user_dict = dict(row)
        user_dict["password"] = ""
        users.append(user_dict)
    return users


# Function to delete all personal data
async def delete_data(user: User):
    query = """
    DELETE FROM users WHERE user_id = $1;
    """
    await db.execute(query, user.user_id)
    return { "message": "Data successfully deleted" }

# Function to update user info
async def update_user_info(user: User, new_info: UpdateUser):
    # Check if username already exists
    if new_info.username != user.username:
        user_exists = await find_user_by_username(new_info.username)
        if user_exists is not None:
            return { "message": "Username already exists" }
    # Check if email already exists
    if new_info.email != user.email:
        email_exists = await find_user_by_email(new_info.email)
        if email_exists is not None:
            return { "message": "Email already exists" }
    
    query = """
    UPDATE users
    SET
        username = $1,
        email = $2
    WHERE
        user_id = $3;
    """
    await db.execute(query, new_info.username, new_info.email, user.user_id)
    return { "message": "User info successfully updated" }

# Function to search for users by username with pagination
async def search_users(page: int, limit: int, username: str):
    query = SELECT_USER_QUERY
    query = query.replace("FILTER", SEARCH_FILTER)
    # Replace the ;
    query = query.replace(";", "")
    query += ORDER_BY_AND_LIMIT_FILTER
    offset = (page - 1) * limit
    result = await db.fetch_rows(query, f"%{username}%", limit, offset)
    users = []
    for row in result:
        user_dict = dict(row)
        user_dict["password"] = ""
        users.append(user_dict)
    return users


# Function to update user password
async def update_user_password(user_id: int, new_password: str):
    hashed_password = pwd_context.hash(new_password)
    query = """
    UPDATE users
    SET
        password = $1
    WHERE
        user_id = $2;
    """
    await db.execute(query, hashed_password, user_id)
    return { "message": "Password successfully updated" }